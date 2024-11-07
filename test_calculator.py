import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-2, 2), 0)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(3, 0), 3)

    #Subtract
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 2),0)
    
    def test_subtract_neg(self):
        self.assertEqual(self.calc.subtract(-2, 2),4)

    def test_subtract_2neg(self):
        self.assertEqual(self.calc.subtract(-2, -2),0)

    #multiply
    def test_mutiply(self):
        self.assertEqual(self.calc.multiply(2, 2),4)
    
    def test_mutiply_zero(self):
        self.assertEqual(self.calc.multiply(2, 0),0)

    def test_mutiply_neg(self):
        self.assertEqual(self.calc.multiply(2, -2),-4)
    
    def test_mutiply_f_neg(self):
        self.assertEqual(self.calc.multiply(-2, 2),-4)

    #devide
    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 2),1)

    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(2, 0),"Can't divide by zero")

    def test_divide_f_zero(self):
        self.assertEqual(self.calc.divide(0, 2),0)

    def test_divide_neg(self):
        self.assertEqual(self.calc.divide(-2, 2),-1)

    #modulo
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_negative_dividend(self):
        self.assertEqual(self.calc.modulo(-10, 3), -1)

    def test_modulo_zero_dividend(self):
    # Test zero divided by non-zero number, should return 0
        self.assertEqual(self.calc.modulo(0, 3), 0)
        


if __name__ == '__main__':
    unittest.main()