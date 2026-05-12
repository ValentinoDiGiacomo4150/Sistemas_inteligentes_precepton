import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Codificación numérica que usaremos (Preparada para el futuro)
# Piedra = -1
# Papel = 0
# Tijera = 1

class Grafico: 

    def __init__(self, Ventana):
        self.ventana = Ventana
        self.figura = plt.figure(figsize=(7, 5), dpi=100) 
        self.subgrafico = self.figura.add_subplot(111)
        
        self.subgrafico.grid(True, linestyle='--', alpha=0.6)

        self.subgrafico.set_title("Espacio de Decisiones: Piedra, Papel o Tijera", 
                                  fontsize=12, fontweight='bold', color='#333333')

        self.subgrafico.set_xlim(-1.5, 1.5)
        self.subgrafico.set_ylim(-1.5, 1.5)

        self.subgrafico.set_xlabel("Jugador 1 (Eje X)", fontsize=10, fontweight='bold')
        self.subgrafico.set_ylabel("Jugador 2 (Eje Y)", fontsize=10, fontweight='bold')

        self.subgrafico.set_xticks([-1, 0, 1])
        self.subgrafico.set_xticklabels(['Piedra\n(-1)', 'Papel\n(0)', 'Tijera\n(1)'], fontsize=9)

        self.subgrafico.set_yticks([-1, 0, 1])
        self.subgrafico.set_yticklabels(['Piedra (-1)', 'Papel (0)', 'Tijera (1)'], fontsize=9)

        self.subgrafico.spines['left'].set_position('zero')
        self.subgrafico.spines['bottom'].set_position('zero')
        self.subgrafico.spines['right'].set_color('none')
        self.subgrafico.spines['top'].set_color('none')

        puntos_x = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        puntos_y = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

        colores_puntos = ['#7f8c8d', '#e74c3c', '#2ecc71', # Empate, Gana J2, Gana J1
                           '#2ecc71', '#7f8c8d', '#e74c3c', # Gana J1, Empate, Gana J2
                           '#e74c3c', '#2ecc71', '#7f8c8d'] # Gana J2, Gana J1, Empate

        textos_resultados = ['Empate', 'Gana J2', 'Gana J1',
                               'Gana J1', 'Empate', 'Gana J2',
                               'Gana J2', 'Gana J1', 'Empate']

        self.scatter = self.subgrafico.scatter(puntos_x, puntos_y, c=colores_puntos, s=150, zorder=5)

        # añadimos los textos de resultado como anotaciones
        for i in range(len(puntos_x)):
            self.subgrafico.annotate(
                textos_resultados[i],
                (puntos_x[i], puntos_y[i]),
                xytext=(0, -20), # Offset hacia abajo
                textcoords="offset points",
                ha='center',
                fontsize=9,
                fontweight='bold',
                color='#34495e',
                zorder=10
            )

        # leyenda de muestra
        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w', label='Empate', markerfacecolor='#7f8c8d', markersize=10),
            plt.Line2D([0], [0], marker='o', color='w', label='Gana J1', markerfacecolor='#2ecc71', markersize=10),
            plt.Line2D([0], [0], marker='o', color='w', label='Gana J2', markerfacecolor='#e74c3c', markersize=10)
        ]
        self.subgrafico.legend(handles=legend_elements, loc='upper right', fontsize=8)


        # lista de rectas dibujadas y anotaciones
        self.lineas = []
        self.anotacion = self.subgrafico.annotate(
            text='',
            xy=(0, 0),
            xytext=(15, 15),
            textcoords="offset points",
            bbox=dict(boxstyle="round", fc="lightyellow"),
            fontsize=8,
            zorder=20
        )
        self.anotacion.set_visible(False)

        # integrar el tkinter
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.ventana)
        self.canvas.draw()
        
        # ubicacion en dashboard
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, pady=(10, 20))

        # al pasar el mouse por arriba de las rectas, da informacion sobre la recta
        self.canvas.mpl_connect('motion_notify_event', self._on_hover)
   
    def _on_hover(self, event):
        # si el mouse esta afuera del area del grafico, oculta el cuadro de texto
        if event.inaxes != self.subgrafico:
            if self.anotacion.get_visible():
                self.anotacion.set_visible(False)
                self.canvas.draw_idle()
            return

        encontrado = False
        for linea, iteracion, ecuacion in self.lineas:
            # contains() devuelve true si el mouse esta suficientemente cerca de la linea
            cerca, _ = linea.contains(event)
            if cerca:
                self.anotacion.xy = (event.xdata, event.ydata)
                self.anotacion.set_text(f"Iteración: {iteracion}\n{ecuacion}")
                self.anotacion.set_visible(True)
                encontrado = True
                break

        if not encontrado and self.anotacion.get_visible():
            self.anotacion.set_visible(False)

        self.canvas.draw_idle()

    def GraficarRecta(self, x1, x2, y1, y2, repeticion):
        """Mantiene la función para graficar la frontera de decisión."""
        # cada iteracion cambia el color
        colores = ['red', 'orange', 'yellow', 'green', 'teal', 'blue', 'purple', 'pink', 'cyan', 'lime']
        color = colores[(repeticion - 1) % len(colores)]

        # ajuste de bordes
        if x1 < -1.5: x1 = -1.5
        if x1 > 1.5: x1 = 1.5
        if x2 < -1.5: x2 = -1.5
        if x2 > 1.5: x2 = 1.5

        if (x2 - x1) != 0:
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            ecuacion = f"y = {m:.2f}x + {b:.2f}"
        else:
            ecuacion = "x = constante"

        x = [x1, x2]
        y = [y1, y2]

        linea, = self.subgrafico.plot(x, y, color=color, linestyle='--', label=f"It. {repeticion}", linewidth=2, picker=5, zorder=15)
        self.lineas.append((linea, repeticion, ecuacion))
        
        self.subgrafico.legend(loc='lower right', fontsize=7) 
        
        self.canvas.draw()


# Gestiona la visualizacion grafica del perceptron dentro de la ventana

# Puntos graficados (tabla de verdad AND)
#   (1, 1)   -> rojo     -> AND = 1
#   (1, -1)  -> verde    -> AND = -1
#   (-1, 1)  -> amarillo -> AND = -1
#   (-1, -1) -> azul     -> AND = -1

# Modificaciones 
#  Las rectas separadoras se acumulan
#  Cada iteracion recibe un color distinto de una paleta de 10 colores
#  Al pasar el mouse sobre una recta aparece un cuadro de texto con el numero de iteracion y la ecuacion de esa recta (y = mx + b)

# Metodos:
#   __init__(Ventana) -> crea el grafico con los 4 puntos iniciales
#   _on_hover(event) -> detecta el mouse sobre rectas y muestra/oculta el tooltip
#   GraficarRecta(x1,x2,y1,y2,repeticion) -> dibuja la recta separadora de la iteracion actual sobre el grafico
