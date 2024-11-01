import unittest
from hw8 import *

class TestMain(unittest.TestCase):
    """This is a new class, TestMain, that is a subclass of the TestCase Class
    from the unittest package
    
    Tests:
    ----------------------------------------
        test_listToDict: test for correct output
        test_newDict: test for correct output
        test_uniqueElems: test for correct output
        test_valFrequency: test for correct output
        test_addsToK: test for correct output
        test_senatorsInfo: test for correct output
        test_noContactForm: test for correct output
        test_congressSessionMembers: test for correct output
    """

    def test_listToDict(self):
        """
        Expect index + 1 as index, and the corresponding
        elements of list as values.
        """
        self.assertEqual({1:2, 2:6, 3:6, 4:1, 5:7, 6:9}, listToDict([2, 6, 6, 1, 7, 9]))

    def test_newDict(self):
        """
        Expect the key-value input of a dictionary to be inverted as
        a new dictionaru with value-key pair.
        """
        # Case 1: Dictionary without duplicates
        dict_1 = listToDict([5, 4, 3, 2, 1])
        self.assertEqual({5:1, 4:2, 3:3, 2:4, 1:5}, newDict(dict_1))

        # Case 2: Dictionary with duplicates. Function prints out 'Please input a valid dictionary without duplicate values.', but should return 
        dict_2 = listToDict([5, 5, 4, 3, 2, 1])
        self.assertEqual({}, newDict(dict_2))

    def test_uniqueElems(self):
        """
        Expect True if list contains all unique elements. False otherwise.
        """
        # Case 1: True case
        self.assertEqual(True, uniqueElems([1, 2, 'a', 'v']))
        # Case 2: False case
        self.assertEqual(False, uniqueElems([1, 2, 'a', 'v', 1]))

    def test_valFrequency(self):
        """
        Expect a dictionary containing keys for elements and counts as values.
        """
        self.assertEqual({'a':1, 'b':3, 'c':2}, valFrequency(['a', 'b', 'b', 'b', 'c', 'c']))
    
    def test_addsToK(self):
        """
        If list, nums, contains two distinct elements (pairs without duplicates) that add up to integer k, return True. Otherwise, False.
        """
        self.assertEqual(False, addsToK(k=4, nums=[1, 2, 2, 2, 4]))
        self.assertEqual(False, addsToK(k=7, nums=[1, 2, 3, 7]))
        self.assertEqual(True, addsToK(k=7, nums=[1, 2, 3, 5, 7, 4]))

    def test_senatorsInfo(self):
        """
        Test for the correct number of keys (extracted data) and the correct length of Names.
        """
        filename = 'senators.json'
        # Case 1: Number of dictionary entries (congress people) in senatorsInfo() list expected at 100.
        self.assertEqual(100, len(senatorsInfo(filename)))
        # Case 2: Number of  keys in each dictionary within list expected at 11.
        self.assertEqual(11, len(senatorsInfo(filename)[0]))
    
    def test_noContactForm(self):
        """
        Expect ['Pete Ricketts'] who is the only congress person without contact form.
        """
        filename = 'senators.json'
        self.assertEqual(['Pete Ricketts'], noContactForm(filename))

    def test_congressSessionMembers(self):
        """
        Expect:
          sessionNumber 116 = 33
          sessionNumber 117 = 64
          sessionNumber 118 = 100
          sessionNumber 119 = 66
          sessionNumber 120 = 34
        """
        filename = 'senators.json'
        self.assertEqual(33, len(congressSessionMembers(filename, 116)))
        self.assertEqual(64, len(congressSessionMembers(filename, 117)))
        self.assertEqual(100, len(congressSessionMembers(filename, 118)))
        self.assertEqual(66, len(congressSessionMembers(filename, 119)))
        self.assertEqual(34, len(congressSessionMembers(filename, 120)))

if __name__ == '__main__':
  unittest.main()