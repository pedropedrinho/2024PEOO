class EquacaoSegundoGrau:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def delta(self):
        return self.b**2 - 4*self.a*self.c

    def tem_raizes_reais(self):
        return self.delta() >= 0

    def raiz1(self):
        if self.tem_raizes_reais():
            return (-self.b + self.delta()**0.5) / (2*self.a)
        else:
            return None

    def raiz2(self):
        if self.tem_raizes_reais():
            return (-self.b - self.delta()**0.5) / (2*self.a)
        else:
            return None

    def __str__(self):
        return f"Equação: {self.a}x^2 + {self.b}x + {self.c}"

class UI:
    @staticmethod
    def main():
        eq = EquacaoSegundoGrau(a=1, b=-3, c=2)
        print(eq)
        print(f"Delta: {eq.delta()}")
        print(f"Tem raízes reais? {eq.tem_raizes_reais()}")
        print(f"Raiz 1: {eq.raiz1()}")
        print(f"Raiz 2: {eq.raiz2()}")
UI.main()