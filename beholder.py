import random, sys
import collections, getpass

matrix_universe = 1000000

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget (encrypt/decrypt)?"
    sys.exit(0)
key_list = []
key = getpass.getpass("Input key: ")
for x in key:
    key_list.append(x)
shiftbox = [37, 59, 62, 15, 33, 76, 63, 21, 83, 77, 31, 61, 21, 8, 60, 16, 11, 17, 58, 2, 90, 43, 18, 8, 52, 59, 75, 7, 9, 27, 23, 30, 70, 82, 74, 30, 31, 58, 79, 68, 60, 81, 69, 8, 62, 65, 75, 6, 43, 57, 88, 70, 23, 3, 76, 18, 2, 55, 19, 40, 85, 42, 72, 2, 61, 48, 85, 6, 62, 17, 16, 36, 77, 49, 24, 0, 8, 28, 58, 12, 0, 69, 79, 84, 78, 77, 83, 6, 74, 83, 9, 21, 49, 14, 11, 67, 88, 0, 4, 81, 59, 47, 14, 6, 59, 69, 12, 20, 16, 83, 35, 57, 80, 19, 90, 61, 24, 91, 14, 9, 69, 17, 30, 16, 82, 36, 9, 70, 9, 44, 78, 38, 30, 89, 37, 36, 50, 63, 26, 16, 46, 83, 64, 31, 2, 88, 46, 60, 60, 29, 24, 57, 32, 85, 47, 67, 74, 68, 67, 15, 85, 56, 25, 6, 6, 63, 54, 12, 30, 75, 36, 27, 40, 41, 57, 36, 45, 50, 66, 47, 51, 74, 35, 45, 79, 36, 62, 76, 44, 66, 30, 56, 81, 63, 43, 0, 90, 49, 57, 85, 28, 14, 62, 78, 4, 73, 0, 3, 4, 63, 68, 24, 34, 62, 62, 88, 12, 32, 2, 73, 16, 36, 53, 73, 5, 54, 64, 40, 48, 29, 62, 27, 89, 14, 68, 68, 19, 28, 42, 23, 91, 7, 80, 23, 85, 24, 47, 69, 68, 45]
#matrixbox = [37054, 78847, 70114, 22156, 25223, 47150, 29377, 57925, 13101, 24806, 55573, 80701, 54354, 51336, 82741, 75460, 97904, 67917, 56072, 7804, 33082, 2840, 92087, 42342, 14423, 37860, 15854, 28530, 16445, 64441, 89252, 87136, 5578, 96984, 65584, 23446, 79177, 80371, 32959, 84880, 25648, 41246, 6133, 58670, 54552, 51574, 68227, 98279, 86027, 22057, 21741, 90204, 33512, 30193, 49117, 82509, 16726, 39163, 95986, 43051, 59463, 36924, 4149, 27589, 50870, 90073, 6156, 28913, 42079, 38325, 34040, 44867, 99821, 1683, 98446, 62852, 19341, 56074, 34412, 8666, 80869, 29567, 45006, 64378, 33684, 67209, 74989, 44526, 63139, 25585, 88244, 73440, 33040, 4972, 47735, 77288, 30418, 92576, 98854, 44463, 67826, 66919, 64052, 82293, 3250, 28918, 22962, 41062, 19688, 14874, 94183, 54021, 59984, 874, 15146, 43894, 31276, 33194, 97845, 40545, 15302, 611, 40364, 86640, 22143, 92000, 79499, 66493, 1354, 32417, 3615, 30678, 90835, 64720, 91047, 82651, 26332, 13285, 85621, 44592, 49929, 27837, 57544, 68880, 24828, 25399, 29401, 92876, 98883, 94449, 3975, 78208, 29510, 41018, 47541, 13727, 63003, 80791, 62381, 16994, 41346, 49371, 12307, 49054, 91148, 57435, 6083, 15515, 2173, 71611, 9484, 73417, 60383, 72665, 6927, 81096, 95783, 25668, 53838, 5823, 93065, 6839, 48082, 54227, 96991, 3372, 87442, 38404, 74794, 72340, 36888, 75226, 27010, 926, 40740, 3594, 61338, 11145, 74543, 41601, 32978, 59713, 18396, 11540, 6388, 29323, 58623, 96905, 64685, 55301, 21779, 47771, 13821, 64797, 85266, 38705, 40101, 77971, 53237, 31048, 95809, 89539, 8569, 3336, 94492, 82523, 21937, 3828, 99046, 47343, 82566, 25565, 26827, 24914, 55293, 89641, 83781, 65472, 97919, 65672, 98171, 84396, 27732, 48331, 69228, 90879, 28755, 92716, 99653, 66895]
matrixbox = [651660, 705822, 507200, 271870, 839165, 471878, 405201, 900993, 335658, 657889, 64529, 80631, 165249, 888982, 215038, 975011, 657979, 365800, 502515, 952604, 900659, 735204, 535593, 897304, 888505, 415005, 580415, 101794, 293564, 617408, 974600, 338071, 862577, 695333, 118545, 267047, 579984, 494338, 907265, 285676, 742755, 56372, 601694, 123268, 508859, 85888, 785855, 368353, 203084, 783215, 481081, 401752, 481808, 143953, 65017, 256731, 865970, 918837, 676813, 394303, 258124, 818909, 499755, 792305, 713399, 194663, 424708, 141376, 581517, 871173, 715973, 854303, 250703, 27514, 172904, 937542, 979313, 3648, 661532, 330265, 996842, 170681, 941083, 84604, 877527, 953958, 27202, 813098, 17447, 228878, 157600, 101679, 376048, 494143, 784349, 783223, 636820, 918856, 690783, 27627, 329535, 466873, 453599, 928381, 71694, 396553, 125175, 37268, 359427, 496167, 392173, 521095, 975762, 627581, 155986, 266699, 158106, 309885, 516484, 986226, 211574, 95506, 809923, 563408, 551483, 614669, 605724, 597017, 193632, 743525, 478388, 18932, 682109, 962964, 718405, 934711, 619695, 768939, 688666, 259126, 937440, 86026, 981191, 63463, 629369, 966284, 359187, 873818, 924128, 106967, 960378, 20638, 159233, 779662, 236818, 265404, 98350, 37272, 667037, 100269, 60808, 564485, 592942, 167570, 39985, 680746, 483934, 259637, 495894, 216753, 839688, 9800, 537315, 735467, 47569, 484162, 682732, 548110, 744514, 439333, 378263, 682024, 74076, 299633, 368699, 468312, 685238, 121643, 589266, 599071, 978508, 492556, 2835, 160117, 238153, 93365, 462223, 180395, 666616, 988403, 626653, 424880, 677061, 759759, 293049, 97770, 12155, 505473, 997846, 695290, 248649, 864925, 841713, 965779, 800348, 735509, 927286, 663044, 467319, 494971, 104682, 955774, 540064, 771648, 750210, 312161, 934211, 281291, 894047, 962334, 133623, 910826, 751472, 580122, 971168, 832293, 934687, 171053, 396360, 150231, 553572, 807568, 974034, 35672, 715626, 93667, 757105, 163841, 893939, 575911]

def encipher_char(data):
	newdata = ""
	init = []
	sub_box = []
        primer = collections.deque()
	sub_primer = collections.deque()
        for x in range(32,123):
                primer.append(chr(x))
		sub_primer.append(chr(x))
        local_key_list = list(key_list)
        shift_value = shiftbox.pop()
        matrix_value = matrixbox.pop()
        key_matrix_value = (matrix_value / 2)
        for x in range(0,len(key_list)):
            key_char = local_key_list.pop(0)
            key_matrix_value += ord(key_char)
        matrix = alpha_matrix(matrix_value, 0)
        key_matrix = alpha_matrix(key_matrix_value, 0)
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
            sub = key_matrix[sub]
            #sub_pos = init.index(sub)
            #sub = key_matrix.pop(sub_pos)
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
        local_key_list = list(key_list)
        shift_value = shiftbox.pop()
        matrix_value = matrixbox.pop()
        key_matrix_value = (matrix_value / 2)
        for x in range(0,len(key_list)):
            key_char = local_key_list.pop(0)
            key_matrix_value += ord(key_char)
        matrix = alpha_matrix(matrix_value, 1)
        key_matrix = alpha_matrix(key_matrix_value, 1)
        sub_primer.rotate(-shift_value)
	for x in range(0,91):
		init.append(primer.popleft())
		sub_box.append(sub_primer.popleft())

	for x in range(0,len(data)):
            try:
		pos = init.index(data[x])
            except ValueError as ver:
                print "Error on char: " + data[x]
            #sub_pos = init.index(data[x])
            #sub = key_matrix.pop(sub_pos)
	    #sub_pos = sub_box.index(sub)
	    sub_pos = sub_box.index(data[x])
	    sub = 0
	    sub = sub_box.pop(pos)
	    sub_box.insert(pos, sub)
            sub = matrix[sub]
            sub = key_matrix[sub]
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
        value = random.randint(0,matrix_universe)
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
    if mode == 0:
        alphabet_dict = {}
        for letter in master_alpha:
            alphabet_dict[letter] = alphabet.popleft()
    elif mode == 1:
        alphabet_dict = {}
        for letter in alphabet:
            alphabet_dict[letter] = master_alpha.popleft()
    elif mode == 2:
        alphabet_dict = []
        for letter in alphabet:
            alphabet_dict.append(letter)
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
