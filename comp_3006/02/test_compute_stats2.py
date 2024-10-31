import unittest
import compute_stats2

class computeStatsTest(unittest.TestCase):
   '''
   This test suite will test the core functionality of the 
   compute_stats function from the compute_stats module.
   Tests:
       test_even : tests a list containing an even number of elemets
       test_odd : tests a list containing an odd number of elements
       test_empty : tests a list containing nothing
       test_single : tests a list containing only one element
       test_output : tests for same output as week 1 hw that I got correct
   '''
   def test_even(self):
        '''
        Expect min = 50, max = 1000, avg = 337.5, med = 150.0
        '''
        output = compute_stats2.compute_stats([100, 200, 1000, 50])
        expected = (50, 1000, 337.5, 150.0)
        self.assertEqual(output, expected)
        
   def test_odd(self):
        '''
        Expect min = 50, max = 1000, avg = 425.4, med = 200
        '''
        output = compute_stats2.compute_stats([50, 100, 200, 777, 1000])
        expected = (50, 1000, 425.4, 200)
        self.assertEqual(output, expected)
   def test_empty(self):
        '''
        Expect None
        '''
        output = compute_stats2.compute_stats([])
        expected = None
        self.assertEqual(output, expected)
   def test_single(self):
        '''
        Expect min = 1, max = 1, avg = 1.0, med =  1
        '''
        output = compute_stats2.compute_stats([1])
        expected = (1, 1, 1.0, 1)
        self.assertEqual(output, expected)
   def test_output(self):
        '''
        Expect (-17.9, 17.1, 2.5414835164835154, 1.65)
        '''
        numbers = compute_stats2.colFromData_Filename(col = 9, filename='data.txt')
        output = compute_stats2.compute_stats(numbers)
        expected = (-17.9, 17.1, 2.5414835164835154, 1.65)
        self.assertEqual(output, expected)
        
if __name__ == '__main__':
    unittest.main()