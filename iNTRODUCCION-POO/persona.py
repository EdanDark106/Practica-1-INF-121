class Persona:
    def __init__(self, nombre, paterno, materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Paterno: {self.paterno}")
        print(f"Materno: {self.materno}")
        print(f"Edad: {self.edad}")
        print(f"CI: {self.ci}")

    def mayorDeEdad(self):
        return self.edad >= 18

    def modificarEdad(self, nuevo):
        self.edad = nuevo

# Instanciar dos personas
p1 = Persona("Carlos", "Lopez", "Martinez", 25, "123456")
p2 = Persona("Maria", "Lopez", "Gonzalez", 17, "654321")

# Mostrar datos
p1.mostrarDatos()
print("¿Es mayor de edad?", p1.mayorDeEdad())

p2.mostrarDatos()
print("¿Es mayor de edad?", p2.mayorDeEdad())

# Modificar edad de p2
p2.modificarEdad(19)
print("Nueva edad de p2:")
p2.mostrarDatos()

# Verificar si tienen el mismo apellido paterno
if p1.paterno == p2.paterno:
    print("Ambas personas tienen el mismo apellido paterno.")
else:
    print("Las personas no tienen el mismo apellido paterno.")