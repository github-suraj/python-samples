def selection_sort(arr):
    '''Python Program for Selection Sort'''
    n = len(arr)
    # Traverse through all list elements
    for i in range(n):
        # Find the minimum element in un-sorted list
        min_idx = i
        for j in range(i, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap the minimum element with the first index element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
