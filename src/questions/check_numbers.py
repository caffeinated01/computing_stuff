"""
In a list of numbers from 1 to 100, print out numbers that are:
- between 30 and 80 inclusive
- divisible by 3 and 5
print out the index of the number as well
"""
numlist = list(range(1, 100 + 1))

for index, number in enumerate(numlist):
    if 30 <= number and number <= 80 and number % 3 == 0 and number % 5 == 0:
        print(index + 1, number)
