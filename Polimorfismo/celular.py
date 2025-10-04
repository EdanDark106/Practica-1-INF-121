class Celular:
    def __init__(self, nroTel, dueno, espacio_ram, nroApp):
        self.nroTel = nroTel
        self.dueno = dueno
        self.espacio_ram = espacio_ram
        self.nroApp = nroApp

    def __add__(self, other):
        self.espacio_ram += 10
        return self

    def __sub__(self, other):
        self.espacio_ram -= 5
        return self

    def mostrar_datos(self):
        print(f"Datos - Antes: nroTel={self.nroTel}, dueno={self.dueno}, espacio_ram={self.espacio_ram}, nroApp={self.nroApp}")
        return self

celular = Celular(123456789, "Juan", 20, 10)
celular.mostrar_datos()
celular + 1  # Aumenta espacio en 10 GB
celular.mostrar_datos()
celular - 1  # Disminuye espacio en 5 GB
celular.mostrar_datos()