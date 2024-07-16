class EntradaCinema:
    def __init__(self, dia, horario):
        self.__dia = dia
        self.__horario = horario

    def calcular_valor_entrada(self):
        """Calcula o valor da entrada com base nas regras."""
        valor_base = 0
        if self.__dia in ["segunda", "terça", "quinta"]:
            valor_base = 16.00
        elif self.__dia == "quarta":
            valor_base = 8.00
        elif self.__dia in ["sexta", "sabado", "domingo"]:
            valor_base = 20.00
        else:
            raise ValueError("Dia informado invalido")

        if 17 <= self.__horario < 24:
            valor_base *= 1.5
        else:
            raise ValueError("Horario informado invalido")

        return valor_base

    def get_dia(self):
        """Retorna o dia da sessão."""
        return self.__dia

    def get_horario(self):
        """Retorna o horário da sessão."""
        return self.__horario

# Exemplo de uso
class UI:
    @staticmethod
    def main():
        dia = input("Informe o dia da sessão: ").lower()
        hrs = int(input("informe o horário da sessão: "))

        x = EntradaCinema(dia, hrs)
        print(f"Dia da sessão: {x.get_dia()}")
        print(f"Horário da sessão: {x.get_horario()}h")
        print(f"Valor da entrada: R${x.calcular_valor_entrada():.2f}")
UI.main()