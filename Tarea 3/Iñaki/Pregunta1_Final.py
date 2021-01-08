'''
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
				if(valor >= lista[i] and subLista[posicion] <= subLista[i]+1):
					subLista[posicion] = subLista[i] + 1
	
	#Return relacionado a la pregunta 1
	return tamanio-max(subLista)

'''
Código correspondiente a la toma de entradas y salida standart
'''
entradas = []
entrada = input("Ingrese inputs - Presione enter para terminar de ingresar\n>")
while entrada != "":
	entrada1 = list(map(int, entrada.strip().split( )))
	valores = entrada1[0]+1
	entrada2 = []
	for x in range(1,valores):
		entrada2.append(entrada1[x])
	entradas.append(entrada2)
	entrada = input("Ingrese inputs - Presione enter para terminar de ingresar\n>")

for entrada in entradas:
	print(SAML_PD(entrada))


