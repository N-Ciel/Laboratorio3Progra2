import random
class Juego:
    def __init__(self, numero_de_vidas):
        self.vidas_iniciales = numero_de_vidas
        self.numero_de_vidas = numero_de_vidas
        self.record = 0

    def reinicia_partida(self):
        self.numero_de_vidas = self.vidas_iniciales

    def actualiza_record(self):
        if self.numero_de_vidas > self.record:
            self.record = self.numero_de_vidas

    def quita_vida(self):
        self.numero_de_vidas -= 1
        if self.numero_de_vidas > 0:
            return True
        print("Te has quedado sin vidas.")
        return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)
        self.numero_a_adivinar = 0

    def valida_numero(self, numero):
        """True si el número está entre 0 y 10, False en caso contrario."""
        return 0 <= numero <= 10

    def genera_numero(self):
        """Genera el número a adivinar (cualquiera entre 0 y 10)."""
        return random.randint(0, 10)

    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = self.genera_numero()
        print("Adivina un número entre 0 y 10")

        while True:
            intento = int(input("Introduce un número: "))

            # Si el número no es válido, se vuelve a pedir (sin quitar vida)
            if not self.valida_numero(intento):
                continue

            if intento == self.numero_a_adivinar:
                print("¡¡Acertaste!!")
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

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)

    def genera_numero(self):
        """Genera un número par entre 0 y 10."""
        return random.randrange(0, 11, 2)

    def valida_numero(self, numero):
        """True si el número es par y está entre 0 y 10."""
        if numero % 2 == 0:
            return super().valida_numero(numero)
        print("Error: debes introducir un número par.")
        return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)

    def genera_numero(self):
        """Genera un número impar entre 0 y 10."""
        return random.randrange(1, 10, 2)

    def valida_numero(self, numero):
        """True si el número es impar y está entre 0 y 10."""
        if numero % 2 != 0:
            return super().valida_numero(numero)
        print("Error: debes introducir un número impar.")
        return False

class Aplicacion:
    @staticmethod
    def main():
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)

        print("=== Juego: adivina número ===")
        juego1.juega()
        print("\n=== Juego: adivina número par ===")
        juego2.juega()
        print("\n=== Juego: adivina número impar ===")
        juego3.juega()

if __name__ == "__main__":
    Aplicacion.main()