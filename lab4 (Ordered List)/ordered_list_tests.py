import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_less_than(self):
        x = OrderedList()
        x.add(1)
        x.add(1.01)
        x.add(0.99)
        self.assertEqual([0.99, 1, 1.01], x.python_list())

    def test_is_empty(self):
        a_list = OrderedList()
        self.assertTrue(a_list.is_empty())

    def test_add(self):
        b_list = OrderedList()
        b_list.add(10)
        self.assertFalse(b_list.add(10))

    def test_add_false(self):
        b_list = OrderedList()
        b_list.add(5)
        b_list.add(10)
        b_list.add(7)
        b_list.add(15)
        self.assertFalse(b_list.add(15))

    def test_remove_items_and_false(self):
        r_list = OrderedList()
        r_list.add(-10)
        r_list.add(20)
        self.assertTrue(r_list.remove(-10))
        r_list.add(30)
        r_list.add(40)
        r_list.add(50)
        self.assertTrue(r_list.remove(30))
        self.assertTrue(r_list.remove(50))
        self.assertFalse(r_list.remove(100))

    def test_index_base(self):
        i_list = OrderedList()
        i_list.add(3.9)
        i_list.add(89)
        i_list.add(87)
        self.assertEqual(2, i_list.index(89))
        self.assertEqual(0, i_list.index(3.9))
        self.assertIsNone(i_list.index(90))

    def test_pop_errors(self):
        p_list = OrderedList()
        p_list.add(8)
        with self.assertRaises(IndexError):
            p_list.pop(-2)

    def test_pop(self):
        p_list = OrderedList()
        p_list.add(99)
        p_list.add(8)
        p_list.add(10)
        p_list.add(6)
        p_list.add(1)
        self.assertEqual(1, p_list.pop(0))
        self.assertEqual(10, p_list.pop(2))
        self.assertEqual(99, p_list.pop(2))

    def test_search_true_and_false(self):
        s_list = OrderedList()
        s_list.add(-10)
        s_list.add(9)
        s_list.add(10)
        self.assertTrue(s_list.search(9))
        self.assertFalse(s_list.search(10.5))

    def test_list_python_list(self):
        c_list = OrderedList()
        self.assertEqual([], c_list.python_list())
        c_list.add(2)
        self.assertEqual([2], c_list.python_list())
        c_list.add(10)
        c_list.add(-10)
        self.assertEqual([-10, 2, 10], c_list.python_list())

    def test_list_reversed(self):
        d_list = OrderedList()
        d_list.add(4)
        d_list.add(2)
        d_list.add(6)
        d_list.add(-10)
        self.assertEqual([6, 4, 2, -10], d_list.python_list_reversed())

    def test_size(self):
        a_list = OrderedList()
        self.assertEqual(0, a_list.size())


if __name__ == '__main__': 
    unittest.main()
