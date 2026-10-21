#se debe realizar un programa para medir la temperatura
# -----------------------------------------
# 1. KELVIN A CELSIUS
# -----------------------------------------

class KelvinACelsius:

    def convertir(self, kelvin):
        return kelvin - 273.15


# -----------------------------------------
# 2. KELVIN A FAHRENHEIT
# -----------------------------------------

class KelvinAFahrenheit:

    def convertir(self, kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32


# -----------------------------------------
# 3. FAHRENHEIT A CELSIUS
# -----------------------------------------

class FahrenheitACelsius:

    def convertir(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9


# -----------------------------------------
# 4. FAHRENHEIT A KELVIN
# -----------------------------------------

class FahrenheitAKelvin:

    def convertir(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9 + 273.15


# -----------------------------------------
# 5. CELSIUS A KELVIN
# -----------------------------------------

class CelsiusAKelvin:

    def convertir(self, celsius):
        return celsius + 273.15


# -----------------------------------------
# 6. CELSIUS A FAHRENHEIT
# -----------------------------------------

class CelsiusAFahrenheit:

    def convertir(self, celsius):
        return (celsius * 9 / 5) + 32


# =========================================
# PROGRAMA PRINCIPAL
# =========================================

print("CONVERSOR DE TEMPERATURAS")
print("--------------------------")

print("1. Kelvin a Celsius")
print("2. Kelvin a Fahrenheit")
print("3. Fahrenheit a Celsius")
print("4. Fahrenheit a Kelvin")
print("5. Celsius a Kelvin")
print("6. Celsius a Fahrenheit")

opcion = int(input("\nSeleccione una opción: "))

temperatura = float(input("Ingrese la temperatura: "))


# Kelvin a Celsius
if opcion == 1:

    conversion = KelvinACelsius()
    resultado = conversion.convertir(temperatura)

    print(f"\nResultado: {resultado:.2f} °C")


# Kelvin a Fahrenheit
elif opcion == 2:

    conversion = KelvinAFahrenheit()
    resultado = conversion.convertir(temperatura)

    print(f"\nResultado: {resultado:.2f} °F")


# Fahrenheit a Celsius
elif opcion == 3:

    conversion = FahrenheitACelsius()
    resultado = conversion.convertir(temperatura)

    print(f"\nResultado: {resultado:.2f} °C")


# Fahrenheit a Kelvin
elif opcion == 4:

    conversion = FahrenheitAKelvin()
    resultado = conversion.convertir(temperatura)

    print(f"\nResultado: {resultado:.2f} K")


# Celsius a Kelvin
elif opcion == 5:

    conversion = CelsiusAKelvin()
    resultado = conversion.convertir(temperatura)

    print(f"\nResultado: {resultado:.2f} K")


# Celsius a Fahrenheit
elif opcion == 6:

    conversion = CelsiusAFahrenheit()
    resultado = conversion.convertir(temperatura)

    print(f"\nResultado: {resultado:.2f} °F")


else:

    print("Opción no válida")
