from typing import List

def longest(arr: List[int])-> int:
    longest=j=0
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]+1:
            longest=max(longest,i-j)
        else:
            j=i-1

    return i-j


arr=[2,20,4,10,3,4,5]

res=longest(arr)
print(res)