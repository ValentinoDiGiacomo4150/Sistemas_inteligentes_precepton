import random

class PerceptronSimple:
    def __init__(self):
        # Mapeo: Piedra = -1, Papel = 0, Tijera = 1
        # [Bias, J1, J2]
        self.entradas = [
            [1.0, -1.0, -1.0], # Piedra vs Piedra -> Empate (-1)
            [1.0, -1.0,  0.0], # Piedra vs Papel  -> Gana J2 (-1)
            [1.0, -1.0,  1.0], # Piedra vs Tijera -> Gana J1 (1)
            [1.0,  0.0, -1.0], # Papel  vs Piedra -> Gana J1 (1)
            [1.0,  0.0,  0.0], # Papel  vs Papel  -> Empate (-1)
            [1.0,  0.0,  1.0], # Papel  vs Tijera -> Gana J2 (-1)
            [1.0,  1.0, -1.0], # Tijera vs Piedra -> Gana J2 (-1)
            [1.0,  1.0,  0.0], # Tijera vs Papel  -> Gana J1 (1)
            [1.0,  1.0,  1.0]  # Tijera vs Tijera -> Empate (-1)
        ]
        self.salidas = [-1.0, -1.0, 1.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0]

        self.total_filas = len(self.entradas)
        self.factor_aprendizaje = 0.5
        self.w0 = random.uniform(-1, 1)
        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)

        self.y = 0.0
        self.error = 0.0
        self.fila = 0
        self.repeticion = 1
        self.bandera = True

    def getEntradas(self, X):
        index = min(self.fila, self.total_filas - 1)
        return self.entradas[index][X]

    def getSalidas(self, X):
        index = min(X, self.total_filas - 1)
        return self.salidas[index]

    def Entrenamiento(self):
        if self.bandera:
            while self.fila < self.total_filas:
                # Cálculo de la suma ponderada
                suma = (self.w0 * self.entradas[self.fila][0] +
                        self.w1 * self.entradas[self.fila][1] +
                        self.w2 * self.entradas[self.fila][2])

                self.y = 1 if suma > 0 else -1
                self.error = self.salidas[self.fila] - self.y

                if self.error == 0.0:
                    self.fila += 1
                else:
                    break

            if self.fila == self.total_filas:
                self.bandera = False

    def Aprendizaje(self):
        self.w0 += self.factor_aprendizaje * self.error * self.entradas[self.fila][0]
        self.w1 += self.factor_aprendizaje * self.error * self.entradas[self.fila][1]
        self.w2 += self.factor_aprendizaje * self.error * self.entradas[self.fila][2]
        self.fila = 0
        self.repeticion += 1

    def PruebaFuncionamiento(self, entrada1, entrada2):
        suma = (self.w0 * 1) + (self.w1 * entrada1) + (self.w2 * entrada2)
        return 1 if suma > 0 else -1

# contiene toda la logica matematica del perceptron simple aplicado a la compuerta logica AND

# Tabla de verdad AND
#   Entrada 0 (bias)  Entrada 1  Entrada 2  Salida esperada
#        1               1           1            1
#        1               1          -1           -1
#        1              -1           1           -1
#        1              -1          -1           -1

# Atributos
#   w0, w1, w2 -> pesos del perceptron, inicializados aleatoriamente
#   factor_aprendizaje -> tasa de aprendizaje (0.6)
#   fila -> fila actual de la tabla evaluada (0 a 3)
#   repeticion -> iteracion actual
#   error -> diferencia entre salida deseada y obtenida
#   y -> salida calculada en el ultimo paso (-1 o 1)
#   bandera -> se vuelve False cuando el entrenamiento finaliza

# Metodos:
#   __init__() -> inicializa tabla de verdad y pesos aleatorios
#   getEntradas(X) -> devuelve la entrada X de la fila actual
#   getSalidas(X) -> devuelve la salida esperada de la fila X
#   Entrenamiento() -> calcula y y error para la fila actual, avanza si error=0, se detiene si hay error
#   Aprendizaje() -> ajusta pesos con la regla del perceptron: w_nuevo = w + (alpha * error * entrada), luego resetea fila=0 y avanza
#   PruebaFuncionamiento() -> clasifica entradas manuales con los pesos finales
