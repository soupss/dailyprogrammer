from random import randrange


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
        print(f'last  {" " * last + "v"}')
    print(f'field {"".join(field)}')
        
    if all(f == '.' for f in field):
        print('Victory!')
        break
    else:
        if not getMoves(field):
            print('Defeat!')
            break
        
    print(f'moves {" ".join(getMoves(field))}')
        
    while True:
        i = input('> ')
        if not i or i == ' ' or not i in getMoves(field):
            print(f'invalid move\navailable moves: {" ".join(getMoves(field))}')
        else:
            break
        
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
