import sys, getpass

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget encrypt/decrypt?")
    sys.exit(1)

def kick_number(char):
    value = ord(char)
    kick = value * (2 ** 17)
    return kick

def shrink_number(num, key):
    shrink = num / int(key)
    return shrink

if mode == "encrypt":
    words = input("Input data: ")
    key_string = ""
    for ctr, letter in enumerate(words):
        value = kick_number(letter)
        value = value + ctr
        key = value / ord(letter)
        key_string += str(key) + " "
        print(value,)
    print("")
    print("Key: ", key)
elif mode == "decrypt":
    keys = []
    words = input("Input data: ")
    words = words.rstrip('\n')
    key = getpass.getpass("Input key: ")
    for ctr, word in enumerate(words.split()):
        num = int(word)
        shrink = num - ctr
        shrink = shrink_number(shrink, key)
        sys.stdout.write(chr(shrink))
    sys.stdout.write("\n")
