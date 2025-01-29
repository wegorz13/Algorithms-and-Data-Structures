from math import floor

def bucketSort(array):
    n=len(array)
    bucket = [[]*n]

    # Insert elements into their respective buckets
    for j in array:
        index_b = floor(n * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(n):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array
