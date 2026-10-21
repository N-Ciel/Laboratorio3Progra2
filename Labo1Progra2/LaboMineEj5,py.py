
class Servidor:
    def __init__(self, ju1="joel", diamant=2000):
        self.__jugadores = []
        self.__diamantes = []
        self.__jugadores.append(ju1)
        self.__diamantes.append(diamant)

    def agregarJugador(self, jug, diamant):
        self.__jugadores.append(jug)
        self.__diamantes.append(diamant)

    def mostrar(self):
        for j in range(len(self.__jugadores)):
            print(f"Jugador: {self.__jugadores[j]}, diamantes: {self.__diamantes[j]}")
    def jugadorConMasDiamantes(self):
        if len(self.__diamantes) == 0:
            print("No hay jugadores en el servidor.")
            return
        mayor_diamantes = self.__diamantes[0]
        posicion_mayor = 0
        for i in range(1, len(self.__diamantes)):
            if self.__diamantes[i] > mayor_diamantes:
                mayor_diamantes = self.__diamantes[i]
                posicion_mayor = i-*
        jugador_max = self.__jugadores[posicion_mayor]
        print(f"El jugador con más diamantes es {jugador_max} con {mayor_diamantes} diamantes.")
    def totalDiamantes(self):
        total = 0
        for cantidad in self.__diamantes:
            total += cantidad
            
        print(f"El total de diamantes entre todos los jugadores es: {total}")
class Main():
    s = Servidor()  
    s.agregarJugador("Angel", 5)
    s.agregarJugador("Maria", 3500)
    
    print("jugadores")
    s.mostrar()
    
    print("May diamantes")
    s.jugadorConMasDiamantes()
    
    print("total de dimantes")
    s.totalDiamantes()
