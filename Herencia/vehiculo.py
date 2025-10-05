# Clase base Vehiculo
class Vehiculo:
    def __init__(self, tipoCombustible, color):
        self.tipoCombustible = tipoCombustible
        self.color = color

    def mostrar_datos(self):
        return f"Tipo de combustible: {self.tipoCombustible}, Color: {self.color}"

# Clase VehiculoTerrestre
class VehiculoTerrestre(Vehiculo):
    def __init__(self, tipoCombustible, color, marca):
        super().__init__(tipoCombustible, color)
        self.marca = marca

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Marca: {self.marca}"

# Clase VehiculoAereo
class VehiculoAereo(Vehiculo):
    def __init__(self, tipoCombustible, color, autonomiaVuelo):
        super().__init__(tipoCombustible, color)
        self.autonomiaVuelo = autonomiaVuelo

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Autonomía de vuelo: {self.autonomiaVuelo} km"

# Clase Tractor
class Tractor(VehiculoTerrestre):
    def __init__(self, tipoCombustible="Diesel", color="Verde", marca="John Deere"):
        super().__init__(tipoCombustible, color, marca)
        self.fuerzaHP = 100

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Fuerza: {self.fuerzaHP} HP"

# Clase Bus
class Bus(VehiculoTerrestre):
    def __init__(self, tipoCombustible, color, marca, numPasajeros):
        super().__init__(tipoCombustible, color, marca)
        self.numPasajeros = numPasajeros

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Número de pasajeros: {self.numPasajeros}"

# Clase Avion
class Avion(VehiculoAereo):
    def __init__(self, tipoCombustible, color, autonomiaVuelo, numMotores):
        super().__init__(tipoCombustible, color, autonomiaVuelo)
        self.numMotores = numMotores

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Número de motores: {self.numMotores}"

# Clase Helicoptero
class Helicoptero(VehiculoAereo):
    def __init__(self, tipoCombustible, color, autonomiaVuelo, numHelices, esMilitar):
        super().__init__(tipoCombustible, color, autonomiaVuelo)
        self.numHelices = numHelices
        self.esMilitar = esMilitar

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Número de hélices: {self.numHelices}, ¿Militar?: {self.esMilitar}"

# a) Instanciar los siguientes objetos
tractor = Tractor()  # Constructor por defecto
avion = Avion("Jet Fuel", "Blanco", 6000, 2)  # Constructor con parámetros
helicoptero = Helicoptero("Jet Fuel", "Negro", 400, 4, True)  # Constructor con parámetros

# b) Comparar si un tractor y un bus tienen el mismo color, mostrando los datos de ambos objetos
bus = Bus("Diesel", "Verde", "Mercedes", 40)
print("Datos del Tractor:")
print(tractor.mostrar_datos())
print("\nDatos del Bus:")
print(bus.mostrar_datos())
if tractor.color == bus.color:
    print("\nEl tractor y el bus tienen el mismo color.")
else:
    print("\nEl tractor y el bus tienen diferente color.")

# c) Método que verifique si un vehículo es apto para áreas urbanas según criterios
def es_apto_urbanas(vehiculo):
    if isinstance(vehiculo, Bus):
        return vehiculo.numPasajeros >= 20
    return False

print("\n¿El Bus es apto para áreas urbanas?")
print(es_apto_urbanas(bus))

# d) Método que determine si un vehículo aéreo es apto para largos alcances
def es_apto_largos_alcances(vehiculo):
    if isinstance(vehiculo, Avion):
        return vehiculo.autonomiaVuelo >= 5000
    elif isinstance(vehiculo, Helicoptero):
        return vehiculo.autonomiaVuelo >= 500
    return False

print("¿El Avión es apto para largos alcances?")
print(es_apto_largos_alcances(avion))
print("¿El Helicóptero es apto para largos alcances?")
print(es_apto_largos_alcances(helicoptero))