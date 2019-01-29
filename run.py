#!/usr/bin/env python3

from secrets import choice
from random import randrange
import string

def generate_pwd():
    pwd_len = randrange(8, 16)
    selection = string.ascii_letters + string.digits + string.punctuation

    return ''.join(choice(selection) for i in range(pwd_len))

if __name__ == "__main__":
    print(f"Your randomly generated password is: { generate_pwd() }")
