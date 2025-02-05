import string
import sys
import random

menu = '''
-- Password generator --
Choose option:
1: generate password
2: exit the program
Your choice: '''
choice = ''


def pick(sequence):
    return random.choice(sequence)


def add_element(elements: list, element):
    elements.append(element)


def print_error():
    print('Please enter a correct value')


def interact_main_menu():
    global choice
    while choice != '2':
        choice = input(menu)
        if choice == '1':
            options = [0]
            try:
                length = int(input('Provide password length:'))
            except ValueError:
                print_error()
                continue
            uppercase = input('Use uppercase letters? (y/n):').strip()
            if uppercase in ('y', 'Y'):
                add_element(options, 1)
            elif uppercase not in ('n', 'N'):
                print_error()
                continue
            digit = input('Use digits? (y/n):').strip()
            if digit in ('y', 'Y'):
                add_element(options, 2)
            elif digit not in ('n', 'N'):
                print_error()
                continue
            special_character = input('Use special characters? (y/n):').strip()
            if special_character in ('y', 'Y'):
                add_element(options, 3)
            elif special_character not in ('n', 'N'):
                print_error()
                continue
            characters = []
            for i in range(length):
                option = pick(options)

                match option:
                    case 0:
                        add_element(characters, pick(string.ascii_lowercase))
                    case 1:
                        add_element(characters, pick(string.ascii_uppercase))
                    case 2:
                        add_element(characters, pick(string.digits))
                    case 3:
                        add_element(characters, pick('!@#$%&^|()_+'))

            password = ''.join(characters)
            print('Generate password: ', password)
        elif choice == '2':
            print('Bye!')
            sys.exit()
        else:
            print_error()


if __name__ == '__main__':
    interact_main_menu()
