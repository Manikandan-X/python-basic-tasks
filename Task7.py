# Task 1: Use super()

# Parent class
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


# Child class 1
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)   
        self.dept = dept
        self.fees = fees


# Child class 2
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)   
        self.salary = salary


# Child class 3
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)  
        self.duration = duration


# Testing
s1 = Student("Mani", 101, "IT", 50000)
f1 = Faculty("Kumar", 201, 60000)
t1 = TempFaculty("Ravi", 301, 45000, "6 months")

print(s1.name, s1.id, s1.dept, s1.fees)
print(f1.name, f1.id, f1.salary)
print(t1.name, t1.id, t1.salary, t1.duration)

#  Task 2: Apply Abstraction

from abc import ABC, abstractmethod


# Abstract Base Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# Child class 1
class Student(AbstractUser):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def get_details(self):
        return f"Student Name: {self.name}, Department: {self.dept}"


# Child class 2
class Faculty(AbstractUser):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Faculty Name: {self.name}, Salary: {self.salary}"


# Testing
s1 = Student("Mani", "IT")
f1 = Faculty("Kumar", 50000)

print(s1.get_details())
print(f1.get_details())

# Task 3: Sorting using key

from functools import reduce


class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


students = [
    Student("Mani", 80000),
    Student("Arun", 50000),
    Student("Kumar", 10000)
]

faculties = [
    Faculty("Ravi", 68000),
    Faculty("Suresh", 27000),
    Faculty("minas", 54000)
]


# Task 4: map() 

names = list(map(lambda s: s.name, students))
print("Student names:", names)


# Task 5: filter()

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculties))

print("\nStudents with fees > 50000:")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nFaculty with salary > 30000:")
for f in high_salary_faculty:
    print(f.name, f.salary)


# Task 6: reduce()

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)

print("\nTotal fees collected:", total_fees)
print("Total faculty salary:", total_salary)


# Task 7: Higher Order Function

def process_users(users, func):
    return list(map(func, users))


student_names = process_users(students, lambda s: s.name)
print("\nProcessed student names:", student_names)

# Build a mini system

from functools import reduce


class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, Fees: {self.fees}"


class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, Salary: {self.salary}"


students = [
    Student("miller", 10000),
    Student("rohit", 50000),
    Student("karunas", 70000)
]

faculties = [
    Faculty("akash", 40000),
    Faculty("kathir", 35000),
    Faculty("Priya", 55000)
]


# Print all details using map()
print("All Student Details:")
student_details = list(map(lambda s: s.get_details(), students))
for detail in student_details:
    print(detail)

print("\nAll Faculty Details:")
faculty_details = list(map(lambda f: f.get_details(), faculties))
for detail in faculty_details:
    print(detail)


# Sort data
students.sort(key=lambda s: s.fees)
faculties.sort(key=lambda f: f.salary)

print("\nSorted Students by Fees:")
for s in students:
    print(s.name, s.fees)

print("\nSorted Faculty by Salary:")
for f in faculties:
    print(f.name, f.salary)


# Filter data
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculties))

print("\nFiltered Students (fees > 50000):")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nFiltered Faculty (salary > 30000):")
for f in high_salary_faculty:
    print(f.name, f.salary)


# Total fees and salary using reduce()
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)

print("\nTotal Fees:", total_fees)
print("Total Salary:", total_salary)