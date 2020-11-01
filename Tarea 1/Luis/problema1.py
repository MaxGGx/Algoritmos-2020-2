def tool(lista,num):
	x = 0
	for c in lista:
		x += c
	if x == num:
		return True
	else:
		return False

def printSubs(lista,target):
	listaP = []
	for item in lista:
		if item != 0:
			listaP.append(item)
	print(listaP)

def subSum(conjuntos,valores,Sconjuntos,Svalores,suma,node,target):
	if target == suma:
		printSubs(valores,target)
		if(node+1 < Sconjuntos and suma-conjuntos[node]+conjuntos[node+1] <= target):
			subSum(conjuntos,valores,Sconjuntos,Svalores-1,suma-conjuntos[node],node+1,target)
		return
	else:
		if node < Sconjuntos and suma+conjuntos[node] <= target:
			i = node
			while i < Sconjuntos:
				valores[Svalores] = conjuntos[i]
				valores.append(0)
				if(suma+conjuntos[i] <= target):
					subSum(conjuntos,valores,Sconjuntos,Svalores+1,suma+conjuntos[i],i+1,target)
				i += 1

def generateSubs(conjuntos,Sconjuntos,target):
	valores = [0]
	total = 0
	conjuntos.reverse()
	i = 0
	while i < Sconjuntos:
		total += conjuntos[i]
		i += 1
	if conjuntos[0] <= target and total >= target:
		subSum(conjuntos,valores,Sconjuntos,0,0,0,target)

items = [6,4,3,3,3,2,2,2]
target = 6

generateSubs(items,len(items),target)