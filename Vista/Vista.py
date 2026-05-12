import tkinter as tk
from tkinter import ttk

class Vista:

    def __init__(self, ventana):
        self.ventana = ventana
        ventana.geometry("850x550")
        ventana.title("Perceptrón: Piedra, Papel o Tijera")
        ventana.configure(bg="#f4f4f4")

        fuenteTitulos = ("Helvetica", 12, "bold")
        fuenteNormal = ("Helvetica", 10)

        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure('EstiloBoton.TButton', font=fuenteNormal, padding=5)
        estilo.configure('TLabelframe', background="#f4f4f4", font=("Helvetica", 11, "bold"))
        estilo.configure('TLabelframe.Label', background="#f4f4f4", foreground="#333333")
        estilo.configure('TLabel', background="#f4f4f4", font=fuenteNormal)

        self.lblTituloPrincipal = tk.Label(ventana, text="HAGA CLICK EN 'Entrenamiento' PARA COMENZAR", 
                                           font=("Helvetica", 14, "bold"), bg="#f4f4f4", fg="#2c3e50", pady=15)
        self.lblTituloPrincipal.grid(row=0, column=0, columnspan=2)

        # ==========================================
        # FRAME 1: PANEL DE CONTROL
        # ==========================================
        frame_controles = ttk.LabelFrame(ventana, text="⚙️ Panel de Control", padding=15)
        frame_controles.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        self.btnEntrenamiento = ttk.Button(frame_controles, text="▶ Entrenamiento", style='EstiloBoton.TButton')
        self.btnEntrenamiento.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

        self.btnAprendizaje = ttk.Button(frame_controles, text="↻ Aprendizaje", style='EstiloBoton.TButton')
        self.btnAprendizaje.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        self.lblFactorAprendizaje = ttk.Label(frame_controles, text="Factor Aprendizaje: 0.6", font=("Helvetica", 9, "italic"))
        self.lblFactorAprendizaje.grid(row=2, column=0, pady=(20, 0))

        # ==========================================
        # FRAME 2: ESTADO DEL PERCEPTRÓN
        # ==========================================
        frame_estado = ttk.LabelFrame(ventana, text="📊 Memoria y Estado", padding=15)
        frame_estado.grid(row=1, column=1, sticky="nsew", padx=20, pady=10)

        ttk.Label(frame_estado, text="Pesos Sinápticos:", font=fuenteTitulos).grid(row=0, column=0, sticky="w", pady=(0,5))
        self.lblUmbral = ttk.Label(frame_estado, text="Umbral (w0): -")
        self.lblUmbral.grid(row=1, column=0, sticky="w", padx=10, pady=2)
        self.lblPeso1 = ttk.Label(frame_estado, text="Peso J1 (w1): -")
        self.lblPeso1.grid(row=2, column=0, sticky="w", padx=10, pady=2)
        self.lblPeso2 = ttk.Label(frame_estado, text="Peso J2 (w2): -")
        self.lblPeso2.grid(row=3, column=0, sticky="w", padx=10, pady=2)

        ttk.Label(frame_estado, text="Partida Evaluada:", font=fuenteTitulos).grid(row=0, column=1, sticky="w", padx=30, pady=(0,5))
        self.lblEntrada1 = ttk.Label(frame_estado, text="Jugador 1: -")
        self.lblEntrada1.grid(row=1, column=1, sticky="w", padx=40, pady=2)
        self.lblEntrada2 = ttk.Label(frame_estado, text="Jugador 2: -")
        self.lblEntrada2.grid(row=2, column=1, sticky="w", padx=40, pady=2)
        
        self.lblSalidaDeseada = ttk.Label(frame_estado, text="Resultado Esperado: -", foreground="#2980b9", font=("Helvetica", 10, "bold"))
        self.lblSalidaDeseada.grid(row=3, column=1, sticky="w", padx=40, pady=2)
        self.lblSalidaObtenida = ttk.Label(frame_estado, text="Predicción de la IA: -", foreground="#8e44ad", font=("Helvetica", 10, "bold"))
        self.lblSalidaObtenida.grid(row=4, column=1, sticky="w", padx=40, pady=2)

        # ==========================================
        # FRAME 3: PRUEBA MANUAL (Simular Partida)
        # ==========================================
        frame_prueba = ttk.LabelFrame(ventana, text="🕹️ Simular Partida", padding=15)
        frame_prueba.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)

        opciones_jugada = ['1 (Tijera)', '0 (Papel)', '-1 (Piedra)']

        ttk.Label(frame_prueba, text="Jugador 1:").grid(row=0, column=0, padx=(10, 5))
        self.jtfEntrada1 = ttk.Combobox(frame_prueba, values=opciones_jugada, width=12, state="readonly")
        self.jtfEntrada1.set('1 (Tijera)')
        self.jtfEntrada1.grid(row=0, column=1, padx=(0, 20))

        ttk.Label(frame_prueba, text="Jugador 2:").grid(row=0, column=2, padx=(10, 5))
        self.jtfEntrada2 = ttk.Combobox(frame_prueba, values=opciones_jugada, width=12, state="readonly")
        self.jtfEntrada2.set('-1 (Piedra)')
        self.jtfEntrada2.grid(row=0, column=3, padx=(0, 20))

        self.btnPrueba = ttk.Button(frame_prueba, text="Predecir Ganador", style='EstiloBoton.TButton')
        self.btnPrueba.grid(row=0, column=4, padx=20)

        self.lblPruebaSalidaObtenida = ttk.Label(frame_prueba, text="Ganador: -", font=("Helvetica", 11, "bold"), foreground="#27ae60")
        self.lblPruebaSalidaObtenida.grid(row=0, column=5, padx=20)

        ventana.columnconfigure(0, weight=1)
        ventana.columnconfigure(1, weight=2)


# organiza  los elementos visuales de la ventana. 

# Botones 
#   btnEntrenamiento -> ejecuta un paso de entrenamiento
#   btnAprendizaje -> ejecuta el recalculo de pesos
#   btnPrueba -> ejecuta la prueba del perceptron con entradas manuales

# Labels actualizados por el controlador:
#   lblTituloPrincipal -> estado del proceso (completado / fallido)
#   lblEntrada1 / lblEntrada2 -> entradas de la fila evaluada
#   lblPeso1 / lblPeso2 / lblUmbral -> pesos actuales w1, w2 y w0
#   lblSalidaDeseada -> salida esperada de la fila actual
#   lblSalidaObtenida -> salida calculada por el perceptron
#   lblPruebaSalidaObtenida -> resultado de la prueba manual
#   Campos de texto (para el usuario):
#   jtfEntrada1 / jtfEntrada2 -> valores para la seccion prueba (solo 1 o -1)
