# @reffin/iso20022

Offline TypeScript reference data for ISO 20022 External Code Sets, Bank
Transaction Codes, and current message identifiers.

```ts
import { PaymentPurposeCode, resolveCode } from "@reffin/iso20022";

PaymentPurposeCode.SALA.label; // "Salary Payment"
resolveCode("ExternalReturnReason1Code", "AC01")?.label; // "Incorrect Account Number"
```

Short external codes are set-qualified. Unknown values return `undefined`, and
obsolete records are available only when explicitly requested. The package is
an unofficial pinned snapshot, not an XML validator or a replacement for the
current [ISO 20022 Repository](https://www.iso20022.org/).

Public registry publication remains disabled pending the repository release
checklist and selection of a license for Reffin-authored software.
