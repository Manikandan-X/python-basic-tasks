# Task 1: Encapsulation (User Class)

class User:
    
    def __init__(self):
        self.__user_name = None     # private variable
        self.__pwd = None           # private variable
        
    def set_user(self,user_name,pwd ) :
        self.__user_name = user_name
        self.__pwd = pwd
        
    def get_user(self):
        return self.__user_name
    
    def register(self):
        print ("Registering user:" ,self.__user_name)
        
    def login(self):
        print("Logging in:",self.__user_name)
        

log = User()
log.set_user("mani","12345")    

log.login()
log.register()  

# Task 2: Inheritance (User → Student, Faculty)

class User:
    def register(self):
        print("registered")
        
    def login(self):
        print("loggined")

class Student(User):
    def student_greet(self):
        print("Hello student")
        

class Faculty(User):
    def Faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Student,Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")
        
user = User()
user.register()
user.login()
stu = Student()
stu.login()
stu.register()
stu.student_greet()
fac = Faculty()
fac.Faculty_greet()
fac.login()
fac.register()

tem = TempFaculty()
tem.register()
tem.Faculty_greet()
tem.student_greet()
tem.tempFaculty_greet()   


# Task 3: Method Overriding

class Student:
    def greet(self):
        print("Welcome student")
        

class Faculty:
    def greet(self):
        print("Welcome Faculty")


class parent:
    def greet(self):
        print("Welcome User")
        
stu = Student()
stu.greet()
par = parent()
par.greet()
fac = Faculty()
fac.greet() 

# Task 4: Method Chaining

class User:
    def register(self):
        print("registered")
        return self
        
    def login(self):
        print("logined")
        return self
    
    def greet(self):
        print("enjoy everyone")
        return self
    
user = User()
user.register()

user.login().greet().register() 


# Task 5: Combined Task (Real-Time)
# Encapsulation
class User:

    users = 0                               # class variable

    def __init__ (self,user_name,pwd):
        self.__user_name = user_name
        self.__pwd = pwd
        User.users += 1
        
    def get_user(self):
        return self.__user_name
    
    def login(self):
        print(f"{self.__user_name} logged in")
        return self
    
    def greet (self):
        print(f"Welcome {self.__user_name}")
        return self
    
    def register (self):
        print(f"Registered user: {self.__user_name}")
        return self
    
    
# inheritance
class Student(User):
    def greet (self):
        print(f"Hello Student {self.get_user()}")
        return self
    
class Faculty(User):
    def greet(self):
        print(f"Hello Faculty {self.get_user()}")
        return self

# Objects
   
s1 = Student("kumar", "5468")
f1 = Faculty("meera","7852")

# Method chaining

s1.login().greet().register()
f1.login().greet().register()

# Class variable
print("Total users:",User.users)

        

