# Definición de la clase Fruta
class Fruta:
    def __init__(self, nombre, tipo, nrVitaminas, vitaminas):
        self.nombre = nombre
        self.tipo = tipo
        self.nrVitaminas = nrVitaminas
        self.vitaminas = vitaminas

# a) Instanciar 3 maneras diferentes 3 frutas con al menos 2 vitaminas cada una
fruta1 = Fruta("Kiwi", "subtropical", 3, ["K", "C", "E"])
fruta2 = Fruta("Naranja", "cítrica", 2, ["C", "A"])
fruta3 = Fruta("Manzana", "temperada", 2, ["B", "C"])

# b) Verificar cuál es la fruta con más vitaminas
frutas = [fruta1, fruta2, fruta3]
fruta_max_vitaminas = max(frutas, key=lambda x: x.nrVitaminas)
print(f"La fruta con más vitaminas es {fruta_max_vitaminas.nombre} con {fruta_max_vitaminas.nrVitaminas} vitaminas.")

# c) Mostrar las vitaminas que tiene la fruta x
def mostrar_vitaminas(fruta):
    print(f"Las vitaminas de {fruta.nombre} son: {', '.join(fruta.vitaminas)}")
mostrar_vitaminas(fruta3)  # Ejemplo con Manzana

# d) Cuantas vitaminas son cítricas
def contar_vitaminas_citricas(frutas):
    vitaminas_citricas = set()
    for fruta in frutas:
        if fruta.tipo == "cítrica":
            vitaminas_citricas.update(fruta.vitaminas)
    return len(vitaminas_citricas)
print(f"Número de vitaminas cítricas: {contar_vitaminas_citricas(frutas)}")

# e) Ordenar las frutas alfabéticamente según el nombre de sus vitaminas
frutas.sort(key=lambda x: ''.join(sorted(x.vitaminas)))
for fruta in frutas:
    print(f"{fruta.nombre}: {', '.join(fruta.vitaminas)}")