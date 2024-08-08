class adivina_jugador:
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
            print(f"Intento {intento}: {' '.join(adivinanza)}")
            posicion_correcta, posicion_incorrecta = self.codigo.procesar_adivinanza(adivinanza)
            print(f"Posiciones correctas: {posicion_correcta} | Posiciones incorrectas: {posicion_incorrecta}")
            
            if posicion_correcta == tamano_codigo:
                print("La computadora adivinó el código.")
                break
        else:
            print("La computadora pierde.")
        print(f"El código era: {' '.join(codigo_jugador)}")