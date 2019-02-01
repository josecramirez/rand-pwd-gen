#!/usr/bin/env python3

from secrets import choice
from random import randrange
import string
import re
import hunspell

def main():
    gen_pwd = ""
    
    while not validate_pwd(gen_pwd):
        gen_pwd = generate_pwd()
        
    print(f"Your password is: { gen_pwd }")

def generate_pwd():
    pwd_len = randrange(8, 16)
    selection = string.ascii_letters + string.digits + string.punctuation

    return ''.join(choice(selection) for i in range(pwd_len))

def validate_pwd(pwd):
    return (any(c.isupper() for c in pwd)
            and any(c.islower() for c in pwd)
            and any(c.isdigit() for c in pwd)
            and any(is_symbol(c) for c in pwd)
            and has_no_words(pwd))

def is_symbol(char):
    return char in string.punctuation

def has_no_words(pwd):
    hobj = hunspell.HunSpell(
        '/usr/share/hunspell/en_US.dic',
        '/usr/share/hunspell/en_US.aff'
    )
    word_regex = r"([a-zA-Z]{2,})"
    results = re.findall(word_regex, pwd)
    
    return not any(hobj.spell(w) for w in results)

if __name__ == "__main__":
    main()
