import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    
    print("--- ¡Bienvenido a Piedra, Papel o Tijera! ---")
    
    while True:
        # Elección del usuario
        usuario = input("\nElegí (piedra, papel, tijera) o 'salir' para terminar: ").lower()
        
        if usuario == "salir":
            print("¡Gracias por jugar!")
            break
            
        if usuario not in opciones:
            print("Opción no válida. Intentá de nuevo.")
            continue
        
        # Elección de la computadora
        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")
        
        # Lógica del juego
        if usuario == computadora:
            print("¡Es un empate!")
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            print("¡Ganaste! 🎉")
        else:
            print("Perdiste... Intentalo otra vez. 🤖")

if __name__ == "__main__":
    jugar()