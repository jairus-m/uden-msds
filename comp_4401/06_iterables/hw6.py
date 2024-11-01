'''
COMP 4401
Homework 6 - Lists & Tuples

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
'''
#--------------------------------------------------------------------------#

# In this assignment we will be working with a Kaggle dataset 
# (https://www.kaggle.com/datasets/bryan2k19/dutch-house-prices-dataset). This is a real state 
# dataset from the Netherlands. The data contains 16 columns and 5555 entries. 

# Our objective with this data is to import and analyze this data in order to help a family 
# member purchace a home in the Netherlands. They will be letting us sleep on their couch in 
# exchange for this service.



###---------------###
###-----Lists-----###
###---------------###

from helper_functions6 import listOfFloats, my_isDigit, separateColumns, computeAverage

# 1. Create a function, called importData, that takes the file name as an argument. The function 
# must handle an exception when the file is not found (this occurs when the file does not exist, 
# if it was misspelled or it's in a different directory). If the exception is raised, the function 
# must ask the user to re-enter the file name and check again. 
# Repeat this as many times as needed until the data is read in. If the user enters nothing, the 
# function should terminate. The function should return the data that was read in, it should be of 
# type list, or return an empty list if the user terminated the function. 
# The output list should have length 5556 
# (10 points)

def inputData(filename: str):
    """
    Reads in data from .csv text file and returns it as a list.
    Args:
      filename (str) : path or name of file
    Returns:
      (list) : list containing the rows of the of the .csv file
    """
    while True:
      # make sure filename input is a string
      if type(filename) != str:
          raise ValueError('Please input a filename as a string.')
      
      # If invalid filename, repeatedly ask user until function receieves a valid filename
      if filename == '':
        return []
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

# 2. Create a function, called castData, that takes in the data read in by the previous function, 
# this should be a list of strings. The function should perform the following casts : 
# Price --> float
# Lot size (m2) --> float
# Living space size (m2) --> float
# Build year --> int
# The function should return the data after fixing the data types, this should be of type list.
# Be mindful of errors in the data, you will need to handle exceptions ! 
# Output list should have length 5438. 
# (10 points)

def castData(data : list):
    """
    Takes in data read in by the previous function, inputData(), and casts price to float, 
    lot size to float, living space to float, and build year to int.
    Args:
        data (list) : data read in by inputData
    Returns:
        (list) : data with the correct cast datatypes
    """

    column_names = data[0].split(',')

    price, lotSize, livingSpace, buildYear = separateColumns(data)

    # convert using listOfFloats() (also handles non-numeric data and missing values)
    price = listOfFloats(price)
    lotSize = listOfFloats(lotSize)
    livingSpace = listOfFloats(livingSpace)
    buildYear = listOfFloats(buildYear)
    
    # convert build_years from float to int 
    for i, year in enumerate(buildYear):
        if my_isDigit(year):
            buildYear[i] = int(year)
        else:
            buildYear[i] = 'NA'
            
    for i,year in enumerate(buildYear):
        if my_isDigit(year) == True and year > 2023:
            buildYear[i] = year / 10
        
    # list comprehension to zip or merge the price/lotSize/livingSpace/buildYear lists together
    # this list still has missing / non-numeric data that were replaced with 'NA' in order to maintain the index of the rows
    converted_data_with_NAs = [list(row) for row in zip(price, lotSize, livingSpace, buildYear)]
    
    # remove all rows with 'NA' values 
    converted_data = []
    for row in converted_data_with_NAs:
        if 'NA' not in row:
            converted_data.append(row)
    
    
    # add column names back
    converted_data.insert(0, column_names) 
    
    return converted_data

# 3. Create a function, called averageValues, that takes in a list. The list contains the price,
# lot size, living space and build year. The function must deal with missing values, keeping 
# track of the number of data points collected for each field (required for computing the average),
# and realistic data points for the year built column.
# The function should return a tuple containing the average home price, lot size, living space, 
# and build year for all homes. Your output should be :
# (557707.7581831556, 686.6248620816476, 146.34608311879367, 1968.9804836656767)
# (10 points)

def averageValues(data : list):
    """
    Takes in a list of data that contains price/lot size/living space/build year and outputs a tuple
    containing average home price, lot size, living space, and build year for all homes.
    Args:
      data (list) : data read in by inputData
    Returns:
      (tuple) : avgHomePrice, avgLotSize, avgLivingSpace, avgBuildYear
    """
    # read in and seperate data
    data = castData(data)
    price, lotSize, livingSpace, buildYear = separateColumns(data)

    # slice numerical data only (remove column names)
    price = price[1:]
    lotSize = lotSize[1:]
    livingSpace = livingSpace[1:]
    buildYear = buildYear[1:]
    
    # if year is greater than 2023, fix the abnormalities by dividing by 10
    for i,year in enumerate(buildYear):
        if year > 2023:
            buildYear[i] = year / 10
    
    return computeAverage(price), computeAverage(lotSize), computeAverage(livingSpace), computeAverage(buildYear)

# 4. Create a function called filterByValues that takes in a list containing real estate 
# information, a minimum price and maximum price, these must be of type list, float and float 
# respectively. The function should return the average home price, lot size, living space, and 
# build year of all homes that fit between the minimum and maximum home values given. 
# Result should be returned as a tuple in the order price, lot size, living space, and build year.

# When function called with minPrice = 100000 and maxPrice = 400000, output should be:
# (324395.9323770492, 216.56045081967213, 110.17930327868852, 1966.869722557298) 
# (10 points)

def filterByValues(data : list, minPrice=None, maxPrice=None):
    """
    This function takes in a list with real estate information, a minimum/maximum price, aand will filter the data based on the 
    min/max price. It will then return avgHomePrice, avgLotSize, avgLivingSpace, and avgBuildYear for the filtered data.
    Args:
      data (list) : list of data read in by inputData
      minPrice (float) : minimum buy price to filter by
      maxPrice (float) : maximum buy price to filter by
    Returns:
      (tuple) : avgHomePrice, avgLotSize, avgLivingSpace, avgBuildYear of filtered data
    """
    # if no min/max input return averages for entire dataset
    if minPrice == None and maxPrice == None:
        return averageValues(data)
    
    filtered_rows = []
    
    # if maxPrice entered and no minPrice entered
    if minPrice == None and (type(maxPrice) == float or type(maxPrice) == int):
        for row in castData(data):
            if my_isDigit(row[0]) == True and row[0] < maxPrice:
                filtered_rows.append(row)
    # if minPrice entered and no maxPrice entered
    elif maxPrice == None and (type(minPrice) == float or type(minPrice) == int):      
        for row in castData(data):
            if my_isDigit(row[0]) == True and row[0] > minPrice:
                filtered_rows.append(row)
    # if minPrice/maxPrice entered            
    else:
        for row in castData(data):
            if my_isDigit(row[0]) == True and row[0] > minPrice and row[0] < maxPrice:
                filtered_rows.append(row)

    # list comprehension to get columns
    price = [row[0] for row in filtered_rows]
    lotSize = [row[1] for row in filtered_rows]
    livingSpace = [row[2] for row in filtered_rows]
    buildYear = [row[3] for row in filtered_rows]
            
    return computeAverage(price), computeAverage(lotSize), computeAverage(livingSpace), computeAverage(buildYear)


###----------------###
###-----Tuples-----###
###----------------###


# 5. Write a function, called minMaxTuple, that takes a list of numbers and returns 
# the smallest element and the largest element as a tuple (smallest, largest). Cannot 
# use the built-in functions min()/max().
# For example : lst = [6, 3, 8, 23, -4, 35] should return (-4, 35) 
# (10 points)

import math
def minMaxTuple(numbers : list):
    """
    Takes a list of numbers and returns the smallest element and the largest element as a tuple (smallest, largest).
    Args:
      numbers (list) : list of numbers 
    Returns:
      (tuple) : (minimum, maximum)
    """
    # if empty list, return []
    if numbers == []:
        return ()
    minimum = math.inf
    for num in numbers:
        if num < minimum:
            minimum = num
        else:
            pass
    maximum = -math.inf
    for num in numbers:
        if num > maximum:
            maximum = num
        else:
            pass
    return (minimum, maximum)

# 6. Write a function, called allPairs, that takes two lists as paramters, x and y, 
# and returns a new list containing all possible pairs consisting of one element from 
# x and one element from y as long as they are not the same. Cannot use built-in 
# functions or sets.
# For example: If the list x = [1, 4, 6, 8] and y = [5, 2, 6] then the result is the list 
# [(1, 5), (1, 2), (1, 6), (4, 5), (4, 2), (4, 6), (6, 5), (6, 2), (8, 5), (8, 2), (8, 6)]. 
# Note that (6, 6) doesn't appear because they are the same element. 
# (10 points)

def allPairs(x:list, y:list):
    """
    Takes two lists of elements and returns a new list containing all possible
    unique pairs without repeating elements within those pairs.
    Args:
      x (list) : list of elements
      y (list) : list of elements
    Returns:
      (list) : list of all possible unique pairs without repeating numbers within those pairs
    """
    # to prevent repeats, make new lists for input params, x and y, without duplicates
    x_unique = []
    y_unique = []
    [x_unique.append(num_x) for num_x in x if num_x not in x_unique]
    [y_unique.append(num_y) for num_y in y if num_y not in y_unique]

    # create new list of all pair combos
    pairs = []
    for num_x in x_unique:
        for num_y in y_unique:
            # if x not equal to y and (x,y) not already in list, pair
            if num_x != num_y and (num_x, num_y) not in pairs:
                pairs.append((num_x, num_y))
    return pairs

# 7. Write a function, called removeDups, that takes a list of tuples and removes any 
# duplicate tuples and returns the modified list. Cannot use built-in functions nor 
# sets.
# For example if the list contains [(1, 2), (1, 4, 5), (1, 2), (3, 5)] then the list 
# will become [(1, 2), (1, 4, 5), (3, 5)]. 
# (10 points)

def removeDups(paired_numbers:list):
    """
    Takes a list of tuples and removes any duplicates.
    Args:
      paired_numbers (list) : list containing paired numbers
    Returns:
      (list) : list containing unique pairs only (without duplicates)
    """
    unique_pairs = []

    # list comprehension that appends pair from original list to unique_list of not already in unique_list
    [unique_pairs.append(pair) for pair in paired_numbers if pair not in unique_pairs]

    return unique_pairs


# 8. Create a function, called resultTuples, which takes a location as an argument, this
# should be of type str. The function will create namedtuples named realEstate. Each 
# namedtuple should have the fields : 
# Location, CheapestBuyPrice, AvgBuyPrice and MostExpBuy. BestLot/BestLiving ?
# To create each tuple you will need to make function calls to our previously defined
# functions in this homework. Also keep in mind that  The function must return the namedtuple created.

# Note1: You will also need to convert the units from sqmt to sqft and euros to 
# dollars using the functions from previous homeworks.
# Note2: You will need to place those functions in the extra_functions.py file and
# import them to use them as we've done in the past.
# Note3: You may need to modify our previously used functions so they work with our
# data.

# Output should look like this :
# (the location can change, I used Madrid as an example, numerical values are correct) :
# realEstate(Location='Madrid', CheapestPrice=149000.0, AvgPrice=557707.7581831556, MostExp=4700000.0)
# (10 points)

from collections import namedtuple
def resultTuples(location: str):
    """
    Takes location as an arguement and creates/returns a namedtuple, "realEstate" with the fields
    Location, CheapestBuyPrice, AvgBuyPrice and MostExpBuy.
    Args:
      location (str) : city location
    Returns:
      namedtuple : realEstate(Location=, CheapestPrice, AvgPrice, MostExp)
    """
    data = castData(inputData('hw6_data.csv'))

    realEstate = namedtuple('realEstate', ['Location', 'CheapestBuyPrice', 'AvgBuyPrice', 'MostExpBuy'])
    
    price, lotSize, livingSpace, buildYear = separateColumns(data)
    
    cheapestPrice = minMaxTuple(price[1:])[0]
    mostExpensivePrice = minMaxTuple(price[1:])[1]
    avgRentPrice = computeAverage(price[1:])
    
    location_summary = realEstate(location, cheapestPrice,avgRentPrice, mostExpensivePrice)
    
    return location_summary