Prepare a class of students with name, age, Id. Arrange it as per name and display all the details

class Student:

def __init__(self, name, age, id):

self.name = name

self.age = age

self.id = id

student1 = Student("Anish Patel", 20, 101)

student2 = Student("Siddharth Rai", 22, 102)

student3 = Student("Aayush Anshul ", 19, 103)

student4 = Student("Jacob John", 21, 104)

students = [student1, student2, student3, student4]

for i in range(len(students)):

for j in range(i+1, len(students)):

if students[i].name > students[j].name:

students[i], students[j] = students[j], students[i]

for student in students:

print("Name:", student.name, ", Age:", student.age, ", ID:", student.id)






Write a program to understand the multiple inheritance concept. Include the concept of constructor overriding

class Engine:

def __init__(self, fuel_type):

self.fuel_type = fuel_type

def start(self):

print("Engine started")

class Transmission:

def __init__(self, transmission_type):

self.transmission_type = transmission_type

def shift_gear(self):

print("Gear shifted")

class Car(Engine, Transmission):

def __init__(self, make, model, fuel_type, transmission_type):

Engine.__init__(self, fuel_type)

Transmission.__init__(self, transmission_type)

self.make = make

self.model = model

def drive(self):

print("Car is being driven")

def display(self):

print(f"Make: {self.make}, Model: {self.model}, Fuel Type: {self.fuel_type}, Transmission Type: {self.transmission_type}")

my_car = Car("BMW", "M3", "Petrol", "Manual")

my_car.start()

my_car.shift_gear()

my_car.drive()

my_car.display()