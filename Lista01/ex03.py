class Banco:
    def __init__(self):
        self.titular = ""
        self.numconta = ""
        self.saldo = 0
    def deposito(self):
        self.saldo = self.saldo + self.depositodin
        return self.saldo
    def sacar(self):
        self.saldo = self.saldo - self.sacardin
        return self.saldo

x = Banco()
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

print(f"seu saldo agora é {x.saldo}")