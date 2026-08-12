# ACH reference codes

This directory is a deterministic snapshot of compact ACH identifiers and
project-authored labels for offline lookup. It is current as of 2026-08-11,
except where a row explicitly has `planned` or `legacy` status. The tables are
reference data, not the Nacha Operating Rules, legal advice, authorization
guidance, return-deadline guidance, or instructions for originating an Entry.

## Files and schemas

- `transaction_codes.csv` (38 rows): `code,name,account_type,direction,entry_kind,return_for_codes,status,source`
- `return_codes.csv` (72 rows; 71 distinct codes): `code,name,category,status,valid_from,valid_to,source`
- `standard_entry_class_codes.csv` (23 rows): `code,name,entry_kind,consumer_or_corporate,direction,addenda_support,status,valid_from,valid_to,source`
- `service_class_codes.csv` (4 rows): `code,name,direction,status,source`
- `record_type_codes.csv` (6 rows): `code,name,status,source`
- `change_codes.csv` (10 rows): `code,name,corrected_field,applies_to,status,valid_from,valid_to,source`
- `addenda_type_codes.csv` (14 rows): `code,name,applies_to,status,source`

All codes are strings so leading zeroes survive. Multi-value cells use `|` in
an otherwise RFC 4180 CSV. Blank lifecycle dates mean that this snapshot does
not establish a boundary. Rows are sorted in numeric or lexical code order.

The return table has 72 physical rows and 71 distinct codes. Exactly 70 codes
resolve on the snapshot date. `R16` has two non-overlapping lifecycle rows: its
present meaning runs through 2028-03-16, and its narrower `Account Frozen`
meaning begins on 2028-03-17. `R90` is also `planned` for 2028-03-17. A
date-aware resolver must exclude both future rows before that date, then select
the successor R16 row and include R90. The table uses the modern R11 meaning
and summarizes all three current R17 uses without copying the Rules'
explanatory text.

The addenda table has 13 `current` rows. Type `01` is retained as `legacy` so
older CBR/PBR files can be decoded; it must be excluded by a current-only
resolver. The change table intentionally contains the ten ordinary NOC codes
and excludes refused-NOC codes C61-C69.

IAT remains a current SEC code with no lifecycle end date. Nacha has published
a revised IAT definition effective 2026-09-18; that future wording change does
not retire or replace the code.

## Provenance

The `source` column contains one or more of these stable source keys:

- `nacha_developer_guide`: Nacha Payments Innovation Alliance, ACH Guide for
  Developers, "ACH File Overview" and "ACH File Details":
  https://achdevguide.nacha.org/ach-file-overview and
  https://achdevguide.nacha.org/index.php/ach-file-details
- `nacha_basic_2025`: Nacha, 2025 Operating Rules Basic Edition appendices,
  publicly indexed reference copy:
  https://nachaoperatingrulesonline.org/assets/attachments/25_basic_appendixes.pdf
- `nacha_iso20022_2023`: Nacha ISO 20022 Guide to Mapping U.S. ACH File
  Formats, camt.053 returns, version 2.01 (August 2023):
  https://www.nacha.org/system/files/2023-08/NACHA_ISO20022_Guide_camt.053_returns%2008-09-23.pdf
- `nacha_rule_r90`: Nacha, "New Return Reason Code for Sanctions Compliance
  Obligations," effective 2028-03-17:
  https://www.nacha.org/rules/new-return-reason-code-sanctions-compliance-obligations
- `nacha_minor_topics_2026`: Nacha, "Minor Topics Rule Changes," effective
  2026-01-01; used to verify the current R17 wording:
  https://www.nacha.org/rules/minor-topics-rule-changes
- `nacha_r11_2020`: Nacha, "Differentiating Unauthorized Return Reasons";
  verifies that the modern R11 meaning took effect on 2020-04-01:
  https://www.nacha.org/rules/differentiating-unauthorized-return-reasons
- `nacha_questionable_2019`: Nacha, "Return for Questionable Transaction";
  used to verify R17's questionable-entry use:
  https://www.nacha.org/rules/return-questionable-transaction
- `nacha_reversals_2021`: Nacha, "Reversals and Enforcement"; used to verify
  R17's improper-reversal use:
  https://www.nacha.org/rules/reversals-and-enforcement
- `nacha_iat_2026`: Nacha, "Definition of IAT Entries," effective
  2026-09-18; records the upcoming definition change without ending the SEC
  code's lifecycle:
  https://www.nacha.org/rules/definition-iat-entries
- `fedglobal_manual_2026`: Federal Reserve Financial Services, FedGlobal ACH
  Payments Service Origination Manual (2026); used as a current public check
  for selected transaction and return codes:
  https://www.frbservices.org/binaries/content/assets/crsocms/financial-services/ach/global-service-orig-manual.pdf

Fixed upstream responses fetched on 2026-08-11 had these SHA-256 values:

- `nacha_iso20022_2023` PDF: `48954a9515ce619a17058761052df81a367cc2322c97f8f2879b85d1245d95d8`
- `fedglobal_manual_2026` PDF: `4aaaf85890cc943101cf187987c6bad8876ed575b9e8c7fd162b39ccb0fa25ce`
- `nacha_basic_2025` published URL response: `7b8ae51374e5a7feee12b644bfca9fcca78d1d97c4f0c193c7d24ce6df6760bc`

The last response was an HTML document-viewer shell despite the `.pdf` URL;
it is not a hash of the appendix PDF bytes. The indexed official document text
was used for verification. This limitation is recorded so a later refresh does
not mistake the wrapper for the source document. No upstream artifact is
committed.

Modern Treasury's public documentation and learning pages were non-authoritative
comparison sources requested for this snapshot:

- https://docs.moderntreasury.com/payments/docs/customize-sec-codes
- https://docs.moderntreasury.com/payments/docs/ach-return-codes
- https://www.moderntreasury.com/learn/ach-return-code-reference

The requested vanity URLs were also checked, but presented glossary shells
rather than complete tables:

- https://www.moderntreasury.com/sec-codes
- https://www.moderntreasury.com/ach-return-codes

None of the Modern Treasury pages was a generation source. Their tables are
incomplete for the full network sets and return material can lag rule changes;
official sources controlled inclusion, status, and current meanings.

The U.S. Treasury Data Registry ACH dictionary was an archived public-domain
comparison source for transaction and addenda identifiers. Its former deep URL
now redirects to a generic data page, so it is not used as a live source key:
https://www.fiscal.treasury.gov/data/FSv49/IAIv10/Library/AttributeDataDictionary.html

Sources were accessed on 2026-08-11.

## Transformation and rights boundary

The transformation selected assigned identifiers, reduced each meaning to a
short independently worded label, added normalized project-authored facets,
and omitted operational prose. In particular, these CSVs do not reproduce
authorization requirements, deadlines, warranties, participant obligations,
written-statement rules, examples, cross-references, or full format tables.

Nacha's website and Rules terms restrict reproduction, database extraction,
and derivative use without permission:

- https://www.nacha.org/content/legal-information
- https://www.nacha.org/system/files/2024-05/Nacha_Rules_TOU_website%2Bebook.pdf

Federal Reserve Financial Services also limits reproduction of site content:
https://www.frbservices.org/terms/

This project treats the compact identifiers, independently authored labels,
and interoperability facts as a fair-use reference snapshot. The maintainer
approved public repository distribution on 2026-08-12. That project-level
determination is not a license grant from Nacha or the Federal Reserve Banks,
and downstream users remain responsible for assessing their own use. Do not
present these tables as an official substitute for the current Rules.

## Integrity and validation

Normalized CSV SHA-256 values:

- `transaction_codes.csv`: `0cab1345fd2a0fa20d4ae19572220d289b8b8b8e7d26fa8fb7e2ca822f6b02cd`
- `return_codes.csv`: `951a59c3316b5e9a40649fd1eca88888669603770134334c77090ea92e5d23fc`
- `standard_entry_class_codes.csv`: `1a9b676796e9637652b2f3c930efab709688d01d23b06d32306becc9bccf8f3e`
- `service_class_codes.csv`: `62102a6b366ebe2a2583ad25c7114d925b78614bc8828070578c8ba5579f4830`
- `record_type_codes.csv`: `df1e64cff8911df719c3881e21b4c63ceb5d641455521a7d9e1b0a778a0424a5`
- `change_codes.csv`: `3127931ae5bd3ebdf91acdbcaab04be953ea29cc7ed755ecc6b5ea0075df9c54`
- `addenda_type_codes.csv`: `6b099ffa26c1e2bf3eba98ba0ccd9f2bb629b4a8a089a353cefd21753e351b9e`

Together the CSVs contain 167 physical rows and 166 distinct identifiers.
Exactly 164 identifiers resolve as current on 2026-08-11; the other identities
are the future-only R90 and historical-only addenda type 01. The second R16
row represents a future meaning of an identifier that already resolves today.

Validation requires the exact headers above, UTF-8 with LF line endings,
nonempty names, deterministic sort order, known statuses, and the exact row
counts above. Codes are unique except for the two non-overlapping R16 lifecycle
rows; return-row identity is `(code, valid_from, valid_to)`. Validation also
confirms that the two planned rows begin on 2028-03-17, that R90 is absent from
earlier resolutions, and that addenda type `01` is the only legacy row.
