class Cinema:
    def __init__(self):
        self.dia = ""
        self.hrs = 0
    
    def sessao(self):
        ingresso = 0
        if self.dia == "Segunda" or self.dia == "Terça" or self.dia == "Quinta":
            ingresso = 16
            #print(f'valor do ingresso está {ingresso},00R$')
            if self.hrs >= 17 <= 24:
                ingresso = ingresso + (ingresso * 50/100)
                print(f"Valor do Ingresso está {int(ingresso)},00R$")
        
        if self.dia == "Quarta":
            ingresso = 8
            print(f"valor do ingresso está {ingresso},00R$")
        
        if self.dia == "Domingo" or self.dia == "sabado" or self.dia == "Sexta":
            ingresso = 20
            if self.hrs >= 17 <= 24:
                ingresso = ingresso + (ingresso * 50/100)
                print(f"Valor do ingresso está {int(ingresso)},00R$")



        
x = Cinema()
x.dia = "Segunda"
x.hrs = 13
x.sessao()