#Finding a missing number in array

#BruteForce: O(n^2)

def missingNum(arr:list[int])->int:
    n = len(arr)
    for i in range(1,n+1):

        flag=0

        for j in range(n):
            if i == arr[j]:
                flag = 1
                break

        if flag==0:
            return i
        
    return -1


#Better approach: O(n)+O(n)

def missingNum(arr:list[int])->int:
    n = len(arr)

    hash=[0]*(n+1)

    for i in range(n-1):
        hash[arr[i]]+=1

    for i in range(1,n+1):
        if hash[i]==0:
            return i
    
    return -1

#Optimal approach: O(n)

def missingNum(arr:list[int])->int:
    n = len(arr)
    xor1=0
    xor2=0

    for i in range(n-1):
        xor1 = xor1 ^ arr[i]
        xor2 = xor2 ^ (i+1)

    xor2=xor2^n

    return xor1^xor2




