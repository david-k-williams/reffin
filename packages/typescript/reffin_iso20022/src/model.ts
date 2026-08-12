// Generated ISO 20022 value models. Do not edit by hand.
// Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
export type Iso20022CodeStatus = "registered" | "obsolete";

export interface Iso20022CodeSetInfo {
  readonly codeSet: string;
  readonly definition: string;
  readonly status: Iso20022CodeStatus | "provisionally_registered";
  readonly sources: readonly string[];
  readonly isCurrent: boolean;
}

export interface Iso20022CodeInfo {
  readonly codeSet: string;
  readonly code: string;
  readonly name: string;
  readonly label: string;
  readonly definition: string;
  readonly requester: string | null;
  readonly status: Iso20022CodeStatus;
  readonly lastUpdated: string | null;
  readonly creationDate: string | null;
  readonly replacedBy: string | null;
  readonly mappingStandard1: string | null;
  readonly mappingValue1: string | null;
  readonly mappingStandard2: string | null;
  readonly mappingValue2: string | null;
  readonly additionalInformation: string | null;
  readonly sources: readonly string[];
  readonly materialSymbol: string;
  readonly isCurrent: boolean;
}

export interface BankTransactionCodeInfo {
  readonly domainCode: string;
  readonly domainName: string;
  readonly familyCode: string;
  readonly familyName: string;
  readonly subfamilyCode: string;
  readonly subfamilyName: string;
  readonly status: string;
  readonly statusDate: string;
  readonly code: string;
}

export interface MessageDefinitionInfo {
  readonly businessArea: string;
  readonly messageId: string;
  readonly messageNumber: string;
  readonly variant: string;
  readonly version: string;
  readonly name: string;
}

export type RawRow = readonly string[];
