import sys

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget to encrypt/decrypt?")
    sys.exit(1)

shift_factor = 13

def gen_alphabet():
    alphabet = {}
    alphabet_rev = {}
    for x in range(0,26):
        value = x + 65
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

alphabet, alphabet_rev = gen_alphabet()
data = input("Input text to cipher:")

if mode == "encrypt":
    cipher_text = ""
    for x in data:
        letter = encrypt(x)
        cipher_text += letter
    print(cipher_text)
elif mode == "decrypt":
    plain_text = ""
    for x in data:
        letter = decrypt(x)
        plain_text += letter
    print(plain_text)
