"""
Ask user how many colors they want to input
Seperate the colors as different items in a list
Reject the color if it is orange or yellow
Example input:
How many colors do you want to input?
4
Colors?
white, orange, black, yellow
The program would print ['white','black']
"""

num = int(input("How many colors do you want to input?\n"))

color = str(input("Colors?\n"))

for i in range(num):
    list = color.split(", ")

for j in list:
    if j == "orange":
        list.remove(j)
    elif j == "yellow":
        list.remove(j)
    else:
        continue

print(list)
