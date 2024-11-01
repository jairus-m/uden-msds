# COMP 4401
# Homework 1 - Variables & Boolean Expressions

# Submit homework 1 responses in a single .py file. Responses to questions 1-4 can be included in Python script files using line comments (# comment) or multiline comments using triple quotes (‘’’comment’’’). 

# For questions 1-4 solve without using python to ensure you understand data types and boolean expression, you can then verify your answers using python.

#--------------------------------------------------------------------------#

# 1. For each of the following expression, identify the data type and value (10 points):
#A) 5+3/5*(4-10) 
    #float
    #5 + (3/5) * (4-10) = 1.4
#B) 17//3**4
    #int
    #17 // 81 = 0


# 2. Evaluate the following boolean expressions (10 points):
#A) 15 % 4 < 20/3
    #3 < 6.667
    #True
#B) False or not (False or True) and True
    #False or not True and True
    #False or False and True
    #False or False
    #False
#C) 3/4==0 or 5<6
    #3/4 == 0 or True
    #False or True
    #True


# 3. Let a = True, b = True, c = False. Evaluate the following (15 points):
#A) a and not b
    #False
#B) b or c
    #True
#C) not b == c
    #True
#D) a and not c
    #True
#E) b or c and not a
    #True
#F) a != b or b != c
    #True


# 4. Select all invalid variable names below and give reason the variable name is invalid (15 points):
#A) speed Of Light 
    #invalid as there are spaces instead of underscores
#B) x_2 
    #valid but descriptiveness will depend on the context of x_2
#C) 3Attempts 
    #invalid as it starts with a number
#D) vertical-distance 
    #invalid as there is a hyphen
#E) B5V 
    #valid HOWEVER upper case by convention is saved for classes, B5V might not be descriptive enough, and convention for variables is to use lower case if a single word


# 5. Write code that initializes a variable to store the length of a square in inches, calculates the perimeter and area of the square, and prints the results. Test the program by changing the initial value for length to different integer values (15 points).

length_of_square = int(input('Length of Square?'))
perimeter_of_square = length_of_square * 4
area_of_square = length_of_square**2

print(f'Perimeter of Square: {perimeter_of_square}')
print(f'Area of square: {area_of_square}')

# 6. Write code that will assign a variable to a given number of seconds and then calculate the equivalent number of hours, minutes and seconds. For example, 300 seconds is 0 hours, 5 minutes and 0 seconds while 4503 seconds is 1 hour, 15 minutes and 3 seconds. Assign separate variables to each of these values (i.e., hours, minutes, seconds). Evaluate your program calculations using different starting times (initial seconds). Be mindful of possible rounding errors, use integers only (15 points).

seconds_input = int(input('Number of seconds?'))
seconds = seconds_input % 60
minutes = (seconds_input // 60) 
hours = minutes // 60
print(f'{hours} hour(s), {minutes % 60} minutes, {seconds} seconds')

# 7. Debug the following code which greets a guest and checks if the guest can get on a ride by checking their age and height (10 points) :

name = "Josh"
height = 62.4
age = 15

#Greeting :
print(f'Hello, {name}')
print(f'Are they older than 12?: {age > 12}')
print(f'Are they taller than 60 inches?: {height > 60}')


# 8. Write code that checks the data types of the following variables and casts them to the proper data type if needed (10 points):

age = 32.4
avgHeight = "73.54"
numOfGuests = 47.0
flightSpeed = "423 miles/hour"
outsideTemp = 73.2

variables = [age, avgHeight, numOfGuests, flightSpeed, outsideTemp]
print('Check dtypes:')
for i,variable in enumerate(variables):
    print(f'{i}: {type(variable)}')
    
variables[1] = float(avgHeight)
variables[3] = 432
print('Re-checked: dtypes')
for i,variable in enumerate(variables):
    print(f'{i}: {type(variable)}')





































