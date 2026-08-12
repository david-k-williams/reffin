# reffin-iso20022

Offline Python reference data for ISO 20022 External Code Sets, Bank
Transaction Codes, and current message identifiers.

```python
from reffin_iso20022 import PaymentPurposeCode, resolve_code

assert PaymentPurposeCode.SALA.label == "Salary Payment"
assert resolve_code("ExternalReturnReason1Code", "AC01").label == "Incorrect Account Number"
```

Short external codes are set-qualified. Unknown values return `None`, and
obsolete records are available only when explicitly requested. The package is
an unofficial pinned snapshot, not an XML validator or a replacement for the
current [ISO 20022 Repository](https://www.iso20022.org/).

Public registry upload remains disabled pending the repository release
checklist and selection of a license for Reffin-authored software.
