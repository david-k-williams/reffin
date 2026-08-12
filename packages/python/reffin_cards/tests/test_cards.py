from __future__ import annotations

import unittest

from reffin_cards import (
    COUNTS,
    DATA_FINGERPRINT,
    RECORDS,
    CardNetwork,
    FormFactor,
    FundingType,
    PaymentMethodFamily,
    PaymentOutcome,
    ProductClass,
    TransactionChannel,
    VerificationOutcome,
)


class CardsTest(unittest.TestCase):
    def test_network_metadata_and_optional_brand_asset(self) -> None:
        self.assertEqual(CardNetwork.VISA.id, "visa")
        self.assertEqual(CardNetwork.VISA.name, "VISA")
        self.assertEqual(CardNetwork.VISA.label, "Visa")
        self.assertEqual(CardNetwork.VISA.material_symbol, "credit_card")
        self.assertEqual(CardNetwork.VISA.brand_asset_key, "visa")
        self.assertIsNone(CardNetwork.OTHER.brand_asset_key)
        self.assertIsNone(CardNetwork.UNKNOWN.brand_asset_key)

    def test_every_vocabulary_has_safe_id_parsing(self) -> None:
        enum_types = (
            CardNetwork,
            FormFactor,
            FundingType,
            PaymentMethodFamily,
            PaymentOutcome,
            ProductClass,
            TransactionChannel,
            VerificationOutcome,
        )
        for enum_type in enum_types:
            for member in enum_type:
                self.assertIs(enum_type.try_parse(member.id), member)
            self.assertIsNone(enum_type.try_parse("not_a_real_value"))
            self.assertIsNone(enum_type.try_parse(None))

    def test_described_values_expose_semantic_metadata(self) -> None:
        self.assertEqual(FundingType.CREDIT.label, "Credit")
        self.assertEqual(FundingType.CREDIT.material_symbol, "credit_score")
        self.assertIn("credit agreement", FundingType.CREDIT.description)
        self.assertEqual(FormFactor.VIRTUAL.material_symbol, "devices")
        self.assertEqual(PaymentMethodFamily.CARD.label, "Card")
        self.assertEqual(PaymentOutcome.APPROVED.material_symbol, "check_circle")
        self.assertEqual(ProductClass.COMMERCIAL.material_symbol, "business")
        self.assertEqual(TransactionChannel.IN_PERSON.material_symbol, "point_of_sale")
        self.assertEqual(VerificationOutcome.MATCH.material_symbol, "verified")

    def test_generated_records_counts_and_fingerprint(self) -> None:
        expected_counts = {
            "card_networks": 16,
            "form_factors": 4,
            "funding_types": 6,
            "payment_method_families": 12,
            "payment_outcomes": 8,
            "product_classes": 5,
            "transaction_channels": 7,
            "verification_outcomes": 10,
        }
        self.assertEqual(dict(COUNTS), expected_counts)
        self.assertEqual(
            {dataset: len(values) for dataset, values in RECORDS.items()},
            expected_counts,
        )
        self.assertEqual(len(DATA_FINGERPRINT), 64)
        self.assertTrue(all(character in "0123456789abcdef" for character in DATA_FINGERPRINT))
        self.assertIsInstance(RECORDS["card_networks"], tuple)


if __name__ == "__main__":
    unittest.main()
