// Generated PaymentGroupStatusCode. Do not edit by hand.
// Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
// ignore_for_file: require_trailing_commas
part of 'generated.dart';

enum PaymentGroupStatusCode {
  accc('ACCC'),
  accp('ACCP'),
  acsc('ACSC'),
  acsp('ACSP'),
  actc('ACTC'),
  acwc('ACWC'),
  part('PART'),
  pdng('PDNG'),
  rcvc('RCVC'),
  rcvd('RCVD'),
  rjct('RJCT'),
  rvcm('RVCM'),
  rvnc('RVNC');

  const PaymentGroupStatusCode(this.code);
  final String code;
  Iso20022CodeInfo get info => resolveCode('ExternalPaymentGroupStatus1Code', code)!;
  String get label => info.label;
  IconData get icon => info.icon;
  static PaymentGroupStatusCode? tryParse(String code) =>
      _paymentGroupStatusByCode[_key(code)];
}

final Map<String, PaymentGroupStatusCode> _paymentGroupStatusByCode = Map.unmodifiable(<String, PaymentGroupStatusCode>{
  for (final value in PaymentGroupStatusCode.values) _key(value.code): value,
});
