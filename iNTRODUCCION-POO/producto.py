class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a vender debe ser mayor que cero.")
            return
        if cantidad > self.stock:
            print("No hay suficiente stock para vender esa cantidad.")
        else:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}.")
    def reabastecer(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a reabastecer debe ser mayor que cero.")
            return
        self.stock += cantidad
        print(f"Se reabastecieron {cantidad} unidades de {self.nombre}.")