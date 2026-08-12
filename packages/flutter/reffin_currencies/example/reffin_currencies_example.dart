import 'package:reffin_currencies/reffin_currencies.dart';

void main() {
  for (final code in <String>['USD', 'JPY', 'CHF']) {
    final currency = resolveCurrency(code);
    if (currency == null) {
      continue;
    }

    print(
      '${currency.code}: ${currency.label}; '
      'symbol=${currency.displaySymbol}; '
      'minorDigits=${currency.minorDigits}; '
      'cashRounding=${currency.cashRounding}',
    );
  }

  print('Unknown code: ${resolveCurrency('not-a-code')}');
}
