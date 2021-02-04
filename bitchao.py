import sys, random, select

if select.select([sys.stdin,],[],[],0.0)[0]:
    words = sys.stdin.read()
else:
    words = input("Enter text to cipher: ")

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget encrypt/decrypt?")
    sys.exit(1)

alpha_sub = [142, 71, 43, 156, 130, 37, 39, 126, 81, 18, 153, 233, 202, 154, 178, 160, 144, 78, 120, 10, 155, 49, 105, 176, 185, 67, 195, 7, 215, 75, 3, 47, 220, 219, 162, 13, 183, 208, 254, 182, 187, 86, 163, 243, 166, 168, 152, 249, 242, 107, 136, 48, 252, 179, 25, 170, 221, 16, 177, 98, 5, 53, 164, 203, 225, 250, 118, 180, 173, 211, 113, 169, 93, 104, 88, 29, 55, 236, 174, 84, 22, 217, 119, 161, 32, 60, 117, 73, 59, 194, 206, 85, 58, 241, 239, 232, 100, 94, 34, 62, 28, 192, 204, 17, 4, 45, 189, 186, 19, 141, 199, 6, 223, 127, 247, 237, 111, 132, 103, 129, 80, 38, 198, 227, 212, 46, 145, 197, 229, 8, 92, 36, 234, 231, 255, 124, 240, 172, 27, 251, 207, 30, 54, 213, 91, 188, 158, 61, 151, 125, 128, 87, 69, 238, 63, 196, 109, 1, 121, 210, 96, 171, 74, 102, 12, 146, 209, 131, 9, 224, 106, 245, 95, 216, 56, 122, 50, 228, 159, 222, 79, 65, 40, 108, 57, 190, 70, 23, 0, 244, 157, 165, 138, 110, 14, 11, 101, 68, 90, 137, 33, 140, 72, 114, 205, 193, 44, 135, 77, 184, 97, 230, 167, 123, 99, 148, 2, 51, 64, 200, 133, 139, 147, 175, 134, 115, 116, 21, 150, 24, 52, 35, 235, 191, 15, 149, 201, 253, 26, 31, 20, 248, 112, 181, 218, 226, 82, 214, 143, 89, 41, 83, 66, 76, 246, 42]
alpha_master = [243, 114, 14, 189, 193, 94, 22, 211, 4, 117, 49, 34, 118, 58, 184, 106, 92, 131, 109, 134, 19, 175, 221, 3, 141, 239, 245, 67, 147, 186, 182, 132, 57, 104, 5, 10, 202, 191, 8, 158, 187, 238, 112, 121, 126, 201, 80, 1, 170, 113, 71, 155, 223, 128, 137, 148, 91, 190, 29, 222, 154, 44, 165, 251, 230, 63, 64, 146, 120, 203, 83, 17, 188, 59, 195, 217, 130, 198, 151, 207, 68, 53, 142, 133, 173, 99, 143, 46, 240, 123, 16, 45, 122, 163, 152, 196, 73, 139, 233, 145, 242, 52, 205, 54, 2, 12, 135, 209, 229, 125, 100, 168, 228, 48, 90, 172, 40, 250, 26, 110, 237, 140, 200, 225, 23, 107, 213, 105, 232, 185, 156, 247, 171, 87, 20, 235, 138, 33, 65, 180, 167, 24, 15, 169, 79, 96, 93, 30, 210, 136, 102, 162, 25, 164, 220, 246, 75, 32, 18, 116, 38, 78, 254, 56, 31, 215, 13, 253, 161, 248, 69, 39, 174, 227, 160, 197, 119, 89, 111, 177, 6, 55, 60, 21, 82, 36, 108, 208, 50, 249, 234, 28, 85, 115, 153, 129, 42, 103, 150, 74, 224, 41, 214, 84, 27, 159, 181, 178, 231, 199, 204, 72, 176, 86, 192, 212, 166, 76, 88, 194, 101, 255, 244, 206, 124, 62, 35, 183, 70, 95, 51, 149, 219, 218, 179, 43, 61, 66, 226, 47, 37, 241, 252, 144, 77, 9, 236, 98, 127, 157, 7, 11, 97, 0, 81, 216]

def gen_alphabet():
    alphabet = []
    alphabet_rev = []
    for x in range(0,256):
        alphabet.append(x)
        alphabet_rev.append(x)
        random.shuffle(alphabet)
        random.shuffle(alphabet_rev)
    return alphabet, alphabet_rev

def permute_alpha_sub(letter):
    index = alpha_sub.index(letter)
    step1 = alpha_sub.pop(0)
    alpha_sub.insert(index,step1)
    step2 = alpha_sub.pop(1)
    alpha_sub.insert(128,step2)

def permute_alpha_master(letter):
    index = alpha_master.index(letter)
    step1 = alpha_master.pop(0)
    alpha_master.insert(index,step1)
    step2 = alpha_master.pop(0)
    alpha_master.append(step2)
    step3 = alpha_master.pop(2)
    alpha_master.insert(128,step3)

def chao_encrypt(words):
    cipher_text = ""
    for letter in words:
        char = ord(letter)
        pos = alpha_master.index(char)
        sub = alpha_sub.pop(pos)
        alpha_sub.insert(pos,sub)
        permute_alpha_sub(sub)
        permute_alpha_master(char)
        cipher_text += chr(sub)
    return cipher_text

def chao_decrypt(words):
    plain_text = ""
    for letter in words:
        char = ord(letter)
        pos = alpha_sub.index(char)
        sub = alpha_master.pop(pos)
        alpha_master.insert(pos,sub)
        permute_alpha_sub(char)
        permute_alpha_master(sub)
        plain_text += chr(sub)
    return plain_text

if mode == "gen":
    alphabet, alphabet_rev = gen_alphabet()
    print(alphabet)
    print(alphabet_rev)
elif mode == "encrypt":
    cipher_text = chao_encrypt(words)
    print(cipher_text)
elif mode == "decrypt":
    plain_text = chao_decrypt(words)
    print(plain_text)
