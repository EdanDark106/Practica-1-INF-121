Class Crucero:
    Def __init__(self, nombre, paisOrigen, paisDestino, nrPasajeros):
        Self.nombre = nombre
        Self.paisOrigen = paisOrigen
        Self.paisDestino = paisDestino
        Self.nrPasajeros = nrPasajeros
        Self.pasajeros = []

    Def __str__(self):  # Sobrecarga del operador + para mostrar
        Return f”Crucero: {self.nombre}, Origen: {self.paisOrigen}, Destino: {self.paisDestino}, Pasajeros: {self.nrPasajeros}”

    Def __add__(self, other):  # Sobrecarga del operador + para leer
        Return f”Leyendo crucero: {self.nombre} y {other.nombre}”

    Def __eq__(self, other):  # Sobrecarga del operador == para suma de costos
        Total_costo = sum(p.costoPasaje for p in self.pasajeros)
        Return f”Suma total de costos del crucero {self.nombre}: ${total_costo}”

    Def __add__(self, other):  # Sobrecarga del operador + para comparar cantidad de pasajeros
        If self.nrPasajeros == other.nrPasajeros:
            Return f”Crucero 1 y Crucero 2 tienen la misma cantidad de pasajeros: {self.nrPasajeros}”
        Return f”Crucero 1 y Crucero 2 tienen diferente cantidad de pasajeros”

Class Pasajero:
    Def __init__(self, nombre, nrHabitacion, costoPasaje, edad, genero):
        Self.nombre = nombre
        Self.nrHabitacion = nrHabitacion
        Self.costoPasaje = costoPasaje
        Self.edad = edad
        Self.genero = genero

    Def __str__(self):  # Sobrecarga del operador + para mostrar
        Return f”Pasajero: {self.nombre}, Habitación: {self.nrHabitacion}, Costo: ${self.costoPasaje}, Edad: {self.edad}, Género: {self.genero}”

    Def __add__(self, other):  # Sobrecarga del operador + para leer
        Return f”Leyendo pasajero: {self.nombre} y {other.nombre}”

    Def __sub__(self, other):  # Sobrecarga del operador – para contar hombres y mujeres
        Hombres = sum(1 for p in [self, other] if p.genero.lower() == “masculino”)
        Mujeres = sum(1 for p in [self, other] if p.genero.lower() == “femenino”)
        Return f”Mujeres: {mujeres}, Hombres: {hombres}”

# a) Instanciar 2 cruceros y 5 pasajeros
Crucero1 = Crucero(“Crucero A”, “España”, “Italia”, 3)
Crucero2 = Crucero(“Crucero B”, “Francia”, “Grecia”, 2)

Pasajeros = [
    Pasajero(“Juan Vargas”, 502, 500, 30, “Masculino”),
    Pasajero(“Martina Vasques”, 603, 1000, 25, “Femenino”),
    Pasajero(“Wilmer Montero”, 401, 925, 35, “Masculino”),
    Pasajero(“Ana Lopez”, 504, 800, 28, “Femenino”),
    Pasajero(“Pedro Gomez”, 305, 600, 40, “Masculino”)
]

# Asignar pasajeros al crucero1
Crucero1.pasajeros = pasajeros[:3]  # Primeros 3 pasajeros
Crucero2.pasajeros = pasajeros[3:]  # Últimos 2 pasajeros
Crucero1.nrPasajeros = len(crucero1.pasajeros)
Crucero2.nrPasajeros = len(crucero2.pasajeros)

# b) Mostrar y leer con operadores + y –
Print(crucero1 + crucero2)  # Leer
Print(crucero1)  # Mostrar
Print(pasajeros[0] + pasajeros[1])  # Leer
Print(pasajeros[0])  # Mostrar

# c) Suma total de costos con ==
Print(crucero1 == crucero2)

# d) Comparar cantidad de pasajeros con +
Print(crucero1 + crucero2)

# e) Contar hombres y mujeres con –
Print(pasajeros[0] – pasajeros[1])