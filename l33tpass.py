#!/usr/bin/python3
# David Lane @phi10s - Scorpion Labs
# Generates a list of weak credential pairs for password attacks with passwords based on
# customizable leetspeak mutations of the usernames. Contains a default leet dictionary
# that can be modified by command line arguments.

import argparse

def leetspeak(username, leet_dict, include=None, exclude=None):
    if include:
        leet_dict = {char: leet_dict[char] for char in include if char in leet_dict}
    elif exclude:
        leet_dict = {char: value for char, value in leet_dict.items() if char not in exclude}
    
    return ''.join(leet_dict.get(char, char) for char in username)

def generate_passwords(input_file, leet_dict, capitalize=False, append_str='', prepend_str='', separator=':', include=None, exclude=None):
    with open(input_file, 'r') as f:
        usernames = f.read().splitlines()
    
    passwords = []
    for username in usernames:
        password = leetspeak(username, leet_dict, include, exclude)
        if capitalize:
            password = password[0:1].capitalize() + password[1:]
        password = f"{prepend_str}{password}{append_str}"
        passwords.append(f"{username}{separator}{password}")
    
    return passwords

def write_output(output_file, passwords):
    if output_file:
        with open(output_file, 'w') as f:
            for line in passwords:
                f.write(f"{line}\n")
    else:
        for line in passwords:
            print(line)

def parse_leet_dict(custom=None):
    leet_dict = {
        'a': '@', 'b': '8', 'e': '3', 'g': '6', 'i': '1', 'l': '1',
        'o': '0', 's': '5', 't': '7', 'z': '2', 'A': '4', 'B': '8',
        'E': '3', 'G': '6', 'I': '1', 'L': '1', 'O': '0', 'S': '5',
        'T': '7', 'Z': '2'
    }

    if custom:
        for pair in custom:
            key, value = pair.split(':')
            leet_dict[key] = value

    return leet_dict

def main():
    parser = argparse.ArgumentParser(
        description="Generate leetspeak passwords from a list of usernames.\n\n"
                    "Default leetspeak dictionary:\n"
                    "{'a': '@', 'b': '8', 'e': '3', 'g': '6', 'i': '1', 'l': '1',\n"
                    "'o': '0', 's': '5', 't': '7', 'z': '2', 'A': '4', 'B': '8',\n"
                    "'E': '3', 'G': '6', 'I': '1', 'L': '1', 'O': '0', 'S': '5',\n"
                    "'T': '7', 'Z': '2'}",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('input_file', help="File containing usernames, one per line.")
    parser.add_argument('-o', '--output_file', help="Output file to write the username:password pairs. If not provided, output is printed.")
    parser.add_argument('-c', '--capitalize', action='store_true', help="Capitalize the first letter of the password.")
    parser.add_argument('-a', '--append', type=str, default='', help="String to append to the end of each password.")
    parser.add_argument('-p', '--prepend', type=str, default='', help="String to prepend to the beginning of each password.")
    parser.add_argument('-s', '--separator', type=str, default=':', help="Separator to use between username and password (default is ':').")
    parser.add_argument('-i', '--include', type=str, nargs='+', help="List of keys to include in the leetspeak replacements.")
    parser.add_argument('-e', '--exclude', type=str, nargs='+', help="List of keys to exclude from the leetspeak replacements.")
    parser.add_argument('-u', '--custom', type=str, nargs='+', help="List of custom key:value pairs to modify the leetspeak dictionary.")

    args = parser.parse_args()

    leet_dict = parse_leet_dict(args.custom)
    passwords = generate_passwords(args.input_file, leet_dict, args.capitalize, args.append, args.prepend, args.separator, args.include, args.exclude)
    write_output(args.output_file, passwords)

if __name__ == "__main__":
    main()

