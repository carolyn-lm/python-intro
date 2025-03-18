# import random module
import random

correct_guess = False
random_number = random.randrange(100)

while not correct_guess:
    user_input = input("Guess a number between 0 and 100: ")
    try:
        number = int(user_input)
        if number == random_number:
            correct_guess = True
        elif number > random_number:
            print("Too high, guess again")
        elif number < random_number:
            print("Too low, guess again")
    except:
        print("Please enter a number")

print("You guessed the right number!")

