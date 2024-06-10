def binary_search(arr,item):

    n=len(arr)
    mid=n//2

    r=n
    l=0

    while l<r:
        mid=(l+r)//2
        if arr[mid]==item:
            return mid
        
        if arr[mid]>item:
            r=mid
        elif arr[mid]<item:
            l=mid
        
    return -1

arr=[1, 2, 3, 4, 5, 6, 7, 8, 9]
res=binary_search(arr,3)

print(res)