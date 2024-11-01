def my_isDigit(string):
    """
    Checks to see if a string is a digit or not.
    Args:
        string (str) : string input
    Returns:
        (boolean) : True if a digit, false if not a digit
    """
    if type(string) == str:
        for character in string:
            # Check if the character is not a digit (0-9 for positives and negatives)
            if character not in ['.','-', '1', '2', '3', '4', '5', '6', '7','8', '9', '0']:
                return False
    elif type(string) == int or type(string) == float:
        return True
    return True

def listOfFloats(listOfValues):
   """
   Takes a list of values and casts each value to a float. If a number cannot be cast to a 
   float (not a digit, is missing, etc.) then it is replaced with 'NA'.
   Args:
    list (list) : list object containins data from read text files
   Returns:
    (list) : list containing floats
   """
   data = []
   for item in listOfValues[1:]:
      # iterate through list and if a valid digit, append to data list
      if my_isDigit(item) and len(item) > 0 and float(item) > 0 :
         data.append(float(item))
      # if not a digit, replace with 'NA'   
      else:
         data.append('NA')
   return data


def separateColumns(data : list):
    """
    This function takes a list of data and 
    converts them into seperate lists.
    Args:
        data (list) : list containing comma seperated values
    Returns:
        (tuple) : prices, lot_sizes, living_space_sizes, build_years 
    """
    # intiates empty lists corresponding to the columns of the data
    price = []
    lotSize = []
    livingSpace = []
    buildYear = []
    
    # if list of data contains rows that are all strings (separate CSV string data)
    if type(data[1:][0]) == str:
        for row in data:
            for i,item in enumerate(row.split(',')):
                if i == 0:
                    price.append(item)
                elif i == 1:
                    lotSize.append(item)
                elif i == 2: 
                    livingSpace.append(item)
                else:
                    buildYear.append(item)
                    
    # if a list of data contains rows with lists of non-string data types (separate data that has already been cast with castData())
    if type(data[1:][0]) == list:
        for row in data:
            price.append(row[0])
            lotSize.append(row[1])
            livingSpace.append(row[2])
            buildYear.append(row[3])

    return price, lotSize, livingSpace, buildYear

def computeAverage(listOfFloats : list):
   """
   Computes the average of a list of floats.
   Args:
    listOfFloats (list) : list object made up of floats
   Returns:
    (float) : average value of list elements
   """
   total = 0
   try: 
       for item in listOfFloats:
          # convert items to float to make sure all items passed in the list are floats
          item = float(item)
          total += item
       numberOfItems = len(listOfFloats)
       return total / numberOfItems
   except ValueError:
        print('Not all values in the list are digits.')
   except ZeroDivisionError:
        print('Cannot find the average of an empty list.')