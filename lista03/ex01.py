from math import sqrt
class Retangulo:
    def __init__(self, b, h):
        self.__b = b
        self.__h = h
        self.set_base(b)
        self.set_altura(h)
    
    def set_base(self, base):
        if self.__b > 0: self.__b = base
        else: raise ValueError("valor informado invalido")
    def set_altura(self, altura):
        if self.__h > 0: self.__h = altura
        else: raise ValueError("valor informado invalido")
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    
    def calc_area(self):
        return self.__b * self.__h
    def calc_diag(self):
        a = self.__b * self.__b + self.__h * self.__h
        return sqrt(a)
    def __str__(self):
        return f"a altura do retangulo é {self.__h} e a base é {self.__b}"
    
class UI:
    @staticmethod
    def main():
        base = float(input("informe o valor da base: "))
        altura = float(input("informe o valor da altura: "))

        r = Retangulo(base, altura)
        print(r)
        print(f"a area do retangulo é {r.calc_area()}")
        print(f"a diagonal do retangulo é {r.calc_diag()}")

UI.main()