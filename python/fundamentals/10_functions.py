"""
Author: Steven Chavez
Filename: 10_functions.py
Date: 4/24/2024
References: w3schools.com/python

A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
"""

########################
### Python Functions ###
########################

# In Python a function is defined using the def keyword
def test():
  print("Hello, World!")

test() # prints Hello, World!


#################
### Arguments ###
#################

"""
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments 
as you want, just separate them with a comma.
"""

# function with arguments example
def test_with_arguments(s):
  print(s)

test_with_arguments("Hello, World!") # prints Hello, World!


############################
### Number of Arguments ####
############################

"""
By default, a function must be called with the correct number of arguments. Meaning that if your function 
expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
"""

# This function expects 2 arguments and gets 2 arguments
def test_two_arguments(x, y):
  print(x + y)

test_two_arguments(10, 20) # prints 30

# If you try to call the function with 1 or 3 arguments, you will get an error
def test_two_arguments(x, y):
  print(x + y)

test_two_arguments(10) # prints error


###########################
### Arbitrary Arguments ###
###########################

"""
If you do not know how many arguments that will be passed into your function, add a * before the 
parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly
"""

#If the number of arguments is unknown, add a * before the parameter name
def arbitrary_arguments(*n):
  add = 0
  for i in n:
    add += i
  print(add)

arbitrary_arguments(10, 20, 30, 40) # prints 100


#########################
### Keyword Arguments ###
#########################


