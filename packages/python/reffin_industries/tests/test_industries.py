from __future__ import annotations

import unittest

from reffin_industries import (
    ALL_INDUSTRIES,
    ALL_NAICS_INDUSTRIES,
    ALL_SIC_INDUSTRIES,
    NAICS_INDUSTRY_COUNT,
    NAICS_VERSION,
    SECTOR_ENTRIES,
    SECTORS,
    SIC_DIVISION_ENTRIES,
    SIC_DIVISIONS,
    SIC_INDUSTRY_COUNT,
    SIC_VERSION,
    IndustryLevel,
    IndustrySector,
    SicDivision,
    SicLevel,
    children_of,
    naics_children_of,
    resolve_naics,
    resolve_industry,
    resolve_sic,
    sic_children_of,
)


class IndustriesTest(unittest.TestCase):
    def test_resolves_hierarchy(self) -> None:
        software = resolve_industry("513210")
        self.assertIsNotNone(software)
        assert software is not None
        self.assertEqual(software.level, IndustryLevel.NATIONAL_INDUSTRY)
        self.assertIsNotNone(software.parent)
        assert software.parent is not None
        self.assertEqual(software.parent.code, "51321")
        self.assertEqual(software.sector, IndustrySector.INFORMATION)
        self.assertEqual(software.sector_entry.code, "51")
        self.assertEqual(software.sector.material_symbol, "language")

    def test_combined_sectors_own_children(self) -> None:
        sector = resolve_industry("31-33")
        self.assertIsNotNone(sector)
        assert sector is not None
        self.assertIn("311", {item.code for item in sector.children})

    def test_catalog_is_complete_and_unknown_safe(self) -> None:
        self.assertEqual(NAICS_VERSION, "2022")
        self.assertEqual(NAICS_INDUSTRY_COUNT, 2125)
        self.assertEqual(len(ALL_INDUSTRIES), NAICS_INDUSTRY_COUNT)
        self.assertEqual(len(SECTORS), 20)
        self.assertEqual(len(SECTOR_ENTRIES), 20)
        self.assertEqual(IndustrySector.try_parse("manufacturing"), IndustrySector.MANUFACTURING)
        self.assertEqual(IndustrySector.from_code("31-33"), IndustrySector.MANUFACTURING)
        self.assertIsNone(resolve_industry("9999999"))

    def test_resolves_sic_hierarchy_and_metadata(self) -> None:
        wheat = resolve_sic("0111")
        self.assertIsNotNone(wheat)
        assert wheat is not None
        self.assertEqual(wheat.title, "Wheat")
        self.assertIs(wheat.level, SicLevel.INDUSTRY)
        self.assertEqual(wheat.level.depth, 4)
        self.assertEqual(wheat.parent.code, "011")
        self.assertIs(wheat.division, SicDivision.AGRICULTURE_FORESTRY_FISHING)
        self.assertEqual(wheat.division_entry.code, "A")
        self.assertEqual(wheat.material_symbol, "agriculture")
        self.assertEqual(
            SicDivision.try_parse("agriculture_forestry_fishing"),
            SicDivision.AGRICULTURE_FORESTRY_FISHING,
        )
        self.assertEqual(
            SicDivision.from_code("A"),
            SicDivision.AGRICULTURE_FORESTRY_FISHING,
        )

    def test_sic_catalog_is_complete_immutable_and_unknown_safe(self) -> None:
        self.assertEqual(SIC_VERSION, "1987")
        self.assertEqual(SIC_INDUSTRY_COUNT, 1524)
        self.assertEqual(len(ALL_SIC_INDUSTRIES), SIC_INDUSTRY_COUNT)
        self.assertEqual(len(SIC_DIVISIONS), 12)
        self.assertEqual(len(SIC_DIVISION_ENTRIES), 12)
        self.assertEqual(
            {item.code for item in sic_children_of("Z")}, set("ABCDEFGHIJK")
        )
        self.assertIsInstance(sic_children_of("Z"), tuple)
        self.assertEqual(sic_children_of("not-a-code"), ())
        self.assertIsNone(resolve_sic("not-a-code"))

    def test_sic_distinguishes_qcew_rollups_from_canonical_industries(self) -> None:
        rollup_codes = {
            item.code
            for item in ALL_SIC_INDUSTRIES
            if item.level is SicLevel.QCEW_ROLLUP
        }
        self.assertEqual(
            rollup_codes,
            {"0740", "0780", "1520", "1540", "4210", "5810", "6510", "7210"},
        )
        rollup = resolve_sic("0740")
        self.assertIsNotNone(rollup)
        assert rollup is not None
        self.assertIs(rollup.level, SicLevel.QCEW_ROLLUP)
        self.assertEqual(rollup.level.depth, 4)

    def test_naics_aliases_preserve_existing_api(self) -> None:
        self.assertIs(ALL_NAICS_INDUSTRIES, ALL_INDUSTRIES)
        self.assertEqual(resolve_naics("513210"), resolve_industry("513210"))
        self.assertEqual(naics_children_of("31-33"), children_of("31-33"))


if __name__ == "__main__":
    unittest.main()
