#!/usr/bin/env python3
"""Generate the Reffin Cards packages from the canonical CSV vocabularies."""

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


@dataclass(frozen=True, slots=True)
class Vocabulary:
    filename: str
    class_name: str
    id_column: str
    constant_stem: str
    ts_records_name: str
    ts_count_name: str
    dart_records_name: str
    dart_count_name: str
    has_description: bool = True
    has_brand_asset_key: bool = False

    @property
    def dataset_id(self) -> str:
        return self.filename.removesuffix(".csv")


@dataclass(frozen=True, slots=True)
class Record:
    id: str
    name: str
    material_symbol: str
    description: str | None = None
    brand_asset_key: str | None = None


VOCABULARIES = (
    Vocabulary(
        "card_networks.csv",
        "CardNetwork",
        "network_id",
        "CARD_NETWORK",
        "cardNetworkRecords",
        "cardNetworkCount",
        "cardNetworkRecords",
        "cardNetworkCount",
        has_description=False,
        has_brand_asset_key=True,
    ),
    Vocabulary(
        "form_factors.csv",
        "FormFactor",
        "id",
        "FORM_FACTOR",
        "formFactorRecords",
        "formFactorCount",
        "formFactorRecords",
        "formFactorCount",
    ),
    Vocabulary(
        "funding_types.csv",
        "FundingType",
        "id",
        "FUNDING_TYPE",
        "fundingTypeRecords",
        "fundingTypeCount",
        "fundingTypeRecords",
        "fundingTypeCount",
    ),
    Vocabulary(
        "payment_method_families.csv",
        "PaymentMethodFamily",
        "id",
        "PAYMENT_METHOD_FAMILY",
        "paymentMethodFamilyRecords",
        "paymentMethodFamilyCount",
        "paymentMethodFamilyRecords",
        "paymentMethodFamilyCount",
    ),
    Vocabulary(
        "payment_outcomes.csv",
        "PaymentOutcome",
        "id",
        "PAYMENT_OUTCOME",
        "paymentOutcomeRecords",
        "paymentOutcomeCount",
        "paymentOutcomeRecords",
        "paymentOutcomeCount",
    ),
    Vocabulary(
        "product_classes.csv",
        "ProductClass",
        "id",
        "PRODUCT_CLASS",
        "productClassRecords",
        "productClassCount",
        "productClassRecords",
        "productClassCount",
    ),
    Vocabulary(
        "transaction_channels.csv",
        "TransactionChannel",
        "id",
        "TRANSACTION_CHANNEL",
        "transactionChannelRecords",
        "transactionChannelCount",
        "transactionChannelRecords",
        "transactionChannelCount",
    ),
    Vocabulary(
        "verification_outcomes.csv",
        "VerificationOutcome",
        "id",
        "VERIFICATION_OUTCOME",
        "verificationOutcomeRecords",
        "verificationOutcomeCount",
        "verificationOutcomeRecords",
        "verificationOutcomeCount",
    ),
)


# Every source symbol must be deliberately mapped to a real Flutter Material icon.
FLUTTER_ICONS = {
    "account_balance": "account_balance",
    "account_balance_wallet": "account_balance_wallet",
    "apps": "apps",
    "block": "block",
    "business": "business",
    "calendar_month": "calendar_month",
    "cancel": "cancel",
    "check_circle": "check_circle",
    "confirmation_number": "confirmation_number",
    "credit_card": "credit_card",
    "credit_score": "credit_score",
    "currency_exchange": "currency_exchange",
    "devices": "devices",
    "devices_other": "devices_other",
    "error_outline": "error_outline",
    "help": "help",
    "help_outline": "help_outline",
    "horizontal_rule": "horizontal_rule",
    "language": "language",
    "mail": "mail",
    "more_horiz": "more_horiz",
    "payments": "payments",
    "person": "person",
    "phone_in_talk": "phone_in_talk",
    "point_of_sale": "point_of_sale",
    "receipt_long": "receipt_long",
    "redeem": "redeem",
    "remove_circle_outline": "remove_circle_outline",
    "rule": "rule",
    "schedule": "schedule",
    "skip_next": "skip_next",
    "smartphone": "smartphone",
    "sync_alt": "sync_alt",
    "undo": "undo",
    "verified": "verified",
}


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


def _read_vocabulary(root: Path, vocabulary: Vocabulary) -> list[Record]:
    path = root / "data" / "cards" / vocabulary.filename
    expected_columns = [vocabulary.id_column, "name", "material_symbol"]
    if vocabulary.has_description:
        expected_columns.append("description")
    if vocabulary.has_brand_asset_key:
        expected_columns.append("brand_asset_key")

    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != expected_columns:
            raise ValueError(
                f"{path}: expected columns {expected_columns!r}, got {reader.fieldnames!r}"
            )
        rows = list(reader)

    if not rows:
        raise ValueError(f"{path}: vocabulary must not be empty")

    records: list[Record] = []
    seen: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        identifier = row[vocabulary.id_column]
        if not re.fullmatch(r"[a-z][a-z0-9]*(?:_[a-z0-9]+)*", identifier):
            raise ValueError(f"{path}:{row_number}: invalid stable ID {identifier!r}")
        if identifier in seen:
            raise ValueError(f"{path}:{row_number}: duplicate ID {identifier!r}")
        seen.add(identifier)

        name = row["name"]
        material_symbol = row["material_symbol"]
        if not name or not material_symbol:
            raise ValueError(f"{path}:{row_number}: name and material_symbol are required")
        if material_symbol not in FLUTTER_ICONS:
            raise ValueError(
                f"{path}:{row_number}: material symbol {material_symbol!r} has no Flutter mapping"
            )

        description = row.get("description") or None
        if vocabulary.has_description and description is None:
            raise ValueError(f"{path}:{row_number}: description is required")
        brand_asset_key = row.get("brand_asset_key") or None
        if brand_asset_key is not None and not re.fullmatch(
            r"[a-z][a-z0-9]*(?:_[a-z0-9]+)*", brand_asset_key
        ):
            raise ValueError(f"{path}:{row_number}: invalid brand_asset_key {brand_asset_key!r}")

        records.append(
            Record(
                id=identifier,
                name=name,
                material_symbol=material_symbol,
                description=description,
                brand_asset_key=brand_asset_key,
            )
        )

    identifiers = [record.id for record in records]
    if identifiers != sorted(identifiers):
        raise ValueError(f"{path}: rows must be sorted by {vocabulary.id_column}")
    return records


def load_vocabularies(root: Path) -> list[tuple[Vocabulary, list[Record]]]:
    return [(vocabulary, _read_vocabulary(root, vocabulary)) for vocabulary in VOCABULARIES]


def input_hash(root: Path) -> str:
    digest = hashlib.sha256()
    cards_dir = root / "data" / "cards"
    for path in sorted(cards_dir.glob("*.csv")):
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def python_output(
    loaded: list[tuple[Vocabulary, list[Record]]], fingerprint: str
) -> str:
    lines = [
        '"""Generated card reference vocabularies. Do not edit by hand."""',
        "",
        f"# Input SHA-256: {fingerprint}",
        "from __future__ import annotations",
        "",
        "from enum import Enum",
        "from types import MappingProxyType",
        "from typing import Final, Mapping, Self",
        "",
        "",
        f"DATA_FINGERPRINT: Final = {py_string(fingerprint)}",
        "",
        "",
        "class _ReferenceEnum(Enum):",
        "    label: str",
        "",
        "    @property",
        "    def id(self) -> str:",
        "        return str(self.value)",
        "",
        "    @classmethod",
        "    def try_parse(cls, value: object) -> Self | None:",
        "        try:",
        "            return cls(value)",
        "        except (TypeError, ValueError):",
        "            return None",
    ]

    for vocabulary, records in loaded:
        lines.extend(["", "", f"class {vocabulary.class_name}(_ReferenceEnum):"])
        for record in records:
            values = [
                py_string(record.id),
                py_string(record.name),
                py_string(record.material_symbol),
            ]
            if vocabulary.has_description:
                assert record.description is not None
                values.append(py_string(record.description))
            if vocabulary.has_brand_asset_key:
                values.append(
                    "None"
                    if record.brand_asset_key is None
                    else py_string(record.brand_asset_key)
                )
            lines.append(f"    {record.id.upper()} = ({', '.join(values)})")

        parameters = [
            "identifier: str",
            "display_name: str",
            "material_symbol: str",
        ]
        if vocabulary.has_description:
            parameters.append("description: str")
        if vocabulary.has_brand_asset_key:
            parameters.append("brand_asset_key: str | None")
        lines.extend(
            [
                "",
                f"    def __new__(cls, {', '.join(parameters)}) -> {vocabulary.class_name}:",
                "        member = object.__new__(cls)",
                "        member._value_ = identifier",
                "        member.label = display_name",
                "        member.material_symbol = material_symbol",
            ]
        )
        if vocabulary.has_description:
            lines.append("        member.description = description")
        if vocabulary.has_brand_asset_key:
            lines.append("        member.brand_asset_key = brand_asset_key")
        lines.extend(["        return member", "", "    material_symbol: str"])
        if vocabulary.has_description:
            lines.append("    description: str")
        if vocabulary.has_brand_asset_key:
            lines.append("    brand_asset_key: str | None")

    lines.extend(["", ""])
    for vocabulary, _ in loaded:
        records_name = f"{vocabulary.constant_stem}_RECORDS"
        count_name = f"{vocabulary.constant_stem}_COUNT"
        lines.append(
            f"{records_name}: Final[tuple[{vocabulary.class_name}, ...]] = "
            f"tuple({vocabulary.class_name})"
        )
        lines.append(f"{count_name}: Final = len({records_name})")
    lines.extend(
        [
            "",
            "RECORDS: Final[Mapping[str, tuple[_ReferenceEnum, ...]]] = MappingProxyType({",
        ]
    )
    for vocabulary, _ in loaded:
        lines.append(
            f"    {py_string(vocabulary.dataset_id)}: "
            f"{vocabulary.constant_stem}_RECORDS,"
        )
    lines.extend(
        [
            "})",
            "COUNTS: Final[Mapping[str, int]] = MappingProxyType({",
        ]
    )
    for vocabulary, _ in loaded:
        lines.append(
            f"    {py_string(vocabulary.dataset_id)}: "
            f"{vocabulary.constant_stem}_COUNT,"
        )
    lines.extend(["})", ""])
    return "\n".join(lines)


def typescript_output(
    loaded: list[tuple[Vocabulary, list[Record]]], fingerprint: str
) -> str:
    lines = [
        "// Generated card reference vocabularies. Do not edit by hand.",
        f"// Input SHA-256: {fingerprint}",
        "",
        f"export const DATA_FINGERPRINT = {ts_string(fingerprint)} as const;",
        "",
        "export interface ReferenceValue {",
        "  readonly id: string;",
        "  readonly name: string;",
        "  readonly materialSymbol: string;",
        "}",
        "",
        "export interface DescribedReferenceValue extends ReferenceValue {",
        "  readonly description: string;",
        "}",
        "",
        "export interface CardNetworkValue extends ReferenceValue {",
        "  readonly brandAssetKey: string | null;",
        "}",
        "",
        "function reference<const T extends DescribedReferenceValue>(item: T): Readonly<T> {",
        "  return Object.freeze(item);",
        "}",
        "",
        "function network<const T extends CardNetworkValue>(item: T): Readonly<T> {",
        "  return Object.freeze(item);",
        "}",
        "",
        "function indexById<T extends ReferenceValue>(values: readonly T[]): ReadonlyMap<string, T> {",
        "  return new Map(values.map((item) => [item.id, item]));",
        "}",
    ]

    for vocabulary, records in loaded:
        constructor = "network" if vocabulary.has_brand_asset_key else "reference"
        lines.extend(["", f"export const {vocabulary.class_name} = Object.freeze({{"])
        for record in records:
            fields = [
                f"id: {ts_string(record.id)}",
                f"name: {ts_string(record.name)}",
                f"materialSymbol: {ts_string(record.material_symbol)}",
            ]
            if vocabulary.has_description:
                assert record.description is not None
                fields.append(f"description: {ts_string(record.description)}")
            if vocabulary.has_brand_asset_key:
                fields.append(
                    "brandAssetKey: null"
                    if record.brand_asset_key is None
                    else f"brandAssetKey: {ts_string(record.brand_asset_key)}"
                )
            lines.append(
                f"  {pascal(record.id)}: {constructor}({{ {', '.join(fields)} }}),"
            )
        lines.extend(
            [
                "});",
                f"export type {vocabulary.class_name} =",
                f"  (typeof {vocabulary.class_name})[keyof typeof {vocabulary.class_name}];",
                f"export type {vocabulary.class_name}Id = {vocabulary.class_name}[\"id\"];",
            ]
        )

    lines.append("")
    for vocabulary, _ in loaded:
        lines.append(
            f"export const {vocabulary.ts_records_name}: readonly {vocabulary.class_name}[] = "
            f"Object.freeze(Object.values({vocabulary.class_name}));"
        )
        lines.append(
            f"export const {vocabulary.ts_count_name} = {vocabulary.ts_records_name}.length;"
        )
        index_name = vocabulary.dart_records_name.removesuffix("Records") + "ById"
        lines.append(
            f"const {index_name} = indexById({vocabulary.ts_records_name});"
        )
        lines.append(
            f"export function tryParse{vocabulary.class_name}(id: string): "
            f"{vocabulary.class_name} | undefined {{"
        )
        lines.append(f"  return {index_name}.get(id);")
        lines.append("}")
        lines.append(
            f"export function is{vocabulary.class_name}Id(id: string): "
            f"id is {vocabulary.class_name}Id {{"
        )
        lines.append(f"  return {index_name}.has(id);")
        lines.extend(["}", ""])

    lines.extend(["export const records = Object.freeze({"])
    for vocabulary, _ in loaded:
        lines.append(f"  {camel(vocabulary.dataset_id)}: {vocabulary.ts_records_name},")
    lines.extend(["});", "", "export const counts = Object.freeze({"])
    for vocabulary, _ in loaded:
        lines.append(f"  {camel(vocabulary.dataset_id)}: {vocabulary.ts_count_name},")
    lines.extend(
        [
            "});",
            "",
            "export const RECORDS = records;",
            "export const COUNTS = counts;",
            "",
        ]
    )
    return "\n".join(lines)


def dart_output(
    loaded: list[tuple[Vocabulary, list[Record]]], fingerprint: str
) -> str:
    lines = [
        "// Generated card reference vocabularies. Do not edit by hand.",
        f"// Input SHA-256: {fingerprint}",
        "",
        "import 'package:flutter/material.dart';",
        "",
        "// ignore: constant_identifier_names",
        f"const String DATA_FINGERPRINT = {dart_string(fingerprint)};",
        "const String dataFingerprint = DATA_FINGERPRINT;",
    ]

    for vocabulary, records in loaded:
        lines.extend(["", f"enum {vocabulary.class_name} {{"])
        for index, record in enumerate(records):
            arguments = [
                dart_string(record.id),
                dart_string(record.name),
                f"Icons.{FLUTTER_ICONS[record.material_symbol]}",
            ]
            if vocabulary.has_description:
                assert record.description is not None
                arguments.append(dart_string(record.description))
            if vocabulary.has_brand_asset_key:
                arguments.append(
                    "null"
                    if record.brand_asset_key is None
                    else dart_string(record.brand_asset_key)
                )
            suffix = ";" if index == len(records) - 1 else ","
            lines.append(f"  {camel(record.id)}({', '.join(arguments)}){suffix}")

        parameters = ["this.id", "this.label", "this.icon"]
        if vocabulary.has_description:
            parameters.append("this.description")
        if vocabulary.has_brand_asset_key:
            parameters.append("this.brandAssetKey")
        lines.extend(
            [
                "",
                f"  const {vocabulary.class_name}({', '.join(parameters)});",
                "  final String id;",
                "  final String label;",
                "  final IconData icon;",
            ]
        )
        if vocabulary.has_description:
            lines.append("  final String description;")
        if vocabulary.has_brand_asset_key:
            lines.append("  final String? brandAssetKey;")
        index_name = "_" + vocabulary.dart_records_name.removesuffix("Records") + "ById"
        lines.extend(
            [
                "",
                f"  static {vocabulary.class_name}? tryParse(String id) => {index_name}[id];",
                "}",
                "",
                f"const Map<String, {vocabulary.class_name}> {index_name} = {{",
            ]
        )
        for record in records:
            lines.append(
                f"  {dart_string(record.id)}: {vocabulary.class_name}.{camel(record.id)},"
            )
        lines.append("};")

    lines.append("")
    for vocabulary, records in loaded:
        lines.append(
            f"const List<{vocabulary.class_name}> {vocabulary.dart_records_name} = "
            f"{vocabulary.class_name}.values;"
        )
        lines.append(f"const int {vocabulary.dart_count_name} = {len(records)};")
    lines.extend(["", "const Map<String, List<Enum>> records = {"])
    for vocabulary, _ in loaded:
        lines.append(
            f"  {dart_string(vocabulary.dataset_id)}: {vocabulary.dart_records_name},"
        )
    lines.extend(["};", "", "const Map<String, int> counts = {"])
    for vocabulary, _ in loaded:
        lines.append(
            f"  {dart_string(vocabulary.dataset_id)}: {vocabulary.dart_count_name},"
        )
    lines.extend(
        [
            "};",
            "",
            "// ignore: constant_identifier_names",
            "const Map<String, List<Enum>> RECORDS = records;",
            "// ignore: constant_identifier_names",
            "const Map<String, int> COUNTS = counts;",
            "",
        ]
    )
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
    loaded = load_vocabularies(root)
    fingerprint = input_hash(root)
    outputs = {
        root
        / "packages"
        / "python"
        / "reffin_cards"
        / "src"
        / "reffin_cards"
        / "_generated.py": python_output(loaded, fingerprint),
        root
        / "packages"
        / "typescript"
        / "reffin_cards"
        / "src"
        / "generated.ts": typescript_output(loaded, fingerprint),
        root
        / "packages"
        / "flutter"
        / "reffin_cards"
        / "lib"
        / "src"
        / "generated.dart": dart_output(loaded, fingerprint),
    }
    stale = [
        path for path, content in outputs.items() if not write_or_check(path, content, check)
    ]
    action = "verified" if check else "generated"
    print(f"{action} {sum(len(rows) for _, rows in loaded)} card vocabulary records")
    return stale


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are stale")
    args = parser.parse_args()
    stale = generate(ROOT, check=args.check)
    if stale:
        for path in stale:
            print(f"stale: {path.relative_to(ROOT)}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
