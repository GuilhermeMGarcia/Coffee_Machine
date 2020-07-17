class Cafeteira():

    def __init__(self, agua, leite, grama, copo, dinheiro):
        self.agua = agua
        self.leite = leite
        self.grama = grama
        self.copo = copo
        self.dinheiro = dinheiro

    def printar(self):
        print('The coffee machine has:')
        print(f'{self.agua} of water')
        print(f'{self.leite} of milk')
        print(f'{self.grama} of coffee beans')
        print(f'{self.copo} of disposable cups')
        print(f'{self.dinheiro} of money')
        print()

    def fill(self, aguas, leites, gramas, copos):
        self.agua += aguas
        self.leite += leites
        self.grama += gramas
        self.copo += copos
        print()
        print('The coffee machine has:')
        print(f'{self.agua} of water')
        print(f'{self.leite} of milk')
        print(f'{self.grama} of coffee beans')
        print(f'{self.copo} of disposable cups')
        print(f'{self.dinheiro} of money')

    def take(self):
        print(f'I gave you ${self.dinheiro}')
        self.dinheiro = 0
        print()
        print('The coffee machine has:')
        print(f'{self.agua} of water')
        print(f'{self.leite} of milk')
        print(f'{self.grama} of coffee beans')
        print(f'{self.copo} of disposable cups')
        print(f'{self.dinheiro} of money')

    def buy_espresso(self):
        copo_expresso = 1
        self.agua -= 250
        self.grama -= 16
        self.copo -= copo_expresso
        self.dinheiro += 4
        print()
        print('The coffee machine has:')
        print(f'{self.agua} of water')
        print(f'{self.leite} of milk')
        print(f'{self.grama} of coffee beans')
        print(f'{self.copo} of disposable cups')
        print(f'{self.dinheiro} of money')

    def buy_latte(self):
        copo_coffe_milk = 1
        self.agua -= 350
        self.leite -= 75
        self.grama -= 20
        self.copo -= copo_coffe_milk
        self.dinheiro += 7
        print()
        print('The coffee machine has:')
        print(f'{self.agua} of water')
        print(f'{self.leite} of milk')
        print(f'{self.grama} of coffee beans')
        print(f'{self.copo} of disposable cups')
        print(f'{self.dinheiro} of money')

    def buy_cappuccino(self):
        copo_caputino = 1
        self.agua -= 200
        self.leite -= 100
        self.grama -= 12
        self.copo -= copo_caputino
        self.dinheiro += 6
        print()
        print('The coffee machine has:')
        print(f'{self.agua} of water')
        print(f'{self.leite} of milk')
        print(f'{self.grama} of coffee beans')
        print(f'{self.copo} of disposable cups')
        print(f'{self.dinheiro} of money')

