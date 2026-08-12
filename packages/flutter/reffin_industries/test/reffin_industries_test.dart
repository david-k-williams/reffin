import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:reffin_industries/reffin_industries.dart';

void main() {
  test('resolves the NAICS hierarchy', () {
    final software = resolveIndustry('513210');
    expect(software?.level, IndustryLevel.nationalIndustry);
    expect(software?.level.depth, 6);
    expect(software?.parent?.code, '51321');
    expect(software?.sector, IndustrySector.information);
    expect(software?.sectorEntry.code, '51');
    expect(software?.icon, Icons.language);
    expect(childrenOf('31-33').map((item) => item.code), contains('311'));
  });

  test('ships the complete snapshot and safe unknowns', () {
    expect(naicsVersion, '2022');
    expect(naicsIndustryCount, 2125);
    expect(industries, hasLength(naicsIndustryCount));
    expect(industrySectors, hasLength(20));
    expect(sectorEntries, hasLength(20));
    expect(IndustrySector.tryParse('manufacturing'), IndustrySector.manufacturing);
    expect(IndustrySector.tryParse('31-33'), IndustrySector.manufacturing);
    expect(resolveIndustry('9999999'), isNull);
  });

  test('resolves the historical SIC hierarchy and native icon', () {
    final wheat = resolveSic('0111');
    expect(wheat?.title, 'Wheat');
    expect(wheat?.level, SicLevel.industry);
    expect(wheat?.level.depth, 4);
    expect(wheat?.parent?.code, '011');
    expect(wheat?.division, SicDivision.agricultureForestryFishing);
    expect(wheat?.divisionEntry.code, 'A');
    expect(wheat?.icon, Icons.agriculture);
    expect(
      SicDivision.tryParse('agriculture_forestry_fishing'),
      SicDivision.agricultureForestryFishing,
    );
    expect(
      SicDivision.tryParse('A'),
      SicDivision.agricultureForestryFishing,
    );
  });

  test('ships the complete immutable SIC snapshot and safe unknowns', () {
    expect(sicVersion, '1987');
    expect(sicIndustryCount, 1524);
    expect(sicIndustries, hasLength(sicIndustryCount));
    expect(sicDivisions, hasLength(12));
    expect(sicDivisionEntries, hasLength(12));
    expect(
      childrenOfSic('Z').map((item) => item.code),
      orderedEquals('ABCDEFGHIJK'.split('')),
    );
    expect(resolveSic('not-a-code'), isNull);
    expect(childrenOfSic('not-a-code'), isEmpty);
    expect(dataFingerprint, matches(RegExp(r'^[0-9a-f]{64}$')));
    expect(
      () => childrenOfSic('Z').add(resolveSic('0111')!),
      throwsUnsupportedError,
    );
  });

  test('keeps explicit NAICS aliases compatible', () {
    expect(naicsIndustries, same(industries));
    expect(resolveNaics('513210'), same(resolveIndustry('513210')));
    expect(childrenOfNaics('31-33'), same(childrenOf('31-33')));
  });

  test('distinguishes QCEW rollups from canonical SIC industries', () {
    expect(
      sicIndustries.where((item) => item.level == SicLevel.qcewRollup).map((item) => item.code),
      orderedEquals([
        '0740',
        '0780',
        '1520',
        '1540',
        '4210',
        '5810',
        '6510',
        '7210',
      ]),
    );
    expect(resolveSic('0740')?.level, SicLevel.qcewRollup);
    expect(SicLevel.qcewRollup.depth, 4);
  });
}
