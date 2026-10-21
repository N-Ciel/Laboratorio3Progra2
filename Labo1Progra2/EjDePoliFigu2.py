
import math

# CLASE PADRE
class Figura:
    def __init__(self, color):
        self.color = color
    def area(self):
        return 0
    def perimetro(self):
        return 0
    def toString(self):
        return "Figura de color " + self.color
# CLASE HIJA: CIRCULO
class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def toString(self):
        return "Círculo de color " + self.color


# CLASE HIJA: RECTANGULO
class Rectangulo(Figura):
    def __init__(self, ancho, alto, color):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def toString(self):
        return "Rectángulo de color " + self.color


# CLASE HIJA: PENTAGONO
class Pentagono(Figura):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return (math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4) * self.lado ** 2

    def perimetro(self):
        return 5 * self.lado

    def toString(self):
        return "Pentágono de color " + self.color


# CREACIÓN DE OBJETOS
circulo = Circulo(5, "Rojo")
rectangulo = Rectangulo(4, 6, "Cian")
pentagono = Pentagono(3, "Verde")


# VECTOR DE FIGURAS
figuras = [circulo, rectangulo, pentagono]


# MOSTRAR LOS DATOS QUE PIDE EL EJERCICIO
print("Area del circulo:", figuras[0].area())
print("Perimetro del rectángulo:", figuras[1].perimetro())
print("Area del pentagono:", figuras[2].area())


# POLIMORFISMO
print("\n--- POLIMORFISMO ---")

for figura in figuras:
    print(figura.toString())
    print("Área:", figura.area())
    print("Perímetro:", figura.perimetro())