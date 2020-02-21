from random import randint


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


def simRoll(rolls, dice):
    total = 0

    for r in range(rolls):
        roll = dice.roll()
        print(roll, end=' ')

        total += roll
    return total


def simRollFromInput(text):
    rolls = int(text.split('d')[0])
    sides = int(text.split('d')[1])

    myDice = Dice(sides)

    return simRoll(rolls, myDice)


def parseInput(f):
    file = open(f, 'r')
    for line in file:
        print(line, end='')
        print(f'\n= {simRollFromInput(line)}\n')


parseInput('input.txt')
