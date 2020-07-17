import time
saida = r'''
starting...'''
print(saida)
time.sleep(1)
print()
print('Welcome!\nWe have')
print('Espresso, latte, cappuccino maker, please choose your order!')
time.sleep(1)
print()
# cafeteira

agua, leite, grama, copo, dinheiro = 400, 540, 120, 9, 550

# funcoes


def printar():
    print()
    print('The coffee machine has:')
    print(f'{agua} of water')
    print(f'{leite} of milk')
    print(f'{grama} of coffee beans')
    print(f'{copo} of disposable cups')
    print(f'{dinheiro} of money')
    print()


def fill(aguas, leites, gramas, copos):
    global agua, leite, grama, copo, dinheiro
    agua += aguas
    leite += leites
    grama += gramas
    copo += copos
    print()


def take():
    global agua, leite, grama, copo, dinheiro
    print(f'I gave you ${dinheiro}')
    dinheiro = 0


def buy_espresso():
    global agua, grama, copo, dinheiro
    nome_lista = ['water', 'coffee beans', 'cups']
    lista = [agua, grama, copo]
    quantia = [250, 16, 1]
    if (agua < 250) or (grama < 16) or (copo == 0):
        cont = 0
        frase = ''
        faltando = ''
        for x in lista:
            if x < quantia[cont]:
                frase = (f'Sorry, not enough {nome_lista[cont]}!')
                faltando = nome_lista[cont]
            cont += 1
        print(frase)
        print(f'Please add more {faltando}')
        print()
    if (agua >= 250) and (grama >= 16) and (copo > 0):
        copo_expresso = 1
        agua -= 250
        grama -= 16
        copo -= copo_expresso
        dinheiro += 4
        print('I have enough resources, making you a coffee!')
        print()


def buy_latte():
    global agua, leite, grama, copo, dinheiro
    nome_lista = ['water', 'milk', 'coffee beans', 'cups']
    lista = [agua, leite, grama, copo]
    quantia = [350, 75, 20, 1]
    if (agua < 350) or (leite < 75) or (grama < 20) or (copo == 0):
        cont = 0
        frase = ''
        faltando = ''
        for x in lista:
            if x < quantia[cont]:
                frase = (f'Sorry, not enough {nome_lista[cont]}!')
                faltando = nome_lista[cont]
            cont += 1
        print(frase)
        print(f'Please add more {faltando}')
        print()
    if (agua >= 350) and (leite >= 75) and (grama >= 20) and (copo > 0):
        copo_coffe_milk = 1
        agua -= 350
        leite -= 75
        grama -= 20
        copo -= copo_coffe_milk
        dinheiro += 7
        print('I have enough resources, making you a coffee!')
        print()



def buy_cappuccino():
    global agua, leite, grama, copo, dinheiro
    nome_lista = ['water', 'milk', 'coffee beans', 'cups']
    lista = [agua, leite, grama, copo]
    quantia = [200, 100, 12, 1]
    if (agua < 200) or (leite < 100) or (grama < 12) or (copo == 0):
        cont = 0
        frase = ''
        faltando = ''
        for x in lista:
            if x < quantia[cont]:
                frase = (f'Sorry, not enough {nome_lista[cont]}!')
                faltando = nome_lista[cont]
            cont += 1
        print(frase)
        print(f'Please add more {faltando}')
        print()
    if (agua >= 200) and (leite >= 100) and (grama >= 12) and (copo > 0):
        copo_caputino = 1
        agua -= 200
        leite -= 100
        grama -= 12
        copo -= copo_caputino
        dinheiro += 6
        print('I have enough resources, making you a coffee!')
        print()


# inicio
op = True
while op:
    print('Write action (buy, fill, take, remaining, exit):')
    op = input()
    if op == 'fill':
        print()
        print('Write how many ml of water do you want to add:')
        aguas = int(input())
        print('Write how many ml of milk do you want to add:')
        leites = int(input())
        print('Write how many grams of coffee beans do you want to add:')
        g = int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        copos = int(input())
        fill(aguas, leites, g, copos)
        print()

    if op == 'take':
        print()
        print('pulling out...')
        time.sleep(1)
        take()
        print()

    if op == 'buy':
        print()
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        op2 = input()
        if op2 == '1':
            print('preparing espresso coffee, please wait ...')
            time.sleep(1)
            buy_espresso()
        elif op2 == '2':
            print('preparing latte coffee, please wait ...')
            time.sleep(1)
            buy_latte()
        elif op2 == '3':
            print('preparing cappuccino coffee, please wait ...')
            time.sleep(1)
            buy_cappuccino()
        elif op2 == 'back':
            print('returning to the menu...')
            time.sleep(1)
            print()
    if op == 'remaining':
        printar()

    if op == 'exit':
        print('leaving please wait...')
        time.sleep(1)
        op = False





