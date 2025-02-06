#Find the union of the two arrays

#BruteForce : O((m+n)log(m+n))

def unionArr(arr1:list[int],arr2:list[int])->list[int]:

    eleFreq={}

    union=[]

    for num in arr1:

        eleFreq[num]=eleFreq.get(num,0)+1

    for num in arr2:

        eleFreq[num]=eleFreq.get(num,0)+1
        
    for num in eleFreq.keys():

        union.append(num)

    return union

#Optimal Solution: O(m+n)

def unionArr(arr1:list[int],arr2:list[int])->list[int]:

    arr1len=len(arr1)
    arr2len=len(arr2)
    union=[]
    i=0
    j=0

    while(i<arr1len and j<arr2len):

        if(arr1[i]<arr2[j]):
            if(len(union)==0 or union[-1]!=arr1[i]):
                union.append(arr1[i])
            i=i+1
        else:
            if(len(union)==0 or union[-1]!=arr2[j]):
                union.append(arr2[j])
            j=j+1

    while(i<arr1len):
        if(len(union)==0 or union[-1]!=arr1[i]):
             union.append(arr1[i])
        i=i+1

    while(j<arr2len):
        if(len(union)==0 or union[-1]!=arr2[j]):
            union.append(arr2[j])
        j=j+1

    return union