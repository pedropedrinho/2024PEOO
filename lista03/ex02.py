class Frete:
    def __init__(self, dist, peso):
        self.__d = dist
        self.__p = peso
        self.set_distancia(dist)
        self.set_peso(peso)

    def set_distancia(self, d):
        if self.__d > 0: self.__d = d
        else: raise ValueError("valor informado invalido")
    def set_peso(self, p):
        if self.__p > 0: self.__p = p
        else: raise ValueError("valor informado invalido")
    def get_distancia(self):
        return self.__dist
    def get_peso(self):
        return self.__p
    
    def calc_frete(self):
        return self.__d * 1 * self.__p
    def __str__(self):
        return f"O peso é {self.__p}Kg e a distância é {self.__d}Km"
    
class UI:
    @staticmethod
    def main():
        distancia = float(input("Informe a distância em Km: "))
        peso = float(input("Informe o peso em Kg: "))

        f = Frete(distancia, peso)
        print(f)
        print(f"Valor total vai ser {f.calc_frete()}centavos")
UI.main()