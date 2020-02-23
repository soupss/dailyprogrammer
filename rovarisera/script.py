consonants = 'bcdfghjklmnpqrstvwxz'


def parseChar(char):
    if char.lower() in consonants:
        return char + 'o' + char.lower()
    else:
        return char


def rövarisera(msg):
    newMsg = ''
    for char in msg:
        newMsg += parseChar(char)
    return newMsg


msg = input('Enter phrase to encode: ')
print(rövarisera(msg))
