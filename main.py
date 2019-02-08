import dice, random, os

diceObj = dice.dice()


def border():
    for border in range(20):
        print '-',
    print ''


while 1:
    option = input('[1] Dice Roll\n[2] Exit\n')
    if option == 1:
        border()
        diceObj.renderDice(random.randint(1, 6))
        diceObj.renderDice(random.randint(1, 6))
        border()
    elif option == 2:
        exit()
