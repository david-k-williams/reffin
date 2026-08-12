# Reffin data policy

This policy explains how source data enters Reffin, what the generated packages
may claim, and how public-distribution decisions are recorded. It complements
the source-specific [data notices](../data/NOTICE.md) and
[third-party notices](../THIRD_PARTY_NOTICES.md); it is not legal advice or a
substitute for the upstream terms.

## Core rules

1. Pin every imported source by version, effective date, retrieval date, URL,
   and hash when the source is available as fixed bytes.
2. Keep normalized, reviewable CSVs as the code-generation inputs. Raw source
   downloads stay out of Git unless their license and a concrete need justify
   committing them.
3. Generate all language artifacts offline and deterministically. A generated
   input fingerprint must change when a code-generation input changes.
4. Preserve source-specific attribution, notices, and license obligations.
   Permission for one source does not apply to another source or to the whole
   repository.
5. Record import status separately from redistribution position.
   `inventory_only` material may guide research but must not become a generation
   input. `fair_use_reference` records a project-specific public-distribution
   decision for limited reference facts; it is not an upstream license grant
   and must be reassessed when the source, selected fields, volume, or intended
   distribution changes. Unresolved material stays `review_required` and does
   not enter a public release.
6. Keep presentation groupings and icons semantically generic. They must not be
   represented as network rules, legal classifications, or decision advice.

## Current domain boundaries

| Domain | Source classification | Redistribution position |
| --- | --- | --- |
| Cards | Project-authored normalization vocabularies | No copied third-party dataset is identified in the current tables. Network names remain subject to trademark and descriptive-use constraints. |
| Currencies | Unicode CLDR 48.2 under Unicode License v3 (`Unicode-3.0`) | Derivatives may be redistributed only with the applicable Unicode notice and license obligations preserved. |
| Industries | Census-published U.S. 2022 NAICS plus BLS-published historical SIC titles and project-authored presentation metadata | BLS states its published material is public domain and asks for attribution. Retain Census attribution and its third-party/contractor caveat; do not extend the NAICS position to separate Canadian or Mexican publications. |
| ACH | Functional ACH identifiers plus concise project-authored labels and structural metadata, checked against public Nacha material and Federal Reserve, archived Treasury, and industry comparisons | The current snapshot is approved for public repository redistribution under Reffin's fair-use reference approach. This does not claim an upstream license. Keep it a reference mapping rather than a substitute for the Nacha Operating Rules, and review package-registry release separately. |
| ISO 20022 | Published Repository External Code Sets, Bank Transaction Codes, and message-definition identifiers | ISO 20022 states that Repository information is intended for free use and reproduction under its IPR policy. Preserve attribution, release metadata, and the unofficial-snapshot disclaimer in every artifact. |
| Merchants | CC BY 4.0 Adyen data plus concise mappings derived from Stripe, Visa, and pinned python-iso18245 views | The current committed snapshot is approved for public repository redistribution. CC BY obligations apply to the Adyen derivative; other listed mappings use the documented fair-use reference position without claiming an upstream license. Package-registry publication remains a separate review. |

This policy describes data-source rights only. Reffin-authored software,
documentation, and project-authored metadata are licensed under the root
[Apache License 2.0](../LICENSE). That license does not apply to or relicense
third-party data, names, or marks. Applicable notices and license texts are in
[`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md),
[`data/NOTICE.md`](../data/NOTICE.md), and [`LICENSES/`](../LICENSES/).

## Merchant distribution decision

The current repository-level decision covers the combined
[`mcc_catalog.csv`](../data/merchants/normalized/mcc_catalog.csv), imported
vendor CSVs, and generated merchant targets committed to this repository:

- Python `reffin-merchants` / `reffin_merchants`;
- npm `@reffin/merchants`; and
- Dart/Flutter `reffin_merchants`.

Reffin has approved this current, limited reference snapshot for public
repository redistribution. Where no separate upstream redistribution license
was identified, the decision rests on the documented fair-use reference
approach. It is not an upstream license grant, a determination for other
material or uses, or legal precedent. Changing the source, selected fields,
volume, or distribution method requires a fresh decision. Package-registry
publication remains independently gated; a green generation or test run is not
package-release clearance.

The merchant sources have deliberately different statuses:

- Adyen DABstep is imported under CC BY 4.0. Sharing requires the supplied
  attribution and license information, an upstream URI where reasonably
  practicable, and an indication of changes.
- Stripe's MIT OpenAPI is used to verify category-key completeness, but it does
  not contain the MCC mapping. The mapping comes from Stripe's Issuing
  documentation and is imported as `fair_use_reference`; no Stripe dataset
  license grant is claimed.
- Visa's April 2026 manual is publicly accessible, but `VISA PUBLIC` is not an
  open-data license. Its extracted rows are imported as `fair_use_reference`;
  no Visa dataset license grant is claimed.
- Pinned `python-iso18245` lists provide Alipay, American Express, ISO 2003,
  Mastercard, and USDA views. The package's MIT repository license does not
  establish rights to its underlying vendor or ISO datasets. The concise
  mappings are imported as `fair_use_reference`; no upstream dataset license
  grant is claimed.
- Mastercard's current official booklet remains separately inventoried and is
  not imported.

The machine-readable authority for import status and redistribution position is
[`sources.csv`](../data/merchants/sources.csv). `fair_use_reference` identifies
the project's decision; `inventory_only` remains excluded from generation.

## Domain-specific interpretation limits

### Cards

Card values normalize application terminology; they do not encode scheme
acceptance, routing, authentication, risk, settlement, dispute, or approval
rules. Applications should retain an original provider value beside a
normalized value. `unknown` means not supplied or not determined; `other`
means known but outside the named values.

Network names are descriptive. Reffin includes no logos. An optional
`brand_asset_key` only points to an asset an application separately supplies
and licenses. The tables deliberately exclude BIN/IIN ranges, PAN-prefix
detection, and full PAN handling.

### Currencies

`active` means the identifier has CLDR validity status `regular` in version
48.2; it is not a live legal-tender determination. Territory lists combine all
CLDR associations recorded for a currency, including historical associations,
without their dates or tender flags. Minor and cash rounding fields are CLDR
increments in the least-significant displayed digit.

### Industries

The current hierarchy is the U.S. Census 2022 NAICS structure. A separate
project-derived lookup retains BLS QCEW rows not explicitly prefixed `1972 SIC`:
the 1987 four-digit SIC code set plus BLS hierarchy containers and eight QCEW
rollups. It must not be presented as current or as the canonical SIC-manual
hierarchy. Reffin does not combine separate Canadian or Mexican NAICS
publications. Stable sector/division IDs, descriptions, and icons are Reffin
presentation metadata rather than Census or BLS fields.

### ACH

ACH identifiers are stored as strings and organized into seven independent
families: transaction, return, Standard Entry Class (SEC), service class,
record type, Notification of Change, and addenda type. The normalized labels
are concise Reffin wording. Public Nacha materials control inclusion and
meaning; Federal Reserve material, an archived U.S. Treasury dictionary, and
Modern Treasury documentation are comparison references rather than complete
or authoritative source tables.

Lifecycle status is part of the API. The return table has 72 rows for 71 codes:
`R16` has non-overlapping meanings before and from 2028-03-17, when the adopted
future return code `R90` also begins. Current-only lookups omit R90 and legacy
addenda type `01`; date-aware lookups select the record whose effective
interval contains the requested date. The snapshot does not silently treat
every number between `R01` and `R85` as a defined return code.

The ACH package decodes reference values. It does not specify whether an entry
is authorized, eligible, timely, compliant, or correctly formatted, and it
does not replace the current Nacha Operating Rules, an ACH operator's
requirements, or an institution's processing agreement. Applications should
retain the original code and consult their governing rules for operational
decisions.

### ISO 20022

ISO 20022 values remain qualified by their official code set. The same short
code can have unrelated meanings in different sets, so generic resolution
requires both the set and code; unqualified search intentionally returns all
matches. Registered records are returned by default, while obsolete records
remain available for historical decoding. Creation and last-update dates are
preserved as source metadata but are not converted into invented effective
intervals.

The package includes payment-focused enhanced values, complete catalog search,
the separately published Domain/Family/SubFamily Bank Transaction Code
hierarchy, and message-identifier lookup. It does not include XML schemas,
message serialization, validation, market-practice rules, or an assertion that
a code is accepted by a particular clearing system or counterparty. Reffin is
an unofficial pinned snapshot; ISO 20022's site remains authoritative for the
current Repository.

### Merchants

Vendor wording and coverage differ, so every lookup keeps the vendor explicit.
MCCs are strings, and broad Reffin groups are presentation aids only. They do
not determine interchange, rewards, eligibility, routing, or merchant risk.

## Icons and UI metadata

Reffin uses generic Material semantic icon names for ACH values, cards,
industry sectors, and merchant groups. Python and TypeScript return the icon
name as metadata. Flutter maps the same meaning to its native Material `Icons`
`IconData`. Currency values use their CLDR typographic symbol data and do not
invent a category icon. ISO 20022 code-set families follow the same generic
icon-metadata convention.

Material icon assignments are not brand marks. Network and product names may
be trademarks of their respective owners, and their inclusion does not imply
affiliation or endorsement.

## Adding or updating a source

Before a new source drives code generation:

1. Record the authoritative publisher URL, version, dates, format, checksum,
   stated license, redistribution status, and transform notes.
2. Confirm that the stated license covers the actual data being imported, not
   merely the surrounding repository, API schema, or public web page.
3. Mark unresolved material `review_required`; keep prohibited or
   comparison-only sources `inventory_only`. Use `fair_use_reference` only
   after documenting a project decision for the specific selected facts and
   intended distribution. Do not describe that status as an upstream license.
4. Normalize only the fields needed by the public API and validate identifiers,
   uniqueness, hierarchy, and deterministic ordering.
5. Regenerate every affected language target and run `python3
   tools/generate.py --check`.
6. Reassess both the public-repository decision and the separate package
   publishing gate. Update this policy, [`data/NOTICE.md`](../data/NOTICE.md),
   and [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) before release.

Detailed provenance and transforms live with each domain:

- [Merchant source inventory](../data/merchants/sources.csv)
- [Card vocabularies](../data/cards/README.md)
- [Currency snapshot](../data/currencies/README.md)
- [Industry snapshot](../data/industries/README.md)
- [ACH snapshot](../data/ach/README.md)
- [ISO 20022 snapshot](../data/iso20022/README.md)
