import assert from "node:assert/strict";
import {
  DATA_FINGERPRINT,
  Mcc,
  MccGroup,
  MccVendor,
  isMcc,
  isMccGroup,
  isMccVendor,
  materialSymbolForMcc,
  mccRecords,
  mccSources,
  resolveMcc,
  resolveVendorKey,
  resolveMccSource,
  sourceForMccDetails,
} from "../dist/index.js";

assert.equal(DATA_FINGERPRINT.length, 64);
assert.equal(mccRecords.length, 4970);
assert.equal(mccSources.length, 6);
assert.equal(resolveMccSource("adyen_dabstep_07d7d7ea")?.license, "CC-BY-4.0");
assert.equal(resolveMccSource("python_iso18245_3b53842")?.status, "imported");
assert.equal(resolveMccSource("python_iso18245_3b53842")?.redistribution, "fair_use_reference");

assert.equal(isMcc("0742"), true);
assert.equal(isMcc("742"), false);
assert.equal(isMccVendor("visa"), true);
assert.equal(isMccVendor("american_express"), true);
assert.equal(isMccGroup("food_and_drink"), true);
assert.equal(isMccGroup("missing"), false);

const stripe = resolveVendorKey(MccVendor.Stripe, "eating_places_restaurants");
assert.equal(stripe?.mcc, Mcc.MCC_5812);
assert.equal(stripe?.name, "Eating Places, Restaurants");
assert.equal(stripe?.group, MccGroup.FoodAndDrink);
assert.equal(materialSymbolForMcc("5812", MccVendor.Stripe), "restaurant");

const visa = resolveMcc("5812", MccVendor.Visa);
assert.equal(visa?.name, "Eating Places and Restaurants");
assert.equal(resolveMcc("742", MccVendor.Visa), undefined);

const importedNames = new Map([
  [MccVendor.Alipay, "Eating places and restaurants"],
  [MccVendor.AmericanExpress, "Eating Places and Restaurants"],
  [MccVendor.Iso18245, "Eating places and restaurants"],
  [MccVendor.Mastercard, "Eating Places, Restaurants"],
  [MccVendor.Usda, "Eating places and Restaurants"],
]);
for (const [vendor, name] of importedNames) {
  const details = resolveMcc("5812", vendor);
  assert.equal(details?.name, name);
  assert.equal(details?.group, MccGroup.FoodAndDrink);
}

for (const [code, group] of [
  ["3998", MccGroup.Transportation],
  ["4733", MccGroup.Entertainment],
  ["7013", MccGroup.RealEstate],
  ["7280", MccGroup.Healthcare],
  ["8912", MccGroup.HomeAndGarden],
]) {
  assert.equal(resolveMcc(code, MccVendor.AmericanExpress)?.group, group);
}

const miscellaneous = resolveVendorKey(MccVendor.Stripe, "miscellaneous");
assert.equal(miscellaneous?.mcc, null);
assert.equal(miscellaneous?.group, MccGroup.Other);
assert.equal(Object.isFrozen(mccRecords), true);
assert.equal(Object.isFrozen(stripe), true);
assert.equal(stripe && sourceForMccDetails(stripe)?.id, stripe?.sourceId);
