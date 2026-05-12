from tkinter import messagebox

class Controlador:

    def __init__(self, Vista, Ventana, PerceptronSimple):
        self.vista = Vista
        self.ventana = Ventana
        self.perceptronSimple = PerceptronSimple

        self.vista.btnEntrenamiento.config(command=self.EventEntrenamiento)
        self.vista.btnAprendizaje.config(command=self.EventAprendizaje)
        self.vista.btnPrueba.config(command=self.EventPrueba)

        # configuramos el cierre seguro de la ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.CerrarProceso)

    def EventEntrenamiento(self):

        self.perceptronSimple.Entrenamiento()

        if self.perceptronSimple.fila == self.perceptronSimple.total_filas:
            self.vista.lblTituloPrincipal.config(text="ENTRENAMIENTO COMPLETADO - DATOS FINALES:")
        else:
            self.vista.lblTituloPrincipal.config(text="ENTRENAMIENTO FALLIDO - DATOS OBTENIDOS:")

        self.vista.lblEntrada1.config(text="Jugador 1: " + str(self.perceptronSimple.getEntradas(0)))
        self.vista.lblEntrada2.config(text="Jugador 2: " + str(self.perceptronSimple.getEntradas(1)))
        
        self.vista.lblPeso1.config(text="Peso J1 (w1): " + str(self.perceptronSimple.w1))
        self.vista.lblPeso2.config(text="Peso J2 (w2): " + str(self.perceptronSimple.w2))
        self.vista.lblUmbral.config(text="Umbral (w0): " + str(self.perceptronSimple.w0))

        self.vista.lblSalidaDeseada.config(text="Resultado Esperado: " + str(self.perceptronSimple.getSalidas(self.perceptronSimple.fila)))
        self.vista.lblSalidaObtenida.config(text="Predicción de la IA: " + str(self.perceptronSimple.y))

    def EventAprendizaje(self):

        if self.perceptronSimple.error != 0.0:

            self.perceptronSimple.Aprendizaje()

            mensaje = "Recalculamos los Pesos\nNuevo Umbral = {}\nNuevo Peso 1 = {}\nNuevo Peso 2 = {}".format(self.perceptronSimple.w0, self.perceptronSimple.w1, self.perceptronSimple.w2)
            messagebox.showinfo("NUEVOS VALORES", mensaje)

    def EventPrueba(self):
        # implementar logica de prueba
        entrada1 = self.vista.jtfEntrada1.get()
        entrada2 = self.vista.jtfEntrada2.get()
        bandera = False

        if entrada1 not in {"1", "-1"} or entrada2 not in {"1", "-1"}:
            messagebox.showerror("Error", "ERROR. Solamente se aceptan valores 1 o -1")
            bandera = True

        if not bandera:
            y = self.perceptronSimple.PruebaFuncionamiento(int(entrada1), int(entrada2))
            self.vista.lblPruebaSalidaObtenida.config(text="Ganador: " + str(y))

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

