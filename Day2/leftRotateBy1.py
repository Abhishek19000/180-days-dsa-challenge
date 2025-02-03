#Left rotate array by 1 place

#BruteForce Solution: O(n) with space complexity also O(n)

def leftRotateBy1(arr:list[int])->list[int]:

    arrlen=len(arr)
    temp = [0] * arrlen
    
    for i in range(1, arrlen):
        temp[i - 1] = arr[i]
    temp[arrlen - 1] = arr[0]

    return temp



#Optimal Solution: O(n)
def leftRotateBy1(arr:list[int])->list[int]:
    temp=arr[0]
    arrlen=len(arr)
    for i in range(1,arrlen):
        arr[i-1]=arr[i]

    arr[arrlen-1]=temp

    return arr
