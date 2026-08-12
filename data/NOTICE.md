# Data notices

This file records the third-party data notices for the current Reffin snapshot.
It is not a blanket license for the repository, project-authored material, or
third-party marks. See the [data policy](../docs/data-policy.md), root
[third-party notices](../THIRD_PARTY_NOTICES.md), and bundled
[`LICENSES`](../LICENSES/) for distribution decisions, attribution, and
applicable license texts.

## Merchant reference data

The current merchant CSV and all generated merchant packages combine sources
with different upstream licensing positions. Reffin has reviewed and approved
the current committed snapshot for public repository redistribution. For the
limited code-title mappings without a separate upstream redistribution
license, that approval rests on the project's documented fair-use reference
approach. It is a project-specific decision, not an upstream license grant, a
determination about other material or uses, or legal precedent. A public
package-registry release remains a separate payload and release review.

- [`adyen_dabstep.csv`](merchants/vendors/adyen_dabstep.csv) is adapted from
  Adyen's DABstep `merchant_category_codes.csv`, revision
  `07d7d7eaab4386f4c25cd63f3f0a32845b6ecd9d`, under
  [CC BY 4.0](../LICENSES/CC-BY-4.0.txt). The source index was removed,
  columns were standardized, rows were joined into a vendor-qualified catalog,
  and independently authored presentation metadata was added. When this
  derivative is shared, retain the attribution, license information, upstream
  URI where reasonably practicable, and indication of changes supplied here
  and in the source inventory.
- [`stripe.csv`](merchants/vendors/stripe.csv) uses the MCC/name mapping on
  Stripe's Issuing documentation. Stripe's MIT-licensed OpenAPI verifies the
  295 category keys but does not supply the MCC mapping. The documentation is
  governed by Stripe's site terms. Reffin includes the current concise mapping
  under the fair-use reference decision described above; no Stripe dataset
  license grant is claimed.
- [`visa.csv`](merchants/vendors/visa.csv) is a mechanical extraction of MCC
  titles from Visa's April 2026 Merchant Data Standards Manual. `VISA PUBLIC`
  is a document classification, not an open-data license. Reffin includes the
  current concise mapping under the fair-use reference decision described
  above; no Visa dataset license grant is claimed.
- Pinned `python-iso18245` 1.4.1 lists supply the Alipay, American Express,
  historical ISO 2003, Mastercard, and USDA views used for generation. Its MIT
  repository license does not establish redistribution rights for the
  underlying ISO and vendor-derived datasets. Reffin includes the current
  concise mappings under the fair-use reference decision described above; no
  upstream dataset license grant is claimed.
- Mastercard's 2 June 2026 Quick Reference Booklet is proprietary. It is
  separately inventoried for discovery only and is deliberately not extracted.

The authoritative per-source versions, retrieval dates, hashes, URLs, import
statuses, and redistribution positions are in
[`merchants/sources.csv`](merchants/sources.csv). An `inventory_only` source
is not an imported input. A `fair_use_reference` position records Reffin's
project decision and does not imply an upstream license. Broad merchant groups
and Material icon assignments in [`merchants/groups.csv`](merchants/groups.csv)
are project-authored presentation metadata, not card-network classifications.

## Currency data

[`currencies/currencies.csv`](currencies/currencies.csv) is derived from
Unicode CLDR 48.2 and is redistributed under the
[Unicode License v3](../LICENSES/Unicode-3.0.txt) (`Unicode-3.0`). A
redistribution must carry Unicode's copyright and permission notice with every
copy of the data or in its associated documentation. The bundled official text
includes the current notice: Copyright © 1991–2026 Unicode, Inc.

The pinned archive URL, official SHA-512 verification, local SHA-256 hashes,
exact CLDR source files, transformations, and known semantic limitations are in
the [currency provenance](currencies/README.md). Unicode and the Unicode Logo
are trademarks of Unicode, Inc.

## Industry data

[`industries/naics_2022.csv`](industries/naics_2022.csv) is a deterministic
transformation of the U.S. Census Bureau's 2022 NAICS structure workbook. The
Census Bureau states that works created by its employees are generally not
subject to copyright protection in the United States, while third-party or
contractor material may be protected. Reffin retains source attribution and
does not extend that statement to separate Canadian or Mexican publications.

[`industries/sectors.csv`](industries/sectors.csv) contains project-authored
stable IDs, descriptions, and generic Material icon keys. See the
[industry provenance](industries/README.md) for the exact source, hash, and
transform.

[`industries/sic_1987.csv`](industries/sic_1987.csv) is normalized from the
U.S. Bureau of Labor Statistics QCEW SIC industry-title table. BLS states that
its published material is public domain except for previously copyrighted
photographs and illustrations, and asks users to cite BLS as the source.
Reffin excludes rows explicitly labeled `1972 SIC`; this is a historical
project-derived lookup containing the 1987 code set plus BLS QCEW hierarchy
containers and eight rollups, not a current or canonical SIC-manual hierarchy.
Stable division IDs, descriptions, and icons in `sic_divisions.csv` are
project-authored.

Sources:

- https://www.bls.gov/cew/classifications/industry/sic-industry-titles.htm
- https://www.bls.gov/bls/linksite.htm#copyright

## Card vocabularies, icons, and marks

The normalized tables under [`cards/`](cards/) are project-authored. They
contain descriptive network names but no brand artwork, BIN/IIN ranges, PAN
detection, routing rules, or scheme rules. Names may be trademarks of their
respective owners. Optional `brand_asset_key` values do not include or license
an asset and do not imply affiliation or endorsement.

Material icon names throughout Reffin are generic presentation metadata. The
Flutter artifacts map them to Flutter's native Material `Icons` values; no
third-party logo artwork is bundled.

## ACH reference data

The normalized tables under [`ach/`](ach/) contain ACH code identifiers and
concise, independently structured Reffin labels and metadata. They are a
reference aid for decoding ACH data, not a reproduction of the Nacha Operating
Rules. The generated packages deliberately omit detailed rule text,
authorization requirements, return deadlines, warranties, formatting
instructions, and compliance procedures.

The code sets and structural facts are checked against public Nacha developer
material, rule-change notices, and an indexed Basic Edition reference. Federal
Reserve material, an archived U.S. Treasury dictionary, and Modern Treasury
documentation and learning pages are comparison sources. Public shortcut
lists are not assumed to be complete: official Nacha sources control
inclusion and meaning, and the snapshot distinguishes current, planned, and
historical values. See the [ACH provenance](ach/README.md) for the source
inventory, snapshot date, transformations, counts, and hashes.

No Nacha or Federal Reserve license grant for this package is claimed. Reffin
has approved the compact identifiers and independently authored metadata in
the current committed snapshot for public repository redistribution under the
project's documented fair-use reference approach. This is a project-specific
decision, not an upstream license grant or legal precedent. It must be
reassessed if the source, fields, volume, or distribution method changes; a
package-registry release remains a separate review.

Nacha and Modern Treasury names may be trademarks of their respective owners.
Their inclusion as source attribution does not imply affiliation, endorsement,
or that Reffin is an official ACH rules publication.

## ISO 20022 Repository reference data

The normalized files under [`iso20022/`](iso20022/) are derived from published
ISO 20022 Repository materials: External Code Sets, Bank Transaction Codes, and
message-definition identifiers. ISO 20022's intellectual-property policy grants
third parties a non-exclusive, royalty-free license to use published Repository
information, and its site terms state that the material is intended for free
use and reproduction. See the [ISO 20022 provenance](iso20022/README.md) for
the exact versions, download URLs, archive hashes, transformations, and counts.

Reffin is not affiliated with ISO, SWIFT, or the ISO 20022 Registration
Authority. Its generated artifacts are unofficial offline snapshots and must
not be represented as the official or current Repository. ISO and related names
and marks may be protected; attribution does not imply endorsement.
