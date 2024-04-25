"""
Author: Steven Chavez
Filename: 08_while-loops.py
Date: 4/17/2024
References: w3schools.com/python

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

#################
### For Loops ###
#################

# Basic for loop
l = ["C++", "Python", "C#"]
for i in l:
  print(i) # prints each item on a new line

# Even strings are iterable objects, they contain a sequence of characters
s = "Who's going to carry the boats!!!"
for c in s:
  print(c) # prints each character on a new line


#######################
### Break Statement ###
#######################

# With the break statement we can stop the loop before it has looped through all the items
for i in l:
  print(i)
  if i == "Python":
    break # because of the break the loop only prints C++ and Python on a new line

# Exit the loop when x is "banana", but this time the break comes before the print
l = ["C++", "Python", "C#"]
for i in l:
  if i == "Python":
    break
  print(i) # prints only C++


##########################
### Continue Statement ###
##########################

# With the continue statement we can stop the current iteration of the loop, and continue with the next
l = ["C++", "Python", "C#"]
for i in l:
  if i == "Python":
    continue
  print(i) # prints everything but Python


########################
### range() Function ###
########################

"""
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments 
by 1 (by default), and ends at a specified number.
"""

# Using the range() function
for i in range(10):
  print(i) # prints 0-9 on new lines

"""
The range() function defaults to 0 as a starting value, however, it is possible to specify 
the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)
"""
# Using the start parameter
for i in range(5, 10):
  print(i) # prints 5-9 on new lines

"""
The range() function defaults to increment the sequence by 1, however, it is possible to specify the 
increment value by adding a third parameter: range(2, 30, 3)
"""
# Increment the sequence with 2 (default is 1)
for i in range(10, 20, 2):
  print(i) # prints 10, 12, 14, 16, and  18 on new lines













