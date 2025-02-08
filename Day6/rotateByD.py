#Rotate the given array by D places 

#BruteForce : O(n) but with space complexity O(d)

def rotateByD(arr:list[int],d)->list[int]:
    n = len(arr)
    temp=[]
    for i in range(d):
        temp.append(arr[i])
    
    for i in range(d,n):
        arr[i-d]=arr[i]
    
    for i in range(d):
        arr[n-d+i]=temp[i]

    return arr