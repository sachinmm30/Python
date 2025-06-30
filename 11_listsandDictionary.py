#Lists and Dictionary with for loops
l = [1,23, 43, 524, 76]
total = 0

for num in l:
    print(total, end=" ") # to print individual count 
    total += num
print(total)
print()

#Looping Through Lists
#A for loop is the most common way to iterate through items in a list.
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total sum:", total)
print()

#Doubling each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print("Doubled List:", doubled)
print()

#Looping through dictionaries
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student in student_marks:
    print(student, end=" ")
print()

#for Loops with range()
#You can also use for loops with the range() function to loop through a sequence of numbers.

students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]

student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)
print()

