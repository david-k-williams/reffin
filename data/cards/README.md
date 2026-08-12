# Card reference vocabularies

This directory contains small project-owned vocabularies for normalizing common
card and payment concepts. The values are intentionally provider-neutral and
are suitable for generated enhanced enums. They are not card-scheme rules,
acceptance requirements, risk advice, or an exhaustive registry.

## Stability and fallback values

- IDs are stable lowercase `snake_case` identifiers. Rows are sorted by ID.
- `unknown` means the value was not supplied or could not be determined.
- `other` means the value is known but is outside the named normalized values.
- Consumers should preserve an original provider value separately when one is
  available. A future provider-mapping dataset may add aliases with explicit
  provider, source version, and effective-date metadata.
- Adding a normalized value is expected to be backward-compatible. Renaming or
  removing an ID is a breaking data change.

## Icons, brand assets, and trademarks

`material_symbol` is a generic semantic icon name for Material-based user
interfaces. It is presentation metadata, not a brand mark. Every card network
uses `credit_card` as its generic fallback.

`brand_asset_key` is only an optional lookup key for an asset supplied by an
application. No logos or other brand artwork are included here, and a key does
not grant permission to use a mark. Applications must license, source, and
display brand assets under the applicable owner guidelines and must fall back
to the generic icon when an asset is unavailable. Network and product names may
be trademarks of their respective owners; their inclusion is descriptive and
does not imply affiliation or endorsement.

The network table contains names only. It deliberately contains no IIN/BIN
ranges, PAN-prefix detection, routing rules, or acceptance claims. Code using
these vocabularies should never require or log a full PAN merely to classify a
network.

## Files

- `card_networks.csv`: normalized display names and optional application asset
  keys for a compact set of card networks.
- `funding_types.csv`: how value is funded or repaid. This is separate from the
  intended customer or organization class.
- `form_factors.csv`: physical versus virtual card credential presentation.
  Tokenization and wallet provisioning are separate concepts.
- `product_classes.csv`: broad intended cardholder or program class. It does
  not encode issuer-specific product tiers or rewards programs.
- `payment_method_families.csv`: high-level tender families. A wallet may still
  use another family such as card or bank transfer underneath.
- `transaction_channels.csv`: the customer interaction surface. These values
  do not imply authentication strength, card-entry mode, credential presence,
  recurring use, or merchant/customer initiation.
- `verification_outcomes.csv`: generic outcomes for checks such as address or
  security-code verification. They contain no provider raw codes and do not
  instruct an application to approve or decline a transaction.
- `payment_outcomes.csv`: coarse processing outcomes. They are not a complete
  payment, settlement, refund, dispute, or chargeback lifecycle.

Except for `card_networks.csv`, each file uses the columns `id`, `name`,
`material_symbol`, and `description`. The network file uses `network_id`,
`name`, `material_symbol`, and `brand_asset_key`.

