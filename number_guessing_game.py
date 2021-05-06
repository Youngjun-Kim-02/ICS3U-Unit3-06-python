#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program checks if guessed number is correct or incorrect


import random

def main():
    # this function checks if guessed number is correct or incorrect

    # input
    print("Can you guess the number I choose from 0 to 9?")
    integer_as_string = input("Enter the guessed number: ")
    print("")

    # process & output
    some_number = random.randint(0, 9) # a number between 0 and 9
    try:
        integer_as_number = int(integer_as_string)

        if integer_as_number == some_number:
            print("Correct!")
        else:
            print("Incorrect, the number was: {0}".format(some_number))
    except:
        print("That was not an integer.")
    finally:
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
