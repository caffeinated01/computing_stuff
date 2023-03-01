# Example usage of loops
# For loops
# range() function takes in three parameters: start, end, interval.
for i in range(5):
    print(i)  # returns 0 1 2 3 4

# We can use for loops to loop through iterables. Iterables include lists, strings and tuples
# Loop through list
numlist = [1, 2, 3, 4, 5]
for i in numlist:
    print(i*i)  # returns 1 4 9 16 25

# Loop through strings
string = "hello, world"
res = []
for a in string:
    res.append(a)
# returns ['h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd']
print(res)

# Loop through user input
userinput = input("Enter a special character\n")  # Example input: hello
for j in userinput:
    print(j*2)

# returns
# hh
# ee
# ll
# ll
# oo

# While loops
# While loops will run until the given condition is False

# While loops can be paried with boolean operators 
counter = 0
while counter < 10:  # Checks if variable counter is less than 10. If not, move on to the next iteration
    print(counter)
    counter += 1  # Adds on to the variable counter until it meets the condition in specified in the while loop

# In this case, the loop will run forever as the condition given is True
while True:
    print("while loops are cool!")