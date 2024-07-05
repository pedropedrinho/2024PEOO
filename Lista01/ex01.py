class Circulo:
    def __init__(self):
        self.r = 0
    def calc_area(self):
        return 3.14 * self.r*self.r

a = Circulo()
a.r = 10
print(f' area do circulo é {a.calc_area()}')