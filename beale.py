import sys

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you forget encrypt/decrypt?")
    sys.exit(1)

try:
    book = sys.argv[2]
except (IndexError,IOError) as ier:
    print("Error: missing input file.")
    sys.exit(1)

def split_words(text):
    words = []
    for word in words.split():
        words.append(word)
    return words

def create_dictionary(book):
    try:
        book_fd = open(book, "r")
    except IOError as ier:
        print("Error: Unable to open book file")
        sys.exit(1)
    book_fd.read()
    book_fd.close()
    dictionary = {}
    dictionary_rev = {}
    master_list = []
    for index, word in enumerate(text.split()):
        if index == 0:
            index = 1
        master_list.append(word[0])
    return master_list

def encipher_text(words, dictionary):
    cipher_text = ""
    for word in words:
        for letter in word.split():
            sub = dictionary.index(letter)
            pop_sub = dictionary.pop(sub)
            dictionary.append(pop_sub)
            cipher_text += str(sub) + ", "
    return cipher_text

def decipher_numbers(numbers, dictionary_rev):
    plain_text = ""
    for number in numbers.split(','):
        if number != " " and number != "":
            num = int(number)
            sub = dictionary_rev.pop(num)
            dictionary_rev.append(sub)
            plain_text += sub
    return plain_text

words = input("Enter text to cipher: ")
dictionary = create_dictionary(book)
dictionary_rev = list(dictionary)

if mode == "encrypt":
    cipher_text = encipher_text(words, dictionary)
    print(cipher_text)
elif mode == "decrypt":
    plain_text = decipher_numbers(words, dictionary_rev)
    print(plain_text)
