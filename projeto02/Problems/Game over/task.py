scores = input().split()
n = 0
cont = 0
num = 0
while n != 3:
    if scores[num] == "I":
        n += 1
    elif scores[num] == "C":
        cont += 1
    num += 1
    if num == len(scores):
        break
if n == 3:
    print("Game over")
else:
    print("You won")
print(cont)