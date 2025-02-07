#Finding the second maximum element in the given array

#BruteForce :O(nlogn)

def secondMax(arr:list[int])->int:
    arr.sort()
    secondMax=arr[-2]

    return secondMax