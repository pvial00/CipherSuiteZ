import sys, getpass

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget encrypt/decrypt?")
    sys.exit(1)

shift_factor = 128

def brutus_encrypt(data):
    cipher_text = ""
    for ctr, letter in enumerate(data):
        sub = (ord(letter) + shift_factor) + ctr * ctr
        for char in key:
            sub += ord(char)
        cipher_text += str(sub) + " "
    return cipher_text

def brutus_decrypt(data):
    plain_text = ""
    for ctr, num in enumerate(data.split()):
        keyed_num = int(num)
        for char in key:
            keyed_num = keyed_num - ord(char)
        plain_text += chr((keyed_num - shift_factor) - ctr * ctr)
    return plain_text

data = input("Enter text to cipher:")
key = getpass.getpass("Enter key:")
if mode == "encrypt":
    cipher_text = brutus_encrypt(data)
    print(cipher_text)
elif mode == "decrypt":
    plain_text = brutus_decrypt(data)
    print(plain_text)
