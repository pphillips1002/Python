import sys
import random


def main():
    """Chooses random names from tuples and prints to the screen"""
    print("Welcome to the Pseudonym Generator!")
    # tuples for first and last names
    first = ('jeffrey', 'carnes')
    last = ('carnes', 'jeffrey')

    while True:
        # choosing random names from tuples
        firstName = random.choice(first)
        lastName = random.choice(last)
        # printing psuedonym to std.out
        print(f"Your pseudonym is: {firstName} {lastName}")
        # asking the user to continue
        game = input("Do you want to play again? Y/N\n")
        if game.lower() == 'n':
            break


if __name__ == '__main__':
    main()
