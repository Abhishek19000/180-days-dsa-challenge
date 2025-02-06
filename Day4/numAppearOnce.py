#Find the number that appear once in an array

#BruteForce: O(n^2)

def numAppearOnce(arr:list[int])->int:

    for i in range(len(arr)):
        cnt=0
        ele=arr[i]
        for j in range(i,len(arr)):

            if(arr[j]==ele):
                cnt=cnt+1

        if(cnt==1):
            return ele


    return -1

#Better Solution: O(NlogM)+O(M)

def numAppearOnce(arr:list[int])->int:

    eleFreq={}

    for num in arr:
        eleFreq[num]=eleFreq.get(num,0)+1

    for num in eleFreq:
        if eleFreq[num]==1:
            return num
        
    return num

#Optimal Solution: O(n)

def numAppearOnce(arr:list[int])->int:

    xor=0
    for num in arr:
        xor^=num

    return xor