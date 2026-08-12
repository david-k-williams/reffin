from __future__ import annotations

import unittest

from reffin_currencies import ALL_CURRENCIES, CLDR_VERSION, Currency, resolve_currency


class CurrencyTest(unittest.TestCase):
    def test_resolves_case_insensitively(self) -> None:
        usd = resolve_currency("usd")
        self.assertIsNotNone(usd)
        assert usd is not None
        self.assertEqual(usd.code, "USD")
        self.assertEqual(usd.minor_digits, 2)
        self.assertEqual(usd.display_symbol, "$")
        self.assertEqual(Currency.USD.display_symbol, "$")
        self.assertIn("US", usd.territories)
        self.assertEqual(CLDR_VERSION, "48.2")

    def test_supports_zero_decimal_and_cash_rounding(self) -> None:
        self.assertEqual(Currency.JPY.info.minor_digits, 0)
        self.assertEqual(Currency.CHF.info.cash_rounding, 5)

    def test_preserves_historic_values_and_safe_unknowns(self) -> None:
        self.assertFalse(Currency.DEM.info.active)
        self.assertIsNone(resolve_currency("NOPE"))
        self.assertEqual(len(ALL_CURRENCIES), len(Currency))


if __name__ == "__main__":
    unittest.main()
