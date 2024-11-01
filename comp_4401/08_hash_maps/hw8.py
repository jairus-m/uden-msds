'''
COMP 4401
Homework 8 - Dictionaries & JSON Files

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


# Table with type equivalence between JSON and Python
# Python	            JSON
#--------------------------------
# dict	                object
# list, tuple	        array
# str	                string
# int, long, float	    number
# True	                true
# False	                false
# None	                null

'''
#--------------------------------------------------------------------------#

import json

###----------------------###
###-----Dictionaries-----###
###----------------------###

# 1. Write a function, called listToDict, that takes a list as an argument 
# and returns a dictionary containing the keys 1 through n, where n is the 
# size of the list, and the values correspond to the values in the list. 
# For example, if the list is [2, 6, 6, 1, 7, 9] then the dictionary maps:
# 1 —> 2, 2 —> 6, 3 —>6, 4 —> 1, 5 —> 7 and 6 —> 9. 
# In Python this would be: {1:2, 2:6, 3:6, 4:1, 5:7, 6:9}
# (10 points)

def listToDict(listOfElements : list):
    """
    Takes a list of elements and returns a dictionary containing the keys 1 through n,
    where n is the size of the list, and the values correspond to the values in the list.
    Args:
        listOfElements (list) : list of elements
    Returns:
        dict : dict that maps {index of element : element}
    """
    try:
        if len(listOfElements) > 0:
            dictOfElements = {}
            # enumerate list and use index-value (i-element respectively) as the key-value pairs
            for i, element in enumerate(listOfElements):
                dictOfElements[i+1] = element
            return dictOfElements
        else:
            # error if trying to iterate through a non-iterable
            raise TypeError
    except:
        print('Please input a valid list of elements.')

# 2. Write a function, called newDict, that takes a dictionary as an argument 
# and returns a new dictionary with the keys and values inverted (keys become 
# values and values become keys). 
# What happens if there are duplicate values? 
# (10 points)

def newDict(dictionary : dict):
    """
    This function takes a dictionary as an argument and returns a new dictionary with 
    the keys and values inverted.
    Args:
        dictionary (dict) : dictionary object
    Return:
        dict : inverted key-value pairs
    """
    newDict = {}
    try:
        # error if there are duplicate values (when inverted, having duplicate keys from duplicate keys is ILLEGAL !!!)
        if len(set(dictionary.values())) != len(dictionary.values()):
               raise TypeError
        # use key-value pair and convert to value-key in newDict
        for (key,value) in dictionary.items():
            newDict[value] = key
        return newDict
    except:
        print('Please input a valid dictionary without duplicate values.')
        return newDict

# 3. Write a function, called uniqueElems, that takes a list of values as a 
# parameter and determines if all elements are unique (no repeated values). 
# Return True if all values are unique, False otherwise. Think of a way to use 
# dictionary to perform this task. 
# (10 points) 

def uniqueElems(elements_list : list):
    """
    This function takes a list of elements and determines if all
    elements in the list are unique.
    Args:
        elements_list (list) : list of elements
    Returns:
        boolean : True or False (based on uniqueness of list of elements)
    """
    try:
        # create unique keys from list
        keys = set(elements_list)

        # create a dictionary that stores the counts of each value per unique key
        newDictCounts = {}
        for key in keys:
            newDictCounts[key] = 0
            for element in elements_list:
                if key == element:
                    newDictCounts[key] += 1
                    
        # search newDictCounts for values > 1
        for valueCount in newDictCounts.values():
            state = True
            # if an occurence of value > 1, state = False
            if valueCount > 1:
                state = False
                break
        return state
    except:
        print('Please input a valid list of non-iterable elements.')


# 4. Write a function, called valFrequency, that given a list of values as a 
# parameter, counts the frequencies for each value in the list. You can do this 
# by returning a dictionary (think about what the key should be and what value 
# should be associated with it). 
# For example, if the list is [1, 3, 5, 2, 1, 2, 5, 8, 4, 5] then we have:
# 2 x 1's, 1 x 3's, 3 x 5's, 2 x 2's, 1 x 4's, 1 x 8’s
# In Python this would be: {1: 2, 3: 1, 5: 3, 2: 2, 8: 1, 4: 1}
# (10 points)

def valFrequency(elements_list : list):
    """
    This function takes a list of elements and returns the value counts
    of each element.    
    Args:
        elements_list (list) : list of elements
    Returns:
        dict : dictionary of value counts
    """
    try:
        # error if list with no elements
        if len(elements_list) == 0 or type(elements_list) == set:
            raise TypeError
        # create unique keys from list
        keys = set(elements_list)
        
        # create a dictionary that stores the counts of each value per unique key
        newDictCounts = {}
        for key in keys:
            newDictCounts[key] = 0
            for element in elements_list:
                if key == element:
                    newDictCounts[key] += 1
        return newDictCounts
    except:
        print('Please input a valid list.')


# 5. Write a function, called addsToK, that given an integer k and a list of n 
# unordered integers A, determines if there is a pair of distinct integers in A 
# that add up to k. Returns True if there are, False otherwise.
# For example : given [1, 6, 7, 3, 7, 10, 3] if k=13 then there is a pair of
# integers that add up to 13 : 10 and 3. If k=14 then there isn’t a pair of distinct
# integers that add up to 14 (can’t use 7 twice even if it appears twice in the list) 
# (10 points)

def addsToK(k : int, nums : list):
    """
    This function takes an integer, k, and a list of unnordered intefers, nums, and determines if
    there is a distinct pair of integers in nums that can add up to k.
    Args:
      k (int) : integer value
    Return:
      boolean : True or False
    """
    try:
        # check validity of arguments
        [int(num) for num in nums]
        if type(k) != int or len(nums) == 0:
            raise TypeError
        # create x,y pairs based of unique values of nums
        x = set(nums)
        y = set(nums)

        # create dict of all possible sum:(x,y) key-value pairs
        pairs = {}
        for num_x in x:
                for num_y in y:
                    # if x not equal to y and (x,y) not already in list, pair
                    if num_x != num_y and (num_x, num_y) not in pairs:
                        pairs[int(num_x) + int(num_y)] = (num_x, num_y)
        if k in pairs:
            return True
        else:
            return False
    except:
        print("Please provide an integer argument for 'k' and a non-empty list of integers for 'nums'.")


###-------------------###
###-----JSON FIle-----###
###-------------------###


# 6. Write a function, called senatorsInfo, that takes a filename string
# as an argument. It should load the json file and extract the Senator's 
# following information:
# First name
# Last name
# State
# Party
# Start date (since when they've been Senators)
# Congress number (which sessions of Congress they were Senators for)
# Contact form
# Phone number
# Twitter handle
# Birthday
# Nickname
# The function should write the senators information to a json file
# called senatorsInfo.json. Use an indent of 2 to make the data more
# readable. The function should also return the data, this should 
# be a list of dictionaries.
# Hint: You may want to use the get() method when getting the data
# (20 points)

def senatorsInfo(filename : str):
    """
    Takes a a filename/pathway and loads a json file that extracts Senator's data.
    The data extracted will contain the Sentator's First name, Last name, state, party, start date, congress number,
    contact form, phone number, twitter handle, and nickname.
    Args:
        filename (str) : filename or pathname to senator json file
    Return:
        senatorsInfo.json (json file) : json object containing extracted Senator data 
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                
        # create a list of the keys for senateDict dictionary 
        keys = ['firstname', 'lastname', 'state', 'party', 'startdate', 'congress_numbers', 
                'contact_form', 'phone', 'twitterid', 'birthday', 'nickname']
        
        # initiate list that will hold dictionaries of senator info
        senatePeopleList = []
        for i in range(len(data['objects'])):
            senatePerson_dict = {}
            for key in keys:
                try:
                    # get the data that is accessed with objects --> index --> 'person' --> key
                    senatePerson_dict[key] = data['objects'][i]['person'][key]
                except KeyError:
                    try:
                        # get the data that is accesssed with objects --> index -> key
                        senatePerson_dict[key] = data['objects'][i][key]
                    except KeyError:
                        try:
                            # get data that is accessed with objects --> index --> 'extra' --> key
                            senatePerson_dict[key] = data['objects'][i]['extra'][key]
                        except:
                            # if no key found, append ''
                            senatePerson_dict[key] = ''
                    except:
                        senatePerson_dict[key] = ''
                except:
                    senatePerson_dict[key] = ''
            senatePeopleList.append(senatePerson_dict)
        # convert list to json object
        senators_json_object = json.dumps(senatePeopleList, indent = 2)  

        # output json file
        output_filename = 'senatorsInfo.json'
        with open(output_filename, 'w') as output_file:
            output_file.write(senators_json_object)
        return senatePeopleList
    except:
        print('Please enter a valid filename.')


# 7. Write a function, called noContactForm, that takes in a filename string, 
# loads the data in from a json file and returns a list containing the first
# and last name of the senators that do 
# not have a contact form.
# (15 points)

def noContactForm(filename : str):
    """
    Takes a filename/path, loads the data from json file, and returns a list 
    continaing the first and last name of the senators that do not have a contact form.
    Args:
        filename (str) : filename or pathname to senator json file
    Return:
        list : list of the full names of senators without a contact form
    """
    try:
        senatePeopleList = senatorsInfo(filename)
        missingForms_FullNames = []
        for i in range(len(senatePeopleList)):
            if senatePeopleList[i]['contact_form'] == '':
                missingForms_FullNames.append(f"{senatePeopleList[i]['firstname']} {senatePeopleList[i]['lastname']}")
        return missingForms_FullNames
    except:
        # default to error message of senatorsInfo()
        pass

# 8. Write a function, called congressSessionMembers, that takes a congress session
# sessionNumber (int) and a filename (str). It should load the data created in question 6 
# and search for all the senators that were part of that particular session of congress. 
# The function should write the resulting senators to a file called 
# congressSession{sessionNumber}.json and returns a list of every senator that was 
# part of the Senate for the given sessionNumber. It should return an empty
# list if none of the senators were members for that congress. 
# (Congress session 1 should have nobody in it (except maybe Chuck Grassley
# and Mitch McConnell)).
# The numbers of senators for each Congress session available.
# sessionNumber 116 = 33
# sessionNumber 117 = 64
# sessionNumber 118 = 100
# sessionNumber 119 = 66
# sessionNumber 120 = 34
# all other session numbers should be empty
# (15 points)

def congressSessionMembers(filename : str, sessionNumber : int):
    """
    This takes a filename/path and sessionNumber, loads data from a json file on Sentaors, and 
    returns a list of every senator (full name) that was part of that particular session of congress.
    Args: 
        filename (str) : filename or pathname to senator json file
        sessionNumber (int) : session number (aka congress number) that senators were part of
    Returns:
        list : list of full names of senators that were part of a particular session number
    """
    try:
        senatePeopleList = senatorsInfo(filename)
        sessionNumber = int(sessionNumber)

        # create the list of congress members that are present in a user specified session of congress
        inSession_FullNames = []
        for i in range(len(senatePeopleList)):
            if sessionNumber in senatePeopleList[i]['congress_numbers']:
                inSession_FullNames.append(f"{senatePeopleList[i]['firstname']} {senatePeopleList[i]['lastname']}")

        # convert list to json object
        senators_json_object = json.dumps(inSession_FullNames, indent = 2)  

        # output json file
        output_filename = f'congressSession{sessionNumber}.json'
        with open(output_filename, 'w') as output_file:
            output_file.write(senators_json_object)

        return inSession_FullNames
    except ValueError:
        print('Please enter a valid number for sessionNumber.')
    except:
        # default to error message of senatorsInfo()
        pass