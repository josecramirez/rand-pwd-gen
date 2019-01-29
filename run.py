#!/usr/bin/env python3

from secrets import choice
from random import randrange
import string

def generate_pwd():
    pwd_len = randrange(8, 16)
    selection = string.ascii_letters + string.digits + string.punctuation

    return ''.join(choice(selection) for i in range(pwd_len))

def validate_pwd(pwd):
    if (any(c.isupper() for c in pwd)
            and any(c.islower() for c in pwd)
            and any(c.isdigit() for c in pwd)
            and any(is_symbol(c) for c in pwd)):
        return True

    return False

def is_symbol(char):
    return (True if char in string.punctuation else False)

if __name__ == "__main__":
    gen_pwd = ''

    while not validate_pwd(gen_pwd):
        gen_pwd = generate_pwd()

    print(f"Your password is: { gen_pwd }")
