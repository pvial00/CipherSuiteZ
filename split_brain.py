import sys, getpass

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

def split_data(data):
    data_len = len(data)
    split_point = len(data) / 2
    left = []
    right = []
    for x in range(0,split_point):
        left.append(data[x])
    left.reverse()
    for x in range(split_point,data_len):
        right.append(data[x])
    right.reverse()
    return left, right

def encrypt_left(block):
    brain_block = ""
    key_copy = keys[:]
    for char in block:
        key_char = key_copy.pop(0)
        key_copy.append(key_char)
        key_sub = ord(key_char) % 3
        calc = ord(char) + key_sub
        brain_block += chr(calc)
    return brain_block

def encrypt_right(block):
    brain_block = ""
    key_copy = keys[:]
    for char in block:
        key_char = key_copy.pop(0)
        key_copy.append(key_char)
        key_sub = ord(key_char) % 3
        calc = ord(char) + key_sub + 1
        brain_block += chr(calc)
    return brain_block

def decrypt_left(block):
    brain_block = ""
    key_copy = keys[:]
    for char in block:
        key_char = key_copy.pop(0)
        key_copy.append(key_char)
        key_sub = ord(key_char) % 3
        calc = ord(char) - key_sub
        brain_block += chr(calc)
    return brain_block

def decrypt_right(block):
    brain_block = ""
    key_copy = keys[:]
    for char in block:
        key_char = key_copy.pop(0)
        key_copy.append(key_char)
        key_sub = ord(key_char) % 3
        calc = ord(char) - key_sub - 1
        brain_block += chr(calc)
    return brain_block

def key_list(key):
    keys = []
    for x in key:
        keys.append(x)
    return keys

key = "a"
keys = key_list(key)
data = raw_input("Enter text to cipher: ")
if mode == "encrypt":
    left, right = split_data(data)
    cipher_left = encrypt_left(left)
    cipher_right = encrypt_right(right)
    cipher_text = cipher_left + cipher_right
    print cipher_text
elif mode == "decrypt":
    left, right = split_data(data)
    plain_left = decrypt_left(left)
    plain_right = decrypt_right(right)
    plain_text = plain_left + plain_right
    print plain_text
