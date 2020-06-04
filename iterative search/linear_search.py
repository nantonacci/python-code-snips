# iterative linear search

def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):

        if arr[i] == target:
            
            return i

    return -1   # not found