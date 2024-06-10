def bubble_sort(arr):
    n=len(arr)
    
    swapped=True
    while swapped:
        swapped=False
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                swapped=True
                arr[i-1],arr[i]=arr[i],arr[i-1]
    
    return arr


arr=[9,8,7,6,5,4,3,2,1]

res=bubble_sort(arr)
print(res)