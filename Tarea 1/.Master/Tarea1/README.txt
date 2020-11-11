Problema 1
Consideraciones:
-Se asume que las entradas seran las correctas.

-Para los inputs estos los ira solicitando hasta que aparezca n = 0. Para luego devolver los resultados por salida estandar.

Problema 2
Consideraciones:
-Las estructuras auxiliares (cola y lista), estan basadas en arreglos
 con su tamaño maximo definido en sus respectivos header files; para
 casos de prueba muy grandes se debe aumentar dicho numero.

-Se considera las coordenadas de la grilla desde 1 hasta n
 verticalmente y 1 hasta m horizontalmente, como se ve en el
 enunciado de la tarea.

-Se asume que las coordenadas (i, j) que se evaluaran siempre representan
 una casilla de agua, como se ve en el enunciado de la tarea. De todas formas,
 si se consulta por una casilla de Tierra (L), printea un 0.
 
-Generalizando, se asume inputs correctos.

-Se probo pasando la entrada estandar por un archivo como en el enunciado
 (./a.out < input.txt), lo que tiende a ignorar o hacer cosas raras con las
 lineas vacias. Aun asi, la diferencia con entrar las lineas a mano una a una,
 sera que printeara instantaneamente.
 
Makefile:
-Basta con escribir "make pregunta1" para ejecutar la pregunta 1 con entrada standard por consola manual (Si se desea usar un archivo .dat como entrada, correr desde consola como se indica en el hint del enunciado).
-Basta con escribir "make" o "make all" en la consola para ejecutar la pregunta 2.
