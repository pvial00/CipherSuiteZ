import sys, time, os
from getpass import getpass

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget encrypt/decrypt?")
    sys.exit(1)

try:
    in_file = sys.argv[2]
except IndexError as ier:
    print("Error: input file is missing")
    sys.exit(1)

try:
    out_file = sys.argv[3]
except IndexError as ier:
    print("Error: output file is missing")
    sys.exit(1)

def gen_session_key(session_key_length):
	session_key = ""
	for key in range(0,session_key_length):
		session_key = session_key + "".join(map(chr, os.urandom(1)))
	return session_key

def krypt(text, key):
	crypt_text = ""
	for x in range(0,len(text)):
		byte = text[x]
		primary_round = ord(byte)
		for y in range(0,len(key)):
			primary_round = primary_round ^ ord(key[y])
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

try:
	infile = open(in_file, "r")
except NameError as ner:
	print("Unable to open infile")
	sys.exit(0)

try:
	outfile = open(out_file, "w")
except NameError as ner:
	print("Unable to open outfile")
	sys.exit(0)

try:
	key = sys.argv[4]
except IndexError:
	key = getpass("key: ")

data = infile.read()
session_key_length =  16 # 16 for 128 bit, 32 for 256 bit, 128 for 1024 bit, 256 for 2048 

start_time = time.time()
if mode == "encrypt":
	cipher_text = krypto_pack(data, key)
	outfile.write(cipher_text)
elif mode == "decrypt":
	plain_text = krypto_unpack(data, key)
	outfile.write(plain_text)

end_time = time.time() - start_time
print("Completed in %s seconds" % end_time)
infile.close()
outfile.close()
