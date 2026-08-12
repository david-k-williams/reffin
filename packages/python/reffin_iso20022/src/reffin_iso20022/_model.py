"""Generated ISO 20022 value models. Do not edit by hand."""
# Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
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
