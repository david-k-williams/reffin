import assert from "node:assert/strict";
import {
  AchAddendaTypeCode,
  AchReturnCode,
  AchServiceClassCode,
  AchTransactionCode,
  DATA_FINGERPRINT,
  currentReturnCodeCount,
  resolveAddendaTypeCode,
  resolveReturnCode,
  resolveReturnCodeAsOf,
  resolveServiceClassCode,
  resolveTransactionCode,
  returnCodeCount,
  returnCodeRecordCount,
} from "../dist/index.js";

assert.equal(AchTransactionCode.Code22.code, "22");
assert.equal(AchTransactionCode.Code22.direction, "credit");
assert.equal(resolveTransactionCode("22"), AchTransactionCode.Code22);
assert.equal(resolveTransactionCode("not-a-code"), undefined);

assert.equal(AchReturnCode.R22.code, "R22");
assert.equal(AchReturnCode.R22.name, "Invalid Individual ID Number");
assert.equal(AchReturnCode.R22.materialSymbol, "undo");
assert.equal(resolveReturnCode("r22"), AchReturnCode.R22);
assert.equal(resolveReturnCode("R00"), undefined);

assert.equal(resolveReturnCode("R90"), undefined);
assert.equal(resolveReturnCode("R90", { includeInactive: true }), AchReturnCode.R90);
assert.equal(resolveReturnCodeAsOf("R90", "2028-03-17")?.name, "Return for Sanctions Compliance");
assert.equal(
  resolveReturnCodeAsOf("R16", "2028-03-16")?.name,
  "Account Frozen or Return per OFAC Instruction",
);
assert.equal(
  resolveReturnCodeAsOf("R16", new Date(2028, 2, 16, 23, 59))?.name,
  "Account Frozen or Return per OFAC Instruction",
);
assert.equal(resolveReturnCodeAsOf("R16", "2028-03-17")?.name, "Account Frozen");
assert.equal(resolveReturnCodeAsOf("R90", "not-a-date"), undefined);

assert.equal(resolveAddendaTypeCode("01"), undefined);
assert.equal(
  resolveAddendaTypeCode("01", { includeInactive: true }),
  AchAddendaTypeCode.Code01,
);
assert.equal(resolveServiceClassCode("280"), AchServiceClassCode.Code280);
assert.equal(AchServiceClassCode.Code280.direction, "accounting");

assert.equal(returnCodeCount, 71);
assert.equal(returnCodeRecordCount, 72);
assert.equal(currentReturnCodeCount, 70);
assert.match(DATA_FINGERPRINT, /^[0-9a-f]{64}$/);
assert.equal(Object.isFrozen(AchReturnCode.R22), true);
assert.equal(Object.isFrozen(AchReturnCode.R22.sources), true);
