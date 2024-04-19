"""
Author: Steven Chavez
Filename: 03_lists.py
Date: 4/17/2024
References: w3schools.com/python

Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.

Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Set items are unchangeable, meaning that we cannot change the items after the set has been created.
"""

###################
### Python Sets ###
###################

# Sets are written with curly brackets.
s = {"Tomatoes", "Peppers", "Kale"}
print(s) # prints {'Kale', 'Tomatoes', 'Peppers'}

# Sets cannot have two items with the same value. Duplicate values will be ignored
s = {"Tomatoes", "Peppers", "Kale", "Kale"}
print(s) # prints {'Kale', 'Tomatoes', 'Peppers'}

# True and 1 are considered the same value. Same with False and 0.
s = {"Tomatoes", "Peppers", "Kale", True, 1, 2}
print(s) # prints {True, 2, 'Kale', 'Tomatoes', 'Peppers'}

# Set items can be any data type and contain different data types
s = {"Tomatoes", "Peppers", "Kale", True, 1, 2}

# Sets are defined as the data type set
print(type(s)) # prints <class 'set'>




