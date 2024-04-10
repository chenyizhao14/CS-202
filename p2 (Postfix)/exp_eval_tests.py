# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_plus(self):
        self.assertAlmostEqual(postfix_eval("3  5 +"), 8)

    def test_postfix_eval_string(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_insufficient_operands(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_too_many_operands(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_empty(self):
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Empty input")

    def test_postfix_eval_minus(self):
        self.assertEqual(6, postfix_eval("9 3 -"))

    def test_postfix_eval_multiply(self):
        self.assertEqual(16, postfix_eval("2 2 4 * *"))

    def test_postfix_eval_division(self):
        self.assertEqual(5, postfix_eval("100 10 / 2 /"))

    def test_postfix_eval_power(self):
        self.assertEqual(8, postfix_eval("2 3 **"))

    def test_postfix_eval_shift_right(self):
        self.assertEqual(11, postfix_eval("22 1 >>"))

    def test_postfix_eval_shift_left(self):
        self.assertEqual(40, postfix_eval("10 2 <<"))

    def test_postfix_eval_rshift_errors(self):
        try:
            postfix_eval("9.0 1.0 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_lshift_errors(self):
        try:
            postfix_eval("9.0 1.0 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_divide_by_0(self):
        with self.assertRaises(ZeroDivisionError):
            postfix_eval("9 0 /")

    def test_infix_to_postfix_simple(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_parenthesis(self):
        self.assertEqual("2 4 2 + *", infix_to_postfix("2 * ( 4 + 2 )"))

    def test_infix_postfix_precedence(self):
        self.assertEqual("9 9 10 * + 8 2 ** 10 + -", infix_to_postfix("9 + 9 * 10 - ( 8 ** 2 + 10 )"))
        
    def test_prefix_to_postfix_working(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

if __name__ == "__main__":
    unittest.main()
