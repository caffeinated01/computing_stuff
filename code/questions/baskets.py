"""
Number of eggs produced is taken in as an input
It is known that a basket can only fit 5 eggs
Calculate the number of baskets needed to fit the eggs and print it
"""

eggs = int(input("Eggs produced by your pet chicken: "))
BASKET_CAPACITY = 5

if eggs % BASKET_CAPACITY > 0:
    basket = (eggs//BASKET_CAPACITY) + 1
else:
    basket = eggs//BASKET_CAPACITY

print(basket)
