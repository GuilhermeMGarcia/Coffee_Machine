from cafeteira import Cafeteira

cafeteira = Cafeteira(agua=500, leite=500, grama=500, copo=9, dinheiro=550)
cafeteira.printar()

print('Write action (buy, fill, take):')
op = input()
if op == 'fill':
    print('Write how many ml of water do you want to add:')
    aguas = int(input())
    print('Write how many ml of milk do you want to add:')
    leites = int(input())
    print('Write how many grams of coffee beans do you want to add:')
    g = int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    copos = int(input())
    cafeteira.fill(aguas, leites, g, copos)

if op == 'take':
    cafeteira.take()

if op == 'buy':
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    op2 = int(input())
    if op2 == 1:
        cafeteira.buy_espresso()
    elif op2 == 2:
        cafeteira.buy_latte()
    elif op2 == 3:
        cafeteira.buy_cappuccino()