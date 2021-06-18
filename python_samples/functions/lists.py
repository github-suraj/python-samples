def swap_elements(arr, pos1, pos2):
    '''Function 2 to interchange elements at position1 and position2 in a list'''
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr

def swap_elements1(arr, pos1, pos2):
    '''Function 1 to interchange elements at position1 and position2 in a list'''
    _temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = _temp
    return arr

def numbers_square(arr):
    '''Python program to create a list of tuples from given list having number and its square in each tuple'''
    square = list(map(lambda x: (x, x**2), arr))
    return square

def numbers_cube(arr):
    '''Python program to create a list of tuples from given list having number and its cube in each tuple'''
    square = list(map(lambda x: (x, x**3), arr))
    return square

def remove_nth_occurrence(arr, word, n):
    '''Python program to remove Nth occurrence of the given word'''
    count = 0
    for i, w in enumerate(arr):
        if word == w:
            count += 1
        if count == n:
            arr.pop(i); break
    return arr

def list_length(arr):
    '''
        Python program to get length of a array
            return len(arr)             # Using len function
                or 
            return arr.__len__()        # Using list magic method
    '''
    count = 0
    for i in arr:
        count += 1
    return count

def is_element_exists(arr, element):
    '''
        Python program to check if element exists in list
            return 'perfect' in arr                                   # Using in Operator
                or
            return bool([ele for ele in arr if ele == 'perfect'])     # Using Comprehension
                or
            return bool(arr.count('perfect'))                         # Using count method
                or
            return any(ele for ele in arr if ele == 'perfect')        # Using any function
    '''
    for ele in arr:
        if ele == element:
            return True
    return False
