"""
**Constructors and the `self` Keyword**

**1. The `__init__()` Constructor**

- **Constructor**: The `__init__()` method in Python is a special method that initializes an object when it’s created. It’s called automatically when you create a new instance of a class.
- **Purpose**: It allows you to set the initial state of the object by defining its attributes.

**Syntax**:

class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2


- Here, `__init__()` receives parameters and sets the initial values of object attributes.

**2. Using `self` in Class Methods**

- **`self`**: Refers to the instance of the class itself, allowing you to access attributes and methods within a class.
  - It is automatically passed as the first argument to methods within the class.
  - **Note**: While `self` is a convention, you can technically use any name (though it's not recommended for readability).

**Example**:
"""
class Person:
    def __init__(self, name, age):
        self.name = name  # 'self.name' is an instance variable
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating an object
person1 = Person("Arjun", 22)
person1.introduce()
print()
"""
**Output**:
My name is Arjun and I am 22 years old.

Here:
- `self.name` and `self.age` are instance variables.
- `introduce()` is a method that accesses the instance variables using `self`.

**3. Creating Multiple Objects with Different Attributes**
By passing different values to `__init__()` when creating objects, each object can have unique attributes.

**Example**:
"""
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Laptop Brand: {self.brand}, Price: ₹{self.price}")

laptop1 = Laptop("Dell", 45000)
laptop2 = Laptop("HP", 55000)

laptop1.show_info()
laptop2.show_info()
print()
"""
Output**:
Laptop Brand: Dell, Price: ₹45000
Laptop Brand: HP, Price: ₹55000

- Each `Laptop` object has its own values for `brand` and `price`, demonstrating unique attribute assignment through `__init__()`.

4. Optional Parameters in Constructors**

Sometimes, it’s helpful to have default values for certain attributes. You can do this by setting default values for parameters in `__init__()`.

**Example**:
"""
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

    def show_book(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Python Programming")
book2 = Book("Machine Learning", "Andrew Ng")

book1.show_book()
book2.show_book()
print()
"""
**Output**:
Title: Python Programming, Author: Unknown
Title: Machine Learning, Author: Andrew Ng
#In this example:
- If an author is not provided, it defaults to `"Unknown"`.
"""