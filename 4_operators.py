#Operators
                #Assignment operator
a = 210
a+=100  # try a-=100 a*=100 a/=100 a%=100
print(a)

                #Comparision operators
a = 10
b = 20

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)  # Output: False
print(a < b)  # Output: True
print(a >= 10)  # Output: True
print(b <= 25 )  # Output: True

                #Logical operators 
print(True and True)   #(3>2) and (2>1) --> o/p True  (1>2 and 4>3) ---> o/p False (because one is true another false)
print(True or False)   
print(not(True))
x = 5
y = 10
z = 15

# and operator
print(x > 0 and y > 5)  # Output: True (both conditions are True) else false

# or operator
print(x > 4 or z > 10)  # Output: True (one of the conditions is True) else false

# not operator
print(not(x > 10))  # Output: True (reverses False to True)


                #Membership operator
my_list = [1, 2, 3, 4, 5]
my_string = "Python"

print(3 in my_list)  # Output: True (3 is in the list)
print(6 not in my_list)  # Output: True (6 is not in the list)
print("P" in my_string)  # Output: True ("P" is in the string)
print("z" not in my_string)  # Output: True ("z" is not in the string)

                #Bitwise operators
a = 5  # In binary: 101
b = 3  # In binary: 011

# Bitwise AND
print(a & b)  # Output: 1 (binary: 001)

# Bitwise OR
print(a | b)  # Output: 7 (binary: 111)

# Bitwise XOR
print(a ^ b)  # Output: 6 (binary: 110)

# Bitwise NOT
print(~a)  # Output: -6 (inverts all bits)

# Left shift
print(a << 1)  # Output: 10 (binary: 1010)

# Right shift
print(a >> 1)  # Output: 2 (binary: 010)

#Arithmetic operator
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a // b)  # Output: 3 (Floor Division)
print(a % b)  # Output: 1 (Modulus)
print(a ** b)  # Output: 1000 (Exponentiation)