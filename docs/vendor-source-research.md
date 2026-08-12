# Vendor MCC source research

Snapshot date: 2026-08-11.

| Publisher | Best machine-readable source | Coverage | Use in Reffin |
| --- | --- | --- | --- |
| Adyen | [DABstep MCC CSV](https://huggingface.co/datasets/adyen/DABstep/blob/main/data/context/merchant_category_codes.csv) | 769 unique MCC/name rows | Included with CC BY 4.0 attribution. This is benchmark context and a 2024 baseline, not an Adyen production taxonomy. |
| python-iso18245 | [Pinned 1.4.1 data tree](https://github.com/jleclanche/python-iso18245/tree/3b53842ff48318ec01d8d9834ad90ec625e327bc/iso18245/data) | Nine CSVs; 932-code mixed-source union; 18 ISO 2003 ranges | Alipay, American Express, ISO 2003, Mastercard, and USDA views are included in the consolidated catalog. The repository is MIT-licensed but does not provide separate per-dataset grants for the underlying ISO or vendor text. Its older Stripe and Visa snapshots remain comparison-only. |
| Stripe | [OpenAPI](https://github.com/stripe/openapi) plus [Issuing categories](https://docs.stripe.com/issuing/categories) | 295 Issuing keys; the docs map 292 of them to MCCs | The MIT-licensed OpenAPI verifies category-key completeness; Stripe's documentation supplies the MCC mapping and is governed by its site terms. |
| Visa | [April 2026 Merchant Data Standards Manual](https://usa.visa.com/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf) | Full reference; 934 unique MCC/title rows extracted | Included as a pinned vendor view in the consolidated catalog. The source document is marked `VISA PUBLIC` and does not state a separate open-data license. |
| Mastercard | [2 June 2026 Quick Reference Booklet](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-quick-reference-booklet-merchant.pdf) | Full list, 20 broad categories, and an attached MCC spreadsheet | Not imported. The booklet is explicitly proprietary. |
| Square | [Locations API guide](https://developer.squareup.com/docs/locations-api) | 51 unique region-specific MCCs accepted during location initialization | Not imported. It is a supported subset, not a complete taxonomy or openly licensed CSV. |

There is no reliable universal vendor grouping. The project therefore keeps
vendor labels separate and owns a small presentation taxonomy in
`data/merchants/groups.csv`. Those groups provide stable names and icons without claiming
to reproduce a network's interchange, risk, or rewards categories.

The pinned python-iso18245 release is not a canonical ISO or vendor source. It
fills vendor views not otherwise covered by newer pinned sources. Its Visa file
has 885 rows versus 934 in the April 2026 manual used here, and its Stripe file
has 287 rows versus 292 current mapped MCCs here. Its own loader declares
`ISO_VERSION_YEAR = 2003`; ISO
[18245:2003 was withdrawn](https://www.iso.org/standard/33365.html) and replaced
by [ISO 18245:2023](https://www.iso.org/standard/79450.html). ISO's
[copyright policy](https://www.iso.org/copyright.html) and
[license agreement](https://www.iso.org/terms-conditions-licence-agreement.html)
document the source terms. None of the repository's CSVs are copied into
generated packages.

To repeat the code-only comparison against a local checkout of the pinned
release without copying descriptions, run:

```sh
python3 tools/audit_python_iso18245.py /path/to/python-iso18245/iso18245/data
```

Mastercard's booklet says its spreadsheet is available through the HTML
booklet's **Download Attachments** action; it does not expose a stable public
CSV/XLSX URL. It can be used as a local verification source when available.
