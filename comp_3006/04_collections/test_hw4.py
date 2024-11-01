import unittest
import math
from hw4_1 import rollDice
from hw4_3 import celsiusToFahrenheit

class TestHW4(unittest.TestCase):
    """
    Tests the output of the rollDice function from 4.1 and 
    celsiusToFarenheight function from 4.3.
    """
    def test_rollDice(self):
        """Test the output of a fair, 6 sided die rolled 100 times"""
        results = rollDice(6, 100)
        self.assertEqual(len(results), 100)
        self.assertEqual(set(results), {1, 2, 3, 4, 5, 6})
    def test_celsiusToFarenheight(self):
        """Test for the correct conversion of C to F degrees."""
        results = list(map(celsiusToFahrenheit, [0, 15, 30]))
        self.assertEqual(results, [32, 59, 86])

if __name__ == '__main__':
    unittest.main()