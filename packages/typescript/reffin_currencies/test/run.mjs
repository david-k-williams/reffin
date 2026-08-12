import assert from "node:assert/strict";
import { CLDR_VERSION, Currency, currencies, isCurrency, resolveCurrency, tryParseCurrency } from "../dist/index.js";

assert.equal(isCurrency("usd"), false);
assert.equal(isCurrency("USD"), true);
assert.equal(tryParseCurrency("usd"), Currency.USD);
assert.equal(resolveCurrency("usd")?.code, Currency.USD);
assert.equal(resolveCurrency("usd")?.displaySymbol, "$");
assert.equal(CLDR_VERSION, "48.2");
assert.equal(resolveCurrency("JPY")?.minorDigits, 0);
assert.equal(resolveCurrency("CHF")?.cashRounding, 5);
assert.equal(resolveCurrency("DEM")?.active, false);
assert.equal(resolveCurrency("NOPE"), undefined);
assert.equal(currencies.length, Object.keys(Currency).length);
assert.equal(Object.isFrozen(currencies), true);
assert.equal(Object.isFrozen(resolveCurrency("USD")), true);
assert.equal(Object.isFrozen(resolveCurrency("USD")?.territories), true);
