import random

colores = ["R", "G", "B", "Y"]
tamano_codigo = 4

class Codigo:
    def __init__(self):
        self.codigo = []

    def generar_codigo_random(self):
        self.codigo = [random.choice(colores) for _ in range(tamano_codigo)]
    
    def procesar_adivinanza(self, adivinanza):
        posicion_correcta = [False] * tamano_codigo
        codigo_restante = self.codigo[:]
        adivinanza_restante = adivinanza[:]
        
        # First pass: find all correct positions
        for i in range(tamano_codigo):
            if adivinanza[i] == self.codigo[i]:
                posicion_correcta[i] = True
                codigo_restante[i] = None
                adivinanza_restante[i] = None
        
        # Second pass: find correct colors in wrong positions
        posicion_incorrecta = [False] * tamano_codigo
        for i in range(tamano_codigo):
            if adivinanza_restante[i] is not None:
                if adivinanza_restante[i] in codigo_restante:
                    posicion_incorrecta[i] = True
                    codigo_restante[codigo_restante.index(adivinanza_restante[i])] = None
        
        retroalimentacion = []
        for i in range(tamano_codigo):
            if posicion_correcta[i]:
                retroalimentacion.append("G")
            elif posicion_incorrecta[i]:
                retroalimentacion.append("O")
            else:
                retroalimentacion.append("W")
                
        return retroalimentacion