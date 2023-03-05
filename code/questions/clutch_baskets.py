"""
There are five clutches of eggs
We want to fit those eggs into baskets, each of a capacity of 10 eggs
Create a program that asks for the number of eggs in each clutch, and calculate the number of baskets needed to fit the eggs
"""

eggs = 0
for i in range(5):
  egg = int(input("Number of eggs: "))
  eggs += egg

BASKET_CAPACITY = 10

if eggs % BASKET_CAPACITY > 0:
  basket = (eggs // BASKET_CAPACITY) + 1
else:
  basket = eggs // BASKET_CAPACITY

print(basket)

