from aeronave import aeronave
from avioneta import avioneta
from helicoptero import helicoptero
from airbus360 import airbus360

# Crear un objeto en cada clase

obj_aeronave = aeronave()
obj_avioneta = avioneta()
obj_airbus360 = airbus360()
obj_helicoptero = helicoptero()

# Llamamos al método describir de cada objeto

obj_aeronave.describir()
obj_avioneta.describir()
obj_airbus360.describir()
obj_helicoptero.describir()


'''
Explicación:
A pesar de que el método describir tiene el mismo nombre en cada clase,funciona correctamente en cada una debido al concepto de polimorfismo.
En Python, el polimorfismo permite que diferentes clases utilicen métodos con el mismo nombre y que se comporten de forma distinta dependiendo de la
clase en la que se ha implementado. Esto es posible gracias a la capacidad de Python de interpretar el contexto del objeto que llama al método, de manera
que se ejecuta el método correspondiente a la clase de cada objeto.


a. ¿Qué instrucciones se utilizaron para establecer la herencia entre las clases?
Para establecer la herencia entre las clases, se utiliza la sintaxis:
class ClaseHija(ClasePadre):
Esto indica que 'ClaseHija' hereda de 'ClasePadre', permitiéndole acceder a los métodos
y atributos de 'ClasePadre'. En este caso, las clases 'EnergiaSolar', 'EnergiaEolica',
y 'EnergiaHidraulica' heredan de la clase 'Energia'.

b. ¿Qué función tiene la instrucción pass?

La instrucción 'pass' se utiliza en Python como un marcador de posición para indicar que no se ha definido ninguna operación en el 
bloque de código donde se encuentra. Esto es útil cuando se está diseñando una clase o función que aún no tiene
implementaciones específicas pero se necesita que el código sea sintácticamente correcto. 'pass' permite que el programa siga ejecutándose 
sin errores.

c. Por cada clase se ha generado un archivo. ¿Cuáles son las instrucciones que se usaron para vincular los archivos entre sí y lograr 
la herencia entre hijos y padre?

Para vincular los archivos, se utiliza la instrucción 'from ... import ...'.

Por ejemplo, 'from energia import energia' permite que el archivo 'polimorfo.py'
acceda a la clase 'Energia' definida en el archivo 'energia.py'. De manera similar,
para cada clase hija, se importa desde su propio archivo, permitiendo la herencia
y el uso de cada clase en 'polimorfo.py'.

d. ¿Para qué sirven las funciones setter y getter que se agregaron a las clases?

Las funciones setter y getter se utilizan para acceder y modificar los atributos de una clase de forma controlada. 
Los 'getter' permiten obtener el valor de un atributo, mientras que los 'setter' permiten establecer o cambiar el valor de
un atributo. Esto es útil para implementar encapsulamiento.

'''


