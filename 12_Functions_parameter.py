#FUNCTIONS
#Defining a fu nction

def function_name():
    print("hello")
function_name()

def greet():
    print("Hello Namaskara")
greet()

#Function Parameter 
#parameter are variables used to pass data into a function
def marriage(boy, girl):
    print(f"{boy} married a {girl}")

marriage("chandan", "chanadana")
marriage("virat", "anushka")

#printing tables using functions
def tables(num):
    for i in range(1, 11):
        print(f"2x{i} = {2*i}")
tables(2)
print()

def tables1(num):
    for i in range(1, 11):
        print(f"{num}x{i} = {num*i}")
tables1(num=3)
tables1(10)
print()

#default parameter values
def marriage1(men="Boy", women="girl"):
    print(f"{men} married {women}")

marriage1()
marriage1("chandan", )

#returning values from function
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("The sum is:", result)

print()
#local and global variable
name = "Global Name"

def greet9():
    name = "Local Name"
    print(name)

greet9()  # Prints local variable
print(name)  # Prints global variable

#another example 
def func():
    x = "chandan"
    print("heloo")
    print(y)
y = "darshan"
print(y)