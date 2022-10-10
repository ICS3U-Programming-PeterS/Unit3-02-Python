#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: October 5, 2022
# This program asks the user for a random number from
# 0 to 9 and checks if it is the correct number
import constants


def main():
    # get random number
    random_number = int(input("Enter a number from 0 to 9: "))

    # if random_number == CORRECT_NUMBER
    if random_number == constants.CORRECT_NUMBER:
        print("You guessed correctly!")

    # if random_number != CORRECT_NUMBER
    if random_number != constants.CORRECT_NUMBER:
        print("You guessed wrong :(")


if __name__ == "__main__":
    main()
