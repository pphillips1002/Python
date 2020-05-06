import sys
import random


def main():
    """Chooses random names from tuples and prints to the screen"""
    print("Welcome to the Pseudonym Generator!")
    # tuples for first and last names
    first = ('Jeffrey', 'Ayesha', 'Pierce', 'Ashlynne', 'Joe')
    last = ('MacDonald', 'Carnes', 'Phillips', 'Exotic', 'Bailey')
    while True:
        # choosing random names from tuples
        first_name = random.choice(first)
        last_name = random.choice(last)
        # printing pseudonym to std.err
        print(f"Your pseudonym is: {first_name} {last_name}")
        # asking the user to continue
        game = input("Do you want to play again? Y/N\n")
        if game.lower() == 'n':
            break


if __name__ == '__main__':
    main()
