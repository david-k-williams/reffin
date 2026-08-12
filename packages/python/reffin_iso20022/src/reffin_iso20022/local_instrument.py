"""Generated LocalInstrumentCode. Do not edit by hand."""
# Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
from __future__ import annotations

from enum import Enum
from typing import Self, cast

from ._model import Iso20022CodeInfo


class LocalInstrumentCode(str, Enum):
    CODE_04 = '04'
    CODE_05 = '05'
    CODE_08 = '08'
    CODE_19 = '19'
    CODE_58 = '58'
    CODE_60 = '60'
    CODE_82 = '82'
    CODE_83 = '83'
    CODE_85 = '85'
    CODE_89 = '89'
    ACCEPT = 'ACCEPT'
    ADD = 'ADD'
    ARC = 'ARC'
    ASTI = 'ASTI'
    B2B = 'B2B'
    B2BAMIPM = 'B2BAMIPM'
    BACP = 'BACP'
    BPA = 'BPA'
    BSE = 'BSE'
    CARD = 'CARD'
    CCD = 'CCD'
    CCI = 'CCI'
    CHN = 'CHN'
    CIE = 'CIE'
    CLSCCPERX = 'CLSCCPERX'
    CLSCCPLCH = 'CLSCCPLCH'
    COR1 = 'COR1'
    CORAMIPM = 'CORAMIPM'
    CORE = 'CORE'
    CPP = 'CPP'
    CR1AMIPM = 'CR1AMIPM'
    CTP = 'CTP'
    CTX = 'CTX'
    DDFA = 'DDFA'
    DDMC = 'DDMC'
    DDMP = 'DDMP'
    DDMU = 'DDMU'
    DDNR = 'DDNR'
    DDT = 'DDT'
    FADAMIPM = 'FADAMIPM'
    FDP = 'FDP'
    GST = 'GST'
    IAT = 'IAT'
    ICMC = 'ICMC'
    IDEAL = 'IDEAL'
    IMD = 'IMD'
    IN_CODE = 'IN'
    INST = 'INST'
    INSTIDEAL = 'INSTIDEAL'
    INSTNT01 = 'INSTNT01'
    INSTNT01IDEAL = 'INSTNT01IDEAL'
    INSTTC01 = 'INSTTC01'
    INSTTC01IDEAL = 'INSTTC01IDEAL'
    IPA = 'IPA'
    ISE = 'ISE'
    ITP = 'ITP'
    MANP = 'MANP'
    MDP = 'MDP'
    NLDO = 'NLDO'
    NLGOV = 'NLGOV'
    NLUP = 'NLUP'
    ONCL = 'ONCL'
    PERI = 'PERI'
    POP = 'POP'
    POS = 'POS'
    PPD = 'PPD'
    RCK = 'RCK'
    RDD = 'RDD'
    RIBA = 'RIBA'
    RIDO = 'RIDO'
    RIDV = 'RIDV'
    RTR = 'RTR'
    SBTI = 'SBTI'
    SCN = 'SCN'
    SDCL = 'SDCL'
    SDD = 'SDD'
    SDN = 'SDN'
    SGT = 'SGT'
    SOP = 'SOP'
    SRD = 'SRD'
    SRT = 'SRT'
    STR = 'STR'
    TEL = 'TEL'
    TRF = 'TRF'
    UDD = 'UDD'
    WEB = 'WEB'

    @property
    def code(self) -> str:
        return str(self.value)

    @property
    def info(self) -> Iso20022CodeInfo:
        from ._generated import resolve_code

        return cast(Iso20022CodeInfo, resolve_code('ExternalLocalInstrument1Code', self.value))

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
