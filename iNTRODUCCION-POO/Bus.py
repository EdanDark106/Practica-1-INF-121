class Bus:
    def __init__(self, total_asientos):
        self.total_asientos = total_asientos
        self.pasajeros = 0
        self.total_recaudado = 0.0

    def subir_pasajeros(self, cantidad):
        if cantidad < 0:
            print("No se puede subir una cantidad negativa de pasajeros.")
            return
        if self.pasajeros + cantidad > self.total_asientos:
            print("No hay suficientes asientos disponibles.")
        else:
            self.pasajeros += cantidad
            print(f"{cantidad} pasajeros subieron al bus.")

    def cobrar_pasaje(self):
        costo = 1.50
        if self.pasajeros == 0:
            print("No hay pasajeros para cobrar.")
            return
        self.total_recaudado += self.pasajeros * costo
        print(f"Se cobraron {self.pasajeros * costo} bs. por {self.pasajeros} pasajeros.")

    def asientos_disponibles(self):
        disponibles = self.total_asientos - self.pasajeros
        print(f"Asientos disponibles: {disponibles}")
        return disponibles

mi_bus = Bus(50)  # Supongamos un bus con 50 asientos

mi_bus.subir_pasajeros(10)
mi_bus.cobrar_pasaje()
mi_bus.asientos_disponibles()

mi_bus.subir_pasajeros(40)
mi_bus.cobrar_pasaje()
mi_bus.asientos_disponibles()