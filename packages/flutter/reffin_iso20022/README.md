# reffin_iso20022

Offline Dart and Flutter reference data for ISO 20022 External Code Sets, Bank
Transaction Codes, and current message identifiers.

```dart
import 'package:reffin_iso20022/reffin_iso20022.dart';

Text(PaymentPurposeCode.sala.label); // Salary Payment
Icon(PaymentPurposeCode.sala.icon);  // native Material icon
```

Short external codes are set-qualified. Unknown values return `null`, and
obsolete records are available only when explicitly requested. The package is
an unofficial pinned snapshot, not an XML validator or a replacement for the
current [ISO 20022 Repository](https://www.iso20022.org/).

`publish_to: none` remains set pending the repository release checklist and
selection of a license for Reffin-authored software.
