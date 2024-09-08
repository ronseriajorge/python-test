import unittest   ## importamos la libreria de unit test
import src.calculator as cal

class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        assert cal.sum(2, 3) == 5

    def test_subtract(self):
        assert cal.substract(10, 5) == 5

    def test_multiply(self):
        assert cal.multiply(3, 2) == 6

    def test_divide(self):
        result = cal.divide(10, 2)
        expected = 5
        assert result == expected