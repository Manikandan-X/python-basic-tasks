# task-1
# Create two variables a = 10 and b = 6.
# Print the result of a & b.

c = 10
b = 6
print(c & b)   #expected o/p - 2

# task-2
# Create two variables x = 12 and y = 5.
# Print the result of x | y.

x = 12
y = 5
print(x|y)      #expected o/p - 13

# task-3
# Create a variable num = 8.
# Print the result of ~num.

num = 8
print(~num)      #expected o/p- -9

# task - 4
# Create two variables a = 15 and b = 9.
# Print the result of a ^ b.

a = 15
b = 9
print(a^b)      #expected o/p- 6

# task - 5
# Create a variable num = 7.
# Perform left shift by 2 and print the result.

num = 7
print((7<<2))       #expected o/p- 28

# task - 6
# Create a variable num = 20.
# Perform right shift by 1 and print the result.

num = 20
print(20>>1)        #expected o/p- 10

# task - 7
# Take two numbers from user input and print AND result.

num1 = int(input("enter the number:"))
num2 = int(input("enter the number:"))
print(num1 & num2)          # using AND bitwise operator

# task - 8
# Take two numbers from user input and print XOR result.

num1 = int(input("enter the number:"))
num2 = int(input("enter the number:"))
print(num1 ^ num2)       # using XOR bitwise operator'''

# String Tasks
# TASK - 9
# Create a string "hi" and print it 4 times using replication.

str = "hi"
print(str * 4)  #  using replication

# task - 10
# Create a string "python" and print it 3 times.

str = "python"
print((str + "\n")*3)

# task - 11
# Create two strings "super" and "man" and combine them using + operator.

str1 = "super"
str2 = "man"
print(str1 + str2)  #using concatination 

# task - 12
# Create three strings "hello", " ", "world" and print "hello world".

str1 = "hello"
str2 = " "
str3 = "world"
print(str1 + str2 + str3)       #  #using concatination 

# task - 13
# Take a name from user input and print it 5 times.

name = input("enter the name:")
print((name + "\n")* 5)

# task - 14
# Take two strings from user input and concatenate them.

str1 = input()
str2 = input()
print(str1 + str2) 

# Input & Type Casting Tasks 
# task - 15
# Take a name from user input and print its data type.

name = input("enter the name:")
print(type(name))     

# task - 16
# Take age from user input and convert it into integer.

user = int(input("enter the age: "))
print(user)

# task 17
# Take two numbers from user input and print their sum.

user1 = int(input("enter the number: "))
user2 = int(input("enter the number: "))
print (user1 + user2)

# task - 18
# Take two marks from user input and print their average.


user1 = int(input("enter the number: "))
user2 = int(input("enter the number: "))
print ((user1 + user2)/2)

# task - 19
# Take two numbers from user input and print

user1 = int(input("enter the number: "))
user2 = int(input("enter the number: "))
print (3*user1 * 2 +  user2-2)

# task - 20
# Take a number from user input and print its data type before and after type casting.

user = input()
print(type(user))  # expected op- "str"
casting = int(user)
print(type(casting)) # expected op- "int"  '''

# Unit Digit Tasks 
# task - 21
# Take a number as string input and print the last digit.

str = input()
print(str[-1]) # expected op- 3'''

# task - 22
# Take a number and print the unit digit using % operator.
num = 5454
print(num%10)  # expected op- 4

# task - 23
# Take a number and remove the last digit using // operator.

num1 = 487
print(num1//10)     # expected op- 48

# task - 24
# Take a number and print the second last digit.

num2 = 456
print(num2%10)      # expected op- 6

# task - 25
# Take a 5 digit number and print its last digit.

num3 = 12345
print(num3%10)      # expected op- 5

# If Statement Tasks
# task - 26
# Create a program that checks if 10 ≥ 5 and prints a message.

if 10>5:
    print("its true")
    
# task - 27
# Take a number from user input and check if it is greater than 50.

user = int(input("enter the number:"))
if user > 50:
    print("yes")
else:
    print("no")

# task - 28
# Take age from user input and check if age ≥ 18.

age = int(input("enter the age:"))
if age >= 18:
    print("you are adult")
else:
    print("you are not an adult")
    
# task - 29
# Take a number and check if it is greater than 100.

num = 55
if num > 100:
    print("yes, its greater than 100")
    
else:
    print("no, its not greater than 100")
    
# task - 30
# Take a number and check if number ≥ 0.

num = 45
if num >= 0:
    print("greater than 0")
    
# If-Else Tasks
# task - 31
# Take a number and check if it is even or odd.

num = 4
if (num & 1!=0):         # using & bitwise operator to compare the numbers 
    print("number is odd")
else:
    print("number is even")
    
# task - 32
# Take marks from user input and check if pass or fail (pass ≥ 35).

marks = int(input("enter the mark:"))
if marks >= 35:
    print("pass")
else:
    print("fail")

# task = 33
# Take a number and check if it is positive or negative.

num = 4
if num >= 0:
    print("positive")
    
else:
    print("negative")


# task = 34
# Take a number and check if it is greater than 10 or not.

num = 34
if num > 10 :
    print("greater than 10")
else:
    print("less than 10")

# Nested If Tasks
# task - 35
# Create a program for job eligibility

age = int(input("enter the age:"))
height = int(input("enter the height:"))
weight = int(input("enter the weight:"))
if age >= 18:
    if height >= 160:
        if weight >=60:
            print("you are selected")
        else:
            print("sorry, your weight is not eligible")
    else:
        print("sorry, your height is not eligible")
else:
    print("sorry, your age is not eligible")


# task - 36
# Create a college admission program

marks = int(input("enter the mark:"))
age = int(input("enter the age:"))
if marks >= 60:
    if age >= 17:
        print("you are eligible")
        
    else:
        print("age is not eligible")
else:
    print("marks are not eligible")


# task - 37
# Create a sports selection program

age = int(input("enter the age:"))
height = int(input("enter the height:"))
weight = int(input("enter the weight:"))
if age >= 16:
    if height >= 150:
        if weight >=50:
            print("you are selected")
        else:
            print("sorry, your weight is not eligible")
    else:
        print("sorry, your height is not eligible")
else:
    print("sorry, your age is not eligible")


# Match Statement Tasks
# task - 38
# Take a number (1-7) and print day name using match.

day = int(input("enter the day number:"))

match day:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("saturday")

# task - 39
# Take a number (1-3) and print

color = int(input("enter the color number:"))    
match color:
    case 1:
        print("red")
    case 2:
        print("blue")
    case 3:
        print("green")

# task - 40
# Take a number (1-4) and print

fruit = int(input("enter the fruit number:"))    
match fruit:
    case 1:
        print("apple")
    case 2:
        print("mango")
    case 3:
        print("orange")
    case 4:
        print("banana")