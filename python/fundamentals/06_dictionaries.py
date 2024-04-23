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





























