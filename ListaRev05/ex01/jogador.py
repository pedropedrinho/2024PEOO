class Jogador:
    def __init__(self):
        self.__nome = ""
        self.__camisa = ""
        self.__gols = 0

    def set_nome(self, nome):
        if self.__nome == "": raise ValueError("insira o nome do jogador")
        else: self.__nome = nome
    def set_camisa(self, c):
        if self.__camisa == "": raise ValueError("Insira um nome valido para a camisa")
        else: self.__camisa == c
    def set_gol(self, gol):
        if self.__gols <= 0: raise ValueError("numero de gols invalido")
        else: self.__gols == gol
    def get_nome(self):
        return self.__jogador
    def get_camisa(self):
        return self.__camisa
    def get_gols(self):
        return self.__gols
    def __str__(self):
        return f"Nome: {self.__nome} Nome na camisa: {self.__camisa} Numero de gols: {self.__gols}"