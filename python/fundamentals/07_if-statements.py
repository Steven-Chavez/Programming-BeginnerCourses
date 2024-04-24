"""
Author: Steven Chavez
Filename: 03_lists.py
Date: 4/23/2024
References: w3schools.com/python

Python supports the usual logical conditions from mathematics:
- Equals: a == b
- Not Equals: a != b
- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using the if keyword.

"""

#################
### If...Else ###
#################

# If statement format
x = 0
y = 20
if x < y:
  print("x is less than y") # prints x is less than y

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition"
x = 0
y = 0
if x > y:
  print("x is greater than y") # does not print because condition is false
elif x == y:
  print("x is the same as y") # prints x is the same as y

# The else keyword catches anything which isn't caught by the preceding conditions.
x = -1
y = 0
if x > y:
  print("x is greater than y") # does not print because condition is false
elif x == y:
  print("x is the same as y") # does not print because condition is false
else:
  print("x is less than y") # prints x is less than y

# One line if statement
x = 0
y = 20
if x < y: print("x is less than y") # prints x is less than y

# One line if else statement:
x = 20
y = 0
print('x') if x < y else print('y') # prints y

# One line if else statement, with 3 conditions
x = 20
y = 40
print("x is greater than y") if x > y else print("x is the same as y") if x == y else print("x is less than y") # prints x is less than y

x = 20
y = 20
print("x is greater than y") if x > y else print("x is the same as y") if x == y else print("x is less than y") # prints x is the same as y

x = 20
y = 10
print("x is greater than y") if x > y else print("x is the same as y") if x == y else print("x is less than y") # prints x is greater than y
