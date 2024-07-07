class banco:
    def __init__(self):
        self.titular = ""
        self.numconta = ""
        self.saldo = 0
    def deposito(self):
        return self.saldo + self.depositodin
    def sacar(self):
        return self.saldo - self.sacardin

x = banco()
x.titular = "Pedro"
x.numconta = "9999999"
x.saldo = 1000
print(f'saldo antes do deposito {x.saldo}')

#depositando dinheiro na conta
x.depositodin = 100
print(f'Saldo depois do deposito {x.deposito()}')

#Sacando dinheiro da conta
x.sacardin = 300
print(f'Saldo depois do saque {x.sacar()}')