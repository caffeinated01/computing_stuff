# Methods to change/manipulate the items/elements within a list.

example = ["hello"]

# Adding items
# You can use .append(), which adds the item to the end of the list.
example.append("world")
print(example)

# Another example of append in a for loop
string = "hello world"
example2 = []
for i in string:
    example2.append(i)
# returns ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(example2)

# You can also use insert() to specify where to add the item.
example3 = ["hello", "world"]
example3.insert(1, "beautiful")
print(example3)

# You can also add lists onto lists with .extend(), which causes the items in the second list (the one in the argument/brackets) to be added onto the end of the first list
example4 = ["hello"]
word = ["beautiful", "world"]
example4.extend(word)
print(example4)

# Removing items
# You can use .remove(), which deletes the first/earliest item which matches your item.
example5 = ["hello", "world", "world"]
example5.remove("world")
print(example5)

# You can use .pop() to delete an item at the specified index.
example6 = ["hello", "hello", "world"]
example6.pop(1)
print(example6)

# Generate a number list with list() and range()
example7 = list(range(0, 11))  # Last number not inclusive
print(example7)  # Returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# How to find average
# average = total sum/number of elements
mixed = [1, 5, 142, 41, 51, 6, 12, 91]
average = sum(mixed)/len(mixed)
print(average)

# Count method
example8 = [11, 13, 15, 17, 18, 11, 14, 12, 13, 17, 14, 16, 18, 19, 14]
print(example.count(11))  # The number of 11's in this list
