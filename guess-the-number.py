import random
import math as m


def no_guess(a : int, b : int):
    print("Welcome to the Game Named Guess the Number")
    if a < 0 or b < 0 :
        print("Please enter a number greater than 0")
        return


    chance = m.ceil(m.log2(b - a))
    chosen_number = random.randint(a,b)
    print(f"The game master has chosen the number between {a} and {b}.")

    no_of_chances = 0

    while no_of_chances < chance:
        user_guess = int(input("Please enter a number:"))

        no_of_chances += 1

        if user_guess > b or user_guess < a:
            print("your guess is out of range")
            continue

        if user_guess == chosen_number:
            print(f"You guessed the number Congratulations. It was: {chosen_number}. \n"
                  f"You took {no_of_chances} chances out of {chance}.")
            break

        elif user_guess > chosen_number:
            print("Your guess is higher")

        elif user_guess < chosen_number:
            print("Your guess is lower")

    else:
         print("sorry you couldn't guess the number, it was: ", chosen_number)


no_guess(1,100)


