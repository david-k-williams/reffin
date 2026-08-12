import assert from "node:assert/strict";
import {
  CardNetwork,
  COUNTS,
  DATA_FINGERPRINT,
  FormFactor,
  FundingType,
  PaymentMethodFamily,
  PaymentOutcome,
  ProductClass,
  RECORDS,
  TransactionChannel,
  VerificationOutcome,
  isCardNetworkId,
  tryParseCardNetwork,
  tryParseFormFactor,
  tryParseFundingType,
  tryParsePaymentMethodFamily,
  tryParsePaymentOutcome,
  tryParseProductClass,
  tryParseTransactionChannel,
  tryParseVerificationOutcome,
} from "../dist/index.js";

assert.equal(CardNetwork.Visa.id, "visa");
assert.equal(CardNetwork.Visa.name, "Visa");
assert.equal(CardNetwork.Visa.materialSymbol, "credit_card");
assert.equal(CardNetwork.Visa.brandAssetKey, "visa");
assert.equal(CardNetwork.Other.brandAssetKey, null);
assert.equal(CardNetwork.Unknown.brandAssetKey, null);
assert.equal(tryParseCardNetwork("visa"), CardNetwork.Visa);
assert.equal(tryParseCardNetwork("missing"), undefined);
assert.equal(isCardNetworkId("visa"), true);
assert.equal(isCardNetworkId("missing"), false);

assert.equal(tryParseFormFactor("virtual"), FormFactor.Virtual);
assert.equal(tryParseFundingType("credit"), FundingType.Credit);
assert.equal(tryParsePaymentMethodFamily("card"), PaymentMethodFamily.Card);
assert.equal(tryParsePaymentOutcome("approved"), PaymentOutcome.Approved);
assert.equal(tryParseProductClass("commercial"), ProductClass.Commercial);
assert.equal(tryParseTransactionChannel("in_person"), TransactionChannel.InPerson);
assert.equal(tryParseVerificationOutcome("match"), VerificationOutcome.Match);

assert.equal(FundingType.Credit.materialSymbol, "credit_score");
assert.match(FundingType.Credit.description, /credit agreement/);
assert.equal(TransactionChannel.InPerson.materialSymbol, "point_of_sale");
assert.equal(VerificationOutcome.Match.materialSymbol, "verified");

assert.deepEqual(COUNTS, {
  cardNetworks: 16,
  formFactors: 4,
  fundingTypes: 6,
  paymentMethodFamilies: 12,
  paymentOutcomes: 8,
  productClasses: 5,
  transactionChannels: 7,
  verificationOutcomes: 10,
});
assert.equal(RECORDS.cardNetworks.length, COUNTS.cardNetworks);
assert.equal(RECORDS.verificationOutcomes.length, COUNTS.verificationOutcomes);
assert.match(DATA_FINGERPRINT, /^[0-9a-f]{64}$/);
assert.equal(Object.isFrozen(CardNetwork), true);
assert.equal(Object.isFrozen(CardNetwork.Visa), true);
