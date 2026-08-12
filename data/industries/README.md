# U.S. industry classifications

`naics_2022.csv` is the complete hierarchy from the U.S. Census Bureau's 2022
North American Industry Classification System structure workbook.

`sectors.csv` adds project-authored stable IDs, descriptions, and generic
Material icon keys for the 20 top-level sectors. These presentation fields are
not part of the Census source and do not alter the NAICS hierarchy.

## Provenance and reuse

- Publisher: U.S. Census Bureau
- Version: 2022 NAICS
- Source page: https://www.census.gov/naics/?input=nationwide&year=2022
- Source workbook:
  https://www.census.gov/naics/2022NAICS/2022_NAICS_Structure.xlsx
- Retrieved: 2026-08-11
- Census data-product policy:
  https://www2.census.gov/foia/ds_policies/ds027.pdf

The Census Bureau states that works created by its employees are generally not
subject to copyright protection in the United States, while third-party or
contractor material may be protected. This snapshot uses the Census-published
U.S. structure table and retains source attribution. NAICS was developed with
Statistics Canada and Mexico's INEGI; this file does not incorporate separate
Canadian or Mexican publications.

The raw workbook is intentionally not committed.

### Integrity

- `2022_NAICS_Structure.xlsx` SHA-256:
  `217c9e0d4d74e7517bc288f5f308b73aa0de5ee787976a6dd222412be28ada22`
- `naics_2022.csv` SHA-256:
  `032ec463fbd155c2bb536fffe714ff134e1e72758d25632c258aba4893846bf8`

The Census download page does not publish a checksum for this workbook; the
input hash records the exact bytes used for this snapshot.

## Transformation

- Read worksheet rows after the title, note, and header rows.
- Skip 19 blank separator rows and retain all 2,125 rows containing a code.
- Trim code and title whitespace.
- Remove the source workbook's trailing `T` trilateral-agreement marker from
  799 titles. The marker is metadata described by the workbook, not part of the
  industry title.
- Omit the change-indicator column because it describes changes from the prior
  NAICS edition rather than the 2022 hierarchy.
- Preserve the workbook's hierarchy order and the combined sector codes
  `31-33`, `44-45`, and `48-49`.
- Set `level` to the hierarchy depth (`2` through `6`). Combined sectors are
  level 2.
- Set `parent` to the immediate containing code. Three-digit children of a
  combined sector point to the combined sector code.
- Set `sector` to the containing two-digit or combined sector for every row.
- Write deterministic UTF-8 CSV with LF line endings.

## Schema and validation

The exact header is:

```text
code,title,level,parent,sector
```

The CSV contains 2,125 unique codes:

- 20 sectors at level 2 (17 single codes and three combined ranges);
- 96 subsectors at level 3;
- 308 industry groups at level 4;
- 689 NAICS industries at level 5; and
- 1,012 national industries at level 6.

Validation confirms that every non-sector row has an existing immediate
parent, every row references an existing sector, titles are nonempty, and all
codes match the expected 2-6 digit or combined-sector format.

The sector presentation table is sorted by its stable `sector_id`; every NAICS
sector occurs exactly once and every icon key has a native Flutter mapping.

## Historical SIC lookup

`sic_1987.csv` is a project-derived slice of the BLS QCEW composite SIC title
table. BLS uses the 1972 SIC edition for data from 1975 through 1987 and the
1987 edition for data from 1988 through 2000. The upstream table mixes both;
Reffin retains rows not explicitly prefixed `1972 SIC`. The result contains the
1987 four-digit code set plus BLS QCEW hierarchy and rollup rows. It is not a
current industry classification.

### Provenance and reuse

- Publisher: U.S. Bureau of Labor Statistics
- Source page:
  https://www.bls.gov/cew/classifications/industry/sic-industry-titles.htm
- Source CSV:
  https://www.bls.gov/cew/classifications/industry/sic-industry-titles-csv.csv
- 1987 SIC manual comparison:
  https://www.osha.gov/data/sic-manual
- Retrieved: 2026-08-11
- BLS copyright and linking policy:
  https://www.bls.gov/bls/linksite.htm#copyright

BLS states that its published material is public domain except for previously
copyrighted photographs and illustrations, and asks users to cite BLS as the
source. This data snapshot contains only the agency's text table and retains
that attribution.

The BLS server rejected non-browser retrieval during this import. The official
HTML table was therefore exported as three text columns and normalized with
`tools/import_bls_sic.py`. The temporary raw export is not committed.

### Integrity and transformation

- Browser-exported BLS table JSON SHA-256:
  `849d8b3061faff486aea4f890ffaea647c5b24bc6c821b7bdcfcf79c4ffe29cd`
- `sic_1987.csv` SHA-256:
  `97e87918e57fa1c369b3e9c0d91927bfe4937d4809b78cf7638da5717d351737`
- `sic_divisions.csv` SHA-256:
  `81934bf203ccbcf320ff68b43e4dacd392b2c6398b6af4f9930ba25d40fb15ef`

The import reads all 1,749 upstream rows, removes 225 rows whose title is
explicitly prefixed `1972 SIC`, strips the remaining `SIC <code>` title prefix,
and retains 1,524 unique entries: 12 BLS hierarchy containers, 83 major groups,
416 industry groups, 1,005 four-digit SIC industries, and eight four-digit QCEW
rollups. The rollups are `0740`, `0780`, `1520`, `1540`, `4210`, `5810`, `6510`,
and `7210`; they have the explicit `qcew_rollup` level. Leading zeroes are
preserved. Every non-root entry references an existing parent and one of the 12
division records.

The 12 top-level records are the ten 1987 SIC divisions A-J plus the BLS QCEW
containers `Z` (All Industries) and `K` (Nonclassifiable Establishments). This
hierarchy follows the BLS QCEW table; it must not be described as the canonical
1987 SIC manual hierarchy. In particular, the BLS table places Major Group 99
under `K`, while the manual places it in Division J.

`sic_divisions.csv` adds project-authored stable IDs, descriptions, and generic
Material icon keys. It does not change the historical BLS QCEW hierarchy.

The normalized schema is:

```text
code,title,level,parent,division
```
