import sys

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget encrypt/decrypt?")
    sys.exit(1)

shift_factor = 128

def cyfr_encrypt(data):
    cipher_text = ""
    for ctr, letter in enumerate(data):
        sub = (ord(letter) + shift_factor) + ctr * ctr
        cipher_text += str(sub) + " "
    return cipher_text

def cyfr_decrypt(data):
    plain_text = ""
    for ctr, num in enumerate(data.split()):
        plain_text += chr((int(num) - shift_factor) - ctr * ctr)
    return plain_text

data = input("Enter text to cipher:")

if mode == "encrypt":
    cipher_text = cyfr_encrypt(data)
    print(cipher_text)
elif mode == "decrypt":
    plain_text = cyfr_decrypt(data)
    print(plain_text)
