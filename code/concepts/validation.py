# isdigit()
# used to check for digits in strings.
digit = input("Enter a number: ")

if digit.isdigit():
    print("All digits")
else:
    print("Not digits")

# isalpha() 
# used to check a string is made of letters
alpha = input("Enter a string: ")

if alpha.isalpha():
    print("All letters")
else:
    print("Not letters")

# isalnum
# used to check for letters and numbers ONLY

alnum = input("Enter a string of letters and numbers: ")

if alnum.isalnum():
    print("All digits and letters")
else:
    print("Not digits and letters")