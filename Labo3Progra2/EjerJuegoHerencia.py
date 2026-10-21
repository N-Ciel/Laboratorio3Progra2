import random
class Juego:
    def __init__(self, numero_de_vidas):
        self.vidas_iniciales = numero_de_vidas
        self.numero_de_vidas = numero_de_vidas
        self.record = 0
    def reinicia_partida(self):
        """Restaura el número de vidas al valor inicial."""
        self.numero_de_vidas = self.vidas_iniciales
    def actualiza_record(self):
        """Si las vidas restantes superan el récord, lo actualiza."""
        if self.numero_de_vidas > self.record:
            self.record = self.numero_de_vidas
    def quita_vida(self):
        """Quita una vida. Devuelve True si aún quedan vidas, False si no."""
        self.numero_de_vidas -= 1
        if self.numero_de_vidas > 0:
            return True
        print("Te has quedado sin vidas.")
        return False
class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)  # se lo pasa al constructor del padre
        self.numero_a_adivinar = 0
    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = random.randint(0, 10)
        print("Adivina un número entre 0 y 10")

        while True:
            intento = int(input("Introduce un número: "))

            if intento == self.numero_a_adivinar:
                print("Acertaste!!")
                self.actualiza_record()
                return

            if self.quita_vida():
                if self.numero_a_adivinar > intento:
                    print("El número a adivinar es mayor. Inténtalo de nuevo.")
                else:
                    print("El número a adivinar es menor. Inténtalo de nuevo.")
            else:
                print(f"El número era {self.numero_a_adivinar}.")
                return

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

if __name__ == "__main__":
    Aplicacion.main()