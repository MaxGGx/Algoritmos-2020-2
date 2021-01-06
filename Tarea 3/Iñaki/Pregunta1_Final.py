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


