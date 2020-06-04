# iterative bubble sort

def bubble_sort(arr):

    for i in range(len(arr)-1):

        for n in range(len(arr)-i-1):

            if arr[n] > arr[n+1]:
                
                arr[n], arr[n+1] = arr[n+1], arr[n]

    return arr