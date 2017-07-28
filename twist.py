import sys, random, collections

mode = sys.argv[1]

def rev_words(words):
    newwords = []
    newstring = ""
    for letter in words:
        newwords.append(letter)
    newwords.reverse()
    for x in newwords:
        newstring += x
    return newstring

def words_to_list(words):
    newwords = []
    newstring = ""
    for letter in words:
        newwords.append(letter)
    return newwords

def twist_block(block):
    block_length = len(block)
    if block_length == 3:
        twisted_block = block.pop(2)
        twisted_block += block.pop(0)
        twisted_block += block.pop()
    elif block_length == 2:
        twisted_block = block.pop(1)
        twisted_block += block.pop()
    elif block_length == 1:
        twisted_block = block.pop()
    return twisted_block

def untwist_block(block):
    block_length = len(block)
    if block_length == 3:
        untwisted_block = block.pop(1)
        untwisted_block += block.pop(1)
        untwisted_block += block.pop()
    elif block_length == 2:
        untwisted_block = block.pop(1)
        untwisted_block += block.pop()
    elif block_length == 1:
        untwisted_block = block.pop()
    return untwisted_block


def block_data(words):
    words_length = len(words)
    num_blocks = words_length / 3
    extra_block = words_length % 3
    blocks = []
    block = []
    for ctr, letter in enumerate(words):
        block.append(letter)
        if len(block) == 3:
            blocks.append(block)
            del block
            block = []
        elif extra_block > 0 and ctr == (words_length - 1):
            blocks.append(block)
    return blocks

def twist_words(blocks):
    cipher_text = ""
    for block in blocks:
        twisted_block = twist_block(block)
        cipher_text += twisted_block
    return cipher_text

def untwist_words(blocks):
    plain_text = ""
    for block in blocks:
        untwisted_block = untwist_block(block)
        plain_text += untwisted_block
    return plain_text
        
words = raw_input("Enter words: ")
if mode == "twist":
    blocked_data = block_data(words)
    twisted_shit = twist_words(blocked_data)
    twisted_shit = rev_words(twisted_shit)
    print twisted_shit
elif mode =="untwist":
    words = rev_words(words)
    blocked_data = block_data(words)
    untwisted_shit = untwist_words(blocked_data)
    print untwisted_shit
