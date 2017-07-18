import random, sys
import collections

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget (encrypt/decrypt)?"
    sys.exit(0)
shiftbox = [37, 59, 62, 15, 33, 76, 63, 21, 83, 77, 31, 61, 21, 8, 60, 16, 11, 17, 58, 2, 90, 43, 18, 8, 52, 59, 75, 7, 9, 27, 23, 30, 70, 82, 74, 30, 31, 58, 79, 68, 60, 81, 69, 8, 62, 65, 75, 6, 43, 57, 88, 70, 23, 3, 76, 18, 2, 55, 19, 40, 85, 42, 72, 2, 61, 48, 85, 6, 62, 17, 16, 36, 77, 49, 24, 0, 8, 28, 58, 12, 0, 69, 79, 84, 78, 77, 83, 6, 74, 83, 9, 21, 49, 14, 11, 67, 88, 0, 4, 81, 59, 47, 14, 6, 59, 69, 12, 20, 16, 83, 35, 57, 80, 19, 90, 61, 24, 91, 14, 9, 69, 17, 30, 16, 82, 36, 9, 70, 9, 44, 78, 38, 30, 89, 37, 36, 50, 63, 26, 16, 46, 83, 64, 31, 2, 88, 46, 60, 60, 29, 24, 57, 32, 85, 47, 67, 74, 68, 67, 15, 85, 56, 25, 6, 6, 63, 54, 12, 30, 75, 36, 27, 40, 41, 57, 36, 45, 50, 66, 47, 51, 74, 35, 45, 79, 36, 62, 76, 44, 66, 30, 56, 81, 63, 43, 0, 90, 49, 57, 85, 28, 14, 62, 78, 4, 73, 0, 3, 4, 63, 68, 24, 34, 62, 62, 88, 12, 32, 2, 73, 16, 36, 53, 73, 5, 54, 64, 40, 48, 29, 62, 27, 89, 14, 68, 68, 19, 28, 42, 23, 91, 7, 80, 23, 85, 24, 47, 69, 68, 45]
matrixbox = [37054, 78847, 70114, 22156, 25223, 47150, 29377, 57925, 13101, 24806, 55573, 80701, 54354, 51336, 82741, 75460, 97904, 67917, 56072, 7804, 33082, 2840, 92087, 42342, 14423, 37860, 15854, 28530, 16445, 64441, 89252, 87136, 5578, 96984, 65584, 23446, 79177, 80371, 32959, 84880, 25648, 41246, 6133, 58670, 54552, 51574, 68227, 98279, 86027, 22057, 21741, 90204, 33512, 30193, 49117, 82509, 16726, 39163, 95986, 43051, 59463, 36924, 4149, 27589, 50870, 90073, 6156, 28913, 42079, 38325, 34040, 44867, 99821, 1683, 98446, 62852, 19341, 56074, 34412, 8666, 80869, 29567, 45006, 64378, 33684, 67209, 74989, 44526, 63139, 25585, 88244, 73440, 33040, 4972, 47735, 77288, 30418, 92576, 98854, 44463, 67826, 66919, 64052, 82293, 3250, 28918, 22962, 41062, 19688, 14874, 94183, 54021, 59984, 874, 15146, 43894, 31276, 33194, 97845, 40545, 15302, 611, 40364, 86640, 22143, 92000, 79499, 66493, 1354, 32417, 3615, 30678, 90835, 64720, 91047, 82651, 26332, 13285, 85621, 44592, 49929, 27837, 57544, 68880, 24828, 25399, 29401, 92876, 98883, 94449, 3975, 78208, 29510, 41018, 47541, 13727, 63003, 80791, 62381, 16994, 41346, 49371, 12307, 49054, 91148, 57435, 6083, 15515, 2173, 71611, 9484, 73417, 60383, 72665, 6927, 81096, 95783, 25668, 53838, 5823, 93065, 6839, 48082, 54227, 96991, 3372, 87442, 38404, 74794, 72340, 36888, 75226, 27010, 926, 40740, 3594, 61338, 11145, 74543, 41601, 32978, 59713, 18396, 11540, 6388, 29323, 58623, 96905, 64685, 55301, 21779, 47771, 13821, 64797, 85266, 38705, 40101, 77971, 53237, 31048, 95809, 89539, 8569, 3336, 94492, 82523, 21937, 3828, 99046, 47343, 82566, 25565, 26827, 24914, 55293, 89641, 83781, 65472, 97919, 65672, 98171, 84396, 27732, 48331, 69228, 90879, 28755, 92716, 99653, 66895]

def encipher_char(data):
	newdata = ""
	init = []
	sub_box = []
        primer = collections.deque()
	sub_primer = collections.deque()
        for x in range(32,123):
                primer.append(chr(x))
		sub_primer.append(chr(x))
        shift_value = shiftbox.pop()
        matrix_value = matrixbox.pop()
        matrix = alpha_matrix(matrix_value, 0)
        sub_primer.rotate(shift_value)
	for x in range(0,91):
		init.append(primer.popleft())
		sub_box.append(sub_primer.popleft())

	for x in range(0,len(data)):
            try:
		pos = init.index(data[x])
            except ValueError as ver:
                print "Error on char: " + data[x]
	    sub_pos = sub_box.index(data[x])
	    sub = sub_box.pop(pos)
	    sub_box.insert(pos, sub)
            sub = matrix[sub]
       	    newdata = newdata + sub
	return newdata

def decipher_char(data):
	newdata = ""
	init = []
	sub_box = []
        primer = collections.deque()
	sub_primer = collections.deque()
        for x in range(32,123):
                primer.append(chr(x))
		sub_primer.append(chr(x))
        shift_value = shiftbox.pop()
        matrix_value = matrixbox.pop()
        matrix = alpha_matrix(matrix_value, 1)
        sub_primer.rotate(-shift_value)
	for x in range(0,91):
		init.append(primer.popleft())
		sub_box.append(sub_primer.popleft())

	for x in range(0,len(data)):
            try:
		pos = init.index(data[x])
            except ValueError as ver:
                print "Error on char: " + data[x]
	    sub_pos = sub_box.index(data[x])
	    sub = 0
	    sub = sub_box.pop(pos)
	    sub_box.insert(pos, sub)
            sub = matrix[sub]
	    newdata = newdata + sub
	return newdata

def random_shiftbox(length):
    shiftbox = []
    for x in range(0,length):
        value = random.randint(0,91)
        shiftbox.append(value)
    return shiftbox

def random_matrixbox(length):
    matrixbox = []
    for x in range(0,length):
        value = random.randint(0,100000)
        matrixbox.append(value)
    return matrixbox

def alpha_matrix(matrix_number, mode):
    index = matrix_number / 91
    index_step = matrix_number % 91
    if index < 1:
        index = 1
    alphabet = collections.deque()
    master_alpha = collections.deque()
    for letter in range(32,123):
        alphabet.append(chr(letter))
        master_alpha.append(chr(letter))
    for x in range(0,index):
        alphabet.rotate(-1)
        for z in range(0,90):
            letter = alphabet.popleft()
            alphabet.append(letter)
    for y in range(0,index_step):
        letter = alphabet.popleft()
        alphabet.append(letter)
    alphabet_dict = {}
    if mode == 0:
        for letter in master_alpha:
            alphabet_dict[letter] = alphabet.popleft()
    elif mode == 1:
        for letter in alphabet:
            alphabet_dict[letter] = master_alpha.popleft()
    return alphabet_dict

if mode == "gen":
    box_value = int(sys.argv[2])

    shiftbox = random_shiftbox(box_value)
    matrixbox = random_matrixbox(box_value)
    print "shiftbox", shiftbox
    print "matrixbox", matrixbox
    sys.exit(0)

data = raw_input("Enter text to cipher: ")

if mode == "encrypt":
    cipher_text = ""
    for char in data:
        cryptdata = encipher_char(char)
        cipher_text += cryptdata
    print cipher_text
elif mode == "decrypt":
    plain_text = ""
    for char in data:
        clear = decipher_char(char)
        plain_text += clear
    print plain_text
