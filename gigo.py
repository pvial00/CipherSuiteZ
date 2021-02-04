import sys, random

mode = sys.argv[1]
shift_factor = 13

def gen_alphabet():
    alphabet = {}
    alphabet_rev = {}
    for x in range(1,27):
        value = x + 64
        alphabet[x] = chr(value)
        alphabet_rev[chr(value)] = x
    return alphabet, alphabet_rev

def encrypt(cipher_text):
    plain_text = ""
    num_value = alphabet_rev[cipher_text]
    encoded_num = (num_value % 26) + shift_factor
    if encoded_num < 0:
        encoded_num = encoded_num + 26
    elif encoded_num > 26:
        encoded_num = encoded_num - 26
    letter = alphabet[encoded_num]
    return letter

def decrypt(cipher_text):
    plain_text = ""
    num_value = alphabet_rev[cipher_text]
    decoded_num = (num_value % 26) - shift_factor
    if decoded_num < 0:
        decoded_num  = decoded_num + 26
    elif decoded_num > 26:
        decoded_num = decoded_num - 26
    letter = alphabet[decoded_num]
    return letter

def garbage_in(cipher_text):
    garbage = ""
    for char in cipher_text:
        rand_char = random.randint(65,91)
        garbage += char + chr(rand_char)
    return garbage

def garbage_out(dirty_text):
    clean_text = ""
    for x, char in enumerate(dirty_text):
        if x % 2 == 0:
            clean_text += char
    return clean_text
alphabet, alphabet_rev = gen_alphabet()
data = input("Input text to cipher:")

if mode == "encrypt":
    cipher_text = ""
    for x in data:
        letter = encrypt(x)
        cipher_text += letter
    garbage = garbage_in(cipher_text)
    print(garbage)
elif mode == "decrypt":
    plain_text = ""
    clean_text = garbage_out(data)
    for x in clean_text:
        letter = decrypt(x)
        plain_text += letter
    print(plain_text)
