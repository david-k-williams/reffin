"""Generate Reffin Currencies for Python, TypeScript, and Flutter."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .common import ROOT, dart_identifier, dart_string, fingerprint, py_string, read_csv, ts_string, write_or_check


DATA_PATH = ROOT / "data" / "currencies" / "currencies.csv"
CLDR_VERSION = "48.2"


def _load() -> list[dict[str, str]]:
    rows = read_csv(DATA_PATH)
    required = (
        "alpha_code",
        "name",
        "minor_digits",
        "minor_rounding",
        "cash_digits",
        "cash_rounding",
        "active",
        "territories",
    )
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        code = row.get("alpha_code", "")
        if len(code) != 3 or not code.isascii() or not code.isalpha() or not code.isupper():
            raise ValueError(f"{DATA_PATH}:{index}: invalid currency code {code!r}")
        if code in seen:
            raise ValueError(f"{DATA_PATH}:{index}: duplicate currency code {code}")
        seen.add(code)
        if any(not row.get(field) for field in required):
            raise ValueError(f"{DATA_PATH}:{index}: missing required currency field")
        for field in ("minor_digits", "minor_rounding", "cash_digits", "cash_rounding"):
            if not row[field].isdigit():
                raise ValueError(f"{DATA_PATH}:{index}: {field} must be a nonnegative integer")
        if row["active"] not in {"true", "false"}:
            raise ValueError(f"{DATA_PATH}:{index}: invalid active flag")
    codes = [row["alpha_code"] for row in rows]
    if codes != sorted(codes):
        raise ValueError(f"{DATA_PATH}: rows must be sorted by alpha_code")
    return rows


def _python(rows: list[dict[str, str]], digest: str) -> str:
    lines = [
        '"""Generated offline currency reference data. Do not edit by hand."""',
        f"# Input SHA-256: {digest}",
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "from enum import Enum",
        "from typing import Final",
        "",
        f"DATA_FINGERPRINT: Final[str] = {py_string(digest)}",
        f"CLDR_VERSION: Final[str] = {py_string(CLDR_VERSION)}",
        "",
        "",
        "@dataclass(frozen=True, slots=True)",
        "class CurrencyInfo:",
        "    code: str",
        "    name: str",
        "    symbol: str | None",
        "    narrow_symbol: str | None",
        "    minor_digits: int",
        "    minor_rounding: int",
        "    cash_digits: int",
        "    cash_rounding: int",
        "    active: bool",
        "    territories: tuple[str, ...]",
        "",
        "    @property",
        "    def display_symbol(self) -> str:",
        "        return self.narrow_symbol or self.symbol or self.code",
        "",
        "",
        "class Currency(str, Enum):",
    ]
    lines.extend(f"    {row['alpha_code']} = {py_string(row['alpha_code'])}" for row in rows)
    lines.extend(
        [
            "",
            "    @classmethod",
            "    def try_parse(cls, code: str) -> Currency | None:",
            "        return _CURRENCY_BY_CODE.get(code.upper()) if isinstance(code, str) else None",
            "",
            "    @property",
            "    def info(self) -> CurrencyInfo:",
            "        return _INFO_BY_CURRENCY[self]",
            "",
            "    @property",
            "    def display_symbol(self) -> str:",
            "        return self.info.display_symbol",
            "",
            "",
            "_INFO_BY_CURRENCY: Final[dict[Currency, CurrencyInfo]] = {",
        ]
    )
    for row in rows:
        symbol = py_string(row["symbol"]) if row["symbol"] else "None"
        narrow = py_string(row["narrow_symbol"]) if row["narrow_symbol"] else "None"
        territories = tuple(item for item in row["territories"].split(";") if item)
        lines.append(
            f"    Currency.{row['alpha_code']}: CurrencyInfo({py_string(row['alpha_code'])}, "
            f"{py_string(row['name'])}, {symbol}, {narrow}, {row['minor_digits']}, "
            f"{row['minor_rounding']}, {row['cash_digits']}, {row['cash_rounding']}, "
            f"{row['active'].title()}, {territories!r}),"
        )
    lines.extend(
        [
            "}",
            "_CURRENCY_BY_CODE: Final = {currency.value: currency for currency in Currency}",
            "ALL_CURRENCIES: Final[tuple[CurrencyInfo, ...]] = tuple(item.info for item in Currency)",
            "",
            "",
            "def resolve_currency(code: str | Currency) -> CurrencyInfo | None:",
            "    currency = code if isinstance(code, Currency) else Currency.try_parse(code)",
            "    return currency.info if currency is not None else None",
        ]
    )
    return "\n".join(lines)


def _typescript(rows: list[dict[str, str]], digest: str) -> str:
    lines = [
        "// Generated offline currency reference data. Do not edit by hand.",
        f"// Input SHA-256: {digest}",
        f"export const DATA_FINGERPRINT = {ts_string(digest)};",
        f"export const CLDR_VERSION = {ts_string(CLDR_VERSION)};",
        "",
        "export const Currency = Object.freeze({",
    ]
    lines.extend(f"  {row['alpha_code']}: {ts_string(row['alpha_code'])}," for row in rows)
    lines.extend(
        [
            "} as const);",
            "export type Currency = (typeof Currency)[keyof typeof Currency];",
            "",
            "export interface CurrencyInfo {",
            "  readonly code: Currency;",
            "  readonly name: string;",
            "  readonly symbol: string | null;",
            "  readonly narrowSymbol: string | null;",
            "  readonly displaySymbol: string;",
            "  readonly minorDigits: number;",
            "  readonly minorRounding: number;",
            "  readonly cashDigits: number;",
            "  readonly cashRounding: number;",
            "  readonly active: boolean;",
            "  readonly territories: readonly string[];",
            "}",
            "",
            "export const currencies: readonly CurrencyInfo[] = Object.freeze([",
        ]
    )
    for row in rows:
        symbol = ts_string(row["symbol"]) if row["symbol"] else "null"
        narrow = ts_string(row["narrow_symbol"]) if row["narrow_symbol"] else "null"
        territories = [item for item in row["territories"].split(";") if item]
        display = row["narrow_symbol"] or row["symbol"] or row["alpha_code"]
        lines.append(
            "  Object.freeze({ "
            f"code: Currency.{row['alpha_code']}, name: {ts_string(row['name'])}, symbol: {symbol}, "
            f"narrowSymbol: {narrow}, displaySymbol: {ts_string(display)}, minorDigits: {row['minor_digits']}, "
            f"minorRounding: {row['minor_rounding']}, cashDigits: {row['cash_digits']}, "
            f"cashRounding: {row['cash_rounding']}, active: {row['active']}, "
            f"territories: Object.freeze({ts_string(territories)}) "
            "}),"
        )
    lines.extend(
        [
            "]);",
            "const byCode = new Map(currencies.map((item) => [item.code, item]));",
            "",
            "export function isCurrency(code: string): code is Currency {",
            "  return byCode.has(code as Currency);",
            "}",
            "",
            "export function tryParseCurrency(code: string): Currency | undefined {",
            "  const normalized = code.toUpperCase();",
            "  return byCode.has(normalized as Currency) ? (normalized as Currency) : undefined;",
            "}",
            "",
            "export function resolveCurrency(code: string): CurrencyInfo | undefined {",
            "  return byCode.get(code.toUpperCase() as Currency);",
            "}",
        ]
    )
    return "\n".join(lines)


def _dart(rows: list[dict[str, str]], digest: str) -> str:
    lines = [
        "// Generated offline currency reference data. Do not edit by hand.",
        f"// Input SHA-256: {digest}",
        f"const String dataFingerprint = {dart_string(digest)};",
        f"const String cldrVersion = {dart_string(CLDR_VERSION)};",
        "",
        "enum Currency {",
    ]
    for index, row in enumerate(rows):
        suffix = ";" if index == len(rows) - 1 else ","
        symbol = dart_string(row["symbol"]) if row["symbol"] else "null"
        narrow = dart_string(row["narrow_symbol"]) if row["narrow_symbol"] else "null"
        territories = [item for item in row["territories"].split(";") if item]
        territory_literal = "<String>[" + ", ".join(dart_string(item) for item in territories) + "]"
        lines.append(
            f"  {dart_identifier(row['alpha_code'].lower())}({dart_string(row['alpha_code'])}, {dart_string(row['name'])}, "
            f"{symbol}, {narrow}, {row['minor_digits']}, {row['minor_rounding']}, "
            f"{row['cash_digits']}, {row['cash_rounding']}, {row['active']}, {territory_literal}){suffix}"
        )
    lines.extend(
        [
            "",
            "  const Currency(",
            "    this.code, this.label, this.symbol, this.narrowSymbol, this.minorDigits,",
            "    this.minorRounding, this.cashDigits, this.cashRounding, this.isActive, this.territories,",
            "  );",
            "  final String code;",
            "  final String label;",
            "  final String? symbol;",
            "  final String? narrowSymbol;",
            "  final int minorDigits;",
            "  final int minorRounding;",
            "  final int cashDigits;",
            "  final int cashRounding;",
            "  final bool isActive;",
            "  final List<String> territories;",
            "  String get displaySymbol => narrowSymbol ?? symbol ?? code;",
            "",
            "  static Currency? tryParse(String code) => _byCode[code.toUpperCase()];",
            "}",
            "",
            "final Map<String, Currency> _byCode = {for (final item in Currency.values) item.code: item};",
            "Currency? resolveCurrency(String code) => Currency.tryParse(code);",
        ]
    )
    return "\n".join(lines)


def generate(check: bool = False) -> list[Path]:
    rows = _load()
    digest = fingerprint((DATA_PATH,))
    outputs = {
        ROOT / "packages" / "python" / "reffin_currencies" / "src" / "reffin_currencies" / "_generated.py": _python(rows, digest),
        ROOT / "packages" / "typescript" / "reffin_currencies" / "src" / "generated.ts": _typescript(rows, digest),
        ROOT / "packages" / "flutter" / "reffin_currencies" / "lib" / "src" / "generated.dart": _dart(rows, digest),
    }
    stale = [path for path, content in outputs.items() if not write_or_check(path, content, check)]
    print(f"{'verified' if check else 'generated'} {len(rows)} currencies")
    return stale


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = generate(check=args.check)
    if stale:
        for path in stale:
            print(f"stale: {path.relative_to(ROOT)}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
