# Assignment 9.4:
# In a separate file, test_homework9.py, write the necessary unittests for questions 9.1 and 9.2. Take careful consideration to 
# test valid and invalid values for the creation of any of the distributions.
from distributions import Distribution, NumpyDistribution
import unittest
import numpy as np
import random

# set sample size
n = 1000000

# Distribution class based off random/statistics.scipy.stats module
normal = Distribution('normal', 0, 1, n)
lognormal = Distribution('lognormal', 0, 1, n)
laplace = Distribution('laplace', 100, 1, n)

# NumpyDistribution class based off Numpy module (NOT LIMITED to noral/lognormal/laplace)
normal_np = NumpyDistribution('normal', 0, 1, n)
lognormal_np = NumpyDistribution('lognormal', 1, 1, n)
laplace_np = NumpyDistribution('laplace', 100, 1, n)
poisson_np = NumpyDistribution("poisson", 1, n)
binomial_np = NumpyDistribution('binomial', n=1000, p=0.9, size=n)
geometric_np = NumpyDistribution('geometric', 0.75, n)

class TestDistribution(unittest.TestCase):
    """
    This suite of tests will test the mean, standard deviation, and length outputs for the three different distributions
    ['normal', 'lognormal', 'laplace'] made by the * Distribution * class.
    Tests:
        test_NormalDist : tests for proper length, mean, and standard deviation for normal distribution
        test_LogNormalDist : tests for proper length, mean, and standard deviation for lognormal distribution
        test_LaplaceDist : tests for proper length, mean, and standard deviation for laplace distribution
    """
    def test_NormalDist(self):
        result = normal.data
        # test length
        self.assertEqual(len(result), n)
        # test mean value
        self.assertAlmostEqual(np.mean(result), np.mean(np.random.normal(0, 1, n)), delta=0.1)
        # test standard deviation
        self.assertAlmostEqual(np.std(result), np.std(np.random.normal(0, 1, n)), delta=0.1)
    def test_LogNormalDist(self):
        result = lognormal.data
        # test length
        self.assertEqual(len(result), n)
        # test mean value
        self.assertAlmostEqual(np.mean(result), np.mean(np.random.lognormal(0, 1, n)), delta=0.1)
        # test standard deviation
        self.assertAlmostEqual(np.std(result), np.std(np.random.lognormal(0, 1, n)), delta=0.1)
    def test_LaplaceDist(self):
        result = laplace.data
        # test length
        self.assertEqual(len(result), n)
        # test mean value
        self.assertAlmostEqual(np.mean(result), np.mean(np.random.laplace(100, 1, n)), delta=.1)
        # test standard deviation
        self.assertAlmostEqual(np.std(result), np.std(np.random.laplace(100, 1, n)), delta=.1)

class TestNumpyDistribution(unittest.TestCase):
    """
        This suite of tests will test the mean, standard deviation, and length outputs for different available Numpy distributions
        made by the * NumpyDistribution * class
        Tests:
            test_NormalDist : tests for proper length, mean, and standard deviation for normal distribution
            test_LogNormalDist : tests for proper length, mean, and standard deviation for lognormal distribution
            test_LaplaceDist : tests for proper length, mean, and standard deviation for laplace distribution
            test_PoissonDist : tests for proper length, mean, and standard deviation for poisson distribution
            test_BinomialDist : tests for proper length, mean, and standard deviation for binomial distribution
            test_GeometricDist : tests for proper length, mean, and standard deviation for geometric distribution
        """
    def test_NormalDist(self):
        result = normal_np.data
        # test length
        self.assertEqual(len(result), n)
        # test mean value
        self.assertAlmostEqual(np.mean(result), np.mean(np.random.normal(0, 1, n)), delta=0.1)
        # test standard deviation
        self.assertAlmostEqual(np.std(result), np.std(np.random.normal(0, 1, n)), delta=0.1)
    def test_LogNormalDist(self):
        result = lognormal_np.data
        # test length
        self.assertEqual(len(result), n)
        # test mean value
        self.assertAlmostEqual(np.mean(result), np.mean(np.random.lognormal(1, 1, n)), delta=0.1)
        # test standard deviation
        self.assertAlmostEqual(np.std(result), np.std(np.random.lognormal(1, 1, n)), delta=0.1)
    def test_LaplaceDist(self):
        result = laplace_np.data
        # test length
        self.assertEqual(len(result), n)
        # test mean value
        self.assertAlmostEqual(np.mean(result), np.mean(np.random.laplace(100, 1, n)), delta=.1)
        # test standard deviation
        self.assertAlmostEqual(np.std(result), np.std(np.random.laplace(100, 1, n)), delta=.1)
    def test_PoissonDist(self):
        result = poisson_np.data
        # test length
        self.assertEqual(len(result), n)
        # test mean value
        self.assertAlmostEqual(np.mean(result), np.mean(np.random.poisson(1, n)), delta=.1)
        # test standard deviation
        self.assertAlmostEqual(np.std(result), np.std(np.random.poisson(1, n)), delta=.1)
    def test_BinomialDist(self):
        result = binomial_np.data
        # test length
        self.assertEqual(len(result), n)
        # test mean value
        self.assertAlmostEqual(np.mean(result), np.mean(np.random.binomial(n=1000, p=0.9, size=n)), delta=.1)
        # test standard deviation
        self.assertAlmostEqual(np.std(result), np.std(np.random.binomial(n=1000, p=0.9, size=n)), delta=.1)
    def test_GeometridDist(self):
        result = geometric_np.data
        # test length
        self.assertEqual(len(result), n)
        # test mean value
        self.assertAlmostEqual(np.mean(result), np.mean(np.random.geometric(0.75, n)), delta=.1)
        # test standard deviation
        self.assertAlmostEqual(np.std(result), np.std(np.random.geometric(0.75, n)), delta=.1)

class TestInvalidValues(unittest.TestCase):
    """
        This suite of tests will test invalid values for both the NumpyDistribution and Distribution class.
        Tests:
            test_InvalidNumpyDistribution: tests for invald distribution/sample size parameters/incorrect dtype
            test_InvalidDistributiont : tests for invald distribution/sample size parameters/incorrect dtype
        """
    def test_InvalidDistribution(self):
        # test invalid amount of arguments (not enough)
        with self.assertRaises(TypeError):
            result = Distribution('uniform')

        # test invalid amount of arguments (too many enough)
        with self.assertRaises(TypeError):
            result = Distribution('normal', 1, 1, 1, 1)

        # test incorrect data types
        self.assertAlmostEqual(np.mean(Distribution('normal', '0', '1', n).data), 0, delta=0.1)

        # test invalid sample size
        with self.assertRaises(ValueError):
            result = Distribution('normal', 1, 1, -1)

        # test invalid distribution
        with self.assertRaises(ValueError):
            result = Distribution('binomial', 1000, 0.9, n)

    def test_InvalidNumpyDistribution(self):
        # test invalid amount of arguments (not enough)
        with self.assertRaises(TypeError):
            result = NumpyDistribution('uniform')

        # test invalid amount of arguments (too many)
        with self.assertRaises(TypeError):
            result = NumpyDistribution('normal', 1, 1, 1, 1)

        # test invalid sample size
        with self.assertRaises(ValueError):
            result = NumpyDistribution('normal', 1, 1, -1)

         # test incorrect data types (should raise ValueError since this class cannot handle incorrect datatypes with *args/**kwargs)
        with self.assertRaises(TypeError):
            result = NumpyDistribution('normal', '0', '1', n)
        
        # test for non-existing distirbutions 
        with self.assertRaises(AttributeError):
            result = NumpyDistribution('fakeDistribution', 0, 1, n)

        
if __name__ == '__main__':
    unittest.main()