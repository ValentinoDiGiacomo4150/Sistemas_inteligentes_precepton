import tkinter as tk
from Modelo.PerceptronSimple import PerceptronSimple
from Modelo.Grafico import Grafico
from Vista.Vista import Vista
from Controlador.Controlador import Controlador

def main():
    ventana = tk.Tk()
    ventana.title("Sistema Inteligente - Perceptrón & Juego PPT")
    perceptronSimple = PerceptronSimple()
    vista = Vista(ventana)
    controlador = Controlador(vista, ventana, perceptronSimple)
    ventana.mainloop()

if __name__ == "__main__":
    main()