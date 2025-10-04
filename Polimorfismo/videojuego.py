Class Videojuego:
    Def __init__(self, nombre=None, plataforma=None, cantidad_jugadores=0):
        # Constructor básico con valores por defecto
        Self.nombre = nombre
        Self.plataforma = plataforma
        Self.cantidad_jugadores = cantidad_jugadores

    Def __init__(self, nombre, plataforma):
        # Segundo constructor con nombre y plataforma obligatorios
        Self.nombre = nombre
        Self.plataforma = plataforma
        Self.cantidad_jugadores = 0

    Def agregarJugadores(self):
        # Método sobrecargado para agregar un solo jugador
        If self.cantidad_jugadores < 10:  # Límite arbitrario de 10 jugadores
            Self.cantidad_jugadores += 1
            Return f”Se agregó 1 jugador. Total: {self.cantidad_jugadores}”
        Return “Límite de jugadores alcanzado (10).”

    Def agregarJugadores(self, cantidad):
        # Método sobrecargado para agregar una cantidad ingresada por teclado
        Try:
            If cantidad > 0:
                Max_agregar = 10 – self.cantidad_jugadores
                If cantidad > max_agregar:
                    Cantidad = max_agregar
                Self.cantidad_jugadores += cantidad
                Return f”Se agregaron {cantidad} jugadores. Total: {self.cantidad_jugadores}”
            Return “La cantidad debe ser positiva.”
        Except:
            Return “Error en la entrada.”

    # Método para mostrar información
    Def mostrar_info(self):
        Return f”Videojuego: {self.nombre}, Plataforma: {self.plataforma}, Jugadores: {self.cantidad_jugadores}”

# a) Instanciar al menos 2 videojuegos
Juego1 = Videojuego(“Minecraft”, “PC”)
Juego2 = Videojuego(“FIFA 2025”, “PlayStation”, 2)

# Pruebas
Print(juego1.mostrar_info())
Print(juego2.mostrar_info())

# c) Probar métodos agregarJugadores
Print(juego1.agregarJugadores())  
Print(juego1.agregarJugadores(3))  
Print(juego2.agregarJugadores())  
Print(juego2.agregarJugadores(5))