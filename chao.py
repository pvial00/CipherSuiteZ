import sys, random

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)
alpha_sub = ['H', 'X', 'U', 'C', 'Z', 'V', 'A', 'M', 'D', 'S', 'L', 'K', 'P', 'E', 'F', 'J', 'R', 'I', 'G', 'T', 'W', 'O', 'B', 'N', 'Y', 'Q']
alpha_master = ['P', 'T', 'L', 'N', 'B', 'Q', 'D', 'E', 'O', 'Y', 'S', 'F', 'A', 'V', 'Z', 'K', 'G', 'J', 'R', 'I', 'H', 'W', 'X', 'U', 'M', 'C']

def gen_alphabet():
    alphabet = []
    alphabet_rev = []
    for x in range(0,26):
        alphabet.append(chr(x + 65))
        alphabet_rev.append(chr(x + 65))
        random.shuffle(alphabet)
        random.shuffle(alphabet_rev)
    return alphabet, alphabet_rev

def permute_alpha_sub(letter):
    while True:
        step1 = alpha_sub.pop(0)
        if step1 == letter:
            alpha_sub.insert(0,step1)
            break
        else:
            alpha_sub.append(step1)
    step2 = alpha_sub.pop(1)
    alpha_sub.insert(12,step2)

def permute_alpha_master(letter):
    nadir = 13
    while True:
        step1 = alpha_master.pop(0)
        if step1 == letter:
            alpha_master.insert(0,step1)
            break
        else:
           alpha_master.append(step1)
    step2 = alpha_master.pop(0)
    alpha_master.append(step2)
    step3 = alpha_master.pop(2)
    alpha_master.insert(12,step3)

def chao_encrypt(words):
    cipher_text = ""
    for word in words.split():
        for letter in word:
            pos = alpha_master.index(letter)
            sub = alpha_sub.pop(pos)
            alpha_sub.insert(pos,sub)
            permute_alpha_sub(sub)
            permute_alpha_master(letter)
            cipher_text += sub
    return cipher_text

def chao_decrypt(words):
    plain_text = ""
    for word in words.split():
        for letter in word:
            pos = alpha_sub.index(letter)
            sub = alpha_master.pop(pos)
            alpha_master.insert(pos,sub)
            permute_alpha_sub(letter)
            permute_alpha_master(sub)
            plain_text += sub
    return plain_text

if mode == "gen":
    alphabet, alphabet_rev = gen_alphabet()
    print alphabet
    print alphabet_rev
elif mode == "encrypt":
    words = raw_input("Enter text to cipher: ")
    cipher_text = chao_encrypt(words)
    print cipher_text
elif mode == "decrypt":
    words = raw_input("Enter text to cipher: ")
    plain_text = chao_decrypt(words)
    print plain_text
