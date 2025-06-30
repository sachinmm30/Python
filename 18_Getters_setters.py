#GETTERS SETTERS METHOD OVERLOADING AND OVERRIDING SUPER() ABSTRACT CLASSES
#Getter
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
s = Student("chandan", 22)
print(s.get_name())
print()

#setter
#Eg:
class Student1:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # Private attribute

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Validation
            self.__age = age
        else:
            print("Invalid age")

# Usage
student = Student1("Anita", 20)
print("Age:", student.get_age())  # Accessing age with getter
student.set_age(21)  # Modifying age with setter
print("Updated Age:", student.get_age())
print()

#method overloading
class Maths:
    def add(self, a, b, c=0):
        print(a+b+c)
    
math = Maths()
math.add(5, 10)
math.add(5, 10, 15)

#method overriding

class Animal:
    def make_sound(self):
        print("animal makes sound")

class Dog(Animal):
    def make_sound(self):
        print("bark")

d = Dog()
d.make_sound()
print()
#super() function

class Animal1:
    def make_sound(self):
        print("animal is making sound")

class Dog1(Animal1):
    def __init__(self, name):
        self.name =name

    def make_sound(self):
        super().make_sound()
        print(f"{self.name} is barking Bark")

    def get_angry(self):
        self.make_sound

d1 = Dog1("Buddy")
d1.make_sound()
d1.get_angry()
print()
#Abstarct Class
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract base class
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method with no implementation

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

# Usage
car = Car()
car.start_engine()