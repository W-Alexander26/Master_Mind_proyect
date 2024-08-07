from colorama import Fore
import random 



# class tablero:
#     def table():
#         tabla = [["O" for i in range(0,4)] for _ in range(0,12)]
#         for i in tabla:
#             print("  ".join(i))
#             # return ("  ".join(i))
    
# codigo_aleatorio = (Fore.BLUE + " O "), (Fore.RED + " O " ), (Fore.YELLOW + " O "), (Fore.GREEN + " O "), (Fore.RESET )
# print(tablero.table())
# print(''.join(codigo_aleatorio))


colores = ["R", "G", "B", "Y"]
intentos = 12
tamano_codigo = 4
    
    
class Game:
    #Juego, dividido en sus respectivas clases y métodos.
    def __init__(self):
        self.code = []
        
    
        #Declaramos variables privadas.    
    def elegirModo(self):
        while True:
            print(f'Hola, Bienvenido a MasterMind. Escoge un Modo de Juego "Adivinador ó Creador de Código"')
            respuesta = input().strip().lower()
            if respuesta not in ('adivinador', 'creador de codigo'):
                print("Agrega una respuesta correcta.")
            else:
                if respuesta == 'adivinador':
                    self.crea_codigo_computadora()
                elif respuesta == 'creador de codigo':
                    self.crea_codigo_jugador()
                break
    
    
    
    def generador_codigo_random(self):
        self.code = [random.choice(colores) for _ in range(tamano_codigo)]       
        
    def adivina_codigo(self):
        while True:
            adivinanza = input("Ingresa tu adivanza : ").upper().split()
            if len(adivinanza) != tamano_codigo:
                print(f"Intenta adivinar los {tamano_codigo} colores")
                continue
            if all(color in colores for color in adivinanza):
                return adivinanza
            else:
                print("Colores invalidos. Intentalo de nuevo")
                
    
    def procesar_adivinanza(self,adivinanza,codigo):
        posicion_correcta = sum(1 for a, c in zip(adivinanza,codigo) if a == c)  
        totales_correctas = sum((adivinanza.count(color) if adivinanza.count(color)<= codigo.count(color) else codigo.count(color)) for color in colores)  
        posicion_incorrecta = totales_correctas - posicion_correcta
        return posicion_correcta, posicion_incorrecta     
    
              
    # def crea_codigo_jugador(self):
    #     print("Ingrese su combinación de colores: verde, amarillo, rojo ó azúl.")
    #     combinacion_de_colores = input().lower()
        
    #     #meter funcion que adivina la computadora sobre nuestra secuencia.
    #     if combinacion_de_colores == self.secuencia:
            
    #         print("estoy aquí vago")
        
    def crea_codigo_computadora(self):
        print("La maquina creo el código secreto")
        self.generador_codigo_random()
        codigo= self.code.copy()
        print("Trata de adivinar el código!")
        for intento in range(1, intentos + 1):
            print(f"Intento {intento}:")
            adivinanza = self.adivina_codigo()
            posicion_correcta, posicion_incorrecta = self.procesar_adivinanza(adivinanza,codigo)
            if posicion_correcta == tamano_codigo:
                print("Felicidadades, adivinaste el codigo")
                break
            print(f"posiciones correctas {posicion_correcta} | posiciones incorrecta {posicion_incorrecta}")
        else:
            print("Gana la pc")
        print(f"El codigo fue: {' '.join(codigo)}")
         
def main():
    Juego = Game()
    Juego.elegirModo()

if __name__ == "__main__":
    # Inicializador del archivo.
    main()
