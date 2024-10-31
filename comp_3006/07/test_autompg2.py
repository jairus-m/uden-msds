import unittest
from autompg2 import AutoMPG, AutoMPGData

prius = AutoMPG('Toyota', 'Prius', 2014, 50.0)
prius2 = AutoMPG('Toyota', 'Prius', 2014, 50.0)
crosstrek = AutoMPG('Subaru', 'Crosstrek', 2024, 27.0)

class TestAutoMPG(unittest.TestCase):
    """
    This test class will test the attributes and methods of the AutoMPG class object.
    Tests:
        test_Attributes : test for correct outputs for class attributes
        test__Str__ : test for correct return string for __str__ and __repr__
        test__Eq__ : test equality of AutoMPG objects (same exact attributes?)
        test__Lt__ : test fot less than/greater than of AutoMPG objects 
        test__Hash__ : test for correct implementation of hash
    """
    def test_Attributes(self):
        self.assertEqual(prius.make, 'Toyota')
        self.assertEqual(crosstrek.model, 'Crosstrek')
        self.assertEqual(crosstrek.year - prius.year, 10)
        self.assertEqual(prius.mpg, 50.0)

    def test__Str__(self):
        self.assertEqual(repr(prius), 'AutoMPG(Toyota, Prius, 2014, 50.0)')
        self.assertEqual(str(crosstrek), 'AutoMPG(Subaru, Crosstrek, 2024, 27.0)')

    def test__Eq__(self):
        # prius != crosstrek
        self.assertEqual(prius == crosstrek, False)
        # prius == prius
        self.assertEqual(prius == prius, True)

    def test_Lt__(self):
        self.assertEqual(prius > crosstrek, True)
        self.assertEqual(crosstrek > crosstrek, False)

    def test__Hash__(self):
        # prius and prius2 should share the same hash ID since they have the same exact attributes
        self.assertEqual(hash(prius) == hash(prius2), True)

        # should have differing IDs since they are considered two different AutoMPG class objects in memory however
        self.assertEqual(id(prius) == id(prius2), False)

class TestAutoMPGData(unittest.TestCase):
    """
    This test class will test the data method of the AutoMPGData class object
    and check if it is an iterable.
    Note: instantiating AutoMPGData() should call _load_data() and/or _clean_data() methods automatically
    Tests:
        test_Data : tests for correct output for the AutoMPGData.data attribute 
        test_DataAttributes : tests for the correct attribute/types after instantiating AutoMPGData
        test__Iter__ : tests to see if AutoMPGData class object is an iterator
    """
    def test_Data(self):
        auto = AutoMPGData()
        data = auto.data
        # check for correct length
        self.assertEqual(len(data), 398)
        # check first AutoMPG object in auto.data
        self.assertEqual(data[0], AutoMPG('Chevrolet', 'Chevelle Malibu', 1970, 18.0))
        # check last AutoMPG object in auto.data
        self.assertEqual(data[-1], AutoMPG('Chevy', 'S-10', 1982, 31.0))

    def test_DataAttributes(self):
        auto = AutoMPGData()
        data = auto.data
        # check for the attributes and data types for row 155
        self.assertEqual(data[155].make, 'Ford')
        self.assertEqual(data[155].make, 'Ford')
        self.assertEqual(data[155].model, 'Maverick')
        self.assertEqual(data[155].year, 1975)
        self.assertEqual(data[155].mpg, 15.0)

    def test__Iter__(self):
        auto = AutoMPGData()
        x = type(iter(auto))
        # check if auto is an iterable (iter() would raise TypeError if not)
        self.assertEqual(str(x), "<class 'list_iterator'>")
        # create list comprhension from AutoMPGData class object itself (proves it is a class iterable)
        self.assertEqual(len([a for a in auto]), 398)

if __name__ == '__main__':
    unittest.main()