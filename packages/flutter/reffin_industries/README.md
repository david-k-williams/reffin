# reffin_industries

Typed, offline U.S. industry reference data for Flutter. The package contains
the complete 2022 U.S. NAICS hierarchy and a separate historical SIC-coded
lookup derived from the Bureau of Labor Statistics QCEW table. Both include
safe resolvers, parent/child traversal, and native Material icons.

## Included data

- 2,125 U.S. 2022 NAICS records from sectors through six-digit national
  industries;
- 20 project-authored sector identities with descriptions and Material icons;
- 1,524 historical SIC-coded BLS/QCEW records;
- 12 project-authored SIC division identities with descriptions and Material
  icons; and
- immutable collections plus a normalized-input fingerprint.

Codes remain strings, preserving leading zeroes such as SIC `0111` and combined
NAICS sectors such as `31-33`. Lookups are exact and return `null` for unknown
codes; child lookups return an empty list.

## Getting started

The package requires Dart 3.8 or later and Flutter. Add it with:

```sh
flutter pub add reffin_industries
```

## Usage

```dart
import 'package:flutter/material.dart';
import 'package:reffin_industries/reffin_industries.dart';

Widget industryTile(String naicsCode) {
  final industry = resolveIndustry(naicsCode);
  if (industry == null) {
    return Text('Unknown NAICS code: $naicsCode');
  }

  return ListTile(
    leading: Icon(industry.icon),
    title: Text('${industry.code}: ${industry.title}'),
    subtitle: Text(industry.sector.label),
  );
}

final software = resolveIndustry('513210');
final softwareParent = software?.parent;       // NAICS 51321
final manufacturing = childrenOf('31-33');    // direct child records

final wheat = resolveSic('0111');
final wheatDivision = wheat?.division;         // Agriculture, Forestry, and Fishing
```

Explicit NAICS aliases are available as `NaicsIndustry`, `NaicsLevel`,
`NaicsSector`, `naicsIndustries`, `resolveNaics`, and `childrenOfNaics`.

See the [complete Flutter example](example/reffin_industries_example.dart).

## Data scope and limitations

The NAICS snapshot is the U.S. Census Bureau's 2022 structure. It does not
combine the separate Canadian or Mexican NAICS publications. Sector IDs,
descriptions, and icons are Reffin presentation metadata rather than Census
fields.

The SIC lookup is historical. It contains the 1987 four-digit code set together
with BLS hierarchy containers and eight QCEW rollups after rows explicitly
marked `1972 SIC` were removed. It is not a current classification and must not
be presented as the canonical 1987 SIC-manual hierarchy. Use `SicLevel` to
distinguish ordinary industries from `qcewRollup` records.

For upstream attribution, transformations, hashes, and exact hierarchy notes,
read the [industry provenance](https://github.com/david-k-williams/reffin/blob/main/data/industries/README.md),
[data notices](https://github.com/david-k-williams/reffin/blob/main/data/NOTICE.md),
and [data policy](https://github.com/david-k-williams/reffin/blob/main/docs/data-policy.md).

The generated catalog exposes `dataFingerprint` so applications and release
tooling can identify the exact normalized-input snapshot. Generated Dart files
should not be edited by hand.
