class Buzon:
    def __init__(self, nro, e080j):
        self.nro = nro
        self.e080j = e080j  # Contenido de la tabla

# Definición de la clase Carta
class Carta:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.remitente = None
        self.destinatario = None

# a) Instanciar 3 buzones diferentes, cada uno con al menos 3 cartas
buzon1 = Buzon(001, [
    Carta("C123", "Querido amigo te escribo para decirte que..."),
    Carta("C456", "Hola, ¿cómo estás?"),
    Carta("C789", "Estimada carta...")
])
buzon2 = Buzon(002, [
    Carta("C123", "Querido amigo te escribo para decirte que..."),
    Carta("C456", "Hola, ¿cómo estás?"),
    Carta("C789", "Estimada carta...")
])
buzon3 = Buzon(003, [
    Carta("C123", "Querido amigo te escribo para decirte que..."),
    Carta("C456", "Hola, ¿cómo estás?"),
    Carta("C789", "Estimada carta...")
])

# b) Instanciar 3 cartas con sus respectivos descriptores
carta1 = Carta("C123", "Querido amigo te escribo para decirte que...")
carta2 = Carta("C456", "Hola, ¿cómo estás?")
carta3 = Carta("C789", "Estimada carta...")

# Asignar remitente y destinatario según la tabla
carta1.remitente = "Juan Alvarez"
carta1.destinatario = "Peter Chaves"
carta2.remitente = "Pepe Mujica"
carta2.destinatario = "Wilmer Pérez"
carta3.remitente = "Paty Vasques"
carta3.destinatario = "Pepe Mujica"

# c) Verificar cuántas cartas recibió el destinatario "X"
def contar_cartas_recibidas(cartas, destinatario):
    return sum(1 for carta in cartas if carta.destinatario == destinatario)
print(f"Cartas recibidas por Pepe Mujica: {contar_cartas_recibidas([carta1, carta2, carta3], 'Pepe Mujica')}")

# d) Verificar si algún remitente ha recibido alguna carta y, en ese caso, indicarlo
def verificar_remitente_recibe(carta):
    for c in [carta1, carta2, carta3]:
        if c.remitente == carta.destinatario:
            return f"{carta.remitente} ha recibido una carta como {carta.destinatario}"
    return "Ningún remitente ha recibido carta como destinatario"
print(verificar_remitente_recibe(carta3))  # Ejemplo con carta3

# e) Buscar una palabra clave (por ejemplo, "amor") en las descripciones de las cartas
def buscar_palabra_clave(cartas, palabra):
    for carta in cartas:
        if palabra.lower() in carta.descripcion.lower():
            return f"La carta con código {carta.codigo} contiene la palabra '{palabra}'"
    return f"No se encontró '{palabra}' en ninguna carta"
print(buscar_palabra_clave([carta1, carta2, carta3], "amor"))

# f) Por cada coincidencia, mostrar el código, remitente y destinatario correspondientes
def mostrar_coincidencias(cartas, palabra):
    for carta in cartas:
        if palabra.lower() in carta.descripcion.lower():
            print(f"Código: {carta.codigo}, Remitente: {carta.remitente}, Destinatario: {carta.destinatario}")
mostrar_coincidencias([carta1, carta2, carta3], "amor")