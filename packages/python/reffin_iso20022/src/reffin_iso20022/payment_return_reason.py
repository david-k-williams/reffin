"""Generated PaymentReturnReasonCode. Do not edit by hand."""
# Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
from __future__ import annotations

from enum import Enum
from typing import Self, cast

from ._model import Iso20022CodeInfo


class PaymentReturnReasonCode(str, Enum):
    AC01 = 'AC01'
    AC02 = 'AC02'
    AC03 = 'AC03'
    AC04 = 'AC04'
    AC06 = 'AC06'
    AC07 = 'AC07'
    AC13 = 'AC13'
    AC14 = 'AC14'
    AC15 = 'AC15'
    AC16 = 'AC16'
    AC17 = 'AC17'
    AG01 = 'AG01'
    AG02 = 'AG02'
    AG07 = 'AG07'
    AGNT = 'AGNT'
    AM01 = 'AM01'
    AM02 = 'AM02'
    AM03 = 'AM03'
    AM04 = 'AM04'
    AM05 = 'AM05'
    AM06 = 'AM06'
    AM07 = 'AM07'
    AM09 = 'AM09'
    AM10 = 'AM10'
    ARDT = 'ARDT'
    BE01 = 'BE01'
    BE04 = 'BE04'
    BE05 = 'BE05'
    BE06 = 'BE06'
    BE07 = 'BE07'
    BE08 = 'BE08'
    BE10 = 'BE10'
    BE11 = 'BE11'
    BE16 = 'BE16'
    BE17 = 'BE17'
    CN01 = 'CN01'
    CNOR = 'CNOR'
    CNPC = 'CNPC'
    CURR = 'CURR'
    CUST = 'CUST'
    DC04 = 'DC04'
    DNOR = 'DNOR'
    DS28 = 'DS28'
    DT01 = 'DT01'
    DT02 = 'DT02'
    DT04 = 'DT04'
    DUPL = 'DUPL'
    ED01 = 'ED01'
    ED03 = 'ED03'
    ED05 = 'ED05'
    EMVL = 'EMVL'
    ERIN = 'ERIN'
    FF03 = 'FF03'
    FF04 = 'FF04'
    FF05 = 'FF05'
    FF06 = 'FF06'
    FF07 = 'FF07'
    FOCR = 'FOCR'
    FR01 = 'FR01'
    FRTR = 'FRTR'
    G004 = 'G004'
    MD01 = 'MD01'
    MD02 = 'MD02'
    MD05 = 'MD05'
    MD06 = 'MD06'
    MD07 = 'MD07'
    MS02 = 'MS02'
    MS03 = 'MS03'
    NARR = 'NARR'
    NOAS = 'NOAS'
    NOCM = 'NOCM'
    NOOR = 'NOOR'
    PINL = 'PINL'
    RC01 = 'RC01'
    RC03 = 'RC03'
    RC04 = 'RC04'
    RC07 = 'RC07'
    RC08 = 'RC08'
    RC11 = 'RC11'
    RF01 = 'RF01'
    RR01 = 'RR01'
    RR02 = 'RR02'
    RR03 = 'RR03'
    RR04 = 'RR04'
    RR05 = 'RR05'
    RR06 = 'RR06'
    RR07 = 'RR07'
    RR08 = 'RR08'
    RR09 = 'RR09'
    RR11 = 'RR11'
    RR12 = 'RR12'
    RUTA = 'RUTA'
    SL01 = 'SL01'
    SL02 = 'SL02'
    SL11 = 'SL11'
    SL12 = 'SL12'
    SL13 = 'SL13'
    SL14 = 'SL14'
    SP01 = 'SP01'
    SP02 = 'SP02'
    SVNR = 'SVNR'
    TM01 = 'TM01'
    TRAC = 'TRAC'
    UPAY = 'UPAY'

    @property
    def code(self) -> str:
        return str(self.value)

    @property
    def info(self) -> Iso20022CodeInfo:
        from ._generated import resolve_code

        return cast(Iso20022CodeInfo, resolve_code('ExternalReturnReason1Code', self.value))

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
