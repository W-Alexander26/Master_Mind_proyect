colores = ["R", "G", "B", "Y"]
tamano_codigo = 4

"""Creamos la clase jugador que contiene la funcion que nos permite adivinar
el codigo de la computadora y la creacion de nuestra secuencia de colores para que la computadora la adivine"""
class Jugador:
    def adivina_codigo(self):
        while True:
            adivinanza = input("Ingresa tu adivinanza: ").upper().split()
            if len(adivinanza) != tamano_codigo:
                print(f"Intenta adivinar los {tamano_codigo} colores")
                continue
            if all(color in colores for color in adivinanza):
                return adivinanza
            else:
                print("Colores inválidos. Inténtalo de nuevo")

    def crea_codigo_jugador(self):
        while True:
            print("Ingrese su combinación de colores: verde(G), amarillo(Y), rojo(R) o azul(B).")
            codigo = input().upper().split()
            if len(codigo) != tamano_codigo or not all(color in colores for color in codigo):
                print(f"Combinación inválida. Utiliza {tamano_codigo} colores válidos.")
            else:
                return codigo