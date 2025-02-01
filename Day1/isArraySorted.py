'''To find whether the given array is sorted or not'''

#Brute Force Approach :- O(n^2)

def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True

#Optimal approach :- O(n)

def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True