from colorama import Fore, Style, init
from codigo import Codigo
from jugador import Jugador
import random
"""Importamos las clases necesarias para utilizar en el archivo game.py."""

init(autoreset=True)

"""Creamos la variables de los colores, intentos y tamaño del codigo aplicando al resto del codigo"""
colores = ["R", "G", "B", "Y"]
intentos = 12
tamano_codigo = 4

"""creamos un diccionario que contiene el color que necesitas al usar la letra correspondiente"""
color_map = {
    "R": Fore.RED + 'O' + Style.RESET_ALL,
    "G": Fore.GREEN + 'O' + Style.RESET_ALL,
    "B": Fore.BLUE + 'O' + Style.RESET_ALL,
    "Y": Fore.YELLOW + 'O' + Style.RESET_ALL
}

"""Creamos otro diccionario que nos va a brindar la retroalimentacion sobre la secuencia de colores"""
feedback_map = {
    "G": Fore.GREEN + '●' + Style.RESET_ALL,
    "O": Fore.LIGHTYELLOW_EX + '●' + Style.RESET_ALL,
    "W": Fore.WHITE + '●' + Style.RESET_ALL
}

"""Creamos una clase que va a contener la ejecucion del juego,"""
class Juego:
    def __init__(self):
        self.codigo = Codigo()
        self.jugador = Jugador()

    """creamos la funcion que nos va a preguntar cual modo de juego nos gustaria jugar"""
    def elegir_modo(self):
        while True:
            print('Hola, bienvenido a MasterMind. Escoge un modo de juego: "Adivinador" o "Creador de Código"')
            respuesta = input().strip().lower()
            if respuesta not in ('adivinador', 'creador de codigo'):
                print("Agrega una respuesta correcta.")
            else:
                if respuesta == 'adivinador':
                    self.crea_codigo_computadora()
                elif respuesta == 'creador de codigo':
                    self.crea_codigo_jugador()
                break

    """se crea la funcion correspondiente para que la computadora adivine el codigo generador por el jugador"""
    def crea_codigo_computadora(self):
        print("La máquina creó el código secreto.")
        self.codigo.generar_codigo_random()
        codigo = self.codigo.codigo
        print("Trata de adivinar el código!")
        for intento in range(1, intentos + 1):
            print(f"Intento {intento}:")
            adivinanza = self.jugador.adivina_codigo()
            retroalimentacion = self.codigo.procesar_adivinanza(adivinanza)
            adivinanza_colored = [color_map[color] for color in adivinanza]
            retroalimentacion_colored = [feedback_map[color] for color in retroalimentacion]
            print(f"Adivinanza: {' '.join(adivinanza_colored)} Retroalimentación: {' '.join(retroalimentacion_colored)}")
            if all(color == "G" for color in retroalimentacion):
                print("¡Felicidades, adivinaste el código!")
                break
        else:
            print("Gana la PC.")
        codigo_colored = [color_map[color] for color in codigo]
        print(f"El código fue: {' '.join(codigo_colored)}")

    """Se crea la funcion que hace al jugador adivinar el codigo de colores generador por la computadora"""
    def crea_codigo_jugador(self):
        codigo_jugador = self.jugador.crea_codigo_jugador()
        self.codigo.codigo = codigo_jugador
        print("La computadora intentará adivinar el código.")
        
        posibles_combinaciones = [[color for color in colores] for _ in range(tamano_codigo)]
        intentos_realizados = []
        
        for intento in range(1, intentos + 1):
            adivinanza = [random.choice(posibles_combinaciones[i]) for i in range(tamano_codigo)]
            if adivinanza in intentos_realizados:
                continue
            intentos_realizados.append(adivinanza)
            adivinanza_colored = [color_map[color] for color in adivinanza]
            retroalimentacion = self.codigo.procesar_adivinanza(adivinanza)
            retroalimentacion_colored = [feedback_map[color] for color in retroalimentacion]
            print(f"Intento {intento}: {' '.join(adivinanza_colored)} Retroalimentación: {' '.join(retroalimentacion_colored)}")
            if all(color == "G" for color in retroalimentacion):
                print("La computadora adivinó el código.")
                break
        else:
            print("La computadora pierde.")
        codigo_jugador_colored = [color_map[color] for color in codigo_jugador]
        print(f"El código era: {' '.join(codigo_jugador_colored)}")
        
"""Funcion para que se ejecute el juego junto con sus instancias"""
def main():
    juego = Juego()
    juego.elegir_modo()

if __name__ == "__main__":
    main()