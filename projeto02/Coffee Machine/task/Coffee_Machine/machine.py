#msg coffe_machine

saida = r'''Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!'''
print(saida)

# quantities needed per coffee
water_per_cup = 200
milk_per_cup = 50
beans_per_cup = 15

# user inputs
print('Water')
water_available = int(input())
print('Milk')
milk_available = int(input())
print('Beans')
beans_available = int(input())
print('Cups')
cups_requested = int(input())

# cups possible based on quantities provided by user
water_for_n_cups = water_available // water_per_cup
milk_for_n_cups = milk_available // milk_per_cup
beans_for_n_cups = beans_available // beans_per_cup

# create list to store cups possible by resource to extrapolate min amount of cups that can be brewed
list = [water_for_n_cups, milk_for_n_cups, beans_for_n_cups]

enough_for_n_cups = min(list)
copos_sobrando = enough_for_n_cups - cups_requested
if enough_for_n_cups == cups_requested:
    print("Yes, I can make that amount of coffee")
elif enough_for_n_cups > cups_requested:
    print(f'Yes, I can make that amount of coffee (and even {copos_sobrando} more than that)')
elif enough_for_n_cups < cups_requested:
    print(f'No, I can make only {enough_for_n_cups} cups of coffee')


