import math
from decorators import elapsed_time, memoize

def is_fibonacci_number(n):
    '''Function to check if a number is a fibonacci series number or not'''
    if n == 0:
        return True
    n1 = 5 * n ** 2 + 4
    n2 = 5 * n ** 2 - 4
    s1 = math.floor(math.sqrt(n1))
    s2 = math.floor(math.sqrt(n2))
    if math.pow(s1, 2) == n1 or math.pow(s2, 2) == n2:
        return True
    return False

@memoize
def nth_fibonacci_number(n):
    '''Function 2 to get nth fibonacci series numbers'''
    if n < 0:
        raise TypeError(f"Expected value equal to or greater than zero(0), but got {n}")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return nth_fibonacci_number(n-1) + nth_fibonacci_number(n-2)

@elapsed_time
def first_n_fibonacci_numbers1(n):
    '''Function 1 to get first n fibonacci series numbers'''
    fibonacci = list()
    for num in range(n):
        fibonacci.append(nth_fibonacci_number(num))
    return fibonacci

@elapsed_time
def first_n_fibonacci_numbers2(n):
    '''Function 2 to get first n fibonacci series numbers'''
    if n < 1:
        raise TypeError(f"Expected value greater than zero(0), but got {n}")
    a, b = 0, 1
    fibonacci = list()
    while True:
        fibonacci.append(a)
        a, b = b, a + b
        if len(fibonacci) == n:
            break
    return fibonacci
