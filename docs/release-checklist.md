# Reffin release checklist

The repository is intentionally safe-by-default: npm packages are `private`,
Dart packages use `publish_to: none`, and Python packages carry PyPI's
`Private :: Do Not Upload` classifier. Do not remove those gates until the
steps below are complete for the specific artifact being released.

1. Preserve the root Apache License 2.0 scope for Reffin-authored software,
   documentation, and project-authored metadata. Do not apply it to or present
   it as relicensing third-party data or marks.
2. Add the artifact's README, changelog, Apache license, applicable third-party
   notices, and complete source provenance to its Python, npm, and Dart package
   payloads. Currency packages must carry the full Unicode License v3 text;
   merchant packages containing the Adyen derivative must carry the CC BY 4.0
   text, attribution, source URI, and change notice.
3. For a merchant registry release, verify that the payload contains only the
   reviewed snapshot and preserves the documented fair-use reference notice
   for Stripe-, Visa-, and `python-iso18245`-derived mappings. Public repository
   approval is not automatic registry-release clearance, and green tests do
   not establish notice completeness.
4. Reserve the intended PyPI names, npm scope/packages, and pub.dev names, then
   add registry metadata and release-build hooks.
5. Run `python3 tools/check_all.py` from a clean dependency install and inspect
   Python wheels, npm tarballs, and Dart dry-run payloads before publishing.
6. Release from a clean, reviewed, tagged commit and record the source-data
   fingerprints in the release notes.

ACH, cards, currencies, industries, and merchants can move through this
checklist independently. The current ACH snapshot is approved for public
repository redistribution under the project's documented fair-use reference
approach. Before a registry release, confirm that descriptions remain concise
project-authored reference metadata and that the package does not reproduce
operating-rule prose, authorization requirements, return timeframes, or
compliance instructions. Reassess the decision if the package payload, source,
scope, or intended distribution changes; the reference approach is not an
upstream license grant. Enabling one artifact does not authorize another.

ISO 20022 can also move through this checklist independently of merchants. Its
release must include the ISO 20022 attribution, source release and artifact
identifiers, archive hashes, and an explicit statement that Reffin is an
unofficial offline snapshot. Confirm the package does not imply that its data
is the official or latest Repository and does not redistribute XML schemas as
a validation SDK.
