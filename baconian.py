import sys

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget encrypt/decrypt?")
    sys.exit(1)

baconian_alphabet = { 'A':'aaaaa', 'B':'aaaab','C':'aaaba','D':'aaabb','E':'aabaa','F':'aabab','G':'aabba','H':'aabbb','I':'abaaa','J':'abaaa','K':'abaab','L':'ababa','M':'ababb','N':'abbaa','O':'abbab','P':'abbba','Q':'abbbb','R':'baaaa','S':'baaab','T':'baaba','U':'baabb','V':'baabb','W':'babaa','X':'babab','Y':'babba','Z':'babbb' }
baconian_alphabet_rev = { 'aaaaa':'A', 'aaaab':'B','aaaba':'C','aaabb':'D','aabaa':'E','aabab':'F','aabba':'G','aabbb':'H','abaaa':'I','abaaa':'J','abaab':'K','ababa':'L','ababb':'M','ababb':'N','abbaa':'O','abbba':'P','abbbb':'Q','baaaa':'R','baaab':'S','baaba':'T','baabb':'U','baabb':'V','babaa':'W','babab':'X','babba':'Y','babbb':'Z' }

if mode == "encrypt":
    cipher_text = ""
    words = input("Enter text to cipher: ")
    for word in words.split():
        for letter in word:
            sub = baconian_alphabet[letter]
            cipher_text += sub + " "
    print(cipher_text)
elif mode == "decrypt":
    plain_text = ""
    words = input("Enter text to decrypt: ")
    for word in words.split():
        sub = baconian_alphabet_rev[word]
        plain_text += sub
    print(plain_text)
