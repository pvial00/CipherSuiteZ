import sys

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

baconian_alphabet = { 'A':'00000', 'B':'00001','C':'00010','D':'00011','E':'00100','F':'00101','G':'00110','H':'00111','I':'01000','J':'01000','K':'01001','L':'01010','M':'01011','N':'01100','O':'01101','P':'01110','Q':'01111','R':'10000','S':'10001','T':'10010','U':'10011','V':'10011','W':'10100','X':'10101','Y':'10110','Z':'10111' }
baconian_alphabet_rev = { '00000':'A', '00001':'B','00010':'C','00011':'D','00100':'E','00101':'F','00110':'G','00111':'H','01000':'I','01000':'J','01001':'K','01010':'L','01011':'M','01011':'N','01100':'O','01110':'P','01111':'Q','10000':'R','10001':'S','10010':'T','10011':'U','10011':'V','10100':'W','10101':'X','10110':'Y','10111':'Z' }

if mode == "encrypt":
    cipher_text = ""
    words = raw_input("Enter text to cipher: ")
    for word in words.split():
        for letter in word:
            sub = baconian_alphabet[letter]
            cipher_text += sub + " "
    print cipher_text
elif mode == "decrypt":
    plain_text = ""
    words = raw_input("Enter text to decrypt: ")
    for word in words.split():
        sub = baconian_alphabet_rev[word]
        plain_text += sub
    print plain_text
