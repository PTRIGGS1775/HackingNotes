#!/bin/python3

#Print String
print('##String Section')
print("Hello, world!")
print("""This string
      runs multiple lines!""") #Triple quotes for lines
print("This string" + "Concatenates lines") #Concatenating
print('\n') #Prints new line
print('Test new line out')



#Math
print('\n')
print('##Math Section')
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 / 6) #division with decimals
print(50 // 6) #no remainder

#Variables
print('\n')
print('##Vairables Section')
quote = "Honor is dead, but I'll see what I can do."
print(quote)
print(quote.upper()) #.METHOD demonstrated here.
print(quote.lower())
print(quote.title())

print(len(quote)) #Total count of all characters in the quote.

name = "Paul" #string
age = 32 #int
gpa = 4.0 #float

print(int(gpa))
print(int(30.9)) #Only prints the number on the left of the decimal and doesn't round.
print("Hello, my name is " + name + " and my age is " + str(age))

age += 1
print(age)
age += int(gpa)

#Functions
print('\n')
print('##Functions Section')
def who_am_i():  #This is a function without parameters.
    name = "Paul"  #local variable within function
    age = 32
    print("Hello, my name is " + name + " and my age is " + str(age))

who_am_i() #Calls function

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100) #Prints 200 because its doing math within the function.

def multiply(x,y):
    print(x * y)

multiply(8,8)

def subtract(x,y):
    return x - y #This stores the value in the function when called but doesn't do anything with it.

iamsubtractor = subtract(4,3)
print(iamsubtractor) #an unnecessary step but worth seeing how you can store functions in variables.

def square_root(x):
    print(x ** .5)

square_root(64)

def nl(): #faster way going forward to print new lines.
    print('\n')

#Boolean Expressions
nl()
print('##Boolean Expressions Section') 










