"""
Author: Steven Chavez
Filename: variables.py
Date: 4/16/2024

Variable Naming Convention
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
  - A variable name must start with a letter or the underscore character
  - A variable name cannot start with a number
  - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
  - Variable names are case-sensitive (age, Age and AGE are three different variables)
  - A variable name cannot be any of the Python keywords.
"""



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



