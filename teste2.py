a = "aiosnfiag@"
for x in a:
    if x == "@":
        print("valido")
        break  # Para evitar imprimir "invalido" para os outros caracteres após encontrar "@"
else:
    print("invalido")