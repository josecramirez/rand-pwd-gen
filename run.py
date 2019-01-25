#!/usr/bin/env python3

import random
import string

def generate_pwd():
    pwd = ''
    pwd_len = random.randrange(8, 16)
    selection = string.ascii_letters + string.digits + string.punctuation

    for i in range(pwd_len):
        pwd += random.choice(selection)

    return pwd

if __name__ == "__main__":
    print(f"Your randomly generated password is: { generate_pwd() }")
