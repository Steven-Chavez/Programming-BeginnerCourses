"""
Author: Steven Chavez
Filename: 03_lists.py
Date: 4/17/2024
References: w3schools.com/python

Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values:
"""

###########################
### Python Dictionaries ###
###########################

# Create and print a dictionary
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
print(d) # prints {'brand': 'Cold Steel', 'model': 'SRK', 'type': 'knife'}

# Print the "brand" value of the dictionary:
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
print(d["brand"]) # prints Cold Steel

# Dictionaries cannot have two items with the same key
# Duplicate values will overwrite existing values
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife",
  "type": "knife"
}
print(d) # print {'brand': 'Cold Steel', 'model': 'SRK', 'type': 'knife'}


####################
### Access Items ###
####################

# Get the value of the "model" key:
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
i = d["model"]
print(i) # prints SRK

# There is also a method called get() that will give you the same result
i = d.get("brand")
print(i) # prints Cold Steel

# The keys() method will return a list of all the keys in the dictionary.
i = d.keys()
print(i) # prints dict_keys(['brand', 'model', 'type'])

# Add a new item to the original dictionary, and see that the keys list gets updated as well
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}

i = d.keys()
print(i) # prints dict_keys(['brand', 'model', 'type'])

d["color"] = "black"
print(i) # prints dict_keys(['brand', 'model', 'type', 'color'])

# The values() method will return a list of all the values in the dictionary.
i = d.values()
print(i) # prints dict_values(['Cold Steel', 'SRK', 'knife', 'black'])

# The items() method will return each item in a dictionary, as tuples in a list.
i = d.items()
print(i) # prints dict_items([('brand', 'Cold Steel'), ('model', 'SRK'), ('type', 'knife'), ('color', 'black')])

# To determine if a specified key is present in a dictionary use the in keyword:
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}

if "model" in d:
  print("Yes, 'model' is a key in the dictionary") # prints Yes, 'model' is a key in the dictionary


####################
### Change Items ###
####################

# You can change the value of a specific item by referring to its key name
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
d["model"] = "AD-15 Lite"
print(d) # prints {'brand': 'Cold Steel', 'model': 'AD-15 Lite', 'type': 'knife'}

# The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
d.update({"model": "AD-15 Lite"})
print(d) # prints {'brand': 'Cold Steel', 'model': 'AD-15 Lite', 'type': 'knife'}


#################
### Add items ###
#################

# Adding an item to the dictionary is done by using a new index key and assigning a value to it
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
d["color"] = "Black/Stainless"
print(d) # prints {'brand': 'Cold Steel', 'model': 'SRK', 'type': 'knife', 'color': 'Black/Stainless'}

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
d.update({"color": "Black/Stainless"})
print(d) # prints {'brand': 'Cold Steel', 'model': 'SRK', 'type': 'knife', 'color': 'Black/Stainless'}


####################
### Remove Items ###
####################

# The pop() method removes the item with the specified key name
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
d.pop("model")
print(d) # prints {'brand': 'Cold Steel', 'type': 'knife'}

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
d.popitem()
print(d) # prints {'brand': 'Cold Steel', 'model': 'SRK'}

# The del keyword removes the item with the specified key name
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
del d["type"]
print(d) # prints {'brand': 'Cold Steel', 'model': 'SRK'}

# The clear() method empties the dictionary
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
d.clear()
print(d) # prints {}


#########################
### Loop Dictionaries ###
#########################

# Print all key names in the dictionary, one by one
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
for i in d:
  print(i) # prints each key on a new line

# Print all values in the dictionary, one by one
for i in d:
  print(d[i]) # prints each value on a new line

# You can also use the values() method to return values of a dictionary:
for i in d.values():
  print(i) # prints each value on a new line

# You can use the keys() method to return the keys of a dictionary
for i in d.keys():
  print(i) # prints each key on a new line

# Loop through both keys and values, by using the items() method:
for k, v in d.items():
  print(k, v) # prints each key/value pair on a new line


#########################
### Copy Dictionaries ###
#########################

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a 
# reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# Make a copy of a dictionary with the copy() method:
d = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
c = d.copy()
print(c) # print {'brand': 'Cold Steel', 'model': 'SRK', 'type': 'knife'}

# Make a copy of a dictionary with the dict() function
c = dict(d)
print(c)  # print {'brand': 'Cold Steel', 'model': 'SRK', 'type': 'knife'}


###########################
### Nested Dictionaries ###
###########################
# A dictionary can contain dictionaries, this is called nested dictionaries.

# Create a dictionary that contain three dictionaries:
nd = {
  "item1": {
    "brand": "Cold Steel",
    "model": "SRK",
    "type": "knife"
  },
  "item2": {
    "brand": "Cold Steel",
    "model": "AD-15 Lite",
    "type": "knife"
  },
  "item3": {
    "brand": "Cold Steel",
    "model": "Demko Hawk",
    "type": "Hatchet"
  }
}
print(nd) # prints {'item1': {'brand': 'Cold Steel', 'model': 'SRK', 'type': 'knife'}, 'item2': {'brand': 'Cold Steel', 'model': 'AD-15 Lite', 'type': 'knife'}, 'item3': {'brand': 'Cold Steel', 'model': 'Demko Hawk', 'type': 'Hatchet'}}

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
item1 = {
  "brand": "Cold Steel",
  "model": "SRK",
  "type": "knife"
}
item2 = {
  "brand": "Cold Steel",
  "model": "AD-15 Lite",
  "type": "knife"
} 
item3 = {
  "brand": "Cold Steel",
  "model": "Demko Hawk",
  "type": "Hatchet"
}
nd = {
  "item1": item1,
  "item2": item2,
  "item3": item3
}
print(nd) # prints {'item1': {'brand': 'Cold Steel', 'model': 'SRK', 'type': 'knife'}, 'item2': {'brand': 'Cold Steel', 'model': 'AD-15 Lite', 'type': 'knife'}, 'item3': {'brand': 'Cold Steel', 'model': 'Demko Hawk', 'type': 'Hatchet'}}

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary
print(nd["item3"]["model"]) # prints Demko Hawk





































