#!/usr/bin/env python3
"""Generate the Reffin ACH packages from normalized offline CSV inputs."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REFERENCE_AS_OF = "2026-08-11"
STATUSES = {"current", "planned", "legacy"}


@dataclass(frozen=True, slots=True)
class Family:
    filename: str
    stem: str
    enum_name: str
    info_name: str
    resolve_name: str
    icon: str
    columns: tuple[str, ...]
    list_columns: tuple[str, ...] = ()

    @property
    def dataset_id(self) -> str:
        return self.filename.removesuffix(".csv")

    @property
    def records_name(self) -> str:
        return f"{self.stem}_RECORDS"

    @property
    def current_records_name(self) -> str:
        return f"CURRENT_{self.stem}_RECORDS"

    @property
    def count_name(self) -> str:
        return f"{self.stem}_COUNT"

    @property
    def record_count_name(self) -> str:
        return f"{self.stem}_RECORD_COUNT"

    @property
    def current_count_name(self) -> str:
        return f"CURRENT_{self.stem}_COUNT"


FAMILIES = (
    Family(
        "transaction_codes.csv",
        "TRANSACTION_CODE",
        "AchTransactionCode",
        "AchTransactionCodeInfo",
        "transaction_code",
        "payments",
        ("account_type", "direction", "entry_kind", "return_for_codes"),
        ("return_for_codes",),
    ),
    Family(
        "return_codes.csv",
        "RETURN_CODE",
        "AchReturnCode",
        "AchReturnCodeInfo",
        "return_code",
        "undo",
        ("category",),
    ),
    Family(
        "standard_entry_class_codes.csv",
        "STANDARD_ENTRY_CLASS_CODE",
        "AchStandardEntryClassCode",
        "AchStandardEntryClassCodeInfo",
        "standard_entry_class_code",
        "account_balance",
        (
            "entry_kind",
            "consumer_or_corporate",
            "direction",
            "addenda_support",
        ),
    ),
    Family(
        "service_class_codes.csv",
        "SERVICE_CLASS_CODE",
        "AchServiceClassCode",
        "AchServiceClassCodeInfo",
        "service_class_code",
        "sync_alt",
        ("direction",),
    ),
    Family(
        "record_type_codes.csv",
        "RECORD_TYPE_CODE",
        "AchRecordTypeCode",
        "AchRecordTypeCodeInfo",
        "record_type_code",
        "description",
        (),
    ),
    Family(
        "change_codes.csv",
        "CHANGE_CODE",
        "AchChangeCode",
        "AchChangeCodeInfo",
        "change_code",
        "edit",
        ("corrected_field", "applies_to"),
        ("corrected_field", "applies_to"),
    ),
    Family(
        "addenda_type_codes.csv",
        "ADDENDA_TYPE_CODE",
        "AchAddendaTypeCode",
        "AchAddendaTypeCodeInfo",
        "addenda_type_code",
        "note_add",
        ("applies_to",),
        ("applies_to",),
    ),
)


EXPECTED_CODES = {
    "transaction_codes": {
        "21", "22", "23", "24", "26", "27", "28", "29",
        "31", "32", "33", "34", "36", "37", "38", "39",
        "41", "42", "43", "44", "46", "47", "48", "49",
        "51", "52", "53", "54", "55", "56",
        "81", "82", "83", "84", "85", "86", "87", "88",
    },
    "return_codes": {
        *(f"R{value:02d}" for value in range(1, 48)),
        "R50", "R51", "R52", "R53", "R61", "R62",
        *(f"R{value}" for value in range(67, 78)),
        *(f"R{value}" for value in range(80, 86)),
        "R90",
    },
    "standard_entry_class_codes": {
        "ACK", "ADV", "ARC", "ATX", "BOC", "CCD", "CIE", "COR",
        "CTX", "DNE", "ENR", "IAT", "MTE", "POP", "POS", "PPD",
        "RCK", "SHR", "TEL", "TRC", "TRX", "WEB", "XCK",
    },
    "service_class_codes": {"200", "220", "225", "280"},
    "record_type_codes": {"1", "5", "6", "7", "8", "9"},
    "change_codes": {
        "C01", "C02", "C03", "C05", "C06",
        "C07", "C08", "C09", "C13", "C14",
    },
    "addenda_type_codes": {
        "01", "02", "05", "10", "11", "12", "13",
        "14", "15", "16", "17", "18", "98", "99",
    },
}


FLUTTER_ICONS = {
    "account_balance": "account_balance",
    "description": "description",
    "edit": "edit",
    "note_add": "note_add",
    "payments": "payments",
    "sync_alt": "sync_alt",
    "undo": "undo",
}


def _words(value: str) -> list[str]:
    return [part for part in re.split(r"[^A-Za-z0-9]+", value) if part]


def _pascal(value: str) -> str:
    return "".join(part[:1].upper() + part[1:].lower() for part in _words(value))


def _camel(value: str) -> str:
    value = _pascal(value)
    return value[:1].lower() + value[1:]


def _snake(value: str) -> str:
    return "_".join(part.lower() for part in _words(value))


def _enum_member(code: str, language: str) -> str:
    if code.isdigit():
        prefix = {"python": "CODE_", "typescript": "Code", "dart": "code"}[language]
        return f"{prefix}{code}"
    if language == "python" or language == "typescript":
        return re.sub(r"[^A-Za-z0-9]", "_", code).upper()
    return re.sub(r"[^A-Za-z0-9]", "", code).lower()


def _py_string(value: str) -> str:
    return repr(value)


def _ts_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _dart_string(value: str) -> str:
    value = value.replace("\\", "\\\\").replace("'", "\\'").replace("$", "\\$")
    return f"'{value}'"


def _date_literal(value: str, language: str) -> str:
    if not value:
        return {"python": "None", "typescript": "null", "dart": "null"}[language]
    year, month, day = (int(part) for part in value.split("-"))
    if language == "python":
        return f"date({year}, {month}, {day})"
    if language == "typescript":
        return _ts_string(value)
    return f"DateTime.utc({year}, {month}, {day})"


def _columns_for(family: Family) -> list[str]:
    columns = ["code", "name", *family.columns, "status"]
    if family.filename in {
        "return_codes.csv", "standard_entry_class_codes.csv", "change_codes.csv"
    }:
        columns.extend(["valid_from", "valid_to"])
    columns.append("source")
    return columns


def _load_family(root: Path, family: Family) -> list[dict[str, str]]:
    path = root / "data" / "ach" / family.filename
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        expected = _columns_for(family)
        if reader.fieldnames != expected:
            raise ValueError(f"{path}: expected columns {expected!r}, got {reader.fieldnames!r}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"{path}: table must not be empty")

    seen_identity: set[tuple[str, str, str]] = set()
    by_code: dict[str, list[dict[str, str]]] = {}
    for row_number, row in enumerate(rows, start=2):
        if any(value != value.strip() for value in row.values()):
            raise ValueError(f"{path}:{row_number}: fields must not have outer whitespace")
        if not row["code"] or not row["name"]:
            raise ValueError(f"{path}:{row_number}: code and name are required")
        if row["status"] not in STATUSES:
            raise ValueError(f"{path}:{row_number}: invalid status {row['status']!r}")
        if not row["source"]:
            raise ValueError(f"{path}:{row_number}: source is required")
        for date_column in ("valid_from", "valid_to"):
            if date_column in row and row[date_column] and not re.fullmatch(
                r"\d{4}-\d{2}-\d{2}", row[date_column]
            ):
                raise ValueError(f"{path}:{row_number}: invalid {date_column}")
        identity = (row["code"], row.get("valid_from", ""), row.get("valid_to", ""))
        if identity in seen_identity:
            raise ValueError(f"{path}:{row_number}: duplicate row identity {identity!r}")
        seen_identity.add(identity)
        by_code.setdefault(row["code"], []).append(row)

    codes = set(by_code)
    expected_codes = EXPECTED_CODES[family.dataset_id]
    if codes != expected_codes:
        raise ValueError(
            f"{path}: code set mismatch; missing={sorted(expected_codes - codes)}, "
            f"extra={sorted(codes - expected_codes)}"
        )
    duplicates = {code for code, records in by_code.items() if len(records) > 1}
    allowed_duplicates = {"R16"} if family.dataset_id == "return_codes" else set()
    if duplicates != allowed_duplicates:
        raise ValueError(f"{path}: unexpected versioned codes {sorted(duplicates)!r}")

    if family.dataset_id == "return_codes":
        r16 = by_code["R16"]
        if [(row["valid_from"], row["valid_to"]) for row in r16] != [
            ("", "2028-03-16"), ("2028-03-17", "")
        ]:
            raise ValueError(f"{path}: R16 lifecycle rows are not contiguous and ordered")
        r90 = by_code["R90"][0]
        if r90["status"] != "planned" or r90["valid_from"] != "2028-03-17":
            raise ValueError(f"{path}: R90 must begin as planned on 2028-03-17")
        planned = [
            (row["code"], row["valid_from"])
            for row in rows
            if row["status"] == "planned"
        ]
        if planned != [("R16", "2028-03-17"), ("R90", "2028-03-17")]:
            raise ValueError(f"{path}: unexpected planned lifecycle rows {planned!r}")
        if sum(row["status"] == "current" for row in rows) != 70:
            raise ValueError(f"{path}: expected exactly 70 current rows")
    if family.dataset_id == "addenda_type_codes":
        legacy = [row["code"] for row in rows if row["status"] == "legacy"]
        if legacy != ["01"]:
            raise ValueError(f"{path}: addenda 01 must be the only legacy row")
        if sum(row["status"] == "current" for row in rows) != 13:
            raise ValueError(f"{path}: expected exactly 13 current rows")
    if family.dataset_id not in {"return_codes", "addenda_type_codes"}:
        noncurrent = [row["code"] for row in rows if row["status"] != "current"]
        if noncurrent:
            raise ValueError(f"{path}: unexpected non-current rows {noncurrent!r}")

    order = [(row["code"], row.get("valid_from", "")) for row in rows]
    if order != sorted(order):
        raise ValueError(f"{path}: rows must be sorted by code and valid_from")
    return rows


def load_families(root: Path) -> list[tuple[Family, list[dict[str, str]]]]:
    loaded = [(family, _load_family(root, family)) for family in FAMILIES]
    source_keys = {
        key
        for _, rows in loaded
        for row in rows
        for key in row["source"].split("|")
    }
    provenance = (root / "data" / "ach" / "README.md").read_text(encoding="utf-8")
    undeclared = sorted(key for key in source_keys if f"`{key}`" not in provenance)
    if undeclared:
        raise ValueError(f"data/ach/README.md: undeclared source keys {undeclared!r}")
    return loaded


def input_hash(root: Path) -> str:
    digest = hashlib.sha256()
    directory = root / "data" / "ach"
    paths = sorted(directory.glob("*.csv")) + [directory / "README.md"]
    for path in paths:
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _py_type(field: str, family: Family) -> str:
    return "tuple[str, ...]" if field in family.list_columns else "str"


def _py_value(row: dict[str, str], field: str, family: Family) -> str:
    if field in family.list_columns:
        values = tuple(part for part in row[field].split("|") if part)
        return repr(values)
    return _py_string(row[field])


def python_output(
    loaded: list[tuple[Family, list[dict[str, str]]]], fingerprint: str
) -> str:
    lines = [
        '"""Generated ACH reference catalogs. Do not edit by hand."""',
        "",
        f"# Input SHA-256: {fingerprint}",
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "from datetime import date, datetime",
        "from enum import Enum",
        "from types import MappingProxyType",
        "from typing import Final, Mapping, Self, TypeVar",
        "",
        f"DATA_FINGERPRINT: Final = {_py_string(fingerprint)}",
        "REFERENCE_AS_OF: Final = date(2026, 8, 11)",
        "",
        "",
        "class AchCodeStatus(str, Enum):",
        "    CURRENT = 'current'",
        "    PLANNED = 'planned'",
        "    LEGACY = 'legacy'",
        "",
        "",
        "@dataclass(frozen=True, slots=True)",
        "class AchReferenceInfo:",
        "    code: str",
        "    name: str",
        "    status: AchCodeStatus",
        "    valid_from: date | None",
        "    valid_to: date | None",
        "    sources: tuple[str, ...]",
        "    material_symbol: str",
        "",
        "    def is_effective(self, on: date = REFERENCE_AS_OF) -> bool:",
        "        if isinstance(on, datetime):",
        "            on = on.date()",
        "        if self.status is AchCodeStatus.LEGACY:",
        "            return False",
        "        if self.valid_from is not None and on < self.valid_from:",
        "            return False",
        "        return self.valid_to is None or on <= self.valid_to",
    ]

    for family, _ in loaded:
        lines.extend(["", "", "@dataclass(frozen=True, slots=True)"])
        lines.append(f"class {family.info_name}(AchReferenceInfo):")
        if family.columns:
            for field in family.columns:
                attr = "corrected_fields" if field == "corrected_field" else field
                lines.append(f"    {attr}: {_py_type(field, family)}")
        else:
            lines.append("    pass")

    lines.extend(
        [
            "",
            "",
            "class _AchCode(str, Enum):",
            "    @property",
            "    def code(self) -> str:",
            "        return str(self.value)",
            "",
            "    @classmethod",
            "    def try_parse(cls, value: object) -> Self | None:",
            "        if isinstance(value, cls):",
            "            return value",
            "        if not isinstance(value, str):",
            "            return None",
            "        try:",
            "            return cls(value.strip().upper())",
            "        except ValueError:",
            "            return None",
        ]
    )

    for family, rows in loaded:
        unique_codes = list(dict.fromkeys(row["code"] for row in rows))
        lines.extend(["", "", f"class {family.enum_name}(_AchCode):"])
        for code in unique_codes:
            lines.append(f"    {_enum_member(code, 'python')} = {_py_string(code)}")
        lines.extend(
            [
                "",
                "    @property",
                f"    def info(self) -> {family.info_name}:",
                f"        return _DEFAULT_{family.stem}_INFO[self.value]",
                "",
                "    @property",
                "    def label(self) -> str:",
                "        return self.info.name",
                "",
                "    @property",
                "    def material_symbol(self) -> str:",
                "        return self.info.material_symbol",
            ]
        )

    for family, rows in loaded:
        lines.extend(["", "", f"{family.records_name}: Final[tuple[{family.info_name}, ...]] = ("])
        for row in rows:
            args = [
                _py_string(row["code"]),
                _py_string(row["name"]),
                f"AchCodeStatus.{row['status'].upper()}",
                _date_literal(row.get("valid_from", ""), "python"),
                _date_literal(row.get("valid_to", ""), "python"),
                repr(tuple(row["source"].split("|"))),
                _py_string(family.icon),
            ]
            args.extend(_py_value(row, field, family) for field in family.columns)
            lines.append(f"    {family.info_name}({', '.join(args)}),")
        lines.append(")")

    lines.extend(
        [
            "",
            "_InfoT = TypeVar('_InfoT', bound=AchReferenceInfo)",
            "",
            "",
            "def _index(records: tuple[_InfoT, ...]) -> Mapping[str, tuple[_InfoT, ...]]:",
            "    mutable: dict[str, list[_InfoT]] = {}",
            "    for record in records:",
            "        mutable.setdefault(record.code, []).append(record)",
            "    return MappingProxyType({code: tuple(values) for code, values in mutable.items()})",
            "",
            "",
            "def _resolve(",
            "    index: Mapping[str, tuple[_InfoT, ...]],",
            "    value: object,",
            "    on: date,",
            "    include_inactive: bool,",
            ") -> _InfoT | None:",
            "    code = value.value if isinstance(value, _AchCode) else value",
            "    if not isinstance(code, str):",
            "        return None",
            "    records = index.get(code.strip().upper())",
            "    if not records:",
            "        return None",
            "    for record in records:",
            "        if record.is_effective(on):",
            "            return record",
            "    return records[0] if include_inactive else None",
        ]
    )

    for family, _ in loaded:
        index_name = f"_{family.stem}_BY_CODE"
        default_name = f"_DEFAULT_{family.stem}_INFO"
        lines.extend(
            [
                "",
                f"{index_name}: Final = _index({family.records_name})",
                f"{default_name}: Final[Mapping[str, {family.info_name}]] = MappingProxyType({{",
                "    code: _resolve(" + index_name + ", code, REFERENCE_AS_OF, True)",
                f"    for code in {index_name}",
                "})  # type: ignore[dict-item]",
                f"{family.current_records_name}: Final = tuple(",
                f"    record for record in {family.records_name} if record.is_effective()",
                ")",
                f"{family.count_name}: Final = len({index_name})",
                f"{family.record_count_name}: Final = len({family.records_name})",
                f"{family.current_count_name}: Final = len({family.current_records_name})",
                "",
                f"def resolve_{family.resolve_name}(",
                f"    code: str | {family.enum_name}, *, include_inactive: bool = False",
                f") -> {family.info_name} | None:",
                f"    return _resolve({index_name}, code, REFERENCE_AS_OF, include_inactive)",
                "",
                f"def resolve_{family.resolve_name}_as_of(",
                f"    code: str | {family.enum_name}, on: date, *, include_inactive: bool = False",
                f") -> {family.info_name} | None:",
                f"    return _resolve({index_name}, code, on, include_inactive)",
            ]
        )

    lines.extend(["", "RECORDS: Final[Mapping[str, tuple[AchReferenceInfo, ...]]] = MappingProxyType({"])
    for family, _ in loaded:
        lines.append(f"    {_py_string(family.dataset_id)}: {family.records_name},")
    lines.extend(["})", "", "COUNTS: Final[Mapping[str, int]] = MappingProxyType({"])
    for family, _ in loaded:
        lines.append(f"    {_py_string(family.dataset_id)}: {family.count_name},")
    lines.extend(["})", ""])
    return "\n".join(lines)


def _ts_field(field: str) -> str:
    if field == "corrected_field":
        return "correctedFields"
    parts = field.split("_")
    return parts[0] + "".join(part.title() for part in parts[1:])


def _ts_value(row: dict[str, str], field: str, family: Family) -> str:
    if field in family.list_columns:
        values = [part for part in row[field].split("|") if part]
        return f"Object.freeze({json.dumps(values, ensure_ascii=False)})"
    return _ts_string(row[field])


def typescript_output(
    loaded: list[tuple[Family, list[dict[str, str]]]], fingerprint: str
) -> str:
    lines = [
        "// Generated ACH reference catalogs. Do not edit by hand.",
        f"// Input SHA-256: {fingerprint}",
        "",
        f"export const DATA_FINGERPRINT = {_ts_string(fingerprint)} as const;",
        f"export const REFERENCE_AS_OF = {_ts_string(REFERENCE_AS_OF)} as const;",
        "export type AchCodeStatus = 'current' | 'planned' | 'legacy';",
        "",
        "export interface AchReferenceInfo {",
        "  readonly code: string;",
        "  readonly name: string;",
        "  readonly status: AchCodeStatus;",
        "  readonly validFrom: string | null;",
        "  readonly validTo: string | null;",
        "  readonly sources: readonly string[];",
        "  readonly materialSymbol: string;",
        "}",
    ]

    for family, _ in loaded:
        lines.extend(["", f"export interface {family.info_name} extends AchReferenceInfo {{"])
        for field in family.columns:
            field_type = "readonly string[]" if field in family.list_columns else "string"
            lines.append(f"  readonly {_ts_field(field)}: {field_type};")
        lines.append("}")

    lines.extend(
        [
            "",
            "function freezeInfo<T extends AchReferenceInfo>(value: T): Readonly<T> {",
            "  return Object.freeze(value);",
            "}",
            "",
            "function normalizeDate(value: Date | string): string | undefined {",
            "  if (typeof value === 'string') {",
            "    const match = /^(\\d{4})-(\\d{2})-(\\d{2})$/.exec(value);",
            "    if (match === null) return undefined;",
            "    const year = Number(match[1]!);",
            "    const month = Number(match[2]!);",
            "    const day = Number(match[3]!);",
            "    const check = new Date(Date.UTC(year, month - 1, day));",
            "    if (check.getUTCFullYear() !== year || check.getUTCMonth() !== month - 1 || check.getUTCDate() !== day) return undefined;",
            "    return value;",
            "  }",
            "  if (Number.isNaN(value.getTime())) return undefined;",
            "  const year = String(value.getFullYear()).padStart(4, '0');",
            "  const month = String(value.getMonth() + 1).padStart(2, '0');",
            "  const day = String(value.getDate()).padStart(2, '0');",
            "  return `${year}-${month}-${day}`;",
            "}",
            "",
            "export function isEffective(info: AchReferenceInfo, on: Date | string = REFERENCE_AS_OF): boolean {",
            "  if (info.status === 'legacy') return false;",
            "  const key = normalizeDate(on);",
            "  if (key === undefined) return false;",
            "  if (info.validFrom !== null && key < info.validFrom) return false;",
            "  return info.validTo === null || key <= info.validTo;",
            "}",
            "",
            "function indexRecords<T extends AchReferenceInfo>(records: readonly T[]): ReadonlyMap<string, readonly T[]> {",
            "  const mutable = new Map<string, T[]>();",
            "  for (const record of records) {",
            "    const values = mutable.get(record.code) ?? [];",
            "    values.push(record);",
            "    mutable.set(record.code, values);",
            "  }",
            "  return new Map([...mutable].map(([code, values]) => [code, Object.freeze(values)]));",
            "}",
            "",
            "function codeOf(value: string | AchReferenceInfo): string {",
            "  return (typeof value === 'string' ? value : value.code).trim().toUpperCase();",
            "}",
            "",
            "function resolveAt<T extends AchReferenceInfo>(",
            "  index: ReadonlyMap<string, readonly T[]>,",
            "  value: string | AchReferenceInfo,",
            "  on: Date | string,",
            "  includeInactive: boolean,",
            "): T | undefined {",
            "  const records = index.get(codeOf(value));",
            "  if (!records) return undefined;",
            "  return records.find((record) => isEffective(record, on)) ?? (includeInactive ? records[0] : undefined);",
            "}",
        ]
    )

    for family, rows in loaded:
        ts_records = _camel(family.records_name)
        lines.extend(["", f"export const {ts_records}: readonly {family.info_name}[] = Object.freeze(["])
        for row in rows:
            fields = [
                f"code: {_ts_string(row['code'])}",
                f"name: {_ts_string(row['name'])}",
                f"status: {_ts_string(row['status'])}",
                f"validFrom: {_date_literal(row.get('valid_from', ''), 'typescript')}",
                f"validTo: {_date_literal(row.get('valid_to', ''), 'typescript')}",
                f"sources: Object.freeze({json.dumps(row['source'].split('|'))})",
                f"materialSymbol: {_ts_string(family.icon)}",
            ]
            fields.extend(
                f"{_ts_field(field)}: {_ts_value(row, field, family)}"
                for field in family.columns
            )
            lines.append(f"  freezeInfo({{ {', '.join(fields)} }}),")
        lines.append("]);")
        index_name = f"_{_camel(family.stem)}ByCode"
        lines.append(f"const {index_name} = indexRecords({ts_records});")

        resolve_camel = _camel(f"resolve_{family.resolve_name}")
        resolve_as_of = resolve_camel + "AsOf"
        lines.extend(
            [
                f"export function {resolve_camel}(",
                f"  code: string | {family.info_name}, options: {{ readonly includeInactive?: boolean }} = {{}},",
                f"): {family.info_name} | undefined {{",
                f"  return resolveAt({index_name}, code, REFERENCE_AS_OF, options.includeInactive ?? false);",
                "}",
                f"export function {resolve_as_of}(",
                f"  code: string | {family.info_name}, on: Date | string,",
                "  options: { readonly includeInactive?: boolean } = {},",
                f"): {family.info_name} | undefined {{",
                f"  return resolveAt({index_name}, code, on, options.includeInactive ?? false);",
                "}",
            ]
        )

        unique_codes = list(dict.fromkeys(row["code"] for row in rows))
        lines.extend([f"export const {family.enum_name} = Object.freeze({{"])
        for code in unique_codes:
            member = _enum_member(code, "typescript")
            lines.append(
                f"  {member}: {resolve_camel}({_ts_string(code)}, {{ includeInactive: true }})!,"
            )
        lines.extend(
            [
                "});",
                f"export type {family.enum_name} = (typeof {family.enum_name})[keyof typeof {family.enum_name}];",
                f"export const {_camel(family.current_records_name)} = Object.freeze(",
                f"  {ts_records}.filter((record) => isEffective(record)),",
                ");",
                f"export const {_camel(family.count_name)} = {index_name}.size;",
                f"export const {_camel(family.record_count_name)} = {ts_records}.length;",
                f"export const {_camel(family.current_count_name)} = {_camel(family.current_records_name)}.length;",
            ]
        )

    lines.extend(["", "export const records = Object.freeze({"])
    for family, _ in loaded:
        lines.append(f"  {_camel(family.dataset_id)}: {_camel(family.records_name)},")
    lines.extend(["});", "", "export const counts = Object.freeze({"])
    for family, _ in loaded:
        lines.append(f"  {_camel(family.dataset_id)}: {_camel(family.count_name)},")
    lines.extend(["});", "", "export const RECORDS = records;", "export const COUNTS = counts;", ""])
    return "\n".join(lines)


def _dart_field(field: str) -> str:
    if field == "corrected_field":
        return "correctedFields"
    return _camel(field)


def _dart_value(row: dict[str, str], field: str, family: Family) -> str:
    if field in family.list_columns:
        values = [part for part in row[field].split("|") if part]
        return "const [" + ", ".join(_dart_string(value) for value in values) + "]"
    return _dart_string(row[field])


def dart_output(
    loaded: list[tuple[Family, list[dict[str, str]]]], fingerprint: str
) -> str:
    lines = [
        "// Generated ACH reference catalogs. Do not edit by hand.",
        f"// Input SHA-256: {fingerprint}",
        "",
        "import 'package:flutter/material.dart';",
        "",
        "// ignore: constant_identifier_names",
        f"const String DATA_FINGERPRINT = {_dart_string(fingerprint)};",
        "const String dataFingerprint = DATA_FINGERPRINT;",
        "final DateTime referenceAsOf = DateTime.utc(2026, 8, 11);",
        "",
        "enum AchCodeStatus { current, planned, legacy }",
        "",
        "abstract final class AchReferenceInfo {",
        "  const AchReferenceInfo({",
        "    required this.code, required this.name, required this.status,",
        "    required this.validFrom, required this.validTo, required this.sources,",
        "    required this.icon,",
        "  });",
        "  final String code;",
        "  final String name;",
        "  final AchCodeStatus status;",
        "  final DateTime? validFrom;",
        "  final DateTime? validTo;",
        "  final List<String> sources;",
        "  final IconData icon;",
        "",
        "  bool isEffective([DateTime? on]) {",
        "    final raw = on ?? referenceAsOf;",
        "    final value = DateTime.utc(raw.year, raw.month, raw.day);",
        "    if (status == AchCodeStatus.legacy) return false;",
        "    if (validFrom != null && value.isBefore(validFrom!)) return false;",
        "    return validTo == null || !value.isAfter(validTo!);",
        "  }",
        "}",
    ]

    for family, _ in loaded:
        lines.extend(["", f"final class {family.info_name} extends AchReferenceInfo {{"])
        lines.append(f"  const {family.info_name}({{")
        lines.extend(
            [
                "    required super.code, required super.name, required super.status,",
                "    required super.validFrom, required super.validTo, required super.sources,",
                "    required super.icon,",
            ]
        )
        for field in family.columns:
            lines.append(f"    required this.{_dart_field(field)},")
        lines.append("  });")
        for field in family.columns:
            field_type = "List<String>" if field in family.list_columns else "String"
            lines.append(f"  final {field_type} {_dart_field(field)};")
        lines.append("}")

    for family, rows in loaded:
        unique_codes = list(dict.fromkeys(row["code"] for row in rows))
        identity_map = f"_{_camel(family.stem)}IdentityByCode"
        default_map = f"_{_camel(family.stem)}DefaultInfo"
        lines.extend(["", f"enum {family.enum_name} {{"])
        for index, code in enumerate(unique_codes):
            suffix = ";" if index == len(unique_codes) - 1 else ","
            lines.append(f"  {_enum_member(code, 'dart')}({_dart_string(code)}){suffix}")
        lines.extend(
            [
                "",
                f"  const {family.enum_name}(this.code);",
                "  final String code;",
                f"  {family.info_name} get info => {default_map}[code]!;",
                "  String get label => info.name;",
                "  IconData get icon => info.icon;",
                f"  static {family.enum_name}? tryParse(String code) => {identity_map}[code.trim().toUpperCase()];",
                "}",
            ]
        )

    lines.extend(
        [
            "",
            "Map<String, List<T>> _indexRecords<T extends AchReferenceInfo>(List<T> records) {",
            "  final result = <String, List<T>>{};",
            "  for (final record in records) {",
            "    result.putIfAbsent(record.code, () => <T>[]).add(record);",
            "  }",
            "  return Map<String, List<T>>.unmodifiable({",
            "    for (final entry in result.entries) entry.key: List<T>.unmodifiable(entry.value),",
            "  });",
            "}",
            "",
            "T? _resolve<T extends AchReferenceInfo>(",
            "  Map<String, List<T>> index, String code, DateTime on, bool includeInactive,",
            ") {",
            "  final values = index[code.trim().toUpperCase()];",
            "  if (values == null) return null;",
            "  for (final value in values) {",
            "    if (value.isEffective(on)) return value;",
            "  }",
            "  return includeInactive ? values.first : null;",
            "}",
        ]
    )

    for family, rows in loaded:
        dart_records = _camel(family.records_name)
        lines.extend(["", f"final List<{family.info_name}> {dart_records} = List.unmodifiable(["])
        for row in rows:
            fields = [
                f"code: {_dart_string(row['code'])}",
                f"name: {_dart_string(row['name'])}",
                f"status: AchCodeStatus.{row['status']}",
                f"validFrom: {_date_literal(row.get('valid_from', ''), 'dart')}",
                f"validTo: {_date_literal(row.get('valid_to', ''), 'dart')}",
                "sources: const [" + ", ".join(_dart_string(v) for v in row["source"].split("|")) + "]",
                f"icon: Icons.{FLUTTER_ICONS[family.icon]}",
            ]
            fields.extend(
                f"{_dart_field(field)}: {_dart_value(row, field, family)}"
                for field in family.columns
            )
            lines.append(f"  {family.info_name}({', '.join(fields)}),")
        lines.append("]);")
        index_name = f"_{_camel(family.stem)}ByCode"
        lines.append(f"final {index_name} = _indexRecords({dart_records});")
        resolve_camel = _camel(f"resolve_{family.resolve_name}")
        lines.extend(
            [
                f"{family.info_name}? {resolve_camel}(String code, {{bool includeInactive = false}}) =>",
                f"    _resolve({index_name}, code, referenceAsOf, includeInactive);",
                f"{family.info_name}? {resolve_camel}AsOf(",
                "  String code,",
                "  DateTime on, {",
                "  bool includeInactive = false,",
                f"}}) => _resolve({index_name}, code, on, includeInactive);",
            ]
        )
        default_map = f"_{_camel(family.stem)}DefaultInfo"
        lines.extend(
            [
                f"final Map<String, {family.info_name}> {default_map} = Map.unmodifiable({{",
                f"  for (final code in {index_name}.keys)",
                f"    code: _resolve({index_name}, code, referenceAsOf, true)!,",
                "});",
                f"final Map<String, {family.enum_name}> _{_camel(family.stem)}IdentityByCode = Map.unmodifiable({{",
                f"  for (final value in {family.enum_name}.values) value.code: value,",
                "});",
                f"final List<{family.info_name}> {_camel(family.current_records_name)} = List.unmodifiable(",
                f"  {dart_records}.where((record) => record.isEffective()),",
                ");",
                f"final int {_camel(family.count_name)} = {index_name}.length;",
                f"final int {_camel(family.record_count_name)} = {dart_records}.length;",
                f"final int {_camel(family.current_count_name)} = {_camel(family.current_records_name)}.length;",
            ]
        )

    lines.extend(["", "final Map<String, List<AchReferenceInfo>> records = Map.unmodifiable({"])
    for family, _ in loaded:
        lines.append(f"  {_dart_string(family.dataset_id)}: {_camel(family.records_name)},")
    lines.extend(["});", "", "final Map<String, int> counts = Map.unmodifiable({"])
    for family, _ in loaded:
        lines.append(f"  {_dart_string(family.dataset_id)}: {_camel(family.count_name)},")
    lines.extend(["});", ""])
    return "\n".join(lines)


def write_or_check(path: Path, content: str, check: bool) -> bool:
    normalized = content.rstrip() + "\n"
    if check:
        return path.exists() and path.read_text(encoding="utf-8") == normalized
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalized, encoding="utf-8")
    return True


def generate(root: Path = ROOT, check: bool = False) -> list[Path]:
    """Generate this domain and return stale paths when ``check`` is true."""
    root = root.resolve()
    loaded = load_families(root)
    fingerprint = input_hash(root)
    outputs = {
        root / "packages/python/reffin_ach/src/reffin_ach/_generated.py": python_output(
            loaded, fingerprint
        ),
        root / "packages/typescript/reffin_ach/src/generated.ts": typescript_output(
            loaded, fingerprint
        ),
        root / "packages/flutter/reffin_ach/lib/src/generated.dart": dart_output(
            loaded, fingerprint
        ),
    }
    stale: list[Path] = []
    for path, content in outputs.items():
        if not write_or_check(path, content, check):
            stale.append(path)
    if not check:
        distinct = sum(len(EXPECTED_CODES[family.dataset_id]) for family, _ in loaded)
        physical = sum(len(rows) for _, rows in loaded)
        print(
            f"generated ACH: {physical:,} rows; {distinct:,} identifiers; "
            f"input {fingerprint[:12]}"
        )
    elif not stale:
        print("verified ACH: 167 rows; 166 identifiers")
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
