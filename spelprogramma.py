import random


def spelProgramma(spelList, minimum=3, maximum=10):
    newList = []

    for i in range(random.randrange(0, random.randrange(minimum, maximum + 1) + 1)):
        rand = random.randrange(0, len(spelList), 1)
        newList.append(spelList[rand])

    return newList


print(spelProgramma(['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']))