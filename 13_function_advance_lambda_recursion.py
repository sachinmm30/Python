#keyword arguments
def display_info(name, age):
    print(f"Name: {name}, \nAge: {age}")

display_info(age=25, name="Kumar")
print()

#variable length arguments

def total_sum(a, b):
    return a + b
c = total_sum(1, 2)
print(c)

#using *args
def add(*a):
    return sum(a)
print(add(1, 2, 3, 4, 5, 6))

#**kwrgs ----> KeyWordArguments
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Anand", age=22, course="Python")

#LAmda function
double = lambda x: x * 2
print(double(5))

add = lambda a, b : a+ b
print(add(4, 5))

students = [
    {"name": "sachin","marks": 25},
    {"name": "darshan", "marks": 104},
    {"name":"kohli", "marks": 45}
]   
students.sort(key= lambda x: x["marks"], reverse=True)
print(students)

#Recursion
# def greet():
#     print("hello")
#     greet()

# greet()

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

#Nested Functions
def outer_function(name):
    def inner_function(age):
        print(f"Hello, {name}!, {age}")
    inner_function(22)

outer_function("Anand")

#example nested function
def calculate(a, b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mult():
        print(a*b)
    add()
    sub()
    mult()
calculate(10, 2)