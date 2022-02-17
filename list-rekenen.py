listOne = [i for i in range(1, 11)]
listTwo = [i for i in range(2, 21, 2)]

def addAndDisplayLists(listOne, listTwo): 
    print('---------')
    print('Add lists')
    for i in range(min(len(listOne), len(listTwo))):
        print("{:<2} + {:<2} = {:<5}".format(listOne[i], listTwo[i], listOne[i] + listTwo[i]))

def substractAndDisplayLists(listOne, listTwo):
    print('---------')
    print('Substract lists')
    for i in range(min(len(listOne), len(listTwo))):
        print("{:<2} - {:<2} = {:<5}".format(listOne[i], listTwo[i], listOne[i] - listTwo[i]))

def multiplyAndDisplayLists (listOne, listTwo):
    print('---------')
    print('Multiply lists')
    for i in range(min(len(listOne), len(listTwo))):
        print("{:<2} * {:<2} = {:<5}".format(listOne[i], listTwo[i], listOne[i] * listTwo[i]))

def divideAndDisplayLists(listOne, listTwo):
    print('---------')
    print('Divide lists')
    for i in range(min(len(listOne), len(listTwo))):
        print("{:<2} / {:<2} = {:<5}".format(listOne[i], listTwo[i], listOne[i] / listTwo[i]))

addAndDisplayLists(listOne, listTwo)
substractAndDisplayLists(listOne, listTwo)
multiplyAndDisplayLists(listOne, listTwo)
divideAndDisplayLists(listOne, listTwo)