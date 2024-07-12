class Triangulo:
    def __init__(self):                   # Entidade
        self.__b = 0                      # Construtor
        self.__h = 0                      # Atributos encapsulados

    def set_base(self, valor):            # armazenar um valor, ates é feita a validação
        if valor >= 0: self.__b = valor
        else: raise ValueError("Valor da base não pode ser negativo")

    def get_base(self):                   # retornar um valor
        return self.__b

    def set_altura(self, valor):
        if valor >= 0: self.__h = valor
        else: raise ValueError("Valor da altura não pode ser negativo")

    def get_altura(self):
        return self.__h

    def calc_area(self):                # métodos = operação - metodo de instancia
        return self.__b * self.__h / 2
    
class UI:                               # Interface com o usuario
    @staticmethod                       # prints e inputs nessa classe
    def main():                         # operação principal da UI - metodo de classe
        x = Triangulo()
        #x.b = float(input("informe o valor da base: "))
        #x.h = float(input("informe o valor da altura: "))

        x.set_base(float(input(f"informe o valor da base: ")))
        x.set_altura(float(input(f"informe o valor da altura: ")))

        print(f"a altura do triangulo é {x.get_altura()}")
        print(f"a base do triangulo é {x.get_base()}")

        print(f"A area do triangulo é {x.calc_area()}")

UI.main()                                 # Rodar o programa