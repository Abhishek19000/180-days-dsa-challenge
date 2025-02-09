#Find the longest subarray with sum K

#BruteForce : O(n^2)

def subArr(arr:list[int],k)->int:
    n=len(arr)
    length=0
    sum=0
    for i in range(n):
        for j in range(i,n):
            sum+=arr[j]

            if sum==k:
                length=max(length,j-i+1)

    return length

#Optimised approach: O(n)

def subArr(arr:list[int],k)->int:
    n=len(arr)
    length=0
    temp={}
    sum=0
    for i in range(n):

        sum+=arr[i]

        if sum==k:
            length=max(length,i)

        preSum=sum-k

        if preSum in temp:
            length=max(length,i-temp[preSum])

        if preSum not in temp:
            temp[preSum]=i

    return length

