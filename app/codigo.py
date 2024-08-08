import random

colores = ["R", "G", "B", "Y"]
tamano_codigo = 4

"""se crea la clase codigo para que esta tenga la funcion de crear un codigo aleatorio
y asi mismo permita tanto al adivinador y al creador de la secuencia de colores ver los aciertos """
class Codigo:
    def __init__(self):
        self.codigo = []

    def generar_codigo_random(self):
        self.codigo = [random.choice(colores) for _ in range(tamano_codigo)]
    
    def procesar_adivinanza(self, adivinanza):
        posicion_correcta = [False] * tamano_codigo
        codigo_restante = self.codigo[:]
        adivinanza_restante = adivinanza[:]
        
        """Primer paso: encuentra todas las posiciones de los colores correctas"""
        for i in range(tamano_codigo):
            if adivinanza[i] == self.codigo[i]:
                posicion_correcta[i] = True
                codigo_restante[i] = None
                adivinanza_restante[i] = None
        
        """Segundo paso: encuentra todas las posiciones de los colores incorrectas"""
        posicion_incorrecta = [False] * tamano_codigo
        for i in range(tamano_codigo):
            if adivinanza_restante[i] is not None:
                if adivinanza_restante[i] in codigo_restante:
                    posicion_incorrecta[i] = True
                    codigo_restante[codigo_restante.index(adivinanza_restante[i])] = None
                    
        """La retroalimentacion nos va a mostrar el acierto o no de la secuencia de colores usada 
        Verde(G) para color correcto en la posicion correcta.
        Amarillo(Y) para indicar que el color se uso en la secuencia pero tiene la posicion incorrecta
        Blanco(W) indicando que color no existe dentro de la secuencia"""
        retroalimentacion = []
        for i in range(tamano_codigo):
            if posicion_correcta[i]:
                retroalimentacion.append("G")
            elif posicion_incorrecta[i]:
                retroalimentacion.append("O")
            else:
                retroalimentacion.append("W")
                
        return retroalimentacion