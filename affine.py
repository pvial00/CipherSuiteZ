import sys

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget encrypt/decrypt?")
    sys.exit(1)

def gen_alphabet():
    alphabet = {}
    alphabet_rev = {}
    for x in range(0,26):
        alphabet[chr(x + 65)] = x
        alphabet_rev[x] = chr(x + 65)
    return alphabet, alphabet_rev

def affine_encrypt(words):
    cipher_text = ""
    for word in words.split():
        for letter in word:
            num = alphabet[letter]
            num = ((num * 5) + 8) % 26
            sub = alphabet_rev[num]
            cipher_text += sub
    return cipher_text

def affine_decrypt(words):
    plain_text = ""
    for word in words.split():
        for letter in word:
            num = alphabet[letter]
            num = (21 * (num - 8)) % 26
            sub = alphabet_rev[num]
            plain_text += sub
    return plain_text

words = input("Enter text to cipher: ")
alphabet, alphabet_rev = gen_alphabet()
if mode == "encrypt":
    cipher_text = affine_encrypt(words)
    print(cipher_text)
elif mode == "decrypt":
    plain_text = affine_decrypt(words)
    print(plain_text)
