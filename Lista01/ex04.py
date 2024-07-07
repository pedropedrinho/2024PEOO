class cinema:
    def __init__(self):
        self.dia = ""
        self.hrs = 0
    def calc_entrada(self):
        self.ingresso = 0
        if self.dia == "Segunda":
            self.ingresso = 16
        if self.dia == "Terça":
            self.ingresso = 16
        if self.dia == "Quinta":
            self.ingresso = 16
        return self.ingresso


x = cinema()
x.dia = "Segunda"
print(f'Valor do ingresso hoje é {x.calc_entrada}')