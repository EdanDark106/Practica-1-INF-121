class Parada:
    def __init__(self, admins=None, autos=None, nombreP=None):
        self.admins = admins if admins is not None else [""] * 10
        self.autos = autos if autos is not None else [[""] * 10] * 2
        self.nombreP = nombreP if nombreP is not None else ""

    def __init__(self, admins, autos, nombreP):
        self.admins = admins
        self.autos = autos
        self.nombreP = nombreP

    def mostrar(self):
        print(f"Nombre: {self.nombreP}")
        print("Administradores:", self.admins)
        print("Autos:", self.autos)
        print(f"Modelo: {self.autos[0][0]}")
        print(f"Conductor: {self.autos[0][1]}")
        print(f"Placa: {self.autos[1][0]}")

    def adicionarX(self, admin):
        for i in range(len(self.admins)):
            if self.admins[i] == "":
                self.admins[i] = admin
                break

    def adicionarXYZ(self, x, y, z):
        for i in range(len(self.autos[0])):
            if self.autos[0][i] == "":
                self.autos[0][i] = x  # modelo
                self.autos[1][i] = y  # conductor
                self.autos[0][i+1] = z  # placa
                break

# Example usage
if __name__ == "__main__":
    p = Parada()
    p.adicionarX("Admin1")
    p.adicionarXYZ("Modelo1", "Conductor1", "Placa1")
    p.mostrar()