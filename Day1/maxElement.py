'''Finding the max Element in the given array'''

# Brute Force Approach:- O(nlogn)

def findLargestElement(arr: list[int]) -> int:
    arr.sort()
    return arr[-1]    

#[-1] is used to access last element in python

print(findLargestElement([3,1,4,2,0]))

#Optimal approach:- 0(n)

def findLargestElement1(arr, n)->int:

    maxElement = arr[0]
    for i in range(0, n):
        if (maxElement < arr[i]):
            maxElement = arr[i]
    return maxElement

print(findLargestElement1([3,1,4,2,0],5))