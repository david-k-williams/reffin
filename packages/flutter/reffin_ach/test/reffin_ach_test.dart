import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:reffin_ach/reffin_ach.dart';

void main() {
  test('exposes transaction and return code identities with native icons', () {
    expect(AchTransactionCode.code22.code, '22');
    expect(AchTransactionCode.code22.info.direction, 'credit');
    expect(resolveTransactionCode('22'), AchTransactionCode.code22.info);
    expect(resolveTransactionCode('not-a-code'), isNull);

    expect(AchReturnCode.r22.code, 'R22');
    expect(AchReturnCode.r22.info.name, 'Invalid Individual ID Number');
    expect(AchReturnCode.r22.info.icon, Icons.undo);
    expect(resolveReturnCode('r22'), AchReturnCode.r22.info);
    expect(resolveReturnCode('R00'), isNull);
  });

  test('resolves planned return codes and versioned R16 by date', () {
    expect(resolveReturnCode('R90'), isNull);
    expect(resolveReturnCode('R90', includeInactive: true), AchReturnCode.r90.info);
    expect(
      resolveReturnCodeAsOf('R90', DateTime.utc(2028, 3, 17))?.name,
      'Return for Sanctions Compliance',
    );
    expect(
      resolveReturnCodeAsOf('R16', DateTime.utc(2028, 3, 16, 23, 59))?.name,
      'Account Frozen or Return per OFAC Instruction',
    );
    expect(
      resolveReturnCodeAsOf('R16', DateTime.utc(2028, 3, 17))?.name,
      'Account Frozen',
    );
  });

  test('excludes legacy addenda and resolves accounting service class', () {
    expect(AchAddendaTypeCode.code01.code, '01');
    expect(resolveAddendaTypeCode('01'), isNull);
    expect(
      resolveAddendaTypeCode('01', includeInactive: true),
      AchAddendaTypeCode.code01.info,
    );
    expect(resolveServiceClassCode('280'), AchServiceClassCode.code280.info);
    expect(AchServiceClassCode.code280.info.direction, 'accounting');
  });

  test('publishes clear version counts, fingerprint, and immutable records', () {
    expect(returnCodeCount, 71);
    expect(returnCodeRecordCount, 72);
    expect(currentReturnCodeCount, 70);
    expect(DATA_FINGERPRINT, matches(RegExp(r'^[0-9a-f]{64}$')));
    expect(
      () => returnCodeRecords.add(AchReturnCode.r22.info),
      throwsUnsupportedError,
    );
  });
}
