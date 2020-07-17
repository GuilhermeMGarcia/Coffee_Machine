Money = int(input())
HaveMoney = Money
if Money >= 23:
    if Money >= 678:
        if Money >= 1296:
            if Money >= 3848:
                if Money >= 6769:
                    Count = Money // 6769
                    if Count > 1:
                        print(Count, "sheeps")
                    else:
                        print("1 sheep")
                else:
                    print("1 cow")
            else:
                Count = Money // 1296
                if Count > 1:
                    print(Count, "pigs")
                else:
                    print("1 pig")
        else:
            print("1 goat")
    else:
        Count = Money // 23
        if Count > 1:
            print(Count, "chickens")
        else:
            print("1 chicken")
else:
    print(None)


Chicken = 23
Goat = 678
Pig = 1296
Cow = 3848
Sheep = 6769
dinheiro = int(input())
Chicken = dinheiro // Chicken
Goat = dinheiro // Goat
Pig = dinheiro // Pig
Cow = dinheiro // Cow
Sheep = dinheiro // Sheep
if Sheep > 0:
        print(f'{Sheep} sheep')
elif Cow > 0:
        if Cow > 1:
            print(f'{Cow} cows')
        else:
            print(f'{Cow} cow')
elif Pig > 0:
        if Goat > 1:
            print(f'{Pig} pigs')
        else:
            print(f'{Pig} pig')
elif Goat > 0:
        if Goat > 1:
            print(f'{Goat} goats')
        else:
            print(f'{Goat} goat')
elif Chicken > 0:
    if Chicken > 1:
        print(f'{Chicken} chickens')
    else:
        print(f'{Chicken} chicken')
else:
    print('None')


