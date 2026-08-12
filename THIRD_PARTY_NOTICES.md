# Third-party notices

Copyright 2026 Reffin contributors

Except where a file or notice states otherwise, Reffin-authored software,
documentation, and project-authored metadata are licensed under the
[Apache License 2.0](LICENSE). That license does **not** license or relicense
third-party data, names, or marks. This document records the sources and terms
applicable to the current committed data snapshot; it does not alter them.

See [`data/NOTICE.md`](data/NOTICE.md) and the domain provenance files for exact
versions, retrieval dates, hashes, and transformations.

## Unicode CLDR

The currency data is derived from Unicode CLDR 48.2.

- Copyright © 1991–2026 Unicode, Inc.
- License: [Unicode License v3](LICENSES/Unicode-3.0.txt)
- Upstream: <https://cldr.unicode.org/>

Reffin selected and normalized the English currency names, symbols, fraction
rules, validity statuses, and territory associations described in the
[currency provenance](data/currencies/README.md). Unicode and the Unicode Logo
are trademarks of Unicode, Inc.

## Adyen DABstep

`data/merchants/vendors/adyen_dabstep.csv` is adapted from Adyen's DABstep
`merchant_category_codes.csv`, revision
`07d7d7eaab4386f4c25cd63f3f0a32845b6ecd9d`.

- Creator and source: Adyen,
  <https://huggingface.co/datasets/adyen/DABstep>
- License: [Creative Commons Attribution 4.0 International](LICENSES/CC-BY-4.0.txt)
- Changes: Reffin removed the source index, standardized columns, joined the
  rows into a vendor-qualified catalog, and added independently authored
  presentation metadata.

The source is a research-benchmark reference and is not represented as Adyen's
current production API taxonomy. Adyen's name is used only for attribution and
does not imply affiliation or endorsement.

## U.S. industry classifications

The NAICS snapshot is transformed from the U.S. Census Bureau's 2022 NAICS
structure workbook. The Census Bureau states that works created by its
employees are generally not subject to copyright protection in the United
States, while third-party or contractor material may be protected.

The historical SIC lookup is normalized from the U.S. Bureau of Labor
Statistics QCEW SIC industry-title table. BLS states that its published
material is public domain except for previously copyrighted photographs and
illustrations, and asks users to cite BLS as the source.

- Census NAICS: <https://www.census.gov/naics/?input=nationwide&year=2022>
- BLS SIC titles:
  <https://www.bls.gov/cew/classifications/industry/sic-industry-titles.htm>
- Transform details: [`data/industries/README.md`](data/industries/README.md)

Reffin's sector and division IDs, descriptions, and generic icon assignments
are project-authored metadata covered by the root Apache License 2.0.

## Merchant reference mappings

The merchant catalog includes concise MCC and name mappings derived from the
source materials recorded in `data/merchants/sources.csv`, including published
Stripe Issuing documentation, Visa's Merchant Data Standards Manual, and
pinned views from `python-iso18245`.

No separate upstream dataset license grant has been identified for those
limited mappings. Reffin has approved inclusion and public repository
redistribution of the current committed snapshot under the project's
documented fair-use reference approach. This is a project-specific decision;
it is not an upstream license grant, a determination about other material or
uses, or legal precedent. Changes in source, fields, volume, or distribution
method require a fresh review.

Mastercard's current Quick Reference Booklet is discovery-only inventory. It
is not extracted into Reffin. Merchant and network names may be trademarks of
their respective owners. Reffin includes no logos and is not affiliated with
or endorsed by any named provider or network.

## ACH reference mappings

The ACH tables contain functional identifiers and concise, independently
structured Reffin labels and metadata checked against public Nacha materials,
Federal Reserve materials, an archived U.S. Treasury dictionary, and industry
cross-checks. They do not reproduce the Nacha Operating Rules or provide
authorization, deadline, warranty, formatting, or compliance instructions.

No upstream license grant for the complete ACH reference package is claimed.
Reffin has approved inclusion and public repository redistribution of the
current committed snapshot under the project's documented fair-use reference
approach. This project-specific decision is not an upstream license grant or
legal precedent and must be revisited if the scope or use changes.

Nacha, Federal Reserve, U.S. Treasury, and Modern Treasury names are used only
for source attribution. Their inclusion does not imply affiliation,
endorsement, or official status.

## ISO 20022 Repository information

The ISO 20022 data is derived from published Repository External Code Sets,
Bank Transaction Codes, and message-definition identifiers. ISO 20022's
intellectual-property policy grants third parties a non-exclusive,
royalty-free license to use published Repository information.

- IPR policy: <https://www.iso20022.org/intellectual-property-rights>
- Terms of use: <https://www.iso20022.org/terms-use>
- Snapshot details: [`data/iso20022/README.md`](data/iso20022/README.md)

Reffin is an unofficial offline snapshot and may not reflect the latest
Repository. Reffin is not affiliated with ISO, SWIFT, or the ISO 20022
Registration Authority. ISO and related names and marks may be protected.

## Generic icon metadata and trademarks

Material icon names in generated data are generic semantic metadata. Flutter
packages refer to the Material `Icons` API supplied by the consuming Flutter
SDK; Reffin does not bundle Google's icon font or third-party logo artwork.

All third-party names, marks, and product names belong to their respective
owners. Their descriptive use does not imply affiliation or endorsement.
