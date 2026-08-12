import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:reffin_merchants/reffin_merchants.dart';

void main() {
  test('exposes snapshot metadata', () {
    expect(dataFingerprint, hasLength(64));
    expect(mccRecords, hasLength(4970));
    expect(mccSources, hasLength(6));
    expect(resolveMccSource('adyen_dabstep_07d7d7ea')?.license, 'CC-BY-4.0');
    expect(
      resolveMccSource('python_iso18245_3b53842')?.status,
      'imported',
    );
    expect(
      resolveMccSource('python_iso18245_3b53842')?.redistribution,
      'fair_use_reference',
    );
    expect(MccVendor.tryParse('visa'), MccVendor.visa);
    expect(
      MccVendor.tryParse('american_express'),
      MccVendor.americanExpress,
    );
    expect(MccGroup.tryParse('food_and_drink'), MccGroup.foodAndDrink);
    expect(MccGroup.tryParse('missing'), isNull);
  });

  test('preserves a leading-zero MCC', () {
    expect(Mcc.tryParse('0742'), Mcc.mcc0742);
    expect(Mcc.tryParse('742'), isNull);
    final details = Mcc.mcc0742.resolve(MccVendor.visa);
    expect(details?.name, 'Veterinary Services');
    expect(details?.group, MccGroup.agriculture);
  });

  test('resolves vendor-specific labels and native Material icons', () {
    final stripe = resolveVendorKey(
      MccVendor.stripe,
      'eating_places_restaurants',
    );
    expect(stripe?.mcc, Mcc.mcc5812);
    expect(stripe?.name, 'Eating Places, Restaurants');
    expect(stripe?.group, MccGroup.foodAndDrink);
    expect(stripe?.icon, Icons.restaurant);
    expect(stripe?.source.id, stripe?.sourceId);

    final visa = resolveMcc('5812', MccVendor.visa);
    expect(visa?.name, 'Eating Places and Restaurants');

    final importedNames = {
      MccVendor.alipay: 'Eating places and restaurants',
      MccVendor.americanExpress: 'Eating Places and Restaurants',
      MccVendor.iso18245: 'Eating places and restaurants',
      MccVendor.mastercard: 'Eating Places, Restaurants',
      MccVendor.usda: 'Eating places and Restaurants',
    };
    for (final entry in importedNames.entries) {
      final details = resolveMcc('5812', entry.key);
      expect(details?.name, entry.value);
      expect(details?.group, MccGroup.foodAndDrink);
    }
  });

  test('groups American Express private MCC meanings', () {
    final expected = {
      '3998': MccGroup.transportation,
      '4733': MccGroup.entertainment,
      '7013': MccGroup.realEstate,
      '7280': MccGroup.healthcare,
      '8912': MccGroup.homeAndGarden,
    };
    for (final entry in expected.entries) {
      expect(
        resolveMcc(entry.key, MccVendor.americanExpress)?.group,
        entry.value,
      );
    }
  });

  test('supports vendor-only categories and safe unknowns', () {
    final miscellaneous = resolveVendorKey(MccVendor.stripe, 'miscellaneous');
    expect(miscellaneous?.mcc, isNull);
    expect(miscellaneous?.group, MccGroup.other);
    expect(resolveMcc('742', MccVendor.visa), isNull);
    expect(resolveMcc('0000', MccVendor.visa), isNull);
  });
}
