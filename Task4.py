# Mini Project 1: Employee Management System
# Concepts: Dictionary, List, Functions

dit = {"name" : ["mani","kumar","vinoth","vignesh"], "age":[24,23,32,25], "role":["developer","intern","tester","team lead", "manager"],"salary":[25000,2100,5000,50000]}
dit["name"].append("king")
dit["age"].append(44)
dit["salary"].append(50000)

dit["age"][3] = 41

delete = "mani"
if delete in dit["name"]:
    ele = dit["name"].index(delete)
                                            # This method going to delete one particular eployee details.
    for key in dit:
        dit[key].pop(ele)
    
print(dit) 

# Mini Project 2: Student Report Card
# Concepts: Dictionary, Functions, Formatting
# Dictionary (student data)

student = { "name": "Mani","marks": [85, 78, 92]}

def calculate(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg


# Function to assign grade
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


# Function to print report
def print_report(student):
    total, avg = calculate(student["marks"])
    grade = get_grade(avg)

    print(f"Name   : {student['name']}")
    print(f"Marks  : {student['marks']}")
    print(f"Total  : {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade  : {grade}")
    
# Call function
print_report(student)

# Mini Project 3: Shopping Cart System
# Concepts: List, Dictionary, Loop

products = {"name": ["helmet", "glove", "glass"], "price": [4500,450,500], "quantity": [1,2,3] }                 

delete = "glove"
if delete in products["name"]:
    ele = products["name"].index(delete)
                                            # This method going to delete one particular details.
    for key in products:
        products[key].pop(ele)

# Calculate total bill
total = 0
for p, q in zip(products["price"], products["quantity"]):
    total += p * q
    
# Display all items in formatted way
print("----- CART DETAILS -----")
for i in range(len(products["name"])):
    print(f"Name: {products['name'][i]} | Price: {products['price'][i]} | Qty: {products['quantity'][i]}")

print("-------------------------")
print(f"TOTAL BILL: {total}")

# Mini Project 4: Login & User Validation
# Concepts: Dictionary, Condition

name = input("enter the username: ")
pw = int(input("enter the password: "))
user = {"Name": name, "PW": pw}

if user["Name"] == "lewis" and user["PW"] == 12345:
    print("login sucess")
    
else:
    print("login failed")
    
# Mini Project 5: Unique Visitor Counter
# Concepts: Set

visitors ={"lotus","max","charles","mike","parley","max"} 
print(type(visitors))
print(len(visitors))

# Mini Project 6: String Formatter Tool
# Concepts: String Formatting

# Input name and product

name = input("enter the name: ")
product = input("enter the product: ")
print(f"CUSTOMER_NAME:{name},PRODUCT:{product}")     # Display formatted sentence

print("***{msg:^30}***".format(msg="THANK YOU FOR COMING"))    
print("***{msg:>30}***".format(msg="VISIT AGAIN"))    
                                                               # Show padded output (left, right, center)
print("***{msg:<30}***".format(msg="EXIT THIS WAY>>"))            

# Mini Project 7: Bank Account System
# Concepts: Functions, Dictionary

# Create account (name, balance)

account = {"name": "kumar","balance": 5000}

def deposit(amount):                               # Deposit money
    if account["name"]== "kumar":
        account["balance"] += amount
        print("deposited: ",amount) 
    
def Withdraw(amount):                               # Withdraw money
    if account["name"]== "kumar":
        if amount <= account["balance"]:
            account["balance"] -= amount
            print("withdrawn: ",amount)

def Check():                                        # Check balance
    if account["name"] == "kumar":
        print("balance: ",account["balance"])
    
Withdraw(500)
deposit(1000)
Check()           


# Mini Project 8: Voting System
# Concepts: Dictionary, Loop

# Store candidates and votes
candidates = {
    "kumar": 0,
    "prabhu": 0,
    "mani": 0
}

# Add votes
while True:
    vote = input("Enter candidate name (or 'stop' to end): ").lower()

    if vote == "stop":
        break

    if vote in candidates:
        candidates[vote] += 1
        print("Vote added")
    else:
        print("Invalid candidate")

# Display all votes
print("\n--- Vote Count ---")
for name, count in candidates.items():
    print(f"{name} : {count}")

# Find winner
max_votes = max(candidates.values())

print("\n--- Winner ---")
for name, count in candidates.items():
    if count == max_votes:
        print(f"{name} is winner with {count} votes")
    

# Mini Project 9: Course Enrollment System
# Concepts: List + Dictionary

# Add student with course list

display = {"name":["kumar", "man", "manik"]}
course = {"courses":[["node","java", "selinium"],["python", "ml","sql"],["cad", "adobe","ms office" ]]} 
course["courses"][1][2] = "flutter"                 # Update courses
print(display["name"][0], course["courses"][0])     # Display student details


# Mini Project 10: Number Utility Tool
# Concepts: Functions, Formatting
# Convert number to binary, octal, hex


def binary(number):
    if number >0 :
        print("binary value: {:b}".format(number))
        
def octal(number):
    if number >0 :
        print("octal value: {:o}".format(number))
        
def hex(number):
    if number >0 :
        print("hex value: {:x}".format(number))
        
def scientific(number):
    if number >0 :                                         # Print scientific notation
        print("scientific value: {:e}".format(number)) 
        
binary(5)
octal(5)
hex(5)
scientific(5)

num = 500000
print("money: {:,}".format(num))                            # Format large numbers with commas
    

    