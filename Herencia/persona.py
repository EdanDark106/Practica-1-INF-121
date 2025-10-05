Class Persona:
    Def __init__(self, nombre, apellido, ci):
        Self.nombre = nombre
        Self.apellido = apellido
        Self.ci = ci

    Def method(self):
        Return f”Método genérico de {self.nombre}”

Class Cliente(Persona):
    Def __init__(self, nombre, apellido, ci, nroCompra, idCliente):
        Super().__init__(nombre, apellido, ci)
        Self.nroCompra = nroCompra
        Self.idCliente = idCliente

    Def realizarCompra(self):
        Return f”{self.nombre} realizó la compra {self.nroCompra}”

Class Jefe(Persona):
    Def __init__(self, nombre, apellido, ci, sucursal, tipo):
        Super().__init__(nombre, apellido, ci)
        Self.sucursal = sucursal
        Self.tipo = tipo

    Def asignarTareas(self):
        Return f”{self.nombre} asignó tareas en {self.sucursal}”

# Ejemplo de uso
Persona1 = Persona(“Juan”, “Pérez”, “123456”)
Cliente1 = Cliente(“Ana”, “Gómez”, “789012”, “C001”, “CL001”)
Jefe1 = Jefe(“Luis”, “Martínez”, “345678”, “Sucursal A”, “Gerente”)

Print(persona1.method())
Print(cliente1.realizarCompra())
Print(jefe1.asignarTareas())