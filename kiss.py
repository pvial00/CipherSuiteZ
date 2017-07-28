import sys, getpass

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

def gen_alphabets():
    alphabet = {}
    alphabet_prime = {}
    for x in range(65,91):
        alphabet[chr(x)] = chr(x)
        alphabet_prime[chr(x)]= chr(x)
    return alphabet, alphabet_prime

def key_alphabet(alphabet, key):
    key_length = len(key)
    alphabet_rev = dict(alphabet)
    for x, letter in enumerate(range(65,91)):
        if x < key_length:
            alphabet[chr(letter)] = key[x]
            alphabet[key[x]] = chr(letter)
            alphabet_rev[key[x]] = chr(letter)
            alphabet_rev[chr(letter)] = key[x]
    return alphabet, alphabet_rev

words = raw_input("Enter text to cipher: ")
key = getpass.getpass("Enter key: ")

alphabet, alphabet_prime = gen_alphabets()
keyed_alphabet, keyed_alphabet_rev = key_alphabet(alphabet_prime, key)
if mode == "encrypt":
    cipher_text = ""
    for letter in words:
        sub = keyed_alphabet[letter]
        cipher_text += sub
    print cipher_text
elif mode == "decrypt":
    plain_text = ""
    for letter in words:
        sub = keyed_alphabet_rev[letter]
        plain_text += sub
    print plain_text
