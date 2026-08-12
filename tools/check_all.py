#!/usr/bin/env python3
"""Run the complete local Reffin verification matrix."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ("merchants", "cards", "currencies", "industries", "ach", "iso20022")


def run(command: list[str], *, cwd: Path = ROOT, env: dict[str, str] | None = None) -> None:
    print(f"\n[{cwd.relative_to(ROOT) or '.'}] {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=cwd, env=env, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-typescript", action="store_true")
    parser.add_argument("--skip-flutter", action="store_true")
    args = parser.parse_args()

    run([sys.executable, "-B", "tools/generate.py", "--check"])
    run([sys.executable, "-B", "tools/check_generated_sizes.py"])

    for domain in DOMAINS:
        package = ROOT / "packages" / "python" / f"reffin_{domain}"
        env = os.environ.copy()
        env["PYTHONPATH"] = str(package / "src")
        run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(package / "tests"), "-v"],
            env=env,
        )

    if not args.skip_typescript:
        run(["npm", "--workspaces", "--if-present", "test"])

    if not args.skip_flutter:
        for domain in DOMAINS:
            package = ROOT / "packages" / "flutter" / f"reffin_{domain}"
            run(["flutter", "test", "--no-pub"], cwd=package)
            run(["flutter", "analyze", "--no-pub"], cwd=package)


if __name__ == "__main__":
    main()
