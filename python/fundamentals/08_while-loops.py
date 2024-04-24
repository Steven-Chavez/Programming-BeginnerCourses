"""
Author: Steven Chavez
Filename: 08_while-loops.py
Date: 4/17/2024
References: w3schools.com/python

Python has two primitive loop commands:

- while loops
- for loops
"""

###################
### While Loops ###
###################

# With the while loop we can execute a set of statements as long as a condition is true
i = 1
while i < 3:
  print(i)
  i += 1 # prints 1 and 2 on new lines

# With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 10:
  print(i) # prints 1 through 5 because loop breaks once i == 5
  if i == 5:
    break
  i += 1 

# With the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 10:
  i += 1 
  if i == 5:
    continue
  print(i) # prints 1-10 except 5 because the loop continues to six once it reaches 5

# With the else statement we can run a block of code once when the condition no longer is true
i = 0
while i < 5:
  print(i) # prints 0-4
  i += 1 
else:
  print("i is no longer less than 5") # prints i is no longer less than 5 once i reaches 5

