#Finding the two elements in the array whose sum is equal to k

#BruteForce: O(n^2)

def sumTwo(arr:list[int],k)->list[int]:
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==k:
                return [arr[i],arr[j]]
    
    return [-1,-1]

#Better approach : O(n) but with the space complexity as O(n) 

def sumTwo(arr:list[int],k)->list[int]:

    eleInMap={}

    for i in range(len(arr)):
        num=arr[i]
        target=k-num

        if target in eleInMap:
            return [eleInMap[target],i]
        
        eleInMap[num]=i

    return -1

#Optimised approach : O(n)

def sumTwo(arr:list[int],k)->list[int]:
    n=len(arr)
    i=0
    j=n-1
    arr.sort()
    
    while(i<j):
        if arr[i]+arr[j]==k:
            return [i,j]
        elif arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1
    return [-1,-1]

