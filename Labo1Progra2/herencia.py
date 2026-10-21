class Animal:
    def __init__(self, comer, dormir):
        self.comer = comer
        self.dormir = dormir
    def __str__(self):
        return "Comer: {}, Dormir: {}".format(self.comer, self.dormir)
class Perro(Animal):
    def ladrar(self):
        return "Guau guau"
    def __str__(self):
        datos = super().__str__()
        return "Perro:\n{}\nLadrar: {}".format(datos, self.ladrar())
class Gato(Animal):
    def maullar(self):
        return "Miau miau"
    def __str__(self):
        datos = super().__str__()
        return "Gato:\n{}\nMaullar: {}".format(datos, self.maullar())
# Perro
mi_perro = Perro("Carne", "En la noche")
print(mi_perro)

# Gato
mi_gato = Gato("Carne", "En la noche")
print(mi_gato)

#esto es como el lic y se tiene que definir metodos 

class Animal:
    def __init__(self, comer, dormir):
        self.comer = comer
        self.dormir = dormir
    def __str__(self):
        return "Comer: {}, Dormir: {}".\
               format(self.comer, self.dormir)
class Perro(Animal):
    def __init__ (self, comer, dormir, ladrar):
        super().__init__(comer, dormir)
        self.ladrar = ladrar
    def __str__ (self):
        datos = super().__str__()
        return "Perro:\n{}\nladrar: {}".\
               format(datos, self.ladrar)
class Gato(Animal):
    def __init__ (self, comer, dormir, maullar):
        super().__init__(comer, dormir)
        self.maullar = maullar
    def __str__ (self):
        datos = super().__str__()
        return "Gato:\n{}\nmaullar: {}".\
               format(datos, self.maullar)
# perro
mi_perro = Perro("Carne", "En la noche","Guau guau")
print(mi_perro)
mi_gato = Gato("Carne", "En la noche","Miau miau")
print(mi_gato)
