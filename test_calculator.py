# https://github.com/andreahernandezm30/lab10-AHM-PP.git
# Partner 1: Prascheel Patel
# Partner 2: Andrea Hernandez Monserratte
import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 10), 6)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(-2, -5), 3)
        self.assertEqual(sub(0, 7), -7)

######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)

    def test_divide(self):
        self.assertAlmostEqual(div(8, 2), 4.0)
        with self.assertRaises(ZeroDivisionError):
            div(8, 0)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 1000), 3.0)
        self.assertAlmostEqual(log(math.e, math.e), 1.0)

    def test_log_invalid_base(self):# 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10) #base 1 is invalid


     ##########################
    
######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(-1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(16), 4.0)
        with self.assertRaises(ValueError):
            square_root(-9)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
