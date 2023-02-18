# Methods to change/manipulate the items/elements within a list.

example = ["hello"]

# Adding items
#You can use .append(), which adds the item to the end of the list.
example.append("world")
print(example)

# You can also use insert() to specify where to add the item.
example.insert(1, "beautiful")
print(example)

# You can also add lists onto lists with .extend(), which causes the items in the second list (the one in the argument/brackets) to be added onto the end of the first list
example1 = ["world"]
example.extend(example1)
print(example)

# Removing items
# You can use .remove(), which deletes the first/earliest item which matches your item.
example.remove("world")
print(example)

# You can use .pop() to delete an item at the specified index.
example.pop(1)
print(example)
