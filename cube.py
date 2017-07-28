import sys, collections, getpass, random

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

def gen_alphadict():
    global alphabet_dict
    global alphabet_dict_rev
    alphabet_dict = {}
    alphabet_dict_rev = {}
    for x in range(0,26):
        alphabet_dict[chr(x + 65)] = x
        alphabet_dict_rev[x] = chr(x + 65)

def key_cube(key):
    for section in master_list:
        for char in key:
            char_value = alphabet_dict[char]
            section_len = len(section)
            for x in range(0,char_value):
                alphabet = section.pop(x)
                pos = alphabet.index(char)
                key_sub = alphabet.pop(pos)
                alphabet.append(key_sub)
                for x in range(0,char_value + x):
                    shuffle = alphabet.pop(0)
                    alphabet.append(shuffle)
                    shuffle = alphabet.pop(2)
                    alphabet.insert(12,shuffle)
                section.insert(x,alphabet)

def gen_cube(length, width, depth):
    global master_list
    master_list = []
    for z in range(0,depth):
        section_list = []
        for y in range(0,width):
            alphabet = []
            for x in range(0,length):
                alphabet.append(chr(x + 65))
            for mod in range(0,y):
                shift = alphabet.pop(0)
                alphabet.append(shift)
                shift = alphabet.pop(2)
                alphabet.insert(12,shift)
            section_list.append(alphabet)
        master_list.append(section_list)
            
def encipher(words):
    cipher_text = ""
    for word in words.split():
        for letter in word:
            for section in master_list:
                for alphabet in section:
                    sub_pos = alphabet_dict[letter]
                    sub = alphabet.pop(sub_pos)
                    alphabet.insert(sub_pos,sub)
                    shift = alphabet.pop(0)
                    alphabet.append(shift)
            cipher_text += sub
    return cipher_text

def decipher(words):
    plain_text = ""
    for word in words.split():
        for letter in word:
            for section in master_list:
                for alphabet in section:
                    sub_pos = alphabet.index(letter)
                    sub = alphabet_dict_rev[sub_pos]
                    shift = alphabet.pop(0)
                    alphabet.append(shift)
            plain_text += sub
    return plain_text
                
words = raw_input("Enter text to cipher: ")
key = getpass.getpass("Enter key: ")
gen_alphadict()
gen_cube(26, 26, 26)
key_cube(key)
if mode == "encrypt":
    cipher_text = encipher(words)
    print cipher_text
elif mode == "decrypt":
    plain_text = decipher(words)
    print plain_text
