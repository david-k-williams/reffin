#!/usr/bin/env python3
"""Compare a local python-iso18245 data tree with this catalog.

The upstream repository is intentionally a non-shipping comparison oracle.
This script reads a user-supplied checkout and emits only counts and MCC-code
differences; it never copies vendor descriptions into the project.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PINNED_COMMIT = "3b53842ff48318ec01d8d9834ad90ec625e327bc"
PINNED_DATA_TREE = "b27c8fdd5a43f788238ca65afd391d509987878c"

UPSTREAM_CODE_LISTS = (
    "alipay_list.csv",
    "amex_list.csv",
    "iso18245_official_list.csv",
    "mastercard_list.csv",
    "stripe_list.csv",
    "usda_list.csv",
    "visa_list.csv",
)

PINNED_SHA256 = {
    "alipay_list.csv": "e00a80e10deb0f369c27be95d6bec9d2e9a4e181d414b11720c83e3347cbc89c",
    "amex_list.csv": "1b53f0d6132dccd72f7a15c24b2b03e4f36d392e7241bbfa677eaa4ba098a835",
    "iso18245_official_list.csv": "a68627523c5ef122bcf1268746a8e70b77332ac4319004a38a3bf6934105095b",
    "iso18245_ranges.csv": "77adc8824bdd426775c1730c59a527fef4cc0b45064339342c6a06632c0cd37e",
    "mastercard_list.csv": "2a5f865d9ab6ceb96d8db3f99c1e11e5b9d8e1bbf3dce17fb623dea032afac2d",
    "private_ranges.csv": "29705e945a302bcc40169e3864d05792116532f3fa826c19d5c97658233bf390",
    "stripe_list.csv": "60700a9420b2f49762c545f8c2196784e3e909d79c04ac09ee144c506717ba9e",
    "usda_list.csv": "48f720a9d6da287f01db87d735c746baf870bbd2b3043a1cd91a0db8e81bcf25",
    "visa_list.csv": "52650003376399236904b9086ce20ade37b9bc34fa97a31866caaf637ede0444",
}


def column(path: Path, name: str) -> list[str]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        return [row[name] for row in csv.DictReader(stream) if row.get(name)]


def local_mccs(vendor: str) -> set[str]:
    return set(column(ROOT / "data" / "merchants" / "vendors" / f"{vendor}.csv", "mcc"))


def comparison(upstream: set[str], current: set[str]) -> dict[str, object]:
    return {
        "upstream_unique_mccs": len(upstream),
        "current_unique_mccs": len(current),
        "current_only": sorted(current - upstream),
        "upstream_only": sorted(upstream - current),
    }


def audit(data_dir: Path) -> dict[str, object]:
    missing = [name for name in PINNED_SHA256 if not (data_dir / name).is_file()]
    if missing:
        raise SystemExit(f"not a python-iso18245 data directory; missing: {', '.join(missing)}")

    for name, expected in PINNED_SHA256.items():
        actual = hashlib.sha256((data_dir / name).read_bytes()).hexdigest()
        if actual != expected:
            raise SystemExit(
                f"{name} does not match python-iso18245 1.4.1; "
                f"expected {expected}, got {actual}"
            )

    summaries: dict[str, dict[str, int]] = {}
    upstream_sets: dict[str, set[str]] = {}
    union: set[str] = set()
    for name in UPSTREAM_CODE_LISTS:
        values = column(data_dir / name, "MCC")
        unique = set(values)
        upstream_sets[name] = unique
        union.update(unique)
        summaries[name] = {
            "rows": len(values),
            "unique_mccs": len(unique),
            "duplicate_rows": len(values) - len(unique),
        }

    iso_ranges = column(data_dir / "iso18245_ranges.csv", "MCC START")
    private_ranges = column(data_dir / "private_ranges.csv", "MCC START")
    return {
        "source": {
            "repository": "https://github.com/jleclanche/python-iso18245",
            "release": "1.4.1",
            "commit": PINNED_COMMIT,
            "data_tree": PINNED_DATA_TREE,
            "file_hashes_verified": True,
            "shipping_input": False,
        },
        "upstream_files": summaries,
        "mixed_source_union_unique_mccs": len(union),
        "iso_range_rows": len(iso_ranges),
        "private_range_rows": len(private_ranges),
        "comparisons": {
            "stripe": comparison(upstream_sets["stripe_list.csv"], local_mccs("stripe")),
            "visa": comparison(upstream_sets["visa_list.csv"], local_mccs("visa")),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data_dir", type=Path, help="Path to python-iso18245/iso18245/data")
    args = parser.parse_args()
    print(json.dumps(audit(args.data_dir), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
