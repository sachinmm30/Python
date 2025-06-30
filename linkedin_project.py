import random
import time

time.sleep(3)
print("picking a num.....")
time.sleep(2)
guess = (input("what is your guess?: "))
correct_number = random.randint(1, 100)
guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("wrong. you need to guess higher what is your guess?:"))
    else:
        guess = int(input("wrong. you need to guess lower what is your guess?:"))
print(f"congrats! the right answer was{correct_number}. it tookyou {guess_count} guesses.")