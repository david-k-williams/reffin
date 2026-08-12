"""Generated offline ISO 20022 catalogs. Do not edit by hand."""
# Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
from __future__ import annotations

from datetime import date
from types import MappingProxyType
from typing import Final, Mapping

from ._model import (
    BankTransactionCodeInfo, Iso20022CodeInfo, Iso20022CodeSetInfo,
    Iso20022CodeStatus, MessageDefinitionInfo,
)
from ._code_sets_00 import ROWS as _CODE_SETS_00_ROWS
from ._external_codes_00 import ROWS as _EXTERNAL_CODES_00_ROWS
from ._external_codes_01 import ROWS as _EXTERNAL_CODES_01_ROWS
from ._external_codes_02 import ROWS as _EXTERNAL_CODES_02_ROWS
from ._external_codes_03 import ROWS as _EXTERNAL_CODES_03_ROWS
from ._external_codes_04 import ROWS as _EXTERNAL_CODES_04_ROWS
from ._external_codes_05 import ROWS as _EXTERNAL_CODES_05_ROWS
from ._external_codes_06 import ROWS as _EXTERNAL_CODES_06_ROWS
from ._external_codes_07 import ROWS as _EXTERNAL_CODES_07_ROWS
from ._external_codes_08 import ROWS as _EXTERNAL_CODES_08_ROWS
from ._external_codes_09 import ROWS as _EXTERNAL_CODES_09_ROWS
from ._external_codes_10 import ROWS as _EXTERNAL_CODES_10_ROWS
from ._external_codes_11 import ROWS as _EXTERNAL_CODES_11_ROWS
from ._external_codes_12 import ROWS as _EXTERNAL_CODES_12_ROWS
from ._external_codes_13 import ROWS as _EXTERNAL_CODES_13_ROWS
from ._external_codes_14 import ROWS as _EXTERNAL_CODES_14_ROWS
from ._external_codes_15 import ROWS as _EXTERNAL_CODES_15_ROWS
from ._external_codes_16 import ROWS as _EXTERNAL_CODES_16_ROWS
from ._external_codes_17 import ROWS as _EXTERNAL_CODES_17_ROWS
from ._external_codes_18 import ROWS as _EXTERNAL_CODES_18_ROWS
from ._external_codes_19 import ROWS as _EXTERNAL_CODES_19_ROWS
from ._bank_transaction_codes_00 import ROWS as _BANK_TRANSACTION_CODES_00_ROWS
from ._bank_transaction_codes_01 import ROWS as _BANK_TRANSACTION_CODES_01_ROWS
from ._bank_transaction_codes_02 import ROWS as _BANK_TRANSACTION_CODES_02_ROWS
from ._bank_transaction_codes_03 import ROWS as _BANK_TRANSACTION_CODES_03_ROWS
from ._message_definitions_00 import ROWS as _MESSAGE_DEFINITIONS_00_ROWS
from ._message_definitions_01 import ROWS as _MESSAGE_DEFINITIONS_01_ROWS

DATA_FINGERPRINT: Final[str] = '19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80'
EXTERNAL_CODE_SETS_VERSION: Final[str] = 'May 2026 v1'
EXTERNAL_CODE_SETS_ARTIFACT_VERSION: Final[str] = '1Q2026_externalcodesets_v1'
BANK_TRANSACTION_CODES_VERSION: Final[str] = '2025-11-30'
MESSAGE_DEFINITIONS_VERSION: Final[str] = '2026-06-26'

_CODE_SETS_ROWS = _CODE_SETS_00_ROWS
_EXTERNAL_CODES_ROWS = _EXTERNAL_CODES_00_ROWS + _EXTERNAL_CODES_01_ROWS + _EXTERNAL_CODES_02_ROWS + _EXTERNAL_CODES_03_ROWS + _EXTERNAL_CODES_04_ROWS + _EXTERNAL_CODES_05_ROWS + _EXTERNAL_CODES_06_ROWS + _EXTERNAL_CODES_07_ROWS + _EXTERNAL_CODES_08_ROWS + _EXTERNAL_CODES_09_ROWS + _EXTERNAL_CODES_10_ROWS + _EXTERNAL_CODES_11_ROWS + _EXTERNAL_CODES_12_ROWS + _EXTERNAL_CODES_13_ROWS + _EXTERNAL_CODES_14_ROWS + _EXTERNAL_CODES_15_ROWS + _EXTERNAL_CODES_16_ROWS + _EXTERNAL_CODES_17_ROWS + _EXTERNAL_CODES_18_ROWS + _EXTERNAL_CODES_19_ROWS
_BANK_TRANSACTION_CODES_ROWS = _BANK_TRANSACTION_CODES_00_ROWS + _BANK_TRANSACTION_CODES_01_ROWS + _BANK_TRANSACTION_CODES_02_ROWS + _BANK_TRANSACTION_CODES_03_ROWS
_MESSAGE_DEFINITIONS_ROWS = _MESSAGE_DEFINITIONS_00_ROWS + _MESSAGE_DEFINITIONS_01_ROWS

_MATERIAL_SYMBOL_BY_SET = {'ExternalPurpose1Code': 'payments', 'ExternalStatusReason1Code': 'error_outline', 'ExternalReturnReason1Code': 'undo', 'ExternalLocalInstrument1Code': 'account_balance', 'ExternalCategoryPurpose1Code': 'category', 'ExternalServiceLevel1Code': 'speed', 'ExternalPaymentTransactionStatus1Code': 'sync', 'ExternalPaymentGroupStatus1Code': 'fact_check'}


def _optional(value: str) -> str | None:
    return value or None


def _date(value: str) -> date | None:
    return date.fromisoformat(value) if value else None


def _sources(value: str) -> tuple[str, ...]:
    return tuple(part for part in value.split('|') if part)


CODE_SETS: Final = tuple(
    Iso20022CodeSetInfo(code_set, definition, status, _sources(source))
    for code_set, definition, status, source in _CODE_SETS_ROWS
)
EXTERNAL_CODE_RECORDS: Final = tuple(
    Iso20022CodeInfo(
        code_set=row[0], code=row[1], name=row[2], label=row[3], definition=row[4],
        requester=_optional(row[5]), status=Iso20022CodeStatus(row[6]),
        last_updated=_date(row[7]), creation_date=_date(row[8]),
        replaced_by=_optional(row[9]), mapping_standard_1=_optional(row[10]),
        mapping_value_1=_optional(row[11]), mapping_standard_2=_optional(row[12]),
        mapping_value_2=_optional(row[13]), additional_information=_optional(row[14]),
        sources=_sources(row[15]), material_symbol=_MATERIAL_SYMBOL_BY_SET.get(row[0], 'code'),
    )
    for row in _EXTERNAL_CODES_ROWS
)
CURRENT_EXTERNAL_CODES: Final = tuple(record for record in EXTERNAL_CODE_RECORDS if record.is_current)
BANK_TRANSACTION_CODE_RECORDS: Final = tuple(
    BankTransactionCodeInfo(*row[:7], date.fromisoformat(row[7]))
    for row in _BANK_TRANSACTION_CODES_ROWS
)
MESSAGE_DEFINITIONS: Final = tuple(MessageDefinitionInfo(*row) for row in _MESSAGE_DEFINITIONS_ROWS)

CODE_SET_COUNT: Final = len(CODE_SETS)
EXTERNAL_CODE_RECORD_COUNT: Final = len(EXTERNAL_CODE_RECORDS)
CURRENT_EXTERNAL_CODE_COUNT: Final = len(CURRENT_EXTERNAL_CODES)
EXTERNAL_CODE_IDENTITY_COUNT: Final = len({(item.code_set, item.code) for item in EXTERNAL_CODE_RECORDS})
BANK_TRANSACTION_CODE_RECORD_COUNT: Final = len(BANK_TRANSACTION_CODE_RECORDS)
BANK_TRANSACTION_CODE_IDENTITY_COUNT: Final = len({
    (item.domain_code, item.family_code, item.subfamily_code)
    for item in BANK_TRANSACTION_CODE_RECORDS
})
MESSAGE_DEFINITION_COUNT: Final = len(MESSAGE_DEFINITIONS)
PAYMENT_CODE_COUNT: Final = 950


def _key(value: str) -> str:
    return value.strip().casefold()


_CODE_SET_BY_NAME: Final = MappingProxyType({_key(item.code_set): item for item in CODE_SETS})
_external_mutable: dict[tuple[str, str], list[Iso20022CodeInfo]] = {}
_external_by_code_mutable: dict[str, list[Iso20022CodeInfo]] = {}
for _record in EXTERNAL_CODE_RECORDS:
    _external_mutable.setdefault((_key(_record.code_set), _key(_record.code)), []).append(_record)
    _external_by_code_mutable.setdefault(_key(_record.code), []).append(_record)
_EXTERNAL_BY_KEY: Final = MappingProxyType({
    key: tuple(values) for key, values in _external_mutable.items()
})
_EXTERNAL_BY_CODE: Final = MappingProxyType({
    key: tuple(values) for key, values in _external_by_code_mutable.items()
})


def resolve_code_set(code_set: str, *, include_obsolete: bool = False) -> Iso20022CodeSetInfo | None:
    if not isinstance(code_set, str):
        return None
    info = _CODE_SET_BY_NAME.get(_key(code_set))
    return info if info is not None and (include_obsolete or info.is_current) else None


def records_for(
    code_set: str, code: str, *, include_obsolete: bool = False
) -> tuple[Iso20022CodeInfo, ...]:
    if not isinstance(code_set, str) or not isinstance(code, str):
        return ()
    values = _EXTERNAL_BY_KEY.get((_key(code_set), _key(code)), ())
    return values if include_obsolete else tuple(item for item in values if item.is_current)


def resolve_code(
    code_set: str, code: str, *, include_obsolete: bool = False
) -> Iso20022CodeInfo | None:
    current = records_for(code_set, code)
    if current:
        return current[0]
    if include_obsolete:
        history = records_for(code_set, code, include_obsolete=True)
        return history[0] if history else None
    return None


def find_codes(code: str, *, include_obsolete: bool = False) -> tuple[Iso20022CodeInfo, ...]:
    if not isinstance(code, str):
        return ()
    values = _EXTERNAL_BY_CODE.get(_key(code), ())
    return values if include_obsolete else tuple(item for item in values if item.is_current)


def search_codes(
    query: str, *, code_set: str | None = None, include_obsolete: bool = False,
    limit: int | None = None,
) -> tuple[Iso20022CodeInfo, ...]:
    if not isinstance(query, str) or not query.strip() or (limit is not None and limit <= 0):
        return ()
    needle = _key(query)
    set_key = _key(code_set) if isinstance(code_set, str) else None
    found: list[Iso20022CodeInfo] = []
    for item in EXTERNAL_CODE_RECORDS:
        if not include_obsolete and not item.is_current:
            continue
        if set_key is not None and _key(item.code_set) != set_key:
            continue
        haystack = '\n'.join((item.code, item.name, item.label, item.definition, item.additional_information or '')).casefold()
        if needle in haystack:
            found.append(item)
            if limit is not None and len(found) >= limit:
                break
    return tuple(found)


_btc_mutable: dict[tuple[str, str, str], list[BankTransactionCodeInfo]] = {}
for _record in BANK_TRANSACTION_CODE_RECORDS:
    _btc_mutable.setdefault(
        (_key(_record.domain_code), _key(_record.family_code), _key(_record.subfamily_code)), []
    ).append(_record)
_BTC_BY_KEY: Final = MappingProxyType({key: tuple(values) for key, values in _btc_mutable.items()})


def resolve_bank_transaction_code(
    domain_code: str, family_code: str, subfamily_code: str,
) -> tuple[BankTransactionCodeInfo, ...]:
    if not all(isinstance(value, str) for value in (domain_code, family_code, subfamily_code)):
        return ()
    return _BTC_BY_KEY.get((_key(domain_code), _key(family_code), _key(subfamily_code)), ())


def find_bank_transaction_codes(
    domain_code: str, *, family_code: str | None = None, subfamily_code: str | None = None,
) -> tuple[BankTransactionCodeInfo, ...]:
    if not isinstance(domain_code, str):
        return ()
    domain_key = _key(domain_code)
    family_key = _key(family_code) if isinstance(family_code, str) else None
    subfamily_key = _key(subfamily_code) if isinstance(subfamily_code, str) else None
    return tuple(
        item for item in BANK_TRANSACTION_CODE_RECORDS
        if _key(item.domain_code) == domain_key
        and (family_key is None or _key(item.family_code) == family_key)
        and (subfamily_key is None or _key(item.subfamily_code) == subfamily_key)
    )


_MESSAGE_BY_ID: Final[Mapping[str, MessageDefinitionInfo]] = MappingProxyType({
    _key(item.message_id): item for item in MESSAGE_DEFINITIONS
})


def resolve_message_identifier(message_id: str) -> MessageDefinitionInfo | None:
    return _MESSAGE_BY_ID.get(_key(message_id)) if isinstance(message_id, str) else None


def find_message_definitions(
    *, business_area: str | None = None, message_number: str | None = None,
) -> tuple[MessageDefinitionInfo, ...]:
    area_key = _key(business_area) if isinstance(business_area, str) else None
    number_key = _key(message_number) if isinstance(message_number, str) else None
    return tuple(
        item for item in MESSAGE_DEFINITIONS
        if (area_key is None or _key(item.business_area) == area_key)
        and (number_key is None or _key(item.message_number) == number_key)
    )
from .payment_purpose import PaymentPurposeCode
from .payment_status_reason import PaymentStatusReasonCode
from .payment_return_reason import PaymentReturnReasonCode
from .local_instrument import LocalInstrumentCode
from .category_purpose import CategoryPurposeCode
from .service_level import ServiceLevelCode
from .payment_transaction_status import PaymentTransactionStatusCode
from .payment_group_status import PaymentGroupStatusCode

__all__ = ['DATA_FINGERPRINT', 'EXTERNAL_CODE_SETS_VERSION', 'EXTERNAL_CODE_SETS_ARTIFACT_VERSION', 'BANK_TRANSACTION_CODES_VERSION', 'MESSAGE_DEFINITIONS_VERSION', 'Iso20022CodeStatus', 'Iso20022CodeSetInfo', 'Iso20022CodeInfo', 'BankTransactionCodeInfo', 'MessageDefinitionInfo', 'CODE_SETS', 'EXTERNAL_CODE_RECORDS', 'CURRENT_EXTERNAL_CODES', 'BANK_TRANSACTION_CODE_RECORDS', 'MESSAGE_DEFINITIONS', 'CODE_SET_COUNT', 'EXTERNAL_CODE_RECORD_COUNT', 'CURRENT_EXTERNAL_CODE_COUNT', 'EXTERNAL_CODE_IDENTITY_COUNT', 'BANK_TRANSACTION_CODE_RECORD_COUNT', 'BANK_TRANSACTION_CODE_IDENTITY_COUNT', 'MESSAGE_DEFINITION_COUNT', 'PAYMENT_CODE_COUNT', 'resolve_code_set', 'records_for', 'resolve_code', 'find_codes', 'search_codes', 'resolve_bank_transaction_code', 'find_bank_transaction_codes', 'resolve_message_identifier', 'find_message_definitions', 'PaymentPurposeCode', 'PaymentStatusReasonCode', 'PaymentReturnReasonCode', 'LocalInstrumentCode', 'CategoryPurposeCode', 'ServiceLevelCode', 'PaymentTransactionStatusCode', 'PaymentGroupStatusCode']
