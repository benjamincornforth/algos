import random
import logging

# Set up logging
logging.basicConfig(filename='heap_sort_debug.log', level=logging.DEBUG, 
                    format='%(message)s')

def heapify(arr, n, i):
    logging.debug(f"Heapify called with i={i}, n={n}")
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n:
        logging.debug(f"Comparing arr[{i}]={arr[i]} with left child arr[{l}]={arr[l]}")
        if arr[i] < arr[l]:
            largest = l

    if r < n:
        logging.debug(f"Comparing arr[{largest}]={arr[largest]} with right child arr[{r}]={arr[r]}")
        if arr[largest] < arr[r]:
            largest = r

    if largest != i:
        logging.debug(f"Swapping arr[{i}]={arr[i]} with arr[{largest}]={arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        logging.debug(f"Array after swap: {arr}")
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    logging.debug(f"Original array: {arr}")
    
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        logging.debug(f"Building heap with heapify called on index {i}")
        heapify(arr, n, i)
        logging.debug(f"Array after heapify on index {i}: {arr}")

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        logging.debug(f"Swapping arr[0]={arr[0]} with arr[{i}]={arr[i]}")
        arr[i], arr[0] = arr[0], arr[i]
        logging.debug(f"Array after extracting max element: {arr}")
        heapify(arr, i, 0)
        logging.debug(f"Array after heapify post-extraction: {arr}")

    logging.debug(f"Sorted array: {arr}")

# Example usage
list = [random.randint(3, 100) for _ in range(10)]
print("Unsorted list:", list)
heap_sort(list)
print("Sorted list:", list)
