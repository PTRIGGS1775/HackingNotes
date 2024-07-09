#!/bin/python3

#USER INPUT
#I got a little carried away with practicing Python on this one. I'll need to return to this at some point to figure out how to break the loop I created at the bottom gracefully.
'''
name = input('What is your name? ')
age = int(input('What is your age? ')) #Even though we're converting this to a string later, we need to do math to the value so it needs to be an int when we work on it.
print('Hello ' + name + ' you will be ' + str(age + 1) + ' next year!') 
'''

def calculator():
    x = float(input("Give me a number: "))
    o = input("Give me an operator: ")
    y = float(input("Give me yet another number: "))

    if o == "+":
	    print(x + y)
    elif o == "-":
	    print(x - y)
    elif o == "/":
	    print(x / y)
    elif o == "*":
	    print(x * y)
    elif o == "**":
	    print(x ** y)
    else:
	    print("Unknown operator.")

def endings():
    endex = input('Would you like to try calculating? ')
    while True:
        if endex.lower() == "y":
            calculator()
        elif endex.lower() == "n":
            print("Goodbye!")
            return 0 #Ends the while loop
        else:
            print("You must choose either 'Y' or 'N'")
            endings() #This lets me restart the process without having to re-enter the command in CLI.

endings() #So I need to call the function first to let it run. But to get it to loop i need to wrap the question as a function and call it as well.

