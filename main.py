import base64
import json
import os
import random
import string
import sys

usernames_and_passwords = {}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_password():
    clear()
    print('Generate Password Menu')
    print('-------------------------------------')
    print('Enter the length of password: (Enter \'0\' to exit menu)')
    length = int(input())
    if length == 0:
        main()
    characters = list(string.ascii_letters +
                      string.digits + string.punctuation)
    random.shuffle(characters)
    characters = ''.join(characters)
    password = random.sample(characters, length)
    random.shuffle(password)
    print('Password:')
    print(''.join(password))
    input('Press \'Enter\' to continue...')
    main()


def add_password():
    clear()
    print('Add Password Menu')
    print('-------------------------------------')
    print('Enter the website address or application name: (Enter \'0\' to exit menu)')
    website = str(input())
    if website == '0':
        main()
    print('Enter your username: (Enter \'0\' to exit menu)')
    username = str(input())
    if username == '0':
        main()
    print('Enter your password: (Enter \'0\' to exit menu)')
    password = str(input())
    if password == '0':
        main()
    password = base64.b64encode(password.encode("utf-8")).decode("utf-8")
    usernames_and_passwords[website] = [username, password]
    with open('passwords.json', 'w') as file:
        file.write(json.dumps(usernames_and_passwords))
    print('Done')
    input('Press \'Enter\' to continue...')
    main()


def change_website():
    clear()
    print('Change Website address/Application name Menu')
    print('-------------------------------------')
    print('Enter the website address or application name: (Enter \'0\' to exit menu)')
    website = str(input())
    if website == '0':
        main()
    print('Enter new website address or application name: (Enter \'0\' to exit menu)')
    new_website = str(input())
    if new_website == '0':
        main()
    usernames_and_passwords[new_website] = [usernames_and_passwords.get(
        website)[0], usernames_and_passwords.get(website)[1]]
    usernames_and_passwords.pop(website)
    with open('passwords.json', 'w') as file:
        file.write(json.dumps(usernames_and_passwords))
    print('Done')
    input('Press \'Enter\' to continue...')
    main()


def change_password():
    clear()
    print('Change Password Menu')
    print('-------------------------------------')
    print('Enter the website address or application name: (Enter \'0\' to exit menu)')
    website = str(input())
    if website == '0':
        main()
    if website not in usernames_and_passwords:
        print('This website/application not exist.')
        str(input('Press \'Enter\' to continue...'))
        change_password()
    print('Enter your new password: (Enter \'0\' to exit menu)')
    password = str(input())
    if password == '0':
        main()
    password = base64.b64encode(password.encode("utf-8")).decode("utf-8")
    usernames_and_passwords[website] = [
        usernames_and_passwords.get(website)[0], password]
    with open('passwords.json', 'w') as file:
        file.write(json.dumps(usernames_and_passwords))
    print('Done')
    input('Press \'Enter\' to continue...')
    main()


def change_username():
    clear()
    print('Change Username Menu')
    print('-------------------------------------')
    print('Enter the website address or application name: (Enter \'0\' to exit menu)')
    website = str(input())
    if website == '0':
        main()
    if website not in usernames_and_passwords:
        print('This website/application not exist.')
        str(input('Press \'Enter\' to continue...'))
        change_username()
    print('Enter your new username: (Enter \'0\' to exit menu)')
    username = str(input())
    if username == '0':
        main()
    usernames_and_passwords[website] = [
        username, usernames_and_passwords.get(website)[1]]
    with open('passwords.json', 'w') as file:
        file.write(json.dumps(usernames_and_passwords))
    print('Done')
    input('Press \'Enter\' to continue...')
    main()


def remove_password():
    clear()
    print('Remove Password Menu')
    print('-------------------------------------')
    print('Enter the website address or application name: (Enter \'0\' to exit menu)')
    website = str(input())
    if website == '0':
        main()
    if website not in usernames_and_passwords:
        print('This website/application not exist.')
        str(input('Press \'Enter\' to continue...'))
        remove_password()
    usernames_and_passwords.pop(website)
    with open('passwords.json', 'w') as file:
        file.write(json.dumps(usernames_and_passwords))
    print('Done')
    input('Press \'Enter\' to continue...')
    main()


def all_usernames_and_passwords():
    clear()
    print('All Usernames And Passwords Menu')
    print('-------------------------------------')
    for key in usernames_and_passwords:
        print('Website: ' + key + ' => Username: ' +
              usernames_and_passwords.get(key)[0] + ' | Password: ' + base64.b64decode(usernames_and_passwords.get(key)[1]).decode("utf-8"))
    input('Press \'Enter\' to continue...')
    main()


def remove_all_usernames_and_passwords():
    usernames_and_passwords.clear()
    with open('passwords.json', 'w') as file:
        file.write('{}')
    print('All usernames and passwords deleted.')
    input('Press \'Enter\' to continue...')
    main()


all_functions = [generate_password, add_password, change_website, change_username, change_password,
                 remove_password, all_usernames_and_passwords, remove_all_usernames_and_passwords]


def main():
    global usernames_and_passwords
    with open('passwords.json', 'r') as file:
        usernames_and_passwords = json.load(file)
    clear()
    print('Welcome to password manager')
    print('-------------------------------------')
    print('Please chose one (1-8): (\'0\' to exit)')
    print('1. Generate password')
    print('2. Add password')
    print('3. Change website address/application name')
    print('4. Change username')
    print('5. Change password')
    print('6. Remove password')
    print('7. Show all usernames and passwords')
    print('8. Remove all usernames and passwords')
    number = int(input())
    if number == 0:
        sys.exit(0)
    all_functions[number-1]()


if __name__ == "__main__":
    main()
