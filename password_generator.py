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


def prompt_boolean_input(prompt):
    """Prompt the user for a yes/no input and return it, retrying until valid.

    Args:
        prompt (str): The message to display to the user.

    Returns:
        str: A valid input, either 'y', 'Y', 'n', or 'N'.
    """
    value = input(prompt).strip()
    while value not in ('y', 'Y', 'n', 'N'):
        print_error()
        value = input(prompt).strip()
    return value


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


def get_password_length():
    """Prompt the user for a valid password length and return it.

    Returns:
        int: A positive integer representing the desired password length,
             or None if the input was invalid.
    """
    try:
        length = int(input('Provide password length:'))
        if length < 1:
            print_error()
            return None
    except ValueError:
        print_error()
        return None
    return length


def get_password_options():
    """Prompt the user for password character options and return the selected options.

    Returns:
        list: A list of selected character type options, or None if input was invalid.
    """
    options = ["lowercase"]
    uppercase = prompt_boolean_input('Use uppercase letters? (y/n):')
    if not add_valid_option(options, uppercase, "uppercase"):
        return None
    digit = prompt_boolean_input('Use digits? (y/n):')
    if not add_valid_option(options, digit, "digit"):
        return None
    special_character = prompt_boolean_input('Use special characters? (y/n):')
    if not add_valid_option(options, special_character, "special_character"):
        return None
    return options


def interact_main_menu():
    """Display the main menu and handle user interaction in a loop until exit."""
    choice = ''
    while choice != '2':
        choice = input(MENU)
        if choice == '1':
            length = get_password_length()
            if length is None:
                continue
            options = get_password_options()
            if options is None:
                continue
            password = generate_password(length, options)
            print('Generated password: ', password)
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
