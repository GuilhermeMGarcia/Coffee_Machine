numbers = range(int(input()))
a = []
for number in numbers:
    x = int(input())
    if x % 7 == 0:
       a.append(x ** 2)

for i in a:
    print(i)


