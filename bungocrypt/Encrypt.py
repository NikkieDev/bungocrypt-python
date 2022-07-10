import random

def encrypt(data, key):
    if len(key) != 42:
        raise "KeyLengthError: Your key must be 42 characters long!"

    encrypted_str = str("")
    to_encrypt = list(data.lower())

    if key is None:
        return TypeError

    string = "%++++++====#$$!$!#@$@#@!"
    string_array = list(string)

    encr_pos = random.randint(0, 24)

    for char in to_encrypt:
        if (char == "a"):
            encrypted_str += key[0]
        elif (char == "b"):
            encrypted_str += key[1]
        elif (char == "c"):
            encrypted_str += key[2]
        elif (char == "d"):
            encrypted_str += key[3]
        elif (char == "e"):
            encrypted_str += key[4]
        elif (char == "f"):
            encrypted_str += key[5]
        elif (char == "g"):
            encrypted_str += key[6]
        elif (char == "h"):
            encrypted_str += key[7]
        elif (char == "i"):
            encrypted_str += key[8]
        elif (char == "j"):
            encrypted_str += key[9]
        elif (char == "k"):
            encrypted_str += key[10]
        elif (char == "l"):
            encrypted_str += key[11]
        elif (char == "m"):
            encrypted_str += key[12]
        elif (char == "n"):
            encrypted_str += key[13]
        elif (char == "o"):
            encrypted_str += key[14]
        elif (char == "p"):
            encrypted_str += key[15]
        elif (char == "q"):
            encrypted_str += key[16]
        elif (char == "r"):
            encrypted_str += key[17]
        elif (char == "s"):
            encrypted_str += key[18]
        elif (char == "t"):
            encrypted_str += key[19]
        elif (char == "u"):
            encrypted_str += key[20]
        elif (char == "v"):
            encrypted_str += key[21]
        elif (char == "w"):
            encrypted_str += key[21]
        elif (char == "x"):
            encrypted_str += key[23]
        elif (char == "y"):
            encrypted_str += key[24]
        elif (char == "z"):
            encrypted_str += key[25]
        elif (char == "1"):
            encrypted_str += key[26]
        elif (char == "2"):
            encrypted_str += key[27]
        elif (char == "3"):
            encrypted_str += key[28]
        elif (char == "4"):
            encrypted_str += key[29]
        elif (char == "5"):
            encrypted_str += key[30]
        elif (char == "6"):
            encrypted_str += key[31]
        elif (char == "7"):
            encrypted_str += key[32]
        elif (char == "8"):
            encrypted_str += key[33]
        elif (char == "9"):
            encrypted_str += key[34]
        elif (char == "0"):
            encrypted_str += key[35]
        elif (char == "!"):
            encrypted_str += key[36]
        elif (char == "@"):
            encrypted_str += key[37]
        elif (char == "#"):
            encrypted_str += key[38]
        elif (char == "$"):
            encrypted_str += key[39]
        elif (char == "("):
            encrypted_str += key[40]
        elif (char == ")"):
            encrypted_str += key[41]
        elif (char == "*"):
            encrypted_str += key[42]

        string_array.insert(encr_pos, encrypted_str)

    return_data = encrypted_str # Returns the encrypted string, and data position in the defined string

    return return_data