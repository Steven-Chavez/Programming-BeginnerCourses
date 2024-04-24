"""
Author: Steven Chavez
Filename: 07_if-statements.py
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


##############################
### One Line If Statements ###
##############################

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


####################
### And Operator ###
####################

# The and keyword is a logical operator, and is used to combine conditional statements
x = 100
y = 50
z = 300

if x > y and z > x:
  print("Both conditions are True") # prints Both conditions are True


###################
### Or Operator ###
###################

# The or keyword is a logical operator, and is used to combine conditional statements
x = 100
y = 50
z = 300

if x == y or y < z:
  print("At least one of the conditions is True") # prints At least one of the conditions is True


####################
### Not Operator ###
####################

# The not keyword is a logical operator, and is used to reverse the result of the conditional statement
x = 100
y = 50

if not x < y:
  print("x is NOT less than y") # prints x is NOT less than y

  
#################
### Nested if ###
#################

# You can have if statements inside if statements, this is called nested if statements
x = 33

if x > 5:
  print("Above 5") # prints Above 5
  if x > 50:
    print("Above 10") # condition is not True
  else:
    print("Not above 50") # prints Not above 50

    
######################
### Pass Statement ###
######################

"""
if statements cannot be empty, but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error.

The pass statement is often used during development as a placeholder before implementing the actual functionality, allowing the code to be syntactically correct without doing anything.
"""
x = 100
y = 50

if x < y:
    pass  # Placeholder for future code
else:
    print("Condition is False") # prints Condition is False
