"""
Taken from https://codingbat.com/python
Given a non-negative number "num", return True if num is within 2 of a multiple of 10
"""

def near_ten(num):
    remainder = num % 10
    return remainder in (0, 1, 2, 8, 9) # Remainder should be 0, 1, 2, 8 or 9 if it is 2 within a multiple of 10

print(near_ten(12)) # True
print(near_ten(156)) # False