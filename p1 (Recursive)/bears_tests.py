import unittest
from bears import *

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):
    def test_bear_branches(self):
        self.assertTrue(bears(250))

    def test_bear_attempt(self):
        self.assertFalse(bears(100))

    def test_bear_base(self):
        self.assertTrue(bears(42))

    def test_bear_prime(self):
        self.assertFalse(bears(53))

    def test_bear_prime2(self):
        self.assertFalse(bears(41))

if __name__ == "__main__":
    unittest.main()
