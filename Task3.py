# Section 1: Loop Basics
# Print numbers from 1 to 50 using for loop


for num in range(1,51):
    print(num)
    
    
# Print even numbers from 1 to 100

for num in range(2,101,2):
    print(num)
    

# Print odd numbers from 1 to 100


for num in range(1,101,2):
    print(num)
    
    
# Print multiplication table of 7


for num in range(1,11):
    print("7 *", num, "=",num*7)
    

# Find sum of numbers from 1 to 100


tem = 0
for num in range(1,101):
    tem = tem + num
print(tem)


# Print numbers in reverse from 50 to 1


for num in range (50,0,-1):
    print(num)
    

# Count how many numbers are divisible by 3 (1–100)


count = 0
for num in range (1,101):
    if num % 3 == 0:
        count = count +1
print(count)


# Print squares of numbers from 1 to 10


for num in range(1,11):
    print(num**2)
    


# Print cube of first 10 numbers


for num in range(1,11):
    print(num*num*num)
    
    

# Take input n, print numbers from 1 to n
    

n = int(input("enter the number:"))
for num in range(1,n+1):
    print(num)
    
    

# Section 2: While Loop
# Print numbers from 1 to 20 using while


num = 1
while num <= 20:
    print(num)
    num = num + 1
    
    
# Find factorial of a number using while


num = 5
fact = 1
while num != 0:
    fact = fact * num
    num -= 1
    print(fact)
    
    
# Reverse a number using while



num = 12345
rev = 0
while num >0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10
print(rev)


# Count digits in a number


num = 54321
count = 0
while num:
    count = count + 1
    num = num // 10
print(count)


# Keep asking input until user enters "stop"


while True:
    user = input()
    if user == "stop":
        break
print("stopped")


# Section 3: Nested Loop 
# Print pattern:

rows = 4


for i in range(1, rows + 1):
    line = ""
    for j in range(i):
        line += "*"
    print(line)  
            
    

# Print pattern:



rows = 4

for i in range(1, rows+ 1):
    line = " "
    for j in range(1,i+ 1):
        line += str(j)
    print(line)
    
    
# Print multiplication table (1 to 5) using nested loop


for i in range(1, 6):                       # tables from 1 to 5
    for j in range(1, 11):                  # multiply from 1 to 10
        print(f"{i} x {j} = {i*j}")
    print()  
                                            # space between tables
        
# Print pattern:


for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()
    

# print pattern


num = 1
for i in range (3):
    for j in range (3): 
        print(num, end=" ")
        num+= 1
    print()
    
    
# Section 4: String Basics

# Count total characters in a string

str = "maanik"
print(len(str))

# Count vowels in a string


str = "vignesh"
no = 0
vowel = ["a", "e","i","o","u"]
for words in str:
    if words in vowel:
        no += 1
print(no)


# Count consonants in a string


str = "vignesh"
no = 0
vowel = ["a", "e","i","o","u"]
for words in str:
    if words not in vowel:
        no += 1
print(no)


# Reverse a string using loop

str = "vinoth"
rev = ""
for words in str:
    rev = words + rev
print(rev)

# Check if string is palindrome

str = "mnb"
if(str == str[::-1]):
    print("palindrome")
else:
    print("not palindrome")
    
# Section 5: String Slicing 
# Print first 5 characters of a string

str = "vigneshvenkat"
print(str[:5:])

# Print last 3 characters

str = "vigneshvenkat"
print(str[-3::])

# Print string in reverse using slicing

str = "kumaresh"
print(str[::-1])

# Print every 2nd character

str = "kumaresh"
print(str[::2])

# Remove first and last character from string


str1 = "kumaresh"
print(str1[1:-1:])      

# Section 6: List Basics
# Create a list of 5 numbers and print sum

list = [4,5,6,2,3]
print(sum(list))

# Find maximum value in list
list = [4,5,6,2,3]
print(max(list))

# Find minimum value in list

list = [4,5,6,2,3]
print(min(list))

# Count total elements in list

list = [4,5,6,2,3]
print(len(list))

# Check if element exists in list

list = [4,5,6,2,3]
if 5 in list:
    print("5 in list")
    
else:
    print("not in list")
    
# Section 7: List Operations
# Add 3 elements using append()

list = [4,5,6,2,3]
list.append(8)
list.append(9)
list.append(11)
print(list)

# Insert element at specific index

list = [4,5,6,2,3]
list.insert(0,0) 
print(list)

# Remove element using remove()

list = [4,5,6,2,3]
list.remove(6)
print(list)

# Reverse list without using .reverse()

list = [4,5,6,2,3]
print(list[::-1])

# Sort list without using .sort()

list = [4, 5, 6, 2, 3]
sorted_list = []

while list:
    m = min(list)
    sorted_list.append(m)
    list.remove(m)
print(sorted_list)