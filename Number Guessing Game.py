# Description: Write a program that randomly generates a number between 1 and 100.
# The user has to guess the number, and the program will give feedback if the guess is too high or too low.
# Use the random module to generate a random number.
# Give the user multiple attempts to guess the number.
# Provide appropriate feedback (e.g., "Too high" or "Too low").
# Exit the game if the user guesses correctly or after a maximum number of attempts.

import random
rand = random.randint(1, 100)
trial = 0
while trial < 3:
    guess = int(input("Enter random number between 1 and 100: "))
    if rand == guess:
        print("Hey you guessed correctly!!")
        break
    elif guess < rand:
        print("Too low")
    elif guess > rand:
        print("Too high")
    else:
        print("Out of bound")
    trial += 1
    print(f"""
            No of Trial {trial} out of 3
            Try again! 
            """)
    print()
    if trial == 3:
        print("Trial Ends")
        print(f"Random number is = {rand}")
        break



