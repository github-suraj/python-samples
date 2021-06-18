def merge_two_sorted_lists(left, right, arr):
    '''Function to merge two sorted arrays'''
    len_l = len(left)
    len_r = len(right)
    i = j = k = 0
    while i < len_l and j < len_r:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len_l:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len_r:
        arr[k] = right[j]
        j += 1
        k += 1
    return arr

def merge_sort(arr):
    '''Python Program for Merge Sort'''
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_two_sorted_lists(left, right, arr)
