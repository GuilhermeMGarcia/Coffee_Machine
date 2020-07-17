class Cafe:

    def cafe_caputino(self,water,milk,coffee_beans,money,disposable_cups):
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
        disposable_cups -= 1
        print('The coffee machine has:')
        print(f'{water} for water')
        print(f'{milk} for milk')
        print(f'{coffee_beans} for coffee beans')
        print(f'{disposable_cups} of disposable cups')
        print(f'{money} for money')




