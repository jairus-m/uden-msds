'''
COMP 4401
Homework 5 - File Input/Output & Exception Handling

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



In this assignment we will be working with a Kaggle dataset 
(https://www.kaggle.com/datasets/bryan2k19/dutch-house-prices-dataset)
(https://www.kaggle.com/datasets/mirbektoktogaraev/madrid-real-estate-market). 
This is a real state dataset from the Netherlands and Madrid, Spain. The data 
contains 16 columns with 5555 entries and 58 columns with 21.7k entries respectively.
We will be working with a subset of the data split into multiple files. 

Our objective with this data is to import and analyze this data in order to help a family 
member purchace a home in the Netherlands/Madrid. They will be letting us sleep on their 
couch in exchange for this service. A fair trade.
'''
#--------------------------------------------------------------------------#

from helper_functions import sqMeterToSqFeet, eurosToUSD, my_isdigit


# 1. Create a function, called inputData, that takes a file name as an argument. 
# The function must handle an exception if the file is not found (this occurs 
# when the file does not exist, if it was misspelled or it's in a different 
# directory). The function must read in the data from the file and return it
# as a list. 
# (15 points)

def inputData(filename: str):
    """
    Reads in data from .csv text file and returns it as a list.
    Args:
      filename (str) : path or name of file
    Returns:
      (list) : list containing the rows of the of the .csv file
    """
    # make sure filename input is a string
    if type(filename) != str:
        raise ValueError('Please input a filename as a string.')
    
    # If invalid filename, repeatedly ask user until function receieves a valid filename
    while True:
      try:
        file = open(filename, 'r')
        data = []
        for line in file.readlines():
            line = line.strip()
            if len(line) > 0:
                data.append(line)
        file.close()
        return data
      except FileNotFoundError:
        filename = input('No file found. Please re-check the file path or filename.')

# 2. Create a function, called listOfFloats, that takes a list of values and casts
# each value to a float. The function must be able to handle exceptions dealing with
# missing values and values that cannot be cast to a float, i.e. "fdshjksd". The
# function must return a list of floats. Note: you must create an empty list inside 
# the function, and append the casted values to it, then return it. 
# (15 points)

def listOfFloats(list):
   """
   Takes a list of values and casts each value to a float.
   Args:
    list (list) : list object containins data from read text files
  Returns:
    (list) : list containing floats
   """
   data = []
   for item in list:
      # iterate through list and if a valid digit, append to data list
      if my_isdigit(item) and float(item) > 0:
         data.append(float(item))
      # if not a digit, do not apppend to data list (pass)   
      else:
         pass
   return data
      
# 3. Create a function, called computeAverage, that takes in a list of floats as an 
# argument. All elements in the list must be floats in order to perform any calculations.
# You cannot use any built-in function to compute the average, instead add up all the
# values and divide by the total number of values you have. Return the average (this
# should be a float). 
# (15 points)

def computeAverage(list):
   """
   Computes the average of a list of floats.
   Args:
    list (list) : list object made up of floats
   Returns:
    (float) : average value of list elements
   """
   total = 0
   try: 
       for item in list:
          # convert items to float to make sure all items passed in the list are floats
          item = float(item)
          total += item
       numberOfItems = len(list)
       return total / numberOfItems
   except ValueError:
        print('Not all values in the list are digits.')
   except ZeroDivisionError:
        print('Cannot find the average of an empty list.')

# 4. Create a function, called filteredData, that takes filename and maxPrice as arguments,
# of types string and float respectively. The function should loop over the list and store the
# results that satisfy the maxprice criteria in a new list (amount is <= maxPrice).
# (use : 
# filteredResults = []
# filteredResults.append(filteredDataPoint) to add the data to the new list). 
# Return the list with the new results. The function must handle the exception of getting an 
# incorrect max value, i.e. "bjfdsk". 
# (15 points)

def filteredData(filename, maxPrice: float):
   """
   This function takes a list and stores values into a new list that meets 
   a specfic criteria, maxPrice.
   Args:
    filename (str) : file path or file name
    maxPrice (float) : maximum price to filter by (i.e store values less then maxPrice)
  Returns:
    (list) : list of floats that are less than the max price specified
   """
   # from filename, convert to a list object, and then cast valid numbers to floats
   data = listOfFloats(inputData(filename))
   # make sure the maxPrice parameter is at least a number of type int or float (although documentation calls for a float)
   if type(maxPrice) != float and type(maxPrice) != int:
      raise TypeError("Input parameter 'maxPrice' must be of type integer or float.")
   filteredResults = []
   try:
      for item in data:
        # convert items to float to make sure all items passed in the list are floats (no strings or 'asdf' allowed)
        item = float(item)
        if item <= maxPrice:
           filteredResults.append(item)
      return filteredResults
   # for redundancy (though listOfFloats() should prevent this), raise ValueError if the filename leads to data that does not contain all digits
   except ValueError:
         print('Not all items in list are digits.')

# 5. Create a function, called realStateAnalysis, that takes a location, type string. The 
# function must ask the user for the file names for buy prices, living space and rent prices 
# whilst handling the file not found error (there is a clever to do this). 

def realStateAnalysis(location: str):
    """
    This codes takes a location, asks the user for 3 file names (for buy price, rent price, living space)
    of the location, and outputs the location, avereage buy price, average rent price, and then average living space.
    Args:
      location (str) : city location
    Returns:
      tuple : location, avg_buyPrice, avg_rentPrice, avg_livingSpace
    """
    # get valid filename from user and save data as list 
    buyPriceData = inputData(input(f'Type in file for buy price corresponding to {location}: '))
    rentPriceData = inputData(input(f'Type in file for rent price corresponding to {location}: '))
    livingSpaceData = inputData(input(f'Type in file for living space corresponding to {location}: '))

    # cast data to floats
    buyPriceDataFloats = listOfFloats(buyPriceData)
    rentPriceDataFloats = listOfFloats(rentPriceData)
    livingSpaceDataFloats = listOfFloats(livingSpaceData)
    
    # calculate averagea
    avg_buyPrice = eurosToUSD(computeAverage(buyPriceDataFloats))
    avg_rentPrice = eurosToUSD(computeAverage(rentPriceDataFloats))
    avg_livingSpace = sqMeterToSqFeet(computeAverage(livingSpaceDataFloats))
    
    return location, avg_buyPrice, avg_rentPrice, avg_livingSpace

# The function must ask the user to enter a file name until they entered a valid file name.
# Note: the file names must have the extension .csv to work

# The function must then compute the average buy price, average rent price and average living 
# space. Perform checks on your data as the data may not be very clean (you should expect 
# missing values and negative values. You must deal with them).

# Write the results in a file called : realStateAnalysis.csv using the following format :
# Location, Avg_buy_price, Avg_rent_price, Avg_sqft

# Note 1: the living space is in square meters, rent and buy prices are in euros, so create
# a second file, helper_functions.py and use our previously defined function to convert sqmt 
# to sqft and euros to dollars (you may need to modify the function to make it work).
# Note 2: You must also use whichever functions created in this homework to accomplish this task.
# Note 3: You will need to call the function twice, once for the data for Madrid and another for
# the Netherlands
# The output for the function should look like this :
# Madrid, 578091.9661429492, 1434.4682101167316, 883.9385353229587
# Netherlands, 602963.3547672321, 3014.7843377841937, 1576.2050598919893
# (40 points)

if __name__ == '__main__':
  print(realStateAnalysis('Madrid'))
  print(realStateAnalysis('Netherlands'))