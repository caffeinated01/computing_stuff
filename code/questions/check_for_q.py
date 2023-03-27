"""
A person is invited to key in a number, one at a time forever
The program will stop inviting the person to enter any more numbers if the person enteres "q" or "Q".
Compute the sum of all the numbers that has been entered
Display the sum of all the numbers that has been entered
Display the total count of numbers entered, the sum and average
"""

q_not_entered = True
count = 0
words = []

while q_not_entered:
    num = int(input("Enter a number: ")) 
    if str(num).lower() == "q":
        q_not_entered = False
    else:
        count+=1
        words.append(num)

word_count = sum(words)
print(count)
print(word_count)
print(word_count/len(words))
