class Viagem:
    def __init__(self):
        self.__km = 0
        self.__hrs = 0
        self.__min = 0
        self.__seg = 0
    def set_dist(self, dist):
        if self.__km > 0: self.__km = dist
    def set_tempo(self, tempo):
        t = tempo.split(":")
        self.__hrs = int(t[0])
        self.__min = int(t[0])
        self.__seg = int(t[0])

    