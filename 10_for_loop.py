#FOR LOOPs
#basic structure
cities = ["mys", "bng", "hub", "mang"]
for city in cities:
    print(city)
print() # to print empty line

#range() in for loops
for i in range(1, 10, 2): #here (start, stop, step/slip)
    print(i)      #stop is not included ---> exclusive
print()

#loops over strings
name = "KARNATAKA"
for state in name:
    print(state*2, end=" ")   #end=" " is used to print in the same line
print()

#Nested for loops 
for i1 in range(1, 11):
    for j1 in range(1, 11):
        print(f"{i1} x {j1} = {i1 * j1}")
    print()


#Break in a for loop
cars = ["BMW", "BENZ", "VOLVO", "PORSHE"]
for car in cars:
    if car == "VOLVO":
        print(f"Found {car}")
        break
    print(car)
print()

#Continue in for loops
cars1 = ["BMW", "BENZ", "VOLVO", "PORSHE"]
for car1 in cars1:
    if car1 == "VOLVO":
        #print(f"Found {car1}")
        continue
    print(car1)
print()

#Looping through a list with enumerate()
cities1 = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for index, city1 in enumerate(cities1):
    print(f"City {index + 1}: {city1}")
print()

#else in for loops
for city in cities:
    print(city)
else:
    print("No more cities!")
print()

#Real-Life Example: Distributing Laddus
laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya", "king", "virat"]

for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
        laddus -= 1
    else:
        print("No laddus left!")
print()

#Homework
#1
for i9 in range(3, 31, 3):
    print(i9, end=" ")
print()

#2
total_sum =0
for i0 in range(1, 11):
    total_sum += i0
    print(total_sum)
print()

#4
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the string:", vowel_count)