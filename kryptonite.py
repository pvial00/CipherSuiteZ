import sys, time, os
from getpass import getpass

rounds = 16

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

try:
    in_file = sys.argv[2]
except IndexError as ier:
    print "Error: input file is missing"
    sys.exit(1)

try:
    out_file = sys.argv[3]
except IndexError as ier:
    print "Error: output file is missing"
    sys.exit(1)

def gen_session_key(session_key_length):
	session_key = ""
	for key in range(0,session_key_length):
		session_key = session_key + os.urandom(1)
	return session_key

def key_scheduler(key):
    sub_key = ""
    for element in key:
        key_value = ord(element) ^ ord(element) ^ 13
        sub_key += chr(key_value)
    return sub_key

def split_data(data):
    left = []
    right = []
    split = len(data) / 2
    for x in range(split):
        left.append(data[x])
    for x in range(len(data)):
        right.append(data[x])
    return left, right


def krypt_block(block, key):
    left, right = split_data(block)
    crypt_text = ""
    newleft = ""
    newright = ""
    for byte in right:
        newleft += byte
    for byte in left:
	primary_round = ord(byte)
	for y in range(0,len(key)):
		primary_round = primary_round ^ ord(key[y])
		crypt_text = crypt_text + chr(primary_round)
	return newleft + newright

def krypt(text, key):
	crypt_text = ""
	for x in range(0,len(text)):
		byte = text[x]
		primary_round = ord(byte)
		for y in range(0,len(key)):
			primary_round = primary_round ^ ord(key[y])
		crypt_text = crypt_text + chr(primary_round)
	return crypt_text

def dual_krypt(text, key1, key2):
	crypt_text = ""
	for x in range(0,len(text)):
		byte = text[x]
		primary_round = ord(byte)
		for y in range(0,len(key1)):
			primary_round = primary_round ^ ord(key1[y])
                for z in range(0,len(key2)):
                    primary_round = primary_round ^ ord(key2[z])
		crypt_text = crypt_text + chr(primary_round)
	return crypt_text

def krypto_pack(plain_text, key):
	session_key = gen_session_key(session_key_length)
	krypt_pkt = krypt(plain_text, session_key)
	krypt_pkt = session_key + krypt_pkt
	krypt_pkt = krypt(krypt_pkt, key)
	return krypt_pkt

def krypto_unpack(cipher_text, key):
	plain_text = ""
	session_key = ""
	second_stage = ""
	first_stage = krypt(cipher_text, key)
	first_stage_len = len(cipher_text)
	for x in range(0,session_key_length):
		session_key = session_key + first_stage[x]
	for x in range(session_key_length,first_stage_len):
		second_stage = second_stage + first_stage[x]
	plain_text = krypt(second_stage, session_key)
	return plain_text

def block_data(data):
    blocks = []
    block = ""
    for byte in data:
        if len(block) == 16:
            blocks.append(block)
            block = ""
        block += byte
    if block != 16:
        blocks.append(block)
    return blocks

def encrypt(blocks, rounds, key):
    sub_key = key
    phase1 = ""
    for x in range(len(blocks)):
        block = blocks.pop(0)
        for r in range(0,rounds):
               sub_key = key_scheduler(sub_key)
               if len(block) < blocksize:
                    block = pad_block(block, blocksize)
               k_block = krypt_block(block, sub_key)
        phase1 += k_block
    return phase1

def decrypt(blocks, rounds, key):
    sub_key = key
    phase1 = ""
    for x in range(len(blocks)):
        block = blocks.pop(0)
        for r in range(0,rounds):
               sub_key = key_scheduler(sub_key)
               k_block = krypt_block(block, sub_key)
               #if x == (len(blocks) - 1):
               k_block = unpad_block(k_block, blocksize)
        phase1 += k_block
    return phase1

def pad_block(block, blocksize):
    pad_string = chr(4)
    for x in range(0, blocksize - len(block)):
        block = block + pad_string
    return block

def unpad_block(block, blocksize):
    pad_string = chr(4)
    pad_block = ""
    pad_count = block.count(pad_string)
    for x in range(len(block) - pad_count):
        pad_block += block[x]
    return pad_block


try:
	infile = open(in_file, "r")
except NameError as ner:
	print "Unable to open infile"
	sys.exit(0)

try:
	outfile = open(out_file, "w")
except NameError as ner:
	print "Unable to open outfile"
	sys.exit(0)

try:
	key = sys.argv[4]
except IndexError:
	key = getpass("Enter key: ")

blocksize = 16
filesize = os.path.getsize(in_file)
num_blocks = filesize / blocksize
odd_size = filesize % blocksize
if odd_size != 0:
    num_blocks += 1

data = infile.read()
infile.close()
session_key_length =  16 # 16 for 128 bit, 32 for 256 bit, 128 for 1024 bit, 256 for 2048 

start_time = time.time()
if mode == "encrypt":
        blocks = block_data(data)
        phase1 = encrypt(blocks, rounds, key)
	phase2 = krypto_pack(phase1, key)
	outfile.write(phase2)
elif mode == "decrypt":
	phase1 = krypto_unpack(data, key)
        blocks = block_data(phase1)
        phase2 = decrypt(blocks, rounds, key)
	outfile.write(phase2)

end_time = time.time() - start_time
print "Completed in %s seconds" % end_time
outfile.close()
