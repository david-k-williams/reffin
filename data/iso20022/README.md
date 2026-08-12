# ISO 20022 provenance

This directory contains deterministic normalized snapshots of information
published in the ISO 20022 Repository. Reffin is an unofficial offline
reference package; `iso20022.org` remains the authoritative source for current
materials.

## Snapshot inventory

| File | Source release | Normalized coverage |
| --- | --- | ---: |
| `code_sets.csv` | External Code Sets, May 2026 v1 | 158 descriptors |
| `external_codes.csv` | External Code Sets, May 2026 v1 | 3,246 physical rows; 3,213 registered and 33 obsolete |
| `bank_transaction_codes.csv` | Bank Transaction Codes, 30 November 2025 v1 | 1,567 physical rows; 1,564 composite identities |
| `message_definitions.csv` | e-Repository, 26 June 2026 | 797 current message identifiers |

The External Code Sets workbook calls itself `29 May 2026 - 1Q2026` even
though the official download page labels the release May 2026 v1. Both labels
are preserved. ISO states that External Code Sets are normally refreshed at
the end of February, May, August, and November, so consumers should compare the
package release to the current official site when freshness matters.

Exact URLs, retrieval dates, archive hashes, unpacked-member hashes, and
transformation notes are recorded in [`sources.csv`](sources.csv). Raw ZIP,
XLSX, XSD, JSON, and e-Repository files are not committed.

## External Code Sets

`tools/import_iso20022_external_codes.mjs` reads the pinned official workbook
with the bundled spreadsheet runtime, normalizes whitespace and ISO dates,
derives a separate UI label from each official concatenated name, and checks
all registered workbook values against the official JSON enums.

The normalized catalog preserves:

- 158 code-set descriptors: 156 registered, one provisionally registered, and
  one obsolete;
- 3,246 physical code rows across 3,245 `(code_set, code)` identities;
- official names, definitions, requester, lifecycle status, source dates,
  replacement and mapping fields, and additional information; and
- the two historical meanings of `ExternalLocalInstrument1Code/CTP`.

Creation and last-update dates are source metadata, not inferred effective
intervals. Ordinary resolution selects the registered record. Historical
record APIs retain obsolete rows without pretending the exact retirement date
is known.

The eight payment-focused enhanced families contain 950 registered values:

| Official set | Values |
| --- | ---: |
| `ExternalPurpose1Code` | 342 |
| `ExternalStatusReason1Code` | 302 |
| `ExternalReturnReason1Code` | 104 |
| `ExternalLocalInstrument1Code` | 86 |
| `ExternalCategoryPurpose1Code` | 49 |
| `ExternalServiceLevel1Code` | 29 |
| `ExternalPaymentTransactionStatus1Code` | 25 |
| `ExternalPaymentGroupStatus1Code` | 13 |

## Bank Transaction Codes

`tools/import_iso20022_bank_transaction_codes.mjs` preserves all physical rows
from the official workbook. A value is qualified by its Domain, Family, and
SubFamily codes; those tokens must not be resolved independently. Three
composite identities occur twice with source variants and are deliberately
available as record lists. The workbook's `new`, `corrected`, and `updated`
statuses describe source changes, not current-versus-obsolete lifecycle.

## Message identifiers

`tools/import_iso20022_message_definitions.mjs` derives the current message set
from the pinned official e-Repository. Dotted identifiers remain strings and
are split into business area, message number, variant, and version only after
validating the complete identifier. For example, the snapshot's current
FI-to-FI Customer Credit Transfer is `pacs.008.001.14`; older versions are not
misrepresented as current catalog entries.

This is message-name and identifier reference data. Reffin does not bundle XML
schemas or provide message serialization, validation, conformance, or
market-practice rules.

## Reuse and attribution

ISO 20022's intellectual-property policy grants third parties a non-exclusive,
royalty-free license to use published Repository information, and its terms of
use state that the material is intended for free use and reproduction:

- https://www.iso20022.org/intellectual-property-rights
- https://www.iso20022.org/terms-use

Redistributed artifacts should retain ISO 20022 attribution, the pinned source
release and hashes, and a clear statement that Reffin is unofficial and may not
reflect the latest Repository.
