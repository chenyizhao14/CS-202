import unittest
from location import *

class TestLab1(unittest.TestCase):
    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location(SLO, 35.3, -120.7)")

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("SLO", 35.0 + 0.1 + 0.1 + 0.1, -120.7)
        loc4 = Location("Paris", 48.9, 2.4)
        self.assertEqual(loc1, loc2)
        self.assertEqual(loc1, loc3)
        self.assertNotEqual(loc2, loc4)

    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name, "SLO")
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.lon, -120.7)

if __name__ == "__main__":
        unittest.main()
