import jogador
import time

class UI:
    @staticmethod
    def menu():
        print("1 - Criar um novo time | 2 - Inserir um jogador | 3 - listar jogadores | 4 - Mostrar artilheiro | 5 - fim")
        return int(input("Digite um numero: "))
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            pass