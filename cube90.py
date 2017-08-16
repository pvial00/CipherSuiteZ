import sys, collections, getpass, select

start_char = 32
end_char = 91

if select.select([sys.stdin,],[],[],0.0)[0]:
    words = sys.stdin.read()
else:
    words = raw_input("Enter text to cipher: ")

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

try:
    key = sys.argv[2]
except IndexError as ier:
    key = getpass.getpass("Enter key: ")

def gen_alphadict():
    global alphabet_dict
    global alphabet_dict_rev
    alphabet_dict = {}
    alphabet_dict_rev = {}
    for x in range(0,end_char):
        alphabet_dict[chr(x + start_char)] = x
        alphabet_dict_rev[x] = chr(x + start_char)

def key_cube(key):
    for section in master_list:
        for char in key:
            char_value = alphabet_dict[char]
            for alphabet in section:
                pos = alphabet.index(char)
                key_sub = alphabet.pop(pos)
                alphabet.append(key_sub)
                for y in range(0,char_value):
                    if y % 2 == 0:
                        shuffle = alphabet.pop(0)
                        alphabet.append(shuffle)
                        shuffle = alphabet.pop(2)
                        alphabet.insert(45,shuffle)
            for x in range(char_value):
                section = master_list.pop(char_value)
                newpos = (char_value + (x * 128)) % end_char
                master_list.insert(newpos,section)

def key_scheduler(key):
    sub_key = ""
    for element in key:
        pos = alphabet_dict[element]
        section = master_list.pop(pos)
        sub_alpha = section.pop(pos)
        shift = sub_alpha.pop(1)
        sub_alpha.append(shift)
        section.insert(pos,sub_alpha)
        master_list.insert(pos,section)
        sub = sub_alpha.pop(pos)
        sub_alpha.insert(pos,sub)
        sub_key += sub
    load_key(sub_key)
    return sub_key

def gen_cube(length, width, depth):
    global master_list
    master_list = []
    for z in range(0,depth):
        section_list = []
        for y in range(0,width):
            alphabet = []
            for x in range(0,length):
                alphabet.append(chr(x + start_char))
            for mod in range(0,y):
                shift = alphabet.pop(0)
                alphabet.append(shift)
                shift = alphabet.pop(2)
                alphabet.insert(45,shift)
            section_list.append(alphabet)
        master_list.append(section_list)

def morph_cube(counter):
    mod_value = counter % end_char
    for key_element in key:
        key_value = ord(key_element)
        shift_value = (mod_value + key_value) % end_char
        for section in master_list:
            for alphabet in section:
                shift = alphabet.pop(mod_value)
                alphabet.insert(shift_value,shift)
        section_shift = master_list.pop(key_value)
        master_list.append(section_shift)
            
def encipher(words):
    sub_key = key
    for word in words:
        for counter, letter in enumerate(word):
            for section in master_list:
                for alphabet in section:
                    sub_pos = alphabet_dict[letter]
                    sub = alphabet.pop(sub_pos)
                    alphabet.insert(sub_pos,sub)
                    shift = alphabet.pop(0)
                    alphabet.append(shift)
            morph_cube(counter)
            sub_key = key_scheduler(sub_key)
            sys.stdout.write(sub)

def decipher(words):
    sub_key = key
    for word in words:
        for counter, letter in enumerate(word):
            for section in master_list:
                for alphabet in section:
                    sub_pos = alphabet.index(letter)
                    sub = alphabet_dict_rev[sub_pos]
                    shift = alphabet.pop(0)
                    alphabet.append(shift)
            morph_cube(counter)
            sub_key = key_scheduler(sub_key)
            sys.stdout.write(sub)

def load_key(key):
    global key_list
    key_list = []
    for element in key:
        key_list.append(element)
                
load_key(key)
gen_alphadict()
gen_cube(90, 90, 90)
key_cube(key)
if mode == "encrypt":
    cipher_text = encipher(words)
    sys.stdout.write("\n")
elif mode == "decrypt":
    plain_text = decipher(words)
    sys.stdout.write("\n")
