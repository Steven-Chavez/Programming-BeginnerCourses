
"""
Author: Steven Chavez
Filename: 03_lists.py
Date: 4/17/2024
References: w3schools.com/python

Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection that is ordered and unchangeable.
Tuples are written with round brackets.

Tuples are ordered, which means that the items have a defined order, and that order will not change.

Tuples are unchangeable, meaning that we cannot change, add, or remove items after the tuple has been created.
"""

# Create a Tuple:
t = ("Goku", "Gohan", "Vegeta")
print(t) # prints ('Goku', 'Gohan', 'Vegeta')

# Since Tuples are index you can have items of the same value
t = ("Goku", "Gohan", "Vegeta", "Gohan")
print(t) # prints ('Goku', 'Gohan', 'Vegeta', 'Gohan')

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
t = ("Goku",)
print(t) # prints ('Goku',)
