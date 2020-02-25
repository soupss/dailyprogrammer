from random import randrange

# https://en.wikipedia.org/wiki/ANSI_escape_code
pre = '\033['
class txt:
    end = pre + '0m'
    #effects
    bold = pre + '1m'
    italic = pre + '3m'
    underline = pre + '4m'
    blink = pre + '6m'
    negative = pre + '7m'
    
    #colors
    white = pre + '107m'
    red = pre + '31m'
    green = pre + '32m'
    yellow = pre + '33m'
    magenta = pre + '35m'
    


def generateField(size):
    field = []
    for _ in range(size):
        field.append(str(randrange(2)))
    return field


def getMoves(field, array = False):
    moves = []
    for i, f in enumerate(field):
        if f == '1':
            moves.append(str(i))
    if not moves:
        return None
    else:
        return moves


def flip(field, index):
    if field[index] == '.':
        field[index] = field[index]
    else:
        field[index] = '1' if field[index] == '0' else '0'


field = generateField(int(input('field size: ')))

last = None
while True:
    if last or last == 0:
        print(f'last  {" " * last}{txt.negative}v{txt.end}')
    print(f'field {txt.negative}{"".join(field)}{txt.end}')
        
    if all(f == '.' for f in field):
        print(f'{txt.bold + txt.blink + txt.green + txt.white + txt.negative}Victory!{txt.end}')
        break
    else:
        if not getMoves(field):
            print(f'{txt.bold + txt.red + txt.white + txt.negative}Defeat!{txt.end}')
            break
        
    print(f'moves {txt.italic}{" ".join(getMoves(field))}{txt.end}')

    while True:
        i = input('> ')
        if not i or i == ' ' or not i in getMoves(field):
            print(f'{txt.yellow}invalid move{txt.end}')
            move = False
        else:
            move = True
        break
        
    if move:
        i = int(i)
        last = i

        field[i] = '.'
        if i + 1 == len(field):
            flip(field, i - 1)
        elif i == 0:
            flip(field, i + 1)
        else:
            flip(field, i - 1)
            flip(field, i + 1)
