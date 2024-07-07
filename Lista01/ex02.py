class Viagem:
    def __init__(self):
        self.km = 0
        self.hrs = 0
        self.min = 0
    def vel_media(self):
        return (self.km - 0)/((self.hrs+(self.min/60))-0)
    
x = Viagem()
x.km = 450
x.hrs = 6
x.min = 0
print(f'A velocidade média atingida é de {x.vel_media()}')