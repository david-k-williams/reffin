import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:reffin_cards/reffin_cards.dart';

void main() {
  test('exposes network metadata and optional brand assets', () {
    expect(CardNetwork.visa.id, 'visa');
    expect(CardNetwork.visa.name, 'visa');
    expect(CardNetwork.visa.label, 'Visa');
    expect(CardNetwork.visa.icon, Icons.credit_card);
    expect(CardNetwork.visa.brandAssetKey, 'visa');
    expect(CardNetwork.other.brandAssetKey, isNull);
    expect(CardNetwork.unknown.brandAssetKey, isNull);
  });

  test('safely parses every vocabulary by stable ID', () {
    expect(CardNetwork.tryParse('visa'), CardNetwork.visa);
    expect(CardNetwork.tryParse('missing'), isNull);
    expect(FormFactor.tryParse('virtual'), FormFactor.virtual);
    expect(FundingType.tryParse('credit'), FundingType.credit);
    expect(PaymentMethodFamily.tryParse('card'), PaymentMethodFamily.card);
    expect(PaymentOutcome.tryParse('approved'), PaymentOutcome.approved);
    expect(ProductClass.tryParse('commercial'), ProductClass.commercial);
    expect(TransactionChannel.tryParse('in_person'), TransactionChannel.inPerson);
    expect(VerificationOutcome.tryParse('match'), VerificationOutcome.match);
  });

  test('uses native Material icons for semantic metadata', () {
    expect(FundingType.credit.label, 'Credit');
    expect(FundingType.credit.icon, Icons.credit_score);
    expect(FundingType.credit.description, contains('credit agreement'));
    expect(FormFactor.virtual.icon, Icons.devices);
    expect(PaymentOutcome.approved.icon, Icons.check_circle);
    expect(TransactionChannel.inPerson.icon, Icons.point_of_sale);
    expect(VerificationOutcome.match.icon, Icons.verified);
  });

  test('publishes deterministic records, counts, and fingerprint', () {
    expect(counts, <String, int>{
      'card_networks': 16,
      'form_factors': 4,
      'funding_types': 6,
      'payment_method_families': 12,
      'payment_outcomes': 8,
      'product_classes': 5,
      'transaction_channels': 7,
      'verification_outcomes': 10,
    });
    expect(records['card_networks'], CardNetwork.values);
    expect(records['verification_outcomes'], VerificationOutcome.values);
    expect(DATA_FINGERPRINT, matches(RegExp(r'^[0-9a-f]{64}$')));
    expect(dataFingerprint, DATA_FINGERPRINT);
  });
}
