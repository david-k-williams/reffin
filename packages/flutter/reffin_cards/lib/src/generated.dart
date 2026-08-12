// Generated card reference vocabularies. Do not edit by hand.
// Input SHA-256: b4c71185e3980ee36870429da227c0e4b8b220a039679e0f6bf3bff18376db44

import 'package:flutter/material.dart';

// ignore: constant_identifier_names
const String DATA_FINGERPRINT = 'b4c71185e3980ee36870429da227c0e4b8b220a039679e0f6bf3bff18376db44';
const String dataFingerprint = DATA_FINGERPRINT;

enum CardNetwork {
  americanExpress('american_express', 'American Express', Icons.credit_card, 'american_express'),
  cartesBancaires('cartes_bancaires', 'Cartes Bancaires', Icons.credit_card, 'cartes_bancaires'),
  dinersClub('diners_club', 'Diners Club', Icons.credit_card, 'diners_club'),
  discover('discover', 'Discover', Icons.credit_card, 'discover'),
  eftposAustralia('eftpos_australia', 'eftpos Australia', Icons.credit_card, 'eftpos_australia'),
  elo('elo', 'Elo', Icons.credit_card, 'elo'),
  girocard('girocard', 'girocard', Icons.credit_card, 'girocard'),
  interac('interac', 'Interac', Icons.credit_card, 'interac'),
  jcb('jcb', 'JCB', Icons.credit_card, 'jcb'),
  maestro('maestro', 'Maestro', Icons.credit_card, 'maestro'),
  mastercard('mastercard', 'Mastercard', Icons.credit_card, 'mastercard'),
  other('other', 'Other', Icons.credit_card, null),
  rupay('rupay', 'RuPay', Icons.credit_card, 'rupay'),
  unionpay('unionpay', 'UnionPay', Icons.credit_card, 'unionpay'),
  unknown('unknown', 'Unknown', Icons.credit_card, null),
  visa('visa', 'Visa', Icons.credit_card, 'visa');

  const CardNetwork(this.id, this.label, this.icon, this.brandAssetKey);
  final String id;
  final String label;
  final IconData icon;
  final String? brandAssetKey;

  static CardNetwork? tryParse(String id) => _cardNetworkById[id];
}

const Map<String, CardNetwork> _cardNetworkById = {
  'american_express': CardNetwork.americanExpress,
  'cartes_bancaires': CardNetwork.cartesBancaires,
  'diners_club': CardNetwork.dinersClub,
  'discover': CardNetwork.discover,
  'eftpos_australia': CardNetwork.eftposAustralia,
  'elo': CardNetwork.elo,
  'girocard': CardNetwork.girocard,
  'interac': CardNetwork.interac,
  'jcb': CardNetwork.jcb,
  'maestro': CardNetwork.maestro,
  'mastercard': CardNetwork.mastercard,
  'other': CardNetwork.other,
  'rupay': CardNetwork.rupay,
  'unionpay': CardNetwork.unionpay,
  'unknown': CardNetwork.unknown,
  'visa': CardNetwork.visa,
};

enum FormFactor {
  other('other', 'Other', Icons.more_horiz, 'A known form factor outside the named normalized values'),
  physical('physical', 'Physical', Icons.credit_card, 'A card credential issued on a tangible card body'),
  unknown('unknown', 'Unknown', Icons.help_outline, 'The form factor was not supplied or could not be determined'),
  virtual('virtual', 'Virtual', Icons.devices, 'A card credential intended for use without a physical card body');

  const FormFactor(this.id, this.label, this.icon, this.description);
  final String id;
  final String label;
  final IconData icon;
  final String description;

  static FormFactor? tryParse(String id) => _formFactorById[id];
}

const Map<String, FormFactor> _formFactorById = {
  'other': FormFactor.other,
  'physical': FormFactor.physical,
  'unknown': FormFactor.unknown,
  'virtual': FormFactor.virtual,
};

enum FundingType {
  charge('charge', 'Charge', Icons.receipt_long, 'A balance that is normally due in full at the end of a billing period'),
  credit('credit', 'Credit', Icons.credit_score, 'Funds extended by an issuer and repaid under a credit agreement'),
  debit('debit', 'Debit', Icons.account_balance_wallet, 'Funds drawn from a linked deposit or transaction account'),
  other('other', 'Other', Icons.more_horiz, 'A known funding model outside the named normalized values'),
  prepaid('prepaid', 'Prepaid', Icons.redeem, 'Value funded before it is used for payment'),
  unknown('unknown', 'Unknown', Icons.help_outline, 'The funding model was not supplied or could not be determined');

  const FundingType(this.id, this.label, this.icon, this.description);
  final String id;
  final String label;
  final IconData icon;
  final String description;

  static FundingType? tryParse(String id) => _fundingTypeById[id];
}

const Map<String, FundingType> _fundingTypeById = {
  'charge': FundingType.charge,
  'credit': FundingType.credit,
  'debit': FundingType.debit,
  'other': FundingType.other,
  'prepaid': FundingType.prepaid,
  'unknown': FundingType.unknown,
};

enum PaymentMethodFamily {
  bankTransfer('bank_transfer', 'Bank Transfer', Icons.account_balance, 'A payer-initiated transfer between financial accounts'),
  buyNowPayLater('buy_now_pay_later', 'Buy Now Pay Later', Icons.calendar_month, 'A purchase paid through a deferred or installment arrangement'),
  card('card', 'Card', Icons.credit_card, 'A payment made with a card credential'),
  cash('cash', 'Cash', Icons.payments, 'A payment made with physical currency'),
  check('check', 'Check', Icons.receipt_long, 'A payment made with a paper or electronic check instrument'),
  cryptocurrency('cryptocurrency', 'Cryptocurrency', Icons.currency_exchange, 'A payment made by transferring a cryptographic asset'),
  digitalWallet('digital_wallet', 'Digital Wallet', Icons.account_balance_wallet, 'A payment initiated through a digital wallet interface'),
  directDebit('direct_debit', 'Direct Debit', Icons.sync_alt, 'A payee-initiated debit from a financial account under an authorization'),
  mobileMoney('mobile_money', 'Mobile Money', Icons.smartphone, 'A payment made through a mobile money account'),
  other('other', 'Other', Icons.more_horiz, 'A known payment method family outside the named normalized values'),
  unknown('unknown', 'Unknown', Icons.help_outline, 'The payment method family was not supplied or could not be determined'),
  voucher('voucher', 'Voucher', Icons.confirmation_number, 'A payment made with a voucher coupon or redeemable code');

  const PaymentMethodFamily(this.id, this.label, this.icon, this.description);
  final String id;
  final String label;
  final IconData icon;
  final String description;

  static PaymentMethodFamily? tryParse(String id) => _paymentMethodFamilyById[id];
}

const Map<String, PaymentMethodFamily> _paymentMethodFamilyById = {
  'bank_transfer': PaymentMethodFamily.bankTransfer,
  'buy_now_pay_later': PaymentMethodFamily.buyNowPayLater,
  'card': PaymentMethodFamily.card,
  'cash': PaymentMethodFamily.cash,
  'check': PaymentMethodFamily.check,
  'cryptocurrency': PaymentMethodFamily.cryptocurrency,
  'digital_wallet': PaymentMethodFamily.digitalWallet,
  'direct_debit': PaymentMethodFamily.directDebit,
  'mobile_money': PaymentMethodFamily.mobileMoney,
  'other': PaymentMethodFamily.other,
  'unknown': PaymentMethodFamily.unknown,
  'voucher': PaymentMethodFamily.voucher,
};

enum PaymentOutcome {
  approved('approved', 'Approved', Icons.check_circle, 'The payment or authorization was accepted for the requested amount'),
  canceled('canceled', 'Canceled', Icons.cancel, 'Processing was stopped before a final successful outcome'),
  declined('declined', 'Declined', Icons.block, 'The payment or authorization was actively refused'),
  failed('failed', 'Failed', Icons.error_outline, 'Processing did not complete because of an error rather than an explicit decline'),
  partiallyApproved('partially_approved', 'Partially Approved', Icons.rule, 'The payment or authorization was accepted for less than the requested amount'),
  pending('pending', 'Pending', Icons.schedule, 'A final processing outcome is not yet available'),
  reversed('reversed', 'Reversed', Icons.undo, 'A previous approval was undone or released before settlement'),
  unknown('unknown', 'Unknown', Icons.help_outline, 'The raw result was missing or had no known normalized outcome');

  const PaymentOutcome(this.id, this.label, this.icon, this.description);
  final String id;
  final String label;
  final IconData icon;
  final String description;

  static PaymentOutcome? tryParse(String id) => _paymentOutcomeById[id];
}

const Map<String, PaymentOutcome> _paymentOutcomeById = {
  'approved': PaymentOutcome.approved,
  'canceled': PaymentOutcome.canceled,
  'declined': PaymentOutcome.declined,
  'failed': PaymentOutcome.failed,
  'partially_approved': PaymentOutcome.partiallyApproved,
  'pending': PaymentOutcome.pending,
  'reversed': PaymentOutcome.reversed,
  'unknown': PaymentOutcome.unknown,
};

enum ProductClass {
  commercial('commercial', 'Commercial', Icons.business, 'A card product intended primarily for organizational or business spending'),
  consumer('consumer', 'Consumer', Icons.person, 'A card product intended primarily for an individual or household'),
  government('government', 'Government', Icons.account_balance, 'A card product intended primarily for a public-sector program'),
  other('other', 'Other', Icons.more_horiz, 'A known product class outside the named normalized values'),
  unknown('unknown', 'Unknown', Icons.help_outline, 'The product class was not supplied or could not be determined');

  const ProductClass(this.id, this.label, this.icon, this.description);
  final String id;
  final String label;
  final IconData icon;
  final String description;

  static ProductClass? tryParse(String id) => _productClassById[id];
}

const Map<String, ProductClass> _productClassById = {
  'commercial': ProductClass.commercial,
  'consumer': ProductClass.consumer,
  'government': ProductClass.government,
  'other': ProductClass.other,
  'unknown': ProductClass.unknown,
};

enum TransactionChannel {
  inApp('in_app', 'In App', Icons.apps, 'A transaction initiated inside a native or installed application'),
  inPerson('in_person', 'In Person', Icons.point_of_sale, 'A transaction initiated with the customer at a staffed or unattended physical location'),
  mailOrder('mail_order', 'Mail Order', Icons.mail, 'A remote transaction initiated through postal correspondence'),
  online('online', 'Online', Icons.language, 'A transaction initiated through a web or other online checkout outside a native application'),
  otherRemote('other_remote', 'Other Remote', Icons.devices_other, 'A known remote interaction surface outside the named normalized values'),
  telephoneOrder('telephone_order', 'Telephone Order', Icons.phone_in_talk, 'A remote transaction initiated through a voice telephone interaction'),
  unknown('unknown', 'Unknown', Icons.help_outline, 'The transaction channel was not supplied or could not be determined');

  const TransactionChannel(this.id, this.label, this.icon, this.description);
  final String id;
  final String label;
  final IconData icon;
  final String description;

  static TransactionChannel? tryParse(String id) => _transactionChannelById[id];
}

const Map<String, TransactionChannel> _transactionChannelById = {
  'in_app': TransactionChannel.inApp,
  'in_person': TransactionChannel.inPerson,
  'mail_order': TransactionChannel.mailOrder,
  'online': TransactionChannel.online,
  'other_remote': TransactionChannel.otherRemote,
  'telephone_order': TransactionChannel.telephoneOrder,
  'unknown': TransactionChannel.unknown,
};

enum VerificationOutcome {
  match('match', 'Match', Icons.verified, 'The submitted value matched the reference used by the verification service'),
  noMatch('no_match', 'No Match', Icons.cancel, 'The submitted value did not match the reference used by the verification service'),
  notApplicable('not_applicable', 'Not Applicable', Icons.remove_circle_outline, 'The verification check did not apply to this transaction or credential'),
  notProvided('not_provided', 'Not Provided', Icons.horizontal_rule, 'A value was not supplied for verification'),
  notSupported('not_supported', 'Not Supported', Icons.block, 'The verification service or source did not support the check'),
  notVerified('not_verified', 'Not Verified', Icons.help, 'A conclusive verification result was not produced'),
  partialMatch('partial_match', 'Partial Match', Icons.rule, 'Only part of the submitted value matched the reference used by the verification service'),
  skipped('skipped', 'Skipped', Icons.skip_next, 'The verification check was intentionally not attempted'),
  systemError('system_error', 'System Error', Icons.error_outline, 'The verification check could not complete because of a system or communication error'),
  unknown('unknown', 'Unknown', Icons.help_outline, 'The raw result was missing or had no known normalized outcome');

  const VerificationOutcome(this.id, this.label, this.icon, this.description);
  final String id;
  final String label;
  final IconData icon;
  final String description;

  static VerificationOutcome? tryParse(String id) => _verificationOutcomeById[id];
}

const Map<String, VerificationOutcome> _verificationOutcomeById = {
  'match': VerificationOutcome.match,
  'no_match': VerificationOutcome.noMatch,
  'not_applicable': VerificationOutcome.notApplicable,
  'not_provided': VerificationOutcome.notProvided,
  'not_supported': VerificationOutcome.notSupported,
  'not_verified': VerificationOutcome.notVerified,
  'partial_match': VerificationOutcome.partialMatch,
  'skipped': VerificationOutcome.skipped,
  'system_error': VerificationOutcome.systemError,
  'unknown': VerificationOutcome.unknown,
};

const List<CardNetwork> cardNetworkRecords = CardNetwork.values;
const int cardNetworkCount = 16;
const List<FormFactor> formFactorRecords = FormFactor.values;
const int formFactorCount = 4;
const List<FundingType> fundingTypeRecords = FundingType.values;
const int fundingTypeCount = 6;
const List<PaymentMethodFamily> paymentMethodFamilyRecords = PaymentMethodFamily.values;
const int paymentMethodFamilyCount = 12;
const List<PaymentOutcome> paymentOutcomeRecords = PaymentOutcome.values;
const int paymentOutcomeCount = 8;
const List<ProductClass> productClassRecords = ProductClass.values;
const int productClassCount = 5;
const List<TransactionChannel> transactionChannelRecords = TransactionChannel.values;
const int transactionChannelCount = 7;
const List<VerificationOutcome> verificationOutcomeRecords = VerificationOutcome.values;
const int verificationOutcomeCount = 10;

const Map<String, List<Enum>> records = {
  'card_networks': cardNetworkRecords,
  'form_factors': formFactorRecords,
  'funding_types': fundingTypeRecords,
  'payment_method_families': paymentMethodFamilyRecords,
  'payment_outcomes': paymentOutcomeRecords,
  'product_classes': productClassRecords,
  'transaction_channels': transactionChannelRecords,
  'verification_outcomes': verificationOutcomeRecords,
};

const Map<String, int> counts = {
  'card_networks': cardNetworkCount,
  'form_factors': formFactorCount,
  'funding_types': fundingTypeCount,
  'payment_method_families': paymentMethodFamilyCount,
  'payment_outcomes': paymentOutcomeCount,
  'product_classes': productClassCount,
  'transaction_channels': transactionChannelCount,
  'verification_outcomes': verificationOutcomeCount,
};

// ignore: constant_identifier_names
const Map<String, List<Enum>> RECORDS = records;
// ignore: constant_identifier_names
const Map<String, int> COUNTS = counts;
