# Find the max number of consecutive ones

def maxConsecutiveOnes(arr:list[int])->int:

    n=len(arr)
    maxi=0
    cnt=0

    for i in range(n):

        if arr[i]==1:
            cnt+=1
        else:
            cnt=0
        maxi=max(maxi,cnt)

    return cnt
