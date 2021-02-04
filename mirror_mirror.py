import sys, getpass

mode = sys.argv[1]
infile = sys.argv[2]
try:
    outfile = sys.argv[3]
except IndexError as ver:
    pass

tag = "MM:"

def inject_text(text):
    image_data = ""
    infile_fd = open(infile, "r")
    outfile_fd = open(outfile, "w")
    chunk = infile_fd.readline()
    image_data += chunk
    rest = infile_fd.read()
    infile_fd.close()
    image_data += rest + "\n" + tag + text
    outfile_fd.write(image_data)
    outfile_fd.close()

def extract_text():
    infile_fd = open(infile, "r")
    data = infile_fd.read()
    data_size = len(data)
    tag_size = len(tag)
    msg_size = data_size - tag_size
    encrypted_message = ""
    if tag in data:
        tag_pos = data.index(tag)
        for x in range(tag_pos+tag_size,data_size):
            encrypted_message += data[x]
        plaintext_message = krypt(encrypted_message, key)
        print(plaintext_message)
    else:
        print("Unable to find secrect message.")
    

def krypt(text, key):
    cipher_text = ""
    for char in text:
        for key_char in key:
            sub = ord(char) ^ ord(key_char)
        cipher_text += chr(sub)
    return cipher_text

if mode == "encrypt":
    text = input("Enter text to hide: ")
    key = getpass.getpass("Enter key: ")
    cipher_text = krypt(text, key)
    inject_text(cipher_text)
elif mode == "decrypt":
    key = getpass.getpass("Enter key: ")
    extract_text()
