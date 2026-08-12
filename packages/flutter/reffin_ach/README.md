# reffin_ach

Typed, offline ACH reference codes for Flutter. The package provides enum-like
code identities, structured metadata, lifecycle-aware resolvers, and native
Material icons without a runtime API call.

## Included code families

- transaction codes;
- return reason codes;
- Standard Entry Class (SEC) codes;
- service class codes;
- record type codes;
- Notification of Change codes; and
- addenda type codes.

Codes remain strings, preserving values such as `01`, `22`, and `R01`.
Resolvers trim input, ignore ASCII letter case, and return `null` for unknown
values. Planned and legacy records are excluded by default. Each family also
has an `AsOf` resolver for date-aware lookup and an `includeInactive` option
when historical or planned metadata is needed explicitly.

The snapshot is referenced to August 11, 2026. Its lifecycle metadata keeps the
planned `R90` return code and the March 17, 2028 change to `R16` separate from
the records effective on the reference date.

## Getting started

The package requires Dart 3.8 or later and Flutter. Add it with:

```sh
flutter pub add reffin_ach
```

## Usage

```dart
import 'package:flutter/material.dart';
import 'package:reffin_ach/reffin_ach.dart';

Widget returnCodeTile(String input) {
  final info = resolveReturnCode(input);
  if (info == null) {
    return Text('Unknown ACH return code: $input');
  }

  return ListTile(
    leading: Icon(info.icon),
    title: Text('${info.code}: ${info.name}'),
    subtitle: Text(info.category),
  );
}

final futureR90 = resolveReturnCodeAsOf(
  'R90',
  DateTime.utc(2028, 3, 17),
);
```

Known identities are also available as enums:

```dart
final checkingCredit = AchTransactionCode.code22;

checkingCredit.code;           // "22"
checkingCredit.label;          // "Checking Credit"
checkingCredit.info.direction; // "credit"
checkingCredit.icon;           // native IconData
```

See the [complete Flutter example](example/reffin_ach_example.dart).

## Data scope and limitations

This is a decoding and display reference. It does not determine whether an ACH
entry is authorized, eligible, timely, compliant, or correctly formatted. It
does not replace the current Nacha Operating Rules, an ACH operator's
requirements, or an institution's processing agreement.

The package contains compact functional identifiers, independently worded
labels, structural facets, source keys, statuses, and effective dates. It
deliberately omits rulebook prose, authorization requirements, return
timeframes, warranties, and processing instructions.

For the source inventory, transformations, counts, and rights boundary, read
the [ACH provenance](https://github.com/david-k-williams/reffin/blob/main/data/ach/README.md),
[data notices](https://github.com/david-k-williams/reffin/blob/main/data/NOTICE.md),
and [data policy](https://github.com/david-k-williams/reffin/blob/main/docs/data-policy.md).

The generated catalog exposes `dataFingerprint` so applications and release
tooling can identify the exact normalized-input snapshot. Generated Dart files
should not be edited by hand.
