# iterative count sort

def count_sort(arr, maximum=None):

    if len(arr) > 0:

        maximum = max(arr) + 1
        listO = [0] * maximum
        bucket = []

        for i in arr:

            if i < 0:

                return "Error, negative numbers not allowed in Count Sort"
                
            else:

                listO[i] += 1

        for n in range(len(listO)):
            
            bucket.extend([n] * listO[n])

        return bucket

    else:
        return arr