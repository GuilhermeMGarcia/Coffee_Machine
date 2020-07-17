A, B, H = int(input()), int(input()), int(input())

if (A < B) and (A > H):
    print('Deficiency')
else:
    if (A < B) and (B < H):
        print('Excess')
    else:
        print('Normal')

