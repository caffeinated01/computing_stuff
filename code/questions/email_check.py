"""
You and your team are organising an event for three schools; Xinmin, Bowen, and Hougang
Each school is only allowed to have three students to participate.
Write a program that takes in emails of students and organises them into lists for their repsective schools
Check if there are available slots for the activity and terminate the program when it is full 
"""

import re

xmslist,bowlist,houlist = [],[],[]

while (len(xmslist)+len(bowlist)+len(houlist)) < 9  :
    email = input("Enter email address: ")
    if (re.fullmatch(".+@xinminss.edu.sg",email)) and (email.count("@")==1):
        if len(xmslist) < 3:
            xmslist.append(email)
            print(xmslist)
    elif (re.fullmatch(".+@bowen.edu.sg",email)) and (email.count("@")==1):
        if len(bowlist) < 3:
            bowlist.append(email)
    elif (re.fullmatch(".+@hougang.edu.sg",email)) and (email.count("@")==1):
        if len(houlist) < 3:
            houlist.append(email)
    else:
        print("Invalid email, re-enter NOW !!!")
        continue

print(f"Shortlisted students:\n{xmslist}\n{bowlist}\n{houlist}")