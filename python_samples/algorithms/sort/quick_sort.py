def partition(arr, start, end):
    '''Function to set pivot at correct position'''
    pivot_idx = start
    pivot = arr[pivot_idx]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        
        while arr[end] > pivot:
            end -= 1
        
        if start < end and start != end:
            arr[end], arr[start] = arr[start], arr[end]
    
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]
    return end

def quick_sort(arr):
    '''Python Program for Quick Sort'''
    def quick_sort_inner(arr, start, end):
        '''Recursive function to set pivot index at correct position'''
        if start < end:
            pi = partition(arr, start, end)
            quick_sort_inner(arr, start, pi - 1)
            quick_sort_inner(arr, pi + 1, end)
    quick_sort_inner(arr, 0, len(arr) - 1)
    return arr
