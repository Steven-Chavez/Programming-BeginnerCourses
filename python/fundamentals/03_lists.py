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
print(l[4:]) # prints ['King Snake']
print(l[-4:-1]) # you can also use negative indexing

# Check if item exists in list
if "Boa" in l:
  print("Yes")

###########################
### Change item in list ###
###########################

# Change the 3rd item using the index
l[2] = "Corn Snake"
print(l) # prints ['Python', 'Cobra', 'Corn Snake', 'Boa', 'King Snake']

# Change a range of item values
l[1:3] = ["Corn Snake", "Cobra"]
print(l) # prints ['Python', 'Corn Snake', 'Cobra', 'Boa', 'King Snake']

# If you add more items than you replace the items will be added in that place and the rest will be moved
l[1:2] = ["Corn Snake", "Viper"]
print(l) # prints ['Python', 'Corn Snake', 'Viper', 'Cobra', 'Boa', 'King Snake']

# You can insert items without replacing existing values by using insert()
l.insert(4, "Anaconda") # adds item in the 5 index
print(l) # prints ['Python', 'Corn Snake', 'Viper', 'Cobra', 'Anaconda', 'Boa', 'King Snake']

#########################
### Add items to list ###
#########################

# append items to list using append()
l.append("Hognose Snake") 
print(l) # prints ['Python', 'Corn Snake', 'Viper', 'Cobra', 'Anaconda', 'Boa', 'King Snake', 'Hognose Snake']

# append list to list using extend()
v = ["Rattle Snake", "Black Mamba"]
l.extend(v)
print(l) # prints ['Python', 'Corn Snake', 'Viper', 'Cobra', 'Anaconda', 'Boa', 'King Snake', 'Hognose Snake', 'Rattle Snake', 'Black Mamba']

# You can use extend to add other iterable objects like tuples, sets, dictionaries, etc.
l = ["Python", "Cobra", "Viper", "Boa", "King Snake"]
t = ("Bull Snake", "Gopher Snake") # tuple
l.extend(t)
print(l) # prints ['Python', 'Cobra', 'Viper', 'Boa', 'King Snake', 'Bull Snake', 'Gopher Snake']

##############################
### Remove items from list ###
##############################

# Use remove() to remove items from the list. If there are duplicates the first occurrence will be removed
l.remove("Cobra")
print(l) # prints ['Python', 'Viper', 'Boa', 'King Snake', 'Bull Snake', 'Gopher Snake']

# Use pop() to remove a specific index from the list
l.pop(2)
print(l) # prints ['Python', 'Viper', 'King Snake', 'Bull Snake', 'Gopher Snake']

# If you don't provide an index for pop() the last item is removed
l.pop()
print(l) # prints ['Python', 'Viper', 'King Snake', 'Bull Snake']

# del keyword can also be used to remove a specified index
del l[1]
print(l) # prints ['Python', 'King Snake', 'Bull Snake']

# The del keyword can delete an entire list
del l
print(l) # prints NameError: name 'l' is not defined

# Empty a list using clear(). list remains
l = ["Python", "Cobra", "Viper", "Boa", "King Snake"]
l.clear()
print(l) # prints []

##################
### Loop Lists ###
##################

# Loop through list using for loop
l = ["Python", "Cobra", "Viper", "Boa", "King Snake"]
for x in l:
  print(x) # prints each item on a new line

# You can loop through a list using indexes using range() and len()
for i in range(len(l)):
  print(l[i]) # prints each item on a new line

# Loop through list using a while loop
i = 0
while i < len(l):
  print(l[i]) # prints each item on a new line
  i += 1
 
# Loop through list using list comprehension
[print(x) for x in l] # prints each item on a new line

##########################
### List Comprehension ###
##########################

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Syntax: newlist = [expression for item in iterable if condition == True]
l = ["Python", "Cobra", "Viper", "Boa", "King Snake"]
n = [x for x in l if "n" in x] 
print(n) # prints ['Python', 'King Snake']

# The condition is optional
n = [x for x in l]
print(n) # prints an exact copy of l

# The expression is the current item in the iteration, but it is also the outcome, which you 
# can manipulate before it ends up like a list item in the new list:
n = [x.lower() for x in l]
print(n) # prints ['python', 'cobra', 'viper', 'boa', 'king snake']

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
n = [x if x != "Boa" else "Boa Constrictor" for x in l]
print(n) # prints ['Python', 'Cobra', 'Viper', 'Boa Constrictor', 'King Snake']

##################
### Sort Lists ###
##################

# sort lists alphanumerically
l = ["Python", "Cobra", "Viper", "Boa", "King Snake"]
l.sort()
print(l) # prints ['Boa', 'Cobra', 'King Snake', 'Python', 'Viper']

# sort descending
l.sort(reverse = True) 
print(l) # prints ['Viper', 'Python', 'King Snake', 'Cobra', 'Boa']

# By default sort() is case sensitive. Capital letters are sorted before lowercase
l = ["Python", "cobra", "viper", "Boa", "king snake"]
l.sort()
print(l) # prints ['Python', 'cobra', 'viper', 'Boa', 'king snake']

# If you want a case-insensitive sort function, use str.lower as a key function
l = ["Python", "cobra", "viper", "Boa", "king snake"]
l.sort(key = str.lower)
print(l) # prints ['Boa', 'cobra', 'king snake', 'Python', 'viper']

# You can use the reverse() method to reverse the current order of the list
l.reverse()
print(l) # prints ['viper', 'Python', 'king snake', 'cobra', 'Boa']

##################
### Copy lists ###
##################
# You cannot copy a list simply by typing list2 = list1, because: list2 will 
# only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# Copy a list using copy()
l = ["Python", "Cobra", "Viper", "Boa", "King Snake"]
c = l.copy()
print(c) # prints ['Python', 'Cobra', 'Viper', 'Boa', 'King Snake']

# You can also use the list() method to make a copy
c = list(l)
print(c) # prints ['Python', 'Cobra', 'Viper', 'Boa', 'King Snake']

##################
### Join Lists ###
##################

# Join lists using the concatenate (+) operator
l1 = ["Python", "cobra", "viper"]
l2 = ["Boa", "king snake"]
l3 = l1 + l2
print(l3) # prints ['Python', 'cobra', 'viper', 'Boa', 'king snake']

# You can also append a list to another one by one
for x in l2:
  l1.append(x)
print(l1) # prints ['Python', 'cobra', 'viper', 'Boa', 'king snake']

# you can use the extend() method, where the purpose is to add elements from one list to another list
l1 = ["Python", "cobra", "viper"]
l2 = ["Boa", "king snake"]
l1.extend(l2)
print(l1) # prints ['Python', 'cobra', 'viper', 'Boa', 'king snake']

####################
### List Methods ###
####################
"""
append() - Adds an element at the end of the list
clear() - Removes all the elements from the list
copy() - Returns a copy of the list
count() - Returns the number of elements with the specified value
extend() - Add the elements of a list (or any iterable), to the end of the current list
index() - Returns the index of the first element with the specified value
insert() - Adds an element at the specified position
pop() - Removes the element at the specified position
remove() - Removes the item with the specified value
reverse() - Reverses the order of the list
sort() - Sorts the list
"""



