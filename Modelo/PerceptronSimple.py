import random

class PerceptronSimple:

    def __init__(self):
        self.entradas = [
            [1.0, 1.0, 1.0],
            [1.0, 1.0, -1.0],
            [1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0]
        ]
        self.salidas = [1.0, -1.0, -1.0, -1.0]

        self.total_filas = len(self.entradas)

        self.factor_aprendizaje = 0.6
        # pesos decimales aleatorios
        self.w0 = random.random()
        self.w1 = random.random()
        self.w2 = random.random()
        
        self.y = 0.0
        self.error = 0.0
        self.fila = 0
        self.repeticion = 1
        self.bandera = True
    
    # metodo para configurar los datos
    def configurar_datos(self, nuevas_entradas, nuevas_salidas):
        self.entradas = nuevas_entradas
        self.salidas = nuevas_salidas
        self.total_filas = len(self.entradas)
        self.fila = 0
        self.repeticion = 1
        self.bandera = True
        # crear una lista dinamica de pesos en lugar de usar solo w0, w1 y w2.
        self.pesos = [random.random() for _ in range(len(self.entradas[0]))]

    def getEntradas(self, X):
        # adaptado para funcionar con cualquier cantidad de filas
        if self.fila >= self.total_filas:
            return self.entradas[self.total_filas - 1][X]
        else:
            return self.entradas[self.fila][X]
        
    def getSalidas(self, X):
        if X >= self.total_filas:
            return self.salidas[self.total_filas - 1]
        else:
            return self.salidas[X]
    
    def Entrenamiento(self):
        if self.bandera == True:
            print(f"PERCEPTRON ENTRENANDO")
            print(f"ITERACION: {self.repeticion} -------------------------------------")

            # como antes eran 4 filas estaticas, para esta modificacion usamos self.total_filas (para que fuincione con n filas )
            while self.fila < self.total_filas: 
                self.y = self.w0 * self.entradas[self.fila][0] + self.w1 * self.entradas[self.fila][1] + self.w2 * self.entradas[self.fila][2]

                if self.y > 0:
                    self.y = 1
                else:
                    self.y = -1

                self.error = self.salidas[self.fila] - self.y
                print(f"Error = {self.error}")

                if self.error == 0.0:
                    self.fila += 1
                else:
                    break
            
            # como antes eran 4 filas estaticas, para esta modificacion usamos self.total_filas (para que fuincione con n filas )
            if self.fila == self.total_filas: 
                print("ENTRENAMIENTO EXITOSO")
                self.bandera = False

    def Aprendizaje(self):
        # se mantiene igual
        self.w0 = self.w0 + (self.factor_aprendizaje * self.error * self.entradas[self.fila][0])
        self.w1 = self.w1 + (self.factor_aprendizaje * self.error * self.entradas[self.fila][1])
        self.w2 = self.w2 + (self.factor_aprendizaje * self.error * self.entradas[self.fila][2])

        self.fila = 0
        self.repeticion += 1

    def PruebaFuncionamiento(self, entrada1, entrada2):
        y = (self.w0 * 1) + (self.w1 * entrada1) + (self.w2 * entrada2)
        if y > 0: return 1
        else: return -1

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

