"""
Create a list of numbers from 30-55
Print out the numbers that are divisible by 7 with their respective positions in the list
"""

list = list(range(30, 55+1))

for index, number in enumerate(list):
    if number % 7 == 0:
        print(index + 1, number)
