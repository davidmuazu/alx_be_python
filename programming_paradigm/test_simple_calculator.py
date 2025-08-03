import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_division(self):
        """test the division method"""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(2, 0), None)
        self.assertEqual(self.calc.divide(7, 3), 2.33)
        self.assertEqual(self.calc.divide(6, 1), 1)

    def test_multiplication(self):
        """test the multiplication method"""
        self.assertEqual(self.calc.multiply(6, 2), 12)
        self.assertEqual(self.calc.divide(6, 1), 6)
        self.assertEqual(self.calc.divide(6, 0), 0)
