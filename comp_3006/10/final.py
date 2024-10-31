'''
COMP 3006
Homework 10 - Pandas

General Homework Guidelines: 
- Homework must be submitted in a .py file. Please do not submit .ipynb files.
- Homework should not use packages or functions that have not yet been discussed in class.
- Use comments to explain what your code is doing. 
- Use a consistent coding style. 
- Use descriptive variable names.
- Test your code regularly using a variety of different inputs. 
- Every function must include a docstring for documentation (see: 
   https://realpython.com/documenting-python-code/). This docstring should include:
     - 1 or 2 lines describing what the function does
     - Args: input parameters, their types and what they are for
     - Returns: return data type and what it is
- All tests of your functions should be commented out in your final submission or
  encolosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.
'''
#--------------------------------------------------------------------------#
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import logging
import argparse

# define the logging from 10.2 so custom logging can be ran when imported into another py file (ex. Unit Test)

# set up the root logger with a default level of DEBUG
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# set the format for log messages
log_format = "%(asctime)s : %(levelname)s : %(lineno)d : %(message)s"
formatter = logging.Formatter(log_format)

## System logger
systemLogger = logging.getLogger('systemLogger')
system_handler = logging.FileHandler('linearSystem.log', 'w')
system_handler.setFormatter(formatter)
systemLogger.addHandler(system_handler)

# Solution logger
solutionLogger = logging.getLogger('solutionLogger')
solution_handler = logging.FileHandler('solution.log', 'w')
solution_handler.setFormatter(formatter)
solutionLogger.addHandler(solution_handler)



# Assignment 10.1:
# Create a class, LinearSolver, which applies Cramer's Rule to solve simultaneous linear 
# equations of 3 unknowns. The class must implement the following methods: contructor, __str__,
# check_system and solver. 
# -The check_system method should verify that the linear system of equations is 3x3 and that 
# the constants is 3x1. 
# -The solver method should implement Cramer's Rule and return the solution to the linear 
# system as a 1d array.
# It must also contain the attributes : system (this is the linear system of equations) and 
# contants (this is a 1-d array with the coefficients).
#
# An example of what the coefficient matrix A looks like:
# A = np.array([[5, -14, -3], [1, 2, 2], [-7, 4, 5]]),
# and the constants are: -39, -2, and -29.
# Hint: For the determinant of matrix A use np.linalg.det(A).

class LinearSolver():
    """Class for solving linear equations using Cramer's Rule"""
    def __init__(self, A, b):
        """
        Class constructor for linear solver (Ax = b).
        Attributs:
            A (np.array) : 3x3 matrix containing the coefficients of the linear equation (aka system attribute)
            b (np.array) 3x1 vector of constants (aka constant attribute)
            solution (np.array) : 1d array that contains solutions to unknown variables in system of linear equations
        Methods:
            __init__: class constructor
            __str__: string representation of LienarSolver class object
            check_system : verifies that the linear system of equations is 3x3 and that the constants vector is 3x1
            solver : implements Cramer's Rule and returns the solution to the linear system as a 1d array
        """
        self.A = A
        self.b = b
        self.solution = self.solver()

        

    def __str__(self):
        """String representation of linear system"""
        return f"Coefficient Matrix A={self.A}, shape={self.A.shape}\nConstants Vector b={self.b}, shape={self.b.shape}"
    def check_systems(self):
        """
        This method verifies the correct shapes for A=(3,3) and b=(3,1).
        Args:
            None
        Rerurns:
            boolean : True if correct shapes for A=(3,3) and b=(3,1).
        """
        return self.A.shape == (3,3) and self.b.shape == (3,1)

    def solver(self):
        """"
        Solves for a linear equation in the form of Ax = b where A is a 3x3 matrix, x is a vector of the three unkowns (r, s, t), and b is a 3x1 vector. 
        Implements Cramer's rule to solve for one variable at a time.
        Inputs:
            A (np.array) : 3x3 matrix containing the coefficients of the linear equation
            b (np.array) 3x1 vector (Ax = b)
        Returns:
            x (np.array) : 1d array containing the solution to the linear system (np.array([r, s, t]))
        """
        systemLogger.debug(f"Input parameters:\nA={self.A}, shape={self.A.shape}\nb={self.b}, shape={self.b.shape}")
        solutionLogger.debug(f"Input parameters:\nA={self.A}, shape={self.A.shape}\nb={self.b}, shape={self.b.shape}")
        try:
            if not self.check_systems():
                raise ValueError
            
            # convert (3,1) array to (3,) since np.insert() expects a 1D array or scalar for insertion
            self.b = self.b.reshape(3,)
            
            # replace each col corresponding to the unknowns with b
            r_matrix = np.insert(self.A.copy()[:, 1:], 0, self.b, axis=1)
            s_matrix = np.insert(self.A.copy()[:, [0,2]], 1, self.b, axis=1)
            t_matrix = np.insert(self.A.copy()[:, :-1], 2, self.b, axis=1)
            systemLogger.debug(f"r_matrix={r_matrix}/s_matrix={s_matrix}\nt_matirx={t_matrix}")

            # calculate determinants
            D = np.linalg.det(self.A)

            # floating point division errors when D should be equal to 0
            threshold = 1e-10
            if np.abs(D) < threshold:
                D = 0
                systemLogger.debug(f"Det(A)={D}")
                if D == 0:
                    raise ZeroDivisionError
                else:
                    pass
            else:
                systemLogger.debug(f"Det(A)={D}")
            

            Dr = np.linalg.det(r_matrix)
            Ds = np.linalg.det(s_matrix)
            Dt = np.linalg.det(t_matrix)
            systemLogger.debug(f"Determinants calculated .")
            
            solutionLogger.debug(f"Solution array = {np.array([Dr/D, Ds/D, Dt/D])}")
            return np.array([Dr/D, Ds/D, Dt/D])
        
        except ZeroDivisionError:
            systemLogger.warning(f'ZeroDivisionError: This linear equation does not contain a unique solution')
            print(f'ZeroDivisionError: This linear equation does not contain a unique solution')
        except ValueError:
            systemLogger.warning(f"ValueError: Check array shapes: A shape is {self.A.shape}, but expected (3,3) and b shape is {self.b.shape} but expected (3,1).")
            print(f"ValueError: Check array shapes: A shape is {self.A.shape}, but expected (3,3) and b shape is {self.b.shape} but expected (3,1).")
        except UnboundLocalError:
            systemLogger.warning(f"UnboundLocalError: Check array shapes: A shape is {self.A.shape}, but expected (3,3) and b shape is {self.b.shape} but expected (3,1).")
            print(f"UnboundLocalError:Check array shapes: A shape is {self.A.shape}, but expected (3,3) and b shape is {self.b.shape} but expected (3,1).")
        
# Assignment 10.2:
# Create 2 custom loggers, systemLogger and solutionLogger, which write to linearSystem.log and 
# solution.log respectively. Use argparser to include the ability to set the logging level for each
# logger but by default both loggers must have a default level of DEBUG. They must also implement 
# the following format: 
# Time when the LogRecord was created : logging level : line number : message
# (You will need to read the documentation at https://docs.python.org/3/library/logging.html)
if __name__ == '__main__':
  # set up the root logger with a default level of DEBUG
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)

  # create an argument parser
  parser = argparse.ArgumentParser(description="Set logging level")

  # arg for system logger level 
  parser.add_argument("--system_log_level", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], default="DEBUG", help="Set the logging level for systemLogger")

  # arg for solution logger level
  parser.add_argument("--solution_log_level", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], default="DEBUG", help="Set the logging level for solutionLogger")

  # parse the command line arguments
  args = parser.parse_args()

  # set the format for log messages
  log_format = "%(asctime)s : %(levelname)s : %(lineno)d : %(message)s"
  formatter = logging.Formatter(log_format)
  
  ## System logger
  systemLogger = logging.getLogger('systemLogger')
  systemLogger.setLevel(getattr(logging, args.system_log_level))
  system_handler = logging.FileHandler('linearSystem.log', 'w')
  system_handler.setFormatter(formatter)
  systemLogger.addHandler(system_handler)

  # Solution logger
  solutionLogger = logging.getLogger('solutionLogger')
  solutionLogger.setLevel(getattr(logging, args.solution_log_level))
  solution_handler = logging.FileHandler('solution.log', 'w')
  solution_handler.setFormatter(formatter)
  solutionLogger.addHandler(solution_handler)


  # working example case to test the logger (unique solution)
  A = np.array([[2, 1, 1], [1, -1, -1], [1, 2, 1]])
  b = np.array([3, 0, 0]).reshape(3,1)

  x = LinearSolver(A,b)

  # working example case to test the logger (no solution)
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  b = np.array([1, 2, 3]).reshape(3,1)

  x = LinearSolver(A,b)

  # working example case to test the logger (incorrect shape)
  A = np.array([[2, 1, 1], [1, -1, -1], [1, 2, 1]])
  b = np.array([3, 0, 0]).reshape(3,)

  x = LinearSolver(A,b)

  print(x.solution)


# Assignment 10.3:
# Create a class, GradeSytem, which holds the grades for a number of classes and a certain number
# of students. The class must implement the following methods: constructor, __str__, __repr__,
# class_stats, class_summary, student_stats, check_students and grades_graph.
# -class_stats should calculate the average and standard deviation of the grades in the class.

# -student_stats should calculate a student's average grade and standard deviation of their grades. To
# make this easier, you may assume that a student is in the same location in each grades list. So the
# student in the first entry in the Math class will also be the first entry in the Science class and so on.

# -check_students must verify that every class has the same number of entries for the students list. It must
# be possible for each class to have a different number of students, i.e. Math might have 20 students whilst
# English might have 16 students. Hint: think of using a filler value like -1 and make sure to handle that
# case in your stats.

# -grades_graph should create a bar plot of the grades either for a class (x-axis should be the student, you can
# simply use the student's location in the grades list to represent them) or for a student (x-axis should be
# the class name). All plots must have appropriate title and axis labels.

# The class must implement a Pandas DataFrame in order to store all the data and compute all the required
# statistics using the built-in DataFrame functions (this is why the length of the grades list must be the
# same for all classes. The 5 number summary could be done using methods not built-in to DataFrames).
# This is a sample of a dictionary that could be used to create a Pandas DataFrame for 8 students (Note: this 
# is a sort of base case where all classes have the same number of students and this won't always be the case)
# Eight students' grades in their respective courses are given via this dictionary: {'Math' : [80, 89, 93, 66, 84, 85, 74, 64],
# 'Science' : [94, 76, 88, 78, 88, 92, 60, 85], 'English' : [83, 76, 93, 96, 77, 85, 92, 60], 'History' : [96, 66, 76, 85, 78, 88, 69, 99]}
# Upload a zip of your source file(s).

class GradeSystem():
    """
    Class that holds the grades for different classes and their students.
    Attributes:
        class_data: original dictionary input containing the different classes (keys) and student grades (values)
        data: pandas.dataframe containing the data from the class_data dictionary
    Methods
        __init__: class constructor
        __str__: string representation of GradeSystem Class
        __repr__: string representation of GradeSystem Class
        create_dataframe: create a pandas.dataframe from the class_data dictionary
        check_students: verifies that every class has the same number of entries for the students list
        check_grades: validates the student grades by checking if they are in the proper value range
        student_stats: calculate a student's average grade and standard deviation of their grades
        class_stats: calculate a class's average grade and standard deviation of their grades
        class_summary:  returns the summary statistics of a class
        grades_graph:  creates a bar plot of the grades (Grades vs Student per Class or Grades vs Class per Student)
    """
    def __init__(self, class_data):
        """Class constructor"""
        self.class_data = class_data
        self.data = self.create_dataframe()

    def __str__(self):
        """String representation of GradeSystem Class"""
        return f'Classes={list(self.class_data.keys())}, TotalStudents={np.max([len(value) for value in self.class_data.values()])}'
    
    def __repr__(self):
        """String representation of GradeSystem Class"""
        return self.__str__()
    
    def create_dataframe(self):
        """
        This method creates a pandas dataframe from the dict, class_data.
        Args:
            None
        Return:
            pandas.dataframe: dataframe containing student grades per class
        """
        # check lengths of class_data value lists (if list lengths equal, return dataframe)
        if self.check_students():
            return self.check_grades(pd.DataFrame(self.class_data))
        # if list lengths are not equal, fill in missing students with np.nan to match class with the most students
        else:
            max_length = np.max([len(value) for value in self.class_data.values()])
            # iterate through dict and fill in missing students with np.nan as needed
            for key, value in self.class_data.items():
                if len(value) < max_length:
                    self.class_data[key] = self.class_data[key] + [np.nan] * (max_length - len(value))
            return self.check_grades(pd.DataFrame(self.class_data))
        
    def check_students(self):
        """Checks that every class has the same number of entries in the student list"""
        # if standard deviation of a list of value lengths != 0, then the lengths are not equal
        return np.std([len(value) for value in self.class_data.values()]) == 0
    
    def check_grades(self, df):
        """
        This function validates the student's grades. If the grades are out of the range (0,100),
        then the grades will be replaced by np.nan.
        Args:
            df (pd.dataframe): dataframe containing class and student grades
        Returns:
            pandas.dataframe: dataframe containing student grades per class in the correct range only
        """
        return df.mask((df < 0) | (df > 100), np.nan)

    def student_stats(self, i : int):
        """
        Calculates the mean and standard deviation of a student's grades across all their classes.
        Args:
            i (int) : index value corresponding to the student taking the class
        Returns:
            tuple : (mean of student grades, standard devation of student grades) across all classes
        """
        df = self.data
        return df.iloc[int(i), :].mean(),  df.iloc[int(i), :].std()
    
    def class_stats(self, class_subject : str):
        """
        Calculates the mean and standard deviation of a class's grades across all students.
        Args:
            class_subject (str) : string of class to get stats of
        Returns:
            tuple : (mean of class grades, standard devation of class grades) across all students
        """
        df = self.data
        return df.loc[:, class_subject].mean(),  df.loc[:, class_subject].std()
    
    def class_summary(self, x : str):
        """
        Calculates the summary statistics of all the data per class or per student.
        Args:
            x (string) : ['student' or 'class'] to get summary statistics from data
        """
        try: 
            if x == 'student':
                return self.data.T.describe()          
            elif x == 'class':
                return self.data.describe()
            else:
                raise ValueError
        except ValueError:
            print(f"Error: Please check for valid agrs for x ['student', 'class']")
        except KeyError:
            print(f"Error: Please check for valid agrs for x ['student', 'class']")
    
    def grades_graph(self, x : str, y : str):
        """
        This function outputs a bar plot based on the grades of a class or the grades of a student.
        Args:
            x (str) : x axis of bar plot (either 'student' or 'class')
            y (str or int) : y axis of bar plot (either specific class (str) or specific Student index (int))
        """
        try: 
            if x == 'student':
                fig, ax = plt.subplots()

                ax.bar(x=self.data.index, height=self.data[y])
                ax.set_xlabel('Student')
                ax.set_ylabel('Grade %')
                ax.set_title(str(y).title() + ' Class Grades')
                for spine in ['top', 'right']:
                    ax.spines[spine].set_visible(False)
                                        
                plt.show()
            elif x == 'class':
                fig, ax = plt.subplots()

                ax.bar(x=self.data.columns, height=self.data.T[int(y)])
                ax.set_xlabel('Classes')
                ax.set_ylabel('Grade %')
                ax.set_title( f' Student {str(int(y)).title()} Grades')
                for spine in ['top', 'right']:
                    ax.spines[spine].set_visible(False)           

                plt.show()
            else:
                raise ValueError
        except ValueError:
            print(f"Error: Please check for valid agrs for x ['student', 'class'] and y (specific class or specific row index of studnet)")
        except KeyError:
            print(f"Error: Please check for valid args for x ['student', 'class'] and y (specific class or specific row index of studnet)")