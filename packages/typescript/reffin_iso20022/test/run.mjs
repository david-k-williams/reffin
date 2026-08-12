import assert from "node:assert/strict";
import {
  DATA_FINGERPRINT,
  EXTERNAL_CODE_SETS_ARTIFACT_VERSION,
  EXTERNAL_CODE_SETS_VERSION,
  BANK_TRANSACTION_CODES_VERSION,
  MESSAGE_DEFINITIONS_VERSION,
  LocalInstrumentCode,
  PaymentPurposeCode,
  PaymentReturnReasonCode,
  bankTransactionCodeRecordCount,
  codeSetCount,
  currentExternalCodeCount,
  externalCodeIdentityCount,
  externalCodeRecordCount,
  findCodes,
  findMessageDefinitions,
  messageDefinitionCount,
  paymentCodeCount,
  recordsFor,
  resolveBankTransactionCode,
  resolveCode,
  resolveMessageIdentifier,
  searchCodes,
} from "../dist/index.js";

assert.equal(codeSetCount, 158);
assert.equal(externalCodeRecordCount, 3246);
assert.equal(externalCodeIdentityCount, 3245);
assert.equal(currentExternalCodeCount, 3213);
assert.equal(paymentCodeCount, 950);
assert.match(DATA_FINGERPRINT, /^[0-9a-f]{64}$/);
assert.equal(EXTERNAL_CODE_SETS_VERSION, "May 2026 v1");
assert.equal(EXTERNAL_CODE_SETS_ARTIFACT_VERSION, "1Q2026_externalcodesets_v1");
assert.equal(BANK_TRANSACTION_CODES_VERSION, "2025-11-30");
assert.equal(MESSAGE_DEFINITIONS_VERSION, "2026-06-26");
assert.equal(resolveCode("ExternalReturnReason1Code", "AC01")?.label, "Incorrect Account Number");
assert.equal(resolveCode("ExternalReturnReason1Code", "not-a-code"), undefined);

const ac01 = findCodes("ac01");
assert.ok(ac01.length >= 3);
assert.equal(new Set(ac01.map((item) => item.codeSet)).size, ac01.length);
const history = recordsFor("ExternalLocalInstrument1Code", "CTP", { includeObsolete: true });
assert.equal(history.length, 2);
assert.equal(LocalInstrumentCode.CTP.label, "Credit Transfer Preferred");
assert.deepEqual(recordsFor("ExternalLocalInstrument1Code", "CTP"), [history[1]]);
assert.equal(searchCodes("salary", { limit: 3 }).length, 3);

assert.equal(PaymentPurposeCode.SALA.code, "SALA");
assert.equal(PaymentPurposeCode.SALA.label, "Salary Payment");
assert.equal(PaymentPurposeCode.SALA.materialSymbol, "payments");
assert.equal(PaymentReturnReasonCode.AC01.materialSymbol, "undo");
assert.equal(Object.isFrozen(PaymentPurposeCode.SALA), true);
assert.equal(Object.isFrozen(PaymentPurposeCode.SALA.sources), true);

assert.ok(bankTransactionCodeRecordCount > 1000);
assert.equal(resolveBankTransactionCode("SECU", "CASH", "CPEN").length, 2);
const message = resolveMessageIdentifier("pacs.008.001.14");
assert.equal(message?.businessArea, "pacs");
assert.equal(message?.version, "14");
assert.equal(resolveMessageIdentifier("pacs.008.001"), undefined);
assert.equal(messageDefinitionCount, 797);
assert.ok(findMessageDefinitions({ businessArea: "pacs" }).length > 0);
