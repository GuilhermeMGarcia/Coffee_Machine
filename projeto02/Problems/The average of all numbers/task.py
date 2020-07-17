# put your python code here
a, b = int(input()), int(input())
count = 0
x = 0
for i in range(a, b+1):
    if i % 3 == 0:
        count += 1
        x += i
s = x / count
print(s)
