# Reffin packages

Reffin defines one independent package per reference domain and language. All
packages are generated from the same committed CSV inputs, work without network
access at runtime, and expose an input fingerprint for drift checks. The names
below come from local manifests and are not a claim of public registry
availability.

| Domain | Python distribution / import | npm | Dart/Flutter |
| --- | --- | --- | --- |
| Merchants | `reffin-merchants` / `reffin_merchants` | `@reffin/merchants` | `reffin_merchants` |
| Cards | `reffin-cards` / `reffin_cards` | `@reffin/cards` | `reffin_cards` |
| Currencies | `reffin-currencies` / `reffin_currencies` | `@reffin/currencies` | `reffin_currencies` |
| Industries | `reffin-industries` / `reffin_industries` | `@reffin/industries` | `reffin_industries` |
| ACH | `reffin-ach` / `reffin_ach` | `@reffin/ach` | `reffin_ach` |
| ISO 20022 | `reffin-iso20022` / `reffin_iso20022` | `@reffin/iso20022` | `reffin_iso20022` |

> [!NOTE]
> The merchant artifacts include concise reference facts from sources that do
> not provide an upstream open-data license. Their inclusion in this public
> repository follows Reffin's documented project-level fair-use determination;
> it is not an upstream license grant or a substitute for a downstream rights
> assessment. See the [data policy](../docs/data-policy.md).

All Dart manifests currently set `publish_to: none`, all npm manifests are
marked `private`, and all Python manifests use PyPI's upload-rejecting
`Private :: Do Not Upload` classifier. No registry release should be enabled
before the project license and per-artifact notice payloads are selected. The
plain `reffin` name is reserved for a possible future convenience bundle.

## Generated API shape

| Domain | Enhanced values and lookups | Presentation metadata |
| --- | --- | --- |
| Merchants | `Mcc`, `MccVendor`, vendor-key and MCC resolvers | Project-authored broad group and icon |
| Cards | Eight enums/const objects for networks, funding, form factor, product class, method family, channel, verification, and outcome | Generic icon for every value; optional app-owned `brandAssetKey` for networks |
| Currencies | Currency values and case-insensitive resolver; name, symbols, minor/cash units, CLDR status, and territories | Typographic `symbol` and `narrowSymbol` |
| Industries | Full NAICS hierarchy plus a separate historical BLS QCEW SIC-coded lookup and resolvers | Project-authored NAICS sector and SIC division descriptions/icons |
| ACH | Seven code families with safe, lifecycle-aware resolvers and current-only collections | Concise labels, structural metadata, status/effective dates, and generic payment icons |
| ISO 20022 | Eight payment-focused enhanced families, qualified full-catalog search, Bank Transaction Code hierarchy, and message-ID resolver | Official names and definitions, lifecycle status, source versions, and set-level icons |

Unknown input returns `None`, `undefined`, or `null` rather than fabricating a
record. ACH lookups exclude planned and historical values by default, with an
explicit API for date-aware or inclusive resolution. Cards also provide
stable `unknown` and `other` enum values where those concepts are part of the
vocabulary.

## Concise examples

Python:

```python
from reffin_ach import AchReturnCode, AchTransactionCode
from reffin_cards import CardNetwork
from reffin_currencies import Currency
from reffin_industries import resolve_industry
from reffin_iso20022 import PaymentPurposeCode

software = resolve_industry("513210")
assert software is not None and software.parent is not None

assert AchTransactionCode.CODE_22.info.name == "Checking Credit"
assert AchReturnCode.R22.info.name == "Invalid Individual ID Number"
assert PaymentPurposeCode.SALA.label == "Salary Payment"
assert CardNetwork.VISA.material_symbol == "credit_card"
assert Currency.JPY.info.minor_digits == 0
assert software.parent.code == "51321"
```

TypeScript:

```ts
import { AchReturnCode, AchTransactionCode } from "@reffin/ach";
import { CardNetwork } from "@reffin/cards";
import { Currency, resolveCurrency } from "@reffin/currencies";
import { sectorForIndustry } from "@reffin/industries";
import { PaymentPurposeCode } from "@reffin/iso20022";

AchTransactionCode.Code22.name;              // "Checking Credit"
AchReturnCode.R22.name;                      // "Invalid Individual ID Number"
PaymentPurposeCode.SALA.label;               // "Salary Payment"
CardNetwork.Visa.materialSymbol;              // "credit_card"
resolveCurrency(Currency.CHF)?.cashRounding;  // 5
sectorForIndustry("513210")?.materialSymbol;  // "language"
```

Flutter:

```dart
import 'package:flutter/material.dart';
import 'package:reffin_ach/reffin_ach.dart';
import 'package:reffin_cards/reffin_cards.dart';
import 'package:reffin_currencies/reffin_currencies.dart';
import 'package:reffin_industries/reffin_industries.dart';
import 'package:reffin_iso20022/reffin_iso20022.dart';

Icon(AchReturnCode.r22.icon);           // native Icons.undo
Text(AchTransactionCode.code22.label);  // Checking Credit
Text(PaymentPurposeCode.sala.label);    // Salary Payment
Icon(CardNetwork.visa.icon);            // native Icons.credit_card
Text(Currency.usd.displaySymbol);       // $
Icon(resolveIndustry('513210')!.icon);  // native Icons.language
```

Python stores icon keys as `material_symbol`; TypeScript uses
`materialSymbol`. Those strings are portable Material Symbols names. Flutter's
ACH, cards, industries, and merchants packages depend on Flutter and expose
native Material `IconData`. The currency package is UI-independent and uses
typographic currency symbols. The ISO 20022 Flutter package likewise exposes
native Material `IconData`.

## Repository layout and checks

```text
packages/
  python/reffin_<domain>/
  typescript/reffin_<domain>/
  flutter/reffin_<domain>/
```

Run the shared generator from the repository root. Supplying no domain writes
all artifacts; supplying domain names limits the run.

```sh
python3 tools/generate.py
python3 tools/generate.py ach cards currencies iso20022
python3 tools/generate.py --check
```

TypeScript package tests can run together with `npm run test:typescript` from
the root. `python3 tools/check_all.py` runs generation freshness, generated-size
budgets, Python and TypeScript tests, Flutter tests, and Flutter static analysis.
Generated files should never be edited by hand.

For source versions, interpretation boundaries, and the public-reference
rights posture, read the [root overview](../README.md),
[data notices](../data/NOTICE.md), and
[data policy](../docs/data-policy.md).
