class Viagem:
    def __init__(self):
        self.__km = 0
        self.__hrs = 0
    
    def set_dist(self, dist): #distancia em km
        if dist > 0: 
            self.__km = dist
        else:
            raise ValueError("distancia inserida invalida")
    
    def set_tempo(self, tempo): #hh:mm
        t = tempo.split(":")
        t0 = int(t[0])
        t1 = int(t[1])
        self.__hrs = (t1/60) + t0
        
        if t0 < 0 or t1 < 0 or t0 + t1 == 0:
            raise ValueError("Valor do tempo invalido")
        
        
     
    def get_tempo(self):
        return self.__hrs

    def get_dist(self):
        return self.__km

    def vel_media(self):
        d_dist = self.__km - 0
        d_tempo = self.__hrs - 0
        return d_dist/d_tempo
    
class UI:
    @staticmethod
    def main():
        x = Viagem()

        dista = int(input("informe a distancia em km: "))
        temp = input("Informe o tempo no formato hh:mm ")

        x.set_dist(dista)
        x.set_tempo(temp)

        print(f"a velocidade média é de {x.vel_media()}")

UI.main()