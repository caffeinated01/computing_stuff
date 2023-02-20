list = list(range(30, 55+1))

for index, number in enumerate(list):
    if number % 7 == 0:
        print(index, number)