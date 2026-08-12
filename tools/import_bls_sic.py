#!/usr/bin/env python3
"""Normalize the official BLS QCEW SIC table exported as browser-row JSON."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "industries" / "sic_1987.csv"
TITLE_PATTERN = re.compile(r"SIC (\d{2,4}) (.+)")
QCEW_ROLLUP_CODES = frozenset(
    {"0740", "0780", "1520", "1540", "4210", "5810", "6510", "7210"}
)


def normalize(rows: list[list[str]]) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    skipped_1972 = 0
    for index, row in enumerate(rows, start=1):
        if len(row) != 3:
            raise ValueError(f"row {index}: expected three columns")
        csv_code, qcew_code, title = row
        if csv_code != f"SIC_{qcew_code}" or not re.fullmatch(r"0[A-KZ]\d{0,4}", qcew_code):
            raise ValueError(f"row {index}: invalid BLS QCEW code")
        division = qcew_code[1]
        suffix = qcew_code[2:]
        if not suffix:
            code = division
            clean_title = title
            level = "division"
            parent = "" if division == "Z" else "Z"
        elif title.startswith("1972 SIC "):
            skipped_1972 += 1
            continue
        else:
            match = TITLE_PATTERN.fullmatch(title)
            if match is None or match.group(1) != suffix:
                raise ValueError(f"row {index}: title/code mismatch")
            code = suffix
            clean_title = match.group(2)
            level = (
                "qcew_rollup"
                if code in QCEW_ROLLUP_CODES
                else {2: "major_group", 3: "industry_group", 4: "industry"}[len(code)]
            )
            parent = division if len(code) == 2 else code[:-1]
        normalized.append(
            {
                "code": code,
                "title": clean_title,
                "level": level,
                "parent": parent,
                "division": division,
            }
        )

    if skipped_1972 != 225:
        raise ValueError(f"expected 225 rows prefixed 1972 SIC, found {skipped_1972}")
    if len(normalized) != 1_524:
        raise ValueError(f"expected 1,524 normalized rows, found {len(normalized)}")
    by_code = {row["code"]: row for row in normalized}
    if len(by_code) != len(normalized):
        raise ValueError("normalized SIC codes are not unique")
    level_counts: dict[str, int] = {}
    for row in normalized:
        level_counts[row["level"]] = level_counts.get(row["level"], 0) + 1
    if level_counts != {
        "division": 12,
        "major_group": 83,
        "industry_group": 416,
        "industry": 1_005,
        "qcew_rollup": 8,
    }:
        raise ValueError(f"unexpected SIC/QCEW level counts: {level_counts!r}")
    for row in normalized:
        if row["parent"] and row["parent"] not in by_code:
            raise ValueError(f"{row['code']}: missing parent {row['parent']}")
        if row["parent"] and row["parent"] != "Z":
            parent = by_code[row["parent"]]
            if parent["division"] != row["division"]:
                raise ValueError(f"{row['code']}: parent crosses QCEW division")
    return normalized


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON array exported from the BLS HTML table")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    rows = json.loads(args.input.read_text(encoding="utf-8"))
    normalized = normalize(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=("code", "title", "level", "parent", "division"),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(normalized)
    print(f"wrote {len(normalized)} BLS SIC rows to {args.output}")


if __name__ == "__main__":
    main()
