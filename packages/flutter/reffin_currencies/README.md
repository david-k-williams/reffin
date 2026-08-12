# reffin_currencies

Typed, offline currency reference data for Dart, generated from Unicode CLDR
48.2.

## Features

- 307 current and historical currency identifiers with English display names.
- Case-insensitive lookup by three-letter currency code.
- Symbols, minor-unit digits, cash digits and rounding increments.
- CLDR status and territory associations.
- Deterministic, in-process lookups with no runtime API or file access.
- A SHA-256 `dataFingerprint` for identifying the generated snapshot.

## Getting started

The package requires Dart 3.8 or later and has no Flutter dependency. Add it
with:

```sh
dart pub add reffin_currencies
```

## Usage

```dart
import 'package:reffin_currencies/reffin_currencies.dart';

void main() {
  final currency = Currency.tryParse('chf');
  if (currency == null) {
    return;
  }

  print(currency.label); // Swiss Franc
  print(currency.displaySymbol); // CHF
  print(currency.minorDigits); // 2
  print(currency.cashDigits); // 2
  print(currency.cashRounding); // 5, meaning 0.05 at two cash digits

  print(resolveCurrency('not-a-code')); // null
}
```

Use `Currency.tryParse` or the equivalent `resolveCurrency` function for codes
from external data. Both normalize the input to uppercase and return `null` for
an unknown code. Generated enum member names are Dart-safe identifiers, so a
code such as `TRY` is most reliably accessed through lookup.

Each `Currency` exposes:

| Field | Meaning |
| --- | --- |
| `code`, `label` | CLDR currency code and English display name |
| `symbol`, `narrowSymbol` | Nullable CLDR symbol forms |
| `displaySymbol` | Narrow symbol, then symbol, then code as a fallback |
| `minorDigits`, `minorRounding` | Standard fraction digits and rounding increment |
| `cashDigits`, `cashRounding` | Cash fraction digits and rounding increment |
| `isActive` | Whether CLDR 48.2 marks the identifier `regular` |
| `territories` | All CLDR territory associations recorded for the currency |

Rounding values are increments in the least-significant displayed digit. For
example, `cashDigits == 2` and `cashRounding == 5` represent `0.05`.

## Data semantics and licensing

The snapshot is derived from Unicode CLDR 48.2 under the
[Unicode License v3](https://www.unicode.org/license.txt). Redistributed copies
must retain Unicode's applicable copyright and permission notice.

`isActive` reflects CLDR validity status in this pinned snapshot; it is not a
live legal-tender determination. Territory associations include historical
associations and do not retain dates or tender flags.

## Additional information

The package is generated from normalized source data. Do not edit
`lib/src/generated.dart` by hand. See the
[currency provenance](https://github.com/david-k-williams/reffin/blob/main/data/currencies/README.md),
[data notices](https://github.com/david-k-williams/reffin/blob/main/data/NOTICE.md),
and [data policy](https://github.com/david-k-williams/reffin/blob/main/docs/data-policy.md)
for the pinned source, checksums, transformation, and distribution boundaries.

The complete runnable example is in
[`example/reffin_currencies_example.dart`](example/reffin_currencies_example.dart).
Issues and contributions are tracked in the
[Reffin repository](https://github.com/david-k-williams/reffin).
