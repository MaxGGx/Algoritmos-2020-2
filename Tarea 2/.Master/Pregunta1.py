def Pregunta1(lista, tamanio, s):
	
	if(tamanio < s):
		return "Entrada no valida para trampas"

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
		en esta seccion ocurre la busqueda de numeros, planteo como primera posicion (actual) de la primera trampa (colocadas)
		y desde ahi recorro el resto de la lista siempre comparando la resta de valores para que revise si encuentra alguno que
		cumpla la condicion con el numero propuesto, en caso de hallarlo, marco esa posicion al sustituir el actual con ese valor 
		y a la vez "coloco" una trampa (colocadas+=1), finalmente sigo iterando para el resto de trampas. Lo interesante, es que
		si encuentra una resta que sea mayor al propuesto, al continuar comparando puede que haya una resta menor a la que ya se tiene
		por eso el ciclo for continua. Finalmente, si no logra colocar todas las trampas o el ciclo se termina. Quiere decir que el valor
		propuesto no fué hallado, por lo que la búsqueda binaria se volvera a hacer ahora por el lado izquierdo del arreglo al no hallar
		posibilidades en la parte mas alta. De esa forma se tiene una forma de resolucion a partir de Decrecer y conquistar, al reducir con
		la busqueda binaria los espacios de busqueda (valga la redundancia) para determinar el valor solicitado.
		'''
		for a in range(1, tamanio):
			if((lista[a] -  actual) >= prop):
				actual = lista[a]
				colocadas+=1
				if(colocadas == s):
					if(sol < prop):
						sol = prop
					izq = prop+1
					flag = 1
					break
		if(flag != 1):
			der = prop

	return sol

string=input()
string2=input()

n=int(string.split(" ")[0])
s=int(string.split(" ")[1])

lista = [int(i) for i in string2.split(" ")]
lista.sort() #se ordena solo para casos que la entrada no sea ordenada

if(len(lista) > n):
	print("Error en el ingreso de datos: n es menor que los valores entregados")
elif(len(lista) < n):
	print("Error en el ingreso de datos: n es mayor que los valores entregados")
else:
	print(Pregunta1(lista, n, s))
