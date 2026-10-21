class Animal:
    def __init__(self, nombre):
        self._nombre = nombre   # protected


class Perro(Animal):
    def cambiar_nombre(self):
        self._nombre = "Firulais"

    def mostrar_nombre(self):
        print("Nombre:", self._nombre)


perro = Perro("Max")

perro.mostrar_nombre()
perro.cambiar_nombre()

perro.mostrar_nombre()
