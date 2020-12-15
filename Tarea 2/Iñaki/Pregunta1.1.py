
'''

#funcion que halla todas las permutaciones
def permutaciones(lista, B, act):
	if len(act) == B:
		print(act)
		return [act]

	for i in range(len(lista)):
		act2 = act.copy()
		act2.append(lista[i])
		permutaciones(lista[i+1:], B, act2)
	return "fin"

print(permutaciones([1,2,4,8,9], 3, []))

for x in len([1,3,43,44,44]):
	print(x)

'''
 
# Prueba con una funcion aparte
def largestMinDist(arr, n, k):
     
    # Sort the positions
    arr.sort(reverse = False)
 
    # Initialize result.
    res = -1
 
    # Consider the maximum possible distance
    left = 0
    right = arr[n - 1]
     
    # left is initialized with 1 and not with arr[0] 
    # because, minimum distance between each element 
    # can be one and not arr[0]. consider this example: 
    # arr[] = {9,12} and you have to place 2 element
    # then left = arr[0] will force the function to
    # look the answer between range arr[0] to arr[n-1], 
    # i.e 9 to 12, but the answer is 3 so It is required 
    # that you initialize the left with 1
 
    # Do binary search for largest 
    # minimum distance
    while (left < right):
        mid = (left + right) / 2
 
        # If it is possible to place k elements
        # with minimum distance mid, search for
        # higher distance.
        if (isFeasible(mid, arr, n, k)):
             
            # Change value of variable max to mid iff
            # all elements can be successfully placed
            res = max(res, mid)
            left = mid + 1
 
        # If not possible to place k elements, 
        # search for lower distance
        else:
            right = mid
 
    return res
 
# Driver code
if __name__ == '__main__':
    arr = [1,2,4,8,9]
    n = len(arr)
    k = 3
    print(largestMinDist(arr, n, k))