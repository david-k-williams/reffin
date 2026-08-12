from __future__ import annotations

import unittest

from reffin_merchants import (
    ALL_RECORDS,
    ALL_SOURCES,
    DATA_FINGERPRINT,
    Mcc,
    MccGroup,
    MccVendor,
    records_for_mcc,
    resolve_mcc,
    resolve_source,
    resolve_vendor_key,
)


class CatalogTest(unittest.TestCase):
    def test_snapshot_metadata(self) -> None:
        self.assertEqual(len(DATA_FINGERPRINT), 64)
        self.assertEqual(len(ALL_RECORDS), 4970)
        self.assertEqual(len(ALL_SOURCES), 6)
        adyen = resolve_source("adyen_dabstep_07d7d7ea")
        self.assertIsNotNone(adyen)
        assert adyen is not None
        self.assertEqual(adyen.license, "CC-BY-4.0")
        python_iso = resolve_source("python_iso18245_3b53842")
        self.assertIsNotNone(python_iso)
        assert python_iso is not None
        self.assertEqual(python_iso.status, "imported")
        self.assertEqual(python_iso.redistribution, "fair_use_reference")
        self.assertEqual(MccVendor.try_parse("visa"), MccVendor.VISA)
        self.assertEqual(
            MccVendor.try_parse("american_express"),
            MccVendor.AMERICAN_EXPRESS,
        )
        self.assertEqual(MccGroup.try_parse("food_and_drink"), MccGroup.FOOD_AND_DRINK)
        self.assertIsNone(MccVendor.try_parse("missing"))

    def test_preserves_leading_zero_mcc(self) -> None:
        self.assertEqual(Mcc.try_parse("0742"), Mcc.MCC_0742)
        self.assertIsNone(Mcc.try_parse("742"))
        details = Mcc.MCC_0742.resolve(MccVendor.VISA)
        self.assertIsNotNone(details)
        assert details is not None
        self.assertEqual(details.name, "Veterinary Services")
        self.assertEqual(details.group, MccGroup.AGRICULTURE)

    def test_vendor_specific_name_and_key(self) -> None:
        stripe = resolve_vendor_key(MccVendor.STRIPE, "eating_places_restaurants")
        self.assertIsNotNone(stripe)
        assert stripe is not None
        self.assertEqual(stripe.mcc, Mcc.MCC_5812)
        self.assertEqual(stripe.name, "Eating Places, Restaurants")
        self.assertEqual(stripe.group, MccGroup.FOOD_AND_DRINK)
        self.assertEqual(stripe.icon_key, "restaurant")
        self.assertEqual(stripe.group.material_symbol, "restaurant")
        self.assertEqual(stripe.source, resolve_source(stripe.source_id))

        visa = resolve_mcc("5812", MccVendor.VISA)
        self.assertIsNotNone(visa)
        assert visa is not None
        self.assertEqual(visa.name, "Eating Places and Restaurants")

        expected_names = {
            MccVendor.ALIPAY: "Eating places and restaurants",
            MccVendor.AMERICAN_EXPRESS: "Eating Places and Restaurants",
            MccVendor.ISO18245: "Eating places and restaurants",
            MccVendor.MASTERCARD: "Eating Places, Restaurants",
            MccVendor.USDA: "Eating places and Restaurants",
        }
        for vendor, name in expected_names.items():
            details = resolve_mcc("5812", vendor)
            self.assertIsNotNone(details, vendor)
            assert details is not None
            self.assertEqual(details.name, name)
            self.assertEqual(details.group, MccGroup.FOOD_AND_DRINK)

    def test_network_private_mcc_group_overrides(self) -> None:
        expected = {
            "3998": MccGroup.TRANSPORTATION,
            "4733": MccGroup.ENTERTAINMENT,
            "7013": MccGroup.REAL_ESTATE,
            "7280": MccGroup.HEALTHCARE,
            "8912": MccGroup.HOME_AND_GARDEN,
        }
        for code, group in expected.items():
            details = resolve_mcc(code, MccVendor.AMERICAN_EXPRESS)
            self.assertIsNotNone(details, code)
            assert details is not None
            self.assertEqual(details.group, group, code)

    def test_vendor_only_category_can_have_no_mcc(self) -> None:
        details = resolve_vendor_key(MccVendor.STRIPE, "miscellaneous")
        self.assertIsNotNone(details)
        assert details is not None
        self.assertIsNone(details.mcc)
        self.assertEqual(details.group, MccGroup.OTHER)

    def test_invalid_and_unknown_values_are_safe(self) -> None:
        self.assertIsNone(resolve_mcc("742", MccVendor.VISA))
        self.assertIsNone(resolve_mcc("abcd", MccVendor.VISA))
        self.assertIsNone(resolve_mcc("0000", MccVendor.VISA))
        self.assertGreaterEqual(len(records_for_mcc("5812")), 3)

    def test_every_four_digit_input_is_safe(self) -> None:
        for value in range(10_000):
            code = f"{value:04d}"
            for vendor in MccVendor:
                details = resolve_mcc(code, vendor)
                if details is not None:
                    self.assertEqual(details.mcc.value, code)

    def test_semantic_group_overrides(self) -> None:
        expected = {
            "2842": MccGroup.WHOLESALE,
            "5046": MccGroup.WHOLESALE,
            "5262": MccGroup.GENERAL_RETAIL,
            "5733": MccGroup.SPECIALTY_RETAIL,
            "5735": MccGroup.SPECIALTY_RETAIL,
            "5960": MccGroup.FINANCIAL_SERVICES,
            "7276": MccGroup.PROFESSIONAL_SERVICES,
            "7511": MccGroup.AUTOMOTIVE,
            "7623": MccGroup.REPAIR_SERVICES,
            "7629": MccGroup.REPAIR_SERVICES,
        }
        for code, group in expected.items():
            details = resolve_mcc(code, MccVendor.ADYEN_DABSTEP)
            self.assertIsNotNone(details, code)
            assert details is not None
            self.assertEqual(details.group, group, code)

        stripe_truck_stop = resolve_vendor_key(
            MccVendor.STRIPE,
            "truck_stop_iteration",
        )
        self.assertEqual(stripe_truck_stop.group, MccGroup.AUTOMOTIVE)


if __name__ == "__main__":
    unittest.main()
