from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from datetime import date, datetime

from reffin_ach import (
    CURRENT_RETURN_CODE_COUNT,
    DATA_FINGERPRINT,
    RETURN_CODE_COUNT,
    RETURN_CODE_RECORD_COUNT,
    AchAddendaTypeCode,
    AchCodeStatus,
    AchReturnCode,
    AchServiceClassCode,
    AchTransactionCode,
    resolve_addenda_type_code,
    resolve_return_code,
    resolve_return_code_as_of,
    resolve_service_class_code,
    resolve_transaction_code,
)


class AchTest(unittest.TestCase):
    def test_transaction_and_return_identities_expose_details(self) -> None:
        self.assertEqual(AchTransactionCode.CODE_22.code, "22")
        self.assertEqual(AchTransactionCode.CODE_22.info.direction, "credit")
        self.assertEqual(resolve_transaction_code("22"), AchTransactionCode.CODE_22.info)

        self.assertEqual(AchReturnCode.R22.code, "R22")
        self.assertEqual(AchReturnCode.R22.info.name, "Invalid Individual ID Number")
        self.assertEqual(AchReturnCode.R22.info.material_symbol, "undo")
        self.assertEqual(resolve_return_code("r22"), AchReturnCode.R22.info)

    def test_resolvers_are_safe_and_default_to_reference_date(self) -> None:
        self.assertIsNone(resolve_transaction_code("not-a-code"))
        self.assertIsNone(resolve_return_code("R00"))
        self.assertIsNone(resolve_return_code("R90"))
        planned = resolve_return_code("R90", include_inactive=True)
        self.assertIsNotNone(planned)
        self.assertEqual(planned.status, AchCodeStatus.PLANNED)

    def test_return_versions_resolve_on_nonoverlapping_boundaries(self) -> None:
        before = resolve_return_code_as_of("R16", datetime(2028, 3, 16, 23, 59))
        after = resolve_return_code_as_of("R16", date(2028, 3, 17))
        r90 = resolve_return_code_as_of("R90", date(2028, 3, 17))
        self.assertEqual(before.name, "Account Frozen or Return per OFAC Instruction")
        self.assertEqual(after.name, "Account Frozen")
        self.assertEqual(r90.name, "Return for Sanctions Compliance")

    def test_legacy_addenda_and_accounting_service_class(self) -> None:
        self.assertEqual(AchAddendaTypeCode.CODE_01.code, "01")
        self.assertIsNone(resolve_addenda_type_code("01"))
        legacy = resolve_addenda_type_code("01", include_inactive=True)
        self.assertEqual(legacy.status, AchCodeStatus.LEGACY)

        service = resolve_service_class_code("280")
        self.assertEqual(AchServiceClassCode.CODE_280.info, service)
        self.assertEqual(service.direction, "accounting")

    def test_version_counts_fingerprint_and_immutability(self) -> None:
        self.assertEqual(RETURN_CODE_COUNT, 71)
        self.assertEqual(RETURN_CODE_RECORD_COUNT, 72)
        self.assertEqual(CURRENT_RETURN_CODE_COUNT, 70)
        self.assertRegex(DATA_FINGERPRINT, r"^[0-9a-f]{64}$")
        with self.assertRaises(FrozenInstanceError):
            AchReturnCode.R22.info.name = "changed"


if __name__ == "__main__":
    unittest.main()
