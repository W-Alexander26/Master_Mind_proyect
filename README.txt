# Master_Mind_proyect
#Se utilizo el paquete de colores colorama
#Tambien se importo choices de la libreria random
#Tambien se utilizo product de la libreria itertools para que la maquina escogiera alguna de las estrategias
 para adivinar el codigo.

#Clase Juego
Se encarga de emular el juego conteniendo las demás clases que permiten el correcto funcionamiento del juego.
Así también se utilizan las instancias "self" para utilizar las variables necesarias como el tamaño del codigo, 
este siendo 4 debido a que son las 4 colores a utilizar para crear la secuencia o adivinarla. (RED; BLUE; GREEN;
 YELLOW )
También se utiliza el diccionario de feedback para dar retroalimentacion al jugador sobre las posiciones correctas
 siendo mostras con un circulo de color verde y otro circulo de color amarillo para mostrar las posiciones
  incorrectas, tambien circulo blanco para dar a entender que el color no esta dentro de la secuencia de colores.
Dentro de esta misma clase se tienen las funciones para escoger el modo de juego.
Y también la funcion para que la computadora adivine el codigo de colores del jugador en un rango de 12 intentos y viceverza.  

#Clase jugador
Dentro de la clase jugador vamos a encontrar las funciones que nos permiten comparar nuestra secuencia
 de colores elegidos con la respuesta aleatoria de la computadora.
 Así como también en caso contrario se va a comparar nuestra adivinanza con respecto al codigo generado por la computadora y comprobar si son correctos o no.


#Clase codigo
La clase codigo se encarga de albergar la funcion para generar un codigo aleatorio de la computadora utilizando los 4 colores antes mencionados.
Comprobar los datos de la secuencia y mostrarlos con los colores correspondientes en caso de ser correctos
 en la posicion correcta, serán enviador como un circulo verde.
 Amarillo si el color seleccionado esta en la secuencia pero en la posicion incorrecta y blanco si el color
  utilizado no existe en la secuencia creada.



