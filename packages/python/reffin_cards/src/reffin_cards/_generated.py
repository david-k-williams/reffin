"""Generated card reference vocabularies. Do not edit by hand."""

# Input SHA-256: b4c71185e3980ee36870429da227c0e4b8b220a039679e0f6bf3bff18376db44
from __future__ import annotations

from enum import Enum
from types import MappingProxyType
from typing import Final, Mapping, Self


DATA_FINGERPRINT: Final = 'b4c71185e3980ee36870429da227c0e4b8b220a039679e0f6bf3bff18376db44'


class _ReferenceEnum(Enum):
    label: str

    @property
    def id(self) -> str:
        return str(self.value)

    @classmethod
    def try_parse(cls, value: object) -> Self | None:
        try:
            return cls(value)
        except (TypeError, ValueError):
            return None


class CardNetwork(_ReferenceEnum):
    AMERICAN_EXPRESS = ('american_express', 'American Express', 'credit_card', 'american_express')
    CARTES_BANCAIRES = ('cartes_bancaires', 'Cartes Bancaires', 'credit_card', 'cartes_bancaires')
    DINERS_CLUB = ('diners_club', 'Diners Club', 'credit_card', 'diners_club')
    DISCOVER = ('discover', 'Discover', 'credit_card', 'discover')
    EFTPOS_AUSTRALIA = ('eftpos_australia', 'eftpos Australia', 'credit_card', 'eftpos_australia')
    ELO = ('elo', 'Elo', 'credit_card', 'elo')
    GIROCARD = ('girocard', 'girocard', 'credit_card', 'girocard')
    INTERAC = ('interac', 'Interac', 'credit_card', 'interac')
    JCB = ('jcb', 'JCB', 'credit_card', 'jcb')
    MAESTRO = ('maestro', 'Maestro', 'credit_card', 'maestro')
    MASTERCARD = ('mastercard', 'Mastercard', 'credit_card', 'mastercard')
    OTHER = ('other', 'Other', 'credit_card', None)
    RUPAY = ('rupay', 'RuPay', 'credit_card', 'rupay')
    UNIONPAY = ('unionpay', 'UnionPay', 'credit_card', 'unionpay')
    UNKNOWN = ('unknown', 'Unknown', 'credit_card', None)
    VISA = ('visa', 'Visa', 'credit_card', 'visa')

    def __new__(cls, identifier: str, display_name: str, material_symbol: str, brand_asset_key: str | None) -> CardNetwork:
        member = object.__new__(cls)
        member._value_ = identifier
        member.label = display_name
        member.material_symbol = material_symbol
        member.brand_asset_key = brand_asset_key
        return member

    material_symbol: str
    brand_asset_key: str | None


class FormFactor(_ReferenceEnum):
    OTHER = ('other', 'Other', 'more_horiz', 'A known form factor outside the named normalized values')
    PHYSICAL = ('physical', 'Physical', 'credit_card', 'A card credential issued on a tangible card body')
    UNKNOWN = ('unknown', 'Unknown', 'help_outline', 'The form factor was not supplied or could not be determined')
    VIRTUAL = ('virtual', 'Virtual', 'devices', 'A card credential intended for use without a physical card body')

    def __new__(cls, identifier: str, display_name: str, material_symbol: str, description: str) -> FormFactor:
        member = object.__new__(cls)
        member._value_ = identifier
        member.label = display_name
        member.material_symbol = material_symbol
        member.description = description
        return member

    material_symbol: str
    description: str


class FundingType(_ReferenceEnum):
    CHARGE = ('charge', 'Charge', 'receipt_long', 'A balance that is normally due in full at the end of a billing period')
    CREDIT = ('credit', 'Credit', 'credit_score', 'Funds extended by an issuer and repaid under a credit agreement')
    DEBIT = ('debit', 'Debit', 'account_balance_wallet', 'Funds drawn from a linked deposit or transaction account')
    OTHER = ('other', 'Other', 'more_horiz', 'A known funding model outside the named normalized values')
    PREPAID = ('prepaid', 'Prepaid', 'redeem', 'Value funded before it is used for payment')
    UNKNOWN = ('unknown', 'Unknown', 'help_outline', 'The funding model was not supplied or could not be determined')

    def __new__(cls, identifier: str, display_name: str, material_symbol: str, description: str) -> FundingType:
        member = object.__new__(cls)
        member._value_ = identifier
        member.label = display_name
        member.material_symbol = material_symbol
        member.description = description
        return member

    material_symbol: str
    description: str


class PaymentMethodFamily(_ReferenceEnum):
    BANK_TRANSFER = ('bank_transfer', 'Bank Transfer', 'account_balance', 'A payer-initiated transfer between financial accounts')
    BUY_NOW_PAY_LATER = ('buy_now_pay_later', 'Buy Now Pay Later', 'calendar_month', 'A purchase paid through a deferred or installment arrangement')
    CARD = ('card', 'Card', 'credit_card', 'A payment made with a card credential')
    CASH = ('cash', 'Cash', 'payments', 'A payment made with physical currency')
    CHECK = ('check', 'Check', 'receipt_long', 'A payment made with a paper or electronic check instrument')
    CRYPTOCURRENCY = ('cryptocurrency', 'Cryptocurrency', 'currency_exchange', 'A payment made by transferring a cryptographic asset')
    DIGITAL_WALLET = ('digital_wallet', 'Digital Wallet', 'account_balance_wallet', 'A payment initiated through a digital wallet interface')
    DIRECT_DEBIT = ('direct_debit', 'Direct Debit', 'sync_alt', 'A payee-initiated debit from a financial account under an authorization')
    MOBILE_MONEY = ('mobile_money', 'Mobile Money', 'smartphone', 'A payment made through a mobile money account')
    OTHER = ('other', 'Other', 'more_horiz', 'A known payment method family outside the named normalized values')
    UNKNOWN = ('unknown', 'Unknown', 'help_outline', 'The payment method family was not supplied or could not be determined')
    VOUCHER = ('voucher', 'Voucher', 'confirmation_number', 'A payment made with a voucher coupon or redeemable code')

    def __new__(cls, identifier: str, display_name: str, material_symbol: str, description: str) -> PaymentMethodFamily:
        member = object.__new__(cls)
        member._value_ = identifier
        member.label = display_name
        member.material_symbol = material_symbol
        member.description = description
        return member

    material_symbol: str
    description: str


class PaymentOutcome(_ReferenceEnum):
    APPROVED = ('approved', 'Approved', 'check_circle', 'The payment or authorization was accepted for the requested amount')
    CANCELED = ('canceled', 'Canceled', 'cancel', 'Processing was stopped before a final successful outcome')
    DECLINED = ('declined', 'Declined', 'block', 'The payment or authorization was actively refused')
    FAILED = ('failed', 'Failed', 'error_outline', 'Processing did not complete because of an error rather than an explicit decline')
    PARTIALLY_APPROVED = ('partially_approved', 'Partially Approved', 'rule', 'The payment or authorization was accepted for less than the requested amount')
    PENDING = ('pending', 'Pending', 'schedule', 'A final processing outcome is not yet available')
    REVERSED = ('reversed', 'Reversed', 'undo', 'A previous approval was undone or released before settlement')
    UNKNOWN = ('unknown', 'Unknown', 'help_outline', 'The raw result was missing or had no known normalized outcome')

    def __new__(cls, identifier: str, display_name: str, material_symbol: str, description: str) -> PaymentOutcome:
        member = object.__new__(cls)
        member._value_ = identifier
        member.label = display_name
        member.material_symbol = material_symbol
        member.description = description
        return member

    material_symbol: str
    description: str


class ProductClass(_ReferenceEnum):
    COMMERCIAL = ('commercial', 'Commercial', 'business', 'A card product intended primarily for organizational or business spending')
    CONSUMER = ('consumer', 'Consumer', 'person', 'A card product intended primarily for an individual or household')
    GOVERNMENT = ('government', 'Government', 'account_balance', 'A card product intended primarily for a public-sector program')
    OTHER = ('other', 'Other', 'more_horiz', 'A known product class outside the named normalized values')
    UNKNOWN = ('unknown', 'Unknown', 'help_outline', 'The product class was not supplied or could not be determined')

    def __new__(cls, identifier: str, display_name: str, material_symbol: str, description: str) -> ProductClass:
        member = object.__new__(cls)
        member._value_ = identifier
        member.label = display_name
        member.material_symbol = material_symbol
        member.description = description
        return member

    material_symbol: str
    description: str


class TransactionChannel(_ReferenceEnum):
    IN_APP = ('in_app', 'In App', 'apps', 'A transaction initiated inside a native or installed application')
    IN_PERSON = ('in_person', 'In Person', 'point_of_sale', 'A transaction initiated with the customer at a staffed or unattended physical location')
    MAIL_ORDER = ('mail_order', 'Mail Order', 'mail', 'A remote transaction initiated through postal correspondence')
    ONLINE = ('online', 'Online', 'language', 'A transaction initiated through a web or other online checkout outside a native application')
    OTHER_REMOTE = ('other_remote', 'Other Remote', 'devices_other', 'A known remote interaction surface outside the named normalized values')
    TELEPHONE_ORDER = ('telephone_order', 'Telephone Order', 'phone_in_talk', 'A remote transaction initiated through a voice telephone interaction')
    UNKNOWN = ('unknown', 'Unknown', 'help_outline', 'The transaction channel was not supplied or could not be determined')

    def __new__(cls, identifier: str, display_name: str, material_symbol: str, description: str) -> TransactionChannel:
        member = object.__new__(cls)
        member._value_ = identifier
        member.label = display_name
        member.material_symbol = material_symbol
        member.description = description
        return member

    material_symbol: str
    description: str


class VerificationOutcome(_ReferenceEnum):
    MATCH = ('match', 'Match', 'verified', 'The submitted value matched the reference used by the verification service')
    NO_MATCH = ('no_match', 'No Match', 'cancel', 'The submitted value did not match the reference used by the verification service')
    NOT_APPLICABLE = ('not_applicable', 'Not Applicable', 'remove_circle_outline', 'The verification check did not apply to this transaction or credential')
    NOT_PROVIDED = ('not_provided', 'Not Provided', 'horizontal_rule', 'A value was not supplied for verification')
    NOT_SUPPORTED = ('not_supported', 'Not Supported', 'block', 'The verification service or source did not support the check')
    NOT_VERIFIED = ('not_verified', 'Not Verified', 'help', 'A conclusive verification result was not produced')
    PARTIAL_MATCH = ('partial_match', 'Partial Match', 'rule', 'Only part of the submitted value matched the reference used by the verification service')
    SKIPPED = ('skipped', 'Skipped', 'skip_next', 'The verification check was intentionally not attempted')
    SYSTEM_ERROR = ('system_error', 'System Error', 'error_outline', 'The verification check could not complete because of a system or communication error')
    UNKNOWN = ('unknown', 'Unknown', 'help_outline', 'The raw result was missing or had no known normalized outcome')

    def __new__(cls, identifier: str, display_name: str, material_symbol: str, description: str) -> VerificationOutcome:
        member = object.__new__(cls)
        member._value_ = identifier
        member.label = display_name
        member.material_symbol = material_symbol
        member.description = description
        return member

    material_symbol: str
    description: str


CARD_NETWORK_RECORDS: Final[tuple[CardNetwork, ...]] = tuple(CardNetwork)
CARD_NETWORK_COUNT: Final = len(CARD_NETWORK_RECORDS)
FORM_FACTOR_RECORDS: Final[tuple[FormFactor, ...]] = tuple(FormFactor)
FORM_FACTOR_COUNT: Final = len(FORM_FACTOR_RECORDS)
FUNDING_TYPE_RECORDS: Final[tuple[FundingType, ...]] = tuple(FundingType)
FUNDING_TYPE_COUNT: Final = len(FUNDING_TYPE_RECORDS)
PAYMENT_METHOD_FAMILY_RECORDS: Final[tuple[PaymentMethodFamily, ...]] = tuple(PaymentMethodFamily)
PAYMENT_METHOD_FAMILY_COUNT: Final = len(PAYMENT_METHOD_FAMILY_RECORDS)
PAYMENT_OUTCOME_RECORDS: Final[tuple[PaymentOutcome, ...]] = tuple(PaymentOutcome)
PAYMENT_OUTCOME_COUNT: Final = len(PAYMENT_OUTCOME_RECORDS)
PRODUCT_CLASS_RECORDS: Final[tuple[ProductClass, ...]] = tuple(ProductClass)
PRODUCT_CLASS_COUNT: Final = len(PRODUCT_CLASS_RECORDS)
TRANSACTION_CHANNEL_RECORDS: Final[tuple[TransactionChannel, ...]] = tuple(TransactionChannel)
TRANSACTION_CHANNEL_COUNT: Final = len(TRANSACTION_CHANNEL_RECORDS)
VERIFICATION_OUTCOME_RECORDS: Final[tuple[VerificationOutcome, ...]] = tuple(VerificationOutcome)
VERIFICATION_OUTCOME_COUNT: Final = len(VERIFICATION_OUTCOME_RECORDS)

RECORDS: Final[Mapping[str, tuple[_ReferenceEnum, ...]]] = MappingProxyType({
    'card_networks': CARD_NETWORK_RECORDS,
    'form_factors': FORM_FACTOR_RECORDS,
    'funding_types': FUNDING_TYPE_RECORDS,
    'payment_method_families': PAYMENT_METHOD_FAMILY_RECORDS,
    'payment_outcomes': PAYMENT_OUTCOME_RECORDS,
    'product_classes': PRODUCT_CLASS_RECORDS,
    'transaction_channels': TRANSACTION_CHANNEL_RECORDS,
    'verification_outcomes': VERIFICATION_OUTCOME_RECORDS,
})
COUNTS: Final[Mapping[str, int]] = MappingProxyType({
    'card_networks': CARD_NETWORK_COUNT,
    'form_factors': FORM_FACTOR_COUNT,
    'funding_types': FUNDING_TYPE_COUNT,
    'payment_method_families': PAYMENT_METHOD_FAMILY_COUNT,
    'payment_outcomes': PAYMENT_OUTCOME_COUNT,
    'product_classes': PRODUCT_CLASS_COUNT,
    'transaction_channels': TRANSACTION_CHANNEL_COUNT,
    'verification_outcomes': VERIFICATION_OUTCOME_COUNT,
})
