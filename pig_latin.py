def vowel_check(letter):
    check = 0
    if letter == "a" or letter == "A":
        check = 1
    elif letter == "e" or letter == "E":
        check = 1
    elif letter == "i" or letter == "I":
        check = 1
    elif letter == "o" or letter == "O":
        check = 1
    elif letter == "u" or letter == "U":
        check = 1
    return check

def pig_pen(words):
    latin = ""
    for word in words.split():
        latin_word = ""
        check = vowel_check(word[0])
        if check == 1:
            latin_word = word
        elif check == 0:
            first = word[0]
            tmpword = ""
            for x in range(1,len(word)):
                tmpword += word[x]
            latin_word += tmpword + first
        latin += latin_word + "ay" + " "
    return latin

words = raw_input("Enter some english: ")

latin = pig_pen(words)
print latin
