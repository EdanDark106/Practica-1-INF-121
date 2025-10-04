class Matriz:
    def __init__(self, matriz=None):
        # a) Constructor predeterminado para instanciar un objeto con valores predeterminados
        if matriz is None:
            self.matriz = [[0.0 for _ in range(10)] for _ in range(10)]
        else:
            # b) Constructor para instanciar una matriz con valores proporcionados
            self.matriz = [row[:] for row in matriz]  # Copia profunda

    def sumarMatriz(self, matriz):
        # c) Método para sumar una matriz
        if len(matriz.matriz) != 10 or len(matriz.matriz[0]) != 10:
            return "Error: Las matrices deben ser 10x10"
        resultado = Matriz()
        for i in range(10):
            for j in range(10):
                resultado.matriz[i][j] = self.matriz[i][j] + matriz.matriz[i][j]
        return resultado

    def restarMatriz(self, matriz):
        # c) Método para restar una matriz
        if len(matriz.matriz) != 10 or len(matriz.matriz[0]) != 10:
            return "Error: Las matrices deben ser 10x10"
        resultado = Matriz()
        for i in range(10):
            for j in range(10):
                resultado.matriz[i][j] = self.matriz[i][j] - matriz.matriz[i][j]
        return resultado

    def igualMatriz(self, matriz):
        # d) Método para verificar igualdad entre matrices
        if len(matriz.matriz) != 10 or len(matriz.matriz[0]) != 10:
            return False
        for i in range(10):
            for j in range(10):
                if self.matriz[i][j] != matriz.matriz[i][j]:
                    return False
        return True

    # Método para mostrar la matriz (opcional, para depuración)
    def mostrar(self):
        for fila in self.matriz:
            print(fila)

# Ejemplo de uso
if __name__ == "__main__":
    # a) Instanciar una matriz predeterminada
    m1 = Matriz()
    print("Matriz 1 (predeterminada):")
    m1.mostrar()

    # b) Instanciar una matriz con valores
    m2 = Matriz([[1.0, 2.0, 3.0] + [0.0] * 7 for _ in range(3)] + [[0.0] * 10] * 7)
    print("\nMatriz 2 (con valores):")
    m2.mostrar()

    # c) Sumar y restar matrices (usando m1 y m2 truncadas a 3x3 para ejemplo)
    m3 = m1.sumarMatriz(m2)
    print("\nSuma de matrices:")
    m3.mostrar()

    m4 = m1.restarMatriz(m2)
    print("\nResta de matrices:")
    m4.mostrar()

    # d) Verificar igualdad
    m5 = Matriz([[0.0] * 10 for _ in range(10)])
    print("\n¿m1 es igual a m5?", m1.igualMatriz(m5))