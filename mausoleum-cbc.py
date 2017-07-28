import collections, sys, time, os
from getpass import getpass
from binascii import hexlify

mode = sys.argv[1]
infile = sys.argv[2]
outfile = sys.argv[3]
blocksize = 8
rounds = 4
iv = 39
hash_iv = 21
cbc_iv = "00000000"
filesize = os.path.getsize(infile)
num_blocks = filesize / blocksize
odd_size = filesize % blocksize
if odd_size != 0:
    num_blocks += 1

def ganja_init_hash(hash, hash_iv):
        for x in range(0,8):
                hash.append(iv)
        return hash

def ganja_hash_round(data, hash):
        for x in range(0,len(data)):
                hash_byte = hash.pop()
                hash_byte = hash_byte ^ ord(data[x])
                hash.insert(0,hash_byte)
        return hash

def ganja_convert_hash_to_hex(hash):
        hex_hash = ""
        for i in range(0,len(hash)):
                hash_byte = hash.pop()
                hex_hash = hex_hash + chr(hash_byte)
        return hex_hash

def key_scheduler(key):
	expanded_key = ""
	hash = []
	ganja_init_hash(hash, hash_iv)
	hash = ganja_hash_round(key, hash)
	expanded_key = ganja_convert_hash_to_hex(hash)
	return expanded_key

def sub_encipher(data):
        newdata = ""
        init = []
        sub_box = []
        primer = collections.deque()
        sub_primer = collections.deque()
        for x in range(0,127):
                primer.append(chr(x))
                sub_primer.append(chr(x))
        sub_primer.rotate(37)
        for x in range(0,127):
                init.append(primer.popleft())
                sub_box.append(sub_primer.popleft())

        for x in range(0,len(data)):
                pos = init.index(data[x])
                sub_pos = sub_box.index(data[x])
                sub = sub_box.pop(pos)
                sub_box.insert(pos, sub)
                newdata = newdata + sub
	return newdata

def split_input(data):
	left = []
	right = []
	middle = len(data) / 2
	for x in reversed(range(0,middle)):
		left.append(data[x])
	for x in reversed(range(middle, len(data))):
		right.append(data[x])
	return left, right

def gen_subkeys(key, rounds):
	sub_keys = []
	for x in range(0,rounds):
		key = sub_encipher(key)
		expanded_key = key_scheduler(key)
		sub_keys.append(expanded_key)
        return sub_keys

def feistel_round(data, key):
	left, right = split_input(data)
	newleft = ""
	newright = ""
	for x in range(0, len(right)):
		newleft = newleft + right.pop()
	for x in range(0, len(left)):
		byte = ord(left.pop())
		for y in range(0, len(key)):
			byte = byte ^ ord(key[y])
		newright = newright + chr(byte)
		
	newdata = newleft + newright
	return newdata

def mod_box(block, blocksize):
	mod_block = ""
	modbox = [ 21, 32, 43, 66, 77, 89, 69, 97]
	for x in range(0,len(block)):
		result = ord(block[x]) ^ modbox.pop()
		mod_block = mod_block + chr(result)
	return mod_block

def cbc_mode(block, last_block):
	cbc_block = ""
	for x in range(0,len(block)):
		byte = ord(block[x]) ^ ord(last_block[x])
		cbc_block += chr(byte)
	return cbc_block

def pad_block(block, blocksize):
	pad_string = chr(4)
	for x in range(0, blocksize - len(block)):
		block = block + pad_string
	return block

def unpad_block(block, blocksize):
	pad_string = chr(4)
	pad_block = ""
	pad_count = block.count(pad_string)
	for x in range(0,(len(block) - pad_count)):
		pad_block += block[x]
	return pad_block
	
try:
	key = sys.argv[4]
except IndexError as ner:
	key = getpass("Enter key: ")

if len(key) < 8:
	print "Error: Keys must be at least 128 bits (8 characters) in length"
	sys.exit(1)

try:
	in_fd = open(infile, "r")
except IOError as ier:
	print "Error: Could not open input file"
	sys.exit(1)

try:
	out_fd = open(outfile, "w")
except IOError as oer:
	print "Error: Could not open output file"

start_time = time.time()
sub_keys = gen_subkeys(key, rounds)
byte_count = 0
sub_keys.reverse()
def encrypt(in_fd, out_fd, sub_keys):
	global byte_count
	global blocksize
	last_block_q = ['00000000']
	last_block = ""
	while True:
		block = in_fd.read(blocksize)
		byte_count = byte_count + len(block)
		if block == "":
			break
		elif len(block) < blocksize:
			block =	pad_block(block, blocksize)
		last_block = last_block_q.pop()
		cbc_block = cbc_mode(block, last_block)
		block = mod_box(cbc_block, blocksize)
		for z in range(0, rounds):
			sub_key = sub_keys.pop()
			sub_keys.insert(0, sub_key)
			block = feistel_round(block, sub_key)
		
		if last_block == "0a0b0c0d":
			#last_block = cbc_iv
			last_block_q.append(block)
		else:
			#last_block = last_block_q.pop()
			last_block_q.append(block)
		out_fd.write(block)

def decrypt(in_fd, out_fd, sub_keys):
	global byte_count
	global blocksize
	last_block = cbc_iv
	last_block_q = ['00000000']
	while True:
		block = in_fd.read(blocksize)
		byte_count = byte_count + len(block)
		if block == "":
			break
		if byte_count == 0:
			last_block_q.append(last_block)
		else:
			last_block = last_block_q.pop()
			last_block_q.append(block)
		for z in range(0, rounds):
			sub_key = sub_keys.pop()
			sub_keys.insert(0, sub_key)
			block = feistel_round(block, sub_key)
		block = mod_box(block, blocksize)
		
		cbc_block = cbc_mode(block, last_block)
                if byte_count / blocksize == num_blocks:
		    cbc_block = unpad_block(cbc_block, blocksize)
		out_fd.write(cbc_block)

if mode == "encrypt":
	encrypt(in_fd, out_fd, sub_keys)
elif mode == "decrypt":
	decrypt(in_fd, out_fd, sub_keys)
		
running_time = time.time() - start_time
print "Processed " + str(byte_count) + " in %s seconds." % running_time
in_fd.close()
out_fd.close()
