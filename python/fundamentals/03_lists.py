"""
Author: Steven Chavez
Filename: 03_lists.py
Date: 4/17/2024
References: w3schools.com/python

Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets:

List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Since lists are indexed, lists can have items with the same value:
"""
# Create a list
l = ["Python", "Cobra", "Viper", "Boa", "King Snake"]

# List length
print(len(l))

# Access list items
print(l[0]) # prints "Python"

# Access list items using negative indexing which means starting from the end
print(l[-1]) # prints last item in the list
print(l[-2]) # prints second to last item in the list

# Specify a range within the list
print(l[2:5]) # prints ['Viper', 'Boa', 'King Snake']

# Similar to slicing you can leave either side empty to start from the beginning or end
print(l[:2]) # prints ['Python', 'Cobra']



