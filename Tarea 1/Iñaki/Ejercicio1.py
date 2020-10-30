#Ejemplo
lista = [8,8,8,8,7,7,6,6,6,5,5,4,3,3,2,2,1,1]
t = 4

def limpieza(lista, t):
	for x in lista:
		if x>t:
			lista = list(filter(lambda a: a != x, lista))
	return lista

print(limpieza(lista, t))