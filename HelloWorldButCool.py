import random



def charByPlace(code):
    code = chr(code+97)
    return code


def rLetter():
    place = random.randint(0, 25)
    return charByPlace(place)

#print((rLetter()))

def targetWord(word):
    string = ""
    loopCounter = 0
    while string != (word):
        string = ""
        for i in range (len(word)):
            string = string+rLetter()
        loopCounter=loopCounter+1
    print(string)
    #print(loopCounter)
    return string

targetWord("hello")
targetWord("world")


