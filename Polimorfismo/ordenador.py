class Ordenador:
    def __init__(self, codigo_serial, numero, memoria_ram, estado):
        self.codigo_serial = codigo_serial
        self.numero = numero
        self.memoria_ram = memoria_ram
        self.estado = estado

    def __str__(self):
        return f"Código: {self.codigo_serial}, Núm: {self.numero}, RAM: {self.memoria_ram}, Estado: {self.estado}"

class Laboratorio:
    def __init__(self, nombre, capacidad, cantidad_ordenadores):
        self.nombre = nombre
        self.capacidad = capacidad
        self.cantidad_ordenadores = cantidad_ordenadores
        self.ordenadores = []

    def agregar_ordenador(self, ordenador):
        if len(self.ordenadores) < self.capacidad:
            self.ordenadores.append(ordenador)
            self.cantidad_ordenadores += 1
        else:
            print("Capacidad máxima alcanzada.")

    def informacion(self):
        print(f"Laboratorio: {self.nombre}, Capacidad: {self.capacidad}, Cantidad: {self.cantidad_ordenadores}")
        for ord in self.ordenadores:
            print(ord)

# a) Crear laboratorios y ordenadores
lab1 = Laboratorio("Lasin 1", 3, 0)
lab2 = Laboratorio("Lasin 2", 3, 0)

# Añadir ordenadores con datos adecuados
ord1 = Ordenador("S001", 1, "8GB", "activo")
ord2 = Ordenador("S002", 2, "4GB", "inactivo")
ord3 = Ordenador("S003", 3, "8GB", "activo")
ord4 = Ordenador("S004", 1, "4GB", "activo")
ord5 = Ordenador("S005", 2, "8GB", "inactivo")
ord6 = Ordenador("S006", 3, "4GB", "activo")

lab1.agregar_ordenador(ord1)
lab1.agregar_ordenador(ord2)
lab1.agregar_ordenador(ord3)
lab2.agregar_ordenador(ord4)
lab2.agregar_ordenador(ord5)
lab2.agregar_ordenador(ord6)

# b) Sobrecarga del método "informacion"
def informacion(lab, filtro=None):
    if not filtro:
        lab.informacion()
    elif filtro == "estado":
        print(f"Ordenadores por estado en {lab.nombre}:")
        activos = [o for o in lab.ordenadores if o.estado == "activo"]
        inactivos = [o for o in lab.ordenadores if o.estado == "inactivo"]
        print("Activos:", [o.__str__() for o in activos])
        print("Inactivos:", [o.__str__() for o in inactivos])
    elif filtro == "laboratorio":
        lab.informacion()
    elif filtro == "ram":
        print(f"Ordenadores con más de 8GB RAM en {lab.nombre}:")
        print([o.__str__() for o in lab.ordenadores if int(o.memoria_ram.replace("GB", "")) > 8])

# Mostrar por estado
informacion(lab1, "estado")
informacion(lab2, "estado")

# Mostrar por laboratorio dado (lab1)
informacion(lab1, "laboratorio")

# Mostrar ordenadores con más de 8GB RAM
informacion(lab1, "ram")

# c) Función para trasladar ordenadores
def trasladar_ordenadores(origen, destino, codigos):
    for cod in codigos:
        ord_a_trasladar = next((o for o in origen.ordenadores if o.codigo_serial == cod), None)
        if ord_a_trasladar:
            origen.ordenadores.remove(ord_a_trasladar)
            origen.cantidad_ordenadores -= 1
            destino.agregar_ordenador(ord_a_trasladar)
            print(f"Trasladado {ord_a_trasladar} de {origen.nombre} a {destino.nombre}")
            print(f"Antes en {origen.nombre}: {[o.__str__() for o in origen.ordenadores]}")
            print(f"Después en {destino.nombre}: {[o.__str__() for o in destino.ordenadores]}")

# Ejemplo de traslado
trasladar_ordenadores(lab1, lab2, ["S001"])