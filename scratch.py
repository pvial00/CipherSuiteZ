import sys, getpass

mode = sys.argv[1]

def gen_alphabet():
    global alphabet_dict
    global alphabet
    global sub_alphabet
    alphabet_dict = {}
    alphabet = []
    sub_alphabet = []
    for x in range(0,26):
        alphabet_dict
    for y in range(65,91):
        alphabet.append(chr(y))
        sub_alphabet.append(chr(y))
    for x in range(0,26):
        letter = alphabet.pop(0)
        alphabet_dict[letter] = x
        alphabet.append(letter)

def key_alphabet():
    for element in key:
        key_value = alphabet_dict[element]
        for x in range(0,key_value):
            shift = sub_alphabet.pop(key_value)
            sub_alphabet.append(shift)

def permute():
    shift = sub_alphabet.pop(25)
    sub_alphabet.insert(0,shift)

def encrypt(text):
    cipher_text = ""
    for letter in text:
        pos = alphabet.index(letter)
        sub = sub_alphabet.pop(pos)
        sub_alphabet.insert(pos,sub)
        permute()
        cipher_text += sub
    return cipher_text

def decrypt(text):
    plain_text = ""
    for letter in text:
        pos = sub_alphabet.index(letter)
        sub = alphabet.pop(pos)
        alphabet.insert(pos,sub)
        permute()
        plain_text += sub
    return plain_text

text = raw_input("Enter text to cipher: ")
key = getpass.getpass("Enter key: ")
gen_alphabet()
key_alphabet()

if mode == "encrypt":
    cipher_text = encrypt(text)
    print cipher_text
elif mode == "decrypt":
    plain_text = decrypt(text)
    print plain_text
