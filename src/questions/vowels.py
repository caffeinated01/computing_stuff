"""
tell me how many element has 2 vowels in the last 4 letters
"""

characters = ["House", "Donald", "Goofy", "Pikachu", "Netflix", "Fantasy"]
VOWEL = "aeiouAEIOU"

for word in characters:
    sliced_word = word[-4:]
    counter = 0
    for char in sliced_word:
        if char in VOWEL:
            counter += 1
    if counter == 2:
        print(word + " has 2 vowels")
    
