import sys

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

def gen_alphabets():
    alphabet = {}
    alphabet_rev = {}
    for y, x in enumerate(reversed(range(65,91))):
        alphabet[chr(y + 65)] = chr(x)
        alphabet_rev[chr(x)] = chr(y + 65)
    return alphabet, alphabet_rev

def encipher(words):
    cipher_text = ""
    for word in words.split():
        for letter in word:
            sub = alphabet[letter]
            cipher_text += sub
    return cipher_text

def decipher(words):
    plain_text = ""
    for word in words.split():
        for letter in word:
            sub = alphabet_rev[letter]
            plain_text += sub
    return plain_text

alphabet, alphabet_rev = gen_alphabets()
if mode == "encrypt":
    words = raw_input("Enter text to cipher: ")
    cipher_text = encipher(words)
    print cipher_text
elif mode == "decrypt":
    words = raw_input("Enter text to cipher: ")
    plain_text = decipher(words)
    print plain_text
