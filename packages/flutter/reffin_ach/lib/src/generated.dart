// Generated ACH reference catalogs. Do not edit by hand.
// Input SHA-256: 252f6495924ee9a8b82ec6088df0325739cb5e902bcf3e3bdc1f86429995de6e

import 'package:flutter/material.dart';

// ignore: constant_identifier_names
const String DATA_FINGERPRINT = '252f6495924ee9a8b82ec6088df0325739cb5e902bcf3e3bdc1f86429995de6e';
const String dataFingerprint = DATA_FINGERPRINT;
final DateTime referenceAsOf = DateTime.utc(2026, 8, 11);

enum AchCodeStatus { current, planned, legacy }

abstract final class AchReferenceInfo {
  const AchReferenceInfo({
    required this.code, required this.name, required this.status,
    required this.validFrom, required this.validTo, required this.sources,
    required this.icon,
  });
  final String code;
  final String name;
  final AchCodeStatus status;
  final DateTime? validFrom;
  final DateTime? validTo;
  final List<String> sources;
  final IconData icon;

  bool isEffective([DateTime? on]) {
    final raw = on ?? referenceAsOf;
    final value = DateTime.utc(raw.year, raw.month, raw.day);
    if (status == AchCodeStatus.legacy) return false;
    if (validFrom != null && value.isBefore(validFrom!)) return false;
    return validTo == null || !value.isAfter(validTo!);
  }
}

final class AchTransactionCodeInfo extends AchReferenceInfo {
  const AchTransactionCodeInfo({
    required super.code, required super.name, required super.status,
    required super.validFrom, required super.validTo, required super.sources,
    required super.icon,
    required this.accountType,
    required this.direction,
    required this.entryKind,
    required this.returnForCodes,
  });
  final String accountType;
  final String direction;
  final String entryKind;
  final List<String> returnForCodes;
}

final class AchReturnCodeInfo extends AchReferenceInfo {
  const AchReturnCodeInfo({
    required super.code, required super.name, required super.status,
    required super.validFrom, required super.validTo, required super.sources,
    required super.icon,
    required this.category,
  });
  final String category;
}

final class AchStandardEntryClassCodeInfo extends AchReferenceInfo {
  const AchStandardEntryClassCodeInfo({
    required super.code, required super.name, required super.status,
    required super.validFrom, required super.validTo, required super.sources,
    required super.icon,
    required this.entryKind,
    required this.consumerOrCorporate,
    required this.direction,
    required this.addendaSupport,
  });
  final String entryKind;
  final String consumerOrCorporate;
  final String direction;
  final String addendaSupport;
}

final class AchServiceClassCodeInfo extends AchReferenceInfo {
  const AchServiceClassCodeInfo({
    required super.code, required super.name, required super.status,
    required super.validFrom, required super.validTo, required super.sources,
    required super.icon,
    required this.direction,
  });
  final String direction;
}

final class AchRecordTypeCodeInfo extends AchReferenceInfo {
  const AchRecordTypeCodeInfo({
    required super.code, required super.name, required super.status,
    required super.validFrom, required super.validTo, required super.sources,
    required super.icon,
  });
}

final class AchChangeCodeInfo extends AchReferenceInfo {
  const AchChangeCodeInfo({
    required super.code, required super.name, required super.status,
    required super.validFrom, required super.validTo, required super.sources,
    required super.icon,
    required this.correctedFields,
    required this.appliesTo,
  });
  final List<String> correctedFields;
  final List<String> appliesTo;
}

final class AchAddendaTypeCodeInfo extends AchReferenceInfo {
  const AchAddendaTypeCodeInfo({
    required super.code, required super.name, required super.status,
    required super.validFrom, required super.validTo, required super.sources,
    required super.icon,
    required this.appliesTo,
  });
  final List<String> appliesTo;
}

enum AchTransactionCode {
  code21('21'),
  code22('22'),
  code23('23'),
  code24('24'),
  code26('26'),
  code27('27'),
  code28('28'),
  code29('29'),
  code31('31'),
  code32('32'),
  code33('33'),
  code34('34'),
  code36('36'),
  code37('37'),
  code38('38'),
  code39('39'),
  code41('41'),
  code42('42'),
  code43('43'),
  code44('44'),
  code46('46'),
  code47('47'),
  code48('48'),
  code49('49'),
  code51('51'),
  code52('52'),
  code53('53'),
  code54('54'),
  code55('55'),
  code56('56'),
  code81('81'),
  code82('82'),
  code83('83'),
  code84('84'),
  code85('85'),
  code86('86'),
  code87('87'),
  code88('88');

  const AchTransactionCode(this.code);
  final String code;
  AchTransactionCodeInfo get info => _transactionCodeDefaultInfo[code]!;
  String get label => info.name;
  IconData get icon => info.icon;
  static AchTransactionCode? tryParse(String code) => _transactionCodeIdentityByCode[code.trim().toUpperCase()];
}

enum AchReturnCode {
  r01('R01'),
  r02('R02'),
  r03('R03'),
  r04('R04'),
  r05('R05'),
  r06('R06'),
  r07('R07'),
  r08('R08'),
  r09('R09'),
  r10('R10'),
  r11('R11'),
  r12('R12'),
  r13('R13'),
  r14('R14'),
  r15('R15'),
  r16('R16'),
  r17('R17'),
  r18('R18'),
  r19('R19'),
  r20('R20'),
  r21('R21'),
  r22('R22'),
  r23('R23'),
  r24('R24'),
  r25('R25'),
  r26('R26'),
  r27('R27'),
  r28('R28'),
  r29('R29'),
  r30('R30'),
  r31('R31'),
  r32('R32'),
  r33('R33'),
  r34('R34'),
  r35('R35'),
  r36('R36'),
  r37('R37'),
  r38('R38'),
  r39('R39'),
  r40('R40'),
  r41('R41'),
  r42('R42'),
  r43('R43'),
  r44('R44'),
  r45('R45'),
  r46('R46'),
  r47('R47'),
  r50('R50'),
  r51('R51'),
  r52('R52'),
  r53('R53'),
  r61('R61'),
  r62('R62'),
  r67('R67'),
  r68('R68'),
  r69('R69'),
  r70('R70'),
  r71('R71'),
  r72('R72'),
  r73('R73'),
  r74('R74'),
  r75('R75'),
  r76('R76'),
  r77('R77'),
  r80('R80'),
  r81('R81'),
  r82('R82'),
  r83('R83'),
  r84('R84'),
  r85('R85'),
  r90('R90');

  const AchReturnCode(this.code);
  final String code;
  AchReturnCodeInfo get info => _returnCodeDefaultInfo[code]!;
  String get label => info.name;
  IconData get icon => info.icon;
  static AchReturnCode? tryParse(String code) => _returnCodeIdentityByCode[code.trim().toUpperCase()];
}

enum AchStandardEntryClassCode {
  ack('ACK'),
  adv('ADV'),
  arc('ARC'),
  atx('ATX'),
  boc('BOC'),
  ccd('CCD'),
  cie('CIE'),
  cor('COR'),
  ctx('CTX'),
  dne('DNE'),
  enr('ENR'),
  iat('IAT'),
  mte('MTE'),
  pop('POP'),
  pos('POS'),
  ppd('PPD'),
  rck('RCK'),
  shr('SHR'),
  tel('TEL'),
  trc('TRC'),
  trx('TRX'),
  web('WEB'),
  xck('XCK');

  const AchStandardEntryClassCode(this.code);
  final String code;
  AchStandardEntryClassCodeInfo get info => _standardEntryClassCodeDefaultInfo[code]!;
  String get label => info.name;
  IconData get icon => info.icon;
  static AchStandardEntryClassCode? tryParse(String code) => _standardEntryClassCodeIdentityByCode[code.trim().toUpperCase()];
}

enum AchServiceClassCode {
  code200('200'),
  code220('220'),
  code225('225'),
  code280('280');

  const AchServiceClassCode(this.code);
  final String code;
  AchServiceClassCodeInfo get info => _serviceClassCodeDefaultInfo[code]!;
  String get label => info.name;
  IconData get icon => info.icon;
  static AchServiceClassCode? tryParse(String code) => _serviceClassCodeIdentityByCode[code.trim().toUpperCase()];
}

enum AchRecordTypeCode {
  code1('1'),
  code5('5'),
  code6('6'),
  code7('7'),
  code8('8'),
  code9('9');

  const AchRecordTypeCode(this.code);
  final String code;
  AchRecordTypeCodeInfo get info => _recordTypeCodeDefaultInfo[code]!;
  String get label => info.name;
  IconData get icon => info.icon;
  static AchRecordTypeCode? tryParse(String code) => _recordTypeCodeIdentityByCode[code.trim().toUpperCase()];
}

enum AchChangeCode {
  c01('C01'),
  c02('C02'),
  c03('C03'),
  c05('C05'),
  c06('C06'),
  c07('C07'),
  c08('C08'),
  c09('C09'),
  c13('C13'),
  c14('C14');

  const AchChangeCode(this.code);
  final String code;
  AchChangeCodeInfo get info => _changeCodeDefaultInfo[code]!;
  String get label => info.name;
  IconData get icon => info.icon;
  static AchChangeCode? tryParse(String code) => _changeCodeIdentityByCode[code.trim().toUpperCase()];
}

enum AchAddendaTypeCode {
  code01('01'),
  code02('02'),
  code05('05'),
  code10('10'),
  code11('11'),
  code12('12'),
  code13('13'),
  code14('14'),
  code15('15'),
  code16('16'),
  code17('17'),
  code18('18'),
  code98('98'),
  code99('99');

  const AchAddendaTypeCode(this.code);
  final String code;
  AchAddendaTypeCodeInfo get info => _addendaTypeCodeDefaultInfo[code]!;
  String get label => info.name;
  IconData get icon => info.icon;
  static AchAddendaTypeCode? tryParse(String code) => _addendaTypeCodeIdentityByCode[code.trim().toUpperCase()];
}

Map<String, List<T>> _indexRecords<T extends AchReferenceInfo>(List<T> records) {
  final result = <String, List<T>>{};
  for (final record in records) {
    result.putIfAbsent(record.code, () => <T>[]).add(record);
  }
  return Map<String, List<T>>.unmodifiable({
    for (final entry in result.entries) entry.key: List<T>.unmodifiable(entry.value),
  });
}

T? _resolve<T extends AchReferenceInfo>(
  Map<String, List<T>> index, String code, DateTime on, bool includeInactive,
) {
  final values = index[code.trim().toUpperCase()];
  if (values == null) return null;
  for (final value in values) {
    if (value.isEffective(on)) return value;
  }
  return includeInactive ? values.first : null;
}

final List<AchTransactionCodeInfo> transactionCodeRecords = List.unmodifiable([
  AchTransactionCodeInfo(code: '21', name: 'Return or NOC for Checking Credit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'checking', direction: 'return_or_noc', entryKind: 'return_or_noc', returnForCodes: const ['22', '23', '24']),
  AchTransactionCodeInfo(code: '22', name: 'Checking Credit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.payments, accountType: 'checking', direction: 'credit', entryKind: 'monetary', returnForCodes: const []),
  AchTransactionCodeInfo(code: '23', name: 'Checking Credit Prenote DNE or ENR', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.payments, accountType: 'checking', direction: 'credit', entryKind: 'prenotification_or_notice', returnForCodes: const []),
  AchTransactionCodeInfo(code: '24', name: 'Checking Zero-Dollar Credit or Acknowledgment', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'checking', direction: 'credit', entryKind: 'zero_dollar_or_acknowledgment', returnForCodes: const []),
  AchTransactionCodeInfo(code: '26', name: 'Return or NOC for Checking Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'checking', direction: 'return_or_noc', entryKind: 'return_or_noc', returnForCodes: const ['27', '28', '29']),
  AchTransactionCodeInfo(code: '27', name: 'Checking Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.payments, accountType: 'checking', direction: 'debit', entryKind: 'monetary', returnForCodes: const []),
  AchTransactionCodeInfo(code: '28', name: 'Checking Debit Prenotification', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.payments, accountType: 'checking', direction: 'debit', entryKind: 'prenotification', returnForCodes: const []),
  AchTransactionCodeInfo(code: '29', name: 'Checking Zero-Dollar Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'checking', direction: 'debit', entryKind: 'zero_dollar', returnForCodes: const []),
  AchTransactionCodeInfo(code: '31', name: 'Return or NOC for Savings Credit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'savings', direction: 'return_or_noc', entryKind: 'return_or_noc', returnForCodes: const ['32', '33', '34']),
  AchTransactionCodeInfo(code: '32', name: 'Savings Credit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.payments, accountType: 'savings', direction: 'credit', entryKind: 'monetary', returnForCodes: const []),
  AchTransactionCodeInfo(code: '33', name: 'Savings Credit Prenote DNE or ENR', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.payments, accountType: 'savings', direction: 'credit', entryKind: 'prenotification_or_notice', returnForCodes: const []),
  AchTransactionCodeInfo(code: '34', name: 'Savings Zero-Dollar Credit or Acknowledgment', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'savings', direction: 'credit', entryKind: 'zero_dollar_or_acknowledgment', returnForCodes: const []),
  AchTransactionCodeInfo(code: '36', name: 'Return or NOC for Savings Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'savings', direction: 'return_or_noc', entryKind: 'return_or_noc', returnForCodes: const ['37', '38', '39']),
  AchTransactionCodeInfo(code: '37', name: 'Savings Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.payments, accountType: 'savings', direction: 'debit', entryKind: 'monetary', returnForCodes: const []),
  AchTransactionCodeInfo(code: '38', name: 'Savings Debit Prenotification', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.payments, accountType: 'savings', direction: 'debit', entryKind: 'prenotification', returnForCodes: const []),
  AchTransactionCodeInfo(code: '39', name: 'Savings Zero-Dollar Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'savings', direction: 'debit', entryKind: 'zero_dollar', returnForCodes: const []),
  AchTransactionCodeInfo(code: '41', name: 'Return or NOC for General Ledger Credit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'general_ledger', direction: 'return_or_noc', entryKind: 'return_or_noc', returnForCodes: const ['42', '43', '44']),
  AchTransactionCodeInfo(code: '42', name: 'General Ledger Credit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'general_ledger', direction: 'credit', entryKind: 'monetary', returnForCodes: const []),
  AchTransactionCodeInfo(code: '43', name: 'General Ledger Credit Prenotification', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'general_ledger', direction: 'credit', entryKind: 'prenotification', returnForCodes: const []),
  AchTransactionCodeInfo(code: '44', name: 'General Ledger Zero-Dollar Credit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'general_ledger', direction: 'credit', entryKind: 'zero_dollar', returnForCodes: const []),
  AchTransactionCodeInfo(code: '46', name: 'Return or NOC for General Ledger Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'general_ledger', direction: 'return_or_noc', entryKind: 'return_or_noc', returnForCodes: const ['47', '48', '49']),
  AchTransactionCodeInfo(code: '47', name: 'General Ledger Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'general_ledger', direction: 'debit', entryKind: 'monetary', returnForCodes: const []),
  AchTransactionCodeInfo(code: '48', name: 'General Ledger Debit Prenotification', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'general_ledger', direction: 'debit', entryKind: 'prenotification', returnForCodes: const []),
  AchTransactionCodeInfo(code: '49', name: 'General Ledger Zero-Dollar Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'general_ledger', direction: 'debit', entryKind: 'zero_dollar', returnForCodes: const []),
  AchTransactionCodeInfo(code: '51', name: 'Return or NOC for Loan Credit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'loan', direction: 'return_or_noc', entryKind: 'return_or_noc', returnForCodes: const ['52', '53', '54']),
  AchTransactionCodeInfo(code: '52', name: 'Loan Credit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'loan', direction: 'credit', entryKind: 'monetary', returnForCodes: const []),
  AchTransactionCodeInfo(code: '53', name: 'Loan Credit Prenotification', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'loan', direction: 'credit', entryKind: 'prenotification', returnForCodes: const []),
  AchTransactionCodeInfo(code: '54', name: 'Loan Zero-Dollar Credit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'loan', direction: 'credit', entryKind: 'zero_dollar', returnForCodes: const []),
  AchTransactionCodeInfo(code: '55', name: 'Loan Debit for Reversal', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'loan', direction: 'debit', entryKind: 'reversal', returnForCodes: const []),
  AchTransactionCodeInfo(code: '56', name: 'Return or NOC for Loan Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'loan', direction: 'return_or_noc', entryKind: 'return_or_noc', returnForCodes: const ['55']),
  AchTransactionCodeInfo(code: '81', name: 'ADV Credit for Originated Debits', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'accounting', direction: 'credit', entryKind: 'accounting', returnForCodes: const []),
  AchTransactionCodeInfo(code: '82', name: 'ADV Debit for Originated Credits', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'accounting', direction: 'debit', entryKind: 'accounting', returnForCodes: const []),
  AchTransactionCodeInfo(code: '83', name: 'ADV Credit for Received Credits', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'accounting', direction: 'credit', entryKind: 'accounting', returnForCodes: const []),
  AchTransactionCodeInfo(code: '84', name: 'ADV Debit for Received Debits', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'accounting', direction: 'debit', entryKind: 'accounting', returnForCodes: const []),
  AchTransactionCodeInfo(code: '85', name: 'ADV Credit for Credits in Rejected Batches', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'accounting', direction: 'credit', entryKind: 'accounting', returnForCodes: const []),
  AchTransactionCodeInfo(code: '86', name: 'ADV Debit for Debits in Rejected Batches', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'accounting', direction: 'debit', entryKind: 'accounting', returnForCodes: const []),
  AchTransactionCodeInfo(code: '87', name: 'ADV Summary Credit for Respondent Activity', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'accounting', direction: 'credit', entryKind: 'accounting', returnForCodes: const []),
  AchTransactionCodeInfo(code: '88', name: 'ADV Summary Debit for Respondent Activity', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.payments, accountType: 'accounting', direction: 'debit', entryKind: 'accounting', returnForCodes: const []),
]);
final _transactionCodeByCode = _indexRecords(transactionCodeRecords);
AchTransactionCodeInfo? resolveTransactionCode(String code, {bool includeInactive = false}) =>
    _resolve(_transactionCodeByCode, code, referenceAsOf, includeInactive);
AchTransactionCodeInfo? resolveTransactionCodeAsOf(
  String code,
  DateTime on, {
  bool includeInactive = false,
}) => _resolve(_transactionCodeByCode, code, on, includeInactive);
final Map<String, AchTransactionCodeInfo> _transactionCodeDefaultInfo = Map.unmodifiable({
  for (final code in _transactionCodeByCode.keys)
    code: _resolve(_transactionCodeByCode, code, referenceAsOf, true)!,
});
final Map<String, AchTransactionCode> _transactionCodeIdentityByCode = Map.unmodifiable({
  for (final value in AchTransactionCode.values) value.code: value,
});
final List<AchTransactionCodeInfo> currentTransactionCodeRecords = List.unmodifiable(
  transactionCodeRecords.where((record) => record.isEffective()),
);
final int transactionCodeCount = _transactionCodeByCode.length;
final int transactionCodeRecordCount = transactionCodeRecords.length;
final int currentTransactionCodeCount = currentTransactionCodeRecords.length;

final List<AchReturnCodeInfo> returnCodeRecords = List.unmodifiable([
  AchReturnCodeInfo(code: 'R01', name: 'Insufficient Funds', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'funds'),
  AchReturnCodeInfo(code: 'R02', name: 'Account Closed', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'account'),
  AchReturnCodeInfo(code: 'R03', name: 'No Account or Unable to Locate Account', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'account'),
  AchReturnCodeInfo(code: 'R04', name: 'Invalid Account Number Structure', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'account'),
  AchReturnCodeInfo(code: 'R05', name: 'Unauthorized Corporate-Code Debit to Consumer Account', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'authorization'),
  AchReturnCodeInfo(code: 'R06', name: 'Returned at ODFI Request', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'request'),
  AchReturnCodeInfo(code: 'R07', name: 'Authorization Revoked by Customer', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'authorization'),
  AchReturnCodeInfo(code: 'R08', name: 'Payment Stopped', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'authorization'),
  AchReturnCodeInfo(code: 'R09', name: 'Uncollected Funds', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'funds'),
  AchReturnCodeInfo(code: 'R10', name: 'Originator Unknown or Not Authorized to Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'authorization'),
  AchReturnCodeInfo(code: 'R11', name: 'Entry Not in Accordance with Authorization', status: AchCodeStatus.current, validFrom: DateTime.utc(2020, 4, 1), validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023', 'nacha_r11_2020'], icon: Icons.undo, category: 'authorization'),
  AchReturnCodeInfo(code: 'R12', name: 'Account Sold to Another DFI', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'account'),
  AchReturnCodeInfo(code: 'R13', name: 'Invalid ACH Routing Number', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'administrative'),
  AchReturnCodeInfo(code: 'R14', name: 'Representative Payee Deceased or Unable to Continue', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'death_or_legal'),
  AchReturnCodeInfo(code: 'R15', name: 'Beneficiary or Account Holder Deceased', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'death_or_legal'),
  AchReturnCodeInfo(code: 'R16', name: 'Account Frozen or Return per OFAC Instruction', status: AchCodeStatus.current, validFrom: null, validTo: DateTime.utc(2028, 3, 16), sources: const ['nacha_basic_2025', 'nacha_iso20022_2023', 'nacha_rule_r90'], icon: Icons.undo, category: 'legal_or_compliance'),
  AchReturnCodeInfo(code: 'R16', name: 'Account Frozen', status: AchCodeStatus.planned, validFrom: DateTime.utc(2028, 3, 17), validTo: null, sources: const ['nacha_rule_r90'], icon: Icons.undo, category: 'legal_or_compliance'),
  AchReturnCodeInfo(code: 'R17', name: 'File Edit Error Questionable Entry or Improper Reversal', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_minor_topics_2026', 'nacha_questionable_2019', 'nacha_reversals_2021'], icon: Icons.undo, category: 'administrative'),
  AchReturnCodeInfo(code: 'R18', name: 'Improper Effective Entry Date', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'administrative'),
  AchReturnCodeInfo(code: 'R19', name: 'Amount Field Error', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'format'),
  AchReturnCodeInfo(code: 'R20', name: 'Non-Transaction Account', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'account'),
  AchReturnCodeInfo(code: 'R21', name: 'Invalid Company Identification', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'administrative'),
  AchReturnCodeInfo(code: 'R22', name: 'Invalid Individual ID Number', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023', 'fedglobal_manual_2026'], icon: Icons.undo, category: 'administrative'),
  AchReturnCodeInfo(code: 'R23', name: 'Credit Entry Refused by Receiver', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'receiver_refusal'),
  AchReturnCodeInfo(code: 'R24', name: 'Duplicate Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'administrative'),
  AchReturnCodeInfo(code: 'R25', name: 'Addenda Error', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'format'),
  AchReturnCodeInfo(code: 'R26', name: 'Mandatory Field Error', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'format'),
  AchReturnCodeInfo(code: 'R27', name: 'Trace Number Error', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'format'),
  AchReturnCodeInfo(code: 'R28', name: 'Routing Number Check Digit Error', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'format'),
  AchReturnCodeInfo(code: 'R29', name: 'Corporate Customer Advises Not Authorized', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'authorization'),
  AchReturnCodeInfo(code: 'R30', name: 'RDFI Not in Check Truncation Program', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'participation'),
  AchReturnCodeInfo(code: 'R31', name: 'Permissible CCD or CTX Return', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'request'),
  AchReturnCodeInfo(code: 'R32', name: 'RDFI Non-Settlement', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'settlement'),
  AchReturnCodeInfo(code: 'R33', name: 'Return of XCK Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'check_entry'),
  AchReturnCodeInfo(code: 'R34', name: 'Limited Participation DFI', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'participation'),
  AchReturnCodeInfo(code: 'R35', name: 'Improper Debit Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'improper_entry'),
  AchReturnCodeInfo(code: 'R36', name: 'Improper Credit Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'improper_entry'),
  AchReturnCodeInfo(code: 'R37', name: 'Source Document Presented for Payment', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'source_document'),
  AchReturnCodeInfo(code: 'R38', name: 'Stop Payment on Source Document', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'source_document'),
  AchReturnCodeInfo(code: 'R39', name: 'Improper Source Document or Duplicate Presentment', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'source_document'),
  AchReturnCodeInfo(code: 'R40', name: 'Federal Agency Return of ENR Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'enrollment'),
  AchReturnCodeInfo(code: 'R41', name: 'Invalid Transaction Code for ENR', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'enrollment'),
  AchReturnCodeInfo(code: 'R42', name: 'Routing Number or Check Digit Error for ENR', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'enrollment'),
  AchReturnCodeInfo(code: 'R43', name: 'Invalid DFI Account Number for ENR', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'enrollment'),
  AchReturnCodeInfo(code: 'R44', name: 'Invalid Identification Number for ENR', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'enrollment'),
  AchReturnCodeInfo(code: 'R45', name: 'Invalid Individual or Company Name for ENR', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'enrollment'),
  AchReturnCodeInfo(code: 'R46', name: 'Invalid Representative Payee Indicator for ENR', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'enrollment'),
  AchReturnCodeInfo(code: 'R47', name: 'Duplicate Enrollment', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'enrollment'),
  AchReturnCodeInfo(code: 'R50', name: 'State Law Affecting RCK Acceptance', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'rck'),
  AchReturnCodeInfo(code: 'R51', name: 'Ineligible or Improper RCK Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'rck'),
  AchReturnCodeInfo(code: 'R52', name: 'Stop Payment on Item Related to RCK Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'rck'),
  AchReturnCodeInfo(code: 'R53', name: 'Item and RCK Entry Presented for Payment', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'rck'),
  AchReturnCodeInfo(code: 'R61', name: 'Misrouted Return', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'dishonored_return'),
  AchReturnCodeInfo(code: 'R62', name: 'Return of Erroneous or Reversing Debit', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'dishonored_return'),
  AchReturnCodeInfo(code: 'R67', name: 'Duplicate Return', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'dishonored_return'),
  AchReturnCodeInfo(code: 'R68', name: 'Untimely Return', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'dishonored_return'),
  AchReturnCodeInfo(code: 'R69', name: 'Return Field Errors', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'dishonored_return'),
  AchReturnCodeInfo(code: 'R70', name: 'Permissible Return Not Accepted or Requested', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'dishonored_return'),
  AchReturnCodeInfo(code: 'R71', name: 'Misrouted Dishonored Return', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'contested_dishonored_return'),
  AchReturnCodeInfo(code: 'R72', name: 'Untimely Dishonored Return', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'contested_dishonored_return'),
  AchReturnCodeInfo(code: 'R73', name: 'Timely Original Return', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'contested_dishonored_return'),
  AchReturnCodeInfo(code: 'R74', name: 'Corrected Return', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'contested_dishonored_return'),
  AchReturnCodeInfo(code: 'R75', name: 'Return Not a Duplicate', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'contested_dishonored_return'),
  AchReturnCodeInfo(code: 'R76', name: 'No Errors Found', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'contested_dishonored_return'),
  AchReturnCodeInfo(code: 'R77', name: 'Non-Acceptance of R62 Dishonored Return', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'contested_dishonored_return'),
  AchReturnCodeInfo(code: 'R80', name: 'IAT Entry Coding Error', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'international'),
  AchReturnCodeInfo(code: 'R81', name: 'Non-Participant in IAT Program', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'international'),
  AchReturnCodeInfo(code: 'R82', name: 'Invalid Foreign Receiving DFI Identification', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'international'),
  AchReturnCodeInfo(code: 'R83', name: 'Foreign Receiving DFI Unable to Settle', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'international'),
  AchReturnCodeInfo(code: 'R84', name: 'Entry Not Processed by Gateway', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'international'),
  AchReturnCodeInfo(code: 'R85', name: 'Incorrectly Coded Outbound International Payment', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'nacha_iso20022_2023'], icon: Icons.undo, category: 'international'),
  AchReturnCodeInfo(code: 'R90', name: 'Return for Sanctions Compliance', status: AchCodeStatus.planned, validFrom: DateTime.utc(2028, 3, 17), validTo: null, sources: const ['nacha_rule_r90'], icon: Icons.undo, category: 'compliance'),
]);
final _returnCodeByCode = _indexRecords(returnCodeRecords);
AchReturnCodeInfo? resolveReturnCode(String code, {bool includeInactive = false}) =>
    _resolve(_returnCodeByCode, code, referenceAsOf, includeInactive);
AchReturnCodeInfo? resolveReturnCodeAsOf(
  String code,
  DateTime on, {
  bool includeInactive = false,
}) => _resolve(_returnCodeByCode, code, on, includeInactive);
final Map<String, AchReturnCodeInfo> _returnCodeDefaultInfo = Map.unmodifiable({
  for (final code in _returnCodeByCode.keys)
    code: _resolve(_returnCodeByCode, code, referenceAsOf, true)!,
});
final Map<String, AchReturnCode> _returnCodeIdentityByCode = Map.unmodifiable({
  for (final value in AchReturnCode.values) value.code: value,
});
final List<AchReturnCodeInfo> currentReturnCodeRecords = List.unmodifiable(
  returnCodeRecords.where((record) => record.isEffective()),
);
final int returnCodeCount = _returnCodeByCode.length;
final int returnCodeRecordCount = returnCodeRecords.length;
final int currentReturnCodeCount = currentReturnCodeRecords.length;

final List<AchStandardEntryClassCodeInfo> standardEntryClassCodeRecords = List.unmodifiable([
  AchStandardEntryClassCodeInfo(code: 'ACK', name: 'Acknowledgment Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'acknowledgment', consumerOrCorporate: 'corporate', direction: 'nonmonetary', addendaSupport: 'optional_one'),
  AchStandardEntryClassCodeInfo(code: 'ADV', name: 'Automated Accounting Advice', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'accounting', consumerOrCorporate: 'financial_institution', direction: 'nonmonetary', addendaSupport: 'none'),
  AchStandardEntryClassCodeInfo(code: 'ARC', name: 'Accounts Receivable Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'check_conversion', consumerOrCorporate: 'consumer', direction: 'debit', addendaSupport: 'none'),
  AchStandardEntryClassCodeInfo(code: 'ATX', name: 'Financial EDI Acknowledgment', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'acknowledgment', consumerOrCorporate: 'corporate', direction: 'nonmonetary', addendaSupport: 'optional_one'),
  AchStandardEntryClassCodeInfo(code: 'BOC', name: 'Back Office Conversion Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'check_conversion', consumerOrCorporate: 'consumer', direction: 'debit', addendaSupport: 'none'),
  AchStandardEntryClassCodeInfo(code: 'CCD', name: 'Corporate Credit or Debit Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'payment', consumerOrCorporate: 'corporate', direction: 'credit_or_debit', addendaSupport: 'optional_one'),
  AchStandardEntryClassCodeInfo(code: 'CIE', name: 'Customer-Initiated Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'payment', consumerOrCorporate: 'consumer_to_corporate', direction: 'credit', addendaSupport: 'optional_one'),
  AchStandardEntryClassCodeInfo(code: 'COR', name: 'Notification of Change', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'notification', consumerOrCorporate: 'consumer_or_corporate', direction: 'nonmonetary', addendaSupport: 'required_one'),
  AchStandardEntryClassCodeInfo(code: 'CTX', name: 'Corporate Trade Exchange Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'payment', consumerOrCorporate: 'corporate', direction: 'credit_or_debit', addendaSupport: 'optional_many'),
  AchStandardEntryClassCodeInfo(code: 'DNE', name: 'Death Notification Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'notification', consumerOrCorporate: 'consumer', direction: 'nonmonetary', addendaSupport: 'required_one'),
  AchStandardEntryClassCodeInfo(code: 'ENR', name: 'Automated Enrollment Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'enrollment', consumerOrCorporate: 'consumer', direction: 'nonmonetary', addendaSupport: 'required_many'),
  AchStandardEntryClassCodeInfo(code: 'IAT', name: 'International ACH Transaction', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025', 'nacha_iat_2026'], icon: Icons.account_balance, entryKind: 'payment', consumerOrCorporate: 'consumer_or_corporate', direction: 'credit_or_debit', addendaSupport: 'required_seven_optional_five'),
  AchStandardEntryClassCodeInfo(code: 'MTE', name: 'Machine Transfer Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'terminal', consumerOrCorporate: 'consumer', direction: 'credit_or_debit', addendaSupport: 'required_one'),
  AchStandardEntryClassCodeInfo(code: 'POP', name: 'Point-of-Purchase Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'check_conversion', consumerOrCorporate: 'consumer', direction: 'debit', addendaSupport: 'none'),
  AchStandardEntryClassCodeInfo(code: 'POS', name: 'Point-of-Sale Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'terminal', consumerOrCorporate: 'consumer', direction: 'debit', addendaSupport: 'required_one'),
  AchStandardEntryClassCodeInfo(code: 'PPD', name: 'Prearranged Payment and Deposit Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'payment', consumerOrCorporate: 'consumer', direction: 'credit_or_debit', addendaSupport: 'optional_one'),
  AchStandardEntryClassCodeInfo(code: 'RCK', name: 'Re-presented Check Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'check_conversion', consumerOrCorporate: 'consumer', direction: 'debit', addendaSupport: 'none'),
  AchStandardEntryClassCodeInfo(code: 'SHR', name: 'Shared Network Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'terminal', consumerOrCorporate: 'consumer', direction: 'debit', addendaSupport: 'required_one'),
  AchStandardEntryClassCodeInfo(code: 'TEL', name: 'Telephone-Initiated Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'payment', consumerOrCorporate: 'consumer', direction: 'debit', addendaSupport: 'none'),
  AchStandardEntryClassCodeInfo(code: 'TRC', name: 'Truncated Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'check_truncation', consumerOrCorporate: 'consumer', direction: 'debit', addendaSupport: 'none'),
  AchStandardEntryClassCodeInfo(code: 'TRX', name: 'Truncated Entries Exchange', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'check_truncation', consumerOrCorporate: 'consumer', direction: 'debit', addendaSupport: 'required_many'),
  AchStandardEntryClassCodeInfo(code: 'WEB', name: 'Internet-Initiated or Mobile Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide', 'nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'payment', consumerOrCorporate: 'consumer', direction: 'credit_or_debit', addendaSupport: 'optional_one'),
  AchStandardEntryClassCodeInfo(code: 'XCK', name: 'Destroyed Check Entry', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.account_balance, entryKind: 'check_replacement', consumerOrCorporate: 'consumer', direction: 'debit', addendaSupport: 'none'),
]);
final _standardEntryClassCodeByCode = _indexRecords(standardEntryClassCodeRecords);
AchStandardEntryClassCodeInfo? resolveStandardEntryClassCode(String code, {bool includeInactive = false}) =>
    _resolve(_standardEntryClassCodeByCode, code, referenceAsOf, includeInactive);
AchStandardEntryClassCodeInfo? resolveStandardEntryClassCodeAsOf(
  String code,
  DateTime on, {
  bool includeInactive = false,
}) => _resolve(_standardEntryClassCodeByCode, code, on, includeInactive);
final Map<String, AchStandardEntryClassCodeInfo> _standardEntryClassCodeDefaultInfo = Map.unmodifiable({
  for (final code in _standardEntryClassCodeByCode.keys)
    code: _resolve(_standardEntryClassCodeByCode, code, referenceAsOf, true)!,
});
final Map<String, AchStandardEntryClassCode> _standardEntryClassCodeIdentityByCode = Map.unmodifiable({
  for (final value in AchStandardEntryClassCode.values) value.code: value,
});
final List<AchStandardEntryClassCodeInfo> currentStandardEntryClassCodeRecords = List.unmodifiable(
  standardEntryClassCodeRecords.where((record) => record.isEffective()),
);
final int standardEntryClassCodeCount = _standardEntryClassCodeByCode.length;
final int standardEntryClassCodeRecordCount = standardEntryClassCodeRecords.length;
final int currentStandardEntryClassCodeCount = currentStandardEntryClassCodeRecords.length;

final List<AchServiceClassCodeInfo> serviceClassCodeRecords = List.unmodifiable([
  AchServiceClassCodeInfo(code: '200', name: 'Mixed Debits and Credits', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide'], icon: Icons.sync_alt, direction: 'mixed'),
  AchServiceClassCodeInfo(code: '220', name: 'Credits Only', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide'], icon: Icons.sync_alt, direction: 'credit'),
  AchServiceClassCodeInfo(code: '225', name: 'Debits Only', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide'], icon: Icons.sync_alt, direction: 'debit'),
  AchServiceClassCodeInfo(code: '280', name: 'Automated Accounting Advices', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.sync_alt, direction: 'accounting'),
]);
final _serviceClassCodeByCode = _indexRecords(serviceClassCodeRecords);
AchServiceClassCodeInfo? resolveServiceClassCode(String code, {bool includeInactive = false}) =>
    _resolve(_serviceClassCodeByCode, code, referenceAsOf, includeInactive);
AchServiceClassCodeInfo? resolveServiceClassCodeAsOf(
  String code,
  DateTime on, {
  bool includeInactive = false,
}) => _resolve(_serviceClassCodeByCode, code, on, includeInactive);
final Map<String, AchServiceClassCodeInfo> _serviceClassCodeDefaultInfo = Map.unmodifiable({
  for (final code in _serviceClassCodeByCode.keys)
    code: _resolve(_serviceClassCodeByCode, code, referenceAsOf, true)!,
});
final Map<String, AchServiceClassCode> _serviceClassCodeIdentityByCode = Map.unmodifiable({
  for (final value in AchServiceClassCode.values) value.code: value,
});
final List<AchServiceClassCodeInfo> currentServiceClassCodeRecords = List.unmodifiable(
  serviceClassCodeRecords.where((record) => record.isEffective()),
);
final int serviceClassCodeCount = _serviceClassCodeByCode.length;
final int serviceClassCodeRecordCount = serviceClassCodeRecords.length;
final int currentServiceClassCodeCount = currentServiceClassCodeRecords.length;

final List<AchRecordTypeCodeInfo> recordTypeCodeRecords = List.unmodifiable([
  AchRecordTypeCodeInfo(code: '1', name: 'File Header', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide'], icon: Icons.description),
  AchRecordTypeCodeInfo(code: '5', name: 'Company or Batch Header', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide'], icon: Icons.description),
  AchRecordTypeCodeInfo(code: '6', name: 'Entry Detail', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide'], icon: Icons.description),
  AchRecordTypeCodeInfo(code: '7', name: 'Addenda', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide'], icon: Icons.description),
  AchRecordTypeCodeInfo(code: '8', name: 'Company or Batch Control', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide'], icon: Icons.description),
  AchRecordTypeCodeInfo(code: '9', name: 'File Control or Padding', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_developer_guide'], icon: Icons.description),
]);
final _recordTypeCodeByCode = _indexRecords(recordTypeCodeRecords);
AchRecordTypeCodeInfo? resolveRecordTypeCode(String code, {bool includeInactive = false}) =>
    _resolve(_recordTypeCodeByCode, code, referenceAsOf, includeInactive);
AchRecordTypeCodeInfo? resolveRecordTypeCodeAsOf(
  String code,
  DateTime on, {
  bool includeInactive = false,
}) => _resolve(_recordTypeCodeByCode, code, on, includeInactive);
final Map<String, AchRecordTypeCodeInfo> _recordTypeCodeDefaultInfo = Map.unmodifiable({
  for (final code in _recordTypeCodeByCode.keys)
    code: _resolve(_recordTypeCodeByCode, code, referenceAsOf, true)!,
});
final Map<String, AchRecordTypeCode> _recordTypeCodeIdentityByCode = Map.unmodifiable({
  for (final value in AchRecordTypeCode.values) value.code: value,
});
final List<AchRecordTypeCodeInfo> currentRecordTypeCodeRecords = List.unmodifiable(
  recordTypeCodeRecords.where((record) => record.isEffective()),
);
final int recordTypeCodeCount = _recordTypeCodeByCode.length;
final int recordTypeCodeRecordCount = recordTypeCodeRecords.length;
final int currentRecordTypeCodeCount = currentRecordTypeCodeRecords.length;

final List<AchChangeCodeInfo> changeCodeRecords = List.unmodifiable([
  AchChangeCodeInfo(code: 'C01', name: 'Incorrect DFI Account Number', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_iso20022_2023', 'nacha_basic_2025'], icon: Icons.edit, correctedFields: const ['account_number'], appliesTo: const ['all']),
  AchChangeCodeInfo(code: 'C02', name: 'Incorrect Routing Number', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_iso20022_2023', 'nacha_basic_2025'], icon: Icons.edit, correctedFields: const ['routing_number'], appliesTo: const ['all']),
  AchChangeCodeInfo(code: 'C03', name: 'Incorrect Routing and DFI Account Numbers', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_iso20022_2023', 'nacha_basic_2025'], icon: Icons.edit, correctedFields: const ['routing_number', 'account_number'], appliesTo: const ['all']),
  AchChangeCodeInfo(code: 'C05', name: 'Incorrect Transaction Code', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_iso20022_2023', 'nacha_basic_2025'], icon: Icons.edit, correctedFields: const ['transaction_code'], appliesTo: const ['all']),
  AchChangeCodeInfo(code: 'C06', name: 'Incorrect DFI Account Number and Transaction Code', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_iso20022_2023', 'nacha_basic_2025'], icon: Icons.edit, correctedFields: const ['account_number', 'transaction_code'], appliesTo: const ['all']),
  AchChangeCodeInfo(code: 'C07', name: 'Incorrect Routing Number DFI Account Number and Transaction Code', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_iso20022_2023', 'nacha_basic_2025'], icon: Icons.edit, correctedFields: const ['routing_number', 'account_number', 'transaction_code'], appliesTo: const ['all']),
  AchChangeCodeInfo(code: 'C08', name: 'Incorrect Receiving DFI Identification', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_iso20022_2023', 'nacha_basic_2025'], icon: Icons.edit, correctedFields: const ['receiving_dfi_identification'], appliesTo: const ['IAT']),
  AchChangeCodeInfo(code: 'C09', name: 'Incorrect Individual or Receiver Identification Number', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_iso20022_2023', 'nacha_basic_2025'], icon: Icons.edit, correctedFields: const ['individual_or_receiver_id'], appliesTo: const ['all']),
  AchChangeCodeInfo(code: 'C13', name: 'Addenda Format Error', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_iso20022_2023', 'nacha_basic_2025'], icon: Icons.edit, correctedFields: const ['addenda_format'], appliesTo: const ['entries_with_addenda']),
  AchChangeCodeInfo(code: 'C14', name: 'Incorrect SEC Code for Outbound International Payment', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_iso20022_2023', 'nacha_basic_2025'], icon: Icons.edit, correctedFields: const ['sec_code'], appliesTo: const ['outbound_international']),
]);
final _changeCodeByCode = _indexRecords(changeCodeRecords);
AchChangeCodeInfo? resolveChangeCode(String code, {bool includeInactive = false}) =>
    _resolve(_changeCodeByCode, code, referenceAsOf, includeInactive);
AchChangeCodeInfo? resolveChangeCodeAsOf(
  String code,
  DateTime on, {
  bool includeInactive = false,
}) => _resolve(_changeCodeByCode, code, on, includeInactive);
final Map<String, AchChangeCodeInfo> _changeCodeDefaultInfo = Map.unmodifiable({
  for (final code in _changeCodeByCode.keys)
    code: _resolve(_changeCodeByCode, code, referenceAsOf, true)!,
});
final Map<String, AchChangeCode> _changeCodeIdentityByCode = Map.unmodifiable({
  for (final value in AchChangeCode.values) value.code: value,
});
final List<AchChangeCodeInfo> currentChangeCodeRecords = List.unmodifiable(
  changeCodeRecords.where((record) => record.isEffective()),
);
final int changeCodeCount = _changeCodeByCode.length;
final int changeCodeRecordCount = changeCodeRecords.length;
final int currentChangeCodeCount = currentChangeCodeRecords.length;

final List<AchAddendaTypeCodeInfo> addendaTypeCodeRecords = List.unmodifiable([
  AchAddendaTypeCodeInfo(code: '01', name: 'Legacy Cross-Border Payment Information', status: AchCodeStatus.legacy, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.note_add, appliesTo: const ['CBR', 'PBR']),
  AchAddendaTypeCodeInfo(code: '02', name: 'Terminal Location Information', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.note_add, appliesTo: const ['MTE', 'POS', 'SHR']),
  AchAddendaTypeCodeInfo(code: '05', name: 'Payment-Related Information', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.note_add, appliesTo: const ['ACK', 'ATX', 'CCD', 'CIE', 'CTX', 'DNE', 'ENR', 'PPD', 'TRX', 'WEB']),
  AchAddendaTypeCodeInfo(code: '10', name: 'First Mandatory IAT Addenda', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'fedglobal_manual_2026'], icon: Icons.note_add, appliesTo: const ['IAT']),
  AchAddendaTypeCodeInfo(code: '11', name: 'Second Mandatory IAT Addenda', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'fedglobal_manual_2026'], icon: Icons.note_add, appliesTo: const ['IAT']),
  AchAddendaTypeCodeInfo(code: '12', name: 'Third Mandatory IAT Addenda', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'fedglobal_manual_2026'], icon: Icons.note_add, appliesTo: const ['IAT']),
  AchAddendaTypeCodeInfo(code: '13', name: 'Fourth Mandatory IAT Addenda', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'fedglobal_manual_2026'], icon: Icons.note_add, appliesTo: const ['IAT']),
  AchAddendaTypeCodeInfo(code: '14', name: 'Fifth Mandatory IAT Addenda', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'fedglobal_manual_2026'], icon: Icons.note_add, appliesTo: const ['IAT']),
  AchAddendaTypeCodeInfo(code: '15', name: 'Sixth Mandatory IAT Addenda', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'fedglobal_manual_2026'], icon: Icons.note_add, appliesTo: const ['IAT']),
  AchAddendaTypeCodeInfo(code: '16', name: 'Seventh Mandatory IAT Addenda', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'fedglobal_manual_2026'], icon: Icons.note_add, appliesTo: const ['IAT']),
  AchAddendaTypeCodeInfo(code: '17', name: 'IAT Remittance Information', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'fedglobal_manual_2026'], icon: Icons.note_add, appliesTo: const ['IAT']),
  AchAddendaTypeCodeInfo(code: '18', name: 'IAT Foreign Correspondent Bank Information', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025', 'fedglobal_manual_2026'], icon: Icons.note_add, appliesTo: const ['IAT']),
  AchAddendaTypeCodeInfo(code: '98', name: 'Notification of Change Information', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.note_add, appliesTo: const ['COR', 'refused_COR']),
  AchAddendaTypeCodeInfo(code: '99', name: 'Return Information', status: AchCodeStatus.current, validFrom: null, validTo: null, sources: const ['nacha_basic_2025'], icon: Icons.note_add, appliesTo: const ['return', 'dishonored_return', 'contested_return']),
]);
final _addendaTypeCodeByCode = _indexRecords(addendaTypeCodeRecords);
AchAddendaTypeCodeInfo? resolveAddendaTypeCode(String code, {bool includeInactive = false}) =>
    _resolve(_addendaTypeCodeByCode, code, referenceAsOf, includeInactive);
AchAddendaTypeCodeInfo? resolveAddendaTypeCodeAsOf(
  String code,
  DateTime on, {
  bool includeInactive = false,
}) => _resolve(_addendaTypeCodeByCode, code, on, includeInactive);
final Map<String, AchAddendaTypeCodeInfo> _addendaTypeCodeDefaultInfo = Map.unmodifiable({
  for (final code in _addendaTypeCodeByCode.keys)
    code: _resolve(_addendaTypeCodeByCode, code, referenceAsOf, true)!,
});
final Map<String, AchAddendaTypeCode> _addendaTypeCodeIdentityByCode = Map.unmodifiable({
  for (final value in AchAddendaTypeCode.values) value.code: value,
});
final List<AchAddendaTypeCodeInfo> currentAddendaTypeCodeRecords = List.unmodifiable(
  addendaTypeCodeRecords.where((record) => record.isEffective()),
);
final int addendaTypeCodeCount = _addendaTypeCodeByCode.length;
final int addendaTypeCodeRecordCount = addendaTypeCodeRecords.length;
final int currentAddendaTypeCodeCount = currentAddendaTypeCodeRecords.length;

final Map<String, List<AchReferenceInfo>> records = Map.unmodifiable({
  'transaction_codes': transactionCodeRecords,
  'return_codes': returnCodeRecords,
  'standard_entry_class_codes': standardEntryClassCodeRecords,
  'service_class_codes': serviceClassCodeRecords,
  'record_type_codes': recordTypeCodeRecords,
  'change_codes': changeCodeRecords,
  'addenda_type_codes': addendaTypeCodeRecords,
});

final Map<String, int> counts = Map.unmodifiable({
  'transaction_codes': transactionCodeCount,
  'return_codes': returnCodeCount,
  'standard_entry_class_codes': standardEntryClassCodeCount,
  'service_class_codes': serviceClassCodeCount,
  'record_type_codes': recordTypeCodeCount,
  'change_codes': changeCodeCount,
  'addenda_type_codes': addendaTypeCodeCount,
});
