"""
Input 5 words and print:
Word with highest no. vowel + vowel count
Word with 2+ vowels
Total no. vowels
"""

words = []
vowels = "aeiouAEIOU"

for i in range(5):
    a = input("Enter word {}: ".format(i+1))
    words.append(a)

vowellist = []
pos = 0 
highest = 0
highest_word = ""
two = []
total = 0

for v in words:
    count = 0
    for j in v:
        if j in vowels:
            count+=1
    vowellist.append(count)

for n in vowellist:
    currentword = words[pos]
    if n > highest:
        highest_word = currentword
        highest = n
    pos += 1
    if n > 2:
        two.append(currentword)
    total += n

print("The word with the highest number of vowels is {}".format(highest_word))
print("The words with two vowels are {}".format(two))
print("The total number of vowels {}".format(total))
