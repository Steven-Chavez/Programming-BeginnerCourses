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


















