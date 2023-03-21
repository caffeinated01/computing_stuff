# Question 4
"""
Write a program that requires someone to enter three words, one at each time. 
The word will be checked with the number of vowels in there.
If number of vowels is equal or more than 2, the word will be pre-fixed with "Big" at the front of the word.
Otherwise it will be pre-fixed with "Small", print out the transformed words in a list format 
"""

from math import pi
words = []
vowels = "aeiouAEIOU"
new = []

for i in range(3):
    userinput = input("Enter a word: ")
    words.append(userinput)

for a in words:
    counter = 0
    for j in a:
        if j in vowels:
            counter += 1
    if counter >= 2:
        new.append("Big {}".format(a))
    else:
        new.append("Small {}".format(a))

print(new)

# Question 5
"""
Write a program that allows the volume of the sphere or right circular cone to be calculated. Allows the person to enter for the type of volume to be calculated - either C (cone) or S (sphere).

Your prgoram will ask for either i) r only (for sphere) ii) r and h (for cone) and compute V - the volume. Use pi from the math module.
The volume displayed should be in 2 decimal places
The printout must follow the format exactly for sphere or cone
>> "Cone volume is V cm3 with radius of r cm and height of h cm"
OR
>> "Sphere volume is V cm3 with radius of r cm"
"""


tvol = input("Calculate what type of volume? (C/S)")
if tvol.lower() == "c":
    cradius = float(input("Enter radius: "))
    cheight = float(input("Enter height: "))
    cvol = round((pi*(cradius**2)*(cheight/3)), 2)
    print("Cone volume is {}cm3 with radius of {}cm and height of {}cm".format(
        cvol, cradius, cheight))
if tvol.lower() == "s":
    sradius = float(input("Enter radius: "))
    svol = round((4/3)*pi*(sradius**3), 2)
    print("SPhere volume is {}cm3 with radius of {}cm".format(svol, sradius))
