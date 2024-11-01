'''
COMP 4401
Homework 2 - Functions & Variable Scope

General Homework Guidelines: 
- Homework must be submitted in a .py file. Please do not submit .ipynb files.
- Homework should not use packages or functions that have not yet been discussed in class.
- Use comments to explain what your code is doing. 
- Use a consistent coding style. 
- Use descriptive variable names.
- Test your code regularly using a variety of different inputs. 
- (NEW) Every function must include a docstring for documentation (see: 
   https://realpython.com/documenting-python-code/). This docstring should include:
     - 1 or 2 lines describing what the function does
     - input parameters, their types and what they are for
     - return data type and what it is
- (NEW) All tests of your functions should be commented out in your final submission or
  encolosed with an if __name__ == '__main__' codeblock.
- (NEW) All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.

Homework 2 Instructions:
You should submit two .py files, this file and a new file you create for problem 6 called : extra_functions.py.

'''
#--------------------------------------------------------------------------#


# 1. Create a function called secondsToHMS that takes an argument `seconds`, 
# an integer number of seconds, and returns a string in the format "xx h, xx m, xx s", 
# where xx is the number of hours, minutes and seconds. This is turning question 6 
# from last week's homework into a function. (15 points)

def secondsToHMS(seconds: int):
	"""
	This function takes the integer input, seconds, and converts it into
	a string made up of converted hours, minutes, and seconds.
	Args:
		seconds (int): time in seconds
	Return:
		'xx h, xx m, xx s' (string): string with hours, minutes, and seconds

	"""
	input_seconds = seconds

	# use modulo and floor division to properly convert seconds to hours, minutes, seconds (since minutes and seconds are base 60)
	seconds = input_seconds % 60
	minutes = input_seconds // 60
	hours = minutes // 60

	timeString = f'{hours} h, {minutes % 60} m, {seconds} s'
	return timeString

if __name__ == '__main__':
    # Test case for secondsToHMS()
    seconds = int(input('Input Seconds:'))
    result = secondsToHMS(seconds)
    print(f"{seconds} is equal to {result}")
    

# 2. Create two functions milesToKm and kmToMiles, each function will take in one 
# parameter, distance, of type float. Each function will convert the distance into 
# either miles or kilometers based on the function used and return that value. 
# (15 points)
# 1 mile = 1.6 kilometers
# 1 kilometer = 0.62 miles

def milesToKm(miles: float):
	"""
	This function takes miles and converts it into kilometers.
	1 mile = 1.6 kilometers.
	Args:
		miles (float): distance in miles
	Return:
		kilometers (float): distance in kilometers
	"""
	#convert mi to km
	kilometers = miles * 1.6
	return kilometers

if __name__ == '__main__':
	# Test case for milesToKm()
	miles = float(input('Input miles for conversion to kilometers:'))
	result = milesToKm(miles)
	print(f'{miles} miles is equal to {result} kilometers')

def kmToMiles(kilometers: float):
	"""
	This function takes kilometers and converts it into miles.
	1 kilometer = 0.62 miles.
	Args:5
		kilometer (float): distance in kilometers
	Return:
		miles (float): distance in miles
	"""
	#convert km to mi
	miles = kilometers * 0.62
	return miles

if __name__ == '__main__':
	# Test case for kmToMiles()
	kilometers = float(input('Input Kilometers for conversion to miles:'))
	result = kmToMiles(kilometers)
	print(f'{kilometers} kilometers is equal to {result} miles')


# 3. Create a function called europeUS that takes 2 paramters, sqmToSqft and euroToDollars, 
# both of type float. The function must return the coverted values as a tuple: sqms, euros. 
# This will allow us to convert real state listings in Europe, which are in metric, to imperial 
# units so we can shop for our next vacation home. (10 points)
# 1 sqm = 10.7639 sqft
# 1 euro = 1.08 dollars

def europeUS(sqmToSqft: float, euroToDollars: float):
	"""
	This function converts two values: 
		- square meters to square feet
		- european dollars (euro) to US dollars (USD)
	Args:
		square meters (float): areas in square meters
		euro (float): european currency 
	Return:
		sqFeet, usDollars (float): tuple containing area of square feet and currency of US dollars
	"""
	# convert sq. meters to sq. feet
	sqMeters = sqmToSqft
	sqFeet = sqMeters * 10.7639

	# convert euros to US dollars
	euros = euroToDollars
	usDollars = euros * 1.08

	return sqFeet, usDollars

if __name__ == '__main__':
	# Test case for eurupreUS()
	sqMeters = float(input('Input Square Meters:'))
	euros = float(input('Input Euros:'))
	sqFeet, usDollars = europeUS(sqMeters, euros)
	print(f'{sqMeters} square meters equals {sqFeet} square feet and {euros} euros is equal to {usDollars} US dollars.')

# 4. Create a function called roadTrip that takes 1 parameter, mpg (miles per gallon), of type float. 
# The function should ask for user input on how far they intend to drive on their road trip. Once 
# you have the distance, calculate the number of gallons they will need to complete the road trip 
# and multiply it by 3.70. Return the cost in gas of the road trip. (15 points)

def roadTrip(mpg: float):
	"""
	This function converts miles, to gallons needed, and then to cost of gas.
	Args:
		mpg (float): miles per gallon of the user's car
	Returns
		total_cost (float): cost of gas based on mileage
	"""
	# calculate total gallons to calculate total cost
	miles = float(input('How many miles will you be driving?'))
	total_gallons = miles / mpg

	total_cost = total_gallons * 3.70

	return total_cost

if __name__ == '__main__':
	# Test case for roadTrip()
	result = roadTrip(mpg=40)
	print(f'Driving {miles} miles will cost ${result}')


# 5. Create a function called insulateHomeCost that takes no parameters and asks the user to input 
# the length, width and height of the the basement of their house. Once you have these values,
# calculate the surface area (sq ft) of each side of the basement. Once you have that value multiply 
# it by 2.75, which is the average cost of spray foam insulation per sqft. Return the value. (15 points)
	
def insulateHomeCost():
	"""
	Take user input of lenth their basement, calculate the area, and then calculate cost
	to insulate basement by multiplying the area by a factor of 2.75.
	Args:
		None
	Return:
		total_cost (float): total cost to insulate the 4 sidewalls of basement
	"""
	length = float(input('length of your basement (feet)?'))
	width = float(input('width of your basement (feet)?'))
	height = float(input('height of your basement (feet)?'))

	total_area = 2*(height*width) + 2*(height*length)
	total_cost = total_area * 2.75

	return total_cost

if __name__ == '__main__':
	# Test insulateHomeCost()
	total_cost = insulateHomeCost()
	print(f'Total cost to insulate your basement: ${total_cost}')

# 6. We're going to practice importing functions from another file. Complete the following steps:
#  - Create a new .py file called extra_functions.py
#  - In extra_functions.py, write a function called midpoint which takes an integer as input and returns 
#    the midpoint between that integer and 0. 
#  - Include an if __name__ == '__main__' codeblock in extra_functions.py to test your midpoint function.
#  - Import extra_functions.py into this file.
#  - Run this line of codee: midpoint_of_10 = midpoint(10)
# (20 points)

# Import function, midpoint(), from extra_functions.py
from extra_functions import midpoint

midpoint_of_10 = midpoint(10)
print(midpoint_of_10)

# 7. Debug the following code (10 points)

def myFunc(height, weight, age):
	"""
	Takes height weight, and age and calculates BMI.
	Args:
		height (float): height in inches
		weight (float) : weight in inches
		age (int) : age in years
	Return:
		float: BMI
	"""
	temp = height * age
	temp2 = height * 12
	temp2 = weight / height**2 * 703

	return temp2
# test function output

if __name__ == '__main__':
	# Test the output of myFunc()
	result = myFunc(65, 127, 24)
	print(result)