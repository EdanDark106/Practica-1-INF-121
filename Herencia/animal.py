# Clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def desplazarse(self):
        pass  # Método abstracto, a redefinir en subclases

# Subclase Leon
class Leon(Animal):
    def desplazarse(self):
        return f"El {self.nombre} camina"

# Subclase Pinguino
class Pinguino(Animal):
    def desplazarse(self):
        return f"El {self.nombre} nada"

# Subclase Canguro
class Canguro(Animal):
    def desplazarse(self):
        return f"El {self.nombre} salta"

# Crear un arreglo de animales y hacer que se desplacen
animales = [
    Leon("Simba", 5),
    Pinguino("Pingo", 2),
    Canguro("Kanga", 3)
]

# Hacer que cada animal se desplace
for animal in animales:
    print(animal.desplazarse())