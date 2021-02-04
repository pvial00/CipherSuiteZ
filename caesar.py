import sys, collections

try:
    mode = sys.argv[1]
except IndexError as ier:
    print("Error: Did you foget encrypt/decrypt?")
    sys.exit(1)

def encipher(data):
	newdata = ""
	init = []
	sub_box = []
        primer = collections.deque()
	sub_primer = collections.deque()
        for x in range(0,127):
                primer.append(chr(x))
		sub_primer.append(chr(x))
        sub_primer.rotate(-3)
	for x in range(0,127):
		init.append(primer.popleft())
		sub_box.append(sub_primer.popleft())

	for x in range(0,len(data)):
		pos = init.index(data[x])
		sub_pos = sub_box.index(data[x])
		sub = sub_box.pop(pos)
		sub_box.insert(pos, sub)	
		newdata = newdata + sub
	return newdata

def decipher(data):
	newdata = ""
	init = []
	sub_box = []
        primer = collections.deque()
	sub_primer = collections.deque()
        for x in range(0,127):
                primer.append(chr(x))
		sub_primer.append(chr(x))
        sub_primer.rotate(3)
	for x in range(0,127):
		init.append(primer.popleft())
		sub_box.append(sub_primer.popleft())

	for x in range(0,len(data)):
		pos = init.index(data[x])
		sub_pos = sub_box.index(data[x])
		sub = 0
		sub = sub_box.pop(pos)
		sub_box.insert(pos, sub)	
		newdata = newdata + sub
	return newdata

data = input("Enter text to cipher: ")

if mode == "encrypt":
	cryptdata = encipher(data)
	print(cryptdata)
elif mode == "decrypt":
	clear = decipher(data)
	print(clear)
