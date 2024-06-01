import random
import os
from colorama import init, Fore

# Inicializar colorama para Windows
init()

# Arte ASCII de una pistola
imagen_pistola = """
     +____________________/\\/__ / /|
   .'' ._____________'._____      / /|/\\
  : () :              :\ ----\|    \ )
   '..'______________.'0|----|      \\
                    0_0/____/        \\
                        |----    /----\\
                       || -\\ --|      \\
                       ||   || ||\\      \\
                        \\____// '|      \\
Bang! Bang!                     .'/       |
                               .:/        |
                               :/_________|\\
"""

def cargar_archivo():
    ruta_archivo = input("Introduce la ruta al archivo que deseas poner en juego: ")
    if not os.path.exists(ruta_archivo):
        print(Fore.RED + "El archivo no existe." + Fore.RESET)
        return None
    return ruta_archivo

def jugar_ruleta():
    numero_muerte = random.randint(1, 6)
    intentos = 0
    mensajes = ["¡Ups! Parece que te estás arriesgando, pero tal vez deberías rendirte.",
                "¿Seguro que quieres seguir jugando? Rendirse es una opción también.",
                "¡Cuidado! Esto se está poniendo peligroso. ¿Quizás quieras rendirte?",
                "Todavía tienes tiempo para rendirte. No esperes demasiado tarde."]
    mensajes_mostrados = []
    while intentos < 4:
        mensaje = random.choice(mensajes)
        while mensaje in mensajes_mostrados:  # Evitar mostrar un mensaje repetido
            mensaje = random.choice(mensajes)
        mensajes_mostrados.append(mensaje)
        
        seleccion = int(input("Elige un número del 1 al 6: "))
        if seleccion == numero_muerte:
            print(Fore.RED + "¡Has perdido! El archivo ha sido eliminado." + Fore.RESET)
            os.remove(archivo)
            return
        else:
            print(Fore.YELLOW + mensaje + Fore.RESET)
        intentos += 1
    print(Fore.GREEN + "¡Has ganado! Aquí tienes el enlace a la página web: https://dark-d4nt3.github.io/eda/" + Fore.RESET)

# Mostrar la imagen de la pistola al inicio del juego
print(imagen_pistola)

archivo = cargar_archivo()
if archivo:
    jugar_ruleta()
