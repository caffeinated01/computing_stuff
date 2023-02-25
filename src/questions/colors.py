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
res = []

color = str(input("Colors?\n"))

list = color.split(", ")

if len(list) > num:
    for i in range(num,len(list)):
        list.pop(i)

for j in list:
    if j == "orange" or j == "yellow":
        list.remove(j)
    else:
        pass

print(list)
