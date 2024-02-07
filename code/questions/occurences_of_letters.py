"""
Ask user to enter 2 letters, x and y
x cannot be equals to y

Ask user to enter a sentence
Return the following:
    - Number of vowels in the sentence
    - Number of occurences of letter x
    - Number of occurences of letter y
    - The indexes at which these x and y values are at
"""

from collections import defaultdict

while True:
    x = input("Enter letter (x): ")
    y = input("Enter letter (y): ")
    
    if (len(x) == 1 or len(y) == 1) and (x.isalpha() and y.isalpha()) and not(x == y):
        print("\n")
        print("Valid input!\n")
        break
    print("\n")
    print("Bad input!\n")

sentence = input("Enter sentence (z): ").lower()

index_map = defaultdict(list)
v_count = 0

for idx,val in enumerate(sentence):
    if val == x:
        index_map[x].append(idx)
    elif val == y:
        index_map[y].append(idx)
    if val in "aeiou":
        v_count += 1

x_count = len(index_map[x])
y_count = len(index_map[y])

x_idxs = index_map[x]
y_idxs = index_map[y]

print("\n")
print("Occurences of (vowels): {}".format(v_count))
print("Occurences of (x): {}\nOccurences of (y): {}".format(x_count,y_count))

print("\nIndexes of (x): {}\nIndexes of (y): {}".format(x_idxs,y_idxs))
