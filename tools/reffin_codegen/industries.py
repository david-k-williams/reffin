"""Generate Reffin Industries for Python, TypeScript, and Flutter."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from .common import (
    ROOT,
    SNAKE_CASE,
    camel,
    dart_string,
    fingerprint,
    pascal,
    py_string,
    read_csv,
    ts_string,
    write_or_check,
)


NAICS_PATH = ROOT / "data" / "industries" / "naics_2022.csv"
NAICS_SECTORS_PATH = ROOT / "data" / "industries" / "sectors.csv"
SIC_PATH = ROOT / "data" / "industries" / "sic_1987.csv"
SIC_DIVISIONS_PATH = ROOT / "data" / "industries" / "sic_divisions.csv"

NAICS_CODE_PATTERN = re.compile(r"(?:\d{2}|\d{2}-\d{2}|\d{3,6})")
SIC_CODE_PATTERN = re.compile(r"(?:[A-KZ]|\d{2,4})")
SIC_LEVEL_PATTERNS = {
    "division": re.compile(r"[A-KZ]"),
    "major_group": re.compile(r"\d{2}"),
    "industry_group": re.compile(r"\d{3}"),
    "industry": re.compile(r"\d{4}"),
    "qcew_rollup": re.compile(r"\d{4}"),
}
SIC_QCEW_ROLLUP_CODES = frozenset(
    {"0740", "0780", "1520", "1540", "4210", "5810", "6510", "7210"}
)

# These names are verified native members of Flutter's Material Icons catalog.
SUPPORTED_FLUTTER_ICONS = {
    "account_balance",
    "agriculture",
    "apartment",
    "attractions",
    "bolt",
    "build",
    "business_center",
    "category",
    "construction",
    "corporate_fare",
    "factory",
    "help_outline",
    "language",
    "local_shipping",
    "medical_services",
    "restaurant",
    "school",
    "storefront",
    "terrain",
    "warehouse",
    "work",
}


def _validate_columns(path: Path, rows: list[dict[str, str]], expected: set[str]) -> None:
    if not rows:
        raise ValueError(f"{path}: no data rows")
    actual = set(rows[0])
    if actual != expected:
        raise ValueError(f"{path}: expected columns {sorted(expected)!r}, got {sorted(actual)!r}")


def _load_naics() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows = read_csv(NAICS_PATH)
    _validate_columns(
        NAICS_PATH,
        rows,
        {"code", "title", "level", "parent", "sector"},
    )
    by_code: dict[str, dict[str, str]] = {}
    for index, row in enumerate(rows, start=2):
        code = row.get("code", "")
        if not NAICS_CODE_PATTERN.fullmatch(code):
            raise ValueError(f"{NAICS_PATH}:{index}: invalid NAICS code {code!r}")
        if code in by_code:
            raise ValueError(f"{NAICS_PATH}:{index}: duplicate NAICS code {code}")
        if not row.get("title") or row.get("level") not in {"2", "3", "4", "5", "6"}:
            raise ValueError(f"{NAICS_PATH}:{index}: invalid title or level")
        if not NAICS_CODE_PATTERN.fullmatch(row.get("sector", "")):
            raise ValueError(f"{NAICS_PATH}:{index}: invalid sector")
        by_code[code] = row

    sector_codes = {row["code"] for row in rows if row["level"] == "2"}
    for code, row in by_code.items():
        parent = row.get("parent", "")
        if row["level"] == "2":
            if parent:
                raise ValueError(f"{NAICS_PATH}: sector {code} cannot have a parent")
        elif parent not in by_code:
            raise ValueError(f"{NAICS_PATH}: {code} has unknown parent {parent}")
        if row["sector"] not in sector_codes:
            raise ValueError(f"{NAICS_PATH}: {code} has unknown sector {row['sector']}")

    sectors = read_csv(NAICS_SECTORS_PATH)
    _validate_columns(
        NAICS_SECTORS_PATH,
        sectors,
        {"sector_id", "sector_code", "name", "material_symbol", "description"},
    )
    seen_ids: set[str] = set()
    seen_codes: set[str] = set()
    for index, sector in enumerate(sectors, start=2):
        sector_id = sector.get("sector_id", "")
        code = sector.get("sector_code", "")
        symbol = sector.get("material_symbol", "")
        if not SNAKE_CASE.fullmatch(sector_id):
            raise ValueError(f"{NAICS_SECTORS_PATH}:{index}: invalid sector_id {sector_id!r}")
        if sector_id in seen_ids or code in seen_codes:
            raise ValueError(f"{NAICS_SECTORS_PATH}:{index}: duplicate sector ID or code")
        if code not in sector_codes:
            raise ValueError(f"{NAICS_SECTORS_PATH}:{index}: unknown sector code {code!r}")
        if not sector.get("name") or not sector.get("description"):
            raise ValueError(f"{NAICS_SECTORS_PATH}:{index}: empty presentation field")
        if symbol not in SUPPORTED_FLUTTER_ICONS:
            raise ValueError(f"{NAICS_SECTORS_PATH}:{index}: unsupported Flutter icon {symbol!r}")
        source_title = by_code[code]["title"]
        if sector["name"] != source_title:
            raise ValueError(
                f"{NAICS_SECTORS_PATH}:{index}: name does not match NAICS title "
                f"{source_title!r}"
            )
        seen_ids.add(sector_id)
        seen_codes.add(code)
    if [row["sector_id"] for row in sectors] != sorted(seen_ids):
        raise ValueError(f"{NAICS_SECTORS_PATH}: rows must be sorted by sector_id")
    if seen_codes != sector_codes:
        raise ValueError(f"{NAICS_SECTORS_PATH}: metadata must cover every sector")
    return rows, sectors


def _load_sic() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows = read_csv(SIC_PATH)
    _validate_columns(
        SIC_PATH,
        rows,
        {"code", "title", "level", "parent", "division"},
    )
    by_code: dict[str, dict[str, str]] = {}
    for index, row in enumerate(rows, start=2):
        code = row.get("code", "")
        level = row.get("level", "")
        if not SIC_CODE_PATTERN.fullmatch(code):
            raise ValueError(f"{SIC_PATH}:{index}: invalid SIC code {code!r}")
        if level not in SIC_LEVEL_PATTERNS or not SIC_LEVEL_PATTERNS[level].fullmatch(code):
            raise ValueError(f"{SIC_PATH}:{index}: code {code!r} does not match level {level!r}")
        if code in by_code:
            raise ValueError(f"{SIC_PATH}:{index}: duplicate SIC code {code}")
        if not row.get("title"):
            raise ValueError(f"{SIC_PATH}:{index}: title is required")
        if not re.fullmatch(r"[A-KZ]", row.get("division", "")):
            raise ValueError(f"{SIC_PATH}:{index}: invalid division {row.get('division')!r}")
        by_code[code] = row

    division_codes = {row["code"] for row in rows if row["level"] == "division"}
    if division_codes != set("ABCDEFGHIJKZ"):
        raise ValueError(f"{SIC_PATH}: expected divisions A-K and Z")
    qcew_rollup_codes = {
        row["code"] for row in rows if row["level"] == "qcew_rollup"
    }
    if qcew_rollup_codes != SIC_QCEW_ROLLUP_CODES:
        raise ValueError(
            f"{SIC_PATH}: expected QCEW rollups {sorted(SIC_QCEW_ROLLUP_CODES)!r}, "
            f"got {sorted(qcew_rollup_codes)!r}"
        )
    for code, row in by_code.items():
        parent = row.get("parent", "")
        if code == "Z":
            if parent:
                raise ValueError(f"{SIC_PATH}: root Z cannot have a parent")
        elif parent not in by_code:
            raise ValueError(f"{SIC_PATH}: {code} has unknown parent {parent}")
        if row["division"] not in division_codes:
            raise ValueError(f"{SIC_PATH}: {code} has unknown division {row['division']}")
        if row["level"] == "division":
            expected_parent = "" if code == "Z" else "Z"
            if parent != expected_parent or row["division"] != code:
                raise ValueError(f"{SIC_PATH}: invalid division hierarchy for {code}")
        else:
            parent_row = by_code[parent]
            if parent_row["division"] != row["division"]:
                raise ValueError(f"{SIC_PATH}: {code} crosses division hierarchy")

    divisions = read_csv(SIC_DIVISIONS_PATH)
    _validate_columns(
        SIC_DIVISIONS_PATH,
        divisions,
        {"division_id", "division_code", "name", "material_symbol", "description"},
    )
    seen_ids: set[str] = set()
    seen_codes: set[str] = set()
    for index, division in enumerate(divisions, start=2):
        division_id = division.get("division_id", "")
        code = division.get("division_code", "")
        symbol = division.get("material_symbol", "")
        if not SNAKE_CASE.fullmatch(division_id):
            raise ValueError(f"{SIC_DIVISIONS_PATH}:{index}: invalid division_id {division_id!r}")
        if division_id in seen_ids or code in seen_codes:
            raise ValueError(f"{SIC_DIVISIONS_PATH}:{index}: duplicate division ID or code")
        if code not in division_codes:
            raise ValueError(f"{SIC_DIVISIONS_PATH}:{index}: unknown division code {code!r}")
        if not division.get("name") or not division.get("description"):
            raise ValueError(f"{SIC_DIVISIONS_PATH}:{index}: empty presentation field")
        if symbol not in SUPPORTED_FLUTTER_ICONS:
            raise ValueError(f"{SIC_DIVISIONS_PATH}:{index}: unsupported Flutter icon {symbol!r}")
        source_title = by_code[code]["title"]
        if division["name"] != source_title:
            raise ValueError(
                f"{SIC_DIVISIONS_PATH}:{index}: name does not match SIC title "
                f"{source_title!r}"
            )
        seen_ids.add(division_id)
        seen_codes.add(code)
    if [row["division_id"] for row in divisions] != sorted(seen_ids):
        raise ValueError(f"{SIC_DIVISIONS_PATH}: rows must be sorted by division_id")
    if seen_codes != division_codes:
        raise ValueError(f"{SIC_DIVISIONS_PATH}: metadata must cover every division")
    return rows, divisions


def _python(
    naics_rows: list[dict[str, str]],
    sectors: list[dict[str, str]],
    sic_rows: list[dict[str, str]],
    divisions: list[dict[str, str]],
    digest: str,
) -> str:
    lines = [
        '"""Generated offline NAICS 2022 and SIC 1987 reference data."""',
        f"# Input SHA-256: {digest}",
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "from enum import Enum",
        "from typing import Final",
        "",
        f"DATA_FINGERPRINT: Final[str] = {py_string(digest)}",
        "NAICS_VERSION: Final[str] = '2022'",
        "SIC_VERSION: Final[str] = '1987'",
        f"NAICS_INDUSTRY_COUNT: Final[int] = {len(naics_rows)}",
        f"SIC_INDUSTRY_COUNT: Final[int] = {len(sic_rows)}",
        "",
        "",
        "class IndustryLevel(int, Enum):",
        "    SECTOR = 2",
        "    SUBSECTOR = 3",
        "    INDUSTRY_GROUP = 4",
        "    NAICS_INDUSTRY = 5",
        "    NATIONAL_INDUSTRY = 6",
        "",
        "",
        "class IndustrySector(str, Enum):",
    ]
    for sector in sectors:
        lines.append(
            f"    {sector['sector_id'].upper()} = ({py_string(sector['sector_id'])}, "
            f"{py_string(sector['sector_code'])}, {py_string(sector['name'])}, "
            f"{py_string(sector['material_symbol'])}, {py_string(sector['description'])})"
        )
    lines.extend(
        [
            "",
            "    def __new__(",
            "        cls, value: str, code: str, label: str, material_symbol: str, description: str",
            "    ) -> IndustrySector:",
            "        member = str.__new__(cls, value)",
            "        member._value_ = value",
            "        member.code = code",
            "        member.label = label",
            "        member.material_symbol = material_symbol",
            "        member.description = description",
            "        return member",
            "",
            "    code: str",
            "    label: str",
            "    material_symbol: str",
            "    description: str",
            "",
            "    @classmethod",
            "    def try_parse(cls, value: str) -> IndustrySector | None:",
            "        return _NAICS_SECTOR_BY_ID.get(value)",
            "",
            "    @classmethod",
            "    def from_code(cls, code: str) -> IndustrySector | None:",
            "        return _NAICS_SECTOR_BY_CODE.get(code)",
            "",
            "",
            "@dataclass(frozen=True, slots=True)",
            "class Industry:",
            "    code: str",
            "    title: str",
            "    level: IndustryLevel",
            "    parent_code: str | None",
            "    sector_code: str",
            "",
            "    @property",
            "    def parent(self) -> Industry | None:",
            "        return resolve_industry(self.parent_code) if self.parent_code else None",
            "",
            "    @property",
            "    def sector(self) -> IndustrySector:",
            "        return _NAICS_SECTOR_BY_CODE[self.sector_code]",
            "",
            "    @property",
            "    def sector_entry(self) -> Industry:",
            "        return _NAICS_BY_CODE[self.sector_code]",
            "",
            "    @property",
            "    def children(self) -> tuple[Industry, ...]:",
            "        return _NAICS_CHILDREN.get(self.code, ())",
            "",
            "",
            "_INDUSTRIES: Final[tuple[Industry, ...]] = (",
        ]
    )
    for row in naics_rows:
        parent = py_string(row["parent"]) if row["parent"] else "None"
        lines.append(
            f"    Industry({py_string(row['code'])}, {py_string(row['title'])}, "
            f"IndustryLevel({row['level']}), {parent}, {py_string(row['sector'])}),"
        )
    lines.extend(
        [
            ")",
            "_NAICS_BY_CODE: Final = {item.code: item for item in _INDUSTRIES}",
            "_NAICS_SECTOR_BY_ID: Final = {item.value: item for item in IndustrySector}",
            "_NAICS_SECTOR_BY_CODE: Final = {item.code: item for item in IndustrySector}",
            "_NAICS_CHILD_LISTS: dict[str, list[Industry]] = {}",
            "for _naics_item in _INDUSTRIES:",
            "    if _naics_item.parent_code is not None:",
            "        _NAICS_CHILD_LISTS.setdefault(_naics_item.parent_code, []).append(_naics_item)",
            "_NAICS_CHILDREN: Final = {",
            "    code: tuple(items) for code, items in _NAICS_CHILD_LISTS.items()",
            "}",
            "del _NAICS_CHILD_LISTS, _naics_item",
            "ALL_INDUSTRIES: Final = _INDUSTRIES",
            "SECTORS: Final = tuple(IndustrySector)",
            "SECTOR_ENTRIES: Final = tuple(",
            "    item for item in _INDUSTRIES if item.level is IndustryLevel.SECTOR",
            ")",
            "",
            "",
            "def resolve_industry(code: str | None) -> Industry | None:",
            "    return _NAICS_BY_CODE.get(code) if isinstance(code, str) else None",
            "",
            "",
            "def children_of(code: str) -> tuple[Industry, ...]:",
            "    return _NAICS_CHILDREN.get(code, ())",
            "",
            "",
            "class SicLevel(str, Enum):",
            "    DIVISION = ('division', 1)",
            "    MAJOR_GROUP = ('major_group', 2)",
            "    INDUSTRY_GROUP = ('industry_group', 3)",
            "    INDUSTRY = ('industry', 4)",
            "    QCEW_ROLLUP = ('qcew_rollup', 4)",
            "",
            "    def __new__(cls, value: str, depth: int) -> SicLevel:",
            "        member = str.__new__(cls, value)",
            "        member._value_ = value",
            "        member.depth = depth",
            "        return member",
            "",
            "    depth: int",
            "",
            "",
            "class SicDivision(str, Enum):",
        ]
    )
    for division in divisions:
        lines.append(
            f"    {division['division_id'].upper()} = ({py_string(division['division_id'])}, "
            f"{py_string(division['division_code'])}, {py_string(division['name'])}, "
            f"{py_string(division['material_symbol'])}, {py_string(division['description'])})"
        )
    lines.extend(
        [
            "",
            "    def __new__(",
            "        cls, value: str, code: str, label: str, material_symbol: str, description: str",
            "    ) -> SicDivision:",
            "        member = str.__new__(cls, value)",
            "        member._value_ = value",
            "        member.code = code",
            "        member.label = label",
            "        member.material_symbol = material_symbol",
            "        member.description = description",
            "        return member",
            "",
            "    code: str",
            "    label: str",
            "    material_symbol: str",
            "    description: str",
            "",
            "    @classmethod",
            "    def try_parse(cls, value: str) -> SicDivision | None:",
            "        return _SIC_DIVISION_BY_ID.get(value)",
            "",
            "    @classmethod",
            "    def from_code(cls, code: str) -> SicDivision | None:",
            "        return _SIC_DIVISION_BY_CODE.get(code)",
            "",
            "",
            "@dataclass(frozen=True, slots=True)",
            "class SicIndustry:",
            "    code: str",
            "    title: str",
            "    level: SicLevel",
            "    parent_code: str | None",
            "    division_code: str",
            "",
            "    @property",
            "    def parent(self) -> SicIndustry | None:",
            "        return resolve_sic(self.parent_code) if self.parent_code else None",
            "",
            "    @property",
            "    def division(self) -> SicDivision:",
            "        return _SIC_DIVISION_BY_CODE[self.division_code]",
            "",
            "    @property",
            "    def division_entry(self) -> SicIndustry:",
            "        return _SIC_BY_CODE[self.division_code]",
            "",
            "    @property",
            "    def children(self) -> tuple[SicIndustry, ...]:",
            "        return _SIC_CHILDREN.get(self.code, ())",
            "",
            "    @property",
            "    def material_symbol(self) -> str:",
            "        return self.division.material_symbol",
            "",
            "",
            "_SIC_INDUSTRIES: Final[tuple[SicIndustry, ...]] = (",
        ]
    )
    for row in sic_rows:
        parent = py_string(row["parent"]) if row["parent"] else "None"
        lines.append(
            f"    SicIndustry({py_string(row['code'])}, {py_string(row['title'])}, "
            f"SicLevel.{row['level'].upper()}, {parent}, {py_string(row['division'])}),"
        )
    lines.extend(
        [
            ")",
            "_SIC_BY_CODE: Final = {item.code: item for item in _SIC_INDUSTRIES}",
            "_SIC_DIVISION_BY_ID: Final = {item.value: item for item in SicDivision}",
            "_SIC_DIVISION_BY_CODE: Final = {item.code: item for item in SicDivision}",
            "_SIC_CHILD_LISTS: dict[str, list[SicIndustry]] = {}",
            "for _sic_item in _SIC_INDUSTRIES:",
            "    if _sic_item.parent_code is not None:",
            "        _SIC_CHILD_LISTS.setdefault(_sic_item.parent_code, []).append(_sic_item)",
            "_SIC_CHILDREN: Final = {",
            "    code: tuple(items) for code, items in _SIC_CHILD_LISTS.items()",
            "}",
            "del _SIC_CHILD_LISTS, _sic_item",
            "ALL_SIC_INDUSTRIES: Final = _SIC_INDUSTRIES",
            "SIC_DIVISIONS: Final = tuple(SicDivision)",
            "SIC_DIVISION_ENTRIES: Final = tuple(",
            "    item for item in _SIC_INDUSTRIES if item.level is SicLevel.DIVISION",
            ")",
            "",
            "",
            "def resolve_sic(code: str | None) -> SicIndustry | None:",
            "    return _SIC_BY_CODE.get(code) if isinstance(code, str) else None",
            "",
            "",
            "def sic_children_of(code: str) -> tuple[SicIndustry, ...]:",
            "    return _SIC_CHILDREN.get(code, ())",
            "",
            "",
            "NaicsIndustry = Industry",
            "NaicsLevel = IndustryLevel",
            "NaicsSector = IndustrySector",
            "ALL_NAICS_INDUSTRIES: Final = ALL_INDUSTRIES",
            "resolve_naics = resolve_industry",
            "naics_children_of = children_of",
        ]
    )
    return "\n".join(lines)


def _typescript(
    naics_rows: list[dict[str, str]],
    sectors: list[dict[str, str]],
    sic_rows: list[dict[str, str]],
    divisions: list[dict[str, str]],
    digest: str,
) -> str:
    naics_level_names = {
        "2": "Sector",
        "3": "Subsector",
        "4": "IndustryGroup",
        "5": "NaicsIndustry",
        "6": "NationalIndustry",
    }
    sic_level_names = {
        "division": "Division",
        "major_group": "MajorGroup",
        "industry_group": "IndustryGroup",
        "industry": "Industry",
        "qcew_rollup": "QcewRollup",
    }
    lines = [
        "// Generated offline NAICS 2022 and SIC 1987 reference data.",
        f"// Input SHA-256: {digest}",
        f"export const DATA_FINGERPRINT = {ts_string(digest)};",
        'export const NAICS_VERSION = "2022";',
        'export const SIC_VERSION = "1987";',
        f"export const naicsIndustryCount = {len(naics_rows)};",
        f"export const sicIndustryCount = {len(sic_rows)};",
        "",
        "export const IndustryLevel = Object.freeze({",
        "  Sector: 2, Subsector: 3, IndustryGroup: 4, NaicsIndustry: 5, NationalIndustry: 6,",
        "} as const);",
        "export type IndustryLevel = (typeof IndustryLevel)[keyof typeof IndustryLevel];",
        "",
        "export interface IndustrySectorValue {",
        "  readonly id: string;",
        "  readonly code: string;",
        "  readonly name: string;",
        "  readonly materialSymbol: string;",
        "  readonly description: string;",
        "}",
        "",
        "export const IndustrySector = Object.freeze({",
    ]
    for sector in sectors:
        lines.append(
            f"  {pascal(sector['sector_id'])}: Object.freeze({{ "
            f"id: {ts_string(sector['sector_id'])}, code: {ts_string(sector['sector_code'])}, "
            f"name: {ts_string(sector['name'])}, "
            f"materialSymbol: {ts_string(sector['material_symbol'])}, "
            f"description: {ts_string(sector['description'])} }}),"
        )
    lines.extend(
        [
            "} as const);",
            "export type IndustrySector = (typeof IndustrySector)[keyof typeof IndustrySector];",
            "export const industrySectors: readonly IndustrySector[] = Object.freeze(",
            "  Object.values(IndustrySector),",
            ");",
            "",
            "export interface Industry {",
            "  readonly code: string;",
            "  readonly title: string;",
            "  readonly level: IndustryLevel;",
            "  readonly parentCode: string | null;",
            "  readonly sectorCode: string;",
            "}",
            "",
            "function industry(item: Industry): Industry { return Object.freeze(item); }",
            "",
            "export const industries: readonly Industry[] = Object.freeze([",
        ]
    )
    for row in naics_rows:
        parent = ts_string(row["parent"]) if row["parent"] else "null"
        lines.append(
            f"  industry({{ code: {ts_string(row['code'])}, title: {ts_string(row['title'])}, "
            f"level: IndustryLevel.{naics_level_names[row['level']]}, parentCode: {parent}, "
            f"sectorCode: {ts_string(row['sector'])} }}),"
        )
    lines.extend(
        [
            "]);",
            "const byCode = new Map(industries.map((item) => [item.code, item]));",
            "const sectorByCode = new Map<string, IndustrySector>(",
            "  industrySectors.map((item) => [item.code, item]),",
            ");",
            "const sectorById = new Map<string, IndustrySector>(",
            "  industrySectors.map((item) => [item.id, item]),",
            ");",
            "const mutableChildren = new Map<string, Industry[]>();",
            "for (const item of industries) {",
            "  if (item.parentCode === null) continue;",
            "  const values = mutableChildren.get(item.parentCode) ?? [];",
            "  values.push(item);",
            "  mutableChildren.set(item.parentCode, values);",
            "}",
            "const children = new Map<string, readonly Industry[]>(",
            "  [...mutableChildren].map(([code, values]) => [code, Object.freeze(values)]),",
            ");",
            "const EMPTY_INDUSTRIES: readonly Industry[] = Object.freeze([]);",
            "export const sectorEntries = Object.freeze(",
            "  industries.filter((item) => item.level === IndustryLevel.Sector),",
            ");",
            "export function resolveIndustry(code: string): Industry | undefined {",
            "  return byCode.get(code);",
            "}",
            "export function resolveIndustrySector(idOrCode: string): IndustrySector | undefined {",
            "  return sectorById.get(idOrCode) ?? sectorByCode.get(idOrCode);",
            "}",
            "export function sectorForIndustry(value: Industry | string): IndustrySector | undefined {",
            "  const item = typeof value === 'string' ? resolveIndustry(value) : value;",
            "  return item ? sectorByCode.get(item.sectorCode) : undefined;",
            "}",
            "export function sectorEntryForIndustry(value: Industry | string): Industry | undefined {",
            "  const sector = sectorForIndustry(value);",
            "  return sector ? resolveIndustry(sector.code) : undefined;",
            "}",
            "export function parentOf(value: Industry | string): Industry | undefined {",
            "  const item = typeof value === 'string' ? resolveIndustry(value) : value;",
            "  return item?.parentCode ? resolveIndustry(item.parentCode) : undefined;",
            "}",
            "export function childrenOf(value: Industry | string): readonly Industry[] {",
            "  const code = typeof value === 'string' ? value : value.code;",
            "  return children.get(code) ?? EMPTY_INDUSTRIES;",
            "}",
            "",
            "export interface SicLevelValue {",
            "  readonly id: string;",
            "  readonly depth: number;",
            "}",
            "",
            "export const SicLevel = Object.freeze({",
            "  Division: Object.freeze({ id: 'division', depth: 1 }),",
            "  MajorGroup: Object.freeze({ id: 'major_group', depth: 2 }),",
            "  IndustryGroup: Object.freeze({ id: 'industry_group', depth: 3 }),",
            "  Industry: Object.freeze({ id: 'industry', depth: 4 }),",
            "  QcewRollup: Object.freeze({ id: 'qcew_rollup', depth: 4 }),",
            "} as const);",
            "export type SicLevel = (typeof SicLevel)[keyof typeof SicLevel];",
            "",
            "export interface SicDivisionValue {",
            "  readonly id: string;",
            "  readonly code: string;",
            "  readonly name: string;",
            "  readonly materialSymbol: string;",
            "  readonly description: string;",
            "}",
            "",
            "export const SicDivision = Object.freeze({",
        ]
    )
    for division in divisions:
        lines.append(
            f"  {pascal(division['division_id'])}: Object.freeze({{ "
            f"id: {ts_string(division['division_id'])}, "
            f"code: {ts_string(division['division_code'])}, "
            f"name: {ts_string(division['name'])}, "
            f"materialSymbol: {ts_string(division['material_symbol'])}, "
            f"description: {ts_string(division['description'])} }}),"
        )
    lines.extend(
        [
            "} as const);",
            "export type SicDivision = (typeof SicDivision)[keyof typeof SicDivision];",
            "export const sicDivisions: readonly SicDivision[] = Object.freeze(",
            "  Object.values(SicDivision),",
            ");",
            "",
            "export interface SicIndustry {",
            "  readonly code: string;",
            "  readonly title: string;",
            "  readonly level: SicLevel;",
            "  readonly parentCode: string | null;",
            "  readonly divisionCode: string;",
            "}",
            "",
            "function sicIndustry(item: SicIndustry): SicIndustry { return Object.freeze(item); }",
            "",
            "export const sicIndustries: readonly SicIndustry[] = Object.freeze([",
        ]
    )
    for row in sic_rows:
        parent = ts_string(row["parent"]) if row["parent"] else "null"
        lines.append(
            f"  sicIndustry({{ code: {ts_string(row['code'])}, title: {ts_string(row['title'])}, "
            f"level: SicLevel.{sic_level_names[row['level']]}, parentCode: {parent}, "
            f"divisionCode: {ts_string(row['division'])} }}),"
        )
    lines.extend(
        [
            "]);",
            "const sicByCode = new Map(sicIndustries.map((item) => [item.code, item]));",
            "const sicDivisionByCode = new Map<string, SicDivision>(",
            "  sicDivisions.map((item) => [item.code, item]),",
            ");",
            "const sicDivisionById = new Map<string, SicDivision>(",
            "  sicDivisions.map((item) => [item.id, item]),",
            ");",
            "const mutableSicChildren = new Map<string, SicIndustry[]>();",
            "for (const item of sicIndustries) {",
            "  if (item.parentCode === null) continue;",
            "  const values = mutableSicChildren.get(item.parentCode) ?? [];",
            "  values.push(item);",
            "  mutableSicChildren.set(item.parentCode, values);",
            "}",
            "const sicChildren = new Map<string, readonly SicIndustry[]>(",
            "  [...mutableSicChildren].map(([code, values]) => [code, Object.freeze(values)]),",
            ");",
            "const EMPTY_SIC_INDUSTRIES: readonly SicIndustry[] = Object.freeze([]);",
            "export const sicDivisionEntries = Object.freeze(",
            "  sicIndustries.filter((item) => item.level === SicLevel.Division),",
            ");",
            "export function resolveSic(code: string): SicIndustry | undefined {",
            "  return sicByCode.get(code);",
            "}",
            "export function resolveSicDivision(idOrCode: string): SicDivision | undefined {",
            "  return sicDivisionById.get(idOrCode) ?? sicDivisionByCode.get(idOrCode);",
            "}",
            "export function divisionForSic(value: SicIndustry | string): SicDivision | undefined {",
            "  const item = typeof value === 'string' ? resolveSic(value) : value;",
            "  return item ? sicDivisionByCode.get(item.divisionCode) : undefined;",
            "}",
            "export function divisionEntryForSic(value: SicIndustry | string): SicIndustry | undefined {",
            "  const division = divisionForSic(value);",
            "  return division ? resolveSic(division.code) : undefined;",
            "}",
            "export function parentOfSic(value: SicIndustry | string): SicIndustry | undefined {",
            "  const item = typeof value === 'string' ? resolveSic(value) : value;",
            "  return item?.parentCode ? resolveSic(item.parentCode) : undefined;",
            "}",
            "export function childrenOfSic(value: SicIndustry | string): readonly SicIndustry[] {",
            "  const code = typeof value === 'string' ? value : value.code;",
            "  return sicChildren.get(code) ?? EMPTY_SIC_INDUSTRIES;",
            "}",
            "export function materialSymbolForSic(value: SicIndustry | string): string | undefined {",
            "  return divisionForSic(value)?.materialSymbol;",
            "}",
            "",
            "export type NaicsIndustry = Industry;",
            "export const NaicsLevel = IndustryLevel;",
            "export type NaicsLevel = IndustryLevel;",
            "export const NaicsSector = IndustrySector;",
            "export type NaicsSector = IndustrySector;",
            "export const naicsIndustries = industries;",
            "export const resolveNaics = resolveIndustry;",
            "export const childrenOfNaics = childrenOf;",
        ]
    )
    return "\n".join(lines)


def _dart(
    naics_rows: list[dict[str, str]],
    sectors: list[dict[str, str]],
    sic_rows: list[dict[str, str]],
    divisions: list[dict[str, str]],
    digest: str,
) -> str:
    naics_level_names = {
        "2": "sector",
        "3": "subsector",
        "4": "industryGroup",
        "5": "naicsIndustry",
        "6": "nationalIndustry",
    }
    sic_level_names = {
        "division": "division",
        "major_group": "majorGroup",
        "industry_group": "industryGroup",
        "industry": "industry",
        "qcew_rollup": "qcewRollup",
    }
    lines = [
        "// Generated offline NAICS 2022 and SIC 1987 reference data.",
        f"// Input SHA-256: {digest}",
        "import 'package:flutter/material.dart';",
        "",
        f"const String dataFingerprint = {dart_string(digest)};",
        "const String naicsVersion = '2022';",
        "const String sicVersion = '1987';",
        f"const int naicsIndustryCount = {len(naics_rows)};",
        f"const int sicIndustryCount = {len(sic_rows)};",
        "",
        "enum IndustryLevel {",
        "  sector(2),",
        "  subsector(3),",
        "  industryGroup(4),",
        "  naicsIndustry(5),",
        "  nationalIndustry(6);",
        "",
        "  const IndustryLevel(this.depth);",
        "  final int depth;",
        "}",
        "",
        "enum IndustrySector {",
    ]
    for index, sector in enumerate(sectors):
        suffix = ";" if index == len(sectors) - 1 else ","
        lines.append(
            f"  {camel(sector['sector_id'])}({dart_string(sector['sector_id'])}, "
            f"{dart_string(sector['sector_code'])}, {dart_string(sector['name'])}, "
            f"{dart_string(sector['description'])}, Icons.{sector['material_symbol']}){suffix}"
        )
    lines.extend(
        [
            "",
            "  const IndustrySector(this.id, this.code, this.label, this.description, this.icon);",
            "  final String id;",
            "  final String code;",
            "  final String label;",
            "  final String description;",
            "  final IconData icon;",
            "  static IndustrySector? tryParse(String idOrCode) =>",
            "      _naicsSectorById[idOrCode] ?? _naicsSectorByCode[idOrCode];",
            "}",
            "",
            "class Industry {",
            "  const Industry(this.code, this.title, this.level, this.parentCode, this.sectorCode);",
            "  final String code;",
            "  final String title;",
            "  final IndustryLevel level;",
            "  final String? parentCode;",
            "  final String sectorCode;",
            "  Industry? get parent => parentCode == null ? null : resolveIndustry(parentCode!);",
            "  IndustrySector get sector => _naicsSectorByCode[sectorCode]!;",
            "  Industry get sectorEntry => resolveIndustry(sectorCode)!;",
            "  IconData get icon => sector.icon;",
            "  List<Industry> get children => childrenOf(code);",
            "}",
            "",
            "const List<Industry> industries = [",
        ]
    )
    for row in naics_rows:
        parent = dart_string(row["parent"]) if row["parent"] else "null"
        lines.append(
            f"  Industry({dart_string(row['code'])}, {dart_string(row['title'])}, "
            f"IndustryLevel.{naics_level_names[row['level']]}, {parent}, "
            f"{dart_string(row['sector'])}),"
        )
    lines.extend(
        [
            "];",
            "final Map<String, IndustrySector> _naicsSectorById = {",
            "  for (final item in IndustrySector.values) item.id: item,",
            "};",
            "final Map<String, IndustrySector> _naicsSectorByCode = {",
            "  for (final item in IndustrySector.values) item.code: item,",
            "};",
            "final Map<String, Industry> _naicsByCode = {",
            "  for (final item in industries) item.code: item,",
            "};",
            "final Map<String, List<Industry>> _naicsChildren = _buildNaicsChildren();",
            "Map<String, List<Industry>> _buildNaicsChildren() {",
            "  final result = <String, List<Industry>>{};",
            "  for (final item in industries) {",
            "    final parentCode = item.parentCode;",
            "    if (parentCode != null) {",
            "      (result[parentCode] ??= <Industry>[]).add(item);",
            "    }",
            "  }",
            "  return Map<String, List<Industry>>.unmodifiable({",
            "    for (final entry in result.entries)",
            "      entry.key: List<Industry>.unmodifiable(entry.value),",
            "  });",
            "}",
            "final List<IndustrySector> industrySectors = List.unmodifiable(IndustrySector.values);",
            "final List<Industry> sectorEntries = List.unmodifiable(",
            "  industries.where((item) => item.level == IndustryLevel.sector),",
            ");",
            "Industry? resolveIndustry(String code) => _naicsByCode[code];",
            "List<Industry> childrenOf(String code) => _naicsChildren[code] ?? const [];",
            "",
            "enum SicLevel {",
            "  division('division', 1),",
            "  majorGroup('major_group', 2),",
            "  industryGroup('industry_group', 3),",
            "  industry('industry', 4),",
            "  qcewRollup('qcew_rollup', 4);",
            "",
            "  const SicLevel(this.id, this.depth);",
            "  final String id;",
            "  final int depth;",
            "}",
            "",
            "enum SicDivision {",
        ]
    )
    for index, division in enumerate(divisions):
        suffix = ";" if index == len(divisions) - 1 else ","
        lines.append(
            f"  {camel(division['division_id'])}({dart_string(division['division_id'])}, "
            f"{dart_string(division['division_code'])}, {dart_string(division['name'])}, "
            f"{dart_string(division['description'])}, Icons.{division['material_symbol']}){suffix}"
        )
    lines.extend(
        [
            "",
            "  const SicDivision(this.id, this.code, this.label, this.description, this.icon);",
            "  final String id;",
            "  final String code;",
            "  final String label;",
            "  final String description;",
            "  final IconData icon;",
            "  static SicDivision? tryParse(String idOrCode) =>",
            "      _sicDivisionById[idOrCode] ?? _sicDivisionByCode[idOrCode];",
            "}",
            "",
            "class SicIndustry {",
            "  const SicIndustry(this.code, this.title, this.level, this.parentCode, this.divisionCode);",
            "  final String code;",
            "  final String title;",
            "  final SicLevel level;",
            "  final String? parentCode;",
            "  final String divisionCode;",
            "  SicIndustry? get parent => parentCode == null ? null : resolveSic(parentCode!);",
            "  SicDivision get division => _sicDivisionByCode[divisionCode]!;",
            "  SicIndustry get divisionEntry => resolveSic(divisionCode)!;",
            "  IconData get icon => division.icon;",
            "  List<SicIndustry> get children => childrenOfSic(code);",
            "}",
            "",
            "const List<SicIndustry> sicIndustries = [",
        ]
    )
    for row in sic_rows:
        parent = dart_string(row["parent"]) if row["parent"] else "null"
        lines.append(
            f"  SicIndustry({dart_string(row['code'])}, {dart_string(row['title'])}, "
            f"SicLevel.{sic_level_names[row['level']]}, {parent}, "
            f"{dart_string(row['division'])}),"
        )
    lines.extend(
        [
            "];",
            "final Map<String, SicDivision> _sicDivisionById = {",
            "  for (final item in SicDivision.values) item.id: item,",
            "};",
            "final Map<String, SicDivision> _sicDivisionByCode = {",
            "  for (final item in SicDivision.values) item.code: item,",
            "};",
            "final Map<String, SicIndustry> _sicByCode = {",
            "  for (final item in sicIndustries) item.code: item,",
            "};",
            "final Map<String, List<SicIndustry>> _sicChildren = _buildSicChildren();",
            "Map<String, List<SicIndustry>> _buildSicChildren() {",
            "  final result = <String, List<SicIndustry>>{};",
            "  for (final item in sicIndustries) {",
            "    final parentCode = item.parentCode;",
            "    if (parentCode != null) {",
            "      (result[parentCode] ??= <SicIndustry>[]).add(item);",
            "    }",
            "  }",
            "  return Map<String, List<SicIndustry>>.unmodifiable({",
            "    for (final entry in result.entries)",
            "      entry.key: List<SicIndustry>.unmodifiable(entry.value),",
            "  });",
            "}",
            "final List<SicDivision> sicDivisions = List.unmodifiable(SicDivision.values);",
            "final List<SicIndustry> sicDivisionEntries = List.unmodifiable(",
            "  sicIndustries.where((item) => item.level == SicLevel.division),",
            ");",
            "SicIndustry? resolveSic(String code) => _sicByCode[code];",
            "List<SicIndustry> childrenOfSic(String code) => _sicChildren[code] ?? const [];",
            "",
            "typedef NaicsIndustry = Industry;",
            "typedef NaicsLevel = IndustryLevel;",
            "typedef NaicsSector = IndustrySector;",
            "const List<Industry> naicsIndustries = industries;",
            "Industry? resolveNaics(String code) => resolveIndustry(code);",
            "List<Industry> childrenOfNaics(String code) => childrenOf(code);",
        ]
    )
    return "\n".join(lines)


def generate(check: bool = False) -> list[Path]:
    naics_rows, sectors = _load_naics()
    sic_rows, divisions = _load_sic()
    digest = fingerprint(
        (NAICS_PATH, NAICS_SECTORS_PATH, SIC_PATH, SIC_DIVISIONS_PATH)
    )
    outputs = {
        ROOT
        / "packages"
        / "python"
        / "reffin_industries"
        / "src"
        / "reffin_industries"
        / "_generated.py": _python(naics_rows, sectors, sic_rows, divisions, digest),
        ROOT
        / "packages"
        / "typescript"
        / "reffin_industries"
        / "src"
        / "generated.ts": _typescript(naics_rows, sectors, sic_rows, divisions, digest),
        ROOT
        / "packages"
        / "flutter"
        / "reffin_industries"
        / "lib"
        / "src"
        / "generated.dart": _dart(naics_rows, sectors, sic_rows, divisions, digest),
    }
    stale = [
        path for path, content in outputs.items() if not write_or_check(path, content, check)
    ]
    action = "verified" if check else "generated"
    print(
        f"{action} {len(naics_rows)} NAICS 2022 and "
        f"{len(sic_rows)} SIC 1987 industries"
    )
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
