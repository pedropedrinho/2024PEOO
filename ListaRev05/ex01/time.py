class Time:
    def __init__(self, nome, estado):
        if self.__nome == "": raise ValueError("Nome de time invalido")
        else: self.__nome = nome
        if self.__estado == "":raise ValueError("Nome de estado invalido")
        else: self.__estado = estado
       
        self.__nome = nome
        self.__estado = estado
        self.__jogadores = []

    def inserir(self, j):
        self.__jogadores.append(j)
    def listar(self):
        return self.__jogadores[:]
    def artilheiro(self):
        return max(self.__jogadores)
    def __str__(self):
        return f"Nome do time: {self.__nome} Estado: {self.__estado} Quantidade de jogadores: {len(self.__jogadores)} "