# Clase padre Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Clase padre Empleado
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Sueldo: {self.sueldo}"

# Clase padre Policia
class Policia(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Grado: {self.grado}"

# Clase hija JefePolicia
class JefePolicia(Empleado, Policia):
    def __init__(self, nombre, edad, sueldo, grado):
        Empleado.__init__(self, nombre, edad, sueldo)
        Policia.__init__(self, nombre, edad, grado)

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Grado: {self.grado}"

# a) Identificar 2 atributos significativos y crear 2 objetos
# Atributos significativos: nombre, sueldo, edad, grado
obj1 = JefePolicia("Juan Pérez", 40, 5000, "Comandante")
obj2 = JefePolicia("María Gómez", 35, 4500, "Teniente")

# b) Mostrar sus datos
print("Datos del objeto 1:")
print(obj1.mostrar_datos())
print("\nDatos del objeto 2:")
print(obj2.mostrar_datos())

# c) Mostrar el nombre de aquel que tiene mayor sueldo
if obj1.sueldo > obj2.sueldo:
    print(f"\nEl de mayor sueldo es: {obj1.nombre}")
elif obj2.sueldo > obj1.sueldo:
    print(f"\nEl de mayor sueldo es: {obj2.nombre}")
else:
    print("\nAmbos tienen el mismo sueldo")

# d) Comparar si ambos tienen mismo grado
if obj1.grado == obj2.grado:
    print(f"Ambos tienen el mismo grado: {obj1.grado}")
else:
    print(f"Los grados son diferentes: {obj1.grado} y {obj2.grado}")