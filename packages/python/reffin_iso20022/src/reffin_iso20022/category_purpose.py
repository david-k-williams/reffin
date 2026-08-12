"""Generated CategoryPurposeCode. Do not edit by hand."""
# Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
from __future__ import annotations

from enum import Enum
from typing import Self, cast

from ._model import Iso20022CodeInfo


class CategoryPurposeCode(str, Enum):
    BONU = 'BONU'
    CASH = 'CASH'
    CBLK = 'CBLK'
    CCRD = 'CCRD'
    CDIS = 'CDIS'
    CGWV = 'CGWV'
    CIPC = 'CIPC'
    CONC = 'CONC'
    CORT = 'CORT'
    CPAY = 'CPAY'
    CRYP = 'CRYP'
    CTDF = 'CTDF'
    DCRD = 'DCRD'
    DIVI = 'DIVI'
    DVPM = 'DVPM'
    EPAY = 'EPAY'
    FCDT = 'FCDT'
    FCIN = 'FCIN'
    FCOL = 'FCOL'
    GOVT = 'GOVT'
    GP2P = 'GP2P'
    HEDG = 'HEDG'
    ICCP = 'ICCP'
    IDCP = 'IDCP'
    INTC = 'INTC'
    INTE = 'INTE'
    LBOX = 'LBOX'
    LOAN = 'LOAN'
    MP2B = 'MP2B'
    MP2P = 'MP2P'
    OTHR = 'OTHR'
    PENS = 'PENS'
    RPRE = 'RPRE'
    RRCT = 'RRCT'
    RVPM = 'RVPM'
    SALA = 'SALA'
    SAVG = 'SAVG'
    SECU = 'SECU'
    SSBE = 'SSBE'
    SUPP = 'SUPP'
    SWEP = 'SWEP'
    TAXS = 'TAXS'
    TOPG = 'TOPG'
    TRAD = 'TRAD'
    TREA = 'TREA'
    VATX = 'VATX'
    VOST = 'VOST'
    WHLD = 'WHLD'
    ZABA = 'ZABA'

    @property
    def code(self) -> str:
        return str(self.value)

    @property
    def info(self) -> Iso20022CodeInfo:
        from ._generated import resolve_code

        return cast(Iso20022CodeInfo, resolve_code('ExternalCategoryPurpose1Code', self.value))

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
