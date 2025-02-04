#Find the element using linear search

def linearSearch(arr:list[int],k)->int:

    n=len(arr)

    for i in range(n):
        if arr[i] == k:
            return arr[i]
    
    return -1
