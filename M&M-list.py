import random,time

aantal = 0
zakje = []
colorsMMS = 0
colors = ['oranje', 'blauw', 'groen', 'bruin']

def vraagMMS():
    aantal = int(input('Hoeveel M*Ms wilt u?\n'))
    if aantal >= 0:
        colorsMMS = int(input('Hoeveel kleuren wilt u toevoegen?\n'))
        if colorsMMS >= 0:
            ZakMMs(aantal)
        else:
            print("Deze optie is niet mogelijk")
    else:
        print('U heeft geen aantal gekozen')
        vraagMMS()

def ZakMMs(aantal):
    global zakje
    for i in range(aantal):
        new = random.choice(colors)
        zakje.append(new)
        zakje.sort()
    print(zakje)
    time.sleep(10)

vraagMMS()