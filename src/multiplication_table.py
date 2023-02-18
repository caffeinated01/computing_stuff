"""
Create a multiplication table that looks like this
1 2 3 4 5 6 --> numbers to be multiplied

2 4 6 8 10 12 --> numbers * 2

3 6 9 12 15 18 --> numbers * 3

4 8 12 16 20 24 --> numbers * 4

5 10 15 20 25 30 --> numbers * 5 

6 12 18 24 30 36 --> numbers * 6
"""

a = list(range(1, 7))
b = list(range(1, 7))
for q, i in enumerate(a):
    if q != 0:
        print("\n")
    for j in b:
        print(i * j, end=" ")
