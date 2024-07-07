class Circulo:
    def __init__(self):
        self.r = 0
    def calc_area(self):
        return 3.14 * self.r*self.r
    def calc_circun(self):
        return 2*3.14*self.r

a = Circulo()
a.r = 15
print(f' area do circulo é {a.calc_area()}')
print(f' circunferência do é {a.calc_circun()}')