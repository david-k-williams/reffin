// Generated PaymentTransactionStatusCode. Do not edit by hand.
// Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
// ignore_for_file: require_trailing_commas
part of 'generated.dart';

enum PaymentTransactionStatusCode {
  accc('ACCC'),
  accp('ACCP'),
  acfc('ACFC'),
  acfw('ACFW'),
  acis('ACIS'),
  acpd('ACPD'),
  acsc('ACSC'),
  acsp('ACSP'),
  actc('ACTC'),
  acwc('ACWC'),
  acwp('ACWP'),
  blck('BLCK'),
  canc('CANC'),
  cpuc('CPUC'),
  patc('PATC'),
  pdng('PDNG'),
  pres('PRES'),
  rcvc('RCVC'),
  rcvd('RCVD'),
  rjct('RJCT'),
  rvcm('RVCM'),
  rvmc('RVMC'),
  rvna('RVNA'),
  rvnc('RVNC'),
  rvnm('RVNM');

  const PaymentTransactionStatusCode(this.code);
  final String code;
  Iso20022CodeInfo get info => resolveCode('ExternalPaymentTransactionStatus1Code', code)!;
  String get label => info.label;
  IconData get icon => info.icon;
  static PaymentTransactionStatusCode? tryParse(String code) =>
      _paymentTransactionStatusByCode[_key(code)];
}

final Map<String, PaymentTransactionStatusCode> _paymentTransactionStatusByCode = Map.unmodifiable(<String, PaymentTransactionStatusCode>{
  for (final value in PaymentTransactionStatusCode.values) _key(value.code): value,
});
