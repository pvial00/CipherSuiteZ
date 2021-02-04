import collections, sys, getpass

mode = sys.argv[1]

def init_alphabets():
    alphabets = {}
    alphabets_rev = {}
    for z, x in enumerate(range(65,91)):
        alphabet = collections.deque()
        alphabet_dict = {}
        alphabet_dict_rev = {}
        for y in range(65,91):
            alphabet.append(chr(y))
        if z == 0:
            shift_factor = z
        else:
            shift_factor = z * -1
        alphabet.rotate(shift_factor)
        for y in range(65,91):
            letter = alphabet.popleft()
            alphabet_dict[chr(y)] = letter
            alphabet_dict_rev[letter] = chr(y)
        alphabets[chr(x)] = alphabet_dict
        alphabets_rev[chr(x)] = alphabet_dict_rev
    return alphabets, alphabets_rev

def expand_key(key, secret):
    expanded_key = []
    key_copy = []
    for x in range(0,len(key)):
        expanded_key.append(key[x])
        key_copy.append(key[x])
    for x in range(0,len(secret)):
        char = key_copy.pop(0)
        key_copy.append(char)
        expanded_key.append(char)
    expanded_key.reverse()
    return expanded_key

def vigenere_decrypt(alphabets, secret, key):
    cipher_text = ""
    for x in range(0,len(secret)):
        keyi = key.pop()
        key.insert(0,keyi)
        sub_dict = alphabets_rev[keyi]
        sub = sub_dict[secret[x]]
        cipher_text = cipher_text + sub
    return cipher_text

def vigenere_encrypt(alphabets, secret, key):
    cipher_text = ""
    for x in range(0,len(secret)):
        keyi = key.pop()
        key.insert(0,keyi)
        sub_dict = alphabets[keyi]
        sub = sub_dict[secret[x]]
        cipher_text = cipher_text + sub
    return cipher_text
	

data = input("Enter text to cipher: ")
key = getpass.getpass("Enter key: ")
alphabets, alphabets_rev = init_alphabets()
expanded_key = expand_key(key, data)
if mode == "encrypt":
    cipher_text = vigenere_encrypt(alphabets, data, expanded_key)
    print(cipher_text)
elif mode == "decrypt":
    plain_text = vigenere_decrypt(alphabets, data, expanded_key)
    print(plain_text)
