# Python3 program to implement 
# the above approach 
  
# Function to check a subsequence can 
# be formed with min difference mid 
def can_place(A, n, B, mid): 
  
    count = 1
    last_position = A[0] 
  
    # If a subsequence of size B 
    # with min diff = mid is possible 
    # return true else false 
    for i in range(1, n): 
        if (A[i] - last_position >= mid): 
            last_position = A[i] 
            count = count + 1
              
            if (count == B): 
                return bool(True) 
                  
    return bool(False) 
  
# Function to find the maximum of 
# all minimum difference of pairs 
# possible among the subsequence 
def find_min_difference(A, n, B): 
  
    # Sort the Array 
    A.sort() 
  
    # Stores the boundaries 
    # of the search space 
    s = 0
    e = A[n - 1] - A[0]
    #print(e) 
  
    # Store the answer 
    ans = 0
  
    # Binary Search 
    while (s <= e): 
        mid = (int)((s + e) / 2) 
        print(mid)
        # If subsequence can be formed 
        # with min diff mid and size B 
        if (can_place(A, n, B, mid)): 
            ans = mid 
  
            # Right half 
            s = mid + 1
          
        else: 
  
            # Left half 
            e = mid - 1
      
    return ans 
  
# Driver code 
A = [ 1, 2, 4, 8, 9 ] 
n = len(A) 
B = 3
  
min_difference = find_min_difference(A, n, B) 
  
print(min_difference) 