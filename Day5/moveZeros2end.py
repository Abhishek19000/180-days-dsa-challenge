#Move all the end to the last of the array

#BruteForce:  O(2n)

def moveZeros2end(arr:list[int])->list[int]:

    n=len(arr)
    temp=[]
    for i in range(n):
        if arr[i]!=0:
            temp.append(arr[i])

    nonZ=len(temp)

    for i in range(nonZ):
        arr[i]=temp[i]

    for i in range(nonZ,n):
        arr[i]=0

    return arr

#Optimal approach: O(n)

def moveZeros2end(arr:list[int])->list[int]:

    n=len(arr)
    j=-1
    for i in range(n):
        if(arr[i]==0):
            j=i
            break

    for i in range(j+1,n):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr




