# Examples of string manipulation
# Slicing
string = "Hello Beautiful World"
# Use square brackets to slice. The number infront of the collon is where the slicing starts, the number after is where it ends
print(string[:5]+" "+string[-5:])  # Returns Hello World

# To reverse a string, use [::-1]
print(string[::-1])  # Returns dlroW lufituaeB olleH

# To specify an interval, add another collon behind with the interval
print(string[::2])  # Returns HloBatflWrd

# Use .upper() or .lower() to make convert a string to upper or lower case
print(string.upper())  # Returns HELLO BEAUTIFUL WORLD
print(string.lower())  # Returns hello beautiful world

# To append each word in a string into a list, use .split()
print(string.split())  # Returns ['Hello', 'Beautiful', 'World']

# You can specify a parameter in the split() function
split = "Hello, Beautiful, World"
print(split.split(", "))  # Returns ['Hello', 'Beautiful', 'World']

# To remove any character from a string, use .strip()
excess = "asasasas.....,,,,,!!!!Hello World"
# Returns Hello World
print(excess.strip("as.,!"))  # Specify the characters as a parameter

# To join elements from a list into a string, use .join()
strings = ["Hello", "Beautiful", "World"]
# Returns Hello Beautiful World
print(" ".join(strings))  # Syntax: string.join(iterable)
