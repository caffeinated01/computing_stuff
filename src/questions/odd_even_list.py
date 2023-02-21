"""
Create a program that has a list of numbers from 101 to 200 inclusive 
For every odd number, minus 3 from it
For every even number, add 2 to it
Print out the new list

Add up all the numbers with the odd indexed positions
Print out the sum

Add up all the numbers with the even indexed positions and the numbers must be divisble by 3 or 7
Print out the sum
"""

numlist = list(range(101,201))
new = []
odd = 0
even = 0

for i in numlist:
  if (i-1)%2 == 0:
    i -= 3
    new.append(i)
  elif i%2 == 0:
    i += 2
    new.append(i)
  else:
    new.append(i)

print("New list: {}".format(new))

for a,v in enumerate(new):
  if (a-1)%2 == 0:
    odd += v
  if a%2 == 0and (v%3 ==0 or v%7 ==0):
    even += v

print("Odd sum: {}".format(odd))
print("Even sum: {}".format(even))
