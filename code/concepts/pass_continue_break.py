# Pass
# Pass means "There is no code to run here" and it will continue through the remainder of the loop body

list1 = list(range(1,15))

for i in list1:
    if i%3:
        pass
    else:
        print(i)

# Continue
# Continue forces the loop to start at the next iteration

list2 = list(range(1,20))

for j in list2:
    if j%3:
        continue
    if j%5:
        continue
    else:
        print(j)

# Break
# Breaks out of the loop

list3 = list(range(1,6))

for a in list3:
    if a == 6:
        break
    else:
        print(a)
