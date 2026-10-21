class Sensor:
    # Atributo de CLASE: es compartido por todas las instancias
    tipo = "Genérico"
    def __init__(self, id):
        # Atributos de INSTANCIA: cada objeto tiene los suyos
        self.id = id
        self.encendido = False

    def activar(self):
        self.encendido = True
        print(f"[{self.tipo}] Sensor {self.id} activado.")

    def desactivar(self):
        self.encendido = False
        print(f"[{self.tipo}] Sensor {self.id} desactivado.")

class Camara(Sensor):
    # Atributo de CLASE (sobrescribe el de Sensor)
    tipo = "Cámara"

    def __init__(self, id, resolucion, **kwargs):
        super().__init__(id=id, **kwargs)
        # Atributo de INSTANCIA
        self.resolucion = resolucion

class SensorLuzLaser(Sensor):
    # Atributo de CLASE (sobrescribe el de Sensor)
    tipo = "Luz Laser"

    def __init__(self, id, alcance, **kwargs):
        super().__init__(id=id, **kwargs)
        # Atributo de INSTANCIA
        self.alcance = alcance

class VehiculoAutonomo(Camara, SensorLuzLaser):
    # Atributo de CLASE (sobrescribe el de Camara y SensorLuzLaser)
    tipo = "Vehículo Autónomo"

    def __init__(self, id, resolucion, alcance):
        # super() sigue el MRO: Camara -> SensorLuzLaser -> Sensor
        super().__init__(id=id, resolucion=resolucion, alcance=alcance)

if __name__ == "__main__":
    vehiculo = VehiculoAutonomo("VA-001", "1920x1080", 120)

    print("Orden de resolución de métodos (MRO):")
    for clase in VehiculoAutonomo.__mro__:
        print("  ", clase.__name__)

    print()
    print("tipo:", vehiculo.tipo)
    print("id:", vehiculo.id)
    print("resolucion:", vehiculo.resolucion)
    print("alcance:", vehiculo.alcance)
    print("encendido:", vehiculo.encendido)

    print()
    vehiculo.activar()
    print("encendido:", vehiculo.encendido)
    vehiculo.desactivar()
    print("encendido:", vehiculo.encendido)

    print()
    print("Atributos de clase:")
    print("  Sensor.tipo =", Sensor.tipo)
    print("  Camara.tipo =", Camara.tipo)
    print("  SensorLuzLaser.tipo =", SensorLuzLaser.tipo)
    print("  VehiculoAutonomo.tipo =", VehiculoAutonomo.tipo)