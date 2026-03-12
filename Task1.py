# Task 1 – Print Formatting

print("Hello World", end = " ")
print("Welcome Python" )
print("Laptop","Keyboard","Mouse", sep = " | ")

# Task 2 – Variables

name = "Ravi"
age = 22
city = "Chennai"
print(name, age, city, sep = "-")

# Task 3 – Multiple Assignment

name, age, student = "Meena", 20, True
print(name, age, student)

# Task 4 – Indexing

word = "python"
print(word[0], word[2], word[5])

# Task 5 – Arithmetic Operators

print(25+10, 50-20, 8*5, 100/10, 10%3, 2**4, 20//3, sep = "\n" )

# Task 6 – BODMAS Expression

print(3 + 2 * 5 ** 2)
'''
Explanation
   step 1 - it will square thu number (5**2 = 25)
   step 2 - Multiply the numbers (2*25 = 50)
   step 3 - Add the numbers (3+50 = 53)
   Output will be - 53'''
   
# Task 7 – Assignment Operator

num = 50
num += 25
print(num)

num = 100
num /= 10
print(num)

# Task 8 – Comparison Operators

print(10>5, 20<15, 5==5, 10!=8, 7>=7, 6<=2, sep ="\n")

# Task 9 – String Comparison

a = "apple"
b = "Apple"
print(a==b) #Python string comparison is case-sensitive

# Task 10 – Logical Operators
                            # conditions
print(10>5 and 5==5)    # True and True → True
print(5>10 or 10==10)   # False or True → True
print(not(5>2))         # not(True) → False

# Task 11 – Membership Operator

numbers = [10,20,30,40,50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

# Task 12 – Swap Variables

a = 10
b = 20
a, b = b, a
print(a,b)

# Another method for swaping
tem = a
a = b
b = tem
print(a,b)       #In this method we added a tem variable for "a" variable and the output will same as input again.

# Task 13 – Bitwise XOR

a = 6
b = 3
print(a^b)      # Bitwise XOR: compares binary bits of 6 and 3