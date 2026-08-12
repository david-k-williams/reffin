import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:reffin_iso20022/reffin_iso20022.dart';

void main() {
  test('resolves qualified catalog values and explicit history', () {
    expect(codeSetCount, 158);
    expect(externalCodeRecordCount, 3246);
    expect(externalCodeIdentityCount, 3245);
    expect(currentExternalCodeCount, 3213);
    expect(paymentCodeCount, 950);
    expect(dataFingerprint, matches(RegExp(r'^[0-9a-f]{64}$')));
    expect(externalCodeSetsVersion, 'May 2026 v1');
    expect(externalCodeSetsArtifactVersion, '1Q2026_externalcodesets_v1');
    expect(bankTransactionCodesVersion, '2025-11-30');
    expect(messageDefinitionsVersion, '2026-06-26');
    expect(resolveCode('ExternalReturnReason1Code', 'AC01')?.label, 'Incorrect Account Number');
    expect(resolveCode('ExternalReturnReason1Code', 'not-a-code'), isNull);
    expect(findCodes('ac01').length, greaterThanOrEqualTo(3));

    final history = recordsFor('ExternalLocalInstrument1Code', 'CTP', includeObsolete: true);
    expect(history.length, 2);
    expect(LocalInstrumentCode.ctp.label, 'Credit Transfer Preferred');
    expect(recordsFor('ExternalLocalInstrument1Code', 'CTP'), [history[1]]);
    expect(searchCodes('salary', limit: 3).length, 3);
  });

  test('exposes payment enums with native Material icons', () {
    expect(PaymentPurposeCode.sala.code, 'SALA');
    expect(PaymentPurposeCode.sala.label, 'Salary Payment');
    expect(PaymentPurposeCode.sala.icon, Icons.payments);
    expect(PaymentReturnReasonCode.ac01.icon, Icons.undo);
    expect(PaymentPurposeCode.tryParse(' sala '), PaymentPurposeCode.sala);
  });

  test('resolves BTC hierarchy and current message identifiers', () {
    expect(bankTransactionCodeRecordCount, greaterThan(1000));
    expect(resolveBankTransactionCode('SECU', 'CASH', 'CPEN').length, 2);
    final message = resolveMessageIdentifier('pacs.008.001.14');
    expect(message?.businessArea, 'pacs');
    expect(message?.version, '14');
    expect(resolveMessageIdentifier('pacs.008.001'), isNull);
    expect(messageDefinitionCount, 797);
    expect(findMessageDefinitions(businessArea: 'pacs'), isNotEmpty);
  });
}
