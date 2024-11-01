'''
COMP 4401
Homework 4 - Classes & Unit Tests

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
     - input parameters, their types and what they are for
     - return data type and what it is
- All tests of your functions should be commented out in your final submission or
  encolosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.


Homework 4 Instructions:
1. You should submit two .py files, this file and a new file you create for called :
called : test_classes.py.

2. Every class, method and function must have proper DocString documentation of the
following form :

def someFunction(arg1, arg2):
    """
    Function DocString. Indent the DocString.
    One or two lines explaining what the function does

    Args:
        arg1 (type): what is this argument
        arg2 (type): what is this argument

    Return:
        (type): what is being returned by the function ?
    """
    #your code here


class SomeClassIMadeUp:
    """
    Class DocString. Indent the DocString
    One or two lines explaining what the class does

    Attributes:
    ----------------------------------------
        attr1 (type): what is this attribute
        attr2 (type): what is this attribute

    Method:
    ----------------------------------------
        method1: what does this method do
        method2: what does this method do
    """

def method_inside_class(arg1, arg2):
    """
    Method DocString. Indent the DocString
    One or two lines explaining what the method does

    Args: (don't include 'self' in the arguments)
        arg1 (type): what is this argument
        arg2 (type): what is this argument

    Return:
        (type): what is being returned by the method ?
    """


'''
#--------------------------------------------------------------------------#


###---------------------###
###------ Classes ------###
###---------------------###

# 1. Complete the following class.
# The class must have the following attributes :
# -color (str)
# -year (int)
# -make (str)
# -model (str)
# -num_doors (this includes the hatch/tail gate) (int)
# -engine_type (gas, diesel, electric) (str)
# -top_speed in miles/hour (float)
# -mpg (miles per gallon, float)

class Car:
   """
   This class is for the Car object. 

    Attributes:
    ----------------------------------------
        make (str): make or brand of the car
        model (str): specific model of the car
        year (int): year that the car was produced
        color (int): color of the car
        num_doors (int): total number of doors including the hatch/tail gate
        top_speed (float): top speed of car in miles per hour
        mpg (float): miles per gallon
        num_cars (int): counts the number of instances of Car objects

    Methods:
    ----------------------------------------
        changeColor: changes the color of the car
        carInfo: returns the make, model, and color of the Car instance
        betterGasMileage: compares the mpg of two cars and returns the car info of the car with better mpg
        getNumCars: returns the number of instances of the Car object
    """
   # class variable initialized at 0
   num_cars = 0

   def __init__(self, make: str, model: str, year: int, color: str, num_doors: int, engine_type: str, top_speed: float, mpg: float):
       """
       Assigns initial attributes of Car class
       """
       self._make = make
       self._model = model
       self._year = year
       self._color = color
       self._num_doors = num_doors
       self._engine_type = engine_type
       self._top_speed = top_speed
       self._mpg = mpg
       # every time __init__ is called to make a new Car instance, this will increment the number of cars
       Car.num_cars += 1


# 2. Complete the following methods :
# changeColor: this method should take in a color as an argument (str)
# and change the color attribute of the Car instance

   def changeColor(self, new_color: str):
       """
       This method will change the color attribute of the Car class 
       Args:
        new_color (str) : a new color value 
      Returns:
        None 
       """
       self._color = new_color
       return None

# carInfo: this method should take no arguments and return a string
# with the basic car info in the format : "Make - Model - Color"

   def carInfo(self):
       """
       Returns the make, model, and color of the car object
       Args:
            None
       Returns:
         (str) : 'Make - Model - Color' 
        """
       return self._make + ' - ' + self._model + ' - ' + self._color

# 3. Complete the following method :
# betterGasMileage: this method should take two instances of the Car
# class and return the car info, using the carInfo method, of the car
# instance that gets the better gas mileage.
   def betterGasMileage(self, other):
       """
       This method compares the mpg of two cars and returns the car info
       of the car with better gas mileage
       Args:
        self (Car object) : car one
        other (Car object) : car two
        Returns:
          (str) : car info or statement that both cars have equal mpg
        """
       if self._mpg > other._mpg:
           return self.carInfo()
       elif self._mpg < other._mpg:
           return other.carInfo()
       else:
           return 'MPGs of both cars are equal'


# 4. Create the following class attribute and class method :
# create a class attribute, called num_cars, which increases every time
# a new Car instance is created.

    # the class attribute num_cars was included in the def __init__ code block of 
    # question # 1

   @staticmethod
   def getNumCars():
    """
    This method will return the number of instances of the Car object
    Args:
        None
    Returns
        (int): number of instances of car object
    """
    return Car.num_cars


# 5. Make a parent class for Car, called Vehicle, which will
# contain an __init__ method for the following attributes :
# -color (str)
# -year (int)
# -make (str)
# -model (str)
# -top_speed in miles/hour (float)
# -mpg (miles per gallon, float)
#
# Don't forget to change the Car class __init__ method to make use of the Vehicle class.

class Vehicle:
    """
    This is the class for the Vehicle object
    Attributes:
    ----------------------------------------
        make (str): make or brand of the car
        model (str): specific model of the car
        year (int): year that the car was produced
        color (int): color of the car
        top_speed (float): top speed of car in miles per hour
        mpg (float): miles per gallon

    """
    def __init__(self, make: str, model: str, year: int, color: str, top_speed: float, mpg: float):
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._top_speed = top_speed
        self._mpg = mpg


class Car(Vehicle):
   """
   This class is for the Car object. 

    Attributes:
    ----------------------------------------
        make (str): make or brand of the car
        model (str): specific model of the car
        year (int): year that the car was produced
        color (int): color of the car
        num_doors (int): total number of doors including the hatch/tail gate
        top_speed (float): top speed of car in miles per hour
        mpg (float): miles per gallon
        num_cars (int): counts the number of instances of Car objects

    Methods:
    ----------------------------------------
        changeColor: changes the color of the car
        carInfo: returns the make, model, and color of the Car instance
        betterGasMileage: compares the mpg of two cars and returns the car info of the car with better mpg
        getNumCars: returns the number of instances of the Car object
    """
   num_cars = 0

   def __init__(self, make: str, model: str, year: int, color: str, num_doors: int, engine_type: str, top_speed: float, mpg: float):
       """
       Assigns initial attributes of Car class and inherits some attrinutes from class, Vehicle
       """
       Vehicle.__init__(self, make, model, year, color, top_speed, mpg)
       self._num_doors = num_doors
       self._engine_type = engine_type
       Car.num_cars += 1
    
   def changeColor(self, new_color: str):
       """
       This method will change the color attribute of the Car class 
       Args:
        new_color (str) : a new color value 
      Returns:
        None 
       """
       # makes sure that the new_color will be a string so that the color attributes remains the correct datatype
       if not isinstance(new_color, str):
            raise TypeError("The new_color argument must be a string.")
       else:
            self._color = new_color
       return None
   
   def carInfo(self):
       """
       Returns the make, model, and color of the car object
       Args:
            None
       Returns:
         (str) : 'Make - Model - Color' 
        """
       return self._make + ' - ' + self._model + ' - ' + self._color
   
   def betterGasMileage(self, other):
       """
       This method compares the mpg of two cars and returns the car info
       of the car with better gas mileage
       Args:
        self (Car object) : car one
        other (Car object) : car two
        Returns:
          (str) : car info or statement that both cars have equal mpg
        """
       if self._mpg > other._mpg:
           return self.carInfo()
       elif self._mpg < other._mpg:
           return other.carInfo()
       else:
           return 'MPGs of both cars are equal'
       
   @staticmethod    
   def getNumCars():
    """
    This method will return the number of instances of the Car object
    Args:
        None
    Returns
        (int): number of instances of car object
    """
    return Car.num_cars