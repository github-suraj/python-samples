def binary_search(arr, element):
    '''Python Program for Binary Search (Iterative)'''
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < element:
            low = mid + 1
        elif arr[mid] > element:
            high = mid
        else:
            return mid
    return -1
