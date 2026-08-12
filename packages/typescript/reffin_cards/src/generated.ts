// Generated card reference vocabularies. Do not edit by hand.
// Input SHA-256: b4c71185e3980ee36870429da227c0e4b8b220a039679e0f6bf3bff18376db44

export const DATA_FINGERPRINT = "b4c71185e3980ee36870429da227c0e4b8b220a039679e0f6bf3bff18376db44" as const;

export interface ReferenceValue {
  readonly id: string;
  readonly name: string;
  readonly materialSymbol: string;
}

export interface DescribedReferenceValue extends ReferenceValue {
  readonly description: string;
}

export interface CardNetworkValue extends ReferenceValue {
  readonly brandAssetKey: string | null;
}

function reference<const T extends DescribedReferenceValue>(item: T): Readonly<T> {
  return Object.freeze(item);
}

function network<const T extends CardNetworkValue>(item: T): Readonly<T> {
  return Object.freeze(item);
}

function indexById<T extends ReferenceValue>(values: readonly T[]): ReadonlyMap<string, T> {
  return new Map(values.map((item) => [item.id, item]));
}

export const CardNetwork = Object.freeze({
  AmericanExpress: network({ id: "american_express", name: "American Express", materialSymbol: "credit_card", brandAssetKey: "american_express" }),
  CartesBancaires: network({ id: "cartes_bancaires", name: "Cartes Bancaires", materialSymbol: "credit_card", brandAssetKey: "cartes_bancaires" }),
  DinersClub: network({ id: "diners_club", name: "Diners Club", materialSymbol: "credit_card", brandAssetKey: "diners_club" }),
  Discover: network({ id: "discover", name: "Discover", materialSymbol: "credit_card", brandAssetKey: "discover" }),
  EftposAustralia: network({ id: "eftpos_australia", name: "eftpos Australia", materialSymbol: "credit_card", brandAssetKey: "eftpos_australia" }),
  Elo: network({ id: "elo", name: "Elo", materialSymbol: "credit_card", brandAssetKey: "elo" }),
  Girocard: network({ id: "girocard", name: "girocard", materialSymbol: "credit_card", brandAssetKey: "girocard" }),
  Interac: network({ id: "interac", name: "Interac", materialSymbol: "credit_card", brandAssetKey: "interac" }),
  Jcb: network({ id: "jcb", name: "JCB", materialSymbol: "credit_card", brandAssetKey: "jcb" }),
  Maestro: network({ id: "maestro", name: "Maestro", materialSymbol: "credit_card", brandAssetKey: "maestro" }),
  Mastercard: network({ id: "mastercard", name: "Mastercard", materialSymbol: "credit_card", brandAssetKey: "mastercard" }),
  Other: network({ id: "other", name: "Other", materialSymbol: "credit_card", brandAssetKey: null }),
  Rupay: network({ id: "rupay", name: "RuPay", materialSymbol: "credit_card", brandAssetKey: "rupay" }),
  Unionpay: network({ id: "unionpay", name: "UnionPay", materialSymbol: "credit_card", brandAssetKey: "unionpay" }),
  Unknown: network({ id: "unknown", name: "Unknown", materialSymbol: "credit_card", brandAssetKey: null }),
  Visa: network({ id: "visa", name: "Visa", materialSymbol: "credit_card", brandAssetKey: "visa" }),
});
export type CardNetwork =
  (typeof CardNetwork)[keyof typeof CardNetwork];
export type CardNetworkId = CardNetwork["id"];

export const FormFactor = Object.freeze({
  Other: reference({ id: "other", name: "Other", materialSymbol: "more_horiz", description: "A known form factor outside the named normalized values" }),
  Physical: reference({ id: "physical", name: "Physical", materialSymbol: "credit_card", description: "A card credential issued on a tangible card body" }),
  Unknown: reference({ id: "unknown", name: "Unknown", materialSymbol: "help_outline", description: "The form factor was not supplied or could not be determined" }),
  Virtual: reference({ id: "virtual", name: "Virtual", materialSymbol: "devices", description: "A card credential intended for use without a physical card body" }),
});
export type FormFactor =
  (typeof FormFactor)[keyof typeof FormFactor];
export type FormFactorId = FormFactor["id"];

export const FundingType = Object.freeze({
  Charge: reference({ id: "charge", name: "Charge", materialSymbol: "receipt_long", description: "A balance that is normally due in full at the end of a billing period" }),
  Credit: reference({ id: "credit", name: "Credit", materialSymbol: "credit_score", description: "Funds extended by an issuer and repaid under a credit agreement" }),
  Debit: reference({ id: "debit", name: "Debit", materialSymbol: "account_balance_wallet", description: "Funds drawn from a linked deposit or transaction account" }),
  Other: reference({ id: "other", name: "Other", materialSymbol: "more_horiz", description: "A known funding model outside the named normalized values" }),
  Prepaid: reference({ id: "prepaid", name: "Prepaid", materialSymbol: "redeem", description: "Value funded before it is used for payment" }),
  Unknown: reference({ id: "unknown", name: "Unknown", materialSymbol: "help_outline", description: "The funding model was not supplied or could not be determined" }),
});
export type FundingType =
  (typeof FundingType)[keyof typeof FundingType];
export type FundingTypeId = FundingType["id"];

export const PaymentMethodFamily = Object.freeze({
  BankTransfer: reference({ id: "bank_transfer", name: "Bank Transfer", materialSymbol: "account_balance", description: "A payer-initiated transfer between financial accounts" }),
  BuyNowPayLater: reference({ id: "buy_now_pay_later", name: "Buy Now Pay Later", materialSymbol: "calendar_month", description: "A purchase paid through a deferred or installment arrangement" }),
  Card: reference({ id: "card", name: "Card", materialSymbol: "credit_card", description: "A payment made with a card credential" }),
  Cash: reference({ id: "cash", name: "Cash", materialSymbol: "payments", description: "A payment made with physical currency" }),
  Check: reference({ id: "check", name: "Check", materialSymbol: "receipt_long", description: "A payment made with a paper or electronic check instrument" }),
  Cryptocurrency: reference({ id: "cryptocurrency", name: "Cryptocurrency", materialSymbol: "currency_exchange", description: "A payment made by transferring a cryptographic asset" }),
  DigitalWallet: reference({ id: "digital_wallet", name: "Digital Wallet", materialSymbol: "account_balance_wallet", description: "A payment initiated through a digital wallet interface" }),
  DirectDebit: reference({ id: "direct_debit", name: "Direct Debit", materialSymbol: "sync_alt", description: "A payee-initiated debit from a financial account under an authorization" }),
  MobileMoney: reference({ id: "mobile_money", name: "Mobile Money", materialSymbol: "smartphone", description: "A payment made through a mobile money account" }),
  Other: reference({ id: "other", name: "Other", materialSymbol: "more_horiz", description: "A known payment method family outside the named normalized values" }),
  Unknown: reference({ id: "unknown", name: "Unknown", materialSymbol: "help_outline", description: "The payment method family was not supplied or could not be determined" }),
  Voucher: reference({ id: "voucher", name: "Voucher", materialSymbol: "confirmation_number", description: "A payment made with a voucher coupon or redeemable code" }),
});
export type PaymentMethodFamily =
  (typeof PaymentMethodFamily)[keyof typeof PaymentMethodFamily];
export type PaymentMethodFamilyId = PaymentMethodFamily["id"];

export const PaymentOutcome = Object.freeze({
  Approved: reference({ id: "approved", name: "Approved", materialSymbol: "check_circle", description: "The payment or authorization was accepted for the requested amount" }),
  Canceled: reference({ id: "canceled", name: "Canceled", materialSymbol: "cancel", description: "Processing was stopped before a final successful outcome" }),
  Declined: reference({ id: "declined", name: "Declined", materialSymbol: "block", description: "The payment or authorization was actively refused" }),
  Failed: reference({ id: "failed", name: "Failed", materialSymbol: "error_outline", description: "Processing did not complete because of an error rather than an explicit decline" }),
  PartiallyApproved: reference({ id: "partially_approved", name: "Partially Approved", materialSymbol: "rule", description: "The payment or authorization was accepted for less than the requested amount" }),
  Pending: reference({ id: "pending", name: "Pending", materialSymbol: "schedule", description: "A final processing outcome is not yet available" }),
  Reversed: reference({ id: "reversed", name: "Reversed", materialSymbol: "undo", description: "A previous approval was undone or released before settlement" }),
  Unknown: reference({ id: "unknown", name: "Unknown", materialSymbol: "help_outline", description: "The raw result was missing or had no known normalized outcome" }),
});
export type PaymentOutcome =
  (typeof PaymentOutcome)[keyof typeof PaymentOutcome];
export type PaymentOutcomeId = PaymentOutcome["id"];

export const ProductClass = Object.freeze({
  Commercial: reference({ id: "commercial", name: "Commercial", materialSymbol: "business", description: "A card product intended primarily for organizational or business spending" }),
  Consumer: reference({ id: "consumer", name: "Consumer", materialSymbol: "person", description: "A card product intended primarily for an individual or household" }),
  Government: reference({ id: "government", name: "Government", materialSymbol: "account_balance", description: "A card product intended primarily for a public-sector program" }),
  Other: reference({ id: "other", name: "Other", materialSymbol: "more_horiz", description: "A known product class outside the named normalized values" }),
  Unknown: reference({ id: "unknown", name: "Unknown", materialSymbol: "help_outline", description: "The product class was not supplied or could not be determined" }),
});
export type ProductClass =
  (typeof ProductClass)[keyof typeof ProductClass];
export type ProductClassId = ProductClass["id"];

export const TransactionChannel = Object.freeze({
  InApp: reference({ id: "in_app", name: "In App", materialSymbol: "apps", description: "A transaction initiated inside a native or installed application" }),
  InPerson: reference({ id: "in_person", name: "In Person", materialSymbol: "point_of_sale", description: "A transaction initiated with the customer at a staffed or unattended physical location" }),
  MailOrder: reference({ id: "mail_order", name: "Mail Order", materialSymbol: "mail", description: "A remote transaction initiated through postal correspondence" }),
  Online: reference({ id: "online", name: "Online", materialSymbol: "language", description: "A transaction initiated through a web or other online checkout outside a native application" }),
  OtherRemote: reference({ id: "other_remote", name: "Other Remote", materialSymbol: "devices_other", description: "A known remote interaction surface outside the named normalized values" }),
  TelephoneOrder: reference({ id: "telephone_order", name: "Telephone Order", materialSymbol: "phone_in_talk", description: "A remote transaction initiated through a voice telephone interaction" }),
  Unknown: reference({ id: "unknown", name: "Unknown", materialSymbol: "help_outline", description: "The transaction channel was not supplied or could not be determined" }),
});
export type TransactionChannel =
  (typeof TransactionChannel)[keyof typeof TransactionChannel];
export type TransactionChannelId = TransactionChannel["id"];

export const VerificationOutcome = Object.freeze({
  Match: reference({ id: "match", name: "Match", materialSymbol: "verified", description: "The submitted value matched the reference used by the verification service" }),
  NoMatch: reference({ id: "no_match", name: "No Match", materialSymbol: "cancel", description: "The submitted value did not match the reference used by the verification service" }),
  NotApplicable: reference({ id: "not_applicable", name: "Not Applicable", materialSymbol: "remove_circle_outline", description: "The verification check did not apply to this transaction or credential" }),
  NotProvided: reference({ id: "not_provided", name: "Not Provided", materialSymbol: "horizontal_rule", description: "A value was not supplied for verification" }),
  NotSupported: reference({ id: "not_supported", name: "Not Supported", materialSymbol: "block", description: "The verification service or source did not support the check" }),
  NotVerified: reference({ id: "not_verified", name: "Not Verified", materialSymbol: "help", description: "A conclusive verification result was not produced" }),
  PartialMatch: reference({ id: "partial_match", name: "Partial Match", materialSymbol: "rule", description: "Only part of the submitted value matched the reference used by the verification service" }),
  Skipped: reference({ id: "skipped", name: "Skipped", materialSymbol: "skip_next", description: "The verification check was intentionally not attempted" }),
  SystemError: reference({ id: "system_error", name: "System Error", materialSymbol: "error_outline", description: "The verification check could not complete because of a system or communication error" }),
  Unknown: reference({ id: "unknown", name: "Unknown", materialSymbol: "help_outline", description: "The raw result was missing or had no known normalized outcome" }),
});
export type VerificationOutcome =
  (typeof VerificationOutcome)[keyof typeof VerificationOutcome];
export type VerificationOutcomeId = VerificationOutcome["id"];

export const cardNetworkRecords: readonly CardNetwork[] = Object.freeze(Object.values(CardNetwork));
export const cardNetworkCount = cardNetworkRecords.length;
const cardNetworkById = indexById(cardNetworkRecords);
export function tryParseCardNetwork(id: string): CardNetwork | undefined {
  return cardNetworkById.get(id);
}
export function isCardNetworkId(id: string): id is CardNetworkId {
  return cardNetworkById.has(id);
}

export const formFactorRecords: readonly FormFactor[] = Object.freeze(Object.values(FormFactor));
export const formFactorCount = formFactorRecords.length;
const formFactorById = indexById(formFactorRecords);
export function tryParseFormFactor(id: string): FormFactor | undefined {
  return formFactorById.get(id);
}
export function isFormFactorId(id: string): id is FormFactorId {
  return formFactorById.has(id);
}

export const fundingTypeRecords: readonly FundingType[] = Object.freeze(Object.values(FundingType));
export const fundingTypeCount = fundingTypeRecords.length;
const fundingTypeById = indexById(fundingTypeRecords);
export function tryParseFundingType(id: string): FundingType | undefined {
  return fundingTypeById.get(id);
}
export function isFundingTypeId(id: string): id is FundingTypeId {
  return fundingTypeById.has(id);
}

export const paymentMethodFamilyRecords: readonly PaymentMethodFamily[] = Object.freeze(Object.values(PaymentMethodFamily));
export const paymentMethodFamilyCount = paymentMethodFamilyRecords.length;
const paymentMethodFamilyById = indexById(paymentMethodFamilyRecords);
export function tryParsePaymentMethodFamily(id: string): PaymentMethodFamily | undefined {
  return paymentMethodFamilyById.get(id);
}
export function isPaymentMethodFamilyId(id: string): id is PaymentMethodFamilyId {
  return paymentMethodFamilyById.has(id);
}

export const paymentOutcomeRecords: readonly PaymentOutcome[] = Object.freeze(Object.values(PaymentOutcome));
export const paymentOutcomeCount = paymentOutcomeRecords.length;
const paymentOutcomeById = indexById(paymentOutcomeRecords);
export function tryParsePaymentOutcome(id: string): PaymentOutcome | undefined {
  return paymentOutcomeById.get(id);
}
export function isPaymentOutcomeId(id: string): id is PaymentOutcomeId {
  return paymentOutcomeById.has(id);
}

export const productClassRecords: readonly ProductClass[] = Object.freeze(Object.values(ProductClass));
export const productClassCount = productClassRecords.length;
const productClassById = indexById(productClassRecords);
export function tryParseProductClass(id: string): ProductClass | undefined {
  return productClassById.get(id);
}
export function isProductClassId(id: string): id is ProductClassId {
  return productClassById.has(id);
}

export const transactionChannelRecords: readonly TransactionChannel[] = Object.freeze(Object.values(TransactionChannel));
export const transactionChannelCount = transactionChannelRecords.length;
const transactionChannelById = indexById(transactionChannelRecords);
export function tryParseTransactionChannel(id: string): TransactionChannel | undefined {
  return transactionChannelById.get(id);
}
export function isTransactionChannelId(id: string): id is TransactionChannelId {
  return transactionChannelById.has(id);
}

export const verificationOutcomeRecords: readonly VerificationOutcome[] = Object.freeze(Object.values(VerificationOutcome));
export const verificationOutcomeCount = verificationOutcomeRecords.length;
const verificationOutcomeById = indexById(verificationOutcomeRecords);
export function tryParseVerificationOutcome(id: string): VerificationOutcome | undefined {
  return verificationOutcomeById.get(id);
}
export function isVerificationOutcomeId(id: string): id is VerificationOutcomeId {
  return verificationOutcomeById.has(id);
}

export const records = Object.freeze({
  cardNetworks: cardNetworkRecords,
  formFactors: formFactorRecords,
  fundingTypes: fundingTypeRecords,
  paymentMethodFamilies: paymentMethodFamilyRecords,
  paymentOutcomes: paymentOutcomeRecords,
  productClasses: productClassRecords,
  transactionChannels: transactionChannelRecords,
  verificationOutcomes: verificationOutcomeRecords,
});

export const counts = Object.freeze({
  cardNetworks: cardNetworkCount,
  formFactors: formFactorCount,
  fundingTypes: fundingTypeCount,
  paymentMethodFamilies: paymentMethodFamilyCount,
  paymentOutcomes: paymentOutcomeCount,
  productClasses: productClassCount,
  transactionChannels: transactionChannelCount,
  verificationOutcomes: verificationOutcomeCount,
});

export const RECORDS = records;
export const COUNTS = counts;
