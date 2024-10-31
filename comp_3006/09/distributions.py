'''
COMP 3006
Homework 9 - Numpy

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

#Assignment 9.1
# Create a class, called Distributions, that has the following attributes : distribution, mean, standard deviation and size. 
# It should have a constructor, __str__ and the ability to generate a normal distribution, lognormal and laplace distributions
# based on the distribution attribute.
# For example:
# my_distribution = Distributions("lognormal", 1, 5, 100)
# should be a lognormal distribution with a mean of 1, standard deviation of 5 and have 100 samples from the distribution
import random
import numpy as np
import matplotlib.pylab as plt
from scipy.stats import laplace

class Distribution():
    """
    Class representing a distribution based on mean, standard deviation, size, and distribution type.
    Attributes:
        dist (str) : distribution ['normal', 'lognormal', 'laplace']
        mean (float) : mean of distribution
        std (float) : standard deviation of distribution
        n (int) : size of distribution
        data (list) : list of integers randomly generated from the specific distribution 
    Methods:
        __str__ : string representation of Distribution class object
        generate_data : returns data of specified distribution
    """
    def __init__(self, dist:str, mean:float, std:float, n:int):
        """Class constructor"""
        self.dist = str(dist)
        self.mean = float(mean)
        self.std = float(std)
        if n >= 0:
            self.n = int(n)
        else:
            raise ValueError('n (sample size) must be greater than 0.')
        self.data = self.generate_data()
    def __str__(self):
        """String representation"""
        return f'Distributions({self.dist}, {self.mean}, {self.std}, {self.n})'
    def generate_data(self):
        """Returns the specified distribution based off selected distributions"""
        random.seed(24)
        if self.dist == 'normal':
            return [random.normalvariate(self.mean, self.std) for _ in range(self.n)]
        elif self.dist == 'lognormal':
            return [random.lognormvariate(self.mean, self.std) for _ in range(self.n)]
        elif self.dist == 'laplace':
            return laplace(self.mean, self.std).rvs(self.n)
        else:
            raise ValueError(f"ValueError: Invalid parameters. Check your distribution ['normal', 'lognormal', 'laplace']")



# Assignment 9.2:
# Repeat the first part, this time calling the class NumpyDistribution, using only numpy methods
# Hint: https://numpy.org/doc/1.22/, you may want to looks at using args and kwargs

class NumpyDistribution():
    """
    Class representing a distribution based on mean, standard deviation, size, and distribution type.
    Attributes:
        dist (str) : any valid distribution available with numpy.random.dist
        *args : any positional argument relevant to np.random.dist
        **kwargs : any key word argument relevant to np.random.dist
        data (list) : list of numbers randomly sampled from specified distribution
        mean (float) : mean of data distribution
        std (float) : standard deviation of data distrubtion
    Methods:
        __str__ : string representation of NumpyDistribution class object
        generate_data : returns data of specified distribution
    """
    def __init__(self, dist:str, *args, **kwargs):
        """Class constructor"""
        self.dist = str(dist)
        self.args = args
        self.kwargs = kwargs
        self.data = self.generate_data()
        self.mean = np.mean(self.data)
        self.std = np.std(self.data)

    def __str__(self):
        """String representation"""
        return f'Distributions(dist={self.dist}, args={self.args}, kwargs={self.kwargs})'
    def generate_data(self):
        """Returns the specified distribution based off selected distributions"""
        try:
            if len(self.args) > 1 or len(self.kwargs) > 1:
                np.random.seed(24)
                # use getatttr() to use string to specify the distribution attribute of np.random
                general_distribution = getattr(np.random, self.dist)
                return general_distribution(*self.args, **self.kwargs)
            else:
                raise TypeError
        except ValueError:
            raise ValueError(f"ValueError: Invalid parameters. Check your distribution parameters.")
        except TypeError:
            raise TypeError(f"TypeError: Invalid expected parameters. Check your distribution parameters.")
        except AttributeError:
            raise AttributeError(f'AttributeError: Invalid distribution. Check Numpy docs.')
        
if __name__ == '__main__':
# Assignment 9.3:
# Use only methods from numpy and matplotlib.

    # set the x and y values
    x_vals = np.linspace(0, 2*np.pi, 60)
    y_cos = [np.cos(x) for x in x_vals]
    y_sin = [np.sin(x) for x in x_vals]

# Fig. 1: 
# Display the plot of one period of both the cosine and sine. They should appear on the same axes. Label the axes and the plot. Provide a grid.

    # one single plot
    fig, ax = plt.subplots(figsize=(10,8))
    # plot the lines
    ax.plot(x_vals, y_cos, label='Cosine')
    ax.plot(x_vals, y_sin, label='Sine')
    # labels n shit
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True)
    ax.set_title('Fig. 1: One Period of Cos(x) and Sin(x)')
    plt.legend()

    plt.show()

# Fig 2:
# Display the plot of one period of both the cosine and sine. They should appear on the different axes but share the y-axis. Label the axes and the plot. Provide a grid.

    # two subplots, sharing y axis
    fig, ax = plt.subplots(1, 2, figsize=(10,8), sharey=True)

    ax[0].plot(x_vals, y_cos, color='cornflowerblue')
    ax[1].plot(x_vals, y_sin, color='orange')
    # set x label and grid setting for both axes
    for x in ax:
        x.set_xlabel('x')
        x.grid(True)
    # labels n shit
    ax[0].set_ylabel('f(x) = cos(x)')
    ax[1].set_ylabel('f(x) = sin(x)')
    ax[0].set_title('Cosine')
    ax[1].set_title('Sine')

    plt.suptitle('Fig. 2: One Period of Cos(x) and Sin(x)')

    plt.show()

# Fig 3:
# Display the plot of one period of both the cosine and sine. They should appear on the different axes but share the x-axis. Label the axes and the plot. Provide a grid.

    # two plots sharing x axis
    fig, ax = plt.subplots(2, 1, figsize=(10,8), sharex=True)

    ax[0].plot(x_vals, y_cos, color='cornflowerblue')
    ax[1].plot(x_vals, y_sin, color='orange')

    for x in ax:
        x.set_xlabel('x')
        x.grid(True)

    ax[0].set_ylabel('f(x) = cos(x)')
    ax[1].set_ylabel('f(x) = sin(x)')
    ax[0].set_title('Cosine')
    ax[1].set_title('Sine')

    plt.suptitle('Fig. 3: One Period of Cos(x) and Sin(x)')

    plt.show()