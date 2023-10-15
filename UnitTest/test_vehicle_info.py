import unittest
from vehicle_info import VehicleInfo


class TestVehicleInfo(unittest.TestCase):

    def test_compute_tax_default(self):
        v = VehicleInfo("BMW", False, 10000)
        expected_tax = 0.05 * (10000 - 0)  # Default tax exemption is 0
        self.assertEqual(v.compute_tax(), expected_tax)

    def test_compute_tax_with_exemption(self):
        v = VehicleInfo("Audi", True, 15000)
        tax_exemption = 500
        expected_tax = 0.02 * (15000 - tax_exemption)
        self.assertEqual(v.compute_tax(tax_exemption), expected_tax)

    def test_compute_tax_negative_exemption(self):
        v = VehicleInfo("Tesla", True, 20000)
        with self.assertRaises(ValueError):
            v.compute_tax(-100)

    def test_can_lease_within_income_limit(self):
        v = VehicleInfo("Toyota", False, 20000)
        year_income = 30000
        self.assertTrue(v.can_lease(year_income))

    def test_can_lease_exceeds_income_limit(self):
        v = VehicleInfo("Honda", False, 25000)
        year_income = 30000
        self.assertFalse(v.can_lease(year_income))

    def test_can_lease_with_zero_income(self):
        v = VehicleInfo("Nissan", True, 12000)
        year_income = 0
        self.assertTrue(v.can_lease(year_income))

    def test_can_lease_with_negative_income(self):
        v = VehicleInfo("Ford", True, 18000)
        year_income = -5000
        self.assertFalse(v.can_lease(year_income))


if __name__ == '__main__':
    unittest.main()
