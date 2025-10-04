class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.ci = ci

class Niño(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci, edad, peso, talla):
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, ci)
        self.edad = int(edad)
        self.peso = peso
        self.talla = talla

class ArchNiño:
    def __init__(self):
        self.niños = []

    # a) Crear, leer, listar y mostrar
    def agregar_niño(self, niño):
        self.niños.append(niño)

    def listar_niños(self):
        for niño in self.niños:
            print(f"Nombre: {niño.nombre} {niño.apellidoPaterno} {niño.apellidoMaterno}, "
                  f"Edad: {niño.edad}, Peso: {niño.peso}, Talla: {niño.talla}")

    # b) Cuántos niños tienen el peso adecuado según su talla y edad
    def contar_peso_adecuado(self):
        # Simple logic: Assume weight is adequate if talla > 100 cm and edad > 5
        adecuados = sum(1 for niño in self.niños if float(niño.talla) > 100 and niño.edad > 5)
        return adecuados

    # c) Mostrar los niños que no tienen el peso o la talla adecuada
    def mostrar_no_adecuados(self):
        no_adecuados = [niño for niño in self.niños if float(niño.talla) <= 100 or niño.edad <= 5]
        for niño in no_adecuados:
            print(f"Nombre: {niño.nombre}, Edad: {niño.edad}, Peso: {niño.peso}, Talla: {niño.talla}")

    # d) Determinar el promedio de edad en los niños
    def promedio_edad(self):
        if not self.niños:
            return 0
        return sum(niño.edad for niño in self.niños) / len(self.niños)

    # e) Buscar al niño con el carnet x
    def buscar_por_ci(self, ci):
        for niño in self.niños:
            if niño.ci == ci:
                return f"Nombre: {niño.nombre}, Edad: {niño.edad}, Peso: {niño.peso}, Talla: {niño.talla}"
        return "Niño no encontrado"

    # f) Mostrar los niños con la talla más alta
    def mostrar_talla_maxima(self):
        if not self.niños:
            return
        talla_max = max(float(niño.talla) for niño in self.niños)
        for niño in self.niños:
            if float(niño.talla) == talla_max:
                print(f"Nombre: {niño.nombre}, Talla: {niño.talla}")

# Ejemplo de uso
arch = ArchNiño()
arch.agregar_niño(Niño("Juan", "Perez", "Gomez", "123", 6, "25", "120"))
arch.agregar_niño(Niño("Maria", "Lopez", "Rodriguez", "124", 4, "18", "90"))
arch.agregar_niño(Niño("Pedro", "Gonzalez", "Martinez", "125", 7, "30", "130"))

# a) Listar y mostrar
print("Lista de niños:")
arch.listar_niños()

# b) Contar niños con peso adecuado
print(f"\nNiños con peso adecuado: {arch.contar_peso_adecuado()}")

# c) Mostrar niños no adecuados
print("\nNiños con peso o talla no adecuada:")
arch.mostrar_no_adecuados()

# d) Promedio de edad
print(f"\nPromedio de edad: {arch.promedio_edad():.2f}")

# e) Buscar por carnet
print(f"\nBuscar niño con CI 124: {arch.buscar_por_ci('124')}")

# f) Mostrar niños con talla más alta
print("\nNiños con la talla más alta:")
arch.mostrar_talla_maxima()