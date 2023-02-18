# Example usage of append
res = []  # creates an empty list
res.append("hi")  # adds string "hi" into list called res
print(res)  # returns ['hi']

# we can also use append in a loop
numlist = []
for i in range(5+1):
    numlist.append(i)
    i += 1
print(numlist)  # returns [0, 1, 2, 3, 4, 5]

# another example of append in a for loop
string = "hello world"
list_with_strings = []
for i in string:
    list_with_strings.append(i)
# returns ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(list_with_strings)
