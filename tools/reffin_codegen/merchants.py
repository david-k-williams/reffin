#!/usr/bin/env python3
"""Generate the Reffin Merchants data and language packages."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MERCHANTS_DIR = ROOT / "data" / "merchants"
GROUPS_PATH = MERCHANTS_DIR / "groups.csv"
SOURCES_PATH = MERCHANTS_DIR / "sources.csv"
VENDORS_DIR = MERCHANTS_DIR / "vendors"


@dataclass(frozen=True)
class Group:
    id: str
    name: str
    material_symbol: str
    flutter_icon: str
    description: str


@dataclass(frozen=True)
class Record:
    vendor: str
    vendor_key: str
    mcc: str
    name: str
    group_id: str
    source_id: str


@dataclass(frozen=True)
class Source:
    id: str
    publisher: str
    title: str
    version: str
    effective_date: str
    retrieved_at: str
    url: str
    format: str
    license: str
    redistribution: str
    status: str
    sha256: str
    notes: str


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        return list(csv.DictReader(stream))


def load_groups() -> dict[str, Group]:
    groups = {
        row["group_id"]: Group(
            id=row["group_id"],
            name=row["name"],
            material_symbol=row["material_symbol"],
            flutter_icon=row["flutter_icon"],
            description=row["description"],
        )
        for row in read_csv(GROUPS_PATH)
    }
    if not groups or len(groups) != len(read_csv(GROUPS_PATH)):
        raise ValueError("groups.csv contains an empty or duplicate group_id")
    return groups


def load_sources() -> list[Source]:
    rows = read_csv(SOURCES_PATH)
    required = (
        "source_id",
        "publisher",
        "title",
        "version",
        "effective_date",
        "retrieved_at",
        "url",
        "format",
        "license",
        "redistribution",
        "status",
        "notes",
    )
    sources: list[Source] = []
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        if any(not row.get(field) for field in required):
            raise ValueError(f"{SOURCES_PATH}:{index}: missing required source metadata")
        source_id = row["source_id"]
        if source_id in seen or not re.fullmatch(r"[a-z][a-z0-9_]+", source_id):
            raise ValueError(f"{SOURCES_PATH}:{index}: invalid or duplicate source_id")
        seen.add(source_id)
        sources.append(
            Source(
                id=source_id,
                publisher=row["publisher"],
                title=row["title"],
                version=row["version"],
                effective_date=row["effective_date"],
                retrieved_at=row["retrieved_at"],
                url=row["url"],
                format=row["format"],
                license=row["license"],
                redistribution=row["redistribution"],
                status=row["status"],
                sha256=row["sha256"],
                notes=row["notes"],
            )
        )
    if not sources:
        raise ValueError(f"{SOURCES_PATH}: no sources")
    return sources


def classify_mcc(mcc: str, vendor_key: str, vendor: str = "") -> str:
    """Map an MCC to an original, presentation-oriented broad group."""
    if not mcc:
        return {
            "marketplaces": "general_retail",
            "truck_stop_iteration": "automotive",
        }.get(vendor_key, "other")

    vendor_overrides = {
        ("american_express", "3998"): "transportation",
        ("american_express", "4733"): "entertainment",
        ("american_express", "7013"): "real_estate",
        ("american_express", "7280"): "healthcare",
        ("american_express", "8912"): "home_and_garden",
    }
    if override := vendor_overrides.get((vendor, mcc)):
        return override

    number = int(mcc)
    project_overrides = {
        "1437": "nonprofit_and_membership",
        "2842": "wholesale",
        "5046": "wholesale",
        "5262": "general_retail",
        "5733": "specialty_retail",
        "5735": "specialty_retail",
        "5960": "financial_services",
        "7276": "professional_services",
        "7511": "automotive",
        "7623": "repair_services",
        "7629": "repair_services",
    }
    if override := project_overrides.get(mcc):
        return override
    if number in range(3000, 3351) or mcc in {"4511", "4582"}:
        return "air_travel"
    if 3351 <= number <= 3500 or mcc in {"7512", "7513", "7519"}:
        return "car_rental"
    if 3501 <= number <= 3999 or mcc in {"7011", "7012", "7032", "7033"}:
        return "lodging"
    if mcc == "4119" or 8011 <= number <= 8099 or mcc == "9702":
        return "healthcare"
    if mcc in {"5047", "5048", "5122", "5912", "5975", "5976"}:
        return "health_and_pharmacy"
    if mcc in {"4829"} or 6000 <= number <= 6999:
        return "real_estate" if mcc == "6513" else "financial_services"
    if mcc in {"4812", "4813", "4814", "4815", "4816", "4821", "4899"}:
        return "telecommunications"
    if mcc == "4900":
        return "utilities"
    if mcc in {
        "4011",
        "4111",
        "4112",
        "4121",
        "4131",
        "4214",
        "4215",
        "4225",
        "4411",
        "4457",
        "4468",
        "4722",
        "4784",
        "4789",
        "7523",
    }:
        return "transportation"
    if mcc in {"5172", "5511", "5521", "5531", "5532", "5533", "5541", "5542", "5551", "5552", "5561", "5571", "5592", "5598", "5599", "5983"}:
        return "automotive"
    if 7531 <= number <= 7549:
        return "automotive"
    if mcc in {"5044", "5045", "5065", "5732", "5734", "5946", "5997", "7622"}:
        return "electronics"
    if mcc in {"5021", "5039", "5072", "5074", "5193", "5198", "5200", "5211", "5231", "5251", "5261", "5271", "5712", "5713", "5714", "5718", "5719", "5722", "5996"}:
        return "home_and_garden"
    if mcc in {"5411", "5422", "5441", "5451", "5462", "5499"}:
        return "grocery"
    if 5611 <= number <= 5699:
        return "apparel"
    if 5811 <= number <= 5814 or mcc == "5921":
        return "food_and_drink"
    if 5815 <= number <= 5818:
        return "digital_goods"
    if 5300 <= number <= 5399 or mcc == "5432":
        return "general_retail"
    if mcc == "5715":
        return "wholesale"
    if 5700 <= number <= 5999:
        return "specialty_retail"
    if 5000 <= number <= 5299:
        return "wholesale"
    if 7210 <= number <= 7299:
        return "personal_services"
    if 7311 <= number <= 7399:
        return "business_services"
    if 7622 <= number <= 7699:
        return "repair_services"
    if 7800 <= number <= 7999:
        return "entertainment"
    if 8211 <= number <= 8351:
        return "education"
    if mcc in {"8398", "8641", "8651", "8661", "8675", "8699"}:
        return "nonprofit_and_membership"
    if mcc in {"8111", "8734", "8911", "8931", "8999"} or 8100 <= number <= 8999:
        return "professional_services"
    if 9000 <= number <= 9699:
        return "government"
    if number < 1500:
        return "agriculture"
    if 1500 <= number <= 1999:
        return "construction"
    if 2000 <= number <= 2999:
        return "business_services"
    if 4000 <= number <= 4799:
        return "transportation"
    if 4800 <= number <= 4999:
        return "utilities"
    return "other"


def load_records(groups: dict[str, Group], sources: list[Source]) -> list[Record]:
    sources_by_id = {source.id: source for source in sources}
    records: list[Record] = []
    seen_vendor_keys: set[tuple[str, str]] = set()
    seen_vendor_mccs: set[tuple[str, str]] = set()
    for path in sorted(VENDORS_DIR.glob("*.csv")):
        vendor = path.stem
        for row in read_csv(path):
            mcc = row["mcc"]
            if mcc and not re.fullmatch(r"\d{4}", mcc):
                raise ValueError(f"{path}: invalid MCC {mcc!r}")
            source = sources_by_id.get(row["source_id"])
            if source is None:
                raise ValueError(f"{path}: unknown source_id {row['source_id']!r}")
            if source.status not in {"imported", "imported_private_only"}:
                raise ValueError(
                    f"{path}: source {source.id!r} with status {source.status!r} "
                    "cannot drive generated records"
                )
            vendor_key = row["vendor_key"]
            key = (vendor, vendor_key)
            if key in seen_vendor_keys:
                raise ValueError(f"duplicate vendor key: {vendor}:{vendor_key}")
            seen_vendor_keys.add(key)
            if mcc:
                mcc_key = (vendor, mcc)
                if mcc_key in seen_vendor_mccs:
                    raise ValueError(f"duplicate vendor MCC: {vendor}:{mcc}")
                seen_vendor_mccs.add(mcc_key)
            group_id = classify_mcc(mcc, vendor_key, vendor)
            if group_id not in groups:
                raise ValueError(f"unknown group generated for {vendor_key}: {group_id}")
            records.append(
                Record(
                    vendor=vendor,
                    vendor_key=vendor_key,
                    mcc=mcc,
                    name=row["name"],
                    group_id=group_id,
                    source_id=row["source_id"],
                )
            )
    records.sort(key=lambda row: (row.vendor, row.mcc == "", row.mcc, row.vendor_key))
    if not records:
        raise ValueError("no vendor CSV records found")
    return records


def input_hash() -> str:
    digest = hashlib.sha256()
    for path in [GROUPS_PATH, SOURCES_PATH, *sorted(VENDORS_DIR.glob("*.csv"))]:
        digest.update(path.relative_to(ROOT).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def words(value: str) -> list[str]:
    return [part for part in re.split(r"[^A-Za-z0-9]+", value) if part]


def pascal(value: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in words(value))


def camel(value: str) -> str:
    result = pascal(value)
    return result[:1].lower() + result[1:]


def py_string(value: str) -> str:
    return repr(value)


def ts_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def dart_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace("'", "\\'").replace("$", "\\$")
    escaped = escaped.replace("\r", "\\r").replace("\n", "\\n")
    return f"'{escaped}'"


def normalized_csv(records: list[Record]) -> str:
    stream = io.StringIO(newline="")
    fieldnames = ("vendor", "vendor_key", "mcc", "name", "group_id", "source_id")
    writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for record in records:
        writer.writerow(record.__dict__)
    return stream.getvalue()


def python_output(
    groups: dict[str, Group],
    records: list[Record],
    sources: list[Source],
    fingerprint: str,
) -> str:
    vendors = sorted({record.vendor for record in records})
    codes = sorted({record.mcc for record in records if record.mcc})
    lines = [
        '"""Generated MCC catalog. Do not edit by hand."""',
        "",
        f"# Input SHA-256: {fingerprint}",
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "from enum import Enum",
        "from typing import Final",
        "",
        f"DATA_FINGERPRINT: Final[str] = {py_string(fingerprint)}",
        "",
        "class MccVendor(str, Enum):",
    ]
    lines.extend(f"    {vendor.upper()} = {py_string(vendor)}" for vendor in vendors)
    lines.extend(
        [
            "",
            "    @classmethod",
            "    def try_parse(cls, value: str) -> MccVendor | None:",
            "        return _VENDOR_BY_ID.get(value)",
            "",
            "",
            "class MccGroup(Enum):",
        ]
    )
    for group in groups.values():
        lines.append(
            f"    {group.id.upper()} = ({py_string(group.id)}, {py_string(group.name)}, "
            f"{py_string(group.material_symbol)}, {py_string(group.description)})"
        )
    lines.extend(
        [
            "",
            "    def __new__(cls, value: str, label: str, material_symbol: str, description: str) -> MccGroup:",
            "        member = object.__new__(cls)",
            "        member._value_ = value",
            "        member.label = label",
            "        member.material_symbol = material_symbol",
            "        member.description = description",
            "        return member",
            "",
            "    label: str",
            "    material_symbol: str",
            "    description: str",
            "",
            "    @classmethod",
            "    def try_parse(cls, value: str) -> MccGroup | None:",
            "        return _GROUP_BY_ID.get(value)",
            "",
            "",
            "class Mcc(str, Enum):",
        ]
    )
    lines.extend(f"    MCC_{code} = {py_string(code)}" for code in codes)
    lines.extend(
        [
            "",
            "    @classmethod",
            "    def try_parse(cls, code: str) -> Mcc | None:",
            "        return _MCC_BY_CODE.get(code)",
            "",
            "    def resolve(self, vendor: MccVendor) -> MccDetails | None:",
            "        return resolve_mcc(self, vendor)",
            "",
            "",
            "@dataclass(frozen=True, slots=True)",
            "class MccSource:",
            "    id: str",
            "    publisher: str",
            "    title: str",
            "    version: str",
            "    effective_date: str",
            "    retrieved_at: str",
            "    url: str",
            "    format: str",
            "    license: str",
            "    redistribution: str",
            "    status: str",
            "    sha256: str | None",
            "    notes: str",
            "",
            "",
            "@dataclass(frozen=True, slots=True)",
            "class MccDetails:",
            "    vendor: MccVendor",
            "    vendor_key: str",
            "    mcc: Mcc | None",
            "    name: str",
            "    group: MccGroup",
            "    source_id: str",
            "",
            "    @property",
            "    def icon_key(self) -> str:",
            "        return self.group.material_symbol",
            "",
            "    @property",
            "    def source(self) -> MccSource:",
            "        return _SOURCE_BY_ID[self.source_id]",
            "",
            "",
            "_SOURCES: Final[tuple[MccSource, ...]] = (",
        ]
    )
    for source in sources:
        sha256 = py_string(source.sha256) if source.sha256 else "None"
        lines.append(
            "    MccSource("
            f"{py_string(source.id)}, {py_string(source.publisher)}, {py_string(source.title)}, "
            f"{py_string(source.version)}, {py_string(source.effective_date)}, "
            f"{py_string(source.retrieved_at)}, {py_string(source.url)}, "
            f"{py_string(source.format)}, {py_string(source.license)}, "
            f"{py_string(source.redistribution)}, {py_string(source.status)}, {sha256}, "
            f"{py_string(source.notes)}),"
        )
    lines.extend(
        [
            ")",
            "",
            "_RECORDS: Final[tuple[MccDetails, ...]] = (",
        ]
    )
    for record in records:
        mcc_value = f"Mcc.MCC_{record.mcc}" if record.mcc else "None"
        lines.append(
            "    MccDetails("
            f"MccVendor.{record.vendor.upper()}, {py_string(record.vendor_key)}, {mcc_value}, "
            f"{py_string(record.name)}, MccGroup.{record.group_id.upper()}, "
            f"{py_string(record.source_id)}),"
        )
    lines.extend(
        [
            ")",
            "",
            "_MCC_BY_CODE: Final = {mcc.value: mcc for mcc in Mcc}",
            "_VENDOR_BY_ID: Final = {vendor.value: vendor for vendor in MccVendor}",
            "_GROUP_BY_ID: Final = {group.value: group for group in MccGroup}",
            "_SOURCE_BY_ID: Final = {source.id: source for source in _SOURCES}",
            "_BY_VENDOR_KEY: Final = {(item.vendor, item.vendor_key): item for item in _RECORDS}",
            "_BY_MCC: Final = {(item.vendor, item.mcc.value): item for item in _RECORDS if item.mcc}",
            "_RECORD_LISTS_BY_MCC: dict[str, list[MccDetails]] = {}",
            "for _item in _RECORDS:",
            "    if _item.mcc is not None:",
            "        _RECORD_LISTS_BY_MCC.setdefault(_item.mcc.value, []).append(_item)",
            "_RECORDS_BY_MCC: Final = {code: tuple(items) for code, items in _RECORD_LISTS_BY_MCC.items()}",
            "del _RECORD_LISTS_BY_MCC, _item",
            "ALL_RECORDS: Final = _RECORDS",
            "ALL_SOURCES: Final = _SOURCES",
            "",
            "",
            "def resolve_mcc(code: str | Mcc, vendor: MccVendor) -> MccDetails | None:",
            "    raw_code = code.value if isinstance(code, Mcc) else code",
            "    if not isinstance(raw_code, str) or not raw_code.isdigit() or len(raw_code) != 4:",
            "        return None",
            "    return _BY_MCC.get((vendor, raw_code))",
            "",
            "",
            "def resolve_vendor_key(vendor: MccVendor, key: str) -> MccDetails | None:",
            "    return _BY_VENDOR_KEY.get((vendor, key))",
            "",
            "",
            "def resolve_source(source_id: str) -> MccSource | None:",
            "    return _SOURCE_BY_ID.get(source_id)",
            "",
            "",
            "def records_for_mcc(code: str | Mcc) -> tuple[MccDetails, ...]:",
            "    raw_code = code.value if isinstance(code, Mcc) else code",
            "    return _RECORDS_BY_MCC.get(raw_code, ())",
            "",
        ]
    )
    return "\n".join(lines)


def typescript_output(
    groups: dict[str, Group],
    records: list[Record],
    sources: list[Source],
    fingerprint: str,
) -> str:
    vendors = sorted({record.vendor for record in records})
    codes = sorted({record.mcc for record in records if record.mcc})
    lines = [
        "// Generated MCC catalog. Do not edit by hand.",
        f"// Input SHA-256: {fingerprint}",
        f"export const DATA_FINGERPRINT = {ts_string(fingerprint)};",
        "",
        "export const MccVendor = Object.freeze({",
    ]
    lines.extend(f"  {pascal(vendor)}: {ts_string(vendor)}," for vendor in vendors)
    lines.extend(
        [
            "} as const);",
            "export type MccVendor = (typeof MccVendor)[keyof typeof MccVendor];",
            "",
            "export const MccGroup = Object.freeze({",
        ]
    )
    lines.extend(f"  {pascal(group.id)}: {ts_string(group.id)}," for group in groups.values())
    lines.extend(
        [
            "} as const);",
            "export type MccGroup = (typeof MccGroup)[keyof typeof MccGroup];",
            "",
            "export const Mcc = Object.freeze({",
        ]
    )
    lines.extend(f"  MCC_{code}: {ts_string(code)}," for code in codes)
    lines.extend(
        [
            "} as const);",
            "export type Mcc = (typeof Mcc)[keyof typeof Mcc];",
            "",
            "export interface MccGroupInfo {",
            "  readonly id: MccGroup;",
            "  readonly name: string;",
            "  readonly materialSymbol: string;",
            "  readonly description: string;",
            "}",
            "",
            "export interface MccDetails {",
            "  readonly vendor: MccVendor;",
            "  readonly vendorKey: string;",
            "  readonly mcc: Mcc | null;",
            "  readonly name: string;",
            "  readonly group: MccGroup;",
            "  readonly sourceId: string;",
            "}",
            "",
            "export interface MccSource {",
            "  readonly id: string;",
            "  readonly publisher: string;",
            "  readonly title: string;",
            "  readonly version: string;",
            "  readonly effectiveDate: string;",
            "  readonly retrievedAt: string;",
            "  readonly url: string;",
            "  readonly format: string;",
            "  readonly license: string;",
            "  readonly redistribution: string;",
            "  readonly status: string;",
            "  readonly sha256: string | null;",
            "  readonly notes: string;",
            "}",
            "",
            "const groupInfoById: Readonly<Record<MccGroup, MccGroupInfo>> = Object.freeze({",
        ]
    )
    for group in groups.values():
        lines.append(
            f"  [MccGroup.{pascal(group.id)}]: Object.freeze({{ id: MccGroup.{pascal(group.id)}, "
            f"name: {ts_string(group.name)}, materialSymbol: {ts_string(group.material_symbol)}, "
            f"description: {ts_string(group.description)} }}),"
        )
    lines.extend(
        [
            "});",
            "",
            "export const mccSources: readonly MccSource[] = Object.freeze([",
        ]
    )
    for source in sources:
        sha256 = ts_string(source.sha256) if source.sha256 else "null"
        lines.append(
            "  Object.freeze({ "
            f"id: {ts_string(source.id)}, publisher: {ts_string(source.publisher)}, "
            f"title: {ts_string(source.title)}, version: {ts_string(source.version)}, "
            f"effectiveDate: {ts_string(source.effective_date)}, retrievedAt: {ts_string(source.retrieved_at)}, "
            f"url: {ts_string(source.url)}, format: {ts_string(source.format)}, "
            f"license: {ts_string(source.license)}, redistribution: {ts_string(source.redistribution)}, "
            f"status: {ts_string(source.status)}, sha256: {sha256}, notes: {ts_string(source.notes)} "
            "}),"
        )
    lines.extend(
        [
            "]);",
            "const sourceById = new Map(mccSources.map((source) => [source.id, source]));",
            "",
            "function detail(",
            "  vendor: MccVendor, vendorKey: string, mcc: Mcc | null, name: string,",
            "  group: MccGroup, sourceId: string,",
            "): MccDetails {",
            "  return Object.freeze({ vendor, vendorKey, mcc, name, group, sourceId });",
            "}",
            "",
            "export const mccRecords: readonly MccDetails[] = Object.freeze([",
        ]
    )
    for record in records:
        mcc_value = f"Mcc.MCC_{record.mcc}" if record.mcc else "null"
        lines.append(
            f"  detail(MccVendor.{pascal(record.vendor)}, {ts_string(record.vendor_key)}, "
            f"{mcc_value}, {ts_string(record.name)}, MccGroup.{pascal(record.group_id)}, "
            f"{ts_string(record.source_id)}),"
        )
    lines.extend(
        [
            "]);",
            "",
            "const byVendorKey = new Map(mccRecords.map((item) => [`${item.vendor}:${item.vendorKey}`, item]));",
            "const byMcc = new Map(",
            "  mccRecords.filter((item): item is MccDetails & { mcc: Mcc } => item.mcc !== null)",
            "    .map((item) => [`${item.vendor}:${item.mcc}`, item]),",
            ");",
            "const recordsByMcc = new Map<string, MccDetails[]>();",
            "for (const item of mccRecords) {",
            "  if (item.mcc === null) continue;",
            "  const values = recordsByMcc.get(item.mcc) ?? [];",
            "  values.push(item);",
            "  recordsByMcc.set(item.mcc, values);",
            "}",
            "for (const [code, values] of recordsByMcc) recordsByMcc.set(code, Object.freeze(values) as MccDetails[]);",
            "",
            "export function isMcc(code: string): code is Mcc {",
            "  return /^[0-9]{4}$/.test(code) && Object.values(Mcc).includes(code as Mcc);",
            "}",
            "",
            "export function isMccVendor(value: string): value is MccVendor {",
            "  return Object.values(MccVendor).includes(value as MccVendor);",
            "}",
            "",
            "export function isMccGroup(value: string): value is MccGroup {",
            "  return Object.values(MccGroup).includes(value as MccGroup);",
            "}",
            "",
            "export function mccGroupInfo(group: MccGroup): MccGroupInfo {",
            "  return groupInfoById[group];",
            "}",
            "",
            "export function resolveMcc(code: string, vendor: MccVendor): MccDetails | undefined {",
            "  if (!/^[0-9]{4}$/.test(code)) return undefined;",
            "  return byMcc.get(`${vendor}:${code}`);",
            "}",
            "",
            "export function resolveVendorKey(vendor: MccVendor, key: string): MccDetails | undefined {",
            "  return byVendorKey.get(`${vendor}:${key}`);",
            "}",
            "",
            "export function resolveMccSource(sourceId: string): MccSource | undefined {",
            "  return sourceById.get(sourceId);",
            "}",
            "",
            "export function sourceForMccDetails(details: MccDetails): MccSource | undefined {",
            "  return resolveMccSource(details.sourceId);",
            "}",
            "",
            "export function recordsForMcc(code: string): readonly MccDetails[] {",
            "  if (!/^[0-9]{4}$/.test(code)) return [];",
            "  return recordsByMcc.get(code) ?? [];",
            "}",
            "",
            "export function materialSymbolForMcc(code: string, vendor: MccVendor): string | undefined {",
            "  const item = resolveMcc(code, vendor);",
            "  return item ? mccGroupInfo(item.group).materialSymbol : undefined;",
            "}",
            "",
        ]
    )
    return "\n".join(lines)


def dart_output(
    groups: dict[str, Group],
    records: list[Record],
    sources: list[Source],
    fingerprint: str,
) -> str:
    vendors = sorted({record.vendor for record in records})
    codes = sorted({record.mcc for record in records if record.mcc})
    lines = [
        "// Generated MCC catalog. Do not edit by hand.",
        f"// Input SHA-256: {fingerprint}",
        "",
        "import 'package:flutter/material.dart';",
        "",
        f"const String dataFingerprint = {dart_string(fingerprint)};",
        "",
        "enum MccVendor {",
    ]
    for index, vendor in enumerate(vendors):
        suffix = ";" if index == len(vendors) - 1 else ","
        lines.append(f"  {camel(vendor)}({dart_string(vendor)}){suffix}")
    lines.extend(
        [
            "",
            "  const MccVendor(this.id);",
            "  final String id;",
            "  static MccVendor? tryParse(String id) => _vendorById[id];",
            "}",
            "",
            "enum MccGroup {",
        ]
    )
    group_values = list(groups.values())
    for index, group in enumerate(group_values):
        suffix = ";" if index == len(group_values) - 1 else ","
        lines.append(
            f"  {camel(group.id)}({dart_string(group.id)}, {dart_string(group.name)}, "
            f"{dart_string(group.description)}, Icons.{group.flutter_icon}){suffix}"
        )
    lines.extend(
        [
            "",
            "  const MccGroup(this.id, this.label, this.description, this.icon);",
            "  final String id;",
            "  final String label;",
            "  final String description;",
            "  final IconData icon;",
            "  static MccGroup? tryParse(String id) => _groupById[id];",
            "}",
            "",
            "enum Mcc {",
        ]
    )
    for index, code in enumerate(codes):
        suffix = ";" if index == len(codes) - 1 else ","
        lines.append(f"  mcc{code}({dart_string(code)}){suffix}")
    lines.extend(
        [
            "",
            "  const Mcc(this.code);",
            "  final String code;",
            "",
            "  static Mcc? tryParse(String code) => _mccByCode[code];",
            "  MccDetails? resolve(MccVendor vendor) => resolveMcc(code, vendor);",
            "}",
            "",
            "@immutable",
            "class MccSource {",
            "  const MccSource({",
            "    required this.id,",
            "    required this.publisher,",
            "    required this.title,",
            "    required this.version,",
            "    required this.effectiveDate,",
            "    required this.retrievedAt,",
            "    required this.url,",
            "    required this.format,",
            "    required this.license,",
            "    required this.redistribution,",
            "    required this.status,",
            "    required this.sha256,",
            "    required this.notes,",
            "  });",
            "  final String id;",
            "  final String publisher;",
            "  final String title;",
            "  final String version;",
            "  final String effectiveDate;",
            "  final String retrievedAt;",
            "  final String url;",
            "  final String format;",
            "  final String license;",
            "  final String redistribution;",
            "  final String status;",
            "  final String? sha256;",
            "  final String notes;",
            "}",
            "",
            "const List<MccSource> mccSources = [",
        ]
    )
    for source in sources:
        sha256 = dart_string(source.sha256) if source.sha256 else "null"
        lines.append(
            "  MccSource("
            f"id: {dart_string(source.id)}, publisher: {dart_string(source.publisher)}, "
            f"title: {dart_string(source.title)}, version: {dart_string(source.version)}, "
            f"effectiveDate: {dart_string(source.effective_date)}, "
            f"retrievedAt: {dart_string(source.retrieved_at)}, url: {dart_string(source.url)}, "
            f"format: {dart_string(source.format)}, license: {dart_string(source.license)}, "
            f"redistribution: {dart_string(source.redistribution)}, status: {dart_string(source.status)}, "
            f"sha256: {sha256}, notes: {dart_string(source.notes)}),"
        )
    lines.extend(
        [
            "];",
            "final Map<String, MccSource> _sourceById = {",
            "  for (final source in mccSources) source.id: source,",
            "};",
            "MccSource? resolveMccSource(String sourceId) => _sourceById[sourceId];",
            "final Map<String, MccVendor> _vendorById = {for (final item in MccVendor.values) item.id: item};",
            "final Map<String, MccGroup> _groupById = {for (final item in MccGroup.values) item.id: item};",
            "",
            "@immutable",
            "class MccDetails {",
            "  const MccDetails({",
            "    required this.vendor,",
            "    required this.vendorKey,",
            "    required this.mcc,",
            "    required this.name,",
            "    required this.group,",
            "    required this.sourceId,",
            "  });",
            "",
            "  final MccVendor vendor;",
            "  final String vendorKey;",
            "  final Mcc? mcc;",
            "  final String name;",
            "  final MccGroup group;",
            "  final String sourceId;",
            "  IconData get icon => group.icon;",
            "  MccSource get source => _sourceById[sourceId]!;",
            "}",
            "",
            "const Map<String, Mcc> _mccByCode = {",
        ]
    )
    lines.extend(f"  {dart_string(code)}: Mcc.mcc{code}," for code in codes)
    lines.extend(["};", "", "const Map<String, MccDetails> _byVendorKey = {"])
    for record in records:
        record_key = f"{record.vendor}:{record.vendor_key}"
        mcc_value = f"Mcc.mcc{record.mcc}" if record.mcc else "null"
        lines.append(
            f"  {dart_string(record_key)}: MccDetails("
            f"vendor: MccVendor.{camel(record.vendor)}, vendorKey: {dart_string(record.vendor_key)}, "
            f"mcc: {mcc_value}, name: {dart_string(record.name)}, "
            f"group: MccGroup.{camel(record.group_id)}, "
            f"sourceId: {dart_string(record.source_id)}),"
        )
    lines.extend(
        [
            "};",
            "final List<MccDetails> mccRecords = List.unmodifiable(_byVendorKey.values);",
            "",
            "final Map<String, MccDetails> _byMcc = {",
            "  for (final item in _byVendorKey.values)",
            "    if (item.mcc != null) '${item.vendor.id}:${item.mcc!.code}': item,",
        ]
    )
    lines.extend(
        [
            "};",
            "",
            "MccDetails? resolveMcc(String code, MccVendor vendor) {",
            "  if (!RegExp(r'^[0-9]{4}$').hasMatch(code)) return null;",
            "  return _byMcc['${vendor.id}:$code'];",
            "}",
            "",
            "MccDetails? resolveVendorKey(MccVendor vendor, String key) {",
            "  return _byVendorKey['${vendor.id}:$key'];",
            "}",
            "",
            "List<MccDetails> recordsForMcc(String code) {",
            "  if (!RegExp(r'^[0-9]{4}$').hasMatch(code)) return const [];",
            "  final matches = <MccDetails>[];",
            "  for (final vendor in MccVendor.values) {",
            "    final item = _byMcc['${vendor.id}:$code'];",
            "    if (item != null) matches.add(item);",
            "  }",
            "  return List.unmodifiable(matches);",
            "}",
            "",
        ]
    )
    return "\n".join(lines)


def write_or_check(path: Path, content: str, check: bool) -> bool:
    content = content.rstrip() + "\n"
    if check:
        return path.exists() and path.read_text(encoding="utf-8") == content
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def generate(check: bool = False) -> list[Path]:
    """Generate this domain and return any stale paths in check mode."""
    groups = load_groups()
    sources = load_sources()
    records = load_records(groups, sources)
    fingerprint = input_hash()
    outputs = {
        MERCHANTS_DIR / "normalized" / "mcc_catalog.csv": normalized_csv(records),
        ROOT / "packages" / "python" / "reffin_merchants" / "src" / "reffin_merchants" / "_generated.py": python_output(groups, records, sources, fingerprint),
        ROOT / "packages" / "typescript" / "reffin_merchants" / "src" / "generated.ts": typescript_output(groups, records, sources, fingerprint),
        ROOT / "packages" / "flutter" / "reffin_merchants" / "lib" / "src" / "generated.dart": dart_output(groups, records, sources, fingerprint),
    }
    stale = [path for path, content in outputs.items() if not write_or_check(path, content, check)]
    action = "verified" if check else "generated"
    print(f"{action} {len(records)} vendor records, {len({r.mcc for r in records if r.mcc})} MCCs")
    return stale


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are stale")
    args = parser.parse_args()
    stale = generate(check=args.check)
    if stale:
        for path in stale:
            print(f"stale: {path.relative_to(ROOT)}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
