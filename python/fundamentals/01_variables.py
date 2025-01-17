"""
Author: Steven Chavez
Filename: variables.py
Date: 4/16/2024
References: w3schools.com/python

Variable Naming Convention
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
  - A variable name must start with a letter or the underscore character
  - A variable name cannot start with a number
  - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
  - Variable names are case-sensitive (age, Age and AGE are three different variables)
  - A variable name cannot be any of the Python keywords.
"""

##############
### BASICS ###
##############
# Variables can change types
v = 0
v = "Python"

# Casting variables - specifies the type instead of being inferred like above
v = int(0)      # 0
v = str(0)      # "0"
v = float(0)    # 0.0

# Check the type of the variable.
print(type(v))  # will be float

# You can use single or double quotes - same thing
v = 'Python'
v = "Python"

# Variable names are case sensitive - below are two different variables
v = 0
V = "Python"

# Multiple work variable names
pythonVariable = "Python"  # Camel Case
PythonVariable = "Python"  # Pascal Case
python_variable = "Python"  # Snake Case

# Assign multiple values in one line
a, b, c = "A", "B", "C"

# Assign same value to multiple variables
a = b = c = 0

# Unpacking a collection
v = ["A", "B", "C"]
a, b, c = v
# a contains "A"
# b contains "B"
# c contains "C"

########################
### GLOBAL VARIABLES ###
########################
# Variables created outside of functions are known as global variables
v = "Python"

def printString():
  print(v)
  
printString()

# If you create a variable inside a function it can only be used in that 
# function unless you use the global keyword to add it to the global scope
def printString()
  global v
  v = "Python"

printString()

print(v)

# If you want to change a global variables value you need to use the global keyword
v = "Python"

def printString():
  global v
  v = "Python3"
  
printString()

print(v)

###############
### NUMBERS ###
###############
# There are three types of number types in Python - int, float, complex

# int - is a whole number positive or negative with no decimals of unlimited length
v = 1
v = 83478628346981237462836487
v = -329837

# float - same as int but with decimals
v = 1.0
v = -1.83782397

# floats - can be a scientific number using an "e" as shorthand for the power of 10
v = 33e5

# complex - written with "j" as the imaginary part
v = 1+1j
v = 5j

# converting types
v = 0
v = float(v) # converts int to float

# random numbers - use the random module
import random
print(random.randrange(1,100))

#############
## STRINGS ##
#############
# You can assign multiline strings by using three quotes """ or '''
v = """ This is
a multiline string
variable
"""
# strings are arrays you can access the characters of a string using []
v = "Python"
print(v[0]) # print "P"

# You can loop through characters in a string
v = "Python"
for c in v:
  print(c) # prints each char in a new line

# How to get the length of a string
v = "Python"
print(len(v)) # prints 6

# You can check the string if phrases or characters are present
v = "How are you?"
if "are" in v:
  print(v)

# You can check if a keyword is not in a string
v = "How are you?"
if "Python" not in v:
  print(v)
  
########################
### String - Slicing ###
########################
# You can return a range of char in a string using slice syntax
v = "Python"
print(v[2:4]) # prints "th"

# Slice from the start
print(v[:2]) # prints "py"

# Slice to the end
print(v[2:]) # prints "thon"

# Negative index slicing
v = "Hello, World!"
print(v[-5:-2]) # prints "orl"

#######################
### String - Modify ###
#######################
# Turn the whole string to upper case letters
v = "Python"
print(v.upper())

# Turn the whole string to lower case letters
v = "Python"
print(v.lower())

# Remove white spaces
v = " Python "
print(v.strip()) # prints "Python" not " Python "

# Replace char or phrase with another
v = "Python"
print(v.replace("Py", "Mara")) # prints "Marathon"

# Split string into a list based on a separator
v = "Python is awesome"
print(v.split(" ")) # prints ['Python', 'is', 'awesome']

##########################
### String - F-Strings ###
##########################

# F-string was introduced in 3.6, add an f in front of string and {} to add the variable to it
version = 3.6
txt = f"Python {version}"
print(txt)

