import math
class Vector3D:
    def __init__(self, a1, a2, a3):
        self.a1 = float(a1)
        self.a2 = float(a2)
        self.a3 = float(a3)
    def __add__(self, b): # a) Suma de dos vectores
        return Vector3D(self.a1 + b.a1, self.a2 + b.a2, self.a3 + b.a3)
    def __sub__(self, b): # Resta (necesaria para comprobar la Figura 1)
        return Vector3D(self.a1 - b.a1, self.a2 - b.a2, self.a3 - b.a3)
    def __mul__(self, otro): # b) Escalar * Vector / f) Producto Vectorial (POLIMORFISMO)
        if isinstance(otro, (int, float)):
            return Vector3D(self.a1 * otro, self.a2 * otro, self.a3 * otro)
        elif isinstance(otro, Vector3D):
            c1 = self.a2 * otro.a3 - self.a3 * otro.a2
            c2 = self.a3 * otro.a1 - self.a1 * otro.a3
            c3 = self.a1 * otro.a2 - self.a2 * otro.a1
            return Vector3D(c1, c2, c3)
    def __rmul__(self, otro):
        return self.__mul__(otro)
    # c) Longitud |a|
    def longitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)
    # d) Normal de un vector
    def normal(self):
        mag = self.longitud()
        if mag != 0:
            return Vector3D(self.a1 / mag, self.a2 / mag, self.a3 / mag)
        return None
    # e) Producto escalar
    def producto_escalar(self, b):
        return (self.a1 * b.a1) + (self.a2 * b.a2) + (self.a3 * b.a3)
    # FIGURA 1: Verificación de perpendicularidad (|a + b| == |a - b|)
    def es_perpendicular(self, b):
        diag1 = (self + b).longitud()
        diag2 = (self - b).longitud()
        return round(diag1, 4) == round(diag2, 4)
    # FIGURA 2: Proyección ortogonal de a sobre b
    def proyeccion_sobre(self, b):
        mag_b_cuadrado = b.longitud() ** 2
        if mag_b_cuadrado != 0:
            escalar = self.producto_escalar(b) / mag_b_cuadrado
            return b * escalar
        return None
    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"
#PROGRAMA PRINCIPAL 
if __name__ == "__main__":
    a = Vector3D(3, 4, 0)
    b = Vector3D(0, 5, 0)
    print("--- OPERACIONES BÁSICAS ---")
    print("Vector a:", a)
    print("Vector b:", b)
    print("a) Suma (a + b):", a + b)
    print("b) Escalar (3 * a):", 3 * a)
    print("c) Longitud (|a|):", a.longitud())
    print("d) Normal de a:", a.normal())
    print("e) Producto escalar (a . b):", a.producto_escalar(b))
    print("f) Producto vectorial (a x b):", a * b)
    print("\nRESOLUCIÓN DE LAS FIGURAS")
    print("Figura 1 - ¿Son perpendiculares?:", a.es_perpendicular(b))
    print("Figura 2 - Proyección de a sobre b:", a.proyeccion_sobre(b))
