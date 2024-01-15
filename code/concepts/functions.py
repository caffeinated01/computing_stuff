# functions are reusable pieces of code that can be used throughout your code

# example:

# syntax:  def function_name(arguments):
# indented --> function code here
def x():
    return 1+2 # --> return keyword does not print the value stated, it just returns it to the function caller

print(x()) # --> returns 3

# arguments is a way for you to provide more information to a function
def sum_up(x, y): # x and y are arguments, when you call the sum_up function you have to provide values for x and y as they are needed for the function to run
    return x + y

print(sum_up(1,2)) # --> prints 3

# the "*" keyword
# when you are working with a variable amount of arguments, you can put the * keyword infront of your argument name and arguments supplied will be sort of stored in a list
def form_sentence(*words):
    sentence_list = [x for x in words]
    return " ".join(sentence_list)

print(form_sentence("Hello", ",", "world", "!")) # --> returns "Hello , World !"

def get_second_argument(*args):
    return args[1] # as discussed earlier, arguments with the "*" keyword infront can be treated as lists, so using index to get the second argument is possible

print(get_second_argument(1,2,3)) # --> returns 2

# variables outside of functions cannot be accessed, unless global
# variables inside of functions cannot be accessed, unless returned
counter = 5

def increase_count(multiplier):
    global counter # using the global keyword, we are accessing the variable outside of the function.
    for i in range(multiplier):
        counter += 1
    return counter

increase_count(5)
print(counter) # --> returns 10