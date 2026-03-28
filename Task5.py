# Task 1: User Info Manager (Functions + Dictionary)

def create_user(**a):
    for key,val in a.items():
        print (key,val, sep = ":")
    

create_user(name = "kumar", age = 24, role= "developer")

def user(names):
    
    for i in names :
        i = i.title()
        print(i)
li = ["mani", "vino", "vikky"]
user(li)    

# Task 2: Dynamic Calculator (*args)


def calculate_total(*numbers):              # Accept unlimited inputs
    sum = 0
    
    for i in numbers:
        sum = sum + i                       # Return sum of all numbers
        avg = sum / len(numbers)            # return average
    print("total:",sum)
    print("avg:",avg)
calculate_total(5,6,4,5,1)  

# Task 3: Keyword Config System (**kwargs)

# Print all key-value pairs

 

def system_config(**settings):
    for key,val in settings.items():
        print (key,val)
    
system_config(mode= ["reset", "shutdown"], version = [2.0, 3]) 


# Task 4: Factorial Service (Recursion)

def factorial(n):
    if n < 0:
        return "negative number"         
        
    if n == 0:
        return 1
    return n *factorial(n-1)

print(factorial(5))


# Task 5: Memory Optimization (Generator)

def square(n):                              # Normal list
    lis =[]
    for i in range(1,n+1):
        lis.append(i*i)
    return lis
         
print(square(5))

def generator(n):                            # generator
    for i in range(1,n+1):
        yield i*i

print(type(generator(5))) 


# Task 6: Exception Handling Module

try :
    numerator = int(input("enter the number:"))
    denominator = int(input("enter the denominator:"))

    result = numerator /  denominator
    print (result)
    
except ZeroDivisionError:
    print("not divided by 0")
    
except ValueError:
    print("invalid input, enter only number")

finally:
    print("program completed")  
        
        
# Task 7: File Handling

# Write user details into file



with open("team_data.txt") as f:                # Create file: team_data.txt                                 
    
    #print(f.write(" team = ferrari"))
    print(f.read())                             # Read and display content
    print(f.closed)                             # Check if file is closed
