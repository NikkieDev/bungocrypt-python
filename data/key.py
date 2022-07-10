import random
import string

def create_key():
    key_arr_1 = []
    key_arr_2 = []
    key = ""

    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
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