"""Generated ACH reference catalogs. Do not edit by hand."""

# Input SHA-256: 252f6495924ee9a8b82ec6088df0325739cb5e902bcf3e3bdc1f86429995de6e
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from types import MappingProxyType
from typing import Final, Mapping, Self, TypeVar

DATA_FINGERPRINT: Final = '252f6495924ee9a8b82ec6088df0325739cb5e902bcf3e3bdc1f86429995de6e'
REFERENCE_AS_OF: Final = date(2026, 8, 11)


class AchCodeStatus(str, Enum):
    CURRENT = 'current'
    PLANNED = 'planned'
    LEGACY = 'legacy'


@dataclass(frozen=True, slots=True)
class AchReferenceInfo:
    code: str
    name: str
    status: AchCodeStatus
    valid_from: date | None
    valid_to: date | None
    sources: tuple[str, ...]
    material_symbol: str

    def is_effective(self, on: date = REFERENCE_AS_OF) -> bool:
        if isinstance(on, datetime):
            on = on.date()
        if self.status is AchCodeStatus.LEGACY:
            return False
        if self.valid_from is not None and on < self.valid_from:
            return False
        return self.valid_to is None or on <= self.valid_to


@dataclass(frozen=True, slots=True)
class AchTransactionCodeInfo(AchReferenceInfo):
    account_type: str
    direction: str
    entry_kind: str
    return_for_codes: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class AchReturnCodeInfo(AchReferenceInfo):
    category: str


@dataclass(frozen=True, slots=True)
class AchStandardEntryClassCodeInfo(AchReferenceInfo):
    entry_kind: str
    consumer_or_corporate: str
    direction: str
    addenda_support: str


@dataclass(frozen=True, slots=True)
class AchServiceClassCodeInfo(AchReferenceInfo):
    direction: str


@dataclass(frozen=True, slots=True)
class AchRecordTypeCodeInfo(AchReferenceInfo):
    pass


@dataclass(frozen=True, slots=True)
class AchChangeCodeInfo(AchReferenceInfo):
    corrected_fields: tuple[str, ...]
    applies_to: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class AchAddendaTypeCodeInfo(AchReferenceInfo):
    applies_to: tuple[str, ...]


class _AchCode(str, Enum):
    @property
    def code(self) -> str:
        return str(self.value)

    @classmethod
    def try_parse(cls, value: object) -> Self | None:
        if isinstance(value, cls):
            return value
        if not isinstance(value, str):
            return None
        try:
            return cls(value.strip().upper())
        except ValueError:
            return None


class AchTransactionCode(_AchCode):
    CODE_21 = '21'
    CODE_22 = '22'
    CODE_23 = '23'
    CODE_24 = '24'
    CODE_26 = '26'
    CODE_27 = '27'
    CODE_28 = '28'
    CODE_29 = '29'
    CODE_31 = '31'
    CODE_32 = '32'
    CODE_33 = '33'
    CODE_34 = '34'
    CODE_36 = '36'
    CODE_37 = '37'
    CODE_38 = '38'
    CODE_39 = '39'
    CODE_41 = '41'
    CODE_42 = '42'
    CODE_43 = '43'
    CODE_44 = '44'
    CODE_46 = '46'
    CODE_47 = '47'
    CODE_48 = '48'
    CODE_49 = '49'
    CODE_51 = '51'
    CODE_52 = '52'
    CODE_53 = '53'
    CODE_54 = '54'
    CODE_55 = '55'
    CODE_56 = '56'
    CODE_81 = '81'
    CODE_82 = '82'
    CODE_83 = '83'
    CODE_84 = '84'
    CODE_85 = '85'
    CODE_86 = '86'
    CODE_87 = '87'
    CODE_88 = '88'

    @property
    def info(self) -> AchTransactionCodeInfo:
        return _DEFAULT_TRANSACTION_CODE_INFO[self.value]

    @property
    def label(self) -> str:
        return self.info.name

    @property
    def material_symbol(self) -> str:
        return self.info.material_symbol


class AchReturnCode(_AchCode):
    R01 = 'R01'
    R02 = 'R02'
    R03 = 'R03'
    R04 = 'R04'
    R05 = 'R05'
    R06 = 'R06'
    R07 = 'R07'
    R08 = 'R08'
    R09 = 'R09'
    R10 = 'R10'
    R11 = 'R11'
    R12 = 'R12'
    R13 = 'R13'
    R14 = 'R14'
    R15 = 'R15'
    R16 = 'R16'
    R17 = 'R17'
    R18 = 'R18'
    R19 = 'R19'
    R20 = 'R20'
    R21 = 'R21'
    R22 = 'R22'
    R23 = 'R23'
    R24 = 'R24'
    R25 = 'R25'
    R26 = 'R26'
    R27 = 'R27'
    R28 = 'R28'
    R29 = 'R29'
    R30 = 'R30'
    R31 = 'R31'
    R32 = 'R32'
    R33 = 'R33'
    R34 = 'R34'
    R35 = 'R35'
    R36 = 'R36'
    R37 = 'R37'
    R38 = 'R38'
    R39 = 'R39'
    R40 = 'R40'
    R41 = 'R41'
    R42 = 'R42'
    R43 = 'R43'
    R44 = 'R44'
    R45 = 'R45'
    R46 = 'R46'
    R47 = 'R47'
    R50 = 'R50'
    R51 = 'R51'
    R52 = 'R52'
    R53 = 'R53'
    R61 = 'R61'
    R62 = 'R62'
    R67 = 'R67'
    R68 = 'R68'
    R69 = 'R69'
    R70 = 'R70'
    R71 = 'R71'
    R72 = 'R72'
    R73 = 'R73'
    R74 = 'R74'
    R75 = 'R75'
    R76 = 'R76'
    R77 = 'R77'
    R80 = 'R80'
    R81 = 'R81'
    R82 = 'R82'
    R83 = 'R83'
    R84 = 'R84'
    R85 = 'R85'
    R90 = 'R90'

    @property
    def info(self) -> AchReturnCodeInfo:
        return _DEFAULT_RETURN_CODE_INFO[self.value]

    @property
    def label(self) -> str:
        return self.info.name

    @property
    def material_symbol(self) -> str:
        return self.info.material_symbol


class AchStandardEntryClassCode(_AchCode):
    ACK = 'ACK'
    ADV = 'ADV'
    ARC = 'ARC'
    ATX = 'ATX'
    BOC = 'BOC'
    CCD = 'CCD'
    CIE = 'CIE'
    COR = 'COR'
    CTX = 'CTX'
    DNE = 'DNE'
    ENR = 'ENR'
    IAT = 'IAT'
    MTE = 'MTE'
    POP = 'POP'
    POS = 'POS'
    PPD = 'PPD'
    RCK = 'RCK'
    SHR = 'SHR'
    TEL = 'TEL'
    TRC = 'TRC'
    TRX = 'TRX'
    WEB = 'WEB'
    XCK = 'XCK'

    @property
    def info(self) -> AchStandardEntryClassCodeInfo:
        return _DEFAULT_STANDARD_ENTRY_CLASS_CODE_INFO[self.value]

    @property
    def label(self) -> str:
        return self.info.name

    @property
    def material_symbol(self) -> str:
        return self.info.material_symbol


class AchServiceClassCode(_AchCode):
    CODE_200 = '200'
    CODE_220 = '220'
    CODE_225 = '225'
    CODE_280 = '280'

    @property
    def info(self) -> AchServiceClassCodeInfo:
        return _DEFAULT_SERVICE_CLASS_CODE_INFO[self.value]

    @property
    def label(self) -> str:
        return self.info.name

    @property
    def material_symbol(self) -> str:
        return self.info.material_symbol


class AchRecordTypeCode(_AchCode):
    CODE_1 = '1'
    CODE_5 = '5'
    CODE_6 = '6'
    CODE_7 = '7'
    CODE_8 = '8'
    CODE_9 = '9'

    @property
    def info(self) -> AchRecordTypeCodeInfo:
        return _DEFAULT_RECORD_TYPE_CODE_INFO[self.value]

    @property
    def label(self) -> str:
        return self.info.name

    @property
    def material_symbol(self) -> str:
        return self.info.material_symbol


class AchChangeCode(_AchCode):
    C01 = 'C01'
    C02 = 'C02'
    C03 = 'C03'
    C05 = 'C05'
    C06 = 'C06'
    C07 = 'C07'
    C08 = 'C08'
    C09 = 'C09'
    C13 = 'C13'
    C14 = 'C14'

    @property
    def info(self) -> AchChangeCodeInfo:
        return _DEFAULT_CHANGE_CODE_INFO[self.value]

    @property
    def label(self) -> str:
        return self.info.name

    @property
    def material_symbol(self) -> str:
        return self.info.material_symbol


class AchAddendaTypeCode(_AchCode):
    CODE_01 = '01'
    CODE_02 = '02'
    CODE_05 = '05'
    CODE_10 = '10'
    CODE_11 = '11'
    CODE_12 = '12'
    CODE_13 = '13'
    CODE_14 = '14'
    CODE_15 = '15'
    CODE_16 = '16'
    CODE_17 = '17'
    CODE_18 = '18'
    CODE_98 = '98'
    CODE_99 = '99'

    @property
    def info(self) -> AchAddendaTypeCodeInfo:
        return _DEFAULT_ADDENDA_TYPE_CODE_INFO[self.value]

    @property
    def label(self) -> str:
        return self.info.name

    @property
    def material_symbol(self) -> str:
        return self.info.material_symbol


TRANSACTION_CODE_RECORDS: Final[tuple[AchTransactionCodeInfo, ...]] = (
    AchTransactionCodeInfo('21', 'Return or NOC for Checking Credit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'checking', 'return_or_noc', 'return_or_noc', ('22', '23', '24')),
    AchTransactionCodeInfo('22', 'Checking Credit', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'payments', 'checking', 'credit', 'monetary', ()),
    AchTransactionCodeInfo('23', 'Checking Credit Prenote DNE or ENR', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'payments', 'checking', 'credit', 'prenotification_or_notice', ()),
    AchTransactionCodeInfo('24', 'Checking Zero-Dollar Credit or Acknowledgment', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'checking', 'credit', 'zero_dollar_or_acknowledgment', ()),
    AchTransactionCodeInfo('26', 'Return or NOC for Checking Debit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'checking', 'return_or_noc', 'return_or_noc', ('27', '28', '29')),
    AchTransactionCodeInfo('27', 'Checking Debit', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'payments', 'checking', 'debit', 'monetary', ()),
    AchTransactionCodeInfo('28', 'Checking Debit Prenotification', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'payments', 'checking', 'debit', 'prenotification', ()),
    AchTransactionCodeInfo('29', 'Checking Zero-Dollar Debit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'checking', 'debit', 'zero_dollar', ()),
    AchTransactionCodeInfo('31', 'Return or NOC for Savings Credit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'savings', 'return_or_noc', 'return_or_noc', ('32', '33', '34')),
    AchTransactionCodeInfo('32', 'Savings Credit', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'payments', 'savings', 'credit', 'monetary', ()),
    AchTransactionCodeInfo('33', 'Savings Credit Prenote DNE or ENR', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'payments', 'savings', 'credit', 'prenotification_or_notice', ()),
    AchTransactionCodeInfo('34', 'Savings Zero-Dollar Credit or Acknowledgment', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'savings', 'credit', 'zero_dollar_or_acknowledgment', ()),
    AchTransactionCodeInfo('36', 'Return or NOC for Savings Debit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'savings', 'return_or_noc', 'return_or_noc', ('37', '38', '39')),
    AchTransactionCodeInfo('37', 'Savings Debit', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'payments', 'savings', 'debit', 'monetary', ()),
    AchTransactionCodeInfo('38', 'Savings Debit Prenotification', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'payments', 'savings', 'debit', 'prenotification', ()),
    AchTransactionCodeInfo('39', 'Savings Zero-Dollar Debit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'savings', 'debit', 'zero_dollar', ()),
    AchTransactionCodeInfo('41', 'Return or NOC for General Ledger Credit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'general_ledger', 'return_or_noc', 'return_or_noc', ('42', '43', '44')),
    AchTransactionCodeInfo('42', 'General Ledger Credit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'general_ledger', 'credit', 'monetary', ()),
    AchTransactionCodeInfo('43', 'General Ledger Credit Prenotification', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'general_ledger', 'credit', 'prenotification', ()),
    AchTransactionCodeInfo('44', 'General Ledger Zero-Dollar Credit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'general_ledger', 'credit', 'zero_dollar', ()),
    AchTransactionCodeInfo('46', 'Return or NOC for General Ledger Debit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'general_ledger', 'return_or_noc', 'return_or_noc', ('47', '48', '49')),
    AchTransactionCodeInfo('47', 'General Ledger Debit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'general_ledger', 'debit', 'monetary', ()),
    AchTransactionCodeInfo('48', 'General Ledger Debit Prenotification', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'general_ledger', 'debit', 'prenotification', ()),
    AchTransactionCodeInfo('49', 'General Ledger Zero-Dollar Debit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'general_ledger', 'debit', 'zero_dollar', ()),
    AchTransactionCodeInfo('51', 'Return or NOC for Loan Credit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'loan', 'return_or_noc', 'return_or_noc', ('52', '53', '54')),
    AchTransactionCodeInfo('52', 'Loan Credit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'loan', 'credit', 'monetary', ()),
    AchTransactionCodeInfo('53', 'Loan Credit Prenotification', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'loan', 'credit', 'prenotification', ()),
    AchTransactionCodeInfo('54', 'Loan Zero-Dollar Credit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'loan', 'credit', 'zero_dollar', ()),
    AchTransactionCodeInfo('55', 'Loan Debit for Reversal', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'loan', 'debit', 'reversal', ()),
    AchTransactionCodeInfo('56', 'Return or NOC for Loan Debit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'loan', 'return_or_noc', 'return_or_noc', ('55',)),
    AchTransactionCodeInfo('81', 'ADV Credit for Originated Debits', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'accounting', 'credit', 'accounting', ()),
    AchTransactionCodeInfo('82', 'ADV Debit for Originated Credits', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'accounting', 'debit', 'accounting', ()),
    AchTransactionCodeInfo('83', 'ADV Credit for Received Credits', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'accounting', 'credit', 'accounting', ()),
    AchTransactionCodeInfo('84', 'ADV Debit for Received Debits', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'accounting', 'debit', 'accounting', ()),
    AchTransactionCodeInfo('85', 'ADV Credit for Credits in Rejected Batches', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'accounting', 'credit', 'accounting', ()),
    AchTransactionCodeInfo('86', 'ADV Debit for Debits in Rejected Batches', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'accounting', 'debit', 'accounting', ()),
    AchTransactionCodeInfo('87', 'ADV Summary Credit for Respondent Activity', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'accounting', 'credit', 'accounting', ()),
    AchTransactionCodeInfo('88', 'ADV Summary Debit for Respondent Activity', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'payments', 'accounting', 'debit', 'accounting', ()),
)


RETURN_CODE_RECORDS: Final[tuple[AchReturnCodeInfo, ...]] = (
    AchReturnCodeInfo('R01', 'Insufficient Funds', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'funds'),
    AchReturnCodeInfo('R02', 'Account Closed', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'account'),
    AchReturnCodeInfo('R03', 'No Account or Unable to Locate Account', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'account'),
    AchReturnCodeInfo('R04', 'Invalid Account Number Structure', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'account'),
    AchReturnCodeInfo('R05', 'Unauthorized Corporate-Code Debit to Consumer Account', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'authorization'),
    AchReturnCodeInfo('R06', 'Returned at ODFI Request', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'request'),
    AchReturnCodeInfo('R07', 'Authorization Revoked by Customer', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'authorization'),
    AchReturnCodeInfo('R08', 'Payment Stopped', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'authorization'),
    AchReturnCodeInfo('R09', 'Uncollected Funds', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'funds'),
    AchReturnCodeInfo('R10', 'Originator Unknown or Not Authorized to Debit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'authorization'),
    AchReturnCodeInfo('R11', 'Entry Not in Accordance with Authorization', AchCodeStatus.CURRENT, date(2020, 4, 1), None, ('nacha_basic_2025', 'nacha_iso20022_2023', 'nacha_r11_2020'), 'undo', 'authorization'),
    AchReturnCodeInfo('R12', 'Account Sold to Another DFI', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'account'),
    AchReturnCodeInfo('R13', 'Invalid ACH Routing Number', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'administrative'),
    AchReturnCodeInfo('R14', 'Representative Payee Deceased or Unable to Continue', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'death_or_legal'),
    AchReturnCodeInfo('R15', 'Beneficiary or Account Holder Deceased', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'death_or_legal'),
    AchReturnCodeInfo('R16', 'Account Frozen or Return per OFAC Instruction', AchCodeStatus.CURRENT, None, date(2028, 3, 16), ('nacha_basic_2025', 'nacha_iso20022_2023', 'nacha_rule_r90'), 'undo', 'legal_or_compliance'),
    AchReturnCodeInfo('R16', 'Account Frozen', AchCodeStatus.PLANNED, date(2028, 3, 17), None, ('nacha_rule_r90',), 'undo', 'legal_or_compliance'),
    AchReturnCodeInfo('R17', 'File Edit Error Questionable Entry or Improper Reversal', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_minor_topics_2026', 'nacha_questionable_2019', 'nacha_reversals_2021'), 'undo', 'administrative'),
    AchReturnCodeInfo('R18', 'Improper Effective Entry Date', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'administrative'),
    AchReturnCodeInfo('R19', 'Amount Field Error', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'format'),
    AchReturnCodeInfo('R20', 'Non-Transaction Account', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'account'),
    AchReturnCodeInfo('R21', 'Invalid Company Identification', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'administrative'),
    AchReturnCodeInfo('R22', 'Invalid Individual ID Number', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023', 'fedglobal_manual_2026'), 'undo', 'administrative'),
    AchReturnCodeInfo('R23', 'Credit Entry Refused by Receiver', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'receiver_refusal'),
    AchReturnCodeInfo('R24', 'Duplicate Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'administrative'),
    AchReturnCodeInfo('R25', 'Addenda Error', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'format'),
    AchReturnCodeInfo('R26', 'Mandatory Field Error', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'format'),
    AchReturnCodeInfo('R27', 'Trace Number Error', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'format'),
    AchReturnCodeInfo('R28', 'Routing Number Check Digit Error', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'format'),
    AchReturnCodeInfo('R29', 'Corporate Customer Advises Not Authorized', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'authorization'),
    AchReturnCodeInfo('R30', 'RDFI Not in Check Truncation Program', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'participation'),
    AchReturnCodeInfo('R31', 'Permissible CCD or CTX Return', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'request'),
    AchReturnCodeInfo('R32', 'RDFI Non-Settlement', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'settlement'),
    AchReturnCodeInfo('R33', 'Return of XCK Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'check_entry'),
    AchReturnCodeInfo('R34', 'Limited Participation DFI', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'participation'),
    AchReturnCodeInfo('R35', 'Improper Debit Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'improper_entry'),
    AchReturnCodeInfo('R36', 'Improper Credit Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'improper_entry'),
    AchReturnCodeInfo('R37', 'Source Document Presented for Payment', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'source_document'),
    AchReturnCodeInfo('R38', 'Stop Payment on Source Document', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'source_document'),
    AchReturnCodeInfo('R39', 'Improper Source Document or Duplicate Presentment', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'source_document'),
    AchReturnCodeInfo('R40', 'Federal Agency Return of ENR Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'enrollment'),
    AchReturnCodeInfo('R41', 'Invalid Transaction Code for ENR', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'enrollment'),
    AchReturnCodeInfo('R42', 'Routing Number or Check Digit Error for ENR', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'enrollment'),
    AchReturnCodeInfo('R43', 'Invalid DFI Account Number for ENR', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'enrollment'),
    AchReturnCodeInfo('R44', 'Invalid Identification Number for ENR', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'enrollment'),
    AchReturnCodeInfo('R45', 'Invalid Individual or Company Name for ENR', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'enrollment'),
    AchReturnCodeInfo('R46', 'Invalid Representative Payee Indicator for ENR', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'enrollment'),
    AchReturnCodeInfo('R47', 'Duplicate Enrollment', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'enrollment'),
    AchReturnCodeInfo('R50', 'State Law Affecting RCK Acceptance', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'rck'),
    AchReturnCodeInfo('R51', 'Ineligible or Improper RCK Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'rck'),
    AchReturnCodeInfo('R52', 'Stop Payment on Item Related to RCK Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'rck'),
    AchReturnCodeInfo('R53', 'Item and RCK Entry Presented for Payment', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'rck'),
    AchReturnCodeInfo('R61', 'Misrouted Return', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'dishonored_return'),
    AchReturnCodeInfo('R62', 'Return of Erroneous or Reversing Debit', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'dishonored_return'),
    AchReturnCodeInfo('R67', 'Duplicate Return', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'dishonored_return'),
    AchReturnCodeInfo('R68', 'Untimely Return', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'dishonored_return'),
    AchReturnCodeInfo('R69', 'Return Field Errors', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'dishonored_return'),
    AchReturnCodeInfo('R70', 'Permissible Return Not Accepted or Requested', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'dishonored_return'),
    AchReturnCodeInfo('R71', 'Misrouted Dishonored Return', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'contested_dishonored_return'),
    AchReturnCodeInfo('R72', 'Untimely Dishonored Return', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'contested_dishonored_return'),
    AchReturnCodeInfo('R73', 'Timely Original Return', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'contested_dishonored_return'),
    AchReturnCodeInfo('R74', 'Corrected Return', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'contested_dishonored_return'),
    AchReturnCodeInfo('R75', 'Return Not a Duplicate', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'contested_dishonored_return'),
    AchReturnCodeInfo('R76', 'No Errors Found', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'contested_dishonored_return'),
    AchReturnCodeInfo('R77', 'Non-Acceptance of R62 Dishonored Return', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'contested_dishonored_return'),
    AchReturnCodeInfo('R80', 'IAT Entry Coding Error', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'international'),
    AchReturnCodeInfo('R81', 'Non-Participant in IAT Program', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'international'),
    AchReturnCodeInfo('R82', 'Invalid Foreign Receiving DFI Identification', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'international'),
    AchReturnCodeInfo('R83', 'Foreign Receiving DFI Unable to Settle', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'international'),
    AchReturnCodeInfo('R84', 'Entry Not Processed by Gateway', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'international'),
    AchReturnCodeInfo('R85', 'Incorrectly Coded Outbound International Payment', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'nacha_iso20022_2023'), 'undo', 'international'),
    AchReturnCodeInfo('R90', 'Return for Sanctions Compliance', AchCodeStatus.PLANNED, date(2028, 3, 17), None, ('nacha_rule_r90',), 'undo', 'compliance'),
)


STANDARD_ENTRY_CLASS_CODE_RECORDS: Final[tuple[AchStandardEntryClassCodeInfo, ...]] = (
    AchStandardEntryClassCodeInfo('ACK', 'Acknowledgment Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'acknowledgment', 'corporate', 'nonmonetary', 'optional_one'),
    AchStandardEntryClassCodeInfo('ADV', 'Automated Accounting Advice', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'accounting', 'financial_institution', 'nonmonetary', 'none'),
    AchStandardEntryClassCodeInfo('ARC', 'Accounts Receivable Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'check_conversion', 'consumer', 'debit', 'none'),
    AchStandardEntryClassCodeInfo('ATX', 'Financial EDI Acknowledgment', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'acknowledgment', 'corporate', 'nonmonetary', 'optional_one'),
    AchStandardEntryClassCodeInfo('BOC', 'Back Office Conversion Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'check_conversion', 'consumer', 'debit', 'none'),
    AchStandardEntryClassCodeInfo('CCD', 'Corporate Credit or Debit Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'payment', 'corporate', 'credit_or_debit', 'optional_one'),
    AchStandardEntryClassCodeInfo('CIE', 'Customer-Initiated Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'payment', 'consumer_to_corporate', 'credit', 'optional_one'),
    AchStandardEntryClassCodeInfo('COR', 'Notification of Change', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'notification', 'consumer_or_corporate', 'nonmonetary', 'required_one'),
    AchStandardEntryClassCodeInfo('CTX', 'Corporate Trade Exchange Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'payment', 'corporate', 'credit_or_debit', 'optional_many'),
    AchStandardEntryClassCodeInfo('DNE', 'Death Notification Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'notification', 'consumer', 'nonmonetary', 'required_one'),
    AchStandardEntryClassCodeInfo('ENR', 'Automated Enrollment Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'enrollment', 'consumer', 'nonmonetary', 'required_many'),
    AchStandardEntryClassCodeInfo('IAT', 'International ACH Transaction', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025', 'nacha_iat_2026'), 'account_balance', 'payment', 'consumer_or_corporate', 'credit_or_debit', 'required_seven_optional_five'),
    AchStandardEntryClassCodeInfo('MTE', 'Machine Transfer Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'terminal', 'consumer', 'credit_or_debit', 'required_one'),
    AchStandardEntryClassCodeInfo('POP', 'Point-of-Purchase Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'check_conversion', 'consumer', 'debit', 'none'),
    AchStandardEntryClassCodeInfo('POS', 'Point-of-Sale Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'terminal', 'consumer', 'debit', 'required_one'),
    AchStandardEntryClassCodeInfo('PPD', 'Prearranged Payment and Deposit Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'payment', 'consumer', 'credit_or_debit', 'optional_one'),
    AchStandardEntryClassCodeInfo('RCK', 'Re-presented Check Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'check_conversion', 'consumer', 'debit', 'none'),
    AchStandardEntryClassCodeInfo('SHR', 'Shared Network Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'terminal', 'consumer', 'debit', 'required_one'),
    AchStandardEntryClassCodeInfo('TEL', 'Telephone-Initiated Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'payment', 'consumer', 'debit', 'none'),
    AchStandardEntryClassCodeInfo('TRC', 'Truncated Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'check_truncation', 'consumer', 'debit', 'none'),
    AchStandardEntryClassCodeInfo('TRX', 'Truncated Entries Exchange', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'check_truncation', 'consumer', 'debit', 'required_many'),
    AchStandardEntryClassCodeInfo('WEB', 'Internet-Initiated or Mobile Entry', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide', 'nacha_basic_2025'), 'account_balance', 'payment', 'consumer', 'credit_or_debit', 'optional_one'),
    AchStandardEntryClassCodeInfo('XCK', 'Destroyed Check Entry', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'account_balance', 'check_replacement', 'consumer', 'debit', 'none'),
)


SERVICE_CLASS_CODE_RECORDS: Final[tuple[AchServiceClassCodeInfo, ...]] = (
    AchServiceClassCodeInfo('200', 'Mixed Debits and Credits', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide',), 'sync_alt', 'mixed'),
    AchServiceClassCodeInfo('220', 'Credits Only', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide',), 'sync_alt', 'credit'),
    AchServiceClassCodeInfo('225', 'Debits Only', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide',), 'sync_alt', 'debit'),
    AchServiceClassCodeInfo('280', 'Automated Accounting Advices', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'sync_alt', 'accounting'),
)


RECORD_TYPE_CODE_RECORDS: Final[tuple[AchRecordTypeCodeInfo, ...]] = (
    AchRecordTypeCodeInfo('1', 'File Header', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide',), 'description'),
    AchRecordTypeCodeInfo('5', 'Company or Batch Header', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide',), 'description'),
    AchRecordTypeCodeInfo('6', 'Entry Detail', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide',), 'description'),
    AchRecordTypeCodeInfo('7', 'Addenda', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide',), 'description'),
    AchRecordTypeCodeInfo('8', 'Company or Batch Control', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide',), 'description'),
    AchRecordTypeCodeInfo('9', 'File Control or Padding', AchCodeStatus.CURRENT, None, None, ('nacha_developer_guide',), 'description'),
)


CHANGE_CODE_RECORDS: Final[tuple[AchChangeCodeInfo, ...]] = (
    AchChangeCodeInfo('C01', 'Incorrect DFI Account Number', AchCodeStatus.CURRENT, None, None, ('nacha_iso20022_2023', 'nacha_basic_2025'), 'edit', ('account_number',), ('all',)),
    AchChangeCodeInfo('C02', 'Incorrect Routing Number', AchCodeStatus.CURRENT, None, None, ('nacha_iso20022_2023', 'nacha_basic_2025'), 'edit', ('routing_number',), ('all',)),
    AchChangeCodeInfo('C03', 'Incorrect Routing and DFI Account Numbers', AchCodeStatus.CURRENT, None, None, ('nacha_iso20022_2023', 'nacha_basic_2025'), 'edit', ('routing_number', 'account_number'), ('all',)),
    AchChangeCodeInfo('C05', 'Incorrect Transaction Code', AchCodeStatus.CURRENT, None, None, ('nacha_iso20022_2023', 'nacha_basic_2025'), 'edit', ('transaction_code',), ('all',)),
    AchChangeCodeInfo('C06', 'Incorrect DFI Account Number and Transaction Code', AchCodeStatus.CURRENT, None, None, ('nacha_iso20022_2023', 'nacha_basic_2025'), 'edit', ('account_number', 'transaction_code'), ('all',)),
    AchChangeCodeInfo('C07', 'Incorrect Routing Number DFI Account Number and Transaction Code', AchCodeStatus.CURRENT, None, None, ('nacha_iso20022_2023', 'nacha_basic_2025'), 'edit', ('routing_number', 'account_number', 'transaction_code'), ('all',)),
    AchChangeCodeInfo('C08', 'Incorrect Receiving DFI Identification', AchCodeStatus.CURRENT, None, None, ('nacha_iso20022_2023', 'nacha_basic_2025'), 'edit', ('receiving_dfi_identification',), ('IAT',)),
    AchChangeCodeInfo('C09', 'Incorrect Individual or Receiver Identification Number', AchCodeStatus.CURRENT, None, None, ('nacha_iso20022_2023', 'nacha_basic_2025'), 'edit', ('individual_or_receiver_id',), ('all',)),
    AchChangeCodeInfo('C13', 'Addenda Format Error', AchCodeStatus.CURRENT, None, None, ('nacha_iso20022_2023', 'nacha_basic_2025'), 'edit', ('addenda_format',), ('entries_with_addenda',)),
    AchChangeCodeInfo('C14', 'Incorrect SEC Code for Outbound International Payment', AchCodeStatus.CURRENT, None, None, ('nacha_iso20022_2023', 'nacha_basic_2025'), 'edit', ('sec_code',), ('outbound_international',)),
)


ADDENDA_TYPE_CODE_RECORDS: Final[tuple[AchAddendaTypeCodeInfo, ...]] = (
    AchAddendaTypeCodeInfo('01', 'Legacy Cross-Border Payment Information', AchCodeStatus.LEGACY, None, None, ('nacha_basic_2025',), 'note_add', ('CBR', 'PBR')),
    AchAddendaTypeCodeInfo('02', 'Terminal Location Information', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'note_add', ('MTE', 'POS', 'SHR')),
    AchAddendaTypeCodeInfo('05', 'Payment-Related Information', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'note_add', ('ACK', 'ATX', 'CCD', 'CIE', 'CTX', 'DNE', 'ENR', 'PPD', 'TRX', 'WEB')),
    AchAddendaTypeCodeInfo('10', 'First Mandatory IAT Addenda', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'fedglobal_manual_2026'), 'note_add', ('IAT',)),
    AchAddendaTypeCodeInfo('11', 'Second Mandatory IAT Addenda', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'fedglobal_manual_2026'), 'note_add', ('IAT',)),
    AchAddendaTypeCodeInfo('12', 'Third Mandatory IAT Addenda', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'fedglobal_manual_2026'), 'note_add', ('IAT',)),
    AchAddendaTypeCodeInfo('13', 'Fourth Mandatory IAT Addenda', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'fedglobal_manual_2026'), 'note_add', ('IAT',)),
    AchAddendaTypeCodeInfo('14', 'Fifth Mandatory IAT Addenda', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'fedglobal_manual_2026'), 'note_add', ('IAT',)),
    AchAddendaTypeCodeInfo('15', 'Sixth Mandatory IAT Addenda', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'fedglobal_manual_2026'), 'note_add', ('IAT',)),
    AchAddendaTypeCodeInfo('16', 'Seventh Mandatory IAT Addenda', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'fedglobal_manual_2026'), 'note_add', ('IAT',)),
    AchAddendaTypeCodeInfo('17', 'IAT Remittance Information', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'fedglobal_manual_2026'), 'note_add', ('IAT',)),
    AchAddendaTypeCodeInfo('18', 'IAT Foreign Correspondent Bank Information', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025', 'fedglobal_manual_2026'), 'note_add', ('IAT',)),
    AchAddendaTypeCodeInfo('98', 'Notification of Change Information', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'note_add', ('COR', 'refused_COR')),
    AchAddendaTypeCodeInfo('99', 'Return Information', AchCodeStatus.CURRENT, None, None, ('nacha_basic_2025',), 'note_add', ('return', 'dishonored_return', 'contested_return')),
)

_InfoT = TypeVar('_InfoT', bound=AchReferenceInfo)


def _index(records: tuple[_InfoT, ...]) -> Mapping[str, tuple[_InfoT, ...]]:
    mutable: dict[str, list[_InfoT]] = {}
    for record in records:
        mutable.setdefault(record.code, []).append(record)
    return MappingProxyType({code: tuple(values) for code, values in mutable.items()})


def _resolve(
    index: Mapping[str, tuple[_InfoT, ...]],
    value: object,
    on: date,
    include_inactive: bool,
) -> _InfoT | None:
    code = value.value if isinstance(value, _AchCode) else value
    if not isinstance(code, str):
        return None
    records = index.get(code.strip().upper())
    if not records:
        return None
    for record in records:
        if record.is_effective(on):
            return record
    return records[0] if include_inactive else None

_TRANSACTION_CODE_BY_CODE: Final = _index(TRANSACTION_CODE_RECORDS)
_DEFAULT_TRANSACTION_CODE_INFO: Final[Mapping[str, AchTransactionCodeInfo]] = MappingProxyType({
    code: _resolve(_TRANSACTION_CODE_BY_CODE, code, REFERENCE_AS_OF, True)
    for code in _TRANSACTION_CODE_BY_CODE
})  # type: ignore[dict-item]
CURRENT_TRANSACTION_CODE_RECORDS: Final = tuple(
    record for record in TRANSACTION_CODE_RECORDS if record.is_effective()
)
TRANSACTION_CODE_COUNT: Final = len(_TRANSACTION_CODE_BY_CODE)
TRANSACTION_CODE_RECORD_COUNT: Final = len(TRANSACTION_CODE_RECORDS)
CURRENT_TRANSACTION_CODE_COUNT: Final = len(CURRENT_TRANSACTION_CODE_RECORDS)

def resolve_transaction_code(
    code: str | AchTransactionCode, *, include_inactive: bool = False
) -> AchTransactionCodeInfo | None:
    return _resolve(_TRANSACTION_CODE_BY_CODE, code, REFERENCE_AS_OF, include_inactive)

def resolve_transaction_code_as_of(
    code: str | AchTransactionCode, on: date, *, include_inactive: bool = False
) -> AchTransactionCodeInfo | None:
    return _resolve(_TRANSACTION_CODE_BY_CODE, code, on, include_inactive)

_RETURN_CODE_BY_CODE: Final = _index(RETURN_CODE_RECORDS)
_DEFAULT_RETURN_CODE_INFO: Final[Mapping[str, AchReturnCodeInfo]] = MappingProxyType({
    code: _resolve(_RETURN_CODE_BY_CODE, code, REFERENCE_AS_OF, True)
    for code in _RETURN_CODE_BY_CODE
})  # type: ignore[dict-item]
CURRENT_RETURN_CODE_RECORDS: Final = tuple(
    record for record in RETURN_CODE_RECORDS if record.is_effective()
)
RETURN_CODE_COUNT: Final = len(_RETURN_CODE_BY_CODE)
RETURN_CODE_RECORD_COUNT: Final = len(RETURN_CODE_RECORDS)
CURRENT_RETURN_CODE_COUNT: Final = len(CURRENT_RETURN_CODE_RECORDS)

def resolve_return_code(
    code: str | AchReturnCode, *, include_inactive: bool = False
) -> AchReturnCodeInfo | None:
    return _resolve(_RETURN_CODE_BY_CODE, code, REFERENCE_AS_OF, include_inactive)

def resolve_return_code_as_of(
    code: str | AchReturnCode, on: date, *, include_inactive: bool = False
) -> AchReturnCodeInfo | None:
    return _resolve(_RETURN_CODE_BY_CODE, code, on, include_inactive)

_STANDARD_ENTRY_CLASS_CODE_BY_CODE: Final = _index(STANDARD_ENTRY_CLASS_CODE_RECORDS)
_DEFAULT_STANDARD_ENTRY_CLASS_CODE_INFO: Final[Mapping[str, AchStandardEntryClassCodeInfo]] = MappingProxyType({
    code: _resolve(_STANDARD_ENTRY_CLASS_CODE_BY_CODE, code, REFERENCE_AS_OF, True)
    for code in _STANDARD_ENTRY_CLASS_CODE_BY_CODE
})  # type: ignore[dict-item]
CURRENT_STANDARD_ENTRY_CLASS_CODE_RECORDS: Final = tuple(
    record for record in STANDARD_ENTRY_CLASS_CODE_RECORDS if record.is_effective()
)
STANDARD_ENTRY_CLASS_CODE_COUNT: Final = len(_STANDARD_ENTRY_CLASS_CODE_BY_CODE)
STANDARD_ENTRY_CLASS_CODE_RECORD_COUNT: Final = len(STANDARD_ENTRY_CLASS_CODE_RECORDS)
CURRENT_STANDARD_ENTRY_CLASS_CODE_COUNT: Final = len(CURRENT_STANDARD_ENTRY_CLASS_CODE_RECORDS)

def resolve_standard_entry_class_code(
    code: str | AchStandardEntryClassCode, *, include_inactive: bool = False
) -> AchStandardEntryClassCodeInfo | None:
    return _resolve(_STANDARD_ENTRY_CLASS_CODE_BY_CODE, code, REFERENCE_AS_OF, include_inactive)

def resolve_standard_entry_class_code_as_of(
    code: str | AchStandardEntryClassCode, on: date, *, include_inactive: bool = False
) -> AchStandardEntryClassCodeInfo | None:
    return _resolve(_STANDARD_ENTRY_CLASS_CODE_BY_CODE, code, on, include_inactive)

_SERVICE_CLASS_CODE_BY_CODE: Final = _index(SERVICE_CLASS_CODE_RECORDS)
_DEFAULT_SERVICE_CLASS_CODE_INFO: Final[Mapping[str, AchServiceClassCodeInfo]] = MappingProxyType({
    code: _resolve(_SERVICE_CLASS_CODE_BY_CODE, code, REFERENCE_AS_OF, True)
    for code in _SERVICE_CLASS_CODE_BY_CODE
})  # type: ignore[dict-item]
CURRENT_SERVICE_CLASS_CODE_RECORDS: Final = tuple(
    record for record in SERVICE_CLASS_CODE_RECORDS if record.is_effective()
)
SERVICE_CLASS_CODE_COUNT: Final = len(_SERVICE_CLASS_CODE_BY_CODE)
SERVICE_CLASS_CODE_RECORD_COUNT: Final = len(SERVICE_CLASS_CODE_RECORDS)
CURRENT_SERVICE_CLASS_CODE_COUNT: Final = len(CURRENT_SERVICE_CLASS_CODE_RECORDS)

def resolve_service_class_code(
    code: str | AchServiceClassCode, *, include_inactive: bool = False
) -> AchServiceClassCodeInfo | None:
    return _resolve(_SERVICE_CLASS_CODE_BY_CODE, code, REFERENCE_AS_OF, include_inactive)

def resolve_service_class_code_as_of(
    code: str | AchServiceClassCode, on: date, *, include_inactive: bool = False
) -> AchServiceClassCodeInfo | None:
    return _resolve(_SERVICE_CLASS_CODE_BY_CODE, code, on, include_inactive)

_RECORD_TYPE_CODE_BY_CODE: Final = _index(RECORD_TYPE_CODE_RECORDS)
_DEFAULT_RECORD_TYPE_CODE_INFO: Final[Mapping[str, AchRecordTypeCodeInfo]] = MappingProxyType({
    code: _resolve(_RECORD_TYPE_CODE_BY_CODE, code, REFERENCE_AS_OF, True)
    for code in _RECORD_TYPE_CODE_BY_CODE
})  # type: ignore[dict-item]
CURRENT_RECORD_TYPE_CODE_RECORDS: Final = tuple(
    record for record in RECORD_TYPE_CODE_RECORDS if record.is_effective()
)
RECORD_TYPE_CODE_COUNT: Final = len(_RECORD_TYPE_CODE_BY_CODE)
RECORD_TYPE_CODE_RECORD_COUNT: Final = len(RECORD_TYPE_CODE_RECORDS)
CURRENT_RECORD_TYPE_CODE_COUNT: Final = len(CURRENT_RECORD_TYPE_CODE_RECORDS)

def resolve_record_type_code(
    code: str | AchRecordTypeCode, *, include_inactive: bool = False
) -> AchRecordTypeCodeInfo | None:
    return _resolve(_RECORD_TYPE_CODE_BY_CODE, code, REFERENCE_AS_OF, include_inactive)

def resolve_record_type_code_as_of(
    code: str | AchRecordTypeCode, on: date, *, include_inactive: bool = False
) -> AchRecordTypeCodeInfo | None:
    return _resolve(_RECORD_TYPE_CODE_BY_CODE, code, on, include_inactive)

_CHANGE_CODE_BY_CODE: Final = _index(CHANGE_CODE_RECORDS)
_DEFAULT_CHANGE_CODE_INFO: Final[Mapping[str, AchChangeCodeInfo]] = MappingProxyType({
    code: _resolve(_CHANGE_CODE_BY_CODE, code, REFERENCE_AS_OF, True)
    for code in _CHANGE_CODE_BY_CODE
})  # type: ignore[dict-item]
CURRENT_CHANGE_CODE_RECORDS: Final = tuple(
    record for record in CHANGE_CODE_RECORDS if record.is_effective()
)
CHANGE_CODE_COUNT: Final = len(_CHANGE_CODE_BY_CODE)
CHANGE_CODE_RECORD_COUNT: Final = len(CHANGE_CODE_RECORDS)
CURRENT_CHANGE_CODE_COUNT: Final = len(CURRENT_CHANGE_CODE_RECORDS)

def resolve_change_code(
    code: str | AchChangeCode, *, include_inactive: bool = False
) -> AchChangeCodeInfo | None:
    return _resolve(_CHANGE_CODE_BY_CODE, code, REFERENCE_AS_OF, include_inactive)

def resolve_change_code_as_of(
    code: str | AchChangeCode, on: date, *, include_inactive: bool = False
) -> AchChangeCodeInfo | None:
    return _resolve(_CHANGE_CODE_BY_CODE, code, on, include_inactive)

_ADDENDA_TYPE_CODE_BY_CODE: Final = _index(ADDENDA_TYPE_CODE_RECORDS)
_DEFAULT_ADDENDA_TYPE_CODE_INFO: Final[Mapping[str, AchAddendaTypeCodeInfo]] = MappingProxyType({
    code: _resolve(_ADDENDA_TYPE_CODE_BY_CODE, code, REFERENCE_AS_OF, True)
    for code in _ADDENDA_TYPE_CODE_BY_CODE
})  # type: ignore[dict-item]
CURRENT_ADDENDA_TYPE_CODE_RECORDS: Final = tuple(
    record for record in ADDENDA_TYPE_CODE_RECORDS if record.is_effective()
)
ADDENDA_TYPE_CODE_COUNT: Final = len(_ADDENDA_TYPE_CODE_BY_CODE)
ADDENDA_TYPE_CODE_RECORD_COUNT: Final = len(ADDENDA_TYPE_CODE_RECORDS)
CURRENT_ADDENDA_TYPE_CODE_COUNT: Final = len(CURRENT_ADDENDA_TYPE_CODE_RECORDS)

def resolve_addenda_type_code(
    code: str | AchAddendaTypeCode, *, include_inactive: bool = False
) -> AchAddendaTypeCodeInfo | None:
    return _resolve(_ADDENDA_TYPE_CODE_BY_CODE, code, REFERENCE_AS_OF, include_inactive)

def resolve_addenda_type_code_as_of(
    code: str | AchAddendaTypeCode, on: date, *, include_inactive: bool = False
) -> AchAddendaTypeCodeInfo | None:
    return _resolve(_ADDENDA_TYPE_CODE_BY_CODE, code, on, include_inactive)

RECORDS: Final[Mapping[str, tuple[AchReferenceInfo, ...]]] = MappingProxyType({
    'transaction_codes': TRANSACTION_CODE_RECORDS,
    'return_codes': RETURN_CODE_RECORDS,
    'standard_entry_class_codes': STANDARD_ENTRY_CLASS_CODE_RECORDS,
    'service_class_codes': SERVICE_CLASS_CODE_RECORDS,
    'record_type_codes': RECORD_TYPE_CODE_RECORDS,
    'change_codes': CHANGE_CODE_RECORDS,
    'addenda_type_codes': ADDENDA_TYPE_CODE_RECORDS,
})

COUNTS: Final[Mapping[str, int]] = MappingProxyType({
    'transaction_codes': TRANSACTION_CODE_COUNT,
    'return_codes': RETURN_CODE_COUNT,
    'standard_entry_class_codes': STANDARD_ENTRY_CLASS_CODE_COUNT,
    'service_class_codes': SERVICE_CLASS_CODE_COUNT,
    'record_type_codes': RECORD_TYPE_CODE_COUNT,
    'change_codes': CHANGE_CODE_COUNT,
    'addenda_type_codes': ADDENDA_TYPE_CODE_COUNT,
})
