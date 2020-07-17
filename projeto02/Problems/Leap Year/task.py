# put your python code here
ano = int(input())

if ano%4== 0 and ano%100!= 0 or ano%400== 0:
    print("Leap")
else:
    print("Ordinary")
