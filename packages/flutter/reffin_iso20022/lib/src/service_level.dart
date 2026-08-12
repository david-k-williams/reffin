// Generated ServiceLevelCode. Do not edit by hand.
// Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
// ignore_for_file: require_trailing_commas
part of 'generated.dart';

enum ServiceLevelCode {
  bktr('BKTR'),
  eaps('EAPS'),
  eolo('EOLO'),
  g001('G001'),
  g002('G002'),
  g003('G003'),
  g004('G004'),
  g005('G005'),
  g006('G006'),
  g007('G007'),
  g009('G009'),
  inst('INST'),
  irca('IRCA'),
  nolo('NOLO'),
  npca('NPCA'),
  nugp('NUGP'),
  nurg('NURG'),
  prpt('PRPT'),
  sd01('SD01'),
  sdva('SDVA'),
  sepa('SEPA'),
  spli('SPLI'),
  spsc('SPSC'),
  srtp('SRTP'),
  svat('SVAT'),
  svde('SVDE'),
  urgp('URGP'),
  urns('URNS'),
  wfsm('WFSM');

  const ServiceLevelCode(this.code);
  final String code;
  Iso20022CodeInfo get info => resolveCode('ExternalServiceLevel1Code', code)!;
  String get label => info.label;
  IconData get icon => info.icon;
  static ServiceLevelCode? tryParse(String code) =>
      _serviceLevelByCode[_key(code)];
}

final Map<String, ServiceLevelCode> _serviceLevelByCode = Map.unmodifiable(<String, ServiceLevelCode>{
  for (final value in ServiceLevelCode.values) _key(value.code): value,
});
