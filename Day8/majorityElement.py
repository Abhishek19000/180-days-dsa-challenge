#Find the element with the occurences greater than n/2

#BruteForce: O(n^2)

def majorityEle(arr:list[int])->list[int]:
    n = len(arr)
    for i in range(n):
        count = 0
        ele=arr[i]
        for j in range(n):
            if arr[j]==ele:
                count+=1
        if count>n/2:
            return ele
    return -1