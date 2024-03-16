a = str(input("Digite o horario no formato hh:mm "))
print(a)
b = str(input("Digite o horario no formato hh:mm "))
print(b)

list(a)
list(b)

min1, min2 = int(a[3]+a[4]),int(b[3]+b[4])
hrs, hrs2 = int(a[0]+a[1]),int(b[0]+b[1])

min3 = min1 + min2
hrs3 = hrs + hrs2

if min3 == 60:
    hrs3 += 1
    min3 = 0
    str(min3)
    min3 = "00"

elif min3 > 60:
    hrs3 +=1
    lista = [min1,min2]
    maior,menor  = max(lista), min(lista)
    mintotal = maior - menor
    print(f'Tempo Total: {hrs3:02d}:{mintotal:02d}')