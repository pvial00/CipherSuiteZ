import sys, time
from getpass import getpass
import collections

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)
try:
    in_file = sys.argv[2]
except IndexError as ier:
    print "Error: input file missing"
    sys.exit(1)
try:
    out_file = sys.argv[3]
except IndexError as ier:
    print "Error: output file missing"
    sys.exit(1)

def vernam_xor(text, key):
    crypt_text = ""
    for x in range(0,len(text)):
	primary_round = ord(text[x])
	primary_round = primary_round ^ ord(key[y])
	crypt_text += chr(primary_round)
    return crypt_text


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
	key
except NameError:
	key = getpass("key: ")

data = infile.read()

start_time = time.time()
if mode == "encrypt":
	cipher_text = vernam_xor(data, key)
	outfile.write(cipher_text)
elif mode == "decrypt":
	plain_text = vernam_xor(data, key)
	outfile.write(plain_text)

end_time = time.time() - start_time
print "Completed in %s seconds" % end_time
infile.close()
outfile.close()
