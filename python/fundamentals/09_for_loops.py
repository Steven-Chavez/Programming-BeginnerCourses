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

# With the break statement we can stop the loop before it has looped through all the items
