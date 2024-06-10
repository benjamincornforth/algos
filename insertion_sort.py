def insertion_sort(arr):
    sorted_idx=0
    n=len(arr)
    j=-1
    while sorted_idx<n-1 :
        j=sorted_idx
        for i in range(sorted_idx,n):
            if arr[i]<arr[j]:
                j=i
            
        arr[sorted_idx],arr[j]=arr[j],arr[sorted_idx]
        sorted_idx+=1
    
    return arr


arr=[9,8,7,6,5,4,3,2,1]

print(insertion_sort(arr))