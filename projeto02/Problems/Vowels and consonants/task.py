N = input()
a = 'aeiou'
for i in N:
    if i in a:
       print('vowel')
    else:
        if not i.isalpha():
            break
        else:
            print('consonant')







