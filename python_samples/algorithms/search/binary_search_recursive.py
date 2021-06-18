def binary_search(arr, element):
    '''Python Program for Binary Search (Recursive)'''
    arr.sort()
    def binary_search_inner(arr, low, high, element):
        if low <= high:
            mid = (low + high) // 2
            if arr[mid] < element:
                return binary_search_inner(arr, mid + 1, high, element)
            elif arr[mid] > element:
                return binary_search_inner(arr, low, mid, element)
            else:
                return mid
        else:
            return -1
    return binary_search_inner(arr, 0, len(arr)-1, element)
