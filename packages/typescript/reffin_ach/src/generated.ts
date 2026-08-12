// Generated ACH reference catalogs. Do not edit by hand.
// Input SHA-256: 252f6495924ee9a8b82ec6088df0325739cb5e902bcf3e3bdc1f86429995de6e

export const DATA_FINGERPRINT = "252f6495924ee9a8b82ec6088df0325739cb5e902bcf3e3bdc1f86429995de6e" as const;
export const REFERENCE_AS_OF = "2026-08-11" as const;
export type AchCodeStatus = 'current' | 'planned' | 'legacy';

export interface AchReferenceInfo {
  readonly code: string;
  readonly name: string;
  readonly status: AchCodeStatus;
  readonly validFrom: string | null;
  readonly validTo: string | null;
  readonly sources: readonly string[];
  readonly materialSymbol: string;
}

export interface AchTransactionCodeInfo extends AchReferenceInfo {
  readonly accountType: string;
  readonly direction: string;
  readonly entryKind: string;
  readonly returnForCodes: readonly string[];
}

export interface AchReturnCodeInfo extends AchReferenceInfo {
  readonly category: string;
}

export interface AchStandardEntryClassCodeInfo extends AchReferenceInfo {
  readonly entryKind: string;
  readonly consumerOrCorporate: string;
  readonly direction: string;
  readonly addendaSupport: string;
}

export interface AchServiceClassCodeInfo extends AchReferenceInfo {
  readonly direction: string;
}

export interface AchRecordTypeCodeInfo extends AchReferenceInfo {
}

export interface AchChangeCodeInfo extends AchReferenceInfo {
  readonly correctedFields: readonly string[];
  readonly appliesTo: readonly string[];
}

export interface AchAddendaTypeCodeInfo extends AchReferenceInfo {
  readonly appliesTo: readonly string[];
}

function freezeInfo<T extends AchReferenceInfo>(value: T): Readonly<T> {
  return Object.freeze(value);
}

function normalizeDate(value: Date | string): string | undefined {
  if (typeof value === 'string') {
    const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(value);
    if (match === null) return undefined;
    const year = Number(match[1]!);
    const month = Number(match[2]!);
    const day = Number(match[3]!);
    const check = new Date(Date.UTC(year, month - 1, day));
    if (check.getUTCFullYear() !== year || check.getUTCMonth() !== month - 1 || check.getUTCDate() !== day) return undefined;
    return value;
  }
  if (Number.isNaN(value.getTime())) return undefined;
  const year = String(value.getFullYear()).padStart(4, '0');
  const month = String(value.getMonth() + 1).padStart(2, '0');
  const day = String(value.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

export function isEffective(info: AchReferenceInfo, on: Date | string = REFERENCE_AS_OF): boolean {
  if (info.status === 'legacy') return false;
  const key = normalizeDate(on);
  if (key === undefined) return false;
  if (info.validFrom !== null && key < info.validFrom) return false;
  return info.validTo === null || key <= info.validTo;
}

function indexRecords<T extends AchReferenceInfo>(records: readonly T[]): ReadonlyMap<string, readonly T[]> {
  const mutable = new Map<string, T[]>();
  for (const record of records) {
    const values = mutable.get(record.code) ?? [];
    values.push(record);
    mutable.set(record.code, values);
  }
  return new Map([...mutable].map(([code, values]) => [code, Object.freeze(values)]));
}

function codeOf(value: string | AchReferenceInfo): string {
  return (typeof value === 'string' ? value : value.code).trim().toUpperCase();
}

function resolveAt<T extends AchReferenceInfo>(
  index: ReadonlyMap<string, readonly T[]>,
  value: string | AchReferenceInfo,
  on: Date | string,
  includeInactive: boolean,
): T | undefined {
  const records = index.get(codeOf(value));
  if (!records) return undefined;
  return records.find((record) => isEffective(record, on)) ?? (includeInactive ? records[0] : undefined);
}

export const transactionCodeRecords: readonly AchTransactionCodeInfo[] = Object.freeze([
  freezeInfo({ code: "21", name: "Return or NOC for Checking Credit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "checking", direction: "return_or_noc", entryKind: "return_or_noc", returnForCodes: Object.freeze(["22", "23", "24"]) }),
  freezeInfo({ code: "22", name: "Checking Credit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "payments", accountType: "checking", direction: "credit", entryKind: "monetary", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "23", name: "Checking Credit Prenote DNE or ENR", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "payments", accountType: "checking", direction: "credit", entryKind: "prenotification_or_notice", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "24", name: "Checking Zero-Dollar Credit or Acknowledgment", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "checking", direction: "credit", entryKind: "zero_dollar_or_acknowledgment", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "26", name: "Return or NOC for Checking Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "checking", direction: "return_or_noc", entryKind: "return_or_noc", returnForCodes: Object.freeze(["27", "28", "29"]) }),
  freezeInfo({ code: "27", name: "Checking Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "payments", accountType: "checking", direction: "debit", entryKind: "monetary", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "28", name: "Checking Debit Prenotification", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "payments", accountType: "checking", direction: "debit", entryKind: "prenotification", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "29", name: "Checking Zero-Dollar Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "checking", direction: "debit", entryKind: "zero_dollar", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "31", name: "Return or NOC for Savings Credit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "savings", direction: "return_or_noc", entryKind: "return_or_noc", returnForCodes: Object.freeze(["32", "33", "34"]) }),
  freezeInfo({ code: "32", name: "Savings Credit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "payments", accountType: "savings", direction: "credit", entryKind: "monetary", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "33", name: "Savings Credit Prenote DNE or ENR", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "payments", accountType: "savings", direction: "credit", entryKind: "prenotification_or_notice", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "34", name: "Savings Zero-Dollar Credit or Acknowledgment", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "savings", direction: "credit", entryKind: "zero_dollar_or_acknowledgment", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "36", name: "Return or NOC for Savings Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "savings", direction: "return_or_noc", entryKind: "return_or_noc", returnForCodes: Object.freeze(["37", "38", "39"]) }),
  freezeInfo({ code: "37", name: "Savings Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "payments", accountType: "savings", direction: "debit", entryKind: "monetary", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "38", name: "Savings Debit Prenotification", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "payments", accountType: "savings", direction: "debit", entryKind: "prenotification", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "39", name: "Savings Zero-Dollar Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "savings", direction: "debit", entryKind: "zero_dollar", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "41", name: "Return or NOC for General Ledger Credit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "general_ledger", direction: "return_or_noc", entryKind: "return_or_noc", returnForCodes: Object.freeze(["42", "43", "44"]) }),
  freezeInfo({ code: "42", name: "General Ledger Credit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "general_ledger", direction: "credit", entryKind: "monetary", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "43", name: "General Ledger Credit Prenotification", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "general_ledger", direction: "credit", entryKind: "prenotification", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "44", name: "General Ledger Zero-Dollar Credit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "general_ledger", direction: "credit", entryKind: "zero_dollar", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "46", name: "Return or NOC for General Ledger Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "general_ledger", direction: "return_or_noc", entryKind: "return_or_noc", returnForCodes: Object.freeze(["47", "48", "49"]) }),
  freezeInfo({ code: "47", name: "General Ledger Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "general_ledger", direction: "debit", entryKind: "monetary", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "48", name: "General Ledger Debit Prenotification", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "general_ledger", direction: "debit", entryKind: "prenotification", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "49", name: "General Ledger Zero-Dollar Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "general_ledger", direction: "debit", entryKind: "zero_dollar", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "51", name: "Return or NOC for Loan Credit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "loan", direction: "return_or_noc", entryKind: "return_or_noc", returnForCodes: Object.freeze(["52", "53", "54"]) }),
  freezeInfo({ code: "52", name: "Loan Credit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "loan", direction: "credit", entryKind: "monetary", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "53", name: "Loan Credit Prenotification", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "loan", direction: "credit", entryKind: "prenotification", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "54", name: "Loan Zero-Dollar Credit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "loan", direction: "credit", entryKind: "zero_dollar", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "55", name: "Loan Debit for Reversal", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "loan", direction: "debit", entryKind: "reversal", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "56", name: "Return or NOC for Loan Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "loan", direction: "return_or_noc", entryKind: "return_or_noc", returnForCodes: Object.freeze(["55"]) }),
  freezeInfo({ code: "81", name: "ADV Credit for Originated Debits", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "accounting", direction: "credit", entryKind: "accounting", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "82", name: "ADV Debit for Originated Credits", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "accounting", direction: "debit", entryKind: "accounting", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "83", name: "ADV Credit for Received Credits", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "accounting", direction: "credit", entryKind: "accounting", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "84", name: "ADV Debit for Received Debits", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "accounting", direction: "debit", entryKind: "accounting", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "85", name: "ADV Credit for Credits in Rejected Batches", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "accounting", direction: "credit", entryKind: "accounting", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "86", name: "ADV Debit for Debits in Rejected Batches", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "accounting", direction: "debit", entryKind: "accounting", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "87", name: "ADV Summary Credit for Respondent Activity", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "accounting", direction: "credit", entryKind: "accounting", returnForCodes: Object.freeze([]) }),
  freezeInfo({ code: "88", name: "ADV Summary Debit for Respondent Activity", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "payments", accountType: "accounting", direction: "debit", entryKind: "accounting", returnForCodes: Object.freeze([]) }),
]);
const _transactionCodeByCode = indexRecords(transactionCodeRecords);
export function resolveTransactionCode(
  code: string | AchTransactionCodeInfo, options: { readonly includeInactive?: boolean } = {},
): AchTransactionCodeInfo | undefined {
  return resolveAt(_transactionCodeByCode, code, REFERENCE_AS_OF, options.includeInactive ?? false);
}
export function resolveTransactionCodeAsOf(
  code: string | AchTransactionCodeInfo, on: Date | string,
  options: { readonly includeInactive?: boolean } = {},
): AchTransactionCodeInfo | undefined {
  return resolveAt(_transactionCodeByCode, code, on, options.includeInactive ?? false);
}
export const AchTransactionCode = Object.freeze({
  Code21: resolveTransactionCode("21", { includeInactive: true })!,
  Code22: resolveTransactionCode("22", { includeInactive: true })!,
  Code23: resolveTransactionCode("23", { includeInactive: true })!,
  Code24: resolveTransactionCode("24", { includeInactive: true })!,
  Code26: resolveTransactionCode("26", { includeInactive: true })!,
  Code27: resolveTransactionCode("27", { includeInactive: true })!,
  Code28: resolveTransactionCode("28", { includeInactive: true })!,
  Code29: resolveTransactionCode("29", { includeInactive: true })!,
  Code31: resolveTransactionCode("31", { includeInactive: true })!,
  Code32: resolveTransactionCode("32", { includeInactive: true })!,
  Code33: resolveTransactionCode("33", { includeInactive: true })!,
  Code34: resolveTransactionCode("34", { includeInactive: true })!,
  Code36: resolveTransactionCode("36", { includeInactive: true })!,
  Code37: resolveTransactionCode("37", { includeInactive: true })!,
  Code38: resolveTransactionCode("38", { includeInactive: true })!,
  Code39: resolveTransactionCode("39", { includeInactive: true })!,
  Code41: resolveTransactionCode("41", { includeInactive: true })!,
  Code42: resolveTransactionCode("42", { includeInactive: true })!,
  Code43: resolveTransactionCode("43", { includeInactive: true })!,
  Code44: resolveTransactionCode("44", { includeInactive: true })!,
  Code46: resolveTransactionCode("46", { includeInactive: true })!,
  Code47: resolveTransactionCode("47", { includeInactive: true })!,
  Code48: resolveTransactionCode("48", { includeInactive: true })!,
  Code49: resolveTransactionCode("49", { includeInactive: true })!,
  Code51: resolveTransactionCode("51", { includeInactive: true })!,
  Code52: resolveTransactionCode("52", { includeInactive: true })!,
  Code53: resolveTransactionCode("53", { includeInactive: true })!,
  Code54: resolveTransactionCode("54", { includeInactive: true })!,
  Code55: resolveTransactionCode("55", { includeInactive: true })!,
  Code56: resolveTransactionCode("56", { includeInactive: true })!,
  Code81: resolveTransactionCode("81", { includeInactive: true })!,
  Code82: resolveTransactionCode("82", { includeInactive: true })!,
  Code83: resolveTransactionCode("83", { includeInactive: true })!,
  Code84: resolveTransactionCode("84", { includeInactive: true })!,
  Code85: resolveTransactionCode("85", { includeInactive: true })!,
  Code86: resolveTransactionCode("86", { includeInactive: true })!,
  Code87: resolveTransactionCode("87", { includeInactive: true })!,
  Code88: resolveTransactionCode("88", { includeInactive: true })!,
});
export type AchTransactionCode = (typeof AchTransactionCode)[keyof typeof AchTransactionCode];
export const currentTransactionCodeRecords = Object.freeze(
  transactionCodeRecords.filter((record) => isEffective(record)),
);
export const transactionCodeCount = _transactionCodeByCode.size;
export const transactionCodeRecordCount = transactionCodeRecords.length;
export const currentTransactionCodeCount = currentTransactionCodeRecords.length;

export const returnCodeRecords: readonly AchReturnCodeInfo[] = Object.freeze([
  freezeInfo({ code: "R01", name: "Insufficient Funds", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "funds" }),
  freezeInfo({ code: "R02", name: "Account Closed", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "account" }),
  freezeInfo({ code: "R03", name: "No Account or Unable to Locate Account", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "account" }),
  freezeInfo({ code: "R04", name: "Invalid Account Number Structure", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "account" }),
  freezeInfo({ code: "R05", name: "Unauthorized Corporate-Code Debit to Consumer Account", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "authorization" }),
  freezeInfo({ code: "R06", name: "Returned at ODFI Request", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "request" }),
  freezeInfo({ code: "R07", name: "Authorization Revoked by Customer", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "authorization" }),
  freezeInfo({ code: "R08", name: "Payment Stopped", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "authorization" }),
  freezeInfo({ code: "R09", name: "Uncollected Funds", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "funds" }),
  freezeInfo({ code: "R10", name: "Originator Unknown or Not Authorized to Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "authorization" }),
  freezeInfo({ code: "R11", name: "Entry Not in Accordance with Authorization", status: "current", validFrom: "2020-04-01", validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023", "nacha_r11_2020"]), materialSymbol: "undo", category: "authorization" }),
  freezeInfo({ code: "R12", name: "Account Sold to Another DFI", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "account" }),
  freezeInfo({ code: "R13", name: "Invalid ACH Routing Number", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "administrative" }),
  freezeInfo({ code: "R14", name: "Representative Payee Deceased or Unable to Continue", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "death_or_legal" }),
  freezeInfo({ code: "R15", name: "Beneficiary or Account Holder Deceased", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "death_or_legal" }),
  freezeInfo({ code: "R16", name: "Account Frozen or Return per OFAC Instruction", status: "current", validFrom: null, validTo: "2028-03-16", sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023", "nacha_rule_r90"]), materialSymbol: "undo", category: "legal_or_compliance" }),
  freezeInfo({ code: "R16", name: "Account Frozen", status: "planned", validFrom: "2028-03-17", validTo: null, sources: Object.freeze(["nacha_rule_r90"]), materialSymbol: "undo", category: "legal_or_compliance" }),
  freezeInfo({ code: "R17", name: "File Edit Error Questionable Entry or Improper Reversal", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_minor_topics_2026", "nacha_questionable_2019", "nacha_reversals_2021"]), materialSymbol: "undo", category: "administrative" }),
  freezeInfo({ code: "R18", name: "Improper Effective Entry Date", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "administrative" }),
  freezeInfo({ code: "R19", name: "Amount Field Error", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "format" }),
  freezeInfo({ code: "R20", name: "Non-Transaction Account", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "account" }),
  freezeInfo({ code: "R21", name: "Invalid Company Identification", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "administrative" }),
  freezeInfo({ code: "R22", name: "Invalid Individual ID Number", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023", "fedglobal_manual_2026"]), materialSymbol: "undo", category: "administrative" }),
  freezeInfo({ code: "R23", name: "Credit Entry Refused by Receiver", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "receiver_refusal" }),
  freezeInfo({ code: "R24", name: "Duplicate Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "administrative" }),
  freezeInfo({ code: "R25", name: "Addenda Error", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "format" }),
  freezeInfo({ code: "R26", name: "Mandatory Field Error", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "format" }),
  freezeInfo({ code: "R27", name: "Trace Number Error", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "format" }),
  freezeInfo({ code: "R28", name: "Routing Number Check Digit Error", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "format" }),
  freezeInfo({ code: "R29", name: "Corporate Customer Advises Not Authorized", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "authorization" }),
  freezeInfo({ code: "R30", name: "RDFI Not in Check Truncation Program", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "participation" }),
  freezeInfo({ code: "R31", name: "Permissible CCD or CTX Return", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "request" }),
  freezeInfo({ code: "R32", name: "RDFI Non-Settlement", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "settlement" }),
  freezeInfo({ code: "R33", name: "Return of XCK Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "check_entry" }),
  freezeInfo({ code: "R34", name: "Limited Participation DFI", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "participation" }),
  freezeInfo({ code: "R35", name: "Improper Debit Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "improper_entry" }),
  freezeInfo({ code: "R36", name: "Improper Credit Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "improper_entry" }),
  freezeInfo({ code: "R37", name: "Source Document Presented for Payment", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "source_document" }),
  freezeInfo({ code: "R38", name: "Stop Payment on Source Document", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "source_document" }),
  freezeInfo({ code: "R39", name: "Improper Source Document or Duplicate Presentment", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "source_document" }),
  freezeInfo({ code: "R40", name: "Federal Agency Return of ENR Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "enrollment" }),
  freezeInfo({ code: "R41", name: "Invalid Transaction Code for ENR", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "enrollment" }),
  freezeInfo({ code: "R42", name: "Routing Number or Check Digit Error for ENR", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "enrollment" }),
  freezeInfo({ code: "R43", name: "Invalid DFI Account Number for ENR", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "enrollment" }),
  freezeInfo({ code: "R44", name: "Invalid Identification Number for ENR", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "enrollment" }),
  freezeInfo({ code: "R45", name: "Invalid Individual or Company Name for ENR", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "enrollment" }),
  freezeInfo({ code: "R46", name: "Invalid Representative Payee Indicator for ENR", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "enrollment" }),
  freezeInfo({ code: "R47", name: "Duplicate Enrollment", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "enrollment" }),
  freezeInfo({ code: "R50", name: "State Law Affecting RCK Acceptance", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "rck" }),
  freezeInfo({ code: "R51", name: "Ineligible or Improper RCK Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "rck" }),
  freezeInfo({ code: "R52", name: "Stop Payment on Item Related to RCK Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "rck" }),
  freezeInfo({ code: "R53", name: "Item and RCK Entry Presented for Payment", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "rck" }),
  freezeInfo({ code: "R61", name: "Misrouted Return", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "dishonored_return" }),
  freezeInfo({ code: "R62", name: "Return of Erroneous or Reversing Debit", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "dishonored_return" }),
  freezeInfo({ code: "R67", name: "Duplicate Return", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "dishonored_return" }),
  freezeInfo({ code: "R68", name: "Untimely Return", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "dishonored_return" }),
  freezeInfo({ code: "R69", name: "Return Field Errors", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "dishonored_return" }),
  freezeInfo({ code: "R70", name: "Permissible Return Not Accepted or Requested", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "dishonored_return" }),
  freezeInfo({ code: "R71", name: "Misrouted Dishonored Return", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "contested_dishonored_return" }),
  freezeInfo({ code: "R72", name: "Untimely Dishonored Return", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "contested_dishonored_return" }),
  freezeInfo({ code: "R73", name: "Timely Original Return", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "contested_dishonored_return" }),
  freezeInfo({ code: "R74", name: "Corrected Return", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "contested_dishonored_return" }),
  freezeInfo({ code: "R75", name: "Return Not a Duplicate", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "contested_dishonored_return" }),
  freezeInfo({ code: "R76", name: "No Errors Found", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "contested_dishonored_return" }),
  freezeInfo({ code: "R77", name: "Non-Acceptance of R62 Dishonored Return", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "contested_dishonored_return" }),
  freezeInfo({ code: "R80", name: "IAT Entry Coding Error", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "international" }),
  freezeInfo({ code: "R81", name: "Non-Participant in IAT Program", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "international" }),
  freezeInfo({ code: "R82", name: "Invalid Foreign Receiving DFI Identification", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "international" }),
  freezeInfo({ code: "R83", name: "Foreign Receiving DFI Unable to Settle", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "international" }),
  freezeInfo({ code: "R84", name: "Entry Not Processed by Gateway", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "international" }),
  freezeInfo({ code: "R85", name: "Incorrectly Coded Outbound International Payment", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "nacha_iso20022_2023"]), materialSymbol: "undo", category: "international" }),
  freezeInfo({ code: "R90", name: "Return for Sanctions Compliance", status: "planned", validFrom: "2028-03-17", validTo: null, sources: Object.freeze(["nacha_rule_r90"]), materialSymbol: "undo", category: "compliance" }),
]);
const _returnCodeByCode = indexRecords(returnCodeRecords);
export function resolveReturnCode(
  code: string | AchReturnCodeInfo, options: { readonly includeInactive?: boolean } = {},
): AchReturnCodeInfo | undefined {
  return resolveAt(_returnCodeByCode, code, REFERENCE_AS_OF, options.includeInactive ?? false);
}
export function resolveReturnCodeAsOf(
  code: string | AchReturnCodeInfo, on: Date | string,
  options: { readonly includeInactive?: boolean } = {},
): AchReturnCodeInfo | undefined {
  return resolveAt(_returnCodeByCode, code, on, options.includeInactive ?? false);
}
export const AchReturnCode = Object.freeze({
  R01: resolveReturnCode("R01", { includeInactive: true })!,
  R02: resolveReturnCode("R02", { includeInactive: true })!,
  R03: resolveReturnCode("R03", { includeInactive: true })!,
  R04: resolveReturnCode("R04", { includeInactive: true })!,
  R05: resolveReturnCode("R05", { includeInactive: true })!,
  R06: resolveReturnCode("R06", { includeInactive: true })!,
  R07: resolveReturnCode("R07", { includeInactive: true })!,
  R08: resolveReturnCode("R08", { includeInactive: true })!,
  R09: resolveReturnCode("R09", { includeInactive: true })!,
  R10: resolveReturnCode("R10", { includeInactive: true })!,
  R11: resolveReturnCode("R11", { includeInactive: true })!,
  R12: resolveReturnCode("R12", { includeInactive: true })!,
  R13: resolveReturnCode("R13", { includeInactive: true })!,
  R14: resolveReturnCode("R14", { includeInactive: true })!,
  R15: resolveReturnCode("R15", { includeInactive: true })!,
  R16: resolveReturnCode("R16", { includeInactive: true })!,
  R17: resolveReturnCode("R17", { includeInactive: true })!,
  R18: resolveReturnCode("R18", { includeInactive: true })!,
  R19: resolveReturnCode("R19", { includeInactive: true })!,
  R20: resolveReturnCode("R20", { includeInactive: true })!,
  R21: resolveReturnCode("R21", { includeInactive: true })!,
  R22: resolveReturnCode("R22", { includeInactive: true })!,
  R23: resolveReturnCode("R23", { includeInactive: true })!,
  R24: resolveReturnCode("R24", { includeInactive: true })!,
  R25: resolveReturnCode("R25", { includeInactive: true })!,
  R26: resolveReturnCode("R26", { includeInactive: true })!,
  R27: resolveReturnCode("R27", { includeInactive: true })!,
  R28: resolveReturnCode("R28", { includeInactive: true })!,
  R29: resolveReturnCode("R29", { includeInactive: true })!,
  R30: resolveReturnCode("R30", { includeInactive: true })!,
  R31: resolveReturnCode("R31", { includeInactive: true })!,
  R32: resolveReturnCode("R32", { includeInactive: true })!,
  R33: resolveReturnCode("R33", { includeInactive: true })!,
  R34: resolveReturnCode("R34", { includeInactive: true })!,
  R35: resolveReturnCode("R35", { includeInactive: true })!,
  R36: resolveReturnCode("R36", { includeInactive: true })!,
  R37: resolveReturnCode("R37", { includeInactive: true })!,
  R38: resolveReturnCode("R38", { includeInactive: true })!,
  R39: resolveReturnCode("R39", { includeInactive: true })!,
  R40: resolveReturnCode("R40", { includeInactive: true })!,
  R41: resolveReturnCode("R41", { includeInactive: true })!,
  R42: resolveReturnCode("R42", { includeInactive: true })!,
  R43: resolveReturnCode("R43", { includeInactive: true })!,
  R44: resolveReturnCode("R44", { includeInactive: true })!,
  R45: resolveReturnCode("R45", { includeInactive: true })!,
  R46: resolveReturnCode("R46", { includeInactive: true })!,
  R47: resolveReturnCode("R47", { includeInactive: true })!,
  R50: resolveReturnCode("R50", { includeInactive: true })!,
  R51: resolveReturnCode("R51", { includeInactive: true })!,
  R52: resolveReturnCode("R52", { includeInactive: true })!,
  R53: resolveReturnCode("R53", { includeInactive: true })!,
  R61: resolveReturnCode("R61", { includeInactive: true })!,
  R62: resolveReturnCode("R62", { includeInactive: true })!,
  R67: resolveReturnCode("R67", { includeInactive: true })!,
  R68: resolveReturnCode("R68", { includeInactive: true })!,
  R69: resolveReturnCode("R69", { includeInactive: true })!,
  R70: resolveReturnCode("R70", { includeInactive: true })!,
  R71: resolveReturnCode("R71", { includeInactive: true })!,
  R72: resolveReturnCode("R72", { includeInactive: true })!,
  R73: resolveReturnCode("R73", { includeInactive: true })!,
  R74: resolveReturnCode("R74", { includeInactive: true })!,
  R75: resolveReturnCode("R75", { includeInactive: true })!,
  R76: resolveReturnCode("R76", { includeInactive: true })!,
  R77: resolveReturnCode("R77", { includeInactive: true })!,
  R80: resolveReturnCode("R80", { includeInactive: true })!,
  R81: resolveReturnCode("R81", { includeInactive: true })!,
  R82: resolveReturnCode("R82", { includeInactive: true })!,
  R83: resolveReturnCode("R83", { includeInactive: true })!,
  R84: resolveReturnCode("R84", { includeInactive: true })!,
  R85: resolveReturnCode("R85", { includeInactive: true })!,
  R90: resolveReturnCode("R90", { includeInactive: true })!,
});
export type AchReturnCode = (typeof AchReturnCode)[keyof typeof AchReturnCode];
export const currentReturnCodeRecords = Object.freeze(
  returnCodeRecords.filter((record) => isEffective(record)),
);
export const returnCodeCount = _returnCodeByCode.size;
export const returnCodeRecordCount = returnCodeRecords.length;
export const currentReturnCodeCount = currentReturnCodeRecords.length;

export const standardEntryClassCodeRecords: readonly AchStandardEntryClassCodeInfo[] = Object.freeze([
  freezeInfo({ code: "ACK", name: "Acknowledgment Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "acknowledgment", consumerOrCorporate: "corporate", direction: "nonmonetary", addendaSupport: "optional_one" }),
  freezeInfo({ code: "ADV", name: "Automated Accounting Advice", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "accounting", consumerOrCorporate: "financial_institution", direction: "nonmonetary", addendaSupport: "none" }),
  freezeInfo({ code: "ARC", name: "Accounts Receivable Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "check_conversion", consumerOrCorporate: "consumer", direction: "debit", addendaSupport: "none" }),
  freezeInfo({ code: "ATX", name: "Financial EDI Acknowledgment", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "acknowledgment", consumerOrCorporate: "corporate", direction: "nonmonetary", addendaSupport: "optional_one" }),
  freezeInfo({ code: "BOC", name: "Back Office Conversion Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "check_conversion", consumerOrCorporate: "consumer", direction: "debit", addendaSupport: "none" }),
  freezeInfo({ code: "CCD", name: "Corporate Credit or Debit Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "payment", consumerOrCorporate: "corporate", direction: "credit_or_debit", addendaSupport: "optional_one" }),
  freezeInfo({ code: "CIE", name: "Customer-Initiated Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "payment", consumerOrCorporate: "consumer_to_corporate", direction: "credit", addendaSupport: "optional_one" }),
  freezeInfo({ code: "COR", name: "Notification of Change", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "notification", consumerOrCorporate: "consumer_or_corporate", direction: "nonmonetary", addendaSupport: "required_one" }),
  freezeInfo({ code: "CTX", name: "Corporate Trade Exchange Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "payment", consumerOrCorporate: "corporate", direction: "credit_or_debit", addendaSupport: "optional_many" }),
  freezeInfo({ code: "DNE", name: "Death Notification Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "notification", consumerOrCorporate: "consumer", direction: "nonmonetary", addendaSupport: "required_one" }),
  freezeInfo({ code: "ENR", name: "Automated Enrollment Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "enrollment", consumerOrCorporate: "consumer", direction: "nonmonetary", addendaSupport: "required_many" }),
  freezeInfo({ code: "IAT", name: "International ACH Transaction", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025", "nacha_iat_2026"]), materialSymbol: "account_balance", entryKind: "payment", consumerOrCorporate: "consumer_or_corporate", direction: "credit_or_debit", addendaSupport: "required_seven_optional_five" }),
  freezeInfo({ code: "MTE", name: "Machine Transfer Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "terminal", consumerOrCorporate: "consumer", direction: "credit_or_debit", addendaSupport: "required_one" }),
  freezeInfo({ code: "POP", name: "Point-of-Purchase Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "check_conversion", consumerOrCorporate: "consumer", direction: "debit", addendaSupport: "none" }),
  freezeInfo({ code: "POS", name: "Point-of-Sale Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "terminal", consumerOrCorporate: "consumer", direction: "debit", addendaSupport: "required_one" }),
  freezeInfo({ code: "PPD", name: "Prearranged Payment and Deposit Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "payment", consumerOrCorporate: "consumer", direction: "credit_or_debit", addendaSupport: "optional_one" }),
  freezeInfo({ code: "RCK", name: "Re-presented Check Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "check_conversion", consumerOrCorporate: "consumer", direction: "debit", addendaSupport: "none" }),
  freezeInfo({ code: "SHR", name: "Shared Network Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "terminal", consumerOrCorporate: "consumer", direction: "debit", addendaSupport: "required_one" }),
  freezeInfo({ code: "TEL", name: "Telephone-Initiated Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "payment", consumerOrCorporate: "consumer", direction: "debit", addendaSupport: "none" }),
  freezeInfo({ code: "TRC", name: "Truncated Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "check_truncation", consumerOrCorporate: "consumer", direction: "debit", addendaSupport: "none" }),
  freezeInfo({ code: "TRX", name: "Truncated Entries Exchange", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "check_truncation", consumerOrCorporate: "consumer", direction: "debit", addendaSupport: "required_many" }),
  freezeInfo({ code: "WEB", name: "Internet-Initiated or Mobile Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide", "nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "payment", consumerOrCorporate: "consumer", direction: "credit_or_debit", addendaSupport: "optional_one" }),
  freezeInfo({ code: "XCK", name: "Destroyed Check Entry", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "account_balance", entryKind: "check_replacement", consumerOrCorporate: "consumer", direction: "debit", addendaSupport: "none" }),
]);
const _standardEntryClassCodeByCode = indexRecords(standardEntryClassCodeRecords);
export function resolveStandardEntryClassCode(
  code: string | AchStandardEntryClassCodeInfo, options: { readonly includeInactive?: boolean } = {},
): AchStandardEntryClassCodeInfo | undefined {
  return resolveAt(_standardEntryClassCodeByCode, code, REFERENCE_AS_OF, options.includeInactive ?? false);
}
export function resolveStandardEntryClassCodeAsOf(
  code: string | AchStandardEntryClassCodeInfo, on: Date | string,
  options: { readonly includeInactive?: boolean } = {},
): AchStandardEntryClassCodeInfo | undefined {
  return resolveAt(_standardEntryClassCodeByCode, code, on, options.includeInactive ?? false);
}
export const AchStandardEntryClassCode = Object.freeze({
  ACK: resolveStandardEntryClassCode("ACK", { includeInactive: true })!,
  ADV: resolveStandardEntryClassCode("ADV", { includeInactive: true })!,
  ARC: resolveStandardEntryClassCode("ARC", { includeInactive: true })!,
  ATX: resolveStandardEntryClassCode("ATX", { includeInactive: true })!,
  BOC: resolveStandardEntryClassCode("BOC", { includeInactive: true })!,
  CCD: resolveStandardEntryClassCode("CCD", { includeInactive: true })!,
  CIE: resolveStandardEntryClassCode("CIE", { includeInactive: true })!,
  COR: resolveStandardEntryClassCode("COR", { includeInactive: true })!,
  CTX: resolveStandardEntryClassCode("CTX", { includeInactive: true })!,
  DNE: resolveStandardEntryClassCode("DNE", { includeInactive: true })!,
  ENR: resolveStandardEntryClassCode("ENR", { includeInactive: true })!,
  IAT: resolveStandardEntryClassCode("IAT", { includeInactive: true })!,
  MTE: resolveStandardEntryClassCode("MTE", { includeInactive: true })!,
  POP: resolveStandardEntryClassCode("POP", { includeInactive: true })!,
  POS: resolveStandardEntryClassCode("POS", { includeInactive: true })!,
  PPD: resolveStandardEntryClassCode("PPD", { includeInactive: true })!,
  RCK: resolveStandardEntryClassCode("RCK", { includeInactive: true })!,
  SHR: resolveStandardEntryClassCode("SHR", { includeInactive: true })!,
  TEL: resolveStandardEntryClassCode("TEL", { includeInactive: true })!,
  TRC: resolveStandardEntryClassCode("TRC", { includeInactive: true })!,
  TRX: resolveStandardEntryClassCode("TRX", { includeInactive: true })!,
  WEB: resolveStandardEntryClassCode("WEB", { includeInactive: true })!,
  XCK: resolveStandardEntryClassCode("XCK", { includeInactive: true })!,
});
export type AchStandardEntryClassCode = (typeof AchStandardEntryClassCode)[keyof typeof AchStandardEntryClassCode];
export const currentStandardEntryClassCodeRecords = Object.freeze(
  standardEntryClassCodeRecords.filter((record) => isEffective(record)),
);
export const standardEntryClassCodeCount = _standardEntryClassCodeByCode.size;
export const standardEntryClassCodeRecordCount = standardEntryClassCodeRecords.length;
export const currentStandardEntryClassCodeCount = currentStandardEntryClassCodeRecords.length;

export const serviceClassCodeRecords: readonly AchServiceClassCodeInfo[] = Object.freeze([
  freezeInfo({ code: "200", name: "Mixed Debits and Credits", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide"]), materialSymbol: "sync_alt", direction: "mixed" }),
  freezeInfo({ code: "220", name: "Credits Only", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide"]), materialSymbol: "sync_alt", direction: "credit" }),
  freezeInfo({ code: "225", name: "Debits Only", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide"]), materialSymbol: "sync_alt", direction: "debit" }),
  freezeInfo({ code: "280", name: "Automated Accounting Advices", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "sync_alt", direction: "accounting" }),
]);
const _serviceClassCodeByCode = indexRecords(serviceClassCodeRecords);
export function resolveServiceClassCode(
  code: string | AchServiceClassCodeInfo, options: { readonly includeInactive?: boolean } = {},
): AchServiceClassCodeInfo | undefined {
  return resolveAt(_serviceClassCodeByCode, code, REFERENCE_AS_OF, options.includeInactive ?? false);
}
export function resolveServiceClassCodeAsOf(
  code: string | AchServiceClassCodeInfo, on: Date | string,
  options: { readonly includeInactive?: boolean } = {},
): AchServiceClassCodeInfo | undefined {
  return resolveAt(_serviceClassCodeByCode, code, on, options.includeInactive ?? false);
}
export const AchServiceClassCode = Object.freeze({
  Code200: resolveServiceClassCode("200", { includeInactive: true })!,
  Code220: resolveServiceClassCode("220", { includeInactive: true })!,
  Code225: resolveServiceClassCode("225", { includeInactive: true })!,
  Code280: resolveServiceClassCode("280", { includeInactive: true })!,
});
export type AchServiceClassCode = (typeof AchServiceClassCode)[keyof typeof AchServiceClassCode];
export const currentServiceClassCodeRecords = Object.freeze(
  serviceClassCodeRecords.filter((record) => isEffective(record)),
);
export const serviceClassCodeCount = _serviceClassCodeByCode.size;
export const serviceClassCodeRecordCount = serviceClassCodeRecords.length;
export const currentServiceClassCodeCount = currentServiceClassCodeRecords.length;

export const recordTypeCodeRecords: readonly AchRecordTypeCodeInfo[] = Object.freeze([
  freezeInfo({ code: "1", name: "File Header", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide"]), materialSymbol: "description" }),
  freezeInfo({ code: "5", name: "Company or Batch Header", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide"]), materialSymbol: "description" }),
  freezeInfo({ code: "6", name: "Entry Detail", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide"]), materialSymbol: "description" }),
  freezeInfo({ code: "7", name: "Addenda", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide"]), materialSymbol: "description" }),
  freezeInfo({ code: "8", name: "Company or Batch Control", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide"]), materialSymbol: "description" }),
  freezeInfo({ code: "9", name: "File Control or Padding", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_developer_guide"]), materialSymbol: "description" }),
]);
const _recordTypeCodeByCode = indexRecords(recordTypeCodeRecords);
export function resolveRecordTypeCode(
  code: string | AchRecordTypeCodeInfo, options: { readonly includeInactive?: boolean } = {},
): AchRecordTypeCodeInfo | undefined {
  return resolveAt(_recordTypeCodeByCode, code, REFERENCE_AS_OF, options.includeInactive ?? false);
}
export function resolveRecordTypeCodeAsOf(
  code: string | AchRecordTypeCodeInfo, on: Date | string,
  options: { readonly includeInactive?: boolean } = {},
): AchRecordTypeCodeInfo | undefined {
  return resolveAt(_recordTypeCodeByCode, code, on, options.includeInactive ?? false);
}
export const AchRecordTypeCode = Object.freeze({
  Code1: resolveRecordTypeCode("1", { includeInactive: true })!,
  Code5: resolveRecordTypeCode("5", { includeInactive: true })!,
  Code6: resolveRecordTypeCode("6", { includeInactive: true })!,
  Code7: resolveRecordTypeCode("7", { includeInactive: true })!,
  Code8: resolveRecordTypeCode("8", { includeInactive: true })!,
  Code9: resolveRecordTypeCode("9", { includeInactive: true })!,
});
export type AchRecordTypeCode = (typeof AchRecordTypeCode)[keyof typeof AchRecordTypeCode];
export const currentRecordTypeCodeRecords = Object.freeze(
  recordTypeCodeRecords.filter((record) => isEffective(record)),
);
export const recordTypeCodeCount = _recordTypeCodeByCode.size;
export const recordTypeCodeRecordCount = recordTypeCodeRecords.length;
export const currentRecordTypeCodeCount = currentRecordTypeCodeRecords.length;

export const changeCodeRecords: readonly AchChangeCodeInfo[] = Object.freeze([
  freezeInfo({ code: "C01", name: "Incorrect DFI Account Number", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_iso20022_2023", "nacha_basic_2025"]), materialSymbol: "edit", correctedFields: Object.freeze(["account_number"]), appliesTo: Object.freeze(["all"]) }),
  freezeInfo({ code: "C02", name: "Incorrect Routing Number", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_iso20022_2023", "nacha_basic_2025"]), materialSymbol: "edit", correctedFields: Object.freeze(["routing_number"]), appliesTo: Object.freeze(["all"]) }),
  freezeInfo({ code: "C03", name: "Incorrect Routing and DFI Account Numbers", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_iso20022_2023", "nacha_basic_2025"]), materialSymbol: "edit", correctedFields: Object.freeze(["routing_number", "account_number"]), appliesTo: Object.freeze(["all"]) }),
  freezeInfo({ code: "C05", name: "Incorrect Transaction Code", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_iso20022_2023", "nacha_basic_2025"]), materialSymbol: "edit", correctedFields: Object.freeze(["transaction_code"]), appliesTo: Object.freeze(["all"]) }),
  freezeInfo({ code: "C06", name: "Incorrect DFI Account Number and Transaction Code", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_iso20022_2023", "nacha_basic_2025"]), materialSymbol: "edit", correctedFields: Object.freeze(["account_number", "transaction_code"]), appliesTo: Object.freeze(["all"]) }),
  freezeInfo({ code: "C07", name: "Incorrect Routing Number DFI Account Number and Transaction Code", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_iso20022_2023", "nacha_basic_2025"]), materialSymbol: "edit", correctedFields: Object.freeze(["routing_number", "account_number", "transaction_code"]), appliesTo: Object.freeze(["all"]) }),
  freezeInfo({ code: "C08", name: "Incorrect Receiving DFI Identification", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_iso20022_2023", "nacha_basic_2025"]), materialSymbol: "edit", correctedFields: Object.freeze(["receiving_dfi_identification"]), appliesTo: Object.freeze(["IAT"]) }),
  freezeInfo({ code: "C09", name: "Incorrect Individual or Receiver Identification Number", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_iso20022_2023", "nacha_basic_2025"]), materialSymbol: "edit", correctedFields: Object.freeze(["individual_or_receiver_id"]), appliesTo: Object.freeze(["all"]) }),
  freezeInfo({ code: "C13", name: "Addenda Format Error", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_iso20022_2023", "nacha_basic_2025"]), materialSymbol: "edit", correctedFields: Object.freeze(["addenda_format"]), appliesTo: Object.freeze(["entries_with_addenda"]) }),
  freezeInfo({ code: "C14", name: "Incorrect SEC Code for Outbound International Payment", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_iso20022_2023", "nacha_basic_2025"]), materialSymbol: "edit", correctedFields: Object.freeze(["sec_code"]), appliesTo: Object.freeze(["outbound_international"]) }),
]);
const _changeCodeByCode = indexRecords(changeCodeRecords);
export function resolveChangeCode(
  code: string | AchChangeCodeInfo, options: { readonly includeInactive?: boolean } = {},
): AchChangeCodeInfo | undefined {
  return resolveAt(_changeCodeByCode, code, REFERENCE_AS_OF, options.includeInactive ?? false);
}
export function resolveChangeCodeAsOf(
  code: string | AchChangeCodeInfo, on: Date | string,
  options: { readonly includeInactive?: boolean } = {},
): AchChangeCodeInfo | undefined {
  return resolveAt(_changeCodeByCode, code, on, options.includeInactive ?? false);
}
export const AchChangeCode = Object.freeze({
  C01: resolveChangeCode("C01", { includeInactive: true })!,
  C02: resolveChangeCode("C02", { includeInactive: true })!,
  C03: resolveChangeCode("C03", { includeInactive: true })!,
  C05: resolveChangeCode("C05", { includeInactive: true })!,
  C06: resolveChangeCode("C06", { includeInactive: true })!,
  C07: resolveChangeCode("C07", { includeInactive: true })!,
  C08: resolveChangeCode("C08", { includeInactive: true })!,
  C09: resolveChangeCode("C09", { includeInactive: true })!,
  C13: resolveChangeCode("C13", { includeInactive: true })!,
  C14: resolveChangeCode("C14", { includeInactive: true })!,
});
export type AchChangeCode = (typeof AchChangeCode)[keyof typeof AchChangeCode];
export const currentChangeCodeRecords = Object.freeze(
  changeCodeRecords.filter((record) => isEffective(record)),
);
export const changeCodeCount = _changeCodeByCode.size;
export const changeCodeRecordCount = changeCodeRecords.length;
export const currentChangeCodeCount = currentChangeCodeRecords.length;

export const addendaTypeCodeRecords: readonly AchAddendaTypeCodeInfo[] = Object.freeze([
  freezeInfo({ code: "01", name: "Legacy Cross-Border Payment Information", status: "legacy", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "note_add", appliesTo: Object.freeze(["CBR", "PBR"]) }),
  freezeInfo({ code: "02", name: "Terminal Location Information", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "note_add", appliesTo: Object.freeze(["MTE", "POS", "SHR"]) }),
  freezeInfo({ code: "05", name: "Payment-Related Information", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "note_add", appliesTo: Object.freeze(["ACK", "ATX", "CCD", "CIE", "CTX", "DNE", "ENR", "PPD", "TRX", "WEB"]) }),
  freezeInfo({ code: "10", name: "First Mandatory IAT Addenda", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "fedglobal_manual_2026"]), materialSymbol: "note_add", appliesTo: Object.freeze(["IAT"]) }),
  freezeInfo({ code: "11", name: "Second Mandatory IAT Addenda", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "fedglobal_manual_2026"]), materialSymbol: "note_add", appliesTo: Object.freeze(["IAT"]) }),
  freezeInfo({ code: "12", name: "Third Mandatory IAT Addenda", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "fedglobal_manual_2026"]), materialSymbol: "note_add", appliesTo: Object.freeze(["IAT"]) }),
  freezeInfo({ code: "13", name: "Fourth Mandatory IAT Addenda", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "fedglobal_manual_2026"]), materialSymbol: "note_add", appliesTo: Object.freeze(["IAT"]) }),
  freezeInfo({ code: "14", name: "Fifth Mandatory IAT Addenda", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "fedglobal_manual_2026"]), materialSymbol: "note_add", appliesTo: Object.freeze(["IAT"]) }),
  freezeInfo({ code: "15", name: "Sixth Mandatory IAT Addenda", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "fedglobal_manual_2026"]), materialSymbol: "note_add", appliesTo: Object.freeze(["IAT"]) }),
  freezeInfo({ code: "16", name: "Seventh Mandatory IAT Addenda", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "fedglobal_manual_2026"]), materialSymbol: "note_add", appliesTo: Object.freeze(["IAT"]) }),
  freezeInfo({ code: "17", name: "IAT Remittance Information", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "fedglobal_manual_2026"]), materialSymbol: "note_add", appliesTo: Object.freeze(["IAT"]) }),
  freezeInfo({ code: "18", name: "IAT Foreign Correspondent Bank Information", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025", "fedglobal_manual_2026"]), materialSymbol: "note_add", appliesTo: Object.freeze(["IAT"]) }),
  freezeInfo({ code: "98", name: "Notification of Change Information", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "note_add", appliesTo: Object.freeze(["COR", "refused_COR"]) }),
  freezeInfo({ code: "99", name: "Return Information", status: "current", validFrom: null, validTo: null, sources: Object.freeze(["nacha_basic_2025"]), materialSymbol: "note_add", appliesTo: Object.freeze(["return", "dishonored_return", "contested_return"]) }),
]);
const _addendaTypeCodeByCode = indexRecords(addendaTypeCodeRecords);
export function resolveAddendaTypeCode(
  code: string | AchAddendaTypeCodeInfo, options: { readonly includeInactive?: boolean } = {},
): AchAddendaTypeCodeInfo | undefined {
  return resolveAt(_addendaTypeCodeByCode, code, REFERENCE_AS_OF, options.includeInactive ?? false);
}
export function resolveAddendaTypeCodeAsOf(
  code: string | AchAddendaTypeCodeInfo, on: Date | string,
  options: { readonly includeInactive?: boolean } = {},
): AchAddendaTypeCodeInfo | undefined {
  return resolveAt(_addendaTypeCodeByCode, code, on, options.includeInactive ?? false);
}
export const AchAddendaTypeCode = Object.freeze({
  Code01: resolveAddendaTypeCode("01", { includeInactive: true })!,
  Code02: resolveAddendaTypeCode("02", { includeInactive: true })!,
  Code05: resolveAddendaTypeCode("05", { includeInactive: true })!,
  Code10: resolveAddendaTypeCode("10", { includeInactive: true })!,
  Code11: resolveAddendaTypeCode("11", { includeInactive: true })!,
  Code12: resolveAddendaTypeCode("12", { includeInactive: true })!,
  Code13: resolveAddendaTypeCode("13", { includeInactive: true })!,
  Code14: resolveAddendaTypeCode("14", { includeInactive: true })!,
  Code15: resolveAddendaTypeCode("15", { includeInactive: true })!,
  Code16: resolveAddendaTypeCode("16", { includeInactive: true })!,
  Code17: resolveAddendaTypeCode("17", { includeInactive: true })!,
  Code18: resolveAddendaTypeCode("18", { includeInactive: true })!,
  Code98: resolveAddendaTypeCode("98", { includeInactive: true })!,
  Code99: resolveAddendaTypeCode("99", { includeInactive: true })!,
});
export type AchAddendaTypeCode = (typeof AchAddendaTypeCode)[keyof typeof AchAddendaTypeCode];
export const currentAddendaTypeCodeRecords = Object.freeze(
  addendaTypeCodeRecords.filter((record) => isEffective(record)),
);
export const addendaTypeCodeCount = _addendaTypeCodeByCode.size;
export const addendaTypeCodeRecordCount = addendaTypeCodeRecords.length;
export const currentAddendaTypeCodeCount = currentAddendaTypeCodeRecords.length;

export const records = Object.freeze({
  transactionCodes: transactionCodeRecords,
  returnCodes: returnCodeRecords,
  standardEntryClassCodes: standardEntryClassCodeRecords,
  serviceClassCodes: serviceClassCodeRecords,
  recordTypeCodes: recordTypeCodeRecords,
  changeCodes: changeCodeRecords,
  addendaTypeCodes: addendaTypeCodeRecords,
});

export const counts = Object.freeze({
  transactionCodes: transactionCodeCount,
  returnCodes: returnCodeCount,
  standardEntryClassCodes: standardEntryClassCodeCount,
  serviceClassCodes: serviceClassCodeCount,
  recordTypeCodes: recordTypeCodeCount,
  changeCodes: changeCodeCount,
  addendaTypeCodes: addendaTypeCodeCount,
});

export const RECORDS = records;
export const COUNTS = counts;
