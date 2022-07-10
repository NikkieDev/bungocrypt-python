import random
import string

def create_key():
    """Only use to store your key. If you want to encrypt your data, please use create_key_arr"""
    key_arr_1 = []
    key_arr_2 = []
    key = ""

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = ["!", "@", "#", "$", "(", ")", "*"]
    total = alphabet + numbers + symbols

    for x in range(0, 21):
        key_arr_1.append(random.choice(total))

    for x in range(0, 20):
        key_arr_2.append(random.choice(total))

    key_arr_1.append(".")

    key_arr = key_arr_1 + key_arr_2

    for key_char in key_arr:
        key += key_char

    return key

def create_key_arr():
    """Creates a 42 character key in an array. This key can be used for encrypting and decrypting. Please store this key somewhere safe (use the arr_to_key function to get a storeable string key.), as you will need it for decrypting your data as well. Losing this key will leave your data encrypted forever, and is unrecoverable!"""
    key_str = create_key()
    key_arr = list(key_str)

    return key_arr

def key_to_arr(key: str):
    """Changes your key from string format to an array that can be used to encrypt and decrypt your data. Key must be 42 characters long"""
    key_arr = list(key)

    return key_arr

def arr_to_key(key: list):
    """Changes your key from array to string format that you can store for later use. Key must be 42 characters long"""
    string = ""

    for key_char in key:
        string += key_char

    return string