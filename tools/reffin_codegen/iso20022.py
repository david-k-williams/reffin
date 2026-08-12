#!/usr/bin/env python3
"""Generate the offline Reffin ISO 20022 packages from normalized CSV inputs."""

from __future__ import annotations

import argparse
import csv
import keyword
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Callable, Sequence

from .common import ROOT, dart_string, fingerprint, py_string, ts_string, write_or_check


DATA_DIR = ROOT / "data" / "iso20022"
CODE_SETS_PATH = DATA_DIR / "code_sets.csv"
EXTERNAL_CODES_PATH = DATA_DIR / "external_codes.csv"
BTC_PATH = DATA_DIR / "bank_transaction_codes.csv"
MESSAGES_PATH = DATA_DIR / "message_definitions.csv"
SOURCES_PATH = DATA_DIR / "sources.csv"
EXTERNAL_CODE_SETS_VERSION = "May 2026 v1"
EXTERNAL_CODE_SETS_ARTIFACT_VERSION = "1Q2026_externalcodesets_v1"
BANK_TRANSACTION_CODES_VERSION = "2025-11-30"
MESSAGE_DEFINITIONS_VERSION = "2026-06-26"
EXTERNAL_SOURCE_ID = "iso20022_external_code_sets_1q2026_v1"
BTC_SOURCE_ID = "iso20022_btc_2025_11_30"
MESSAGE_SOURCE_ID = "iso20022_erepository_2026_06_26"

CODE_SET_COLUMNS = ("code_set", "definition", "status", "source")
EXTERNAL_CODE_COLUMNS = (
    "code_set",
    "code",
    "name",
    "label",
    "definition",
    "requester",
    "status",
    "last_updated",
    "creation_date",
    "replaced_by",
    "mapping_standard_1",
    "mapping_value_1",
    "mapping_standard_2",
    "mapping_value_2",
    "additional_information",
    "source",
)
BTC_COLUMNS = (
    "domain_code",
    "domain_name",
    "family_code",
    "family_name",
    "subfamily_code",
    "subfamily_name",
    "status",
    "status_date",
)
MESSAGE_COLUMNS = (
    "business_area",
    "message_id",
    "message_number",
    "variant",
    "version",
    "name",
)
EXTERNAL_STATUSES = {"registered", "obsolete"}
CODE_SET_STATUSES = EXTERNAL_STATUSES | {"provisionally_registered"}


@dataclass(frozen=True, slots=True)
class PaymentFamily:
    public_name: str
    code_set: str
    expected_current: int
    material_symbol: str
    python_module: str
    typescript_module: str
    dart_module: str


PAYMENT_FAMILIES = (
    PaymentFamily(
        "PaymentPurposeCode",
        "ExternalPurpose1Code",
        342,
        "payments",
        "payment_purpose",
        "paymentPurpose",
        "payment_purpose",
    ),
    PaymentFamily(
        "PaymentStatusReasonCode",
        "ExternalStatusReason1Code",
        302,
        "error_outline",
        "payment_status_reason",
        "paymentStatusReason",
        "payment_status_reason",
    ),
    PaymentFamily(
        "PaymentReturnReasonCode",
        "ExternalReturnReason1Code",
        104,
        "undo",
        "payment_return_reason",
        "paymentReturnReason",
        "payment_return_reason",
    ),
    PaymentFamily(
        "LocalInstrumentCode",
        "ExternalLocalInstrument1Code",
        86,
        "account_balance",
        "local_instrument",
        "localInstrument",
        "local_instrument",
    ),
    PaymentFamily(
        "CategoryPurposeCode",
        "ExternalCategoryPurpose1Code",
        49,
        "category",
        "category_purpose",
        "categoryPurpose",
        "category_purpose",
    ),
    PaymentFamily(
        "ServiceLevelCode",
        "ExternalServiceLevel1Code",
        29,
        "speed",
        "service_level",
        "serviceLevel",
        "service_level",
    ),
    PaymentFamily(
        "PaymentTransactionStatusCode",
        "ExternalPaymentTransactionStatus1Code",
        25,
        "sync",
        "payment_transaction_status",
        "paymentTransactionStatus",
        "payment_transaction_status",
    ),
    PaymentFamily(
        "PaymentGroupStatusCode",
        "ExternalPaymentGroupStatus1Code",
        13,
        "fact_check",
        "payment_group_status",
        "paymentGroupStatus",
        "payment_group_status",
    ),
)
PAYMENT_SET_BY_NAME = {family.code_set: family for family in PAYMENT_FAMILIES}
EXPECTED_PAYMENT_CURRENT = sum(family.expected_current for family in PAYMENT_FAMILIES)
SHARD_TARGET = 52_000


def _read_exact(path: Path, columns: tuple[str, ...]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if tuple(reader.fieldnames or ()) != columns:
            raise ValueError(f"{path}: expected columns {columns!r}, got {reader.fieldnames!r}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"{path}: no data rows")
    for row_number, row in enumerate(rows, start=2):
        for field, value in row.items():
            if value != value.strip():
                raise ValueError(f"{path}:{row_number}: {field} has outer whitespace")
    return rows


def _validate_date(path: Path, row_number: int, field: str, value: str) -> None:
    if not value:
        return
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"{path}:{row_number}: invalid {field} {value!r}")
    try:
        date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"{path}:{row_number}: invalid {field} {value!r}") from error


def _validate_sources(rows: Sequence[dict[str, str]], path: Path) -> None:
    for row_number, row in enumerate(rows, start=2):
        if not row.get("source"):
            raise ValueError(f"{path}:{row_number}: source is required")


def _load() -> tuple[
    list[dict[str, str]],
    list[dict[str, str]],
    list[dict[str, str]],
    list[dict[str, str]],
]:
    code_sets = _read_exact(CODE_SETS_PATH, CODE_SET_COLUMNS)
    external = _read_exact(EXTERNAL_CODES_PATH, EXTERNAL_CODE_COLUMNS)
    btc = _read_exact(BTC_PATH, BTC_COLUMNS)
    messages = _read_exact(MESSAGES_PATH, MESSAGE_COLUMNS)
    with SOURCES_PATH.open(newline="", encoding="utf-8-sig") as stream:
        source_reader = csv.DictReader(stream)
        expected_source_columns = (
            "source_id", "publisher", "title", "version", "published_date", "retrieved_at",
            "url", "format", "sha256", "notes",
        )
        if tuple(source_reader.fieldnames or ()) != expected_source_columns:
            raise ValueError(
                f"{SOURCES_PATH}: expected columns {expected_source_columns!r}, "
                f"got {source_reader.fieldnames!r}"
            )
        source_rows = list(source_reader)
    source_ids = {row.get("source_id", "") for row in source_rows}
    required_source_ids = {EXTERNAL_SOURCE_ID, BTC_SOURCE_ID, MESSAGE_SOURCE_ID}
    if not required_source_ids <= source_ids:
        raise ValueError(
            f"{SOURCES_PATH}: missing required source identifiers "
            f"{sorted(required_source_ids - source_ids)!r}"
        )
    undeclared = sorted(
        {
            source
            for rows in (code_sets, external)
            for row in rows
            for source in row["source"].split("|")
            if source and source not in source_ids
        }
    )
    if undeclared:
        raise ValueError(f"{SOURCES_PATH}: undeclared source identifiers {undeclared!r}")
    observed_external_sources = {
        source
        for rows in (code_sets, external)
        for row in rows
        for source in row["source"].split("|")
        if source
    }
    if observed_external_sources != {EXTERNAL_SOURCE_ID}:
        raise ValueError(
            f"external catalogs must cite only {EXTERNAL_SOURCE_ID!r}; "
            f"got {sorted(observed_external_sources)!r}"
        )

    if len(code_sets) != 158:
        raise ValueError(f"{CODE_SETS_PATH}: expected 158 rows, got {len(code_sets)}")
    if len(external) != 3_246:
        raise ValueError(f"{EXTERNAL_CODES_PATH}: expected 3,246 rows, got {len(external)}")
    if len(btc) != 1_567:
        raise ValueError(f"{BTC_PATH}: expected 1,567 rows, got {len(btc)}")
    if len(messages) != 797:
        raise ValueError(f"{MESSAGES_PATH}: expected 797 rows, got {len(messages)}")

    set_names = [row["code_set"] for row in code_sets]
    if any(not value for value in set_names):
        raise ValueError(f"{CODE_SETS_PATH}: code_set is required")
    if len(set_names) != len(set(set_names)):
        raise ValueError(f"{CODE_SETS_PATH}: duplicate code_set")
    for row_number, row in enumerate(code_sets, start=2):
        if row["status"] not in CODE_SET_STATUSES:
            raise ValueError(f"{CODE_SETS_PATH}:{row_number}: invalid status {row['status']!r}")
    _validate_sources(code_sets, CODE_SETS_PATH)

    known_sets = set(set_names)
    identities: Counter[tuple[str, str]] = Counter()
    statuses: Counter[str] = Counter()
    for row_number, row in enumerate(external, start=2):
        if row["code_set"] not in known_sets:
            raise ValueError(
                f"{EXTERNAL_CODES_PATH}:{row_number}: unknown code set {row['code_set']!r}"
            )
        if not row["code"] or not row["name"] or not row["label"]:
            raise ValueError(
                f"{EXTERNAL_CODES_PATH}:{row_number}: code, name, and label are required"
            )
        if row["status"] not in EXTERNAL_STATUSES:
            raise ValueError(
                f"{EXTERNAL_CODES_PATH}:{row_number}: invalid status {row['status']!r}"
            )
        _validate_date(EXTERNAL_CODES_PATH, row_number, "last_updated", row["last_updated"])
        _validate_date(EXTERNAL_CODES_PATH, row_number, "creation_date", row["creation_date"])
        identities[(row["code_set"], row["code"])] += 1
        statuses[row["status"]] += 1
    _validate_sources(external, EXTERNAL_CODES_PATH)
    if statuses != Counter({"registered": 3_213, "obsolete": 33}):
        raise ValueError(f"{EXTERNAL_CODES_PATH}: unexpected status counts {dict(statuses)!r}")
    if len(identities) != 3_245:
        raise ValueError(
            f"{EXTERNAL_CODES_PATH}: expected 3,245 set/code identities, got {len(identities)}"
        )
    duplicates = {identity: count for identity, count in identities.items() if count > 1}
    if duplicates != {("ExternalLocalInstrument1Code", "CTP"): 2}:
        raise ValueError(f"{EXTERNAL_CODES_PATH}: unexpected history identities {duplicates!r}")

    for family in PAYMENT_FAMILIES:
        rows = [
            row
            for row in external
            if row["code_set"] == family.code_set and row["status"] == "registered"
        ]
        if len(rows) != family.expected_current:
            raise ValueError(
                f"{EXTERNAL_CODES_PATH}: {family.code_set} expected "
                f"{family.expected_current} registered rows, got {len(rows)}"
            )
        codes = [row["code"] for row in rows]
        if len(codes) != len(set(codes)):
            raise ValueError(f"{EXTERNAL_CODES_PATH}: current {family.code_set} codes repeat")
        _validate_member_names(codes, family.code_set)

    btc_identities: set[tuple[str, str, str]] = set()
    for row_number, row in enumerate(btc, start=2):
        required = (
            "domain_code",
            "domain_name",
            "family_code",
            "family_name",
            "subfamily_code",
            "subfamily_name",
            "status",
            "status_date",
        )
        if any(not row[field] for field in required):
            raise ValueError(f"{BTC_PATH}:{row_number}: hierarchy code and name fields are required")
        btc_identities.add(
            (row["domain_code"], row["family_code"], row["subfamily_code"])
        )
        _validate_date(BTC_PATH, row_number, "status_date", row["status_date"])
    if not btc_identities:
        raise ValueError(f"{BTC_PATH}: no composite identities")
    if len(btc_identities) != 1_564:
        raise ValueError(f"{BTC_PATH}: expected 1,564 composite identities, got {len(btc_identities)}")
    btc_statuses = Counter(row["status"] for row in btc)
    if btc_statuses != Counter({"new": 1_528, "corrected": 35, "updated": 4}):
        raise ValueError(f"{BTC_PATH}: unexpected status counts {dict(btc_statuses)!r}")

    message_ids: set[str] = set()
    pattern = re.compile(r"^([a-z]{4})\.(\d{3})\.(\d{3})\.(\d{2})$")
    for row_number, row in enumerate(messages, start=2):
        match = pattern.fullmatch(row["message_id"])
        if match is None:
            raise ValueError(f"{MESSAGES_PATH}:{row_number}: invalid message_id")
        area, number, variant, version = match.groups()
        expected = (row["business_area"], row["message_number"], row["variant"], row["version"])
        if (area, number, variant, version) != expected:
            raise ValueError(f"{MESSAGES_PATH}:{row_number}: identifier components disagree")
        if not row["name"]:
            raise ValueError(f"{MESSAGES_PATH}:{row_number}: name is required")
        if row["message_id"] in message_ids:
            raise ValueError(f"{MESSAGES_PATH}:{row_number}: duplicate message_id")
        message_ids.add(row["message_id"])

    return code_sets, external, btc, messages


def _python_member(code: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "_", code).strip("_").upper()
    if not value or value[0].isdigit():
        value = f"CODE_{value}"
    if keyword.iskeyword(value.lower()):
        value = f"{value}_CODE"
    return value


def _typescript_member(code: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "_", code).strip("_")
    if not value:
        return "Code"
    if value[0].isdigit():
        return "Code" + value
    return value


def _dart_member(code: str) -> str:
    parts = [part for part in re.split(r"[^A-Za-z0-9]+", code) if part]
    if not parts:
        value = "code"
    elif parts[0][0].isdigit():
        value = "code" + "".join(part[:1].upper() + part[1:].lower() for part in parts)
    else:
        first, *rest = parts
        value = first.lower() + "".join(part[:1].upper() + part[1:].lower() for part in rest)
    if value in {
        "assert", "break", "case", "catch", "class", "const", "continue", "default",
        "do", "else", "enum", "extends", "false", "final", "finally", "for", "if",
        "in", "is", "new", "null", "rethrow", "return", "super", "switch", "this",
        "throw", "true", "try", "var", "void", "while", "with",
    }:
        value += "Code"
    return value


def _validate_member_names(codes: Sequence[str], code_set: str) -> None:
    for language, transform in (
        ("Python", _python_member),
        ("TypeScript", _typescript_member),
        ("Dart", _dart_member),
    ):
        values = [transform(code) for code in codes]
        duplicates = sorted(name for name, count in Counter(values).items() if count > 1)
        if duplicates:
            raise ValueError(f"{code_set}: colliding {language} members {duplicates!r}")


def _dart_dataset_name(value: str) -> str:
    parts = value.split("_")
    return parts[0] + "".join(part[:1].upper() + part[1:] for part in parts[1:])


def _row_literal(row: dict[str, str], columns: Sequence[str], quote: Callable[[str], str]) -> str:
    return "[" + ", ".join(quote(row[column]) for column in columns) + "]"


def _chunks(
    rows: Sequence[dict[str, str]],
    columns: Sequence[str],
    quote: Callable[[str], str],
) -> list[list[str]]:
    chunks: list[list[str]] = []
    current: list[str] = []
    current_size = 0
    for row in rows:
        literal = _row_literal(row, columns, quote)
        projected = current_size + len(literal) + 4
        if current and projected > SHARD_TARGET:
            chunks.append(current)
            current = []
            current_size = 0
        current.append(literal)
        current_size += len(literal) + 4
    if current:
        chunks.append(current)
    return chunks


def _python_model(digest: str) -> str:
    return f'''"""Generated ISO 20022 value models. Do not edit by hand."""
# Input SHA-256: {digest}
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum


class Iso20022CodeStatus(str, Enum):
    REGISTERED = "registered"
    OBSOLETE = "obsolete"


@dataclass(frozen=True, slots=True)
class Iso20022CodeSetInfo:
    code_set: str
    definition: str
    status: str
    sources: tuple[str, ...]

    @property
    def is_current(self) -> bool:
        return self.status != Iso20022CodeStatus.OBSOLETE.value


@dataclass(frozen=True, slots=True)
class Iso20022CodeInfo:
    code_set: str
    code: str
    name: str
    label: str
    definition: str
    requester: str | None
    status: Iso20022CodeStatus
    last_updated: date | None
    creation_date: date | None
    replaced_by: str | None
    mapping_standard_1: str | None
    mapping_value_1: str | None
    mapping_standard_2: str | None
    mapping_value_2: str | None
    additional_information: str | None
    sources: tuple[str, ...]
    material_symbol: str

    @property
    def is_current(self) -> bool:
        return self.status is Iso20022CodeStatus.REGISTERED


@dataclass(frozen=True, slots=True)
class BankTransactionCodeInfo:
    domain_code: str
    domain_name: str
    family_code: str
    family_name: str
    subfamily_code: str
    subfamily_name: str
    status: str
    status_date: date

    @property
    def code(self) -> str:
        return "-".join((self.domain_code, self.family_code, self.subfamily_code))


@dataclass(frozen=True, slots=True)
class MessageDefinitionInfo:
    business_area: str
    message_id: str
    message_number: str
    variant: str
    version: str
    name: str
'''


def _python_shards(
    label: str,
    rows: Sequence[dict[str, str]],
    columns: Sequence[str],
    digest: str,
) -> tuple[dict[str, str], list[str]]:
    chunks = _chunks(rows, columns, py_string)
    outputs: dict[str, str] = {}
    names: list[str] = []
    for index, chunk in enumerate(chunks):
        name = f"_{label}_{index:02d}"
        names.append(name)
        body = [
            f'"""Generated ISO 20022 {label} shard. Do not edit by hand."""',
            f"# Input SHA-256: {digest}",
            "",
            "ROWS = (",
        ]
        body.extend(f"    ({literal[1:-1]})," for literal in chunk)
        body.append(")")
        outputs[f"{name}.py"] = "\n".join(body)
    return outputs, names


def _python_enum(family: PaymentFamily, codes: Sequence[str], digest: str) -> str:
    lines = [
        f'"""Generated {family.public_name}. Do not edit by hand."""',
        f"# Input SHA-256: {digest}",
        "from __future__ import annotations",
        "",
        "from enum import Enum",
        "from typing import Self, cast",
        "",
        "from ._model import Iso20022CodeInfo",
        "",
        "",
        f"class {family.public_name}(str, Enum):",
    ]
    lines.extend(f"    {_python_member(code)} = {py_string(code)}" for code in codes)
    lines.extend(
        [
            "",
            "    @property",
            "    def code(self) -> str:",
            "        return str(self.value)",
            "",
            "    @property",
            "    def info(self) -> Iso20022CodeInfo:",
            "        from ._generated import resolve_code",
            "",
            f"        return cast(Iso20022CodeInfo, resolve_code({py_string(family.code_set)}, self.value))",
            "",
            "    @property",
            "    def label(self) -> str:",
            "        return self.info.label",
            "",
            "    @property",
            "    def material_symbol(self) -> str:",
            "        return self.info.material_symbol",
            "",
            "    @classmethod",
            f"    def try_parse(cls, code: object) -> Self | None:",
            "        if isinstance(code, cls):",
            "            return code",
            "        if not isinstance(code, str):",
            "            return None",
            "        normalized = code.strip().casefold()",
            "        return next((value for value in cls if value.value.casefold() == normalized), None)",
        ]
    )
    return "\n".join(lines)


def _python_runtime(
    py_shards: dict[str, list[str]],
    digest: str,
    btc_count: int,
) -> str:
    lines = [
        '"""Generated offline ISO 20022 catalogs. Do not edit by hand."""',
        f"# Input SHA-256: {digest}",
        "from __future__ import annotations",
        "",
        "from datetime import date",
        "from types import MappingProxyType",
        "from typing import Final, Mapping",
        "",
        "from ._model import (",
        "    BankTransactionCodeInfo, Iso20022CodeInfo, Iso20022CodeSetInfo,",
        "    Iso20022CodeStatus, MessageDefinitionInfo,",
        ")",
    ]
    for label, names in py_shards.items():
        for name in names:
            lines.append(f"from .{name} import ROWS as {name.upper()}_ROWS")
    lines.extend(
        [
            "",
            f"DATA_FINGERPRINT: Final[str] = {py_string(digest)}",
            f"EXTERNAL_CODE_SETS_VERSION: Final[str] = {py_string(EXTERNAL_CODE_SETS_VERSION)}",
            f"EXTERNAL_CODE_SETS_ARTIFACT_VERSION: Final[str] = {py_string(EXTERNAL_CODE_SETS_ARTIFACT_VERSION)}",
            f"BANK_TRANSACTION_CODES_VERSION: Final[str] = {py_string(BANK_TRANSACTION_CODES_VERSION)}",
            f"MESSAGE_DEFINITIONS_VERSION: Final[str] = {py_string(MESSAGE_DEFINITIONS_VERSION)}",
            "",
        ]
    )
    for label, names in py_shards.items():
        expression = " + ".join(f"{name.upper()}_ROWS" for name in names)
        lines.append(f"_{label.upper()}_ROWS = {expression}")
    icon_items = {family.code_set: family.material_symbol for family in PAYMENT_FAMILIES}
    lines.extend(
        [
            "",
            f"_MATERIAL_SYMBOL_BY_SET = {icon_items!r}",
            "",
            "",
            "def _optional(value: str) -> str | None:",
            "    return value or None",
            "",
            "",
            "def _date(value: str) -> date | None:",
            "    return date.fromisoformat(value) if value else None",
            "",
            "",
            "def _sources(value: str) -> tuple[str, ...]:",
            "    return tuple(part for part in value.split('|') if part)",
            "",
            "",
            "CODE_SETS: Final = tuple(",
            "    Iso20022CodeSetInfo(code_set, definition, status, _sources(source))",
            "    for code_set, definition, status, source in _CODE_SETS_ROWS",
            ")",
            "EXTERNAL_CODE_RECORDS: Final = tuple(",
            "    Iso20022CodeInfo(",
            "        code_set=row[0], code=row[1], name=row[2], label=row[3], definition=row[4],",
            "        requester=_optional(row[5]), status=Iso20022CodeStatus(row[6]),",
            "        last_updated=_date(row[7]), creation_date=_date(row[8]),",
            "        replaced_by=_optional(row[9]), mapping_standard_1=_optional(row[10]),",
            "        mapping_value_1=_optional(row[11]), mapping_standard_2=_optional(row[12]),",
            "        mapping_value_2=_optional(row[13]), additional_information=_optional(row[14]),",
            "        sources=_sources(row[15]), material_symbol=_MATERIAL_SYMBOL_BY_SET.get(row[0], 'code'),",
            "    )",
            "    for row in _EXTERNAL_CODES_ROWS",
            ")",
            "CURRENT_EXTERNAL_CODES: Final = tuple(record for record in EXTERNAL_CODE_RECORDS if record.is_current)",
            "BANK_TRANSACTION_CODE_RECORDS: Final = tuple(",
            "    BankTransactionCodeInfo(*row[:7], date.fromisoformat(row[7]))",
            "    for row in _BANK_TRANSACTION_CODES_ROWS",
            ")",
            "MESSAGE_DEFINITIONS: Final = tuple(MessageDefinitionInfo(*row) for row in _MESSAGE_DEFINITIONS_ROWS)",
            "",
            "CODE_SET_COUNT: Final = len(CODE_SETS)",
            "EXTERNAL_CODE_RECORD_COUNT: Final = len(EXTERNAL_CODE_RECORDS)",
            "CURRENT_EXTERNAL_CODE_COUNT: Final = len(CURRENT_EXTERNAL_CODES)",
            "EXTERNAL_CODE_IDENTITY_COUNT: Final = len({(item.code_set, item.code) for item in EXTERNAL_CODE_RECORDS})",
            "BANK_TRANSACTION_CODE_RECORD_COUNT: Final = len(BANK_TRANSACTION_CODE_RECORDS)",
            "BANK_TRANSACTION_CODE_IDENTITY_COUNT: Final = len({",
            "    (item.domain_code, item.family_code, item.subfamily_code)",
            "    for item in BANK_TRANSACTION_CODE_RECORDS",
            "})",
            "MESSAGE_DEFINITION_COUNT: Final = len(MESSAGE_DEFINITIONS)",
            f"PAYMENT_CODE_COUNT: Final = {EXPECTED_PAYMENT_CURRENT}",
            "",
            "",
            "def _key(value: str) -> str:",
            "    return value.strip().casefold()",
            "",
            "",
            "_CODE_SET_BY_NAME: Final = MappingProxyType({_key(item.code_set): item for item in CODE_SETS})",
            "_external_mutable: dict[tuple[str, str], list[Iso20022CodeInfo]] = {}",
            "_external_by_code_mutable: dict[str, list[Iso20022CodeInfo]] = {}",
            "for _record in EXTERNAL_CODE_RECORDS:",
            "    _external_mutable.setdefault((_key(_record.code_set), _key(_record.code)), []).append(_record)",
            "    _external_by_code_mutable.setdefault(_key(_record.code), []).append(_record)",
            "_EXTERNAL_BY_KEY: Final = MappingProxyType({",
            "    key: tuple(values) for key, values in _external_mutable.items()",
            "})",
            "_EXTERNAL_BY_CODE: Final = MappingProxyType({",
            "    key: tuple(values) for key, values in _external_by_code_mutable.items()",
            "})",
            "",
            "",
            "def resolve_code_set(code_set: str, *, include_obsolete: bool = False) -> Iso20022CodeSetInfo | None:",
            "    if not isinstance(code_set, str):",
            "        return None",
            "    info = _CODE_SET_BY_NAME.get(_key(code_set))",
            "    return info if info is not None and (include_obsolete or info.is_current) else None",
            "",
            "",
            "def records_for(",
            "    code_set: str, code: str, *, include_obsolete: bool = False",
            ") -> tuple[Iso20022CodeInfo, ...]:",
            "    if not isinstance(code_set, str) or not isinstance(code, str):",
            "        return ()",
            "    values = _EXTERNAL_BY_KEY.get((_key(code_set), _key(code)), ())",
            "    return values if include_obsolete else tuple(item for item in values if item.is_current)",
            "",
            "",
            "def resolve_code(",
            "    code_set: str, code: str, *, include_obsolete: bool = False",
            ") -> Iso20022CodeInfo | None:",
            "    current = records_for(code_set, code)",
            "    if current:",
            "        return current[0]",
            "    if include_obsolete:",
            "        history = records_for(code_set, code, include_obsolete=True)",
            "        return history[0] if history else None",
            "    return None",
            "",
            "",
            "def find_codes(code: str, *, include_obsolete: bool = False) -> tuple[Iso20022CodeInfo, ...]:",
            "    if not isinstance(code, str):",
            "        return ()",
            "    values = _EXTERNAL_BY_CODE.get(_key(code), ())",
            "    return values if include_obsolete else tuple(item for item in values if item.is_current)",
            "",
            "",
            "def search_codes(",
            "    query: str, *, code_set: str | None = None, include_obsolete: bool = False,",
            "    limit: int | None = None,",
            ") -> tuple[Iso20022CodeInfo, ...]:",
            "    if not isinstance(query, str) or not query.strip() or (limit is not None and limit <= 0):",
            "        return ()",
            "    needle = _key(query)",
            "    set_key = _key(code_set) if isinstance(code_set, str) else None",
            "    found: list[Iso20022CodeInfo] = []",
            "    for item in EXTERNAL_CODE_RECORDS:",
            "        if not include_obsolete and not item.is_current:",
            "            continue",
            "        if set_key is not None and _key(item.code_set) != set_key:",
            "            continue",
            "        haystack = '\\n'.join((item.code, item.name, item.label, item.definition, item.additional_information or '')).casefold()",
            "        if needle in haystack:",
            "            found.append(item)",
            "            if limit is not None and len(found) >= limit:",
            "                break",
            "    return tuple(found)",
            "",
            "",
            "_btc_mutable: dict[tuple[str, str, str], list[BankTransactionCodeInfo]] = {}",
            "for _record in BANK_TRANSACTION_CODE_RECORDS:",
            "    _btc_mutable.setdefault(",
            "        (_key(_record.domain_code), _key(_record.family_code), _key(_record.subfamily_code)), []",
            "    ).append(_record)",
            "_BTC_BY_KEY: Final = MappingProxyType({key: tuple(values) for key, values in _btc_mutable.items()})",
            "",
            "",
            "def resolve_bank_transaction_code(",
            "    domain_code: str, family_code: str, subfamily_code: str,",
            ") -> tuple[BankTransactionCodeInfo, ...]:",
            "    if not all(isinstance(value, str) for value in (domain_code, family_code, subfamily_code)):",
            "        return ()",
            "    return _BTC_BY_KEY.get((_key(domain_code), _key(family_code), _key(subfamily_code)), ())",
            "",
            "",
            "def find_bank_transaction_codes(",
            "    domain_code: str, *, family_code: str | None = None, subfamily_code: str | None = None,",
            ") -> tuple[BankTransactionCodeInfo, ...]:",
            "    if not isinstance(domain_code, str):",
            "        return ()",
            "    domain_key = _key(domain_code)",
            "    family_key = _key(family_code) if isinstance(family_code, str) else None",
            "    subfamily_key = _key(subfamily_code) if isinstance(subfamily_code, str) else None",
            "    return tuple(",
            "        item for item in BANK_TRANSACTION_CODE_RECORDS",
            "        if _key(item.domain_code) == domain_key",
            "        and (family_key is None or _key(item.family_code) == family_key)",
            "        and (subfamily_key is None or _key(item.subfamily_code) == subfamily_key)",
            "    )",
            "",
            "",
            "_MESSAGE_BY_ID: Final[Mapping[str, MessageDefinitionInfo]] = MappingProxyType({",
            "    _key(item.message_id): item for item in MESSAGE_DEFINITIONS",
            "})",
            "",
            "",
            "def resolve_message_identifier(message_id: str) -> MessageDefinitionInfo | None:",
            "    return _MESSAGE_BY_ID.get(_key(message_id)) if isinstance(message_id, str) else None",
            "",
            "",
            "def find_message_definitions(",
            "    *, business_area: str | None = None, message_number: str | None = None,",
            ") -> tuple[MessageDefinitionInfo, ...]:",
            "    area_key = _key(business_area) if isinstance(business_area, str) else None",
            "    number_key = _key(message_number) if isinstance(message_number, str) else None",
            "    return tuple(",
            "        item for item in MESSAGE_DEFINITIONS",
            "        if (area_key is None or _key(item.business_area) == area_key)",
            "        and (number_key is None or _key(item.message_number) == number_key)",
            "    )",
        ]
    )
    for family in PAYMENT_FAMILIES:
        lines.append(f"from .{family.python_module} import {family.public_name}")
    exported = [
        "DATA_FINGERPRINT", "EXTERNAL_CODE_SETS_VERSION", "EXTERNAL_CODE_SETS_ARTIFACT_VERSION",
        "BANK_TRANSACTION_CODES_VERSION", "MESSAGE_DEFINITIONS_VERSION",
        "Iso20022CodeStatus", "Iso20022CodeSetInfo", "Iso20022CodeInfo",
        "BankTransactionCodeInfo", "MessageDefinitionInfo", "CODE_SETS", "EXTERNAL_CODE_RECORDS",
        "CURRENT_EXTERNAL_CODES", "BANK_TRANSACTION_CODE_RECORDS", "MESSAGE_DEFINITIONS",
        "CODE_SET_COUNT", "EXTERNAL_CODE_RECORD_COUNT", "CURRENT_EXTERNAL_CODE_COUNT",
        "EXTERNAL_CODE_IDENTITY_COUNT", "BANK_TRANSACTION_CODE_RECORD_COUNT",
        "BANK_TRANSACTION_CODE_IDENTITY_COUNT", "MESSAGE_DEFINITION_COUNT", "PAYMENT_CODE_COUNT",
        "resolve_code_set", "records_for", "resolve_code", "find_codes", "search_codes",
        "resolve_bank_transaction_code", "find_bank_transaction_codes",
        "resolve_message_identifier", "find_message_definitions",
        *(family.public_name for family in PAYMENT_FAMILIES),
    ]
    lines.extend(["", f"__all__ = {exported!r}"])
    return "\n".join(lines)


def _ts_model(digest: str) -> str:
    return f'''// Generated ISO 20022 value models. Do not edit by hand.
// Input SHA-256: {digest}
export type Iso20022CodeStatus = "registered" | "obsolete";

export interface Iso20022CodeSetInfo {{
  readonly codeSet: string;
  readonly definition: string;
  readonly status: Iso20022CodeStatus | "provisionally_registered";
  readonly sources: readonly string[];
  readonly isCurrent: boolean;
}}

export interface Iso20022CodeInfo {{
  readonly codeSet: string;
  readonly code: string;
  readonly name: string;
  readonly label: string;
  readonly definition: string;
  readonly requester: string | null;
  readonly status: Iso20022CodeStatus;
  readonly lastUpdated: string | null;
  readonly creationDate: string | null;
  readonly replacedBy: string | null;
  readonly mappingStandard1: string | null;
  readonly mappingValue1: string | null;
  readonly mappingStandard2: string | null;
  readonly mappingValue2: string | null;
  readonly additionalInformation: string | null;
  readonly sources: readonly string[];
  readonly materialSymbol: string;
  readonly isCurrent: boolean;
}}

export interface BankTransactionCodeInfo {{
  readonly domainCode: string;
  readonly domainName: string;
  readonly familyCode: string;
  readonly familyName: string;
  readonly subfamilyCode: string;
  readonly subfamilyName: string;
  readonly status: string;
  readonly statusDate: string;
  readonly code: string;
}}

export interface MessageDefinitionInfo {{
  readonly businessArea: string;
  readonly messageId: string;
  readonly messageNumber: string;
  readonly variant: string;
  readonly version: string;
  readonly name: string;
}}

export type RawRow = readonly string[];
'''


def _ts_shards(
    label: str,
    rows: Sequence[dict[str, str]],
    columns: Sequence[str],
    digest: str,
) -> tuple[dict[str, str], list[str]]:
    chunks = _chunks(rows, columns, ts_string)
    outputs: dict[str, str] = {}
    names: list[str] = []
    for index, chunk in enumerate(chunks):
        name = f"{label}{index:02d}"
        names.append(name)
        body = [
            f"// Generated ISO 20022 {label} shard. Do not edit by hand.",
            f"// Input SHA-256: {digest}",
            'import type { RawRow } from "../model.js";',
            "",
            "export const rows: readonly RawRow[] = Object.freeze([",
        ]
        body.extend(f"  Object.freeze({literal})," for literal in chunk)
        body.append("]);")
        outputs[f"data/{name}.ts"] = "\n".join(body)
    return outputs, names


def _ts_enum(family: PaymentFamily, codes: Sequence[str], digest: str) -> str:
    lines = [
        f"// Generated {family.public_name}. Do not edit by hand.",
        f"// Input SHA-256: {digest}",
        'import { resolveCode } from "./generated.js";',
        "",
        f"export const {family.public_name} = Object.freeze({{",
    ]
    lines.extend(
        f"  {_typescript_member(code)}: resolveCode({ts_string(family.code_set)}, {ts_string(code)})!,"
        for code in codes
    )
    lines.extend(
        [
            "});",
            f"export type {family.public_name} =",
            f"  (typeof {family.public_name})[keyof typeof {family.public_name}];",
        ]
    )
    return "\n".join(lines)


def _ts_runtime(ts_shards: dict[str, list[str]], digest: str, btc_count: int) -> str:
    lines = [
        "// Generated offline ISO 20022 catalogs. Do not edit by hand.",
        f"// Input SHA-256: {digest}",
        "import type {",
        "  BankTransactionCodeInfo, Iso20022CodeInfo, Iso20022CodeSetInfo,",
        "  MessageDefinitionInfo, RawRow,",
        '} from "./model.js";',
        'export type * from "./model.js";',
    ]
    aliases: dict[str, list[str]] = {}
    for label, names in ts_shards.items():
        aliases[label] = []
        for name in names:
            alias = f"{name}Rows"
            aliases[label].append(alias)
            lines.append(f'import {{ rows as {alias} }} from "./data/{name}.js";')
    lines.extend(
        [
            "",
            f"export const DATA_FINGERPRINT = {ts_string(digest)} as const;",
            f"export const EXTERNAL_CODE_SETS_VERSION = {ts_string(EXTERNAL_CODE_SETS_VERSION)} as const;",
            f"export const EXTERNAL_CODE_SETS_ARTIFACT_VERSION = {ts_string(EXTERNAL_CODE_SETS_ARTIFACT_VERSION)} as const;",
            f"export const BANK_TRANSACTION_CODES_VERSION = {ts_string(BANK_TRANSACTION_CODES_VERSION)} as const;",
            f"export const MESSAGE_DEFINITIONS_VERSION = {ts_string(MESSAGE_DEFINITIONS_VERSION)} as const;",
            "",
        ]
    )
    ts_dataset_names = {
        "code_sets": "codeSetsRows",
        "external_codes": "externalCodesRows",
        "bank_transaction_codes": "bankTransactionCodesRows",
        "message_definitions": "messageDefinitionsRows",
    }
    for label, names in aliases.items():
        lines.append(f"const {ts_dataset_names[label]}: readonly RawRow[] = Object.freeze([")
        for name in names:
            lines.append(f"  ...{name},")
        lines.append("]);")
    icon_items = ", ".join(
        f"[{ts_string(family.code_set)}, {ts_string(family.material_symbol)}]"
        for family in PAYMENT_FAMILIES
    )
    lines.extend(
        [
            "",
            f"const materialSymbolBySet = new Map<string, string>([{icon_items}]);",
            "const optional = (value: string): string | null => value || null;",
            "const sources = (value: string): readonly string[] => Object.freeze(value.split('|').filter(Boolean));",
            "const key = (value: string): string => value.trim().toLowerCase();",
            "const composite = (...values: readonly string[]): string => values.map(key).join('\\u0000');",
            "",
            "export const codeSets: readonly Iso20022CodeSetInfo[] = Object.freeze(codeSetsRows.map((row) =>",
            "  Object.freeze({ codeSet: row[0]!, definition: row[1]!, status: row[2]! as 'registered' | 'obsolete' | 'provisionally_registered',",
            "    sources: sources(row[3]!), isCurrent: row[2] !== 'obsolete' }),",
            "));",
            "export const externalCodeRecords: readonly Iso20022CodeInfo[] = Object.freeze(externalCodesRows.map((row) =>",
            "  Object.freeze({",
            "    codeSet: row[0]!, code: row[1]!, name: row[2]!, label: row[3]!, definition: row[4]!,",
            "    requester: optional(row[5]!), status: row[6]! as 'registered' | 'obsolete',",
            "    lastUpdated: optional(row[7]!), creationDate: optional(row[8]!), replacedBy: optional(row[9]!),",
            "    mappingStandard1: optional(row[10]!), mappingValue1: optional(row[11]!),",
            "    mappingStandard2: optional(row[12]!), mappingValue2: optional(row[13]!),",
            "    additionalInformation: optional(row[14]!), sources: sources(row[15]!),",
            "    materialSymbol: materialSymbolBySet.get(row[0]!) ?? 'code', isCurrent: row[6] === 'registered',",
            "  }),",
            "));",
            "export const currentExternalCodes = Object.freeze(externalCodeRecords.filter((item) => item.isCurrent));",
            "export const bankTransactionCodeRecords: readonly BankTransactionCodeInfo[] = Object.freeze(",
            "  bankTransactionCodesRows.map((row) => Object.freeze({",
            "    domainCode: row[0]!, domainName: row[1]!, familyCode: row[2]!, familyName: row[3]!,",
            "    subfamilyCode: row[4]!, subfamilyName: row[5]!, status: row[6]!, statusDate: row[7]!,",
            "    code: `${row[0]!}-${row[2]!}-${row[4]!}` ,",
            "  })),",
            ");",
            "export const messageDefinitions: readonly MessageDefinitionInfo[] = Object.freeze(",
            "  messageDefinitionsRows.map((row) => Object.freeze({",
            "    businessArea: row[0]!, messageId: row[1]!, messageNumber: row[2]!, variant: row[3]!,",
            "    version: row[4]!, name: row[5]!,",
            "  })),",
            ");",
            "",
            "export const codeSetCount = codeSets.length;",
            "export const externalCodeRecordCount = externalCodeRecords.length;",
            "export const currentExternalCodeCount = currentExternalCodes.length;",
            "export const externalCodeIdentityCount = new Set(externalCodeRecords.map((item) => composite(item.codeSet, item.code))).size;",
            "export const bankTransactionCodeRecordCount = bankTransactionCodeRecords.length;",
            "export const bankTransactionCodeIdentityCount = new Set(bankTransactionCodeRecords.map((item) => composite(item.domainCode, item.familyCode, item.subfamilyCode))).size;",
            "export const messageDefinitionCount = messageDefinitions.length;",
            f"export const paymentCodeCount = {EXPECTED_PAYMENT_CURRENT};",
            "",
            "const codeSetByName = new Map(codeSets.map((item) => [key(item.codeSet), item]));",
            "const externalByKey = new Map<string, Iso20022CodeInfo[]>();",
            "const externalByCode = new Map<string, Iso20022CodeInfo[]>();",
            "for (const item of externalCodeRecords) {",
            "  const qualified = composite(item.codeSet, item.code);",
            "  externalByKey.set(qualified, [...(externalByKey.get(qualified) ?? []), item]);",
            "  externalByCode.set(key(item.code), [...(externalByCode.get(key(item.code)) ?? []), item]);",
            "}",
            "for (const [indexKey, values] of externalByKey) externalByKey.set(indexKey, Object.freeze(values) as Iso20022CodeInfo[]);",
            "for (const [indexKey, values] of externalByCode) externalByCode.set(indexKey, Object.freeze(values) as Iso20022CodeInfo[]);",
            "",
            "export function resolveCodeSet(codeSet: string, options: { readonly includeObsolete?: boolean } = {}): Iso20022CodeSetInfo | undefined {",
            "  const item = codeSetByName.get(key(codeSet));",
            "  return item && (options.includeObsolete || item.isCurrent) ? item : undefined;",
            "}",
            "export function recordsFor(codeSet: string, code: string, options: { readonly includeObsolete?: boolean } = {}): readonly Iso20022CodeInfo[] {",
            "  const values = externalByKey.get(composite(codeSet, code)) ?? [];",
            "  return options.includeObsolete ? values : Object.freeze(values.filter((item) => item.isCurrent));",
            "}",
            "export function resolveCode(codeSet: string, code: string, options: { readonly includeObsolete?: boolean } = {}): Iso20022CodeInfo | undefined {",
            "  const current = recordsFor(codeSet, code);",
            "  return current[0] ?? (options.includeObsolete ? recordsFor(codeSet, code, { includeObsolete: true })[0] : undefined);",
            "}",
            "export function findCodes(code: string, options: { readonly includeObsolete?: boolean } = {}): readonly Iso20022CodeInfo[] {",
            "  const values = externalByCode.get(key(code)) ?? [];",
            "  return options.includeObsolete ? values : Object.freeze(values.filter((item) => item.isCurrent));",
            "}",
            "export function searchCodes(query: string, options: { readonly codeSet?: string; readonly includeObsolete?: boolean; readonly limit?: number } = {}): readonly Iso20022CodeInfo[] {",
            "  const needle = key(query);",
            "  if (!needle || (options.limit !== undefined && options.limit <= 0)) return Object.freeze([]);",
            "  const setKey = options.codeSet === undefined ? undefined : key(options.codeSet);",
            "  const found: Iso20022CodeInfo[] = [];",
            "  for (const item of externalCodeRecords) {",
            "    if (!options.includeObsolete && !item.isCurrent) continue;",
            "    if (setKey !== undefined && key(item.codeSet) !== setKey) continue;",
            "    const text = [item.code, item.name, item.label, item.definition, item.additionalInformation ?? ''].join('\\n').toLowerCase();",
            "    if (text.includes(needle)) { found.push(item); if (options.limit !== undefined && found.length >= options.limit) break; }",
            "  }",
            "  return Object.freeze(found);",
            "}",
            "",
            "const btcByKey = new Map<string, BankTransactionCodeInfo[]>();",
            "for (const item of bankTransactionCodeRecords) {",
            "  const itemKey = composite(item.domainCode, item.familyCode, item.subfamilyCode);",
            "  btcByKey.set(itemKey, [...(btcByKey.get(itemKey) ?? []), item]);",
            "}",
            "for (const [indexKey, values] of btcByKey) btcByKey.set(indexKey, Object.freeze(values) as BankTransactionCodeInfo[]);",
            "export function resolveBankTransactionCode(domainCode: string, familyCode: string, subfamilyCode: string): readonly BankTransactionCodeInfo[] {",
            "  return btcByKey.get(composite(domainCode, familyCode, subfamilyCode)) ?? Object.freeze([]);",
            "}",
            "export function findBankTransactionCodes(domainCode: string, options: { readonly familyCode?: string; readonly subfamilyCode?: string } = {}): readonly BankTransactionCodeInfo[] {",
            "  const domain = key(domainCode); const family = options.familyCode === undefined ? undefined : key(options.familyCode);",
            "  const subfamily = options.subfamilyCode === undefined ? undefined : key(options.subfamilyCode);",
            "  return Object.freeze(bankTransactionCodeRecords.filter((item) => key(item.domainCode) === domain",
            "    && (family === undefined || key(item.familyCode) === family)",
            "    && (subfamily === undefined || key(item.subfamilyCode) === subfamily)));",
            "}",
            "",
            "const messageById = new Map(messageDefinitions.map((item) => [key(item.messageId), item]));",
            "export function resolveMessageIdentifier(messageId: string): MessageDefinitionInfo | undefined {",
            "  return messageById.get(key(messageId));",
            "}",
            "export function findMessageDefinitions(options: { readonly businessArea?: string; readonly messageNumber?: string } = {}): readonly MessageDefinitionInfo[] {",
            "  const area = options.businessArea === undefined ? undefined : key(options.businessArea);",
            "  const number = options.messageNumber === undefined ? undefined : key(options.messageNumber);",
            "  return Object.freeze(messageDefinitions.filter((item) => (area === undefined || key(item.businessArea) === area)",
            "    && (number === undefined || key(item.messageNumber) === number)));",
            "}",
        ]
    )
    return "\n".join(lines)


def _dart_shards(
    label: str,
    rows: Sequence[dict[str, str]],
    columns: Sequence[str],
    digest: str,
) -> tuple[dict[str, str], list[str]]:
    chunks = _chunks(rows, columns, dart_string)
    outputs: dict[str, str] = {}
    names: list[str] = []
    for index, chunk in enumerate(chunks):
        name = f"{label}_{index:02d}"
        names.append(name)
        variable = f"_{_dart_dataset_name(label)}Rows{index:02d}"
        body = [
            f"// Generated ISO 20022 {label} shard. Do not edit by hand.",
            f"// Input SHA-256: {digest}",
            "// ignore_for_file: require_trailing_commas",
            "part of '../generated.dart';",
            "",
            f"const List<List<String>> {variable} = <List<String>>[",
        ]
        body.extend(f"  <String>{literal}," for literal in chunk)
        body.append("];")
        outputs[f"lib/src/data/{name}.dart"] = "\n".join(body)
    return outputs, names


def _dart_enum(family: PaymentFamily, codes: Sequence[str], digest: str) -> str:
    lines = [
        f"// Generated {family.public_name}. Do not edit by hand.",
        f"// Input SHA-256: {digest}",
        "// ignore_for_file: require_trailing_commas",
        "part of 'generated.dart';",
        "",
        f"enum {family.public_name} {{",
    ]
    for index, code in enumerate(codes):
        suffix = ";" if index == len(codes) - 1 else ","
        lines.append(f"  {_dart_member(code)}({dart_string(code)}){suffix}")
    lines.extend(
        [
            "",
            f"  const {family.public_name}(this.code);",
            "  final String code;",
            f"  Iso20022CodeInfo get info => resolveCode({dart_string(family.code_set)}, code)!;",
            "  String get label => info.label;",
            "  IconData get icon => info.icon;",
            f"  static {family.public_name}? tryParse(String code) =>",
            f"      _{_dart_dataset_name(family.dart_module)}ByCode[_key(code)];",
            "}",
            "",
            f"final Map<String, {family.public_name}> _{_dart_dataset_name(family.dart_module)}ByCode = Map.unmodifiable(<String, {family.public_name}>{{",
            f"  for (final value in {family.public_name}.values) _key(value.code): value,",
            "});",
        ]
    )
    return "\n".join(lines)


def _dart_runtime(dart_shards: dict[str, list[str]], digest: str, btc_count: int) -> str:
    lines = [
        "// Generated offline ISO 20022 catalogs. Do not edit by hand.",
        f"// Input SHA-256: {digest}",
        "// ignore_for_file: require_trailing_commas",
        "",
        "import 'package:flutter/material.dart';",
        "",
    ]
    for label, names in dart_shards.items():
        for name in names:
            lines.append(f"part 'data/{name}.dart';")
    for family in PAYMENT_FAMILIES:
        lines.append(f"part '{family.dart_module}.dart';")
    lines.extend(
        [
            "",
            f"const String dataFingerprint = {dart_string(digest)};",
            "// ignore: constant_identifier_names",
            "const String DATA_FINGERPRINT = dataFingerprint;",
            f"const String externalCodeSetsVersion = {dart_string(EXTERNAL_CODE_SETS_VERSION)};",
            f"const String externalCodeSetsArtifactVersion = {dart_string(EXTERNAL_CODE_SETS_ARTIFACT_VERSION)};",
            f"const String bankTransactionCodesVersion = {dart_string(BANK_TRANSACTION_CODES_VERSION)};",
            f"const String messageDefinitionsVersion = {dart_string(MESSAGE_DEFINITIONS_VERSION)};",
            "",
            "enum Iso20022CodeStatus { registered, obsolete }",
            "",
            "final class Iso20022CodeSetInfo {",
            "  const Iso20022CodeSetInfo({required this.codeSet, required this.definition, required this.status, required this.sources});",
            "  final String codeSet; final String definition; final String status; final List<String> sources;",
            "  bool get isCurrent => status != 'obsolete';",
            "}",
            "",
            "final class Iso20022CodeInfo {",
            "  const Iso20022CodeInfo({",
            "    required this.codeSet, required this.code, required this.name, required this.label,",
            "    required this.definition, required this.requester, required this.status,",
            "    required this.lastUpdated, required this.creationDate, required this.replacedBy,",
            "    required this.mappingStandard1, required this.mappingValue1,",
            "    required this.mappingStandard2, required this.mappingValue2,",
            "    required this.additionalInformation, required this.sources, required this.icon,",
            "  });",
            "  final String codeSet; final String code; final String name; final String label; final String definition;",
            "  final String? requester; final Iso20022CodeStatus status; final DateTime? lastUpdated; final DateTime? creationDate;",
            "  final String? replacedBy; final String? mappingStandard1; final String? mappingValue1;",
            "  final String? mappingStandard2; final String? mappingValue2; final String? additionalInformation;",
            "  final List<String> sources; final IconData icon;",
            "  bool get isCurrent => status == Iso20022CodeStatus.registered;",
            "}",
            "",
            "final class BankTransactionCodeInfo {",
            "  const BankTransactionCodeInfo({required this.domainCode, required this.domainName, required this.familyCode, required this.familyName, required this.subfamilyCode, required this.subfamilyName, required this.status, required this.statusDate});",
            "  final String domainCode; final String domainName; final String familyCode; final String familyName;",
            "  final String subfamilyCode; final String subfamilyName; final String status; final DateTime statusDate;",
            "  String get code => '$domainCode-$familyCode-$subfamilyCode';",
            "}",
            "",
            "final class MessageDefinitionInfo {",
            "  const MessageDefinitionInfo({required this.businessArea, required this.messageId, required this.messageNumber, required this.variant, required this.version, required this.name});",
            "  final String businessArea; final String messageId; final String messageNumber; final String variant;",
            "  final String version; final String name;",
            "}",
            "",
        ]
    )
    for label, names in dart_shards.items():
        dart_label = _dart_dataset_name(label)
        rows = ", ".join(f"..._{dart_label}Rows{index:02d}" for index, _ in enumerate(names))
        lines.append(f"const List<List<String>> _{dart_label}Rows = <List<String>>[{rows}];")
    icon_cases = "\n".join(
        f"    {dart_string(family.code_set)} => Icons.{family.material_symbol},"
        for family in PAYMENT_FAMILIES
    )
    lines.extend(
        [
            "",
            "String? _optional(String value) => value.isEmpty ? null : value;",
            "DateTime? _date(String value) => value.isEmpty ? null : DateTime.parse(value);",
            "List<String> _sources(String value) => List.unmodifiable(value.split('|').where((item) => item.isNotEmpty));",
            "String _key(String value) => value.trim().toLowerCase();",
            "String _composite(Iterable<String> values) => values.map(_key).join('\\u0000');",
            "IconData _iconForSet(String codeSet) => switch (codeSet) {",
            icon_cases,
            "    _ => Icons.code,",
            "  };",
            "",
            "final List<Iso20022CodeSetInfo> codeSets = List.unmodifiable(_codeSetsRows.map((row) => Iso20022CodeSetInfo(",
            "  codeSet: row[0], definition: row[1], status: row[2], sources: _sources(row[3]),",
            ")));",
            "final List<Iso20022CodeInfo> externalCodeRecords = List.unmodifiable(_externalCodesRows.map((row) => Iso20022CodeInfo(",
            "  codeSet: row[0], code: row[1], name: row[2], label: row[3], definition: row[4], requester: _optional(row[5]),",
            "  status: Iso20022CodeStatus.values.byName(row[6]), lastUpdated: _date(row[7]), creationDate: _date(row[8]),",
            "  replacedBy: _optional(row[9]), mappingStandard1: _optional(row[10]), mappingValue1: _optional(row[11]),",
            "  mappingStandard2: _optional(row[12]), mappingValue2: _optional(row[13]), additionalInformation: _optional(row[14]),",
            "  sources: _sources(row[15]), icon: _iconForSet(row[0]),",
            ")));",
            "final List<Iso20022CodeInfo> currentExternalCodes = List.unmodifiable(externalCodeRecords.where((item) => item.isCurrent));",
            "final List<BankTransactionCodeInfo> bankTransactionCodeRecords = List.unmodifiable(_bankTransactionCodesRows.map((row) => BankTransactionCodeInfo(",
            "  domainCode: row[0], domainName: row[1], familyCode: row[2], familyName: row[3],",
            "  subfamilyCode: row[4], subfamilyName: row[5], status: row[6], statusDate: DateTime.parse(row[7]),",
            ")));",
            "final List<MessageDefinitionInfo> messageDefinitions = List.unmodifiable(_messageDefinitionsRows.map((row) => MessageDefinitionInfo(",
            "  businessArea: row[0], messageId: row[1], messageNumber: row[2], variant: row[3], version: row[4],",
            "  name: row[5],",
            ")));",
            "",
            "final int codeSetCount = codeSets.length;",
            "final int externalCodeRecordCount = externalCodeRecords.length;",
            "final int currentExternalCodeCount = currentExternalCodes.length;",
            "final int externalCodeIdentityCount = externalCodeRecords.map((item) => _composite([item.codeSet, item.code])).toSet().length;",
            "final int bankTransactionCodeRecordCount = bankTransactionCodeRecords.length;",
            "final int bankTransactionCodeIdentityCount = bankTransactionCodeRecords.map((item) => _composite([item.domainCode, item.familyCode, item.subfamilyCode])).toSet().length;",
            "final int messageDefinitionCount = messageDefinitions.length;",
            f"const int paymentCodeCount = {EXPECTED_PAYMENT_CURRENT};",
            "",
            "final Map<String, Iso20022CodeSetInfo> _codeSetByName = Map.unmodifiable({for (final item in codeSets) _key(item.codeSet): item});",
            "final Map<String, List<Iso20022CodeInfo>> _externalByKey = _indexExternal((item) => _composite([item.codeSet, item.code]));",
            "final Map<String, List<Iso20022CodeInfo>> _externalByCode = _indexExternal((item) => _key(item.code));",
            "Map<String, List<Iso20022CodeInfo>> _indexExternal(String Function(Iso20022CodeInfo) selector) {",
            "  final mutable = <String, List<Iso20022CodeInfo>>{};",
            "  for (final item in externalCodeRecords) { mutable.putIfAbsent(selector(item), () => []).add(item); }",
            "  return Map.unmodifiable({for (final entry in mutable.entries) entry.key: List<Iso20022CodeInfo>.unmodifiable(entry.value)});",
            "}",
            "Iso20022CodeSetInfo? resolveCodeSet(String codeSet, {bool includeObsolete = false}) {",
            "  final item = _codeSetByName[_key(codeSet)]; return item != null && (includeObsolete || item.isCurrent) ? item : null;",
            "}",
            "List<Iso20022CodeInfo> recordsFor(String codeSet, String code, {bool includeObsolete = false}) {",
            "  final values = _externalByKey[_composite([codeSet, code])] ?? const <Iso20022CodeInfo>[];",
            "  return includeObsolete ? values : List.unmodifiable(values.where((item) => item.isCurrent));",
            "}",
            "Iso20022CodeInfo? resolveCode(String codeSet, String code, {bool includeObsolete = false}) {",
            "  final current = recordsFor(codeSet, code); if (current.isNotEmpty) return current.first;",
            "  if (!includeObsolete) return null; final history = recordsFor(codeSet, code, includeObsolete: true);",
            "  return history.isEmpty ? null : history.first;",
            "}",
            "List<Iso20022CodeInfo> findCodes(String code, {bool includeObsolete = false}) {",
            "  final values = _externalByCode[_key(code)] ?? const <Iso20022CodeInfo>[];",
            "  return includeObsolete ? values : List.unmodifiable(values.where((item) => item.isCurrent));",
            "}",
            "List<Iso20022CodeInfo> searchCodes(String query, {String? codeSet, bool includeObsolete = false, int? limit}) {",
            "  final needle = _key(query); if (needle.isEmpty || (limit != null && limit <= 0)) return const [];",
            "  final setKey = codeSet == null ? null : _key(codeSet); final found = <Iso20022CodeInfo>[];",
            "  for (final item in externalCodeRecords) {",
            "    if (!includeObsolete && !item.isCurrent) continue; if (setKey != null && _key(item.codeSet) != setKey) continue;",
            "    final text = [item.code, item.name, item.label, item.definition, item.additionalInformation ?? ''].join('\\n').toLowerCase();",
            "    if (text.contains(needle)) { found.add(item); if (limit != null && found.length >= limit) break; }",
            "  } return List.unmodifiable(found);",
            "}",
            "",
            "final Map<String, List<BankTransactionCodeInfo>> _btcByKey = _indexBtc();",
            "Map<String, List<BankTransactionCodeInfo>> _indexBtc() {",
            "  final mutable = <String, List<BankTransactionCodeInfo>>{}; for (final item in bankTransactionCodeRecords) {",
            "    mutable.putIfAbsent(_composite([item.domainCode, item.familyCode, item.subfamilyCode]), () => []).add(item);",
            "  } return Map.unmodifiable({for (final entry in mutable.entries) entry.key: List<BankTransactionCodeInfo>.unmodifiable(entry.value)});",
            "}",
            "List<BankTransactionCodeInfo> resolveBankTransactionCode(String domainCode, String familyCode, String subfamilyCode) =>",
            "  _btcByKey[_composite([domainCode, familyCode, subfamilyCode])] ?? const [];",
            "List<BankTransactionCodeInfo> findBankTransactionCodes(String domainCode, {String? familyCode, String? subfamilyCode}) {",
            "  final domain = _key(domainCode); final family = familyCode == null ? null : _key(familyCode);",
            "  final subfamily = subfamilyCode == null ? null : _key(subfamilyCode);",
            "  return List.unmodifiable(bankTransactionCodeRecords.where((item) => _key(item.domainCode) == domain",
            "    && (family == null || _key(item.familyCode) == family) && (subfamily == null || _key(item.subfamilyCode) == subfamily)));",
            "}",
            "",
            "final Map<String, MessageDefinitionInfo> _messageById = Map.unmodifiable({for (final item in messageDefinitions) _key(item.messageId): item});",
            "MessageDefinitionInfo? resolveMessageIdentifier(String messageId) => _messageById[_key(messageId)];",
            "List<MessageDefinitionInfo> findMessageDefinitions({String? businessArea, String? messageNumber}) {",
            "  final area = businessArea == null ? null : _key(businessArea); final number = messageNumber == null ? null : _key(messageNumber);",
            "  return List.unmodifiable(messageDefinitions.where((item) => (area == null || _key(item.businessArea) == area)",
            "    && (number == null || _key(item.messageNumber) == number)));",
            "}",
        ]
    )
    return "\n".join(lines)


def _package_outputs(
    code_sets: list[dict[str, str]],
    external: list[dict[str, str]],
    btc: list[dict[str, str]],
    messages: list[dict[str, str]],
    digest: str,
) -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    py_root = ROOT / "packages/python/reffin_iso20022/src/reffin_iso20022"
    ts_root = ROOT / "packages/typescript/reffin_iso20022/src"
    dart_root = ROOT / "packages/flutter/reffin_iso20022"

    datasets = (
        ("code_sets", code_sets, CODE_SET_COLUMNS),
        ("external_codes", external, EXTERNAL_CODE_COLUMNS),
        ("bank_transaction_codes", btc, BTC_COLUMNS),
        ("message_definitions", messages, MESSAGE_COLUMNS),
    )
    py_names: dict[str, list[str]] = {}
    ts_names: dict[str, list[str]] = {}
    dart_names: dict[str, list[str]] = {}
    for label, rows, columns in datasets:
        generated, names = _python_shards(label, rows, columns, digest)
        py_names[label] = names
        outputs.update({py_root / path: content for path, content in generated.items()})
        generated, names = _ts_shards(label, rows, columns, digest)
        ts_names[label] = names
        outputs.update({ts_root / path: content for path, content in generated.items()})
        generated, names = _dart_shards(label, rows, columns, digest)
        dart_names[label] = names
        outputs.update({dart_root / path: content for path, content in generated.items()})

    outputs[py_root / "_model.py"] = _python_model(digest)
    outputs[ts_root / "model.ts"] = _ts_model(digest)
    for family in PAYMENT_FAMILIES:
        codes = [
            row["code"]
            for row in external
            if row["code_set"] == family.code_set and row["status"] == "registered"
        ]
        outputs[py_root / f"{family.python_module}.py"] = _python_enum(family, codes, digest)
        outputs[ts_root / f"{family.typescript_module}.ts"] = _ts_enum(family, codes, digest)
        outputs[dart_root / "lib/src" / f"{family.dart_module}.dart"] = _dart_enum(
            family, codes, digest
        )
    outputs[py_root / "_generated.py"] = _python_runtime(py_names, digest, len(btc))
    outputs[ts_root / "generated.ts"] = _ts_runtime(ts_names, digest, len(btc))
    outputs[dart_root / "lib/src/generated.dart"] = _dart_runtime(
        dart_names, digest, len(btc)
    )
    exports = ['export * from "./generated.js";']
    exports.extend(
        f'export * from "./{family.typescript_module}.js";' for family in PAYMENT_FAMILIES
    )
    outputs[ts_root / "index.ts"] = "\n".join(exports)
    return outputs


def _generated_candidates() -> set[Path]:
    candidates: set[Path] = set()
    roots = (
        ROOT / "packages/python/reffin_iso20022/src/reffin_iso20022",
        ROOT / "packages/typescript/reffin_iso20022/src",
        ROOT / "packages/flutter/reffin_iso20022/lib/src",
    )
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix not in {".py", ".ts", ".dart"}:
                continue
            if path.name in {"__init__.py", "index.ts"}:
                continue
            try:
                first_line = path.open(encoding="utf-8").readline()
            except OSError:
                continue
            if "Generated" in first_line:
                candidates.add(path)
    return candidates


def generate(check: bool = False) -> list[Path]:
    code_sets, external, btc, messages = _load()
    inputs = [
        CODE_SETS_PATH,
        EXTERNAL_CODES_PATH,
        BTC_PATH,
        MESSAGES_PATH,
        SOURCES_PATH,
    ]
    readme = DATA_DIR / "README.md"
    if readme.exists():
        inputs.append(readme)
    digest = fingerprint(inputs)
    outputs = _package_outputs(code_sets, external, btc, messages, digest)
    stale = [path for path, content in outputs.items() if not write_or_check(path, content, check)]
    unexpected = _generated_candidates() - set(outputs)
    if check:
        stale.extend(sorted(unexpected))
    else:
        for path in unexpected:
            path.unlink()
    if not stale:
        action = "verified" if check else "generated"
        print(
            f"{action} ISO 20022: {len(code_sets):,} sets; {len(external):,} external rows; "
            f"{len(btc):,} BTC rows; {len(messages):,} messages; input {digest[:12]}"
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
