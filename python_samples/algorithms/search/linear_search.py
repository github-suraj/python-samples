def linear_search(arr, element):
    '''Python Program for Linear Search'''
    for i, x in enumerate(arr):
        if x == element:
            return i
    return -1
