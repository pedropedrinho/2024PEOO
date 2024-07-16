class ContaBancaria:
    def __init__(self, nome_titular, numero_conta, saldo_inicial=0.0):
        self.__nome_titular = nome_titular
        self.__numero_conta = numero_conta
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        """Realiza um saque da conta."""
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def get_saldo(self):
        """Retorna o saldo atual da conta."""
        return self.__saldo

    def set_nome_titular(self, novo_nome):
        """Define o nome do titular da conta."""
        self.__nome_titular = novo_nome

    def get_nome_titular(self):
        """Retorna o nome do titular da conta."""
        return self.__nome_titular

    def set_numero_conta(self, novo_numero):
        """Define o número da conta."""
        self.__numero_conta = novo_numero

    def get_numero_conta(self):
        """Retorna o número da conta."""
        return self.__numero_conta

# Exemplo de uso
class UI:
    @staticmethod
    def main():
        x = ContaBancaria(nome_titular="Pedro", numero_conta="12345", saldo_inicial=1000.0)
        print(f"Titular da conta: {x.get_nome_titular()}")
        print(f"Número da conta: {x.get_numero_conta()}")
        print(f"Saldo atual: R${x.get_saldo():.2f}")

        d = float(input("Informe o valor do deposito: "))
        s = float(input("Informe o valor do saque: "))
        print(f"valor do deposito {d}")
        print(f"valor do saque {s}")

        
        x.depositar(d)
        x.sacar(s)
        
        print(f"Saldo atual: R${x.get_saldo():.2f}")
UI.main()