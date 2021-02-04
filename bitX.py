import sys

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget encrypt/decrypt?")
    sys.exit(1)
try:
    infile = sys.argv[2]
except IndexError as ier:
    print("Error: Input file is missing")
    sys.exit(1)
try:
    outfile = sys.argv[3]
except IndexError as ier:
    print("Error: Output file is missing")
    sys.exit(1)

def bit_encipher(words):
    cipher_text = ""
    for letter in words:
        sub = ord(letter) << 1
        cipher_text += chr(sub)
    return cipher_text

def bit_decipher(words):
    plain_text = ""
    for letter in words:
        sub = ord(letter) >> 1
        plain_text += chr(sub)
    return plain_text

try:
    infile_fd = open(infile, "r")
except IOError as ier:
    print("Error: Unable to open input file.")
    sys.exit(1)
try:
    outfile_fd = open(outfile, "w")
except IOError as ier:
    print("Error: Unable to open output file.")
    sys.exit(1)
words = infile_fd.read()
infile_fd.close()

if mode == "encrypt":
    cipher_text = bit_encipher(words)
    outfile_fd.write(cipher_text)
    outfile_fd.close()
elif mode == "decrypt":
    plain_text = bit_decipher(words)
    print(plain_text)
    outfile_fd.write(plain_text)
    outfile_fd.close()
