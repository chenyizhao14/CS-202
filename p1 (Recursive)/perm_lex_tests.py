import unittest
from perm_lex import perm_gen_lex

# Starter test cases - write more!
class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_empty(self):
        self.assertEqual([], perm_gen_lex(''))

    def test_perm_gen_lex_one(self):
        self.assertEqual(['a'], perm_gen_lex('a'))

    def test_perm_gen_lex_two(self):
        self.assertEqual(['ab','ba'], perm_gen_lex('ab'))

    def test_perm_gen_lex_three(self):
        self.assertEqual(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'], perm_gen_lex('abc'))

    def test_perm_gen_lex_four(self):
        self.assertEqual(
            [
                'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba',
            ],
            perm_gen_lex('abcd'),
        )

if __name__ == "__main__":
        unittest.main()
