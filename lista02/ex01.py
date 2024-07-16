class Circulo:
    def __init__(self):
        self.__r = 0
    
    def set_raio(self, raio):
        if raio >= 0: self.__r= raio
        else: raise ValueError("o valor do raio nao pode ser negativo.")
    
    def get_raio(self):
        return self.__r 
    
    def calc_circun(self):
        return self.__r*2*3.14
    
    def calc_area(self):
        return 3.14 *(self.__r * self.__r)

class UI:
    @staticmethod
    def main():
        c = Circulo()
        c.set_raio(float(input("informe o valor do raio: ")))
        print(f"o comprimento da circunferencia é: {c.calc_circun()}")
        print(f"o valor da area é: {c.calc_area()}")
UI.main()