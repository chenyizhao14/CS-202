import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):
    TEST_LIST = [2, 4, 5, 6, 8, 9, 19, 29, 30]

    def test_max_list_iter_none(self):
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(None)

    def test_max_list_iter_empty(self):
        self.assertIsNone(max_list_iter([]))

    def test_max_list_iter_one(self):
        self.assertEqual(max_list_iter([2]), 2)

    def test_max_list_iter_first(self):
        self.assertEqual(max_list_iter([10, 2, 4, 6, 0]), 10)

    def test_max_list_iter_last(self):
        self.assertEqual(max_list_iter([1, 9, 20, -5, 98]), 98)

    def test_max_list_iter_mid(self):
        self.assertEqual(max_list_iter([1, 2, 5, -4, -9]), 5)

    def test_reverse_rec_none(self):
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_reverse_rec_empty(self):
        self.assertEqual(reverse_rec([]), [])

    def test_reverse_rec_one(self):
        self.assertEqual(reverse_rec([1]), [1])

    def test_reverse_rec_some(self):
        self.assertEqual(reverse_rec([10, 20, 30, 40, 50]), [50, 40, 30, 20, 10])

    def test_bin_search_none(self):
        with self.assertRaises(ValueError):
            bin_search(1, 0, 10, None)

    def test_bin_search_empty(self):
        self.assertIsNone(bin_search(1, 0, 0, []))

    def test_bin_search_before(self):
        self.assertIsNone(bin_search(-4, 0, 5, [1, 4, 5, 6, 7, 8]))

    def test_bin_search_after(self):
        self.assertIsNone(bin_search(14, 0, 5, [1, 4, 5, 6, 7, 8]))

    def test_bin_search_reverse(self):
        self.assertIsNone(bin_search(10, 2, 1, [2, 4, 10]))

    def test_bin_search_mid(self):
        self.assertEqual(bin_search(8, 0, len(self.TEST_LIST) - 1, self.TEST_LIST), 4)

    def test_bin_search_first_half(self):
        self.assertEqual(bin_search(4, 0, len(self.TEST_LIST) - 1, self.TEST_LIST), 1)

    def test_bin_search_second_half(self):
        self.assertEqual(bin_search(29, 0, len(self.TEST_LIST) - 1, self.TEST_LIST), 7)

    def test_bin_search_first(self):
        self.assertEqual(bin_search(2, 0, len(self.TEST_LIST) - 1, self.TEST_LIST), 0)

    def test_bin_search_last(self):
        self.assertEqual(bin_search(30, 0, len(self.TEST_LIST) - 1, self.TEST_LIST), 8)

    def test_reverse_list_mutate_none(self):
        with self.assertRaises(ValueError):
            reverse_list_mutate(None)

    def test_reverse_list_mutate_empty(self):
        x = []
        self.assertIsNone(reverse_list_mutate(x))
        self.assertEqual(x, [])

    def test_reverse_list_mutate_one(self):
        x = [1]
        self.assertIsNone(reverse_list_mutate(x))
        self.assertEqual(x, [1])

    def test_reverse_list_mutate_some(self):
        x = [1, 4, 5]
        self.assertIsNone(reverse_list_mutate(x))
        self.assertEqual(x, [5, 4, 1])


if __name__ == "__main__":
        unittest.main()

    
