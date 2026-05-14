from tkinter import messagebox
from Modelo.Grafico import Grafico

class Controlador:
    def __init__(self, Vista, Ventana, PerceptronSimple):
        self.vista = Vista
        self.ventana = Ventana
        self.perceptronSimple = PerceptronSimple
        self.grafico = Grafico(self.ventana) # Inicializa el gráfico

        self.vista.btnEntrenamiento.config(command=self.EventEntrenamiento)
        self.vista.btnAprendizaje.config(command=self.EventAprendizaje)
        self.vista.btnPrueba.config(command=self.EventPrueba)
        self.ventana.protocol("WM_DELETE_WINDOW", self.CerrarProceso)

    def EventEntrenamiento(self):
        self.perceptronSimple.Entrenamiento()

        if self.perceptronSimple.fila == self.perceptronSimple.total_filas:
            self.vista.lblTituloPrincipal.config(text="ENTRENAMIENTO COMPLETADO", foreground="green")
        else:
            self.vista.lblTituloPrincipal.config(text="ERROR ENCONTRADO - REQUIERE APRENDIZAJE", foreground="red")

        # Actualizar etiquetas de la Vista
        self.vista.lblEntrada1.config(text=f"J1: {self.perceptronSimple.getEntradas(1)}")
        self.vista.lblEntrada2.config(text=f"J2: {self.perceptronSimple.getEntradas(2)}")
        self.vista.lblPeso1.config(text=f"Peso J1 (w1): {round(self.perceptronSimple.w1, 4)}")
        self.vista.lblPeso2.config(text=f"Peso J2 (w2): {round(self.perceptronSimple.w2, 4)}")
        self.vista.lblUmbral.config(text=f"Umbral (w0): {round(self.perceptronSimple.w0, 4)}")

        self.vista.lblSalidaDeseada.config(text=f"Esperado: {self.perceptronSimple.getSalidas(self.perceptronSimple.fila)}")
        self.vista.lblSalidaObtenida.config(text=f"IA dice: {self.perceptronSimple.y}")

        # Graficar la recta actual
        if self.perceptronSimple.w2 != 0:
            x1, x2 = -2, 2
            y1 = (-self.perceptronSimple.w0 - self.perceptronSimple.w1 * x1) / self.perceptronSimple.w2
            y2 = (-self.perceptronSimple.w0 - self.perceptronSimple.w1 * x2) / self.perceptronSimple.w2
            self.grafico.GraficarRecta(x1, x2, y1, y2, self.perceptronSimple.repeticion)

    def EventAprendizaje(self):
        if self.perceptronSimple.error != 0.0:
            self.perceptronSimple.Aprendizaje()
            mensaje = f"Pesos ajustados.\nNuevo w0: {round(self.perceptronSimple.w0,2)}\nNuevo w1: {round(self.perceptronSimple.w1,2)}\nNuevo w2: {round(self.perceptronSimple.w2,2)}"
            messagebox.showinfo("APRENDIZAJE", mensaje)

    def EventPrueba(self):
        try:
            # Extraemos el primer caracter (el número) y lo convertimos
            e1 = int(self.vista.jtfEntrada1.get().split()[0])
            e2 = int(self.vista.jtfEntrada2.get().split()[0])

            y = self.perceptronSimple.PruebaFuncionamiento(e1, e2)

            resultado = "Gana Jugador 1" if y == 1 else "Gana Jugador 2 / Empate"
            self.vista.lblPruebaSalidaObtenida.config(text=resultado)
        except Exception as e:
            messagebox.showerror("Error", "Seleccione valores válidos de la lista")

    def CerrarProceso(self):
        self.ventana.quit()
        self.ventana.destroy()

# mediador entre la vista (tkinter) y el modelo (PerceptronSimpleAND + Grafico).

# recibe eventos de la Vista, delega al Modelo, y devuelve los resultados actualizando los labels de la Vista.

# Eventos
#   EventEntrenamiento()
#     ejecuta un paso de entrenamiento del perceptron
#     actualiza en la Vista: entradas, pesos, umbral, salidas deseada/obtenida
#     calcula los extremos de la recta separadora y llama a GraficarRecta

#   EventAprendizaje()
#     solo actua si el ultimo entrenamiento tuvo error (error != 0)
#     llama a Aprendizaje() para recalcular los pesos
#     muestra un popup con los nuevos valores de w0, w1 y w2

#   EventPrueba()
#     lee las entradas manuales del usuario desde la Vista
#     valida que sean 1 o -1; muestra error si no lo son
#     llama a PruebaFuncionamiento() y muestra el resultado en la Vista

#   CerrarProceso(event)
#     se dispara al cerrar la ventana del grafico matplotlib
#     cierra matplotlib y termina la aplicacion tkinter

# Calculo de la recta separadora (en EventEntrenamiento):
#   la frontera de decision cumple: w0 + w1*x1 + w2*x2 = 0
#   despejando x2:  y = (-w0 - w1*x) / w2
#   se evalua en x=-2 y x=2 para obtener los dos extremos de la recta