
"""
Create a program that shows me the element that has more than 1 copy
"""
num, suspect = [11, 13, 15, 17, 18, 11, 14, 12, 13, 17, 14, 16, 18, 19, 14], []
for i in num:
    a = num.count(i)
    if a > 1:
        if i not in suspect:
            suspect.append(i)
print(suspect)
