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


