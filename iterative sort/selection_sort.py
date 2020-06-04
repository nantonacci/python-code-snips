# iterative selection sort

def selection_sort(arr):

    for i in range(0, len(arr) - 1):

        cur_index = i

        smallest_index = cur_index

        for n in range(i+1, len(arr)):

            if arr[smallest_index] > arr[n]:

                smallest_index = n

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        
    return arr