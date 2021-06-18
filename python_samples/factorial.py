from functools import reduce
from decorators import memoize

@memoize
def factorial(n):
    '''Function to calculate factorial of a numbers using recursion'''
    if n < 0:
        raise TypeError(f"Expected value equal to or greater than zero(0), but got {n}")
    elif n == 0:
        return 1
    return n * factorial(n-1)

def factorial_using_itr(n):
    '''Function to calculate factorial of a numbers using iteration'''
    if n < 0:
        raise TypeError(f"Expected value equal to or greater than zero(0), but got {n}")
    fact = 1
    while n:
        fact = fact * n
        n = n - 1
    return fact

def factorial_using_reduce(n):
    '''Function to calculate factorial of a numbers using reduce'''
    if n < 0:
        raise TypeError(f"Expected value equal to or greater than zero(0), but got {n}")
    if n == 0 or n == 1:
        return 1
    return reduce(lambda a, b: a*b, range(1, n+1))
