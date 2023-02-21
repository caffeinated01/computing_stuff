# Examples of string manipulation
# Slicing
string = "hello beautiful world"
# Use square brackets to slice. The number infront of the collon is where the slicing starts, the number after is where it ends
print(string[:5]+" "+string[-5:])  # Returns hello world

# To reverse a string, use [::-1]
print(string[::-1])  # Returns dlrow lufituaeb olleh

# To specify an interval, add another collon behind with the interval
print(string[::2])  # Returns hlobatflwrd
