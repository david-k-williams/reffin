#!/usr/bin/env python3
"""Standardize supported MCC sources into the repository's vendor CSV shape.

This command deliberately accepts local source files instead of downloading
them. That keeps source acquisition, terms review, and checksum recording an
explicit step.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


FIELDS = ("source_id", "vendor_key", "mcc", "name")

PYTHON_ISO18245_FILES = {
    "alipay": (
        "alipay_list.csv",
        "e00a80e10deb0f369c27be95d6bec9d2e9a4e181d414b11720c83e3347cbc89c",
    ),
    "american_express": (
        "amex_list.csv",
        "1b53f0d6132dccd72f7a15c24b2b03e4f36d392e7241bbfa677eaa4ba098a835",
    ),
    "iso18245": (
        "iso18245_official_list.csv",
        "a68627523c5ef122bcf1268746a8e70b77332ac4319004a38a3bf6934105095b",
    ),
    "mastercard": (
        "mastercard_list.csv",
        "2a5f865d9ab6ceb96d8db3f99c1e11e5b9d8e1bbf3dce17fb623dea032afac2d",
    ),
    "usda": (
        "usda_list.csv",
        "48f720a9d6da287f01db87d735c746baf870bbd2b3043a1cd91a0db8e81bcf25",
    ),
}

PYTHON_ISO18245_SOURCE_ID = "python_iso18245_3b53842"


def clean(value: str) -> str:
    return " ".join(value.replace("\u00a0", " ").split())


def write_rows(output: Path, rows: Iterable[dict[str, str]]) -> None:
    normalized = list(rows)
    seen_keys: set[str] = set()
    seen_mccs: set[str] = set()
    for row in normalized:
        key = row["vendor_key"]
        mcc = row["mcc"]
        if not key or key in seen_keys:
            raise ValueError(f"duplicate or empty vendor key: {key!r}")
        seen_keys.add(key)
        if mcc:
            if not re.fullmatch(r"\d{4}", mcc):
                raise ValueError(f"MCC must contain exactly four digits: {mcc!r}")
            if mcc in seen_mccs:
                raise ValueError(f"duplicate MCC: {mcc}")
            seen_mccs.add(mcc)
        if not row["name"]:
            raise ValueError(f"empty name for {key}")

    normalized.sort(key=lambda row: (row["mcc"] == "", row["mcc"], row["vendor_key"]))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(normalized)


def import_adyen(args: argparse.Namespace) -> None:
    with args.input.open(newline="", encoding="utf-8-sig") as stream:
        source_rows = csv.DictReader(stream)
        rows = []
        for source in source_rows:
            raw_mcc = clean(source["mcc"])
            mcc = raw_mcc.zfill(4) if raw_mcc.isdigit() else raw_mcc
            rows.append(
                {
                    "source_id": args.source_id,
                    "vendor_key": mcc,
                    "mcc": mcc,
                    "name": clean(source["description"]),
                }
            )
    write_rows(args.output, rows)


class StripeTableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_row = False
        self.in_cell = False
        self.in_code = False
        self.cells: list[tuple[str, str]] = []
        self.cell_text: list[str] = []
        self.code_text: list[str] = []
        self.rows: list[list[tuple[str, str]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        if tag == "tr":
            self.in_row = True
            self.cells = []
        elif tag in ("td", "th") and self.in_row:
            self.in_cell = True
            self.cell_text = []
            self.code_text = []
        elif tag == "code" and self.in_cell:
            self.in_code = True
        elif tag == "br" and self.in_cell:
            self.cell_text.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag == "code":
            self.in_code = False
        elif tag in ("td", "th") and self.in_cell:
            self.cells.append(("".join(self.cell_text).strip(), "".join(self.code_text).strip()))
            self.in_cell = False
        elif tag == "tr" and self.in_row:
            if self.cells:
                self.rows.append(self.cells)
            self.in_row = False

    def handle_data(self, data: str) -> None:
        if self.in_cell:
            self.cell_text.append(data)
            if self.in_code:
                self.code_text.append(data)


def humanize_key(key: str) -> str:
    return key.replace("_", " ").title()


def stripe_openapi_categories(path: Path) -> list[str]:
    document = json.loads(path.read_text(encoding="utf-8"))
    return document["components"]["schemas"]["issuing_card_authorization_controls"][
        "properties"
    ]["allowed_categories"]["items"]["enum"]


def import_stripe(args: argparse.Namespace) -> None:
    parser = StripeTableParser()
    parser.feed(args.html.read_text(encoding="utf-8"))
    by_key: dict[str, dict[str, str]] = {}
    for cells in parser.rows:
        if len(cells) != 2:
            continue
        mcc = clean(cells[1][0])
        key = clean(cells[0][1]).replace("\u200b", "")
        if not re.fullmatch(r"\d{4}", mcc) or not key:
            continue
        name = clean(cells[0][0].split("\n", 1)[0])
        by_key[key] = {
            "source_id": args.source_id,
            "vendor_key": key,
            "mcc": mcc,
            "name": name,
        }

    if args.openapi:
        for key in stripe_openapi_categories(args.openapi):
            by_key.setdefault(
                key,
                {
                    "source_id": args.source_id,
                    "vendor_key": key,
                    "mcc": "",
                    "name": humanize_key(key),
                },
            )
    write_rows(args.output, by_key.values())


def import_visa(args: argparse.Namespace) -> None:
    try:
        import pdfplumber  # type: ignore[import-not-found]
    except ImportError as error:
        raise SystemExit("Visa PDF extraction requires pdfplumber") from error

    rows = []
    with pdfplumber.open(args.pdf) as document:
        # The April 2026 manual's MCC listing runs from printed pages 27-110,
        # which are PDF pages 29-112. Restricting extraction avoids examples
        # and similar-MCC references elsewhere in the manual.
        for page_number in range(29, 113):
            page = document.pages[page_number - 1]
            for table in page.extract_tables():
                for cells in table:
                    for index, raw_cell in enumerate(cells):
                        cell = clean(str(raw_cell or ""))
                        if not re.fullmatch(r"\d{4}", cell):
                            continue
                        title = next(
                            (
                                clean(str(candidate))
                                for candidate in cells[index + 1 :]
                                if candidate and clean(str(candidate))
                            ),
                            "",
                        )
                        if title:
                            rows.append(
                                {
                                    "source_id": args.source_id,
                                    "vendor_key": cell,
                                    "mcc": cell,
                                    "name": title,
                                }
                            )
                        break
    write_rows(args.output, rows)


def import_python_iso18245(args: argparse.Namespace) -> None:
    """Import one pinned python-iso18245 list into the shared vendor shape."""
    filename, expected_sha256 = PYTHON_ISO18245_FILES[args.vendor]
    source = args.data_dir / filename
    if not source.is_file():
        raise SystemExit(f"missing python-iso18245 input: {source}")
    actual_sha256 = hashlib.sha256(source.read_bytes()).hexdigest()
    if actual_sha256 != expected_sha256:
        raise SystemExit(
            f"{filename} does not match python-iso18245 1.4.1; "
            f"expected {expected_sha256}, got {actual_sha256}"
        )

    by_mcc: dict[str, dict[str, str]] = {}
    with source.open(newline="", encoding="utf-8-sig") as stream:
        for source_row in csv.DictReader(stream):
            mcc = clean(source_row["MCC"])
            name = clean(source_row["DESCRIPTION"])
            if mcc in by_mcc:
                # USDA contains repeated MCC rows with narrower search labels.
                # Match the package API, which returns the first description.
                continue
            by_mcc[mcc] = {
                "source_id": PYTHON_ISO18245_SOURCE_ID,
                "vendor_key": mcc,
                "mcc": mcc,
                "name": name,
            }
    write_rows(args.output, by_mcc.values())


def import_all_python_iso18245(args: argparse.Namespace) -> None:
    for vendor in PYTHON_ISO18245_FILES:
        import_python_iso18245(
            argparse.Namespace(
                data_dir=args.data_dir,
                vendor=vendor,
                output=args.output_dir / f"{vendor}.csv",
            )
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    adyen = commands.add_parser("adyen", help="Import Adyen DABstep CSV")
    adyen.add_argument("--input", type=Path, required=True)
    adyen.add_argument("--output", type=Path, required=True)
    adyen.add_argument("--source-id", required=True)
    adyen.set_defaults(handler=import_adyen)

    stripe = commands.add_parser("stripe", help="Import Stripe docs table")
    stripe.add_argument("--html", type=Path, required=True)
    stripe.add_argument("--openapi", type=Path)
    stripe.add_argument("--output", type=Path, required=True)
    stripe.add_argument("--source-id", required=True)
    stripe.set_defaults(handler=import_stripe)

    visa = commands.add_parser("visa", help="Import Visa public manual")
    visa.add_argument("--pdf", type=Path, required=True)
    visa.add_argument("--output", type=Path, required=True)
    visa.add_argument("--source-id", required=True)
    visa.set_defaults(handler=import_visa)

    python_iso18245 = commands.add_parser(
        "python-iso18245",
        help="Import a pinned list from python-iso18245 1.4.1",
    )
    python_iso18245.add_argument("--data-dir", type=Path, required=True)
    python_iso18245.add_argument(
        "--vendor",
        choices=sorted(PYTHON_ISO18245_FILES),
        required=True,
    )
    python_iso18245.add_argument("--output", type=Path, required=True)
    python_iso18245.set_defaults(handler=import_python_iso18245)

    python_iso18245_all = commands.add_parser(
        "python-iso18245-all",
        help="Import all supported lists from pinned python-iso18245 1.4.1",
    )
    python_iso18245_all.add_argument("--data-dir", type=Path, required=True)
    python_iso18245_all.add_argument("--output-dir", type=Path, required=True)
    python_iso18245_all.set_defaults(handler=import_all_python_iso18245)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
