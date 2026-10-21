# se desa tener un programa que permite transformar temperaruras,para ello se cer la siguiente::
class Termometro:
    def __init__(self, valor: float, unidad: str):
        self.valor = valor
        self.unidad = unidad.upper()
#hacer lo en diferentes clases de 3 
    def convertir_a(self, unidad_destino: str):
        u_origen = self.unidad
        u_destino = unidad_destino.upper()
        temp = self.valor

        if u_origen == u_destino:
            return Termometro(temp, u_destino)

        #I Convertir la temperatura de origen a Celsius como base inter
        if u_origen == "F":
            celsius = (temp - 32) * (5 / 9)
        elif u_origen == "K":
            celsius = temp - 273.15
        else:
            # u_origen == °C
            celsius = temp
        #II Convertir de Celsius a la unidad de destino
        if u_destino == "F":
            resultado = (celsius * 9 / 5) + 32
        elif u_destino == "K":
            resultado = celsius + 273.15
        else:
            #u_destino == °C
            resultado = celsius

        return Termometro(resultado, u_destino)

    def __str__(self):
        return f"{self.valor:.2f} °{self.unidad}"
def main():
    t1 = Termometro(30.2, "C")
    t2 = Termometro(40.2, "F")

    # Conversión
    t2_convertido = t2.convertir_a("C")

    print(f"Termómetro 1: {t1}")
    print(f"Termómetro 2 original: {t2}")
    print(f"Termómetro 2 en Celsius: {t2_convertido}")


if __name__ == "__main__":
    main()
