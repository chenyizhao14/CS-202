import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
#from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    def test_is_empty_and_full(self):
        stack = Stack(0)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.is_full())

    def test_is_full_function(self):
        stack = Stack(1)
        stack.push(1)
        self.assertTrue(stack.is_full())

    def test_push_Index_Error(self):
        stack = Stack(1)
        stack.push(1)
        with self.assertRaises(IndexError):
            stack.push(2)

    def test_pop_Index_Error(self):
        stack = Stack(3)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_pop(self):
        stack = Stack(3)
        stack.push(2)
        stack.push(8)
        self.assertEqual(8, stack.pop())
        self.assertEqual(2, stack.pop())

    def test_peek(self):
        stack = Stack(1)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)

    def test_peek_error(self):
        stack = Stack(4)
        with self.assertRaises(IndexError):
            stack.peek()

    def test_size(self):
        stack = Stack(2)
        stack.push(6)
        self.assertEqual(stack.size(), 1)
        stack.push(4)
        self.assertEqual(stack.size(), 2)

if __name__ == '__main__':
    unittest.main()
