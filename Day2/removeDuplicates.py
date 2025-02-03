#Remove duplicates from the array


#BruteForce :- O(nlogn)+O(n)

def removeDup(arr:list[int])->list[int]:

    st=set()
    arr2=[]
    arrlen=len(arr)
    for i in range(arrlen):
        st.add(arr[i])
 
    j=0
    for num in st:
        arr2.append(num)
        j+=1
    
    return arr2


#Optimized Solution :- O(n)

def removeDuplicates(arr: list[int]) -> list[int]:
    seen = set()
    arr2 = []
    for num in arr:  # Loop through each element in arr (O(N))
        if num not in seen: 
            seen.add(num) 
            arr2.append(num) 
    return arr2
    