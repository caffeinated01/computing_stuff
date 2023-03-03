"""
Create a program that asks for 10 letters as input, one at each time.
The letters will be classified as vowels or consonants. Print out the count of vowels and consonants in the format:
Vowels: x Consonants: y
"""

letters = []
vowel = "aeiouAEIOU"
vowels = 0
consonants = 0

for i in range(10):
  letter = input("Enter a letter: ")
  letters.append(letter)

for v in letters:
  if v in vowel:
    vowels += 1
  else:
    consonants += 1

print("Vowels: {}".format(vowels), end=" ")
print("Consonants: {}".format(consonants))

