def bubble_sort(arr):
    '''Python Program for Bubble Sort'''
    n = len(arr)
    # Traverse through all list elements
    for i in range(n):
        swapped = False
        # Last i elements are already sorted/in place
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # If no two eleents were swapped by inner loop, the list is already sorted
        if not swapped:
            break
    return arr
