name = "Sachin" #string
age = 22 #integer
is_student = False #bool
weight = 51.8 #float
print(type(weight))

x = None
print(type(x))

age = float(age)
print(age)

s = "100"
print(s)
print(type(s))

#print(s+age) this is gives error because s is string and age is float. therefore we have to change s value to float.

l="100"
m="200"
print(l+m) #OUTPUT for adding two or more strings result in concatination -------> 100200S




                                             # DATA TYPES IN PYTHON
# Python has various built-in data types. Some common ones are:

        # int: For integers (e.g., 1, -3, 100)
        # float: For floating-point numbers (e.g., 3.14, -0.001)
        # str: For strings (e.g., "Hello", "Python")
        # bool: For boolean values (True or False)
        # Type Checking:
        # You can use the type() function to check the type of a variable.

#example
    # x = 10
    # print(type(x))  # Output: <class 'int'>


                                            #TYPE CONVERSION
    # Python allows you to convert between data types using functions like int(), float(), str(), etc.

# Example:
        # x = "10"  # x is a string
        # y = int(x)  # Convert string to integer
        # z = float(y)  # Convert integer to float
        # print(z)  # Output: 10.0