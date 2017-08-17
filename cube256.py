import sys, collections, getpass, select

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

if select.select([sys.stdin,],[],[],0.0)[0]:
    words = sys.stdin.read()

try:
    key = sys.argv[4]
except IndexError as ier:
    key = getpass.getpass("Enter key: ")

def gen_alphadict():
    global alphabet_dict
    alphabet_dict = {}
    for x in range(0,256):
        alphabet_dict[x] = x

def key_cube(key):
    for section in master_list:
        for char in key:
            char_value = alphabet_dict[ord(char)]
            section_len = len(section)
            for x in range(section_len):
                alphabet = section.pop(x)
                pos = alphabet.index(ord(char))
                key_sub = alphabet.pop(pos)
                alphabet.append(key_sub)
                for x in range(0,char_value + x):
                    if x % 2 == 0:
                        shuffle = alphabet.pop(0)
                        alphabet.append(shuffle)
                        shuffle = alphabet.pop(2)
                        alphabet.insert(128,shuffle)
                section.insert(x,alphabet)
            for x in range(char_value):
                section = master_list.pop(0)
                newpos = (char_value + (x * 128)) % 256
                master_list.append(section)

def key_scheduler(key):
    sub_key = ""
    for element in key:
        pos = alphabet_dict[ord(element)]
	pos = pos % 16
        section = master_list.pop(pos)
        sub_alpha = section.pop(pos)
        shift = sub_alpha.pop(1)
        sub_alpha.append(shift)
        section.insert(pos,sub_alpha)
        master_list.insert(pos,section)
        sub = sub_alpha.pop(pos)
        sub_alpha.insert(pos,sub)
        sub_key += chr(sub)
    load_key(sub_key)
    return sub_key

def gen_cube(depth, width, length):
    global master_list
    master_list = []
    for z in range(0,depth):
        section_list = []
        for y in range(0,width):
            alphabet = []
            for x in range(0,length):
                alphabet.append(x + 0)
            for mod in range(0,y):
                shift = alphabet.pop(0)
                alphabet.append(shift)
                shift = alphabet.pop(2)
                alphabet.insert(128,shift)
            section_list.append(alphabet)
        master_list.append(section_list)

def morph_cube(counter):
    mod_value = counter % 256
    for key_element in key:
    	key_value = ord(key_element)
    	shift_value = (128 * key_value) % 256
    	for section in master_list:
        	for alphabet in section:
            		shift = alphabet.pop(mod_value)
            		alphabet.insert(shift_value,shift)
    	section_shift = master_list.pop(key_value % 16)
    	master_list.append(section_shift)
            
def encipher(words):
    cipher_text = ""
    sub_key = key
    for word in words:
        for counter, letter in enumerate(word):
            for section in master_list:
                for alphabet in section:
		    keytmp = key_list.pop(0)
		    key_list.append(keytmp)
                    sub_pos = ord(keytmp)
                    sub = alphabet.pop(sub_pos)
                    xor_sub = ord(letter) ^ sub
                    alphabet.insert(sub_pos,sub)
                    shift = alphabet.pop(0)
                    alphabet.append(shift)
            morph_cube(counter)
            sub_key = key_scheduler(sub_key)
            sys.stdout.write(chr(xor_sub))

def load_key(key):
    global key_list
    key_list = []
    for element in key:
        key_list.append(element)
                
load_key(key)
gen_alphadict()
gen_cube(16, 16, 256)
key_cube(key)
if mode == "encrypt":
    encipher(words)
elif mode == "decrypt":
    encipher(words)
