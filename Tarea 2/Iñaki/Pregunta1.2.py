def Pregunta1(lista, tamanio, B):
	
	if(tamanio < B):
		return "Entrada no valida"

	sol=-1

	#preparacion busqueda binaria

	izq= 1
	der= lista[-1]

	#Buscamos a partir de una distancia promedio entre los valores
	#a buscar, proponiendo un valor llamado "prop" el cual dentro
	#de la busqueda binaria y dependiendo de hacia donde se vaya
	#(izquierda o derecha) propondra otros valores utilizando esos
	#limites que modifique la busqueda binaria
	while(izq < der):
		prop = (izq+der)//2 #Dividimos y solo sacamos la parte entera
		
		'''
		haciendo uso del valor propuesto, el algoritmo va a tratar de armar
		una combinacion que permita obtener como diferencia minima
		el valor propuesto. En caso de que lo encuentre, se cambian los limites para
		continuar con la busqueda binaria para hallar algun otro propuesto o mas alto, o mas bajo
		'''
		actual = lista[0]
		colocadas = 1
		flag = 0

		'''
		en esta seccion ocurre la busqueda de numeros, planteo como primera posicion (actual) de la primera bomba (colocadas)
		y desde ahi recorro el resto de la lista siempre comparando la resta de valores para que revise si encuentra alguno que
		cumpla la condicion con el numero propuesto, en caso de hallarlo, marco esa posicion al sustituir el actual con ese valor 
		y a la vez "coloco" una bomba (colocadas+=1), finalmente sigo iterando para el resto de bombas. Lo interesante, es que
		si encuentra una resta que sea mayor al propuesto, al continuar comparando puede que haya una resta menor a la que ya se tiene
		por eso el ciclo for continua. Finalmente, si no logra colocar todas las bombas o el ciclo se termina. Quiere decir que el valor
		propuesto no fué hallado, por lo que la búsqueda binaria, se volvera a hacer ahora por el lado izquierdo del arreglo al no hallar
		posibilidades en la parte mas alta. De esa forma se tiene una forma de resolucion a partir de Decrecer y conquistar, al reducir con
		la busqueda binaria los espacios de busqueda (valga la redundancia) para determinar el valor solicitado.
		'''
		for a in range(1, tamanio):
			if((lista[a] -  actual) >= prop):
				actual = lista[a]
				colocadas+=1
				if(colocadas == B):
					if(sol < prop):
						sol = prop
					izq = prop+1
					flag = 1
					break
		if(flag != 1):
			der = prop

	return sol

print(Pregunta1([9,12], len([9,12]), 3))


