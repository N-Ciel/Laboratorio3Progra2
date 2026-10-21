import math
class MiPunto:
    # Constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # Getter de x
    def getX(self):
        return self.x
    # Getter de y
    def getY(self):
        return self.y
    # Distancia entre este punto y otro punto
    def distancia(self, otro):
        distancia = math.sqrt(
            (self.x - otro.x) ** 2 +
            (self.y - otro.y) ** 2
        )
        return distancia
# Crear el primer punto
punto1 = MiPunto()
# Crear el segundo punto
punto2 = MiPunto(10, 30.5)
# Mostrar los puntos
print("Punto 1:")
print("X =", punto1.getX())
print("Y =", punto1.getY())
print("Punto 2:")
print("X =", punto2.getX())
print("Y =", punto2.getY())
# Calcular la distancia
distancia = punto1.distancia(punto2)
print("La distancia entre los dos puntos es:", distancia)
