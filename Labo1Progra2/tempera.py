class Temperatura:
    def __init__(self, valor: float, unidad: str):
        self.valor = valor
        self.unidad = unidad.upper().strip()

    def _a_celsius(self) -> float:
        """Método auxiliar interno: convierte la unidad de origen a Celsius."""
        if self.unidad == "C":
            return self.valor
        elif self.unidad == "F":
            return (self.valor - 32) * (5 / 9)
        elif self.unidad == "K":
            return self.valor - 273.15
        else:
            raise ValueError(f"Unidad no soportada: {self.unidad}")

    def convertir(self, unidad_destino: str) -> "Temperatura":
        """Convierte la temperatura actual a la unidad de destino deseada."""
        u_dest = unidad_destino.upper().strip()
        celsius = self._a_celsius()

        if u_dest == "C":
            nuevo_valor = celsius
        elif u_dest == "F":
            nuevo_valor = (celsius * 9 / 5) + 32
        elif u_dest == "K":
            nuevo_valor = celsius + 273.15
        else:
            raise ValueError(f"Unidad de destino no válida: {unidad_destino}")

        return Temperatura(nuevo_valor, u_dest)

    def __str__(self):
        return f"{self.valor:.2f} °{self.unidad}"


# --- EJEMPLO DE USO Y PRUEBAS ---
def main():
    # Puedes crear un objeto indicando qué dato tienes (Celsius, Kelvin o Fahrenheit)
    temp1 = Temperatura(30.2, "C")
    temp2 = Temperatura(40.2, "F")
    temp3 = Temperatura(300.0, "K")

    print(f"Dato de entrada 1: {temp1}")
    print(f"Dato de entrada 2: {temp2}")
    print(f"Dato de entrada 3: {temp3}")
    print("-" * 40)

    # Conversiones a la unidad que tú elijas:
    print(f"De {temp1} a Kelvin: {temp1.convertir('K')}")
    print(f"De {temp2} a Celsius: {temp2.convertir('C')}")
    print(f"De {temp3} a Fahrenheit: {temp3.convertir('F')}")


if __name__ == "__main__":
    main()
