#!/usr/bin/env python3
"""Generate every Reffin offline reference-data artifact."""

from __future__ import annotations

import argparse
import importlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ("merchants", "cards", "currencies", "industries", "ach", "iso20022")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are stale")
    parser.add_argument(
        "domains",
        nargs="*",
        metavar="DOMAIN",
        help="Optional domains to generate; the default is every domain",
    )
    args = parser.parse_args()

    invalid_domains = sorted(set(args.domains) - set(DOMAINS))
    if invalid_domains:
        parser.error(
            f"invalid domain(s): {', '.join(invalid_domains)}; "
            f"choose from {', '.join(DOMAINS)}"
        )

    stale: list[Path] = []
    for domain in args.domains or DOMAINS:
        module = importlib.import_module(f"reffin_codegen.{domain}")
        stale.extend(module.generate(check=args.check))
    if stale:
        for path in stale:
            print(f"stale: {path.relative_to(ROOT)}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
