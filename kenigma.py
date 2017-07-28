import collections, sys, random

etw_wheel = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#rotor2_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#rotor3_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


rotor1_set = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2_set = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3_set = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector_set = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

rotor1_dict = {'A':'E', 'B':'K', 'C':'M', 'D':'F','E':'L','F':'G','G':'D','H':'Q','I':'V','J':'Z','K':'N','L':'T','M':'O','N':'W','O':'Y','P':'H','Q':'X','R':'U','S':'S','T':'P','U':'A','V':'I','W':'B','X':'R','Y':'C','Z':'J' }

reflector = {'A':'Y', 'B':'R', 'C':'U', 'D':'H','E':'Q','F':'S','G':'L','H':'D','I':'P','J':'X','K':'N','L':'G','M':'O','N':'K','O':'M','P':'I','Q':'E','R':'B','S':'F','T':'Z','U':'C','V':'W','W':'V','X':'J','Y':'A','Z':'T' }

#rotor1_dict = {'A':'E', 'B':'K', 'C':'M', 'D':'F','E':'L','F':'G','G':'D','H':'Q','I':'V','J':'Z','K':'N','L':'T','M':'O','N':'W','O':'Y','P':'H','Q':'X','R':'U','S':'S','T':'P','U':'A','V':'I','W':'B','X':'R','Y':'C','Z':'J' }

plugboard = {'A':'A', 'B':'B', 'C':'C', 'D':'D','E':'E','F':'F','G':'G','H':'H','I':'I','J':'J','K':'K','L':'L','M':'M','N':'N','O':'O','P':'P','Q':'Q','R':'R','S':'S','T':'T','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z':'Z' }

global rotor1_settings
rotor1_settings = collections.deque()
global rotor1_step_counter
rotor1_step_counter = 0
global rotor1_pos
global rotor2_settings
rotor2_settings = collections.deque()
global rotor2_step_counter
rotor2_step_counter = 0
global rotor3_settings
rotor3_settings = collections.deque()
global rotor3_step_counter
rotor3_step_counter = 0
global rotor3_ring_setting
rotor3_ring_setting = "A"
global rotor1_init
rotor1_init = []
rotor2_init = []
rotor3_init = []
etw_wheel_settings = []
global reflector_settings
reflector_settings = collections.deque()
primer = collections.deque()
gohome = 0

def rotor1(char):
	global rotor1_settings
	global rotor1_step_counter
	global rotor1_pos
	global rotor1_dict
	round_settings = []
	round_settings = convert_rotor1_deque(rotor1_settings)
	print "settings: ", round_settings
	pos = rotor1_init.index(char)
	sub_pos = pos
	if gohome == 0:
		sub = round_settings.pop(sub_pos)
		if rotor1_step_counter < 25:
			rotor1_step_counter = rotor1_step_counter + 1
		if rotor1_step_counter >= 25:
			rotor1_step_counter = 0
       			rotor1_settings.rotate(-1)
	elif gohome == 1:
		pos = round_settings.index(char)
		print "shit: ", pos
		sub = etw_wheel_settings.pop(pos)
		etw_wheel_settings.insert(pos, sub)
	#rotor1_pos = round_settings[rotor1_step_counter]
	
	print "1sub: ", sub
	return sub

def rotor2(char):
	global rotor2_settings
	global rotor2_step_counter
	round_settings = []
	round_settings = convert_rotor2_deque(rotor2_settings)
	print "settings: ", round_settings
	print "2 init: ", rotor2_init
	print "2 step: ", rotor2_step_counter

	
	pos = rotor2_init.index(char)
	#pos = pos
	sub_pos = pos - rotor3_step_counter
	if gohome == 0:
		sub = round_settings.pop(sub_pos)
		#if rotor2_step_counter < 25:
			#rotor2_step_counter = rotor2_step_counter + 1
		if rotor2_step_counter == 25:
			print "2steP"
			rotor2_step_counter = 0
			#exit(0)
			#rotate_rotor1()
			#rotor1_settings.rotate(-1)
	#print sub_pos
	if gohome == 1:
		pos = round_settings.index(char)
		print "2pos", pos
		sub = etw_wheel_settings.pop(pos)
		print sub
		etw_wheel_settings.insert(pos, sub)
		
	print "2sub: ",sub
	return sub

def rotor3(char):
	global rotor3_setting
	global rotor2_step_counter
	global rotor3_step_counter
	global rotor3_ring_setting
	global gohome
	print "counter: ", rotor3_step_counter
	if gohome == 0:
		if rotor3_step_counter < 25:
			rotor3_settings.rotate(-1)
			rotate_rotor3(1)
			round_settings = []
			round_settings = convert_rotor3_deque(rotor3_settings)
			rotor3_step_counter = rotor3_step_counter + 1
			rotor2_step_counter = rotor2_step_counter + 1
			print "3settings: ", round_settings
		print "counter: ", rotor3_step_counter
		if rotor3_step_counter == 22:
			rotor2_step_counter = 0
			print "new count: ", rotor3_step_counter
			rotate_rotor2(1)
			rotor2_settings.rotate(-1)
		elif rotor3_step_counter >= 25:
			rotor3_step_counter = 0
		step_pos = rotor3_step_counter
		rotor3_ring_setting = str(step_pos)
		pos = etw_wheel_settings.index(char)
		sub = round_settings.pop(pos)
	elif gohome == 1:
		round_settings = []
		round_settings = convert_rotor3_deque(rotor3_settings)
		print "settings: ", round_settings
		print "3settings: ", rotor3_init
		pos = etw_wheel_settings.index(char)
		#apos = rotor3_init.index(char)
		pos = pos + rotor3_step_counter
		if pos >= 26:
			pos = pos - 26
		#pos = etw_wheel_settings.index(char)
		#sub = round_settings.pop(pos)
		sub = round_settings.pop(pos)
                print "alsub", sub
                round_settings.insert(pos, sub)
                pos = etw_wheel_settings.index(sub)
                pos = round_settings.index(sub)
                sub = etw_wheel_settings.pop(pos)
                etw_wheel_settings.insert(pos, sub)
                pos = round_settings.index(sub)
                sub = etw_wheel_settings.pop(pos)
                print sub
                etw_wheel_settings.insert(pos, sub)

	print "roundset len: ", len(round_settings)
	#sub = round_settings.pop(entry_pos)
	print "3sub: ",sub
	return sub

def rotate_rotor1(num):
	for x in range(0,num):
		rotor1_init.reverse()
		step = rotor1_init.pop()
		rotor1_init.reverse()
		rotor1_init.append(step)
		#print "rotate: ", rotor1_init

def rotate_rotor2(num):
	for x in range(0,num):
		rotor2_init.reverse()
		step = rotor2_init.pop()
		rotor2_init.reverse()
		rotor2_init.append(step)
		#print "rotate: ", rotor2_init

def rotate_rotor3(num):
	for x in range(0,num):
		rotor3_init.reverse()
		step = rotor3_init.pop()
		rotor3_init.reverse()
		rotor3_init.append(step)
		print "rotate: ", rotor3_init

def rotate_etw():
	etw_wheel_settings.reverse()
	step = etw_wheel_settings.pop()
	etw_wheel_settings.reverse()
	etw_wheel_settings.append(step)
	print "etw rotate: ", etw_wheel_settings

def convert_rotor1_deque(_set):
	new_list = []
	for x in range(0,len(_set)):
		item = _set.popleft()
		rotor1_settings.append(item)
		new_list.append(item)
	return new_list

def convert_rotor2_deque(_set):
	new_list = []
	for x in range(0,len(_set)):
		item = _set.popleft()
		rotor2_settings.append(item)
		new_list.append(item)
	return new_list

def convert_rotor3_deque(_set):
	new_list = []
	for x in range(0,len(_set)):
		item = _set.popleft()
		rotor3_settings.append(item)
		new_list.append(item)
	return new_list

def neutral_rotors():
	global rotor1_settings
	global rotor2_settings
	global rotor3_settings
        global primer
        #sub_primer = collections.deque()
        for x in range(65,91):
                primer.append(chr(x))
		rotor1_init.append(chr(x))
		rotor2_init.append(chr(x))
		rotor3_init.append(chr(x))
		etw_wheel_settings.append(chr(x))
                #rotor1_settings.append(chr(x))
                #rotor2_settings.append(chr(x))
                #rotor3_settings.append(chr(x))
	#print rotor1_settings
	#print "etw_wheel: ", etw_wheel_settings
	#r1_len = len(rotor1_settings)
	#rand = random.randint(0,r1_len)
        #rotor1_settings.rotate(rand)

def init_rotors():
	for x in range(0,len(rotor1_set)):
		rotor1_settings.append(rotor1_set[x])
	for x in range(0,len(rotor2_set)):
		rotor2_settings.append(rotor2_set[x])
	for x in range(0,len(rotor3_set)):
		rotor3_settings.append(rotor3_set[x])
	for x in range(0,len(reflector_set)):
		reflector_settings.append(reflector_set[x])

def configure_plugboard(config):
	if config != "" or config != "\n":
		config = config.split()
		for pair in config:
			one = pair[0]
			two = pair[1]
			plugboard[one] = two
			plugboard[two] = one
	print plugboard

def configure_rotors(settings):
	global rotor1_step_counter
	global rotor2_step_counter
	global rotor3_step_counter
	if settings != "" or settings != "\n":
		rotor1_step_counter = settings[0]
		rotor1_step_counter = etw_wheel_settings.index(rotor1_step_counter)
		rotate_rotor1(rotor1_step_counter)
		rotor1_settings.rotate(-rotor1_step_counter)
		rotor2_step_counter = settings[1]
		rotor2_step_counter = etw_wheel_settings.index(rotor2_step_counter)
		rotate_rotor2(rotor2_step_counter)
		rotor2_settings.rotate(-rotor2_step_counter)
		rotor3_step_counter = settings[2]
		rotor3_step_counter = etw_wheel_settings.index(rotor3_step_counter)
		rotate_rotor3(rotor3_step_counter)
		rotor3_settings.rotate(-rotor3_step_counter)
		#print rotor1_step_counter, rotor2_step_counter, rotor3_step_counter

neutral_rotors()
init_rotors()
#ring_settings = raw_input("Ring settings: ")
#configure_rotors(ring_settings)
plugboard_config = raw_input("Plugboard configuration: ")
configure_plugboard(plugboard_config)
string = raw_input("Enter: ")
newstring = ""
#neutral_rotors()
#init_rotors()
#rotor3_settings.rotate(-1)
#rotate_etw()
#rotate_rotor3(1)
for char in range(0,len(string)):
	gohome = 0
	sub = plugboard[string[char]]
	sub = rotor3(sub)
	sub = rotor2(sub)
	sub = rotor1(sub)
	sub = reflector[sub]
	gohome = 1
	print sub
	sub = rotor1(sub)
	sub = rotor2(sub)
	sub = rotor3(sub)
	sub = plugboard[sub]
	newstring = newstring + sub
print newstring
