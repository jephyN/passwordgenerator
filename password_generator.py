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
    return random.choice(sequence)


def add_element(elements: list, element):
    elements.append(element)


def print_error():
    print('Please enter a correct value')


def add_valid_option(password_options: list, input_option, name):
    if input_option in ('y', 'Y'):
        add_element(password_options, name)
    elif input_option not in ('n', 'N'):
        print_error()
        return False
    return True


def interact_main_menu(choice=''):
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
    characters = []
    for i in range(length):
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
