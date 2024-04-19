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


########################
### Access Set items ###
########################

# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified
# value is present in a set, by using the in keyword.
s = {"Tomatoes", "Peppers", "Kale"}
for i in s:
  print(i) # prints each item on a new line

# Check if an item is present in a set
print("Kale" in s) # prints True

# Check if an item is not present in a set
print("Kale" not in s) # prints False

# Once a set is created, you cannot change its items, but you can add new items.


#####################
### Add Set Items ###
#####################

# To add one item to a set use the add() method.
s = {"Tomatoes", "Peppers", "Kale"}
s.add("Spinach")
print(s) # prints {'Spinach', 'Kale', 'Tomatoes', 'Peppers'}

# To add items from another set into the current set, use the update() method.
s1 = {"Tomatoes", "Peppers"}
s2 = {"Spinach", "Kale"}
s1.update(s2)
print(s1) # prints {'Spinach', 'Kale', 'Tomatoes', 'Peppers'}

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
s = {"Tomatoes", "Peppers"}
l = ["Spinach", "Kale"]
s.update(l)
print(s) # prints {'Spinach', 'Kale', 'Tomatoes', 'Peppers'}


########################
### Remove Set Items ###
########################

# To remove an item in a set, use the remove(), or the discard() method.
s = {"Tomatoes", "Peppers", "Kale", "Spinach"}





