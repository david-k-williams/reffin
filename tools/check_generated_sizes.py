#!/usr/bin/env python3
"""Enforce generous source-size ceilings for generated Reffin catalogs."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LIMITS = {
    "packages/python/reffin_ach/src/reffin_ach/_generated.py": 65_000,
    "packages/python/reffin_cards/src/reffin_cards/_generated.py": 25_000,
    "packages/python/reffin_currencies/src/reffin_currencies/_generated.py": 60_000,
    "packages/python/reffin_industries/src/reffin_industries/_generated.py": 450_000,
    "packages/python/reffin_merchants/src/reffin_merchants/_generated.py": 800_000,
    "packages/typescript/reffin_ach/src/generated.ts": 90_000,
    "packages/typescript/reffin_cards/src/generated.ts": 30_000,
    "packages/typescript/reffin_currencies/src/generated.ts": 110_000,
    "packages/typescript/reffin_industries/src/generated.ts": 700_000,
    "packages/typescript/reffin_merchants/src/generated.ts": 760_000,
    "packages/flutter/reffin_ach/lib/src/generated.dart": 85_000,
    "packages/flutter/reffin_cards/lib/src/generated.dart": 25_000,
    "packages/flutter/reffin_currencies/lib/src/generated.dart": 45_000,
    "packages/flutter/reffin_industries/lib/src/generated.dart": 480_000,
    "packages/flutter/reffin_merchants/lib/src/generated.dart": 1_400_000,
}

# ISO 20022 is deliberately split into small generated source shards. Guard both
# the largest shard (to keep editors and compilers responsive) and the complete
# generated package footprint (to make catalog growth explicit during review).
DIRECTORY_LIMITS = {
    "packages/python/reffin_iso20022/src/reffin_iso20022": (75_000, 1_750_000),
    "packages/typescript/reffin_iso20022/src": (75_000, 1_900_000),
    "packages/flutter/reffin_iso20022/lib": (75_000, 1_800_000),
}


def main() -> None:
    failures: list[str] = []
    total = 0
    for relative_path, limit in LIMITS.items():
        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"missing: {relative_path}")
            continue
        size = path.stat().st_size
        total += size
        if size > limit:
            failures.append(f"too large: {relative_path} ({size:,} > {limit:,} bytes)")
    for relative_path, (file_limit, directory_limit) in DIRECTORY_LIMITS.items():
        path = ROOT / relative_path
        if not path.is_dir():
            failures.append(f"missing: {relative_path}")
            continue
        source_files = tuple(
            item
            for item in path.rglob("*")
            if item.is_file()
            and item.suffix in {".dart", ".py", ".ts"}
            and "__pycache__" not in item.parts
        )
        directory_size = sum(item.stat().st_size for item in source_files)
        total += directory_size
        if directory_size > directory_limit:
            failures.append(
                f"too large: {relative_path} "
                f"({directory_size:,} > {directory_limit:,} bytes total)"
            )
        for item in source_files:
            size = item.stat().st_size
            if size > file_limit:
                failures.append(
                    f"too large: {item.relative_to(ROOT)} "
                    f"({size:,} > {file_limit:,} bytes per file)"
                )
    if failures:
        print("\n".join(failures), file=sys.stderr)
        raise SystemExit(1)
    print(
        f"verified {len(LIMITS)} generated files and "
        f"{len(DIRECTORY_LIMITS)} sharded packages ({total:,} bytes)"
    )


if __name__ == "__main__":
    main()
