from decorators import elapsed_time, memoize

@memoize
def nth_lucas_number(n):
    '''Function to get nth lucas series numbers'''
    if n < 0:
        raise TypeError(f"Expected value equal to or greater than zero(0), but got {n}")
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    return nth_lucas_number(n-1) + nth_lucas_number(n-2)

@elapsed_time
def first_n_lucas_numbers1(n):
    '''Function 1 to get first n lucas series numbers'''
    lucas = list()
    for num in range(n):
        lucas.append(nth_lucas_number(num))
    return lucas

@elapsed_time
def first_n_lucas_numbers2(n):
    '''Function 2 to get first n lucas series numbers'''
    if n < 1:
        raise TypeError(f"Expected value greater than zero(0), but got {n}")
    a, b = 2, 1
    lucas = list()
    while True:
        lucas.append(a)
        a, b = b, a + b
        if len(lucas) == n:
            break
    return lucas
