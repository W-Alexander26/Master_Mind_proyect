from colorama import Fore
from time import sleep
import keyboard
import random 

class Game:
    #Juego, dividido en sus respectivas clases y métodos.
    def __init__(self, rojo, azul, verde, amarillo, reset):
        self.rojo = rojo
        self.azul = azul
        self.verde = verde
        self.amarillo = amarillo
        self.reset = reset
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
        print("Ingrese su combinación de colores: verde, amarillo, rojo ó azúl.")
        combinacion_de_colores = input().lower()
        #meter funcion que adivina la computadora sobre nuestra secuencia.
        opciones_random = []
        if combinacion_de_colores == self.secuencia:
            
            print("estoy aquí vago")
        
    def CreaComputadora(self):
        while True:
            posiblesOpciones = (self.rojo, self.azul, self.amarillo, self.verde)
            self.secuencia.insert(1, random.choice(posiblesOpciones) + self.reset)
            if len(self.secuencia) == 4:
                print(''.join(self.secuencia) + self.reset)
                break
def main():
    Juego = Game(azul=(Fore.BLUE + " O "), rojo=(Fore.RED + " O "), amarillo=(Fore.YELLOW + " O "), verde=(Fore.GREEN + " O "), reset=Fore.RESET)
    Juego.elegirModo()
if __name__ == "__main__":
    # Inicializador del archivo.
    main()
