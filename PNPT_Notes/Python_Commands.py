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
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()

#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >=7
less_than_equal_to = 7 <= 7

test_and = True and True #True
test_and2 = True and False #False
test_or = True or True #True
test_or2 = True or False #True

test_not = not True #False:

#Conditional Statements
nl()
print('##Conditional Statements Section') 

def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"

print(drink(3))
print(drink(1))


def alcohol(age,money):
	if(age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too poor and too young!"
		
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

#Lists
nl()
print('##Lists Section')

movies = ['John Wick','LOTR','Revolver','Horrible Bosses']
print(movies[1]) #Returns the second item in the list because the index starts at 0
print(movies[0:2]) #Not inclusive and will only print 2 items.
print(movies[1:]) #Prints everything from the second value on.
print(movies[:2]) #Prints the values from before the 3rd value not including the 3rd value.
print(movies[-1]) #Prints the last item.

print('length')
print(len(movies))
nl()
print('append method:')
movies.append('Constantine')
print(movies)
nl()
print('insert method:')
movies.insert(2,'Tenacious D')
print(movies)
nl()
print('pop method:')
movies.pop() #Removes the last item, constantine. Putting an index value in here will modify which item gets removed.
print(movies)

print('combine lists:')
wife_movies = ['The holiday','Paddington']
our_movies = movies + wife_movies
print(our_movies)

grades = [['Bob', 83], ['Alice', 90], ['Jeff', 99]]
bobs_grade = grades[0][1] #Pulls the second item from the first index.
print(bobs_grade)
grades[0][1] = 91
print(grades)

#Tuples - Do not change, ()
grades = ("a", "b", "c", "d", "f")

#grades.pop #grades.append won't work - not mutable

print(grades[1])

#Looping
nl()
print('##Looping Section')
#For loops execute until complete.
vegetable = ['kale','broccoli','carrots']
for veggies in vegetable:
    print(veggies)

#ip = range(254)
#for x in ip:
#    ping 192.168.1.x

#While executes as long as true
i = 1
while i < 10:
    print(i)
    i += 1






