"""
Generate a number list through the range function with a and b keyed in as arguments. 
Print out all the numbers, one at a time, except for those that satisfy the following criteria:
i) Greater than 20
ii) Odd number
iii) divisible by 3 or 5
(either of these criteria must be met)
"""
a = 10
b = 200
list = list(range(a,b))
new = []

for i in list:
  if i > 20:
    pass
  elif i%2 == 1:
    pass
  elif i%3 == 0 or i%5 == 0:
    pass
else:
    new.append(i)

for a in new:
  print(a)
