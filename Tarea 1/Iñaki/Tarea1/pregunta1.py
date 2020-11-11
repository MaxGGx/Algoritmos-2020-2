soluciones=[]

'''
lista = lista de elementos que conforman la sumatoria que es igual a target
target = valor que se buscaba sumar con los elementos del input
'''
def printSubsecuencia(lista,target):
	global soluciones
	listaP = []
	sumaT = 0
	for item in lista:
		if item != 0:
			if (sumaT+item)<=target:
				sumaT+=item
				listaP.append(item)
			else:
				break
	listaP.sort(reverse=True)
	if sum(listaP) == target and (listaP not in soluciones):	
		soluciones.append(listaP)
		print("+".join(list(map(str,listaP))))
'''
conjuntos = lista de conjuntos a evaluar para generar la suma
valores = lista que contiene los números que califican para llegar a la suma indicada
subconjuntos = tamaño de la lista conjuntos
subvalores = tamaño de la lista valores
suma = valor sumado hasta el momento
nodo = nodo del arbol (teoricamente) sobre el que se encuentra
target = valor a encontrar
'''
def subSumas(conjuntos,valores,Subconjuntos,Subvalores,suma,nodo,target):
	if target == suma:
		printSubsecuencia(valores,target)
		if(nodo+1 < Subconjuntos and suma-conjuntos[nodo]+conjuntos[nodo+1] <= target):
			subSumas(conjuntos,valores,Subconjuntos,Subvalores-1,suma-conjuntos[nodo],nodo+1,target)
		return 0
	else:
		if nodo < Subconjuntos and suma+conjuntos[nodo] <= target:
			i = nodo
			while i < Subconjuntos:
				valores[Subvalores] = conjuntos[i]
				valores.append(0)
				if(suma+conjuntos[i] <= target):
					subSumas(conjuntos,valores,Subconjuntos,Subvalores+1,suma+conjuntos[i],i+1,target)
				i += 1

'''
conjuntos = lista de posibles conjuntos de números que califican para llegar a la suma especificada
Sconjuntos = tamaño de la lista conjuntos
target = valor a encontrar en la sumatoria de elementos
'''
def generaSubconjuntos(conjuntos,Sconjuntos,target):
	valores = [0]
	total = 0
	conjuntos.reverse()
	i = 0
	while i < Sconjuntos:
		total += conjuntos[i]
		i += 1
	if conjuntos[0] <= target and total >= target:
		subSumas(conjuntos,valores,Sconjuntos,0,0,0,target)
		return 0

print("  _______                     __ ")                        
print(" |__   __|                   /_ |")                       
print("    | | __ _ _ __ ___  __ _   | |")                       
print("    | |/ _` | '__/ _ \/ _` |  | |")                       
print("    | | (_| | | |  __/ (_| |  | |")                       
print("    |_|\__,_|_|  \___|\__,_|  |_|")                       
print("     /\   | |                (_) |")                      
print("    /  \  | | __ _  ___  _ __ _| |_ _ __ ___   ___  ___ ")
print("   / /\ \ | |/ _` |/ _ \| '__| | __| '_ ` _ \ / _ \/ __|")
print("  / ____ \| | (_| | (_) | |  | | |_| | | | | | (_) \__ \ ")
print(" /_/    \_\_|\__, |\___/|_|  |_|\__|_| |_| |_|\___/|___/")
print("              __/ |                                     ")
print("             |___/                                      ")

inputs = []

while(True):
	string = input("Ingrese entradas:\n>")
	if string.split(" ")[1] == '0':
		break
	inputs.append(list(map(int,string.split(" "))))

for entrada in inputs:
	items=[]
	target = entrada[0]
	for x in range(2,entrada[1]+2):
		items.append(entrada[x])
	print("Suma de "+str(target)+":")
	if generaSubconjuntos(items,len(items),target) == None:
		print("NADA")
