"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(arr, low, high):
    if low < high: 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quicksort(arr, low, pi-1) 
        quicksort(arr, pi+1, high)
    return arr
        
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )
    
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test, 0, len(test)-1)