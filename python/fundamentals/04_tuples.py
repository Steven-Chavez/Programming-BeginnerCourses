
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

# Tuples can be any data type or contain different data types in the same Tuple
t = ("Goku", 3000, True)
print(t) # print ('Goku', 3000, True)

# Tuples are defined objects with the data type of tuple
print(type(t)) # prints <class 'tuple'>


#####################
### Access Tuples ###
#####################
# You can access tuples the same way you access lists
# - Index in side square brackets t[1]
# - Negative indexing [-1]
# - Range of indexes [2:4]
# - Range of negative indexes [-4:-1]
# - Check if item exists using in


#####################
### Update Tuples ###
#####################

# Tuples are unchangeable but there is a workaround. Change the tuple into a list and back into a tuple
t = ("Goku", "Gohan", "Vegeta")
l = list(t)
l.append("Piccolo")
t = tuple(l)
print(t) # prints ('Goku', 'Gohan', 'Vegeta', 'Piccolo')

# You can add Tuples to Tuples
t = ("Goku", "Gohan", "Vegeta")
t2 = ("Piccolo",)
t += t2
print(t) # prints ('Goku', 'Gohan', 'Vegeta', 'Piccolo')

# To remove items from a tuple you have to use the same method to add to a tuple
t = ("Goku", "Gohan", "Vegeta")
l = list(t)
l.remove("Gohan")
t = tuple(l)
print(t) # prints ('Goku', 'Vegeta')

# You can use del to delete the tuple completely
del t
print(t) # prints error

########################
### Unpacking Tuples ###
########################

# Packing a tuple
t = ("Goku", "Gohan", "Vegeta")

# You extract values back to variables - called unpacking
(dbz1, dbz2, dbz3) = t
print(dbz1) # prints Goku
print(dbz2) # prints Gohan
print(dbz3) # prints Vegeta

# If the number of variables is less than the number of values, you can add an * 
# to the variable name and the values will be assigned to the variable as a list:
t = ("Goku", "Gohan", "Vegeta")
(dbz1, *dbz2) = t
print(dbz1) # prints Goku
print(dbz2) # prints ['Gohan', 'Vegeta']


###################
### Loop Tuples ###
###################

# You can loop through Tuples the same you loop through lists
# - for loop
# - while loop
# - loop through index for i in range(len(t)):


###################
### Join Tuples ###
###################

# You can use the + operator to join two or more Tuples
t1 = ("Goku", "Gohan")
t2 = ("Piccolo", "Vegeta")

t3 = t1 + t2
print(t3) # prints ('Goku', 'Gohan', 'Piccolo', 'Vegeta')

# You can multiply the contents of Tuples
t = ("Goku", "Gohan")
t = t * 4
print(t) # prints ('Goku', 'Gohan', 'Goku', 'Gohan', 'Goku', 'Gohan', 'Goku', 'Gohan')


#####################
### Tuple Methods ###
#####################

"""
Python has two built-in methods that you can use on tuples.

count() - Returns the number of times a specified value occurs in a tuple
index()	- Searches the tuple for a specified value and returns the position of where it was found
"""














