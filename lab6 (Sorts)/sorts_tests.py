import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection(self):
        nums = [10, 34, 52, 1, 354, 21, 235, 121, 543, 232]
        comps = selection_sort(nums)
        self.assertEqual(comps, 45)
        self.assertEqual(nums, [1, 10, 21, 34, 52, 121, 232, 235, 354, 543])

    def test_insertion(self):
        nums = [10, 34, 52, 1, 354, 21, 235, 121, 543, 232]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 20)
        self.assertEqual(nums, [1, 10, 21, 34, 52, 121, 232, 235, 354, 543])

if __name__ == '__main__': 
    unittest.main()
