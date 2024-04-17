"""
Author: Steven Chavez
Filename: operators.py
Date: 4/17/2024
References: w3schools.com/python

Operators are used to perform operations on variables and values.

Python divides the operators into the following groups:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators
"""

############################
### Arithmetic Operators ###
############################
# + - addition
v = 1 + 1

# - - substration
V = 1 - 1

# * - multiplication
v = 1 * 1

# / - division
v = 1 / 1

# % - modulus
v = 10 % 2

# ** - exponentiation
v = 4 ** 2

# // - floor division
v = 4 // 2

############################
### Assignment Operators ###
############################

# = - assignment 
v = 0

# += - add to variable
v += 1 # increments v by 1

# -= - subtract from variable
v -= 1 # subtracts 1 from v

# *= - multiplies variable by number
v *= 5 # times v by 5

# /= - divides variable by number
v /= 2 # divides v by 2

# %= - modulus variable by number
v %= 2 # mods v by 2

# **= - raises variable to the power of a number
v **= 2 # v is raised to the power of 2

############################
### Comparison Operators ###
############################

# == - Same as or equals too
print(v == w) # checks to see if the two variables are the same or not

# != - Not the same or not equal
print(v != w) # checks if variables are not the same

# > - Greater than
print(v > w) # checks to see if v is greater than w

# < - Less than
print(v < w) # checks to see if v is less than w

# >= - Greater than or equal to 
print(v >= w) # checks if v is greater than or equal to w

# <= - Less than or equal to
print(v <= w) # checks if v is less than or equal to w

#########################
### Logical Operators ###
#########################

# and - Returns true if both statements are true
print(1 > 0 and 0 < 1) # returns True

# or - Returns true if one of the statements is true
print(1 < 0 or 0 == 0) # returns True

# not - returns false if the result is true
print(not(1 < 0 or 0 == 0)) # returns false

##########################
### Identity Operators ###
##########################

# is - used to test whether two variables refer to the same object in memory
x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)  # Output: False

x = [1, 2, 3]
y = x

print(x is y)  # Output: True

# is not - used to test whether two variables do not refer to the same object in memory
x = [1, 2, 3]
y = [1, 2, 3]

print(x is not y)  # Output: True

x = [1, 2, 3]
y = x

print(x is not y)  # Output: False

############################
### Membership Operators ###
############################

# in - checks to see if data is in another set of data
v = "P"
w = "Python"
print(v in w) # equals True

# not in - checks to see if data is not in another set of data
v = "P"
w = "Python"
print(v not in w) # equals False








