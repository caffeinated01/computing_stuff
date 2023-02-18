# Examples of booleans

# Booleans represent 2 states, either off or on.
example1 = True
example2 = False

# You can create these booleans using evaulations, which creates the booleans based on the inputs you give.

# == means equal.
print("apple" == "apple") # True
print("apple" == "orange") # False

# != means NOT equal.
print("apple" != "orange") # True
print("apple" != "apple") # False

# > means greater than.
print(5 > 3) # True
print(3 > 5) # False
print(5 > 5) # False

# >= means equal or greater than.
print(5 >= 5) # True
print(6 >= 5) # True

# < means lesser than.
print(3 < 5) # True
print(5 < 3) # False
print(5 < 5) # False

# <= means equal or lesser than.
print(5 <= 5) # True
print(4 <= 5) # True



# You can reverse a boolean using not().
print(not(True)) # False

# You can use "and" to give True when both its inputs are True.
print(True and True) # True
print(True and False) # False
print(False and False) # False
print(1 == 1 and 3 > 2) # True
print(2 != 1 and not(3 <= 3)) # False

# You can use "or" to give True when either input is True.
print(True or False) # True
print(True or True) # True
print(False or False) # False
print(1 != 1 or 1 == 1) # True

# You can combine both "or" and "and" together.
# It's better to bracket the evaluations to make it more readable.
print(3 == 4 or (5 < 6 and 6 > 5)) # True
print(3 == 4 or 5 < 6 and 6 > 5) # Is also True, but a bit harder to understand.
