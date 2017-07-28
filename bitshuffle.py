import sys

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

def bit_shuffle(words):
    cipher_text = ""
    for letter in words:
        left_bin_block = []
        right_bin_block = []
        cipher_block = ""
        bin_list = bin(ord(letter)).split("0b")
        bin_bits = bin_list.pop()
        block_length = len(bin_bits)
        split_index = block_length / 2
        extra_bit = block_length % 2
        for x in range(0,split_index):
            left_bin_block.append(bin_bits[x])
        for x in range(split_index, block_length):
            right_bin_block.append(bin_bits[x])
        if len(left_bin_block) == 3:
            left_bit_shift = [2, 0, 0]
        if len(right_bin_block) == 4:
            right_bit_shift = [2, 0, 0, 0]
        if len(right_bin_block) == 3:
            right_bit_shift = [1, 1, 0]
        for bit in left_bit_shift:
            cipher_block += left_bin_block.pop(bit)
        for bit in right_bit_shift:
            cipher_block += right_bin_block.pop(bit)
        del left_bin_block[:]
        del right_bin_block[:]
        cipher_text += cipher_block + " "
    return cipher_text

def bit_unshuffle(bits):
    plain_text = ""
    for letter in bits.split():
        left_bin_block = []
        right_bin_block = []
        cipher_block = ""
        block_length = len(letter)
        split_index = block_length / 2
        extra_bit = block_length % 2
        for x in range(0,split_index):
            left_bin_block.append(letter[x])
        for x in range(split_index, block_length):
            right_bin_block.append(letter[x])
        if len(left_bin_block) == 3:
            left_bit_shift = [1, 1, 0]
        if len(right_bin_block) == 4:
            right_bit_shift = [1, 1, 0 , 0]
        if len(right_bin_block) == 3:
            right_bit_shift = [2, 0, 0 ]
        for bit in left_bit_shift:
            cipher_block += left_bin_block.pop(bit)
        for bit in right_bit_shift:
            cipher_block += right_bin_block.pop(bit)
        del left_bin_block[:]
        del right_bin_block[:]
        plain_text += chr(int(cipher_block, 2))
    return plain_text

words = raw_input("Enter text to cipher: ")

if mode == "encrypt":
    cipher_text = bit_shuffle(words)
    print cipher_text
elif mode == "decrypt":
    plain_text = bit_unshuffle(words)
    print plain_text
