from random import randint


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


def simRoll(rolls, dice):
    total = 0

    for roll in range(rolls):
        rollValue = dice.roll()

        print('You rolled a {0} on roll number {1}'.format(
            rollValue, roll + 1))

        total += rollValue

    return total


def simRollFromInput(text):
    rolls = int(text.split('d')[0])
    sides = int(text.split('d')[1])

    myDice = Dice(sides)

    return simRoll(rolls, myDice)


def parseInput(f):
    file = open(f, 'r')
    for line in file:
        print('Total value: {}\n'.format(simRollFromInput(line)))


parseInput('input.txt')
