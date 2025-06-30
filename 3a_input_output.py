print("Hello") #output

age = input("NAME: ") #input
print(age)

boy_name = input("boy Name is : ")
girl_name = input("Girl name is: ")
boy_age = int(input("Boy Age is: "))
girl_age = int(input("Girl Age is: "))
Age_diff= abs(boy_age - girl_age) #abs is used to print absolute value like -30 absolute value is 30.

print(boy_name + " loves " + girl_name)    # NormalConcatination
print("age difference is : " + str(Age_diff))
print(f"age difference is : {Age_diff} " + boy_name) #Formal concatination



                                       # 1. Input and Output in Python
# 1.1 Input from the User:
    # In Python, we use the input() function to take input from the user.
    # The data entered by the user is always received as a string, so if you want to use it as a different data type (e.g., integer or float), 
    # you'll need to convert it using type conversion functions like int() or float().

    # name = input("Enter your name: ")
    # age = int(input("Enter your age: "))  # Convert input to integer
# 1.2 Output to the Console:
    # The print() function is used to display output to the console. You can use it to display text, variables, or results of expressions.

    # print("Hello, " + name + "! You are " + str(age) + " years old.")
    # You can also use f-strings (formatted string literals) for more readable code:

    # print(f"Hello, {name}! You are {age} years old.")
                            
                            
                            # 3. Comments in Python
    # Comments are ignored by the Python interpreter and are used to explain the code or leave notes for yourself or others. 
    # They do not affect the execution of the program.

            # Single-line comments start with #:
    # # This is a single-line comment
    # print("Hello, World!")

            # Multi-line comments
    # Multi-line comments can be written using triple quotes (""" or '''). 
    # These are often used to write detailed explanations or temporarily block sections of code:

"""
    # This is a multi-line comment.
    # It can span multiple lines.
"""
    # print("Hello, Python!")                                    


#homework1
Name=input("Enter your name: ")    
Age=int(input("Age: "))   
print(Name)
print(Age)
print("Hello, "+ Name +"!" +" you are " + str(Age) +" old.")
print(f"Hello, {Name}! you are {Age} old." ) 

#homework2
