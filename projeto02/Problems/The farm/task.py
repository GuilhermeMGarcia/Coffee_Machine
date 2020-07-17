Money = int(input())
HaveMoney = Money
if Money >= 23:
    if Money >= 678:
        if Money >= 1296:
            if Money >= 3848:
                if Money >= 6769:
                    Count = Money // 6769
                    if Count > 1:
                        print(Count, "sheep")
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