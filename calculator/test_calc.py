import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)

    def test_div(self):
        self.assertEqual(self.calc.div(10, 2), 5)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(5, 0)

    def test_pow(self):
        self.assertEqual(self.calc.pow(2, 3), 8)

    def test_pow_negative_exponent(self):
        self.assertEqual(self.calc.pow(2, -3), 0.125)

    def test_pow_zero_base(self):
        self.assertEqual(self.calc.pow(0, 5), 0)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)

if __name__ == '__main__':
    unittest.main()
