import sys

mode = sys.argv[1]
#shift_index = 1527 arabic
# 896 greak
#shift_index = 896
shift_index = 1530
def translate_to_arabic(data):
    arabic = ""
    for letter in data:
        avalue = ord(letter) + shift_index
        arabic += chr(avalue)
    return arabic

def translate_to_english(data):
    english = ""
    for letter in data.decode('utf-8'):
        avalue = ord(letter) - shift_index
        english += chr(avalue)
    return english

def display_plaintext(data):
    english = ""
    for letter in data:
        avalue = ord(letter) - shift_index
        english += chr(avalue)
    return english

data = input("Enter text to encipher:")
if mode == "encrypt":
    arabic = translate_to_arabic(data)
    print(arabic)
    english = display_plaintext(arabic)
    print(english)
elif mode == "decrypt":
    english = translate_to_english(data)
    print(english)
