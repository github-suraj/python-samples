from decorators import elapsed_time

@elapsed_time
def max_subarray_sum1(_list):
    '''Function 1 to get the maximum subarray/sublist sum for an iterable having numbers'''
    if len(_list) == 0:
        raise TypeError("iterable expected to have at least 1 element")
    max_so_far = _list[0]
    max_ending_here = 0
    for num in _list:
        max_ending_here += num
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

@elapsed_time
def max_subarray_sum2(_list):
    '''Function 2 to get the maximum subarray/sublist sum for an iterable having numbers'''
    if len(_list) == 0:
        raise TypeError("iterable expected to have at least 1 element")
    max_so_far = _list[0]
    max_ending_here = _list[0]
    for num in _list[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
