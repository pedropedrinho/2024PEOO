a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a,b,c,d)
par = []
impar = []

if a%2==0:
    par.append(a)
if b%2==0:
    par.append(b)
if c%2==0:
    par.append(c)
if d%2==0:
    par.append(d)

soma1 = sum(par)

if a%2!=0:
    impar.append(a)
if b%2!=0:
    impar.append(b)
if c%2!=0:
    impar.append(c)
if d%2!=0:
    impar.append(d)

soma2 = sum(impar)

print(f"soma dos pares {soma1}")
print(f"soma dos impares {soma2}")