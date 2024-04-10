import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(6)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0) 
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0) # Causes rehash        
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_index("v"), 16)

    def test_prime(self):
        ht = HashTable(8)
        self.assertEqual(11, ht.get_table_size())

    def test_replace_value(self):
        ht = HashTable(3)
        ht.insert("v", 0)
        ht.insert("v", 2)
        self.assertEqual(ht.get_value("v"), 2)

    def test_low_table_size(self):
        ht = HashTable(1)
        self.assertEqual(ht.table_size, 2)

    def test_primes(self):
        ht = HashTable(9)
        ht.next_prime(48)

    def test_in_table(self):
        ht = HashTable(5)
        ht.insert("a", 0)
        ht.insert("f", 2)
        self.assertTrue(ht.in_table("a"))
        self.assertTrue(ht.in_table("f"))
        self.assertFalse(ht.in_table("k"))
        self.assertFalse(ht.in_table("x"))

    def test_get_index(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        ht.insert("h", 2)
        ht.insert("p", 10)
        self.assertEqual(ht.get_index("a"), 6)
        self.assertEqual(ht.get_index("h"), 0)
        self.assertIsNone(ht.get_index("f"))
        self.assertIsNone(ht.get_index("o"))
        self.assertFalse(ht.get_index("o"))

    def test_get_value(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        ht.insert("h", 2)
        self.assertEqual(ht.get_value("a"), 0)
        self.assertEqual(ht.get_value("h"), 2)
        self.assertIsNone(ht.get_value("o"))
        self.assertIsNone(ht.get_value("b"))
        self.assertIsNone(ht.get_value("c"))
        self.assertIsNone(ht.get_value("d"))
        ht.insert("o", 10)
        self.assertEqual(ht.get_value("o"), 10)

if __name__ == '__main__':
   unittest.main()
