# reffin_cards

Provider-neutral card and payment reference vocabularies for Flutter, available
offline as typed enums with native Material icons.

## Features

- 68 values across eight compact normalization vocabularies.
- Stable lowercase `snake_case` IDs and safe `tryParse` lookups.
- Human-readable labels and descriptions.
- Native Flutter `IconData` using generic Material icons.
- Optional application-owned brand asset keys for card networks; no logos are
  bundled.
- Deterministic record collections, counts, and a SHA-256 `dataFingerprint`.

## Getting started

The package requires Dart 3.8 or later and Flutter because its generated values
expose Material icons. Add it with:

```sh
flutter pub add reffin_cards
```

## Usage

```dart
import 'package:flutter/material.dart';
import 'package:reffin_cards/reffin_cards.dart';

Widget normalizedCardSummary() {
  final network = CardNetwork.tryParse('visa') ?? CardNetwork.unknown;
  final funding = FundingType.tryParse('credit') ?? FundingType.unknown;

  return ListTile(
    leading: Icon(network.icon),
    title: Text(network.label),
    subtitle: Text('${funding.label}: ${funding.description}'),
  );
}
```

`tryParse` accepts a stable Reffin ID and returns `null` when it is not in the
vocabulary. Use the explicit `unknown` value when the source value is missing
or cannot be determined, and `other` when it is known but outside the named
values. Preserve the original provider value alongside the normalized value.

The public vocabularies are:

| Enum | Represents |
| --- | --- |
| `CardNetwork` | Descriptive network names and optional app asset keys |
| `FormFactor` | Physical or virtual credential presentation |
| `FundingType` | How card value is funded or repaid |
| `PaymentMethodFamily` | High-level tender families |
| `PaymentOutcome` | Coarse payment or authorization outcomes |
| `ProductClass` | Broad intended cardholder or program classes |
| `TransactionChannel` | Customer interaction surfaces |
| `VerificationOutcome` | Generic verification results |

Each enum exposes `id`, `label`, and `icon`; all except `CardNetwork` also
expose `description`. A network's nullable `brandAssetKey` is only a lookup key
for an asset that the application separately supplies and licenses. Always
retain the generic `icon` fallback.

The package also exports typed record lists and counts for each vocabulary,
plus aggregate `records` and `counts` maps.

## Scope and interpretation

These values normalize application terminology. They do not encode card-scheme
acceptance, routing, authentication, risk, settlement, dispute, or approval
rules. The package deliberately includes no logos, BIN/IIN ranges, PAN-prefix
detection, or full-PAN handling.

Network and product names may be trademarks of their owners. Their descriptive
inclusion and the presence of a `brandAssetKey` do not grant permission to use
a mark or imply affiliation or endorsement.

## Additional information

The package is generated from normalized source data. Do not edit
`lib/src/generated.dart` by hand. See the
[card vocabulary notes](https://github.com/david-k-williams/reffin/blob/main/data/cards/README.md),
[data notices](https://github.com/david-k-williams/reffin/blob/main/data/NOTICE.md),
and [data policy](https://github.com/david-k-williams/reffin/blob/main/docs/data-policy.md)
for stability rules, provenance, and interpretation boundaries.

The complete Flutter example is in
[`example/reffin_cards_example.dart`](example/reffin_cards_example.dart).
Issues and contributions are tracked in the
[Reffin repository](https://github.com/david-k-williams/reffin).
