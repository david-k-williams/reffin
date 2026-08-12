import 'package:reffin_currencies/reffin_currencies.dart';
import 'package:test/test.dart';

void main() {
  test('resolves currency metadata offline', () {
    expect(Currency.tryParse('usd'), Currency.usd);
    expect(Currency.usd.minorDigits, 2);
    expect(Currency.usd.displaySymbol, r'$');
    expect(cldrVersion, '48.2');
    expect(Currency.usd.territories, contains('US'));
    expect(Currency.jpy.minorDigits, 0);
    expect(Currency.chf.cashRounding, 5);
  });

  test('preserves historic currencies and safe unknowns', () {
    expect(Currency.dem.isActive, isFalse);
    expect(resolveCurrency('NOPE'), isNull);
  });
}
