# O(nlogn)
# W rzeczywistości złożoność Quicksorta może osiągnąć nawet O(n^2) przy słabym wybieraniu pivota


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def partition2(array, low, high):
    i = low
    j = high - 1
    pivot = array[high]

    while i < j:
        while i < high and array[i] < pivot:
            i += 1
        while j > low and array[j] >= pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[high] = array[high], array[i]
    #end while
    return i

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


arr = [7, 2, 1, 6, 8, 5, 3, 4]
quicksort(arr, 0, len(arr) - 1)
print(arr)