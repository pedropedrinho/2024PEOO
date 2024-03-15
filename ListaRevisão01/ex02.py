a = int(input())
b = int(input())
c = int(input())
d = int(input())

md = (a + b + c + d) / 4

print('Média',md)
print('numeros menores que a média')

if a < md: print(a)
if b < md: print(b)
if c < md: print(c)
if d < md: print(d)

print('numeros maiores ou iguais a média')

if a >= md: print(a)
if b >= md: print(b)
if c >= md: print(c)
if d >= md: print(d)