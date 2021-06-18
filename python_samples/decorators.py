from functools import wraps
from time import time

def elapsed_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''Function to get elapsed time for another function'''
        t = time()
        result = func(*args, **kwargs)
        print('Elapsed Time :', time() - t)
        return result
    return wrapper

def memoize(func):
    memory = dict()
    @wraps(func)
    def wrapper(n):
        '''Function to calculte some math problems with memoization'''
        if n not in memory:
            memory[n] = func(n)
        return memory[n]
    return wrapper
