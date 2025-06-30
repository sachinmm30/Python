#The Basic Structure of a while Loop
i = 1
while i <= 5:
    print(i)
    i += 1  # Incrementing i by 1 after each iteration

#Common Example: Counting Sheep

sheep_count = 1
while sheep_count <= 10:
    print(f"Sheep {sheep_count}")
    sheep_count += 1

#Avoiding Infinite Loops
# i = 1
# while i <= 5:
#     print(i)
    # Forgot to update i, so the condition remains True forever!

is_failed = True
i1 = 1 #attempt

while is_failed and i1<=100:
    print(f"try{i1}")
    i1 = i1 +1
print("i gave up")

#Using break to Exit a while Loop
sheep_count1 = 1
while sheep_count1 <=10:
    print(f"Sheep {sheep_count1}")
    if sheep_count1 == 5:
        print("Enough counting")
        break
    sheep_count1 +=1

#to find even numbers
is_failed1 = True
i2 = 1 #attempt

while is_failed1 and i2<=100:
    if i2%2!=0: #not even that is odd
        i2 = i2 +1  
        continue
    print(f"Attempt {i2}")
    i2 = i2 +1
    if i2 > 100:
        print("i gave up")

#to print num from 0 to 10
i3 = 0
while i3<=10:
    print(i3)
    i3 +=1

#Using continue to Skip an Iteration
sheep_count = 1
while sheep_count <= 5:
    if sheep_count == 4:
        sheep_count += 1
        continue
    print(f"Sheep {sheep_count}")
    sheep_count += 1


#Using while Loops for User Input
pin = ""
correct_pin = "1234"
while pin != correct_pin:
    pin = input("Enter your PIN: ")
    if pin != correct_pin:
        print("Incorrect PIN. Try again.")
print("PIN accepted. You can proceed.")

#Nested While loop

i6 = 0
while i6<=10:
    x = i6
    while x<i:
        print("chandan") 
        x += 1
    i6 += 1

#Real-life Example: KSRTC Bus Seats Availability

available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")

#Nested while Loops
snacks_available = 3
money = 10

while snacks_available > 0 and money > 0:
    print(f"Snacks available: {snacks_available}. Money: ₹{money}")
    buy = input("Do you want to buy a snack for ₹5? (yes/no): ").lower()
    
    if buy == "yes" and money >= 5:
        snacks_available -= 1
        money -= 5
        print("Snack purchased!")
    else:
        print("No purchase made.")
        
print("Either snacks are sold out or you are out of money.")