# variables
# Used to store information in a computer's memory
# to declare a variable we need a name for it
#age = 20
# we can change the variable, and it will print the current value
#age = 30
# the program is executed top to bottom
#print(age)
# variable examples
#price = 19.95
#first_name = "Mosh"
#is_online = False
# variable exercise
#Person = "John Smith"
#Age = 20
#Patient_Type = "New"
# -----------------------------------
# Receiving an Input
#the input function allows us to give the user a chance to  input values

#name = input("What is your name? ")
#print("Hello " + name)

#In this example we can see that we are able to assign an input to a variable
#which can be used in other ways

#---------------------------------------
#type conversion
#this example shows how to calculate someones ages based on the year of birth
#this is done by convering a string to an int to function.
#birth_year = input("Enter your birth year: ")
#age = 2022-int(birth_year)
#print(age)
#key words to type cast
#int()
#float()
#bool()
#str()

#Calculator exercise

#First = input("First: ")
#Second = input("Second:")
#Output = float(Second) + float(First)
#print("Output: " + str(Output))

#type casting can be done in the variable allocation as well
#------------------------------------------

#strings
#here we can see what we can do with strings. We are able to use a "." to
#use multiple premade functions to code.

#course = "Python for Beginners"
#print("Python" in course)
# above we can see another way to do the find function using the in operator
#-------------------------------------------------------

#arithmetic operators
# they are the same as maths however a usefual way to count loops can be seen
#x =+ 3
#------------------------------------------------------

#Operator Precedence
#follows bodmas rules
#x = 10 + 3 * 2
#--------------------------------------------------------

#Comparison Operators
#these operators are used to compare values
#>, >=, <, <=, ==, !=

#----------------------------------------------------------

#Logical Operators
#these are used to build complex roles and conditions

#price = 15
#print(not price < 10 )

# and (both)
# or (at least one)
# not (inverse of the value given)

#------------------------------------------------------------

#if Statements
#used to make decisions within the programme

#temperature = 15

#if temperature > 30:
    #print("It's bloody hot today")
#elif temperature < 10:
    #print("Feeling cold today big man")
#else:
    #print("Today is a normal day")

#exercise - Weight converter Programme

#Weight = int(input("Weight: "))
#Unit = input("(K)g or (L)bs:")

#if Unit.upper() == "K":
#    converted = Weight / 0.45
#    print("Weight in Lbs: " + str(converted))
#else:
#     converted = Weight * 0.45
#     print("weight in Kg :" + str(converted))

#-----------------------------------------------------------------

#While Loops
# used to repeat a block of code multiple times

# i = 1
# while i <= 10:
#     print(i * "*")
#     i = i+1
#--------------------------------------------------------------------

#lists
#we use these whenever we need to represent #a list of objects

#names = ["A", "B", "C", "D"]
#print(names)

#List exercise
#this is an exercise to find the largest number in a list
# numbers =[3,6,2,8,4,10]
# max =  numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
#------------------------------------------

#List Methods
#like objects there are a number of methods that can be used to
#change and sort how an object is seen or used.

#number= [1,2,3,4,5]

#print(len(number))

#list methods exercise
#this is a program to remove duplicates from a list

# numbers = [2,2,4,6,3,4,6,1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)


#-----------------------------------------------------------------

#for loops
# these are used to repeat a block of code while
# accessing each item indiviually

#numbers = [ 1,2,3,4,5]

#for item in numbers:
#    print(item)
#-------------------------------------------------------------------

#the range function
#it is used to generate a sequence of numbers
#for number in range(5):
#    print(number)

#--------------------------------------------------------------------

#tuples
#like lists but they are immutable

#numbers = (1,2,3)

#---------------------------------------------------------------------

#Making a Guessing game  - Exercise
# Guess_Count = 0
# Answer = 9
# Guess_limt = 3
# while Guess_Count < Guess_limt:
#     Guess = int(input("Guess: "))
#     Guess_Count += 1
#     if Guess == Answer:
#         print("You Won!")
#         break
# else:
#     print("Sorry you failed!")
#--------------------------------------------------------------------

#Car Game - Exercise
# command = ""
# started = False
# while True:
#     command = input(">").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car Started...")
#
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car Stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry I do not understand")

#--------------------------------------------------------------
#Nested loops
#it is a loop inside another loop

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")
#------------------------------------------------------------------

# nested loop Exercise
#this makes an L made out of X's
# numbers =[2,2,2,2,7]
#
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output += "x"
#     print(output)

#----------------------------------------------------------------

#2D lists
#are power tools withing data science and machine learning
# here we are looking at matrixes

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)
#-----------------------------------------------

#unpacking
#

# coordinates = (1,2,3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
#the code above is the simpler version of the code below
#the method below is better practice

# coordinates = (1,2,3)
# x,y,z = coordinates
#this allows us to unpack things to shorten code

#dictionaries
#used to store info that come as key value pairs
#e.g name, email, phone no. the key would be the name

# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# print(customer.get("name"))#or use key brackets with index position

#exercise for dictionaries

# phone = input("Phone: ")
#
# digits_mapping = {
#     "1" : "one ",
#     "2" : "two ",
#     "3" : "three ",
#     "4" : "four "
# }
# output = " "
# for ch in phone:
#     output += digits_mapping.get(ch,"!")+ ""
# print(output
#     )

#emoji converter exercise

# message = input(">")
# words = message.split(" ")
# emojis = {
#     ":)" : "😀",
#     ":(" : "😭"
# }
# output = " "
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

#------------------------------------------------------
#functions 2 30 42















