
'''

'''
def chequeoSubsec(valores, tamanio, mitad, bombas ): 
  
    contador = 1
    ulti = valores[0]
   
    for i in range(1, tamanio): 
        if (valores[i] - ulti >= mitad): 
            ulti = valores[i] 
            contador = contador + 1
              
            if (contador == bombas): 
                return True
                  
    return False 
  
# Function to find the maximum of 
# all minimum difference of pairs 
# possible among the subsequence
'''

''' 
def minDif(valores, tamanio, bombas): 
	sol = 0  
	inicio = 0
	fin = valores[-1] - valores[0]
     
	while (inicio <= fin): 
		mitad = (int((inicio + fin) / 2)) 
        # If subsequence can be formed 
        # with min diff mid and size bombas 
		if (chequeoSubsec(valores, tamanio, mitad, bombas)): 
			sol = mitad 
			inicio = mitad + 1     
		else:  
			fin = mitad - 1
      
	return sol 
  
# Valores de entrada
valores = [ 1, 2, 4, 8, 9 ] 
tamanio = len(valores) 
bombas = 3
  
minimo = minDif(valores, tamanio, bombas) 
  
print(minimo) 