// Generated offline ISO 20022 catalogs. Do not edit by hand.
// Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
import type {
  BankTransactionCodeInfo, Iso20022CodeInfo, Iso20022CodeSetInfo,
  MessageDefinitionInfo, RawRow,
} from "./model.js";
export type * from "./model.js";
import { rows as code_sets00Rows } from "./data/code_sets00.js";
import { rows as external_codes00Rows } from "./data/external_codes00.js";
import { rows as external_codes01Rows } from "./data/external_codes01.js";
import { rows as external_codes02Rows } from "./data/external_codes02.js";
import { rows as external_codes03Rows } from "./data/external_codes03.js";
import { rows as external_codes04Rows } from "./data/external_codes04.js";
import { rows as external_codes05Rows } from "./data/external_codes05.js";
import { rows as external_codes06Rows } from "./data/external_codes06.js";
import { rows as external_codes07Rows } from "./data/external_codes07.js";
import { rows as external_codes08Rows } from "./data/external_codes08.js";
import { rows as external_codes09Rows } from "./data/external_codes09.js";
import { rows as external_codes10Rows } from "./data/external_codes10.js";
import { rows as external_codes11Rows } from "./data/external_codes11.js";
import { rows as external_codes12Rows } from "./data/external_codes12.js";
import { rows as external_codes13Rows } from "./data/external_codes13.js";
import { rows as external_codes14Rows } from "./data/external_codes14.js";
import { rows as external_codes15Rows } from "./data/external_codes15.js";
import { rows as external_codes16Rows } from "./data/external_codes16.js";
import { rows as external_codes17Rows } from "./data/external_codes17.js";
import { rows as external_codes18Rows } from "./data/external_codes18.js";
import { rows as external_codes19Rows } from "./data/external_codes19.js";
import { rows as bank_transaction_codes00Rows } from "./data/bank_transaction_codes00.js";
import { rows as bank_transaction_codes01Rows } from "./data/bank_transaction_codes01.js";
import { rows as bank_transaction_codes02Rows } from "./data/bank_transaction_codes02.js";
import { rows as bank_transaction_codes03Rows } from "./data/bank_transaction_codes03.js";
import { rows as message_definitions00Rows } from "./data/message_definitions00.js";
import { rows as message_definitions01Rows } from "./data/message_definitions01.js";

export const DATA_FINGERPRINT = "19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80" as const;
export const EXTERNAL_CODE_SETS_VERSION = "May 2026 v1" as const;
export const EXTERNAL_CODE_SETS_ARTIFACT_VERSION = "1Q2026_externalcodesets_v1" as const;
export const BANK_TRANSACTION_CODES_VERSION = "2025-11-30" as const;
export const MESSAGE_DEFINITIONS_VERSION = "2026-06-26" as const;

const codeSetsRows: readonly RawRow[] = Object.freeze([
  ...code_sets00Rows,
]);
const externalCodesRows: readonly RawRow[] = Object.freeze([
  ...external_codes00Rows,
  ...external_codes01Rows,
  ...external_codes02Rows,
  ...external_codes03Rows,
  ...external_codes04Rows,
  ...external_codes05Rows,
  ...external_codes06Rows,
  ...external_codes07Rows,
  ...external_codes08Rows,
  ...external_codes09Rows,
  ...external_codes10Rows,
  ...external_codes11Rows,
  ...external_codes12Rows,
  ...external_codes13Rows,
  ...external_codes14Rows,
  ...external_codes15Rows,
  ...external_codes16Rows,
  ...external_codes17Rows,
  ...external_codes18Rows,
  ...external_codes19Rows,
]);
const bankTransactionCodesRows: readonly RawRow[] = Object.freeze([
  ...bank_transaction_codes00Rows,
  ...bank_transaction_codes01Rows,
  ...bank_transaction_codes02Rows,
  ...bank_transaction_codes03Rows,
]);
const messageDefinitionsRows: readonly RawRow[] = Object.freeze([
  ...message_definitions00Rows,
  ...message_definitions01Rows,
]);

const materialSymbolBySet = new Map<string, string>([["ExternalPurpose1Code", "payments"], ["ExternalStatusReason1Code", "error_outline"], ["ExternalReturnReason1Code", "undo"], ["ExternalLocalInstrument1Code", "account_balance"], ["ExternalCategoryPurpose1Code", "category"], ["ExternalServiceLevel1Code", "speed"], ["ExternalPaymentTransactionStatus1Code", "sync"], ["ExternalPaymentGroupStatus1Code", "fact_check"]]);
const optional = (value: string): string | null => value || null;
const sources = (value: string): readonly string[] => Object.freeze(value.split('|').filter(Boolean));
const key = (value: string): string => value.trim().toLowerCase();
const composite = (...values: readonly string[]): string => values.map(key).join('\u0000');

export const codeSets: readonly Iso20022CodeSetInfo[] = Object.freeze(codeSetsRows.map((row) =>
  Object.freeze({ codeSet: row[0]!, definition: row[1]!, status: row[2]! as 'registered' | 'obsolete' | 'provisionally_registered',
    sources: sources(row[3]!), isCurrent: row[2] !== 'obsolete' }),
));
export const externalCodeRecords: readonly Iso20022CodeInfo[] = Object.freeze(externalCodesRows.map((row) =>
  Object.freeze({
    codeSet: row[0]!, code: row[1]!, name: row[2]!, label: row[3]!, definition: row[4]!,
    requester: optional(row[5]!), status: row[6]! as 'registered' | 'obsolete',
    lastUpdated: optional(row[7]!), creationDate: optional(row[8]!), replacedBy: optional(row[9]!),
    mappingStandard1: optional(row[10]!), mappingValue1: optional(row[11]!),
    mappingStandard2: optional(row[12]!), mappingValue2: optional(row[13]!),
    additionalInformation: optional(row[14]!), sources: sources(row[15]!),
    materialSymbol: materialSymbolBySet.get(row[0]!) ?? 'code', isCurrent: row[6] === 'registered',
  }),
));
export const currentExternalCodes = Object.freeze(externalCodeRecords.filter((item) => item.isCurrent));
export const bankTransactionCodeRecords: readonly BankTransactionCodeInfo[] = Object.freeze(
  bankTransactionCodesRows.map((row) => Object.freeze({
    domainCode: row[0]!, domainName: row[1]!, familyCode: row[2]!, familyName: row[3]!,
    subfamilyCode: row[4]!, subfamilyName: row[5]!, status: row[6]!, statusDate: row[7]!,
    code: `${row[0]!}-${row[2]!}-${row[4]!}` ,
  })),
);
export const messageDefinitions: readonly MessageDefinitionInfo[] = Object.freeze(
  messageDefinitionsRows.map((row) => Object.freeze({
    businessArea: row[0]!, messageId: row[1]!, messageNumber: row[2]!, variant: row[3]!,
    version: row[4]!, name: row[5]!,
  })),
);

export const codeSetCount = codeSets.length;
export const externalCodeRecordCount = externalCodeRecords.length;
export const currentExternalCodeCount = currentExternalCodes.length;
export const externalCodeIdentityCount = new Set(externalCodeRecords.map((item) => composite(item.codeSet, item.code))).size;
export const bankTransactionCodeRecordCount = bankTransactionCodeRecords.length;
export const bankTransactionCodeIdentityCount = new Set(bankTransactionCodeRecords.map((item) => composite(item.domainCode, item.familyCode, item.subfamilyCode))).size;
export const messageDefinitionCount = messageDefinitions.length;
export const paymentCodeCount = 950;

const codeSetByName = new Map(codeSets.map((item) => [key(item.codeSet), item]));
const externalByKey = new Map<string, Iso20022CodeInfo[]>();
const externalByCode = new Map<string, Iso20022CodeInfo[]>();
for (const item of externalCodeRecords) {
  const qualified = composite(item.codeSet, item.code);
  externalByKey.set(qualified, [...(externalByKey.get(qualified) ?? []), item]);
  externalByCode.set(key(item.code), [...(externalByCode.get(key(item.code)) ?? []), item]);
}
for (const [indexKey, values] of externalByKey) externalByKey.set(indexKey, Object.freeze(values) as Iso20022CodeInfo[]);
for (const [indexKey, values] of externalByCode) externalByCode.set(indexKey, Object.freeze(values) as Iso20022CodeInfo[]);

export function resolveCodeSet(codeSet: string, options: { readonly includeObsolete?: boolean } = {}): Iso20022CodeSetInfo | undefined {
  const item = codeSetByName.get(key(codeSet));
  return item && (options.includeObsolete || item.isCurrent) ? item : undefined;
}
export function recordsFor(codeSet: string, code: string, options: { readonly includeObsolete?: boolean } = {}): readonly Iso20022CodeInfo[] {
  const values = externalByKey.get(composite(codeSet, code)) ?? [];
  return options.includeObsolete ? values : Object.freeze(values.filter((item) => item.isCurrent));
}
export function resolveCode(codeSet: string, code: string, options: { readonly includeObsolete?: boolean } = {}): Iso20022CodeInfo | undefined {
  const current = recordsFor(codeSet, code);
  return current[0] ?? (options.includeObsolete ? recordsFor(codeSet, code, { includeObsolete: true })[0] : undefined);
}
export function findCodes(code: string, options: { readonly includeObsolete?: boolean } = {}): readonly Iso20022CodeInfo[] {
  const values = externalByCode.get(key(code)) ?? [];
  return options.includeObsolete ? values : Object.freeze(values.filter((item) => item.isCurrent));
}
export function searchCodes(query: string, options: { readonly codeSet?: string; readonly includeObsolete?: boolean; readonly limit?: number } = {}): readonly Iso20022CodeInfo[] {
  const needle = key(query);
  if (!needle || (options.limit !== undefined && options.limit <= 0)) return Object.freeze([]);
  const setKey = options.codeSet === undefined ? undefined : key(options.codeSet);
  const found: Iso20022CodeInfo[] = [];
  for (const item of externalCodeRecords) {
    if (!options.includeObsolete && !item.isCurrent) continue;
    if (setKey !== undefined && key(item.codeSet) !== setKey) continue;
    const text = [item.code, item.name, item.label, item.definition, item.additionalInformation ?? ''].join('\n').toLowerCase();
    if (text.includes(needle)) { found.push(item); if (options.limit !== undefined && found.length >= options.limit) break; }
  }
  return Object.freeze(found);
}

const btcByKey = new Map<string, BankTransactionCodeInfo[]>();
for (const item of bankTransactionCodeRecords) {
  const itemKey = composite(item.domainCode, item.familyCode, item.subfamilyCode);
  btcByKey.set(itemKey, [...(btcByKey.get(itemKey) ?? []), item]);
}
for (const [indexKey, values] of btcByKey) btcByKey.set(indexKey, Object.freeze(values) as BankTransactionCodeInfo[]);
export function resolveBankTransactionCode(domainCode: string, familyCode: string, subfamilyCode: string): readonly BankTransactionCodeInfo[] {
  return btcByKey.get(composite(domainCode, familyCode, subfamilyCode)) ?? Object.freeze([]);
}
export function findBankTransactionCodes(domainCode: string, options: { readonly familyCode?: string; readonly subfamilyCode?: string } = {}): readonly BankTransactionCodeInfo[] {
  const domain = key(domainCode); const family = options.familyCode === undefined ? undefined : key(options.familyCode);
  const subfamily = options.subfamilyCode === undefined ? undefined : key(options.subfamilyCode);
  return Object.freeze(bankTransactionCodeRecords.filter((item) => key(item.domainCode) === domain
    && (family === undefined || key(item.familyCode) === family)
    && (subfamily === undefined || key(item.subfamilyCode) === subfamily)));
}

const messageById = new Map(messageDefinitions.map((item) => [key(item.messageId), item]));
export function resolveMessageIdentifier(messageId: string): MessageDefinitionInfo | undefined {
  return messageById.get(key(messageId));
}
export function findMessageDefinitions(options: { readonly businessArea?: string; readonly messageNumber?: string } = {}): readonly MessageDefinitionInfo[] {
  const area = options.businessArea === undefined ? undefined : key(options.businessArea);
  const number = options.messageNumber === undefined ? undefined : key(options.messageNumber);
  return Object.freeze(messageDefinitions.filter((item) => (area === undefined || key(item.businessArea) === area)
    && (number === undefined || key(item.messageNumber) === number)));
}
