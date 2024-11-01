###------------------------###
###------ Unit Tests ------###
###------------------------###


# In a separate file, called test_hw6.py, complete the class for the 
# unit tests. This should be questions 9 and 10. You may use the unit test
# file from homework 4 as a template.
# Remember to import all necessary packages and modules.

import unittest
from helper_functions6 import *
from hw6 import *

class TestMain(unittest.TestCase):
    """This is a new class, TestMain, that is a subclass of the TestCase Class
    from the unittest package
    
    Tests:
    ----------------------------------------
        test_minMaxTuple: checks that the function gives you the correct output
        test_filterByValues: checks that the average values for the fields average price, lot size, living space, and build year is correct for filtered datas
        test_averageValues: checks the output of averageValues is correct for all data
        test_allPairs: checks for correct output
        test_removeDups: checks for corret output
        test_resultTuples: checks for correct output
    """

# 9. Write a unit test, called test_minMaxTuple, that checks that the function
# gives you the correct output for a sample list of elements, a list with no elements,
# a list with a single element and multiple elements of the same value.
# (10 points)

    def test_minMaxTuple(self):
        """
        Checks that the function gives you the correct output for a sample list of elements, 
        a list with no elements, a list with a single element and multiple elements of the same value.
        """
        # list of [-10,2456,100,-12,123456], expect (-12, 123456)
        self.assertEqual((-12, 123456), minMaxTuple([-10,2456,100,-12,123456]))

        # empty list, expect ()
        self.assertEqual((), minMaxTuple([]))

        # list of multiple elements of the same value [1,1,1,1,1], expect (1,1)
        self.assertEqual((1,1), minMaxTuple([1,1,1,1,1]))


# 10. Write a unit test, called test_filterByValues, that checks that the average
# values for the fields average price, lot size, living space, and build year
# Case 1: for a minPrice = 100000 and maxPrice = 400000, has the following output :
# (324395.9323770492, 216.56045081967213, 110.17930327868852, 1966.869722557298) 
# Case 2: for no minPrice and no maxPrice, has the following output :
# (557707.7581831556, 686.6248620816476, 146.34608311879367, 1968.9804836656767)
# (10 points)

    def test_filterByValues(self):
        """
        Checks that the average values for the values for the fields of average price, average lot size, average living space, 
        and average build year are correct.
        """
        data = inputData('hw6_data.csv')
        # case 1 : minPrice = 100000, maxPrice = 400000. 
        # Expect (324395.9323770492, 216.56045081967213, 110.17930327868852, 1966.869722557298) 
        self.assertEqual((324395.9323770492, 216.56045081967213, 110.17930327868852, 1967.001536885246) , filterByValues(data, minPrice=100000, maxPrice=400000))


        # case 2: no minPrice and no maxPrice enetered. 
        # Expect (557707.7581831556, 686.6248620816476, 146.34608311879367, 1968.9804836656767).
        self.assertEqual((557707.7581831556, 686.6248620816476, 146.34608311879367, 1969.2833762412652) , filterByValues(data))


# extra tests aka "sanity checks" from hw6 comments
    def test_averageValues(self):
        """
        Test the output of averageValues(). 
        Expect (557707.7581831556, 686.6248620816476, 146.34608311879367, 1969.2833762412652).
        """
        data = inputData('hw6_data.csv')
        self.assertEqual((557707.7581831556, 686.6248620816476, 146.34608311879367, 1969.2833762412652), averageValues(data))

    def test_allPairs(self):
        """
        Test the output of allPairs() for x = [1, 4, 6, 8], y = [5, 2, 6]. 
        Expect [(1, 5), (1, 2), (1, 6), (4, 5), (4, 2), (4, 6), (6, 5), (6, 2), (8, 5), (8, 2), (8, 6)]. 
        """
        self.assertEqual([(1, 5), (1, 2), (1, 6), (4, 5), (4, 2), (4, 6), (6, 5), (6, 2), (8, 5), (8, 2), (8, 6)], allPairs(x = [1, 4, 6, 8], y = [5, 2, 6]))

    def test_removeDups(self):
        """
        Test the output of removeDups for [(1, 2), (1, 4, 5), (1, 2), (3, 5)].
        Expect [(1, 2), (1, 4, 5), (3, 5)].
        """
        self.assertEqual([(1, 2), (1, 4, 5), (3, 5)], removeDups([(1, 2), (1, 4, 5), (1, 2), (3, 5)]))

    def test_resultTuples(self):
        """
        Test the output of resultTuples for location 'Madrid'.
        Expect realEstate(Location='Madrid', CheapestBuyPrice=149000.0, AvgBuyPrice=557707.7581831556, MostExpBuy=4700000.0).
        """
        realEstate = namedtuple('realEstate', ['Location', 'CheapestBuyPrice', 'AvgBuyPrice', 'MostExpBuy'])
        self.assertEqual(realEstate(Location='Madrid', CheapestBuyPrice=149000.0, AvgBuyPrice=557707.7581831556, MostExpBuy=4700000.0), resultTuples('Madrid'))
        
                         


if __name__ == '__main__':
    unittest.main()