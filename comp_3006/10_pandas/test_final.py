from final import LinearSolver, GradeSystem
import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal

class TestLinearSolver(unittest.TestCase):
    """
    This test suite tests for the correct output and functionality of the LinearSolver class.
    Tests:
        test_LinearSolver : tests for proper solutions of LinearSolver (unique solution/no solution)
        test_Inputs : tests for invalid shapes
        test_Attributes : tests for proper output of attributes
    """
    def test_LinearSolver(self):
        """
        Tests for proper output of LinearSolve. 
        Two tests with unique solutions, one test with no solution.
        """
        # test case 1 : unique solution from purple math 
        A = np.array([[2, 1, 1], [1, -1, -1], [1, 2, 1]])
        b = np.array([3, 0, 0]).reshape(3,1)
        result = LinearSolver(A,b).solution
        test_solution = np.linalg.solve(A, b).flatten()
        self.assertTrue(np.allclose(result, test_solution, rtol=1e-8, atol=1e-8))

        # test case 2 : unique solution from hw assignment
        A = np.array([[5, -14, -3], [1, 2, 2], [-7, 4, 5]])
        b = np.array([-39, -2, -29]).reshape(3,1)
        result = LinearSolver(A,b).solution
        test_solution = np.linalg.solve(A, b).flatten()
        self.assertTrue(np.allclose(result, test_solution, rtol=1e-8, atol=1e-8))

        # test case 3 : no solution
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        b = np.array([1, 2, 3]).reshape(3,1)
        self.assertEqual(LinearSolver(A, b).solver(), None)
    def test_Inputs(self):
        """
        Tests for invalid shape inputs and proper exception handling.
        """
        # test 1 : b not in (3,1) shape
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        b = np.array([1, 2, 3])
        self.assertEqual(LinearSolver(A, b).solver(), None)

        # test 2 : A not in (3,3) shape
        A = np.array([[1, 2, 3], [7, 8, 9]])
        b = np.array([1, 2, 3]).reshape(3,1)
        self.assertEqual(LinearSolver(A, b).solver(), None)

    def test_Attributes(self):
        """
        Tests for the correct attributes of the LinearSolver class (A/system attribute and b/constant attribute).
        """
        # test case 1 : check LinearSolver.A (system attribute) 
        A = np.array([[2, 1, 1], [1, -1, -1], [1, 2, 1]])
        b = np.array([3, 0, 0]).reshape(3,1)
        result = LinearSolver(A,b).A
        self.assertTrue(np.allclose(result, A, rtol=1e-8, atol=1e-8))

        # test case 2 : check LinearSolver.b (constants attribute) 
        A = np.array([[2, 1, 1], [1, -1, -1], [1, 2, 1]])
        b = np.array([3, 0, 0]).reshape(3,1)
        result = LinearSolver(A,b).b
        self.assertTrue(np.allclose(result, b.flatten(), rtol=1e-8, atol=1e-8))


# this is the test data that contains different amounts of students per class,
# an empty class, and grades that are outside of the correct grade range 0 to 100
class_data = {'Math' : [200, 89, 93, 66, 84, 85], 'Science' : [94, 76, 88, -1, 92, 60, 85], 
 'English' : [83, 76, 93, 96, 77, 85, 92, 60], 'History' : [200, 66, 76, 85, 78, 88, 69, 100], 'CompSci': []}

grades = GradeSystem(class_data)
df = grades.data

class TestGradeSystem(unittest.TestCase):
    """
    This test suite tests for proper functionality and output of the GradeSystem class.
    Tests:
        test_GradeSystem : 8 different tests that test for output 
    """
    def test_GradeSystem(self):
        # test # 1 : test for class_data attribute
        result = list(grades.class_data.keys())
        self.assertEqual(result, list(df.columns))

        # test 2 : test for student stats for student at index 3
        i = 3
        result = grades.student_stats(i)
        self.assertEqual(result, (df.iloc[i].mean(), df.iloc[i].std()))

        # test 3 : test for class stats for 'Math' class
        c = 'Math'
        result = grades.class_stats(c)
        self.assertEqual(result, (df[c].mean(), df[c].std()))

        # test 4 : test length of resulting dataframe
        result = len(grades.data)
        self.assertEqual(result, len(df))

        # test 5 : test check_grades which convert all values outside of [0,100] with np.nan (expect 3 na's)
        class_data2 = {'Math' : [0, 89, 93, 66, 84, 85], 'Science' : [94, 76, 88, -1, 92, 60], 
                      'English' : [83, 76, 93, 96, 200, 85], 'History' : [200, 66, 76, 85, 78, 88]}
        
        result = grades.check_grades(df=pd.DataFrame(class_data2)).isna().sum().sum()
        self.assertEqual(result, 3)

        # test 6 : since create_dataframe() fixes the lengths of the student list, check_students() should return True
        result = grades.check_students()
        self.assertTrue(result)

        # test 7 : test for output of class_summary('student')
        result = grades.class_summary('student')
        assert_frame_equal(result, df.T.describe())

        # test 8 : test for output of class_summary('class')
        result = grades.class_summary('class')
        assert_frame_equal(result, df.describe())

if __name__ == "__main__":
    unittest.main()