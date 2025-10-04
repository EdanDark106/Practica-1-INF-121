# Clase Crucero
class Crucero:
    def __init__(self, nombre, paisOrigen, paisDestino, nroPasajeros, pasajeros):
        self.nombre = nombre
        self.paisOrigen = paisOrigen
        self.paisDestino = paisDestino
        self.nroPasajeros = nroPasajeros
        self.pasajeros = pasajeros

# Clase Pasajero
class Pasajero:
    def __init__(self, nombre, nroHabitacion, costoPasaje):
        self.nombre = nombre
        self.nroHabitacion = nroHabitacion
        self.costoPasaje = costoPasaje
        self.edad = 0  # Inicialmente 0, se puede modificar
        self.genero = ""  # Inicialmente vacío, se puede modificar

# Crear instancias de pasajeros
pasajeros = [
    Pasajero("Juan Vargas", 502, 5000),
    Pasajero("Martina Vasques", 603, 10000),
    Pasajero("Wilmer Montero", 401, 925)
]

# Crear instancia de crucero
crucero = Crucero("Crucero del Mar", "España", "Italia", 3, pasajeros)

# a) Recargar los operadores == y > - leer y mostrar respectivamente en ambas
# Comparación de igualdad
def comparar_igualdad(pasajero1, pasajero2):
    return pasajero1.nombre == pasajero2.nombre and pasajero1.nroHabitacion == pasajero2.nroHabitacion

# Comparación mayor que (por costoPasaje)
def comparar_mayor(pasajero1, pasajero2):
    return pasajero1.costoPasaje > pasajero2.costoPasaje

# Ejemplo de uso
print("Comparación de igualdad entre Juan y Martina:", comparar_igualdad(pasajeros[0], pasajeros[1]))
print("Comparación de mayor costo entre Juan y Martina:", comparar_mayor(pasajeros[0], pasajeros[1]))

# b) Sobrecargar el operador "*" para mostrar la suma total del costo de los pasajes
def calcular_costo_total(pasajeros):
    return sum(p.costoPasaje for p in pasajeros)

print("Suma total del costo de los pasajes:", calcular_costo_total(pasajeros))

# c) Sobrecargar el operador "*" para mostrar cuántas mujeres y cuántos hombres existen en el crucero
def contar_generos(pasajeros):
    hombres = sum(1 for p in pasajeros if p.genero.lower() == "hombre")
    mujeres = sum(1 for p in pasajeros if p.genero.lower() == "mujer")
    return hombres, mujeres

# Asignar géneros de ejemplo (en un caso real, se debería pedir al usuario)
pasajeros[0].genero = "Hombre"
pasajeros[1].genero = "Mujer"
pasajeros[2].genero = "Hombre"

hombres, mujeres = contar_generos(pasajeros)
print(f"Cantidad de hombres: {hombres}, Cantidad de mujeres: {mujeres}")