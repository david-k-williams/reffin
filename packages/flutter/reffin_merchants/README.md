# reffin_merchants

Typed, offline Merchant Category Code (MCC) reference data for Flutter. The
package keeps each source's terminology separate, preserves leading zeroes, and
adds broad presentation groups and native Material icons.

## Features

- Typed `Mcc`, `MccVendor`, and `MccGroup` values.
- Vendor-specific lookup by MCC or a vendor's category key.
- Safe `null` or empty-list results for unknown input.
- Generic Material icons for presentation; no brand artwork.
- Source metadata and a SHA-256 input fingerprint for auditing data drift.

## Getting started

The package requires Dart 3.8 or later and Flutter. Add it with:

```sh
flutter pub add reffin_merchants
```

## Usage

Keep MCCs as four-character strings so leading zeroes survive:

```dart
import 'package:reffin_merchants/reffin_merchants.dart';

final restaurant = resolveMcc('5812', MccVendor.visa);
if (restaurant != null) {
  print(restaurant.name);        // Eating Places and Restaurants
  print(restaurant.group.label); // Food and Drink
}

final veterinary = Mcc.tryParse('0742')?.resolve(MccVendor.visa);
final stripeCategory = resolveVendorKey(
  MccVendor.stripe,
  'eating_places_restaurants',
);
final vendorViews = recordsForMcc('5812');
```

`MccDetails.icon` returns native Flutter `IconData`, so records can be rendered
without a separate icon mapping:

```dart
Icon(restaurant!.icon, semanticLabel: restaurant.name);
```

See [`example/reffin_merchants_example.dart`](example/reffin_merchants_example.dart)
for a small Flutter example.

## Data model

Vendor wording and coverage differ. Pass an explicit `MccVendor` rather than
treating one source as a universal MCC definition. `MccDetails.source` exposes
the provenance record used for a result, while `dataFingerprint` identifies the
complete generated input snapshot.

The broad groups and icons are Reffin presentation metadata. They do not
determine interchange, rewards, eligibility, routing, merchant risk, or
regulatory treatment. Applications should retain their original provider value
alongside normalized data.

For the source inventory and redistribution status, read the
[data policy](https://github.com/david-k-williams/reffin/blob/main/docs/data-policy.md)
and [data notices](https://github.com/david-k-williams/reffin/blob/main/data/NOTICE.md).

## Generation

This library is generated from committed CSV inputs. Do not edit
`lib/src/generated.dart` by hand. From the repository root, regenerate or check
the snapshot with:

```sh
python3 tools/generate.py merchants
python3 tools/generate.py --check
```

Reffin is not an official publication of any card network or source vendor.
