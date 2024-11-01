'''
COMP 4401
Homework 3 - Control Flow Statements

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

# 1. Create a function distanceConversion that takes in two parameters, distance and unit, 
# of types float and string respectively. Based on the unit type, "metric" or "imperial", it 
# will convert distance into miles or kilometers. This is creating a single function from 
# milesToKm and kmToMiles in the last homework. (10 points)

def distanceConversion(distance: float, unit: str):
	"""
	Takes a distance and the units (metric or imperial) and will convert the distance to 
	either metric or imperial units.
	Args:
		distance (float) : numeric distance
		units (string)   : 'metric' or 'imperial' 
	Returns:
		convertered_value (float) : the converted distance in the proper units
	"""
	distance = distance
	unit = unit

	# converting distance basaed on user input of 'units'
	if unit == 'imperial':
		kilometers = distance * 1.6
		converted_value = f'{round(kilometers,2)} kilometers'
	else:
		miles = distance * 0.62
		converted_value = f'{round(miles, 2)} miles'
	return converted_value

if __name__ == '__main__':
	# input test case for distanceConversion
	distance = float(input('Enter distance: '))
	units = str(input("Enter units, 'metric' or 'imperial': "))
	print(distanceConversion(distance, units))


# 2. Create a function called brickPath that takes three parameters: wallLength, smallBricks, and largeBricks.
# You want to make a row of bricks that is wallLength inches long with the given length of the small and large 
# bricks. Return 'Possible' if it is possible to make the goal by choosing from the given bricks. Otherwise 
# return 'Not Possible'.
# For example: 
# If wallLength = 8, smallGBricks = 2, largeGBricks = 3 then it’s not possible because there is no way 
# to get 8 inches using the given bricks. 
# On the other hand, wallLength = 7 with smallBricks = 2 and largeBricks = 3 is possible (1 large and 2 small 
# gives you 7). (15 points)

def brickPath(wallLength: int, smallBricks: int, largerBricks: int):
	"""
	Given the length of a wall and the length of the small/large bricks, this function will tell you if it is
	possible to create a row of bricks that is the correct length using the small/large bricks.
	Args:
		wallLength (int)   : length of wall (inches)
		smallBricks (int)  : length of small birck (inches)
		largeBricks (int)  : length of large bricks (inches)
	Returns:
		'possible' or 'impossible" (string) : whether it is possible or impossible to create wall with given bricks
	"""
	wallLength = wallLength


	smallBricks = smallBricks
	largerBricks = largerBricks

	if smallBricks > largerBricks:
		print('Smaller brick must be a smaller value.')
		return 'Please restoart the script and try again.'
	else:
		# checks if small / larger brick are multiples of the wall length
		if wallLength % smallBricks == 0:
			return 'Possible'
		elif wallLength % largerBricks == 0:
			return 'Possible'
		# checks to see once any multiple of bricks are laid, if the other size can fill the remainder
		elif wallLength % largerBricks == smallBricks:
			return 'Possible'
		elif wallLength % smallBricks == largerBricks:
			return 'Possible'
		# checks to see if the bricks added together are a multiple of wall length or have a remainder that can be filled with either brick
		elif wallLength % (smallBricks + largerBricks) == 0 or \
			wallLength % (smallBricks + largerBricks) == smallBricks or wallLength % (smallBricks + largerBricks) == largerBricks:
			return 'Possible'
		else:
			return 'Not Possible'

if __name__ == '__main__':
	# test for brickPath
	wallLength = int(input('Length of wall: '))
	# make sure that the user input for the smaller brick < larger brick
	smallBricks = 1
	largerBricks = -1
	while smallBricks > largerBricks:
		print('Please maker sure the smaller brick is < larger brick.')
		smallBricks = int(input('Length of small bricks: '))
		largerBricks = int(input('Length of larger bricks: '))
	print(brickPath(wallLength, smallBricks, largerBricks))


# 3. Write a function, called calcSum, that takes 3 integer values as arguments: a, b and c. The function 
# must return their sum. However, if one of the values is a duplicate, the duplicate value does not count 
# towards the sum. You cannot use the built-in method sum().
# For example 2, 4, 5 returns 11. The inputs 2, 2, 5 returns 7 and the inputs 1, 1, 1 returns 1. (10 points)

def calcSum(a: int, b: int, c: int):
	"""
	This function takes 3 integer values and returns their sum for non duplicate inputs.
	Args:
		a (int) : first integer
		b (int) : second integer
		c (int) : third integer
	Returns:
		sum (int) : sum of three integers (not including duplicates)
	"""
	a = a
	b = b
	c = c

	# if all numbers the same, return the single value
	if a == b and b == c:
		sum = a
	# if 2 of 3 integers are the same, sum up the two unique values only 
	elif b == c:
		sum = a + b
	elif a == c:
		sum = b + c
	elif a == b :
		sum = a + c
	# if all numbers different, sum up the 3 unique values
	else:
		sum = a + b + c
	return sum

if __name__ == '__main__':
	# test for calcSum
	a = int(input('a int: '))
	b = int(input('b int: '))
	c = int(input('c int: '))
	print(calcSum(a, b, c))


# 4. Create a function that takes in 4 parameters, intVal, strVal, floatVal, and floatVal2. Check that each 
# parameter is of the corresponding type, int, string, float and float respectively. If their data type does 
# not match these types, cast them to the right data type. Then return all 4 values as a tuple. (10 points)

def dataTypeCheck(intVal, strVal, floatVal, floatVal2):
	"""
	This function checks to see if four inputs are the correct corresponding data type. If the data type
	is not correct, they will be cast to their correct datat type.
	Args:
		intVal (int) : some integer value
		strVal (str) : some string value
		floatVal (float) : some float value
		float2Val (float) : some float value
	Returns:
	intVal, strVal, floatVal, float2Val (tuple) : tuple of the values
	"""
	intVal = intVal
	strVal = strVal
	floatVal = floatVal
	floatVal2 = floatVal2

	# check data type, if incorrect, cast the correct data type
	if type(intVal) != int:
		intVal = int(round(float(intVal)))
	if type(strVal) != str:
		strVal = str(strVal)
	if type(floatVal) != float:
		floatVal = float(floatVal)
	if type(floatVal2) != float:
		floatVal2 = float(floatVal2)

	return intVal, strVal, floatVal, floatVal2 

if __name__ == '__main__':
	# test dataTypeCheck
	intVal = input('intVal: ')
	strVal = input('strVal: ')
	floatVal = input('floatVal: ')
	floatVal2 = input('floatVal2: ')
	print(dataTypeCheck(intVal, strVal, floatVal, floatVal2))


# 5. Create a function, called change, that takes an input, cash (a float), and determines 
# the least number of dollar bills and coins needed for change. Note that bills are: 1, 5, 10, 20, 50, and 100.
# Coins can be: 1 cent, 5 cents, 10 cents and 25 cents (penny, nickel, dime, quarter). (15 points)
# Example:
# If the dollar amount is 35.63, then your function should return the string:
# "1 x $20 bill, 1 x $10 bill, 1 x $5 bill, 2 quarters, 1 dime, 3 pennies"

def change(cash: float):
	"""
	This function takes a dollar amount as input and returns the change needed (dollar bills and coins).
	Args:
		cash (float) : dollar amount
	Returns:
	change (string) : 'x $100 bills, x $50 bills, ..., x dimes, x pennies'
	"""
	cash = cash

	# floor division of total cash to get number of x bills (or coins)
	oneHundreds = int(cash // 100)
	# update cash to cash remaining after using the bills (if cash < value of bill/coin, reamining cash will remain the same)
	cash = cash % 100

	# continue this pattern for every level of currency 

	fifties = int(cash // 50)
	cash = cash % 50

	twenties = int(cash // 20)
	cash = cash % 20

	tens = int(cash // 10)
	cash = cash % 10

	fives = int(cash // 5)
	cash = cash % 5

	ones = int(cash // 1)
	cash = cash % 1

	quarters = int(cash //.25)
	cash = cash % .25

	dimes = int(cash // .10)
	cash = cash % .10

	nickles = int(cash // .05)
	# need to round due to floating point errors in calculation with decimals 
	cash = round(cash % .05, 2)

	pennies = int(cash // .01) 

	return print(f'{oneHundreds} x $100 bill, {fifties} x $50 bills, {twenties} x $20 bills, \n {tens} x $10 bills, {fives} x $5 bills, {ones} x $1 bills \n {quarters} x quarters, {dimes} x dimes, {nickles} x nickels, {pennies} x pennies.')

if __name__ == '__main__':
	# test cash
	cash = float(input('Cash?: '))
	change(cash)

# 6. Create a function, called bottlesOfBeer, that accurately prints the “99 bottles of beer on the wall” song: 
# http://www.99-bottles-of-beer.net/lyrics.html
# Your program should account for changes in plural vs. singular nouns and should count down from 99 to 0. 
# (10 points)

def bottlesOfBeer():
	"""
	This function prints out the "99 bottles of beer on the wall" song.
	Args:
		None
	Returns:
		"99 bottles of beer on the wall" song (string)
	"""
	# count down from 99 to 0 and create conditions that address the plural vs singular nouns
	for i in range(99, -1, -1):
		if i > 2:
			print(f"{i} bottles of beer on the wall, {i} bottles of beer. \n Take one down and pass it around, {i-1} bottles of beer on the wall.")
		elif i == 2:
			print(f"{i} bottles of beer on the wall, {i} bottles of beer. \n Take one down and pass it around, {i-1} bottle of beer on the wall.")
		elif i == 1:
			print(f"{i} bottle of beer on the wall, {i} bottle of beer. \n Take one down and pass it around, no more bottles of beer on the wall.")
		else:
			print('No more bottles of beer on the wall, no more bottles of beer. \n Go to the store and buy some more, 99 bottles of beer on the wall.')
	return

if __name__ == '__main__':
	# test bottlesOfBeer
	input("Print out '99 Bottles of Beer on the Wall?")
	bottlesOfBeer()

# 7. Check age and height (15 points)

def checkAgeHeight(age: int, height: int):
	"""
	This function takes two inputs, height and age and determines if you meet the criteria
	to safely get on the ride.
	Args:
		age (int) : age of rider
		height (int) : height of rider in inches
	"""
	# checks criteria 
	if age > 12:
		print("You're old enough to get on the ride")
		if height > 54:
			print("You can get on the ride. Enjoy")
		else:
			print("You're a bit too short, sorry")
	else:
		print("Too young")

if __name__ == "__main__":
	# test checkAgeHeight
	age = int(input('How old are you?'))
	height = int(input('How tall are you (inches)? '))
	checkAgeHeight(age, height)


# 8. Debug the following code (15 points):
def changeNumber(myNum, myType):
	"""
	This function will change a number from int to float or float to int
	Args:
		myNum (int/float): input number
		myType (int/float): the type we want to get back
	Returns:
		myNum but with correct type
	"""
	if myType == 'float':
		myNum = float(myNum)
	else:
		myNum = int(round(float(myNum)))
	
	return myNum

if __name__ == '__main__':
	# test changeNumber
	myNum = input('Enter number for data type converion: ')
	myType = input("Enter data type 'float' or 'int': ")
	print(changeNumber(myNum, myType))