soluciones=[]

def tool(lista,num):
	x = 0
	for c in lista:
		x += c
	if x == num:
		return True
	else:
		return False

def printSubs(lista,target):
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
	if sum(listaP) == target and (listaP not in soluciones):	
		soluciones.append(listaP)
		print("+".join(list(map(str,listaP))))

def subSum(conjuntos,valores,Sconjuntos,Svalores,suma,node,target):
	if target == suma:
		printSubs(valores,target)
		if(node+1 < Sconjuntos and suma-conjuntos[node]+conjuntos[node+1] <= target):
			subSum(conjuntos,valores,Sconjuntos,Svalores-1,suma-conjuntos[node],node+1,target)
		return 0
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
	if generateSubs(items,len(items),target) == None:
		print("NADA")