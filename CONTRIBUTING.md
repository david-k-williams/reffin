# Contributing to Reffin

Thanks for helping improve Reffin. Contributions can include code, reference
data, source research, tests, and documentation.

## Before you begin

- Search existing issues before opening a new one.
- Use the security policy for vulnerabilities; never put an unpatched
  vulnerability or credentials in a public issue.
- Read `docs/data-policy.md` before proposing source data. Every imported data
  set needs clear provenance and a documented distribution basis.
- Keep changes focused. Open an issue before a broad API redesign or a large new
  data domain so the scope can be agreed first.

Participation in this project is governed by the
[Code of Conduct](CODE_OF_CONDUCT.md).

## Development setup

The repository expects:

- Python 3.11 or newer;
- Node.js 22 with npm; and
- a stable Flutter SDK with Dart 3.8 or newer.

Install the TypeScript workspace dependencies with `npm ci`. Before running the
complete test matrix, run `flutter pub get` once in every package under
`packages/flutter/`.

## Changing reference data

Canonical CSV files under `data/` and the generator under `tools/` are the
sources of truth. Do not edit generated Python, TypeScript, or Dart catalogs by
hand.

For a data change:

1. Update the canonical CSV and its source inventory or notice.
2. Run `python3 tools/generate.py`.
3. Review generated changes in all three languages.
4. Run `python3 tools/check_all.py`.

Source URLs should point directly to the authoritative material. Record the
publisher, edition or effective date, applicable terms, and transformation
notes when relevant.

## Code changes

Preserve the equivalent public behavior across Python, TypeScript, and Flutter
unless the pull request clearly documents a language-specific reason. Add or
update tests for externally visible behavior.

Run the complete verification matrix with:

```text
python3 tools/check_all.py
```

For a smaller change, targeted tests are welcome while iterating, but the full
matrix should pass before review.

## Pull requests

In the pull request:

- explain the user-facing reason for the change;
- link related issues;
- identify authoritative sources for data changes;
- list the checks you ran; and
- call out compatibility or package-size effects.

By contributing, you agree that your contribution may be distributed under the
licenses and data terms documented by this repository.
