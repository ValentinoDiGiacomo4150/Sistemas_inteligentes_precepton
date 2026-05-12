import tkinter as tkinter

from Modelo.PerceptronSimple import PerceptronSimple
from Modelo.Grafico import Grafico
from Vista.Vista import Vista
from Controlador.Controlador import Controlador

ventana = tkinter.Tk()
vista = Vista(ventana)
perceptronSimple = PerceptronSimple()
controlador = Controlador(vista, ventana, perceptronSimple)

ventana.mainloop()
