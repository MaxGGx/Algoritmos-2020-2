def bB (elementos, l, r, x):  
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # El elemento esta justo en la mitad 
        if elementos[mid] == x: 
            return mid 
          
        # Búsqueda en el lado izquierdo 
        elif elementos[mid] > x: 
            return bB(elementos, l, mid-1, x) 
  
        # Búsqueda en el lado derecho 
        else: 
            return bB(elementos, mid + 1, r, x) 
  
    else: 
        # Elemento no se encuentra en la lista
        return -1
  
# Main
elementos = [ 10, 6, 7, 5, 4, 6, 3, 1, 0] 
x = 1
  
result = bB(elementos, 0, len(elementos)-1, x) 
  
if result != -1: 
    print ("El elemento se encuentra en la posición % d" % result) 
else: 
    print ("El elemento no se encuentra en la lista") 