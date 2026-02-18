"""This module handles password generation."""

import string
import sys
import random

MENU = '''
-- Password generator --
Choose option:
1: generate password
2: exit the program
Your choice: '''


def pick(sequence):
    """Return a random element from the given sequence."""
    return random.choice(sequence)


def add_element(elements: list, element):
    """Append an element to the given list."""
    elements.append(element)


def print_error():
    """Print an error message prompting the user to enter a correct value."""
    print('Please enter a correct value')


def add_valid_option(password_options: list, input_option, name):
    """Add a password option to the list if the user confirmed with 'y' or 'Y'.

        Args:
            password_options (list): The list of active password options.
            input_option (str): The user's input ('y', 'Y', 'n', or 'N').
            name (str): The name of the option to add if confirmed.

        Returns:
            bool: True if the input was valid, False otherwise.
    """
    if input_option in ('y', 'Y'):
        add_element(password_options, name)
    elif input_option not in ('n', 'N'):
        print_error()
        return False
    return True


def interact_main_menu(choice=''):
    """Display the main menu and handle user interaction in a loop until exit."""
    while choice != '2':
        choice = input(MENU)
        if choice == '1':
            options = ["lowercase"]
            try:
                length = int(input('Provide password length:'))
                if length < 1:
                    print_error()
                    continue
            except ValueError:
                print_error()
                continue
            uppercase = input('Use uppercase letters? (y/n):').strip()
            if not add_valid_option(options, uppercase, "uppercase"):
                continue
            digit = input('Use digits? (y/n):').strip()
            if not add_valid_option(options, digit, "digit"):
                continue
            special_character = input('Use special characters? (y/n):').strip()
            if not add_valid_option(options, special_character, "special_character"):
                continue

            password = generate_password(length, options)
            print('Generate password: ', password)
        elif choice == '2':
            print('Bye!')
            sys.exit()
        else:
            print_error()


def generate_password(length, options):
    """Generate a random password based on the specified length and character options.

        Args:
            length (int): The desired length of the password.
            options (list): A list of character types to use (e.g. 'lowercase', 'uppercase',
                            'digit', 'special_character').

        Returns:
            str: The generated password.
    """
    characters = []
    for _ in range(length):
        option = pick(options)
        match option:
            case "lowercase":
                add_element(characters, pick(string.ascii_lowercase))
            case "uppercase":
                add_element(characters, pick(string.ascii_uppercase))
            case "digit":
                add_element(characters, pick(string.digits))
            case "special_character":
                add_element(characters, pick('!@#$%&^|()_+'))
    password = ''.join(characters)
    return password


if __name__ == '__main__':
    interact_main_menu()
