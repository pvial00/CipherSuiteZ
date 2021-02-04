import collections, sys, random

wheels = []
alphabets = [ 'JZRQUOFMSHCPLEXVNAIGBKDWYT', 'HINPTAYFWDOVKEQBXZJCLRGUSM', 'WDGKFOUPRNJBCZAHIMVXQYELTS', 'QKVZUAGNRPFLYCOTJBEXIHSWDM', 'MIFSBPRJEAGVDYCLNZOKWHTUQX', 'PYGVZXUKEBSHNICAJTLMDFQWOR', 'XATCJRKBEQPYLVUMSINFWODHZG', 'DJEGQPFLNXOABVMUYWSCZKTIRH', 'CJADKWQPXBLOEUTNRZIFYVMGSH', 'YZIQBGRPDWMFATVEOXCKLNHJSU', 'JAIMDGBRUCEVXNFWOYSZQLTKHP', 'IKTURDESLBGZYJNPWOHVAFCXQM', 'VWHIYEJBRUZOLMFKDPNGTXSQAC', 'SORQTWJIUCZELKAYFBXDVHMNPG', 'HLUICTONPSAWRBJYVMGQZFKDXE', 'PLSQOVFEMNWBGHCXZTRYIJKDUA', 'PLSQOVFEMNWBGHCXZTRYIJKDUA', 'IXAOLSMHBFWYRDKENTCPUVGQZJ', 'LBYDNARWOXSTIMHFCKEJVZQGUP', 'POIKUTYDRJNSGHFMLACXWQEVZB', 'CTPKARFUWNVMJYDLOEBSQHZXIG', 'ATKZQXLMUPEYJNRVIGDHWFSOBC', 'KDSYBLHEQJVNUGAIXTFCRWPMOZ', 'WSYCXGVRLNFIHEDMAOKPTJUBZQ', 'UZCTNLDYAKWEBIHMFSJORGQXVP', 'WOCNDQUTEASLRHJMBKFVPIZXYG', 'VFQGTUJSWYDOKZCPBRANXEILMH' ]

def init_wheels(num_wheels):
    global wheels
    for x in range(0,num_wheels):
        temp_que = collections.deque()
        for y in range(65,91):
            temp_que.append(chr(y))
            random.shuffle(temp_que)
        for y in range(0,26):
            popi = temp_que.popleft()
            sys.stdout.write(popi)
        sys.stdout.write("\n")
        wwheels.append(temp_que)
    return wheels

def program_wheels(num_wheels):
    global wheels
    global alphabets
    for x in range(0,num_wheels):
        alpha_set = alphabets.pop()
        temp_que = collections.deque()
        for letter in alpha_set:
            temp_que.append(letter)
        wheels.append(temp_que)
    return

def rotate_wheel(wheel_num, char):
    global wheels
    temp_que = wheels.pop(wheel_num)
    found = 0
    while found != 1:
         letter = temp_que.popleft()
         if letter != char:
             temp_que.appendleft(letter)
             temp_que.rotate(-1)
         elif letter == char:
             temp_que.appendleft(letter)
             wheels.append(temp_que)
             found = 1
             break
    return
	
def jefferson_cipher(data):
    global wheels
    wheel = []
    for x in reversed(range(0,len(data))):
        rotate_wheel(x, data[x])
    wheels.reverse()
    print("*************** POSSIBLE CIPHER TEXTS: ********************")
    for z in reversed(range(0,26)):
        for x in range(0,len(wheels)):
            wheel = wheels.pop(x)
            wheel.reverse()
            letter = wheel.pop()
            wheels.insert(x, wheel)
            sys.stdout.write(letter)
        sys.stdout.write("\n")

num_wheels = 26
program_wheels(num_wheels)
print("Jefferson Wheel Cipher (Enter a message up to 26 characters)")
data = input("Enter cipher text: ")
if len(data) > 26:
    print("Your message must be 26 characters or less.  Try again.")
    sys.exit(0)
jefferson_cipher(data)
