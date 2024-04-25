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
