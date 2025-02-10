#Sort the array containing 0's ,1's and 2's

#BruteForce: O(nlogn)

def sort012(arr:list[int])->list[int]:
    arr.sort()

    return arr

#Better approach: O(2n)

def sort012(arr:list[int])->list[int]:
    n = len(arr)
    cnt=0
    cnt1=0
    cnt2=0
    for i in range(n):
        if arr[i]==0:
            cnt+=1
        elif arr[i]==1:
            cnt1+=1
        elif arr[i]==2:
            cnt2+=1
    
    for j in range(cnt):
        arr[j]=0

    for j in range(cnt,cnt+cnt1):
        arr[j]=1
    
    for j in range(cnt+cnt1,cnt+cnt1+cnt2):
        arr[j]=2
    
    return arr