"""
Take in a string as an input
Spell the word with a for loop
"""

string = input("enter string: ")
output = ""

for char in string:
    output += char
    print(output)

