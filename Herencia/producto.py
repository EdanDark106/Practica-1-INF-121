# Definición de las clases según el diagrama UML
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Bebida(Producto):
    def __init__(self, nombre, precio, contenido, gaseosa):
        super().__init__(nombre, precio)
        self.contenido = contenido  # en litros
        self.gaseosa = gaseosa      # booleano

class Comida(Producto):
    def __init__(self, nombre, precio, calorias):
        super().__init__(nombre, precio)
        self.calorias = calorias    # en calorías

# a) Agregar un nuevo producto "No comestible"
class NoComestible(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

# b) Instanciar 5 productos distintos
bebida1 = Bebida("Agua", 1.5, 0.5, False)
bebida2 = Bebida("Refresco", 2.0, 0.33, True)
comida1 = Comida("Sandwich", 3.5, 300)
comida2 = Comida("Ensalada", 2.5, 150)
no_comestible1 = NoComestible("Bolígrafo", 0.5)

# c) Crear un método para ver el nombre y el precio de un producto
def ver_detalles(producto):
    return f"Nombre: {producto.nombre}, Precio: ${producto.precio}"

# d) Almacenar los productos en un arreglo y comparar una bebida y un no comestible
productos = [bebida1, bebida2, comida1, comida2, no_comestible1]

# Comparar una bebida y un no comestible (ejemplo: bebida1 y no_comestible1)
bebida_ejemplo = bebida1
no_comestible_ejemplo = no_comestible1

print("Detalles de la bebida:", ver_detalles(bebida_ejemplo))
print("Detalles del no comestible:", ver_detalles(no_comestible_ejemplo))
print("Comparación de precios:", "La bebida es más cara" if bebida_ejemplo.precio > no_comestible_ejemplo.precio else "El no comestible es más caro o igual")