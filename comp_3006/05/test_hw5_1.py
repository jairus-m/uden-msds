import unittest
from hw5_1 import Quadratic

class TestRoots(unittest.TestCase):
    """
    This test suite will test the Quadratic.roots() method of the Quadratic class.
    Tests:
        test_TwoSolutions : tests coefficients w/ two real solutions
        test_OneSolution : tests coefficients w/ one solution
        test_NoSolutions : test coeffcients w/ no REAL solution
        test_AllZeros : tests for zero division
    """
    def test_TwoSolutions(self):
        """Test case if discriminant > 0 (two real solutions)."""
        eq = Quadratic(1, -5, 6)
        roots = eq.roots()
        self.assertEqual((3.0, 2.0), roots)
    
    def test_OneSolution(self):
        """Test case if discriminant = 0 (one real solutions)."""
        eq = Quadratic(1, -4, 4)
        roots = eq.roots()
        self.assertEqual(2.0, roots)
        
    def test_NoSolutions(self):
        """Test case if discriminant < 0 (no real solutions)."""
        eq = Quadratic(1, 2, 5)
        roots = eq.roots()
        self.assertEqual(None, roots)

    def test_AllZeros(self):
        """Test case of coefficient a = 0 (check ZeroDivisionError)"""
        eq = Quadratic(0, 0, 0)
        self.assertEqual(None, eq.roots())

if __name__ == '__main__':
    unittest.main()