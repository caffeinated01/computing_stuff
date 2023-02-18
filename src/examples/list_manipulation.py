# Methods to change/manipulate the items/elements within a list.

example = ["hello"]

# Adding items
#You can use .append(), which adds the item to the end of the list.
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
example3 = ["hello","world"]
example3.insert(1, "beautiful")
print(example3)

# You can also add lists onto lists with .extend(), which causes the items in the second list (the one in the argument/brackets) to be added onto the end of the first list
example4 = ["hello"]
word = ["beautiful","world"]
example4.extend(word)
print(example4)

# Removing items
# You can use .remove(), which deletes the first/earliest item which matches your item.
example5 = ["hello","world","world"]
example5.remove("world")
print(example5)

# You can use .pop() to delete an item at the specified index.
example6 = ["hello","hello","world"]
example6.pop(1)
print(example6)
