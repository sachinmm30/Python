# if-elif-else

x = int(input("num: "))   #x = 10

if x==10:
    print("yes it's 10")
    print("you are right")

#if Statement
time = 20  # 20 represents 8 PM in 24-hour format
if time == 20:
    print("It's time for dinner!")

#else statement
time = 18  # 6 PM
if time == 20:
    print("It's time for dinner!")
else:
    print("It's not dinner time yet.")

#elif statement
time = 15  # 3 PM
if time == 8:
    print("It's breakfast time!")
elif time == 13:
    print("It's lunch time!")
elif time == 20:
    print("It's dinner time!")
else:
    print("It's not a meal time.")

#Comparison Operators in if Statements
age = 19

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#example
atendance= 75
is_techer_friend = True
# if atendance>= 75:
#     print("Exam")
if atendance>=75 or is_techer_friend==True:
    print("Atend Exam")
else:
    print("ready to fail")

#example Checking bus tickets

gender=input("Gender : ")
age = int(input("Age : "))
if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")

#example Checking bus tickets using nested if statements
gender1=input("Gender1 : ")
age1 = int(input("Age1 : "))
if gender1=="female":
    print("free ticket")
else:
    if age<=12:
        print("you get children discount")
    elif age>=60:
        print("you get senior citizen discount")
    else:
        print("you have to pay full fare")

#The match-case Statement (Python 3.10+)
# day = "Sunday"

#match day:
    # case "Monday":
    #     print("Start of the work week.")
    # case "Friday":
    #     print("Almost weekend!")
    # case "Saturday" | "Sunday":
    #     print("It's the weekend!")
    # case _:
    #     print("Just another weekday.")