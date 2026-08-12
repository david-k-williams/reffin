# Currency reference data

`currencies.csv` is a compact, deterministic snapshot of currency metadata from
Unicode CLDR 48.2. It includes current and historical currency identifiers for
which CLDR supplies an English display name.

## Provenance and license

- Upstream project: Unicode Common Locale Data Repository (CLDR)
- Pinned release: 48.2, released 2026-03-17
- Release page: https://cldr.unicode.org/index/downloads
- Pinned archive: https://unicode.org/Public/cldr/48.2/core.zip
- Checksum manifest:
  https://unicode.org/Public/cldr/48.2/hashes/SHASUM512.txt
- Retrieved: 2026-08-11
- License: Unicode License v3 (`Unicode-3.0`), as stated in the archive's
  `LICENSE` file and at https://www.unicode.org/license.txt

The raw archive is intentionally not committed.

### Integrity

- `core.zip` SHA-256:
  `d2844f9dbf6124d11a7b047f5381a467902d82a673be3d658f4c0791ffa0b83b`
- `core.zip` SHA-512:
  `de8660f5371e0fcfd03a42e3b4fc4c686ec6cd602b402f1e3d227844005a54eb7952873894443523837d5828c42874a1a267a19f91ded207a2d166144791fa62`
- The SHA-512 value matches the official manifest entry for `core.zip`.
- `currencies.csv` SHA-256:
  `911b17a281b53b973225bf05819dcdb10d0d074a4745541aba2cbbd30a2f48ce`

## Source files and transformation

The snapshot uses these files from the pinned archive:

- `common/validity/currency.xml` for identifier status;
- `common/main/en.xml` for English display names and English symbol overrides;
- `common/main/root.xml` for inherited symbols, including narrow symbols; and
- `common/supplemental/supplementalData.xml` for fraction rules and territory
  associations.

Rows are sorted by `alpha_code` and written as UTF-8 CSV with LF line endings.
CLDR compact validity ranges are expanded before joining the sources. The
unqualified English `displayName` is used as `name`. English values override
root-locale symbols; a missing English symbol inherits the root value.

`minor_digits` and `minor_rounding` use the currency-specific CLDR fraction
record or CLDR's `DEFAULT` record (`2` digits and `0` rounding). Missing cash
fields inherit the resolved minor-unit values. Rounding values are CLDR
increments in units of the least-significant displayed digit: for example,
cash digits `2` and cash rounding `5` represent rounding to `0.05`.

`active` is `true` only for identifiers with CLDR validity status `regular`.
It is snapshot metadata, not a real-time legal-tender determination. The
`territories` field is the sorted, semicolon-delimited union of CLDR territory
associations across all recorded periods, including historical associations;
the CSV does not preserve each association's dates or tender flag.

CLDR validity contains 308 expanded identifiers. One deprecated identifier,
`XAD`, has fraction metadata but no English currency display name in CLDR 48.2,
so it is intentionally omitted rather than assigned a fabricated name. The
result contains all 307 identifiers with an English display name: 153 regular,
153 deprecated, and one unknown (`XXX`).

## Schema and validation

The exact header is:

```text
alpha_code,name,symbol,narrow_symbol,minor_digits,minor_rounding,cash_digits,cash_rounding,active,territories
```

Validation confirms 307 data rows, unique three-letter uppercase alpha codes,
integer digit and rounding fields, 153 active rows, and no missing validity
status among emitted rows.
