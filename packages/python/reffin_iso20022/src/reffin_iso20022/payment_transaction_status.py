"""Generated PaymentTransactionStatusCode. Do not edit by hand."""
# Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
from __future__ import annotations

from enum import Enum
from typing import Self, cast

from ._model import Iso20022CodeInfo


class PaymentTransactionStatusCode(str, Enum):
    ACCC = 'ACCC'
    ACCP = 'ACCP'
    ACFC = 'ACFC'
    ACFW = 'ACFW'
    ACIS = 'ACIS'
    ACPD = 'ACPD'
    ACSC = 'ACSC'
    ACSP = 'ACSP'
    ACTC = 'ACTC'
    ACWC = 'ACWC'
    ACWP = 'ACWP'
    BLCK = 'BLCK'
    CANC = 'CANC'
    CPUC = 'CPUC'
    PATC = 'PATC'
    PDNG = 'PDNG'
    PRES = 'PRES'
    RCVC = 'RCVC'
    RCVD = 'RCVD'
    RJCT = 'RJCT'
    RVCM = 'RVCM'
    RVMC = 'RVMC'
    RVNA = 'RVNA'
    RVNC = 'RVNC'
    RVNM = 'RVNM'

    @property
    def code(self) -> str:
        return str(self.value)

    @property
    def info(self) -> Iso20022CodeInfo:
        from ._generated import resolve_code

        return cast(Iso20022CodeInfo, resolve_code('ExternalPaymentTransactionStatus1Code', self.value))

    @property
    def label(self) -> str:
        return self.info.label

    @property
    def material_symbol(self) -> str:
        return self.info.material_symbol

    @classmethod
    def try_parse(cls, code: object) -> Self | None:
        if isinstance(code, cls):
            return code
        if not isinstance(code, str):
            return None
        normalized = code.strip().casefold()
        return next((value for value in cls if value.value.casefold() == normalized), None)
