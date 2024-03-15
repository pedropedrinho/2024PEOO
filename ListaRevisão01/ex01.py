a = int(input())
b = int(input())

'''if a == b:
    print('os numero são iguais!')
#usando max
else: print('o maior é', max(a, b))'''
#não usando max
if a == b:
    print('os numero são iguais!')
elif a > b:
    print('o maior numero é',a)
else:
    print('o maior numero é',b)