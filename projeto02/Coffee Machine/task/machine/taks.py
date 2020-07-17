from cafe_expresso import  Cafe
# msg_cafeteira
saida = r'''Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!'''
print(saida)
# cafeteira
water = 400
milk = 540
coffee_beans = 120
money = 550
# quantities needed per coffee
water_per_cup = 250
milk_per_cup = 50
beans_per_cup = 15
disposable_cups = 9

# funçoes





# loop_para_opção
opcao = ['buy', 'fill', 'take']

print('The coffee machine has:')
print(f'{water} for water')
print(f'{milk} for milk')
print(f'{coffee_beans} for coffee beans')
print(f'{disposable_cups} of disposable cups')
print(f'{money} for money')
print()
print('Write action (buy, fill, take):')
loop = True
while loop:
        # cups possible based on quantities provided by user
        water_for_n_cups = water // water_per_cup
        milk_for_n_cups = milk // milk_per_cup
        beans_for_n_cups = coffee_beans // beans_per_cup
        # create list to store cups possible by resource to extrapolate min amount of cups that can be brewed
        list = [water_for_n_cups, milk_for_n_cups, beans_for_n_cups]
        enough_for_n_cups = min(list)
        op = str(input())
        if op == 'buy':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
            op_buy = int(input())
            if op_buy == 3:
                Cafe.cafe_caputino(water,milk,coffee_beans,money, 9)
                loop = False
