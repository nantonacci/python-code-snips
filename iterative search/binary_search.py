# iterative binary search

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (high+low)//2

        if target == arr[middle]:

            return middle

        elif arr[middle] > target:

            high = middle-1

        elif arr[middle] < target:

            low = middle+1
        
    return -1  # not found