import math
class AlgebraVectorial: # 1. CLASE BASE (Superclase)
    def __init__(self, a=None, b=None):
        self.a = a if a is not None else [0.0, 0.0, 0.0]
        self.b = b if b is not None else [0.0, 0.0, 0.0]
    def modulo(self, v): # Métodos auxilliares reutilizables por las subclases
        suma = v[0]**2 + v[1]**2 + v[2]**2
        return math.sqrt(suma)
    def producto_punto(self, v1, v2):
        return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    def producto_cruz(self, v1, v2):
        rx = v1[1]*v2[2] - v1[2]*v2[1]
        ry = v1[2]*v2[0] - v1[0]*v2[2]
        rz = v1[0]*v2[1] - v1[1]*v2[0]
        return [rx, ry, rz]
    def suma(self, v1, v2):
        return [v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2]]
    def resta(self, v1, v2):
        return [v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2]]
    def evaluar(self): # Método polimórfico (se redefine en cada clase hija)
        pass
class PerpendicularModulo(AlgebraVectorial):# 2. SUBCLASES (Polimorfismo para Perpendicularidad)
    """ Inciso a: |a + b| = |a - b| """
    def evaluar(self):
        suma_v = self.suma(self.a, self.b)
        resta_v = self.resta(self.a, self.b)
        return math.isclose(self.modulo(suma_v), self.modulo(resta_v), abs_tol=1e-5)
class PerpendicularPunto(AlgebraVectorial):
    """ Inciso c: a . b = 0 """
    def evaluar(self):
        dot = self.producto_punto(self.a, self.b)
        return math.isclose(dot, 0.0, abs_tol=1e-5)
class PerpendicularPitagoras(AlgebraVectorial):
    """ Inciso d: |a + b|^2 = |a|^2 + |b|^2 """
    def evaluar(self):
        mod_suma_sq = self.modulo(self.suma(self.a, self.b)) ** 2
        mod_a_sq = self.modulo(self.a) ** 2
        mod_b_sq = self.modulo(self.b) ** 2
        return math.isclose(mod_suma_sq, mod_a_sq + mod_b_sq, abs_tol=1e-5)
# 3. SUBCLASES (Polimorfismo para Paralelismo)
class ParaleloEscalar(AlgebraVectorial):
    """ Inciso e: a = r * b """
    def __init__(self, a, b, r=1.0):
        super().__init__(a, b)
        self.r = r
    def evaluar(self):
        rb = [self.r * self.b[0], self.r * self.b[1], self.r * self.b[2]]
        return (math.isclose(self.a[0], rb[0], abs_tol=1e-5) and
                math.isclose(self.a[1], rb[1], abs_tol=1e-5) and
                math.isclose(self.a[2], rb[2], abs_tol=1e-5))
class ParaleloCruz(AlgebraVectorial):
    """ Inciso f: a x b = 0 """
    def evaluar(self):
        cruz = self.producto_cruz(self.a, self.b)
        return math.isclose(self.modulo(cruz), 0.0, abs_tol=1e-5)
# 4. SUBCLASES (Proyección y Componente)
class ProyeccionVectorial(AlgebraVectorial):
    """ Inciso g: Proy_b a = (a . b / |b|^2) * b """
    def evaluar(self):
        dot = self.producto_punto(self.a, self.b)
        mod_b_sq = self.modulo(self.b) ** 2
        if mod_b_sq == 0:
            return [0.0, 0.0, 0.0]
        factor = dot / mod_b_sq
        return [factor * self.b[0], factor * self.b[1], factor * self.b[2]]
class ComponenteVectorial(AlgebraVectorial):
    """ Inciso h: Comp_b a = (a . b) / |b| """
    def evaluar(self):
        dot = self.producto_punto(self.a, self.b)
        mod_b = self.modulo(self.b)
        if mod_b == 0:
            return 0.0
        return dot / mod_b
#DEMOSTRCAIÓN DEL POLIMORFISMO EN MAIN
if __name__ == "__main__":
    v1 = [1.0, 0.0, 0.0]
    v2 = [0.0, 2.0, 0.0]
    # Lista de objetos de distintas subclases
    operaciones = [
        PerpendicularModulo(v1, v2),
        PerpendicularPunto(v1, v2),
        PerpendicularPitagoras(v1, v2),
        ParaleloCruz(v1, v2),
        ProyeccionVectorial(v1, v2),
        ComponenteVectorial(v1, v2)]
    print("EJECUCIÓN POLIMÓRFICA")
    for op in operaciones:
        # Llamamos al mismo método .evaluar() y cada objeto ejecuta su propia versión
        nombre_clase = op.__class__.__name__
        resultado = op.evaluar()
        print(f"{nombre_clase}: {resultado}")
