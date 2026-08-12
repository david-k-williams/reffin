# Reffin

Reffin is a monorepo of typed, offline reference data for payments and finance.
One set of normalized CSV inputs generates independent Python, TypeScript, and
Dart/Flutter packages. Applications get enum-like values, safe resolvers,
display metadata, and deterministic results without a runtime API call.

The current committed data snapshot has been reviewed and approved for public
repository distribution. Public package-registry releases remain separately
gated so each artifact carries the correct licenses, notices, provenance, and
release metadata.

## Reference domains

| Domain | Contents | Source basis | Current size |
| --- | --- | --- | ---: |
| Merchants | Vendor-aware MCC names, broad presentation groups, and icons | Adyen DABstep; Stripe Issuing; Visa MDS; pinned python-iso18245 views | 992 MCCs; 4,970 vendor rows |
| Cards | Provider-neutral card, payment-method, channel, and outcome vocabularies | Project-authored | 68 values in eight vocabularies |
| Currencies | Names, symbols, minor and cash units, status, and territory associations | Unicode CLDR 48.2 | 307 currencies |
| Industries | Current U.S. NAICS hierarchy plus a separate historical SIC lookup | Census 2022 NAICS and BLS QCEW SIC | 2,125 NAICS rows; 1,524 SIC rows |
| ACH | Transaction, return, SEC, service-class, record-type, NOC/change, and addenda-type codes | Public Nacha materials; Federal Reserve, archived Treasury, and industry cross-checks | 166 distinct identifiers; 164 current today, 1 future-only, 1 historical |
| ISO 20022 | External payment code sets, generic catalog search, Bank Transaction Codes, and message identifiers | ISO 20022 Repository | Pinned May 2026 external-code snapshot plus separately versioned catalogs |

MCC, NAICS, SIC, and ACH codes remain strings. This preserves leading zeroes
such as MCC `0742`, SIC `0111`, ACH addenda type `02`, and combined NAICS
sectors such as `31-33`.

## Package names

Each domain is an independent artifact. These are the names in the local
manifests; they do not imply that a package is currently available from a
public registry.

| Domain | Python distribution / import | npm | Dart/Flutter |
| --- | --- | --- | --- |
| Merchants | `reffin-merchants` / `reffin_merchants` | `@reffin/merchants` | `reffin_merchants` |
| Cards | `reffin-cards` / `reffin_cards` | `@reffin/cards` | `reffin_cards` |
| Currencies | `reffin-currencies` / `reffin_currencies` | `@reffin/currencies` | `reffin_currencies` |
| Industries | `reffin-industries` / `reffin_industries` | `@reffin/industries` | `reffin_industries` |
| ACH | `reffin-ach` / `reffin_ach` | `@reffin/ach` | `reffin_ach` |
| ISO 20022 | `reffin-iso20022` / `reffin_iso20022` | `@reffin/iso20022` | `reffin_iso20022` |

See the [package guide](packages/README.md) for the generated API surfaces and
repository paths.

## API examples

These examples show the local package APIs.

Python:

```python
from reffin_ach import AchReturnCode, AchTransactionCode
from reffin_cards import CardNetwork
from reffin_currencies import Currency
from reffin_industries import resolve_industry
from reffin_iso20022 import PaymentPurposeCode
from reffin_merchants import Mcc, MccVendor

software = resolve_industry("513210")
restaurant = Mcc.MCC_5812.resolve(MccVendor.STRIPE)
assert software is not None and restaurant is not None

AchTransactionCode.CODE_22.info.name             # "Checking Credit"
AchReturnCode.R22.info.name                      # "Invalid Individual ID Number"
PaymentPurposeCode.SALA.label                    # "Salary Payment"
CardNetwork.VISA.material_symbol                 # "credit_card"
Currency.USD.display_symbol                      # "$"
software.sector.material_symbol                  # "language"
restaurant.name                                  # "Eating Places, Restaurants"
```

TypeScript:

```ts
import { AchReturnCode, AchTransactionCode } from "@reffin/ach";
import { CardNetwork } from "@reffin/cards";
import { Currency, resolveCurrency } from "@reffin/currencies";
import { sectorForIndustry } from "@reffin/industries";
import { PaymentPurposeCode } from "@reffin/iso20022";
import { MccVendor, materialSymbolForMcc } from "@reffin/merchants";

AchTransactionCode.Code22.name;                         // "Checking Credit"
AchReturnCode.R22.name;                                 // "Invalid Individual ID Number"
PaymentPurposeCode.SALA.label;                          // "Salary Payment"
CardNetwork.Visa.materialSymbol;                         // "credit_card"
resolveCurrency(Currency.USD)?.displaySymbol;            // "$"
sectorForIndustry("513210")?.materialSymbol;             // "language"
materialSymbolForMcc("5812", MccVendor.Stripe);          // "restaurant"
```

Python and TypeScript expose Material Symbol names as portable presentation
metadata. TypeScript has no native icon runtime, so a UI can pass the returned
ligature to its Material Symbols component or map it to another icon set.

Flutter:

```dart
import 'package:flutter/material.dart';
import 'package:reffin_ach/reffin_ach.dart';
import 'package:reffin_cards/reffin_cards.dart';
import 'package:reffin_currencies/reffin_currencies.dart';
import 'package:reffin_industries/reffin_industries.dart';
import 'package:reffin_iso20022/reffin_iso20022.dart';
import 'package:reffin_merchants/reffin_merchants.dart';

Icon(AchReturnCode.r22.icon);                       // Icons.undo
Text(AchTransactionCode.code22.label);              // Checking Credit
Text(PaymentPurposeCode.sala.label);                // Salary Payment
Icon(CardNetwork.visa.icon);                         // Icons.credit_card
Text(Currency.usd.displaySymbol);                    // $
Icon(resolveIndustry('513210')!.icon);               // Icons.language
Icon(Mcc.mcc5812.resolve(MccVendor.stripe)!.icon);   // Icons.restaurant
```

Flutter's ACH, cards, industries, and merchants packages expose native
Material `IconData`. Currency values use their typographic symbol or narrow
symbol instead of an illustrative icon. The ISO 20022 Flutter package likewise
exposes native Material `IconData`.

## Deterministic, offline generation

The shared generator reads the committed source CSVs, validates each domain,
and writes all three language targets. It performs no network access. Generated
files contain a SHA-256 fingerprint of their inputs so source CSV drift is
visible.

```sh
# Generate every domain.
python3 tools/generate.py

# Generate selected domains.
python3 tools/generate.py currencies industries

# Fail when committed generated files do not match their inputs.
python3 tools/generate.py --check
```

The root npm scripts provide equivalent all-domain entry points:

```sh
npm run generate
npm run check:generated
npm run check:sizes
npm run test:typescript
```

Run the entire local matrix, including Python, TypeScript, Flutter tests, and
Flutter static analysis, with `python3 tools/check_all.py` after dependencies
have been installed once.

Vendor imports are a separate, explicit normalization step. The merchant
importer does not download or silently refresh upstream material. Sources
marked `inventory_only` do not drive generated packages. Imported sources
without an explicit upstream redistribution license require a documented
project distribution decision; the current snapshot's decision is recorded in
the data policy and notices.

## Data rights and interpretation

Every source has its own permission boundary; there is no blanket license that
turns all upstream data into freely redistributable Reffin data.

- Cards are project-authored normalization vocabularies. Network names may be
  trademarks; no logos, BIN/IIN ranges, routing rules, or acceptance rules are
  included.
- Currencies are derived from CLDR 48.2 under the Unicode License v3. Its
  notice and license obligations travel with redistributed derivatives.
- Industries use the Census-published U.S. 2022 NAICS structure and the
  historical BLS QCEW SIC title table. BLS describes its published material as
  public domain and asks for attribution. Census employee works are generally
  public domain in the United States, with its caveat for third-party or
  contractor material. Presentation descriptions and icons are project-authored.
- ACH contains functional identifiers and concise, independently structured
  reference metadata. It is designed for decoding and display, not as a copy
  of the Nacha Operating Rules or as authorization, timing, compliance, or
  processing advice. Lifecycle metadata keeps future R90 distinct from the
  codes currently in effect and selects the applicable R16 meaning across its
  non-overlapping 2028 transition.
- ISO 20022 is an unofficial offline snapshot of information published in the
  ISO 20022 Repository. Codes must be interpreted within their qualified code
  set; message and transaction-code metadata is reference information rather
  than a schema validator or processing rule.
- Merchants mix an attributable CC BY 4.0 Adyen source with concise mappings
  derived from Stripe, Visa, and pinned `python-iso18245` views. Where no
  separate upstream dataset license was identified, Reffin has approved the
  current limited reference snapshot for public repository redistribution
  under its documented fair-use approach. That project-specific decision is
  not an upstream license grant or legal precedent. Mastercard's current
  booklet remains inventory-only and is not extracted.

Groups, icons, outcomes, and statuses are display and normalization metadata.
They are not interchange, eligibility, rewards, routing, risk, approval, or
regulatory advice.

Read the [data policy](docs/data-policy.md), [data notices](data/NOTICE.md),
[third-party notices](THIRD_PARTY_NOTICES.md), and domain provenance before
distributing data or generated artifacts:

- [Merchant source inventory](data/merchants/sources.csv)
- [Card vocabulary notes](data/cards/README.md)
- [Currency provenance](data/currencies/README.md)
- [Industry provenance](data/industries/README.md)
- [ACH provenance](data/ach/README.md)
- [ISO 20022 provenance](data/iso20022/README.md)

Registry publication is deliberately disabled. The
[release checklist](docs/release-checklist.md) records the remaining license,
notice-payload, name-reservation, and clean-package checks.

## License

Copyright 2026 Reffin contributors.

Except where otherwise identified, Reffin-authored software, documentation,
and project-authored metadata are licensed under the
[Apache License 2.0](LICENSE). The Apache license does not apply to or
relicense third-party data, names, or marks. Those materials remain subject to
their applicable terms, exceptions, and limitations; see
[third-party notices](THIRD_PARTY_NOTICES.md), [data notices](data/NOTICE.md),
and the bundled texts in [`LICENSES/`](LICENSES/).
