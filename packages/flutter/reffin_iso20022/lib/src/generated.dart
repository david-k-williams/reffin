// Generated offline ISO 20022 catalogs. Do not edit by hand.
// Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
// ignore_for_file: require_trailing_commas

import 'package:flutter/material.dart';

part 'data/code_sets_00.dart';
part 'data/external_codes_00.dart';
part 'data/external_codes_01.dart';
part 'data/external_codes_02.dart';
part 'data/external_codes_03.dart';
part 'data/external_codes_04.dart';
part 'data/external_codes_05.dart';
part 'data/external_codes_06.dart';
part 'data/external_codes_07.dart';
part 'data/external_codes_08.dart';
part 'data/external_codes_09.dart';
part 'data/external_codes_10.dart';
part 'data/external_codes_11.dart';
part 'data/external_codes_12.dart';
part 'data/external_codes_13.dart';
part 'data/external_codes_14.dart';
part 'data/external_codes_15.dart';
part 'data/external_codes_16.dart';
part 'data/external_codes_17.dart';
part 'data/external_codes_18.dart';
part 'data/external_codes_19.dart';
part 'data/bank_transaction_codes_00.dart';
part 'data/bank_transaction_codes_01.dart';
part 'data/bank_transaction_codes_02.dart';
part 'data/bank_transaction_codes_03.dart';
part 'data/message_definitions_00.dart';
part 'data/message_definitions_01.dart';
part 'payment_purpose.dart';
part 'payment_status_reason.dart';
part 'payment_return_reason.dart';
part 'local_instrument.dart';
part 'category_purpose.dart';
part 'service_level.dart';
part 'payment_transaction_status.dart';
part 'payment_group_status.dart';

const String dataFingerprint = '19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80';
// ignore: constant_identifier_names
const String DATA_FINGERPRINT = dataFingerprint;
const String externalCodeSetsVersion = 'May 2026 v1';
const String externalCodeSetsArtifactVersion = '1Q2026_externalcodesets_v1';
const String bankTransactionCodesVersion = '2025-11-30';
const String messageDefinitionsVersion = '2026-06-26';

enum Iso20022CodeStatus { registered, obsolete }

final class Iso20022CodeSetInfo {
  const Iso20022CodeSetInfo({required this.codeSet, required this.definition, required this.status, required this.sources});
  final String codeSet; final String definition; final String status; final List<String> sources;
  bool get isCurrent => status != 'obsolete';
}

final class Iso20022CodeInfo {
  const Iso20022CodeInfo({
    required this.codeSet, required this.code, required this.name, required this.label,
    required this.definition, required this.requester, required this.status,
    required this.lastUpdated, required this.creationDate, required this.replacedBy,
    required this.mappingStandard1, required this.mappingValue1,
    required this.mappingStandard2, required this.mappingValue2,
    required this.additionalInformation, required this.sources, required this.icon,
  });
  final String codeSet; final String code; final String name; final String label; final String definition;
  final String? requester; final Iso20022CodeStatus status; final DateTime? lastUpdated; final DateTime? creationDate;
  final String? replacedBy; final String? mappingStandard1; final String? mappingValue1;
  final String? mappingStandard2; final String? mappingValue2; final String? additionalInformation;
  final List<String> sources; final IconData icon;
  bool get isCurrent => status == Iso20022CodeStatus.registered;
}

final class BankTransactionCodeInfo {
  const BankTransactionCodeInfo({required this.domainCode, required this.domainName, required this.familyCode, required this.familyName, required this.subfamilyCode, required this.subfamilyName, required this.status, required this.statusDate});
  final String domainCode; final String domainName; final String familyCode; final String familyName;
  final String subfamilyCode; final String subfamilyName; final String status; final DateTime statusDate;
  String get code => '$domainCode-$familyCode-$subfamilyCode';
}

final class MessageDefinitionInfo {
  const MessageDefinitionInfo({required this.businessArea, required this.messageId, required this.messageNumber, required this.variant, required this.version, required this.name});
  final String businessArea; final String messageId; final String messageNumber; final String variant;
  final String version; final String name;
}

const List<List<String>> _codeSetsRows = <List<String>>[..._codeSetsRows00];
const List<List<String>> _externalCodesRows = <List<String>>[..._externalCodesRows00, ..._externalCodesRows01, ..._externalCodesRows02, ..._externalCodesRows03, ..._externalCodesRows04, ..._externalCodesRows05, ..._externalCodesRows06, ..._externalCodesRows07, ..._externalCodesRows08, ..._externalCodesRows09, ..._externalCodesRows10, ..._externalCodesRows11, ..._externalCodesRows12, ..._externalCodesRows13, ..._externalCodesRows14, ..._externalCodesRows15, ..._externalCodesRows16, ..._externalCodesRows17, ..._externalCodesRows18, ..._externalCodesRows19];
const List<List<String>> _bankTransactionCodesRows = <List<String>>[..._bankTransactionCodesRows00, ..._bankTransactionCodesRows01, ..._bankTransactionCodesRows02, ..._bankTransactionCodesRows03];
const List<List<String>> _messageDefinitionsRows = <List<String>>[..._messageDefinitionsRows00, ..._messageDefinitionsRows01];

String? _optional(String value) => value.isEmpty ? null : value;
DateTime? _date(String value) => value.isEmpty ? null : DateTime.parse(value);
List<String> _sources(String value) => List.unmodifiable(value.split('|').where((item) => item.isNotEmpty));
String _key(String value) => value.trim().toLowerCase();
String _composite(Iterable<String> values) => values.map(_key).join('\u0000');
IconData _iconForSet(String codeSet) => switch (codeSet) {
    'ExternalPurpose1Code' => Icons.payments,
    'ExternalStatusReason1Code' => Icons.error_outline,
    'ExternalReturnReason1Code' => Icons.undo,
    'ExternalLocalInstrument1Code' => Icons.account_balance,
    'ExternalCategoryPurpose1Code' => Icons.category,
    'ExternalServiceLevel1Code' => Icons.speed,
    'ExternalPaymentTransactionStatus1Code' => Icons.sync,
    'ExternalPaymentGroupStatus1Code' => Icons.fact_check,
    _ => Icons.code,
  };

final List<Iso20022CodeSetInfo> codeSets = List.unmodifiable(_codeSetsRows.map((row) => Iso20022CodeSetInfo(
  codeSet: row[0], definition: row[1], status: row[2], sources: _sources(row[3]),
)));
final List<Iso20022CodeInfo> externalCodeRecords = List.unmodifiable(_externalCodesRows.map((row) => Iso20022CodeInfo(
  codeSet: row[0], code: row[1], name: row[2], label: row[3], definition: row[4], requester: _optional(row[5]),
  status: Iso20022CodeStatus.values.byName(row[6]), lastUpdated: _date(row[7]), creationDate: _date(row[8]),
  replacedBy: _optional(row[9]), mappingStandard1: _optional(row[10]), mappingValue1: _optional(row[11]),
  mappingStandard2: _optional(row[12]), mappingValue2: _optional(row[13]), additionalInformation: _optional(row[14]),
  sources: _sources(row[15]), icon: _iconForSet(row[0]),
)));
final List<Iso20022CodeInfo> currentExternalCodes = List.unmodifiable(externalCodeRecords.where((item) => item.isCurrent));
final List<BankTransactionCodeInfo> bankTransactionCodeRecords = List.unmodifiable(_bankTransactionCodesRows.map((row) => BankTransactionCodeInfo(
  domainCode: row[0], domainName: row[1], familyCode: row[2], familyName: row[3],
  subfamilyCode: row[4], subfamilyName: row[5], status: row[6], statusDate: DateTime.parse(row[7]),
)));
final List<MessageDefinitionInfo> messageDefinitions = List.unmodifiable(_messageDefinitionsRows.map((row) => MessageDefinitionInfo(
  businessArea: row[0], messageId: row[1], messageNumber: row[2], variant: row[3], version: row[4],
  name: row[5],
)));

final int codeSetCount = codeSets.length;
final int externalCodeRecordCount = externalCodeRecords.length;
final int currentExternalCodeCount = currentExternalCodes.length;
final int externalCodeIdentityCount = externalCodeRecords.map((item) => _composite([item.codeSet, item.code])).toSet().length;
final int bankTransactionCodeRecordCount = bankTransactionCodeRecords.length;
final int bankTransactionCodeIdentityCount = bankTransactionCodeRecords.map((item) => _composite([item.domainCode, item.familyCode, item.subfamilyCode])).toSet().length;
final int messageDefinitionCount = messageDefinitions.length;
const int paymentCodeCount = 950;

final Map<String, Iso20022CodeSetInfo> _codeSetByName = Map.unmodifiable({for (final item in codeSets) _key(item.codeSet): item});
final Map<String, List<Iso20022CodeInfo>> _externalByKey = _indexExternal((item) => _composite([item.codeSet, item.code]));
final Map<String, List<Iso20022CodeInfo>> _externalByCode = _indexExternal((item) => _key(item.code));
Map<String, List<Iso20022CodeInfo>> _indexExternal(String Function(Iso20022CodeInfo) selector) {
  final mutable = <String, List<Iso20022CodeInfo>>{};
  for (final item in externalCodeRecords) { mutable.putIfAbsent(selector(item), () => []).add(item); }
  return Map.unmodifiable({for (final entry in mutable.entries) entry.key: List<Iso20022CodeInfo>.unmodifiable(entry.value)});
}
Iso20022CodeSetInfo? resolveCodeSet(String codeSet, {bool includeObsolete = false}) {
  final item = _codeSetByName[_key(codeSet)]; return item != null && (includeObsolete || item.isCurrent) ? item : null;
}
List<Iso20022CodeInfo> recordsFor(String codeSet, String code, {bool includeObsolete = false}) {
  final values = _externalByKey[_composite([codeSet, code])] ?? const <Iso20022CodeInfo>[];
  return includeObsolete ? values : List.unmodifiable(values.where((item) => item.isCurrent));
}
Iso20022CodeInfo? resolveCode(String codeSet, String code, {bool includeObsolete = false}) {
  final current = recordsFor(codeSet, code); if (current.isNotEmpty) return current.first;
  if (!includeObsolete) return null; final history = recordsFor(codeSet, code, includeObsolete: true);
  return history.isEmpty ? null : history.first;
}
List<Iso20022CodeInfo> findCodes(String code, {bool includeObsolete = false}) {
  final values = _externalByCode[_key(code)] ?? const <Iso20022CodeInfo>[];
  return includeObsolete ? values : List.unmodifiable(values.where((item) => item.isCurrent));
}
List<Iso20022CodeInfo> searchCodes(String query, {String? codeSet, bool includeObsolete = false, int? limit}) {
  final needle = _key(query); if (needle.isEmpty || (limit != null && limit <= 0)) return const [];
  final setKey = codeSet == null ? null : _key(codeSet); final found = <Iso20022CodeInfo>[];
  for (final item in externalCodeRecords) {
    if (!includeObsolete && !item.isCurrent) continue; if (setKey != null && _key(item.codeSet) != setKey) continue;
    final text = [item.code, item.name, item.label, item.definition, item.additionalInformation ?? ''].join('\n').toLowerCase();
    if (text.contains(needle)) { found.add(item); if (limit != null && found.length >= limit) break; }
  } return List.unmodifiable(found);
}

final Map<String, List<BankTransactionCodeInfo>> _btcByKey = _indexBtc();
Map<String, List<BankTransactionCodeInfo>> _indexBtc() {
  final mutable = <String, List<BankTransactionCodeInfo>>{}; for (final item in bankTransactionCodeRecords) {
    mutable.putIfAbsent(_composite([item.domainCode, item.familyCode, item.subfamilyCode]), () => []).add(item);
  } return Map.unmodifiable({for (final entry in mutable.entries) entry.key: List<BankTransactionCodeInfo>.unmodifiable(entry.value)});
}
List<BankTransactionCodeInfo> resolveBankTransactionCode(String domainCode, String familyCode, String subfamilyCode) =>
  _btcByKey[_composite([domainCode, familyCode, subfamilyCode])] ?? const [];
List<BankTransactionCodeInfo> findBankTransactionCodes(String domainCode, {String? familyCode, String? subfamilyCode}) {
  final domain = _key(domainCode); final family = familyCode == null ? null : _key(familyCode);
  final subfamily = subfamilyCode == null ? null : _key(subfamilyCode);
  return List.unmodifiable(bankTransactionCodeRecords.where((item) => _key(item.domainCode) == domain
    && (family == null || _key(item.familyCode) == family) && (subfamily == null || _key(item.subfamilyCode) == subfamily)));
}

final Map<String, MessageDefinitionInfo> _messageById = Map.unmodifiable({for (final item in messageDefinitions) _key(item.messageId): item});
MessageDefinitionInfo? resolveMessageIdentifier(String messageId) => _messageById[_key(messageId)];
List<MessageDefinitionInfo> findMessageDefinitions({String? businessArea, String? messageNumber}) {
  final area = businessArea == null ? null : _key(businessArea); final number = messageNumber == null ? null : _key(messageNumber);
  return List.unmodifiable(messageDefinitions.where((item) => (area == null || _key(item.businessArea) == area)
    && (number == null || _key(item.messageNumber) == number)));
}
