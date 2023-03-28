"""
A person is invited to key in a number, one at a time forever
The program will stop inviting the person to enter any more numbers if the person enteres "q" or "Q".
Compute the sum of all the numbers that has been entered
Display the sum of all the numbers that has been entered
Display the total count of numbers entered, the sum and average
"""
q_not_entered = True
listnum = []

while q_not_entered:
    number = input("Enter a number: ")
    if number.lower() != 'q':
        listnum.append(int(number))
    else:
        q_not_entered = False

sumlist = sum(listnum)
avg = sumlist/len(listnum)

print("Count is {}, Average is {}, and Sum is {}".format(len(listnum),avg,sumlist))