"""Generated ServiceLevelCode. Do not edit by hand."""
# Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
from __future__ import annotations

from enum import Enum
from typing import Self, cast

from ._model import Iso20022CodeInfo


class ServiceLevelCode(str, Enum):
    BKTR = 'BKTR'
    EAPS = 'EAPS'
    EOLO = 'EOLO'
    G001 = 'G001'
    G002 = 'G002'
    G003 = 'G003'
    G004 = 'G004'
    G005 = 'G005'
    G006 = 'G006'
    G007 = 'G007'
    G009 = 'G009'
    INST = 'INST'
    IRCA = 'IRCA'
    NOLO = 'NOLO'
    NPCA = 'NPCA'
    NUGP = 'NUGP'
    NURG = 'NURG'
    PRPT = 'PRPT'
    SD01 = 'SD01'
    SDVA = 'SDVA'
    SEPA = 'SEPA'
    SPLI = 'SPLI'
    SPSC = 'SPSC'
    SRTP = 'SRTP'
    SVAT = 'SVAT'
    SVDE = 'SVDE'
    URGP = 'URGP'
    URNS = 'URNS'
    WFSM = 'WFSM'

    @property
    def code(self) -> str:
        return str(self.value)

    @property
    def info(self) -> Iso20022CodeInfo:
        from ._generated import resolve_code

        return cast(Iso20022CodeInfo, resolve_code('ExternalServiceLevel1Code', self.value))

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
