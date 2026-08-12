import assert from "node:assert/strict";
import {
  DATA_FINGERPRINT,
  NAICS_VERSION,
  SIC_VERSION,
  childrenOf,
  childrenOfNaics,
  childrenOfSic,
  divisionEntryForSic,
  divisionForSic,
  industries,
  IndustryLevel,
  IndustrySector,
  industrySectors,
  materialSymbolForSic,
  naicsIndustries,
  naicsIndustryCount,
  parentOf,
  parentOfSic,
  resolveIndustry,
  resolveIndustrySector,
  resolveNaics,
  resolveSic,
  resolveSicDivision,
  sectorEntries,
  sectorForIndustry,
  sicDivisionEntries,
  SicDivision,
  sicDivisions,
  sicIndustries,
  sicIndustryCount,
  SicLevel,
} from "../dist/index.js";

const software = resolveIndustry("513210");
assert.equal(software?.level, IndustryLevel.NationalIndustry);
assert.equal(parentOf(software)?.code, "51321");
assert.equal(software?.sectorCode, "51");
assert.equal(sectorForIndustry(software), IndustrySector.Information);
assert.equal(sectorForIndustry(software)?.materialSymbol, "language");
assert.ok(childrenOf("31-33").some((item) => item.code === "311"));
assert.equal(industries.length, 2125);
assert.equal(industrySectors.length, 20);
assert.equal(sectorEntries.length, 20);
assert.equal(resolveIndustrySector("manufacturing"), IndustrySector.Manufacturing);
assert.equal(resolveIndustrySector("31-33"), IndustrySector.Manufacturing);
assert.equal(resolveIndustry("9999999"), undefined);
assert.equal(Object.isFrozen(industries), true);
assert.equal(Object.isFrozen(software), true);
assert.equal(Object.isFrozen(childrenOf("31-33")), true);

assert.equal(NAICS_VERSION, "2022");
assert.equal(naicsIndustryCount, 2125);
assert.equal(naicsIndustries, industries);
assert.equal(resolveNaics("513210"), software);
assert.equal(childrenOfNaics("31-33"), childrenOf("31-33"));

const wheat = resolveSic("0111");
assert.equal(wheat?.title, "Wheat");
assert.equal(wheat?.level, SicLevel.Industry);
assert.equal(wheat?.level.depth, 4);
assert.equal(parentOfSic(wheat)?.code, "011");
assert.equal(wheat?.divisionCode, "A");
assert.equal(divisionForSic(wheat), SicDivision.AgricultureForestryFishing);
assert.equal(divisionEntryForSic(wheat)?.code, "A");
assert.equal(materialSymbolForSic(wheat), "agriculture");
assert.equal(
  resolveSicDivision("agriculture_forestry_fishing"),
  SicDivision.AgricultureForestryFishing,
);
assert.equal(resolveSicDivision("A"), SicDivision.AgricultureForestryFishing);

assert.equal(SIC_VERSION, "1987");
assert.equal(sicIndustryCount, 1524);
assert.equal(sicIndustries.length, sicIndustryCount);
assert.equal(sicDivisions.length, 12);
assert.equal(sicDivisionEntries.length, 12);
assert.deepEqual(childrenOfSic("Z").map((item) => item.code), [..."ABCDEFGHIJK"]);
assert.equal(resolveSic("not-a-code"), undefined);
assert.deepEqual(childrenOfSic("not-a-code"), []);
assert.match(DATA_FINGERPRINT, /^[0-9a-f]{64}$/);
assert.equal(Object.isFrozen(sicIndustries), true);
assert.equal(Object.isFrozen(wheat), true);
assert.equal(Object.isFrozen(childrenOfSic("Z")), true);
assert.equal(Object.isFrozen(childrenOfSic("not-a-code")), true);
assert.equal(Object.isFrozen(SicDivision.AgricultureForestryFishing), true);

const qcewRollupCodes = sicIndustries
  .filter((item) => item.level === SicLevel.QcewRollup)
  .map((item) => item.code);
assert.deepEqual(qcewRollupCodes, [
  "0740",
  "0780",
  "1520",
  "1540",
  "4210",
  "5810",
  "6510",
  "7210",
]);
assert.equal(resolveSic("0740")?.level, SicLevel.QcewRollup);
assert.equal(SicLevel.QcewRollup.depth, 4);
