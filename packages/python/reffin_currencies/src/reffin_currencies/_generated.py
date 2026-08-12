"""Generated offline currency reference data. Do not edit by hand."""
# Input SHA-256: 7332e4ab9b1caa548d3637aec8e31eeb36f374fd662e3c6eff56bf041c8ee416
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final

DATA_FINGERPRINT: Final[str] = '7332e4ab9b1caa548d3637aec8e31eeb36f374fd662e3c6eff56bf041c8ee416'
CLDR_VERSION: Final[str] = '48.2'


@dataclass(frozen=True, slots=True)
class CurrencyInfo:
    code: str
    name: str
    symbol: str | None
    narrow_symbol: str | None
    minor_digits: int
    minor_rounding: int
    cash_digits: int
    cash_rounding: int
    active: bool
    territories: tuple[str, ...]

    @property
    def display_symbol(self) -> str:
        return self.narrow_symbol or self.symbol or self.code


class Currency(str, Enum):
    ADP = 'ADP'
    AED = 'AED'
    AFA = 'AFA'
    AFN = 'AFN'
    ALK = 'ALK'
    ALL = 'ALL'
    AMD = 'AMD'
    ANG = 'ANG'
    AOA = 'AOA'
    AOK = 'AOK'
    AON = 'AON'
    AOR = 'AOR'
    ARA = 'ARA'
    ARL = 'ARL'
    ARM = 'ARM'
    ARP = 'ARP'
    ARS = 'ARS'
    ATS = 'ATS'
    AUD = 'AUD'
    AWG = 'AWG'
    AZM = 'AZM'
    AZN = 'AZN'
    BAD = 'BAD'
    BAM = 'BAM'
    BAN = 'BAN'
    BBD = 'BBD'
    BDT = 'BDT'
    BEC = 'BEC'
    BEF = 'BEF'
    BEL = 'BEL'
    BGL = 'BGL'
    BGM = 'BGM'
    BGN = 'BGN'
    BGO = 'BGO'
    BHD = 'BHD'
    BIF = 'BIF'
    BMD = 'BMD'
    BND = 'BND'
    BOB = 'BOB'
    BOL = 'BOL'
    BOP = 'BOP'
    BOV = 'BOV'
    BRB = 'BRB'
    BRC = 'BRC'
    BRE = 'BRE'
    BRL = 'BRL'
    BRN = 'BRN'
    BRR = 'BRR'
    BRZ = 'BRZ'
    BSD = 'BSD'
    BTN = 'BTN'
    BUK = 'BUK'
    BWP = 'BWP'
    BYB = 'BYB'
    BYN = 'BYN'
    BYR = 'BYR'
    BZD = 'BZD'
    CAD = 'CAD'
    CDF = 'CDF'
    CHE = 'CHE'
    CHF = 'CHF'
    CHW = 'CHW'
    CLE = 'CLE'
    CLF = 'CLF'
    CLP = 'CLP'
    CNH = 'CNH'
    CNX = 'CNX'
    CNY = 'CNY'
    COP = 'COP'
    COU = 'COU'
    CRC = 'CRC'
    CSD = 'CSD'
    CSK = 'CSK'
    CUC = 'CUC'
    CUP = 'CUP'
    CVE = 'CVE'
    CYP = 'CYP'
    CZK = 'CZK'
    DDM = 'DDM'
    DEM = 'DEM'
    DJF = 'DJF'
    DKK = 'DKK'
    DOP = 'DOP'
    DZD = 'DZD'
    ECS = 'ECS'
    ECV = 'ECV'
    EEK = 'EEK'
    EGP = 'EGP'
    ERN = 'ERN'
    ESA = 'ESA'
    ESB = 'ESB'
    ESP = 'ESP'
    ETB = 'ETB'
    EUR = 'EUR'
    FIM = 'FIM'
    FJD = 'FJD'
    FKP = 'FKP'
    FRF = 'FRF'
    GBP = 'GBP'
    GEK = 'GEK'
    GEL = 'GEL'
    GHC = 'GHC'
    GHS = 'GHS'
    GIP = 'GIP'
    GMD = 'GMD'
    GNF = 'GNF'
    GNS = 'GNS'
    GQE = 'GQE'
    GRD = 'GRD'
    GTQ = 'GTQ'
    GWE = 'GWE'
    GWP = 'GWP'
    GYD = 'GYD'
    HKD = 'HKD'
    HNL = 'HNL'
    HRD = 'HRD'
    HRK = 'HRK'
    HTG = 'HTG'
    HUF = 'HUF'
    IDR = 'IDR'
    IEP = 'IEP'
    ILP = 'ILP'
    ILR = 'ILR'
    ILS = 'ILS'
    INR = 'INR'
    IQD = 'IQD'
    IRR = 'IRR'
    ISJ = 'ISJ'
    ISK = 'ISK'
    ITL = 'ITL'
    JMD = 'JMD'
    JOD = 'JOD'
    JPY = 'JPY'
    KES = 'KES'
    KGS = 'KGS'
    KHR = 'KHR'
    KMF = 'KMF'
    KPW = 'KPW'
    KRH = 'KRH'
    KRO = 'KRO'
    KRW = 'KRW'
    KWD = 'KWD'
    KYD = 'KYD'
    KZT = 'KZT'
    LAK = 'LAK'
    LBP = 'LBP'
    LKR = 'LKR'
    LRD = 'LRD'
    LSL = 'LSL'
    LTL = 'LTL'
    LTT = 'LTT'
    LUC = 'LUC'
    LUF = 'LUF'
    LUL = 'LUL'
    LVL = 'LVL'
    LVR = 'LVR'
    LYD = 'LYD'
    MAD = 'MAD'
    MAF = 'MAF'
    MCF = 'MCF'
    MDC = 'MDC'
    MDL = 'MDL'
    MGA = 'MGA'
    MGF = 'MGF'
    MKD = 'MKD'
    MKN = 'MKN'
    MLF = 'MLF'
    MMK = 'MMK'
    MNT = 'MNT'
    MOP = 'MOP'
    MRO = 'MRO'
    MRU = 'MRU'
    MTL = 'MTL'
    MTP = 'MTP'
    MUR = 'MUR'
    MVP = 'MVP'
    MVR = 'MVR'
    MWK = 'MWK'
    MXN = 'MXN'
    MXP = 'MXP'
    MXV = 'MXV'
    MYR = 'MYR'
    MZE = 'MZE'
    MZM = 'MZM'
    MZN = 'MZN'
    NAD = 'NAD'
    NGN = 'NGN'
    NIC = 'NIC'
    NIO = 'NIO'
    NLG = 'NLG'
    NOK = 'NOK'
    NPR = 'NPR'
    NZD = 'NZD'
    OMR = 'OMR'
    PAB = 'PAB'
    PEI = 'PEI'
    PEN = 'PEN'
    PES = 'PES'
    PGK = 'PGK'
    PHP = 'PHP'
    PKR = 'PKR'
    PLN = 'PLN'
    PLZ = 'PLZ'
    PTE = 'PTE'
    PYG = 'PYG'
    QAR = 'QAR'
    RHD = 'RHD'
    ROL = 'ROL'
    RON = 'RON'
    RSD = 'RSD'
    RUB = 'RUB'
    RUR = 'RUR'
    RWF = 'RWF'
    SAR = 'SAR'
    SBD = 'SBD'
    SCR = 'SCR'
    SDD = 'SDD'
    SDG = 'SDG'
    SDP = 'SDP'
    SEK = 'SEK'
    SGD = 'SGD'
    SHP = 'SHP'
    SIT = 'SIT'
    SKK = 'SKK'
    SLE = 'SLE'
    SLL = 'SLL'
    SOS = 'SOS'
    SRD = 'SRD'
    SRG = 'SRG'
    SSP = 'SSP'
    STD = 'STD'
    STN = 'STN'
    SUR = 'SUR'
    SVC = 'SVC'
    SYP = 'SYP'
    SZL = 'SZL'
    THB = 'THB'
    TJR = 'TJR'
    TJS = 'TJS'
    TMM = 'TMM'
    TMT = 'TMT'
    TND = 'TND'
    TOP = 'TOP'
    TPE = 'TPE'
    TRL = 'TRL'
    TRY = 'TRY'
    TTD = 'TTD'
    TWD = 'TWD'
    TZS = 'TZS'
    UAH = 'UAH'
    UAK = 'UAK'
    UGS = 'UGS'
    UGX = 'UGX'
    USD = 'USD'
    USN = 'USN'
    USS = 'USS'
    UYI = 'UYI'
    UYP = 'UYP'
    UYU = 'UYU'
    UYW = 'UYW'
    UZS = 'UZS'
    VEB = 'VEB'
    VED = 'VED'
    VEF = 'VEF'
    VES = 'VES'
    VND = 'VND'
    VNN = 'VNN'
    VUV = 'VUV'
    WST = 'WST'
    XAF = 'XAF'
    XAG = 'XAG'
    XAU = 'XAU'
    XBA = 'XBA'
    XBB = 'XBB'
    XBC = 'XBC'
    XBD = 'XBD'
    XCD = 'XCD'
    XCG = 'XCG'
    XDR = 'XDR'
    XEU = 'XEU'
    XFO = 'XFO'
    XFU = 'XFU'
    XOF = 'XOF'
    XPD = 'XPD'
    XPF = 'XPF'
    XPT = 'XPT'
    XRE = 'XRE'
    XSU = 'XSU'
    XTS = 'XTS'
    XUA = 'XUA'
    XXX = 'XXX'
    YDD = 'YDD'
    YER = 'YER'
    YUD = 'YUD'
    YUM = 'YUM'
    YUN = 'YUN'
    YUR = 'YUR'
    ZAL = 'ZAL'
    ZAR = 'ZAR'
    ZMK = 'ZMK'
    ZMW = 'ZMW'
    ZRN = 'ZRN'
    ZRZ = 'ZRZ'
    ZWD = 'ZWD'
    ZWG = 'ZWG'
    ZWL = 'ZWL'
    ZWR = 'ZWR'

    @classmethod
    def try_parse(cls, code: str) -> Currency | None:
        return _CURRENCY_BY_CODE.get(code.upper()) if isinstance(code, str) else None

    @property
    def info(self) -> CurrencyInfo:
        return _INFO_BY_CURRENCY[self]

    @property
    def display_symbol(self) -> str:
        return self.info.display_symbol


_INFO_BY_CURRENCY: Final[dict[Currency, CurrencyInfo]] = {
    Currency.ADP: CurrencyInfo('ADP', 'Andorran Peseta', None, None, 0, 0, 0, 0, False, ('AD',)),
    Currency.AED: CurrencyInfo('AED', 'United Arab Emirates Dirham', 'AED', None, 2, 0, 2, 0, True, ('AE',)),
    Currency.AFA: CurrencyInfo('AFA', 'Afghan Afghani (1927–2002)', None, None, 2, 0, 2, 0, False, ('AF',)),
    Currency.AFN: CurrencyInfo('AFN', 'Afghan Afghani', 'AFN', '؋', 0, 0, 0, 0, True, ('AF',)),
    Currency.ALK: CurrencyInfo('ALK', 'Albanian Lek (1946–1965)', None, None, 2, 0, 2, 0, False, ('AL',)),
    Currency.ALL: CurrencyInfo('ALL', 'Albanian Lek', 'ALL', None, 0, 0, 0, 0, True, ('AL',)),
    Currency.AMD: CurrencyInfo('AMD', 'Armenian Dram', 'AMD', '֏', 2, 0, 0, 0, True, ('AM',)),
    Currency.ANG: CurrencyInfo('ANG', 'Netherlands Antillean Guilder', 'ANG', None, 2, 0, 2, 0, False, ('AW', 'BQ', 'CW', 'SX')),
    Currency.AOA: CurrencyInfo('AOA', 'Angolan Kwanza', 'AOA', 'Kz', 2, 0, 2, 0, True, ('AO',)),
    Currency.AOK: CurrencyInfo('AOK', 'Angolan Kwanza (1977–1991)', None, None, 2, 0, 2, 0, False, ('AO',)),
    Currency.AON: CurrencyInfo('AON', 'Angolan New Kwanza (1990–2000)', None, None, 2, 0, 2, 0, False, ('AO',)),
    Currency.AOR: CurrencyInfo('AOR', 'Angolan Readjusted Kwanza (1995–1999)', None, None, 2, 0, 2, 0, False, ('AO',)),
    Currency.ARA: CurrencyInfo('ARA', 'Argentine Austral', None, None, 2, 0, 2, 0, False, ('AR',)),
    Currency.ARL: CurrencyInfo('ARL', 'Argentine Peso Ley (1970–1983)', None, None, 2, 0, 2, 0, False, ('AR',)),
    Currency.ARM: CurrencyInfo('ARM', 'Argentine Peso (1881–1970)', None, None, 2, 0, 2, 0, False, ('AR',)),
    Currency.ARP: CurrencyInfo('ARP', 'Argentine Peso (1983–1985)', None, None, 2, 0, 2, 0, False, ('AR',)),
    Currency.ARS: CurrencyInfo('ARS', 'Argentine Peso', 'ARS', '$', 2, 0, 2, 0, True, ('AR',)),
    Currency.ATS: CurrencyInfo('ATS', 'Austrian Schilling', None, None, 2, 0, 2, 0, False, ('AT',)),
    Currency.AUD: CurrencyInfo('AUD', 'Australian Dollar', 'A$', '$', 2, 0, 2, 0, True, ('AU', 'CC', 'CX', 'HM', 'KI', 'NF', 'NR', 'PG', 'SB', 'TV')),
    Currency.AWG: CurrencyInfo('AWG', 'Aruban Florin', 'AWG', None, 2, 0, 2, 0, True, ('AW',)),
    Currency.AZM: CurrencyInfo('AZM', 'Azerbaijani Manat (1993–2006)', None, None, 2, 0, 2, 0, False, ('AZ',)),
    Currency.AZN: CurrencyInfo('AZN', 'Azerbaijani Manat', 'AZN', '₼', 2, 0, 2, 0, True, ('AZ',)),
    Currency.BAD: CurrencyInfo('BAD', 'Bosnia-Herzegovina Dinar (1992–1994)', None, None, 2, 0, 2, 0, False, ('BA',)),
    Currency.BAM: CurrencyInfo('BAM', 'Bosnia-Herzegovina Convertible Mark', 'BAM', 'KM', 2, 0, 2, 0, True, ('BA',)),
    Currency.BAN: CurrencyInfo('BAN', 'Bosnia-Herzegovina New Dinar (1994–1997)', None, None, 2, 0, 2, 0, False, ('BA',)),
    Currency.BBD: CurrencyInfo('BBD', 'Barbadian Dollar', 'BBD', '$', 2, 0, 2, 0, True, ('BB',)),
    Currency.BDT: CurrencyInfo('BDT', 'Bangladeshi Taka', 'BDT', '৳', 2, 0, 2, 0, True, ('BD',)),
    Currency.BEC: CurrencyInfo('BEC', 'Belgian Franc (convertible)', None, None, 2, 0, 2, 0, False, ('BE',)),
    Currency.BEF: CurrencyInfo('BEF', 'Belgian Franc', None, None, 2, 0, 2, 0, False, ('BE',)),
    Currency.BEL: CurrencyInfo('BEL', 'Belgian Franc (financial)', None, None, 2, 0, 2, 0, False, ('BE',)),
    Currency.BGL: CurrencyInfo('BGL', 'Bulgarian Hard Lev', None, None, 2, 0, 2, 0, False, ('BG',)),
    Currency.BGM: CurrencyInfo('BGM', 'Bulgarian Socialist Lev', None, None, 2, 0, 2, 0, False, ('BG',)),
    Currency.BGN: CurrencyInfo('BGN', 'Bulgarian Lev', 'BGN', None, 2, 0, 2, 0, False, ('BG',)),
    Currency.BGO: CurrencyInfo('BGO', 'Bulgarian Lev (1879–1952)', None, None, 2, 0, 2, 0, False, ('BG',)),
    Currency.BHD: CurrencyInfo('BHD', 'Bahraini Dinar', 'BHD', None, 3, 0, 3, 0, True, ('BH',)),
    Currency.BIF: CurrencyInfo('BIF', 'Burundian Franc', 'BIF', None, 0, 0, 0, 0, True, ('BI',)),
    Currency.BMD: CurrencyInfo('BMD', 'Bermudan Dollar', 'BMD', '$', 2, 0, 2, 0, True, ('BM',)),
    Currency.BND: CurrencyInfo('BND', 'Brunei Dollar', 'BND', '$', 2, 0, 2, 0, True, ('BN',)),
    Currency.BOB: CurrencyInfo('BOB', 'Bolivian Boliviano', 'BOB', 'Bs', 2, 0, 2, 0, True, ('BO',)),
    Currency.BOL: CurrencyInfo('BOL', 'Bolivian Boliviano (1863–1963)', None, None, 2, 0, 2, 0, False, ('BO',)),
    Currency.BOP: CurrencyInfo('BOP', 'Bolivian Peso', None, None, 2, 0, 2, 0, False, ('BO',)),
    Currency.BOV: CurrencyInfo('BOV', 'Bolivian Mvdol', None, None, 2, 0, 2, 0, False, ('BO',)),
    Currency.BRB: CurrencyInfo('BRB', 'Brazilian New Cruzeiro (1967–1986)', None, None, 2, 0, 2, 0, False, ('BR',)),
    Currency.BRC: CurrencyInfo('BRC', 'Brazilian Cruzado (1986–1989)', None, None, 2, 0, 2, 0, False, ('BR',)),
    Currency.BRE: CurrencyInfo('BRE', 'Brazilian Cruzeiro (1990–1993)', None, None, 2, 0, 2, 0, False, ('BR',)),
    Currency.BRL: CurrencyInfo('BRL', 'Brazilian Real', 'R$', 'R$', 2, 0, 2, 0, True, ('BR',)),
    Currency.BRN: CurrencyInfo('BRN', 'Brazilian New Cruzado (1989–1990)', None, None, 2, 0, 2, 0, False, ('BR',)),
    Currency.BRR: CurrencyInfo('BRR', 'Brazilian Cruzeiro (1993–1994)', None, None, 2, 0, 2, 0, False, ('BR',)),
    Currency.BRZ: CurrencyInfo('BRZ', 'Brazilian Cruzeiro (1942–1967)', None, None, 2, 0, 2, 0, False, ('BR',)),
    Currency.BSD: CurrencyInfo('BSD', 'Bahamian Dollar', 'BSD', '$', 2, 0, 2, 0, True, ('BS',)),
    Currency.BTN: CurrencyInfo('BTN', 'Bhutanese Ngultrum', 'BTN', None, 2, 0, 2, 0, True, ('BT',)),
    Currency.BUK: CurrencyInfo('BUK', 'Burmese Kyat', None, None, 2, 0, 2, 0, False, ('BU', 'MM')),
    Currency.BWP: CurrencyInfo('BWP', 'Botswanan Pula', 'BWP', 'P', 2, 0, 2, 0, True, ('BW',)),
    Currency.BYB: CurrencyInfo('BYB', 'Belarusian Ruble (1994–1999)', None, None, 2, 0, 2, 0, False, ('BY',)),
    Currency.BYN: CurrencyInfo('BYN', 'Belarusian Ruble', 'BYN', None, 2, 0, 2, 0, True, ('BY',)),
    Currency.BYR: CurrencyInfo('BYR', 'Belarusian Ruble (2000–2016)', None, None, 0, 0, 0, 0, False, ('BY',)),
    Currency.BZD: CurrencyInfo('BZD', 'Belize Dollar', 'BZD', '$', 2, 0, 2, 0, True, ('BZ',)),
    Currency.CAD: CurrencyInfo('CAD', 'Canadian Dollar', 'CA$', '$', 2, 0, 2, 5, True, ('CA',)),
    Currency.CDF: CurrencyInfo('CDF', 'Congolese Franc', 'CDF', None, 2, 0, 2, 0, True, ('CD',)),
    Currency.CHE: CurrencyInfo('CHE', 'WIR Euro', None, None, 2, 0, 2, 0, False, ('CH',)),
    Currency.CHF: CurrencyInfo('CHF', 'Swiss Franc', 'CHF', None, 2, 0, 2, 5, True, ('CH', 'LI')),
    Currency.CHW: CurrencyInfo('CHW', 'WIR Franc', None, None, 2, 0, 2, 0, False, ('CH',)),
    Currency.CLE: CurrencyInfo('CLE', 'Chilean Escudo', None, None, 2, 0, 2, 0, False, ('CL',)),
    Currency.CLF: CurrencyInfo('CLF', 'Chilean Unit of Account (UF)', None, None, 4, 0, 4, 0, False, ('CL',)),
    Currency.CLP: CurrencyInfo('CLP', 'Chilean Peso', 'CLP', '$', 0, 0, 0, 0, True, ('CL',)),
    Currency.CNH: CurrencyInfo('CNH', 'Chinese Yuan (offshore)', 'CNH', None, 2, 0, 2, 0, False, ('CN',)),
    Currency.CNX: CurrencyInfo('CNX', 'Chinese People’s Bank Dollar', None, None, 2, 0, 2, 0, False, ('CN',)),
    Currency.CNY: CurrencyInfo('CNY', 'Chinese Yuan', 'CN¥', '¥', 2, 0, 2, 0, True, ('CN',)),
    Currency.COP: CurrencyInfo('COP', 'Colombian Peso', 'COP', '$', 0, 0, 0, 0, True, ('CO',)),
    Currency.COU: CurrencyInfo('COU', 'Colombian Real Value Unit', None, None, 2, 0, 2, 0, False, ('CO',)),
    Currency.CRC: CurrencyInfo('CRC', 'Costa Rican Colón', 'CRC', '₡', 2, 0, 0, 0, True, ('CR',)),
    Currency.CSD: CurrencyInfo('CSD', 'Serbian Dinar (2002–2006)', None, None, 2, 0, 2, 0, False, ('CS', 'RS')),
    Currency.CSK: CurrencyInfo('CSK', 'Czechoslovak Hard Koruna', None, None, 2, 0, 2, 0, False, ('CZ', 'SK')),
    Currency.CUC: CurrencyInfo('CUC', 'Cuban Convertible Peso', 'CUC', '$', 2, 0, 2, 0, False, ('CU',)),
    Currency.CUP: CurrencyInfo('CUP', 'Cuban Peso', 'CUP', '$', 2, 0, 2, 0, True, ('CU',)),
    Currency.CVE: CurrencyInfo('CVE', 'Cape Verdean Escudo', 'CVE', None, 2, 0, 2, 0, True, ('CV',)),
    Currency.CYP: CurrencyInfo('CYP', 'Cypriot Pound', None, None, 2, 0, 2, 0, False, ('CY',)),
    Currency.CZK: CurrencyInfo('CZK', 'Czech Koruna', 'CZK', 'Kč', 2, 0, 0, 0, True, ('CZ',)),
    Currency.DDM: CurrencyInfo('DDM', 'East German Mark', None, None, 2, 0, 2, 0, False, ('DD',)),
    Currency.DEM: CurrencyInfo('DEM', 'German Mark', None, None, 2, 0, 2, 0, False, ('DE', 'ME', 'XK')),
    Currency.DJF: CurrencyInfo('DJF', 'Djiboutian Franc', 'DJF', None, 0, 0, 0, 0, True, ('DJ',)),
    Currency.DKK: CurrencyInfo('DKK', 'Danish Krone', 'DKK', 'kr', 2, 0, 2, 50, True, ('DK', 'FO', 'GL', 'IS')),
    Currency.DOP: CurrencyInfo('DOP', 'Dominican Peso', 'DOP', '$', 2, 0, 2, 0, True, ('DO',)),
    Currency.DZD: CurrencyInfo('DZD', 'Algerian Dinar', 'DZD', None, 2, 0, 2, 0, True, ('DZ',)),
    Currency.ECS: CurrencyInfo('ECS', 'Ecuadorian Sucre', None, None, 2, 0, 2, 0, False, ('EC',)),
    Currency.ECV: CurrencyInfo('ECV', 'Ecuadorian Unit of Constant Value', None, None, 2, 0, 2, 0, False, ('EC',)),
    Currency.EEK: CurrencyInfo('EEK', 'Estonian Kroon', None, None, 2, 0, 2, 0, False, ('EE',)),
    Currency.EGP: CurrencyInfo('EGP', 'Egyptian Pound', 'EGP', 'E£', 2, 0, 2, 0, True, ('EG', 'IQ', 'SD')),
    Currency.ERN: CurrencyInfo('ERN', 'Eritrean Nakfa', 'ERN', None, 2, 0, 2, 0, True, ('ER',)),
    Currency.ESA: CurrencyInfo('ESA', 'Spanish Peseta (A account)', None, None, 2, 0, 2, 0, False, ('ES',)),
    Currency.ESB: CurrencyInfo('ESB', 'Spanish Peseta (convertible account)', None, None, 2, 0, 2, 0, False, ('ES',)),
    Currency.ESP: CurrencyInfo('ESP', 'Spanish Peseta', None, '₧', 0, 0, 0, 0, False, ('AD', 'ES', 'PR')),
    Currency.ETB: CurrencyInfo('ETB', 'Ethiopian Birr', 'ETB', None, 2, 0, 2, 0, True, ('ER', 'ET')),
    Currency.EUR: CurrencyInfo('EUR', 'Euro', '€', '€', 2, 0, 2, 0, True, ('AD', 'AT', 'AX', 'BE', 'BG', 'BL', 'CS', 'CY', 'DE', 'EA', 'EE', 'ES', 'EU', 'FI', 'FR', 'GF', 'GP', 'GR', 'HR', 'IC', 'IE', 'IT', 'LT', 'LU', 'LV', 'MC', 'ME', 'MF', 'MQ', 'MT', 'NL', 'PM', 'PT', 'RE', 'SI', 'SK', 'SM', 'TF', 'VA', 'XK', 'YT')),
    Currency.FIM: CurrencyInfo('FIM', 'Finnish Markka', None, None, 2, 0, 2, 0, False, ('FI',)),
    Currency.FJD: CurrencyInfo('FJD', 'Fijian Dollar', 'FJD', '$', 2, 0, 2, 0, True, ('FJ',)),
    Currency.FKP: CurrencyInfo('FKP', 'Falkland Islands Pound', 'FKP', '£', 2, 0, 2, 0, True, ('FK',)),
    Currency.FRF: CurrencyInfo('FRF', 'French Franc', None, None, 2, 0, 2, 0, False, ('AD', 'BL', 'FR', 'GF', 'GP', 'MC', 'MF', 'MQ', 'PM', 'RE', 'TF', 'YT')),
    Currency.GBP: CurrencyInfo('GBP', 'British Pound', '£', '£', 2, 0, 2, 0, True, ('GB', 'GG', 'GS', 'IE', 'IM', 'JE', 'SD', 'SL', 'TA', 'VG')),
    Currency.GEK: CurrencyInfo('GEK', 'Georgian Kupon Larit', None, None, 2, 0, 2, 0, False, ('GE',)),
    Currency.GEL: CurrencyInfo('GEL', 'Georgian Lari', 'GEL', '₾', 2, 0, 2, 0, True, ('GE',)),
    Currency.GHC: CurrencyInfo('GHC', 'Ghanaian Cedi (1979–2007)', None, None, 2, 0, 2, 0, False, ('GH',)),
    Currency.GHS: CurrencyInfo('GHS', 'Ghanaian Cedi', 'GHS', 'GH₵', 2, 0, 2, 0, True, ('GH',)),
    Currency.GIP: CurrencyInfo('GIP', 'Gibraltar Pound', 'GIP', '£', 2, 0, 2, 0, True, ('GI',)),
    Currency.GMD: CurrencyInfo('GMD', 'Gambian Dalasi', 'GMD', None, 2, 0, 2, 0, True, ('GM',)),
    Currency.GNF: CurrencyInfo('GNF', 'Guinean Franc', 'GNF', 'FG', 0, 0, 0, 0, True, ('GN',)),
    Currency.GNS: CurrencyInfo('GNS', 'Guinean Syli', None, None, 2, 0, 2, 0, False, ('GN',)),
    Currency.GQE: CurrencyInfo('GQE', 'Equatorial Guinean Ekwele', None, None, 2, 0, 2, 0, False, ('GQ',)),
    Currency.GRD: CurrencyInfo('GRD', 'Greek Drachma', None, None, 2, 0, 2, 0, False, ('GR',)),
    Currency.GTQ: CurrencyInfo('GTQ', 'Guatemalan Quetzal', 'GTQ', 'Q', 2, 0, 2, 0, True, ('GT',)),
    Currency.GWE: CurrencyInfo('GWE', 'Portuguese Guinea Escudo', None, None, 2, 0, 2, 0, False, ('GW',)),
    Currency.GWP: CurrencyInfo('GWP', 'Guinea-Bissau Peso', None, None, 2, 0, 2, 0, False, ('GW',)),
    Currency.GYD: CurrencyInfo('GYD', 'Guyanaese Dollar', 'GYD', '$', 2, 0, 0, 0, True, ('GY',)),
    Currency.HKD: CurrencyInfo('HKD', 'Hong Kong Dollar', 'HK$', '$', 2, 0, 2, 0, True, ('HK',)),
    Currency.HNL: CurrencyInfo('HNL', 'Honduran Lempira', 'HNL', 'L', 2, 0, 2, 0, True, ('HN',)),
    Currency.HRD: CurrencyInfo('HRD', 'Croatian Dinar', None, None, 2, 0, 2, 0, False, ('HR',)),
    Currency.HRK: CurrencyInfo('HRK', 'Croatian Kuna', 'HRK', 'kn', 2, 0, 2, 0, False, ('HR',)),
    Currency.HTG: CurrencyInfo('HTG', 'Haitian Gourde', 'HTG', None, 2, 0, 2, 0, True, ('HT',)),
    Currency.HUF: CurrencyInfo('HUF', 'Hungarian Forint', 'HUF', 'Ft', 0, 0, 0, 5, True, ('HU',)),
    Currency.IDR: CurrencyInfo('IDR', 'Indonesian Rupiah', 'IDR', 'Rp', 0, 0, 0, 0, True, ('ID', 'TL', 'TP')),
    Currency.IEP: CurrencyInfo('IEP', 'Irish Pound', None, None, 2, 0, 2, 0, False, ('IE',)),
    Currency.ILP: CurrencyInfo('ILP', 'Israeli Pound', None, None, 2, 0, 2, 0, False, ('IL', 'PS')),
    Currency.ILR: CurrencyInfo('ILR', 'Israeli Shekel (1980–1985)', None, None, 2, 0, 2, 0, False, ('IL',)),
    Currency.ILS: CurrencyInfo('ILS', 'Israeli New Shekel', '₪', '₪', 2, 0, 2, 0, True, ('IL', 'PS')),
    Currency.INR: CurrencyInfo('INR', 'Indian Rupee', '₹', '₹', 2, 0, 2, 0, True, ('BD', 'BT', 'IN', 'IQ', 'NP', 'PK')),
    Currency.IQD: CurrencyInfo('IQD', 'Iraqi Dinar', 'IQD', None, 0, 0, 0, 0, True, ('IQ',)),
    Currency.IRR: CurrencyInfo('IRR', 'Iranian Rial', 'IRR', None, 0, 0, 0, 0, True, ('IR',)),
    Currency.ISJ: CurrencyInfo('ISJ', 'Icelandic Króna (1918–1981)', None, None, 2, 0, 2, 0, False, ('IS',)),
    Currency.ISK: CurrencyInfo('ISK', 'Icelandic Króna', 'ISK', 'kr', 0, 0, 0, 0, True, ('IS',)),
    Currency.ITL: CurrencyInfo('ITL', 'Italian Lira', None, None, 0, 0, 0, 0, False, ('IT', 'SM', 'VA')),
    Currency.JMD: CurrencyInfo('JMD', 'Jamaican Dollar', 'JMD', '$', 2, 0, 2, 0, True, ('JM', 'KY')),
    Currency.JOD: CurrencyInfo('JOD', 'Jordanian Dinar', 'JOD', None, 3, 0, 3, 0, True, ('JO', 'PS')),
    Currency.JPY: CurrencyInfo('JPY', 'Japanese Yen', '¥', '¥', 0, 0, 0, 0, True, ('FM', 'JP')),
    Currency.KES: CurrencyInfo('KES', 'Kenyan Shilling', 'KES', None, 2, 0, 2, 0, True, ('KE',)),
    Currency.KGS: CurrencyInfo('KGS', 'Kyrgyz Som', 'KGS', '⃀', 2, 0, 2, 0, True, ('KG',)),
    Currency.KHR: CurrencyInfo('KHR', 'Cambodian Riel', 'KHR', '៛', 2, 0, 2, 0, True, ('KH',)),
    Currency.KMF: CurrencyInfo('KMF', 'Comorian Franc', 'KMF', 'CF', 0, 0, 0, 0, True, ('KM', 'YT')),
    Currency.KPW: CurrencyInfo('KPW', 'North Korean Won', 'KPW', '₩', 0, 0, 0, 0, True, ('KP',)),
    Currency.KRH: CurrencyInfo('KRH', 'South Korean Hwan (1953–1962)', None, None, 2, 0, 2, 0, False, ('KR',)),
    Currency.KRO: CurrencyInfo('KRO', 'South Korean Won (1945–1953)', None, None, 2, 0, 2, 0, False, ('KR',)),
    Currency.KRW: CurrencyInfo('KRW', 'South Korean Won', '₩', '₩', 0, 0, 0, 0, True, ('KR',)),
    Currency.KWD: CurrencyInfo('KWD', 'Kuwaiti Dinar', 'KWD', None, 3, 0, 3, 0, True, ('KW',)),
    Currency.KYD: CurrencyInfo('KYD', 'Cayman Islands Dollar', 'KYD', '$', 2, 0, 2, 0, True, ('KY',)),
    Currency.KZT: CurrencyInfo('KZT', 'Kazakhstani Tenge', 'KZT', '₸', 2, 0, 2, 0, True, ('KZ',)),
    Currency.LAK: CurrencyInfo('LAK', 'Laotian Kip', 'LAK', '₭', 0, 0, 0, 0, True, ('LA',)),
    Currency.LBP: CurrencyInfo('LBP', 'Lebanese Pound', 'LBP', 'L£', 0, 0, 0, 0, True, ('LB',)),
    Currency.LKR: CurrencyInfo('LKR', 'Sri Lankan Rupee', 'LKR', 'Rs', 2, 0, 2, 0, True, ('LK',)),
    Currency.LRD: CurrencyInfo('LRD', 'Liberian Dollar', 'LRD', '$', 2, 0, 2, 0, True, ('LR',)),
    Currency.LSL: CurrencyInfo('LSL', 'Lesotho Loti', 'LSL', None, 2, 0, 2, 0, True, ('LS',)),
    Currency.LTL: CurrencyInfo('LTL', 'Lithuanian Litas', None, 'Lt', 2, 0, 2, 0, False, ('LT',)),
    Currency.LTT: CurrencyInfo('LTT', 'Lithuanian Talonas', None, None, 2, 0, 2, 0, False, ('LT',)),
    Currency.LUC: CurrencyInfo('LUC', 'Luxembourgian Convertible Franc', None, None, 2, 0, 2, 0, False, ('LU',)),
    Currency.LUF: CurrencyInfo('LUF', 'Luxembourgian Franc', None, None, 0, 0, 0, 0, False, ('LU',)),
    Currency.LUL: CurrencyInfo('LUL', 'Luxembourg Financial Franc', None, None, 2, 0, 2, 0, False, ('LU',)),
    Currency.LVL: CurrencyInfo('LVL', 'Latvian Lats', None, 'Ls', 2, 0, 2, 0, False, ('LV',)),
    Currency.LVR: CurrencyInfo('LVR', 'Latvian Ruble', None, None, 2, 0, 2, 0, False, ('LV',)),
    Currency.LYD: CurrencyInfo('LYD', 'Libyan Dinar', 'LYD', None, 3, 0, 3, 0, True, ('LY',)),
    Currency.MAD: CurrencyInfo('MAD', 'Moroccan Dirham', 'MAD', None, 2, 0, 2, 0, True, ('EH', 'MA')),
    Currency.MAF: CurrencyInfo('MAF', 'Moroccan Franc', None, None, 2, 0, 2, 0, False, ('MA',)),
    Currency.MCF: CurrencyInfo('MCF', 'Monegasque Franc', None, None, 2, 0, 2, 0, False, ('MC',)),
    Currency.MDC: CurrencyInfo('MDC', 'Moldovan Cupon', None, None, 2, 0, 2, 0, False, ('MD',)),
    Currency.MDL: CurrencyInfo('MDL', 'Moldovan Leu', 'MDL', None, 2, 0, 2, 0, True, ('MD',)),
    Currency.MGA: CurrencyInfo('MGA', 'Malagasy Ariary', 'MGA', 'Ar', 0, 0, 0, 0, True, ('MG',)),
    Currency.MGF: CurrencyInfo('MGF', 'Malagasy Franc', None, None, 0, 0, 0, 0, False, ('MG',)),
    Currency.MKD: CurrencyInfo('MKD', 'Macedonian Denar', 'MKD', None, 2, 0, 2, 0, True, ('MK',)),
    Currency.MKN: CurrencyInfo('MKN', 'Macedonian Denar (1992–1993)', None, None, 2, 0, 2, 0, False, ('MK',)),
    Currency.MLF: CurrencyInfo('MLF', 'Malian Franc', None, None, 2, 0, 2, 0, False, ('ML',)),
    Currency.MMK: CurrencyInfo('MMK', 'Myanmar Kyat', 'MMK', 'K', 0, 0, 0, 0, True, ('MM',)),
    Currency.MNT: CurrencyInfo('MNT', 'Mongolian Tugrik', 'MNT', '₮', 2, 0, 0, 0, True, ('MN',)),
    Currency.MOP: CurrencyInfo('MOP', 'Macanese Pataca', 'MOP', None, 2, 0, 2, 0, True, ('MO',)),
    Currency.MRO: CurrencyInfo('MRO', 'Mauritanian Ouguiya (1973–2017)', None, None, 0, 0, 0, 0, False, ('MR',)),
    Currency.MRU: CurrencyInfo('MRU', 'Mauritanian Ouguiya', 'MRU', None, 2, 0, 2, 0, True, ('MR',)),
    Currency.MTL: CurrencyInfo('MTL', 'Maltese Lira', None, None, 2, 0, 2, 0, False, ('MT',)),
    Currency.MTP: CurrencyInfo('MTP', 'Maltese Pound', None, None, 2, 0, 2, 0, False, ('MT',)),
    Currency.MUR: CurrencyInfo('MUR', 'Mauritian Rupee', 'MUR', 'Rs', 2, 0, 0, 0, True, ('MU',)),
    Currency.MVP: CurrencyInfo('MVP', 'Maldivian Rupee (1947–1981)', None, None, 2, 0, 2, 0, False, ('MV',)),
    Currency.MVR: CurrencyInfo('MVR', 'Maldivian Rufiyaa', 'MVR', None, 2, 0, 2, 0, True, ('MV',)),
    Currency.MWK: CurrencyInfo('MWK', 'Malawian Kwacha', 'MWK', None, 2, 0, 2, 0, True, ('MW',)),
    Currency.MXN: CurrencyInfo('MXN', 'Mexican Peso', 'MX$', '$', 2, 0, 2, 0, True, ('MX',)),
    Currency.MXP: CurrencyInfo('MXP', 'Mexican Silver Peso (1861–1992)', None, None, 2, 0, 2, 0, False, ('MX',)),
    Currency.MXV: CurrencyInfo('MXV', 'Mexican Investment Unit', None, None, 2, 0, 2, 0, False, ('MX',)),
    Currency.MYR: CurrencyInfo('MYR', 'Malaysian Ringgit', 'MYR', 'RM', 2, 0, 2, 0, True, ('BN', 'MY', 'SG')),
    Currency.MZE: CurrencyInfo('MZE', 'Mozambican Escudo', None, None, 2, 0, 2, 0, False, ('MZ',)),
    Currency.MZM: CurrencyInfo('MZM', 'Mozambican Metical (1980–2006)', None, None, 2, 0, 2, 0, False, ('MZ',)),
    Currency.MZN: CurrencyInfo('MZN', 'Mozambican Metical', 'MZN', None, 2, 0, 2, 0, True, ('MZ',)),
    Currency.NAD: CurrencyInfo('NAD', 'Namibian Dollar', 'NAD', '$', 2, 0, 2, 0, True, ('NA',)),
    Currency.NGN: CurrencyInfo('NGN', 'Nigerian Naira', 'NGN', '₦', 2, 0, 2, 0, True, ('NG',)),
    Currency.NIC: CurrencyInfo('NIC', 'Nicaraguan Córdoba (1988–1991)', None, None, 2, 0, 2, 0, False, ('NI',)),
    Currency.NIO: CurrencyInfo('NIO', 'Nicaraguan Córdoba', 'NIO', 'C$', 2, 0, 2, 0, True, ('NI',)),
    Currency.NLG: CurrencyInfo('NLG', 'Dutch Guilder', None, None, 2, 0, 2, 0, False, ('BE', 'NL', 'SR')),
    Currency.NOK: CurrencyInfo('NOK', 'Norwegian Krone', 'NOK', 'kr', 2, 0, 0, 0, True, ('BV', 'NO', 'SJ')),
    Currency.NPR: CurrencyInfo('NPR', 'Nepalese Rupee', 'NPR', 'Rs', 2, 0, 2, 0, True, ('NP',)),
    Currency.NZD: CurrencyInfo('NZD', 'New Zealand Dollar', 'NZ$', '$', 2, 0, 2, 0, True, ('CK', 'NU', 'NZ', 'PN', 'TK')),
    Currency.OMR: CurrencyInfo('OMR', 'Omani Rial', 'OMR', None, 3, 0, 3, 0, True, ('OM',)),
    Currency.PAB: CurrencyInfo('PAB', 'Panamanian Balboa', 'PAB', None, 2, 0, 2, 0, True, ('PA',)),
    Currency.PEI: CurrencyInfo('PEI', 'Peruvian Inti', None, None, 2, 0, 2, 0, False, ('PE',)),
    Currency.PEN: CurrencyInfo('PEN', 'Peruvian Sol', 'PEN', None, 2, 0, 2, 0, True, ('PE',)),
    Currency.PES: CurrencyInfo('PES', 'Peruvian Sol (1863–1965)', None, None, 2, 0, 2, 0, False, ('PE',)),
    Currency.PGK: CurrencyInfo('PGK', 'Papua New Guinean Kina', 'PGK', None, 2, 0, 2, 0, True, ('PG',)),
    Currency.PHP: CurrencyInfo('PHP', 'Philippine Peso', '₱', '₱', 2, 0, 2, 0, True, ('PH',)),
    Currency.PKR: CurrencyInfo('PKR', 'Pakistani Rupee', 'PKR', 'Rs', 0, 0, 0, 0, True, ('BD', 'PK')),
    Currency.PLN: CurrencyInfo('PLN', 'Polish Zloty', 'PLN', 'zł', 2, 0, 2, 0, True, ('PL',)),
    Currency.PLZ: CurrencyInfo('PLZ', 'Polish Zloty (1950–1995)', None, None, 2, 0, 2, 0, False, ('PL',)),
    Currency.PTE: CurrencyInfo('PTE', 'Portuguese Escudo', None, None, 2, 0, 2, 0, False, ('CV', 'PT')),
    Currency.PYG: CurrencyInfo('PYG', 'Paraguayan Guarani', 'PYG', '₲', 0, 0, 0, 0, True, ('PY',)),
    Currency.QAR: CurrencyInfo('QAR', 'Qatari Riyal', 'QAR', None, 2, 0, 2, 0, True, ('QA',)),
    Currency.RHD: CurrencyInfo('RHD', 'Rhodesian Dollar', None, None, 2, 0, 2, 0, False, ('ZW',)),
    Currency.ROL: CurrencyInfo('ROL', 'Romanian Leu (1952–2006)', None, None, 2, 0, 2, 0, False, ('RO',)),
    Currency.RON: CurrencyInfo('RON', 'Romanian Leu', 'RON', 'lei', 2, 0, 2, 0, True, ('RO',)),
    Currency.RSD: CurrencyInfo('RSD', 'Serbian Dinar', 'RSD', None, 2, 0, 0, 0, True, ('RS',)),
    Currency.RUB: CurrencyInfo('RUB', 'Russian Ruble', 'RUB', '₽', 2, 0, 2, 0, True, ('RU',)),
    Currency.RUR: CurrencyInfo('RUR', 'Russian Ruble (1991–1998)', None, None, 2, 0, 2, 0, False, ('AM', 'AZ', 'BY', 'GE', 'KG', 'RU', 'TJ', 'TM', 'UA')),
    Currency.RWF: CurrencyInfo('RWF', 'Rwandan Franc', 'RWF', 'RF', 0, 0, 0, 0, True, ('RW',)),
    Currency.SAR: CurrencyInfo('SAR', 'Saudi Riyal', 'SAR', None, 2, 0, 2, 0, True, ('SA',)),
    Currency.SBD: CurrencyInfo('SBD', 'Solomon Islands Dollar', 'SBD', '$', 2, 0, 2, 0, True, ('SB',)),
    Currency.SCR: CurrencyInfo('SCR', 'Seychellois Rupee', 'SCR', None, 2, 0, 2, 0, True, ('SC',)),
    Currency.SDD: CurrencyInfo('SDD', 'Sudanese Dinar (1992–2007)', None, None, 2, 0, 2, 0, False, ('SD',)),
    Currency.SDG: CurrencyInfo('SDG', 'Sudanese Pound', 'SDG', None, 2, 0, 2, 0, True, ('SD', 'SS')),
    Currency.SDP: CurrencyInfo('SDP', 'Sudanese Pound (1957–1998)', None, None, 2, 0, 2, 0, False, ('SD',)),
    Currency.SEK: CurrencyInfo('SEK', 'Swedish Krona', 'SEK', 'kr', 2, 0, 0, 0, True, ('NO', 'SE')),
    Currency.SGD: CurrencyInfo('SGD', 'Singapore Dollar', 'SGD', '$', 2, 0, 2, 0, True, ('SG',)),
    Currency.SHP: CurrencyInfo('SHP', 'St. Helena Pound', 'SHP', '£', 2, 0, 2, 0, True, ('AC', 'SH')),
    Currency.SIT: CurrencyInfo('SIT', 'Slovenian Tolar', None, None, 2, 0, 2, 0, False, ('SI',)),
    Currency.SKK: CurrencyInfo('SKK', 'Slovak Koruna', None, None, 2, 0, 2, 0, False, ('SK',)),
    Currency.SLE: CurrencyInfo('SLE', 'Sierra Leonean Leone', 'SLE', None, 2, 0, 2, 0, True, ('SL',)),
    Currency.SLL: CurrencyInfo('SLL', 'Sierra Leonean Leone (1964—2022)', 'SLL', None, 0, 0, 0, 0, False, ('SL',)),
    Currency.SOS: CurrencyInfo('SOS', 'Somali Shilling', 'SOS', None, 0, 0, 0, 0, True, ('SO',)),
    Currency.SRD: CurrencyInfo('SRD', 'Surinamese Dollar', 'SRD', '$', 2, 0, 2, 0, True, ('SR',)),
    Currency.SRG: CurrencyInfo('SRG', 'Surinamese Guilder', None, None, 2, 0, 2, 0, False, ('SR',)),
    Currency.SSP: CurrencyInfo('SSP', 'South Sudanese Pound', 'SSP', '£', 2, 0, 2, 0, True, ('SS',)),
    Currency.STD: CurrencyInfo('STD', 'São Tomé & Príncipe Dobra (1977–2017)', None, None, 0, 0, 0, 0, False, ('ST',)),
    Currency.STN: CurrencyInfo('STN', 'São Tomé & Príncipe Dobra', 'STN', 'Db', 2, 0, 2, 0, True, ('ST',)),
    Currency.SUR: CurrencyInfo('SUR', 'Soviet Rouble', None, None, 2, 0, 2, 0, False, ('AM', 'AZ', 'BY', 'EE', 'GE', 'KG', 'LT', 'LV', 'SU', 'TM', 'UA')),
    Currency.SVC: CurrencyInfo('SVC', 'Salvadoran Colón', None, None, 2, 0, 2, 0, False, ('SV',)),
    Currency.SYP: CurrencyInfo('SYP', 'Syrian Pound', 'SYP', '£', 0, 0, 0, 0, True, ('SY',)),
    Currency.SZL: CurrencyInfo('SZL', 'Swazi Lilangeni', 'SZL', None, 2, 0, 2, 0, True, ('SZ',)),
    Currency.THB: CurrencyInfo('THB', 'Thai Baht', 'THB', '฿', 2, 0, 2, 0, True, ('TH',)),
    Currency.TJR: CurrencyInfo('TJR', 'Tajikistani Ruble', None, None, 2, 0, 2, 0, False, ('TJ',)),
    Currency.TJS: CurrencyInfo('TJS', 'Tajikistani Somoni', 'TJS', None, 2, 0, 2, 0, True, ('TJ',)),
    Currency.TMM: CurrencyInfo('TMM', 'Turkmenistani Manat (1993–2009)', None, None, 0, 0, 0, 0, False, ('TM',)),
    Currency.TMT: CurrencyInfo('TMT', 'Turkmenistani Manat', 'TMT', None, 2, 0, 2, 0, True, ('TM',)),
    Currency.TND: CurrencyInfo('TND', 'Tunisian Dinar', 'TND', None, 3, 0, 3, 0, True, ('TN',)),
    Currency.TOP: CurrencyInfo('TOP', 'Tongan Paʻanga', 'TOP', 'T$', 2, 0, 2, 0, True, ('TO',)),
    Currency.TPE: CurrencyInfo('TPE', 'Timorese Escudo', None, None, 2, 0, 2, 0, False, ('TL', 'TP')),
    Currency.TRL: CurrencyInfo('TRL', 'Turkish Lira (1922–2005)', None, None, 0, 0, 0, 0, False, ('TR',)),
    Currency.TRY: CurrencyInfo('TRY', 'Turkish Lira', 'TRY', '₺', 2, 0, 2, 0, True, ('TR',)),
    Currency.TTD: CurrencyInfo('TTD', 'Trinidad & Tobago Dollar', 'TTD', '$', 2, 0, 2, 0, True, ('TT',)),
    Currency.TWD: CurrencyInfo('TWD', 'New Taiwan Dollar', 'NT$', '$', 2, 0, 0, 0, True, ('TW',)),
    Currency.TZS: CurrencyInfo('TZS', 'Tanzanian Shilling', 'TZS', None, 2, 0, 0, 0, True, ('TZ',)),
    Currency.UAH: CurrencyInfo('UAH', 'Ukrainian Hryvnia', 'UAH', '₴', 2, 0, 2, 0, True, ('UA',)),
    Currency.UAK: CurrencyInfo('UAK', 'Ukrainian Karbovanets', None, None, 2, 0, 2, 0, False, ('UA',)),
    Currency.UGS: CurrencyInfo('UGS', 'Ugandan Shilling (1966–1987)', None, None, 2, 0, 2, 0, False, ('UG',)),
    Currency.UGX: CurrencyInfo('UGX', 'Ugandan Shilling', 'UGX', None, 0, 0, 0, 0, True, ('UG',)),
    Currency.USD: CurrencyInfo('USD', 'US Dollar', '$', '$', 2, 0, 2, 0, True, ('AS', 'BQ', 'CU', 'DG', 'DO', 'EC', 'FM', 'GU', 'HT', 'IO', 'MH', 'MP', 'PA', 'PR', 'PW', 'SV', 'TC', 'TL', 'UM', 'US', 'VG', 'VI', 'ZW')),
    Currency.USN: CurrencyInfo('USN', 'US Dollar (Next day)', None, None, 2, 0, 2, 0, False, ('US',)),
    Currency.USS: CurrencyInfo('USS', 'US Dollar (Same day)', None, None, 2, 0, 2, 0, False, ('US',)),
    Currency.UYI: CurrencyInfo('UYI', 'Uruguayan Peso (Indexed Units)', None, None, 0, 0, 0, 0, False, ('UY',)),
    Currency.UYP: CurrencyInfo('UYP', 'Uruguayan Peso (1975–1993)', None, None, 2, 0, 2, 0, False, ('UY',)),
    Currency.UYU: CurrencyInfo('UYU', 'Uruguayan Peso', 'UYU', '$', 2, 0, 2, 0, True, ('UY',)),
    Currency.UYW: CurrencyInfo('UYW', 'Uruguayan Nominal Wage Index Unit', None, None, 4, 0, 4, 0, False, ('UY',)),
    Currency.UZS: CurrencyInfo('UZS', 'Uzbekistani Som', 'UZS', None, 2, 0, 0, 0, True, ('UZ',)),
    Currency.VEB: CurrencyInfo('VEB', 'Venezuelan Bolívar (1871–2008)', None, None, 2, 0, 2, 0, False, ('VE',)),
    Currency.VED: CurrencyInfo('VED', 'Bolívar Soberano', None, None, 2, 0, 2, 0, False, ('VE',)),
    Currency.VEF: CurrencyInfo('VEF', 'Venezuelan Bolívar (2008–2018)', None, 'Bs', 2, 0, 0, 0, False, ('VE',)),
    Currency.VES: CurrencyInfo('VES', 'Venezuelan Bolívar', 'VES', None, 2, 0, 2, 0, True, ('VE',)),
    Currency.VND: CurrencyInfo('VND', 'Vietnamese Dong', '₫', '₫', 0, 0, 0, 0, True, ('VN',)),
    Currency.VNN: CurrencyInfo('VNN', 'Vietnamese Dong (1978–1985)', None, None, 2, 0, 2, 0, False, ('VN',)),
    Currency.VUV: CurrencyInfo('VUV', 'Vanuatu Vatu', 'VUV', None, 0, 0, 0, 0, True, ('VU',)),
    Currency.WST: CurrencyInfo('WST', 'Samoan Tala', 'WST', None, 2, 0, 2, 0, True, ('WS',)),
    Currency.XAF: CurrencyInfo('XAF', 'Central African CFA Franc', 'FCFA', None, 0, 0, 0, 0, True, ('CF', 'CG', 'CM', 'GA', 'GQ', 'TD')),
    Currency.XAG: CurrencyInfo('XAG', 'Silver', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XAU: CurrencyInfo('XAU', 'Gold', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XBA: CurrencyInfo('XBA', 'European Composite Unit', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XBB: CurrencyInfo('XBB', 'European Monetary Unit', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XBC: CurrencyInfo('XBC', 'European Unit of Account (XBC)', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XBD: CurrencyInfo('XBD', 'European Unit of Account (XBD)', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XCD: CurrencyInfo('XCD', 'East Caribbean Dollar', 'EC$', '$', 2, 0, 2, 0, True, ('AG', 'AI', 'BB', 'DM', 'GD', 'KN', 'LC', 'MS', 'VC')),
    Currency.XCG: CurrencyInfo('XCG', 'Caribbean guilder', 'Cg.', None, 2, 0, 2, 0, True, ('CW', 'SX')),
    Currency.XDR: CurrencyInfo('XDR', 'Special Drawing Rights', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XEU: CurrencyInfo('XEU', 'European Currency Unit', None, None, 2, 0, 2, 0, False, ('EU',)),
    Currency.XFO: CurrencyInfo('XFO', 'French Gold Franc', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XFU: CurrencyInfo('XFU', 'French UIC-Franc', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XOF: CurrencyInfo('XOF', 'West African CFA Franc', 'F\u202fCFA', None, 0, 0, 0, 0, True, ('BF', 'BJ', 'CI', 'GW', 'ML', 'MR', 'NE', 'SN', 'TG')),
    Currency.XPD: CurrencyInfo('XPD', 'Palladium', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XPF: CurrencyInfo('XPF', 'CFP Franc', 'CFPF', None, 0, 0, 0, 0, True, ('NC', 'PF', 'WF')),
    Currency.XPT: CurrencyInfo('XPT', 'Platinum', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XRE: CurrencyInfo('XRE', 'RINET Funds', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XSU: CurrencyInfo('XSU', 'Sucre', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XTS: CurrencyInfo('XTS', 'Testing Currency Code', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XUA: CurrencyInfo('XUA', 'ADB Unit of Account', None, None, 2, 0, 2, 0, False, ('ZZ',)),
    Currency.XXX: CurrencyInfo('XXX', 'Unknown Currency', '¤', None, 2, 0, 2, 0, False, ('AQ', 'CP', 'ZZ')),
    Currency.YDD: CurrencyInfo('YDD', 'Yemeni Dinar', None, None, 2, 0, 2, 0, False, ('YD',)),
    Currency.YER: CurrencyInfo('YER', 'Yemeni Rial', 'YER', None, 0, 0, 0, 0, True, ('YE',)),
    Currency.YUD: CurrencyInfo('YUD', 'Yugoslavian Hard Dinar (1966–1990)', None, None, 2, 0, 2, 0, False, ('BA', 'HR', 'YU')),
    Currency.YUM: CurrencyInfo('YUM', 'Yugoslavian New Dinar (1994–2002)', None, None, 2, 0, 2, 0, False, ('CS', 'ME', 'RS', 'XK', 'YU')),
    Currency.YUN: CurrencyInfo('YUN', 'Yugoslavian Convertible Dinar (1990–1992)', None, None, 2, 0, 2, 0, False, ('BA', 'HR', 'YU')),
    Currency.YUR: CurrencyInfo('YUR', 'Yugoslavian Reformed Dinar (1992–1993)', None, None, 2, 0, 2, 0, False, ('BA',)),
    Currency.ZAL: CurrencyInfo('ZAL', 'South African Rand (financial)', None, None, 2, 0, 2, 0, False, ('ZA',)),
    Currency.ZAR: CurrencyInfo('ZAR', 'South African Rand', 'ZAR', 'R', 2, 0, 2, 0, True, ('BW', 'LS', 'NA', 'ZA')),
    Currency.ZMK: CurrencyInfo('ZMK', 'Zambian Kwacha (1968–2012)', None, None, 0, 0, 0, 0, False, ('ZM',)),
    Currency.ZMW: CurrencyInfo('ZMW', 'Zambian Kwacha', 'ZMW', 'ZK', 2, 0, 2, 0, True, ('ZM',)),
    Currency.ZRN: CurrencyInfo('ZRN', 'Zairean New Zaire (1993–1998)', None, None, 2, 0, 2, 0, False, ('CD', 'ZR')),
    Currency.ZRZ: CurrencyInfo('ZRZ', 'Zairean Zaire (1971–1993)', None, None, 2, 0, 2, 0, False, ('CD', 'ZR')),
    Currency.ZWD: CurrencyInfo('ZWD', 'Zimbabwean Dollar (1980–2008)', None, None, 0, 0, 0, 0, False, ('ZW',)),
    Currency.ZWG: CurrencyInfo('ZWG', 'Zimbabwean Gold', 'ZWG', None, 2, 0, 2, 0, True, ('ZW',)),
    Currency.ZWL: CurrencyInfo('ZWL', 'Zimbabwean Dollar (2009–2024)', None, None, 2, 0, 2, 0, False, ('ZW',)),
    Currency.ZWR: CurrencyInfo('ZWR', 'Zimbabwean Dollar (2008)', None, None, 2, 0, 2, 0, False, ('ZW',)),
}
_CURRENCY_BY_CODE: Final = {currency.value: currency for currency in Currency}
ALL_CURRENCIES: Final[tuple[CurrencyInfo, ...]] = tuple(item.info for item in Currency)


def resolve_currency(code: str | Currency) -> CurrencyInfo | None:
    currency = code if isinstance(code, Currency) else Currency.try_parse(code)
    return currency.info if currency is not None else None
