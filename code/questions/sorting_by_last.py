"""
Enter words seperated by dash,
Sort in alphabetical order by the last letter
"""

words = input("WORDS\n")
words = words.split("-")
words.sort(key=lambda x: x[-1])
words = " ".join(words)
print(words)
