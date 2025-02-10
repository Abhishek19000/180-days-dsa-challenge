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

#Better approach:

def majorityEle(arr:list[int])->list[int]:
    n = len(arr)
    eleFreq={}
    for num in arr:
        if num in eleFreq:
            eleFreq[num]+=1
        else:
            eleFreq[num]=1

    for num,count in eleFreq.items():
        if count>n/2:
            return num
        
    return -1
