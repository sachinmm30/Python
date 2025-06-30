first_name="Sachin"
last_name="Shaiva"
full_name= first_name + " " + last_name
print(full_name)

#repetition
message = "Warning! "*3     # 3 times Warning! Warning! Warning! stored in message variable
print(message*3)            #9 times prints Warning! Warning! Warning! Warning! Warning! Warning! Warning! Warning! Warning!

'''
Concatenation: Joining two or more strings together using the + operator.
Repetition: Repeating a string multiple times using the * operator.
'''

                #String Methods:
cricketer="Virat Kohli"
print(cricketer)
print(cricketer.upper())             # upper(): Converts a string to uppercase.
print(cricketer.lower())            # lower(): Converts a string to lowercase.
print(cricketer.strip()*2)          # strip(): Removes leading and trailing spaces from a string.
print(cricketer.replace("Kohli", "anushka"))    # replace(old, new): Replaces a substring with another string

name= '''"chandan said 'hello'
                          darshan said 'hi' ""'''
print(name) #OR 'chandan said "hello"'

PM="Narendra Modi"
print(len(PM)) #length 

                    #2.3 Accessing String Characters:

text="python programming"       # python 0,1,2,3,4,5
print(text[0:6])    # text[index number]
print(text[0:6])
print(text[7:])
print(text[3])      #output = h  # index = position -1
print(text[1:6])
print(text[:2])
print(text[3:])
print(text[-1])

king= "modi"
print(king[-2])  #Negative Index

CM="cystone"        #String slicing
print(CM[::3])          #[start: end: Step/Skip]

# You can access individual characters in a string using indexing. Python uses zero-based indexing, so the first character has an index of 0.

# text = "Python"
# print(text[0])  # Output: P
# print(text[2])  # Output: t
# You can also use negative indexing to start counting from the end of the string.

# print(text[-1])  # Output: n
# print(text[-3])  # Output: h

# 2.4 Slicing Strings:
# You can extract a portion (substring) of a string using slicing.

# text = "Python Programming"
# print(text[0:6])  # Output: Python (extracts from index 0 to 5)
# print(text[:6])  # Output: Python (same as above)
# print(text[7:])  # Output: Programming (from index 7 to the end)