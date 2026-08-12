from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError

from reffin_iso20022 import (
    BANK_TRANSACTION_CODE_RECORD_COUNT,
    CODE_SET_COUNT,
    CURRENT_EXTERNAL_CODE_COUNT,
    DATA_FINGERPRINT,
    EXTERNAL_CODE_IDENTITY_COUNT,
    EXTERNAL_CODE_RECORD_COUNT,
    EXTERNAL_CODE_SETS_ARTIFACT_VERSION,
    EXTERNAL_CODE_SETS_VERSION,
    BANK_TRANSACTION_CODES_VERSION,
    MESSAGE_DEFINITION_COUNT,
    MESSAGE_DEFINITIONS_VERSION,
    PAYMENT_CODE_COUNT,
    LocalInstrumentCode,
    PaymentPurposeCode,
    PaymentReturnReasonCode,
    find_codes,
    find_message_definitions,
    records_for,
    resolve_bank_transaction_code,
    resolve_code,
    resolve_message_identifier,
    search_codes,
)


class Iso20022Test(unittest.TestCase):
    def test_catalog_counts_and_qualified_resolution(self) -> None:
        self.assertEqual(CODE_SET_COUNT, 158)
        self.assertEqual(EXTERNAL_CODE_RECORD_COUNT, 3_246)
        self.assertEqual(EXTERNAL_CODE_IDENTITY_COUNT, 3_245)
        self.assertEqual(CURRENT_EXTERNAL_CODE_COUNT, 3_213)
        self.assertEqual(PAYMENT_CODE_COUNT, 950)
        self.assertRegex(DATA_FINGERPRINT, r"^[0-9a-f]{64}$")
        self.assertEqual(EXTERNAL_CODE_SETS_VERSION, "May 2026 v1")
        self.assertEqual(EXTERNAL_CODE_SETS_ARTIFACT_VERSION, "1Q2026_externalcodesets_v1")
        self.assertEqual(BANK_TRANSACTION_CODES_VERSION, "2025-11-30")
        self.assertEqual(MESSAGE_DEFINITIONS_VERSION, "2026-06-26")
        self.assertEqual(
            resolve_code("ExternalReturnReason1Code", "AC01").label,
            "Incorrect Account Number",
        )
        self.assertIsNone(resolve_code("ExternalReturnReason1Code", "not-a-code"))

    def test_code_search_is_set_qualified_and_history_is_explicit(self) -> None:
        ac01 = find_codes("ac01")
        self.assertGreaterEqual(len(ac01), 3)
        self.assertEqual(len({item.code_set for item in ac01}), len(ac01))
        history = records_for(
            "ExternalLocalInstrument1Code", "CTP", include_obsolete=True
        )
        self.assertEqual(len(history), 2)
        self.assertEqual(LocalInstrumentCode.CTP.label, "Credit Transfer Preferred")
        self.assertEqual(records_for("ExternalLocalInstrument1Code", "CTP"), (history[1],))
        self.assertEqual(len(search_codes("salary", limit=3)), 3)

    def test_payment_enhanced_enums(self) -> None:
        self.assertEqual(PaymentPurposeCode.SALA.code, "SALA")
        self.assertEqual(PaymentPurposeCode.SALA.label, "Salary Payment")
        self.assertEqual(PaymentPurposeCode.SALA.material_symbol, "payments")
        self.assertEqual(PaymentReturnReasonCode.AC01.material_symbol, "undo")
        self.assertIs(PaymentPurposeCode.try_parse(" sala "), PaymentPurposeCode.SALA)
        with self.assertRaises(FrozenInstanceError):
            PaymentPurposeCode.SALA.info.label = "changed"

    def test_btc_and_message_identifier_resolvers(self) -> None:
        self.assertGreater(BANK_TRANSACTION_CODE_RECORD_COUNT, 1_000)
        first = resolve_bank_transaction_code("SECU", "CASH", "CPEN")
        self.assertEqual(len(first), 2)
        message = resolve_message_identifier("pacs.008.001.14")
        self.assertIsNotNone(message)
        self.assertEqual(message.business_area, "pacs")
        self.assertEqual(message.version, "14")
        self.assertIsNone(resolve_message_identifier("pacs.008.001"))
        self.assertEqual(MESSAGE_DEFINITION_COUNT, 797)
        self.assertTrue(find_message_definitions(business_area="pacs"))


if __name__ == "__main__":
    unittest.main()
