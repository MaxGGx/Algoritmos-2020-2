'''
Primer análisis para la pregunta 1:

Si se analiza el hint que nos entregan, podemos hallar una relacion al obtener el subarreglo ordenado mas alto, ya que, si encontramos dicho arreglo
y luego lo restamos por el len del array completo, obtenemos los valores que no son parte de ese sub-array mas largo, por lo que deben ser movidos
para llegar a que estuviese por completo ordenado. Por lo tanto, en un primer lugar debemos obtener la recursion para lograr obtener el sub arreglo
ordenado mas largo y luego solo será restarlo con el len del array para obtener el valor solicitado.

'''

#SAML - Recusivo (Sub Arreglo Mas Largo)
'''
Para poder obtener el sub arreglo mas largo sera necesario, entregar un valor de fin o de indexacion, es decir, hasta donde tomare un sub
array para comparar. De esta forma se arman todas las posibilidades, para asi ir ejecutando recusrivamente la funcion, tomando como caso base
que para un valor de indexacion igual a cero, se retornará 1, ya que para los arrays de len = 1 es el unico mas alto.

'''

def SAML(lista, i):
	if(i==0):
		return 1
	
	maximo=1
	for j in range(0,i-1):
		if(lista[j]<lista[i]):
			maximo = max(maximo, 1+SAML(lista, j))
	return maximo

print(SAML([3,1,5,0],3)+1) #El +1 cuenta a la posicion misma


'''
De lo anterior se observa que constantemente SAML irá calculando repetitivamente valores para sub arrays, si es que se observa el arbol que
va armando el algoritmo, es por ello que podemos recurrir a programacion dinamica para reducir su tiempo de ejecucion

Resolucion en programacion dinamica:
Para poder resolver este problema con programacion dinamica, evitando recalcular constantemente, lo que se hara sera inicializar
un array con todos los valores en 1, ya que, al menos para cada valor el sub array más alto será 1. Lo que luego haremos sera iterar
de a dos posiciones comparando las cantidades. Si el valor en la posicion de la derecha es mas alto que el de la izquierda, querrá decir
que el valor del sub array mas alto hasta ese punto del array original sera del valor que contiene el valor de la izquierda + 1. 
'''

def SAML_PD(lista):
	tamanio = len(lista)
	subLista = [1]*tamanio

	for posicion, valor in enumerate(lista):
		if (posicion >= 1):
			for i in range(0,posicion):
				if(valor > lista[i] and subLista[posicion] < subLista[i]+1):
					subLista[posicion] = subLista[i] + 1
	
	#Return relacionado a la pregunta 1
	return tamanio-max(subLista)

print(SAML_PD([1,2,3,4,2,7]))








