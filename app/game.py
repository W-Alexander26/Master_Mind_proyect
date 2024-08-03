from colorama import Fore
from time import sleep
import keyboard

class Game:
    #Juego, dividido en sus respectivas clases y métodos.
    def __init__(self):
        #Declaramos variables privadas.
        self.secuencia = []
        self.intentoDeSecuencia = []
    def elegirModo(self):
        while True:
            print(f'Hola, Bienvenido a MasterMind. Escoge un Modo de Juego "Adivinador ó Creador de Código"')
            respuesta = input().strip().lower()
            if respuesta not in ('adivinador', 'creador de codigo'):
                print("Agrega una respuesta correcta.")
            else:
                if respuesta == 'adivinador':
                    self.CreaComputadora()
                elif respuesta == 'creador de codigo':
                    self.CreaJugador()
                break
                
    def CreaJugador(self):
        input("Ingrese su combinación de colores: verde, amarillo, rojo ó azúl.")
    def CreaComputadora(self):
        print("compu crea")
def main():
    Juego = Game()
    Juego.elegirModo()
if __name__ == "__main__":
    # Inicializador del archivo.
    main()
