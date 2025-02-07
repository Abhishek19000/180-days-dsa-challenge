#Finding the second maximum element in the given array

#BruteForce :O(nlogn)

def secondMax(arr:list[int])->int:
    arr.sort()
    secondMax=arr[-2]

    return secondMax

#Better approach: O(2n)

def secondMax(arr:list[int])->int:
    maxi=float('-inf')
    secondMax=float('-inf')
    n=len(arr)

    for i in range(n):
        if arr[i]>maxi:
            maxi=max(maxi,arr[i])
    
    for i in range(n):
        if arr[i]>secondMax and arr[i]!=maxi:
            secondMax=arr[i]

    return secondMax

#Optimal approach: O(n)

def secondMax(arr:list[int])->int:
    maxi=float('-inf')
    secondMax=float('-inf')