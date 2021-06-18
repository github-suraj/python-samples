import math
from decorators import elapsed_time

'''
Elapsed Time : 123.60299468040466
1000007279 is a Prime Number
'''
@elapsed_time
def is_prime1(n):
    '''Method 1 to check if a number is a prime or not'''
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

'''
Elapsed Time : 0.021999120712280273
1000007279 is a Prime Number
'''
@elapsed_time
def is_prime2(n):
    '''Method 2 to check if a number is a prime or not'''
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n)) + 1
    for i in range(2, max_div):
        if n % i == 0:
            return False
    return True

'''
Elapsed Time : 0.0019960403442382812
1000007279 is a Prime Number
'''
def is_prime3(n):
    '''Method 3 to check if a number is a prime or not'''
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(n)) + 1
    for i in range(3, max_div, 2):
        if n % i == 0:
            return False
    return True

'''
Elapsed Time : 3.897956371307373
Prime numbers between 1 and 1000000 : 78498
'''
@elapsed_time
def get_prime_numbers1(start, end):
    '''Function to get prime numbers between two numbers'''
    primes = list()
    for num in range(start, end+1):
        if is_prime3(num):
            primes.append(num)
    return primes

'''
Elapsed Time : 0.4239964485168457
Prime numbers between 1 and 1000000 : 78498
'''
@elapsed_time
def get_prime_numbers2(start, end):
    '''Sieve Method to get prime numbers between two numbers'''
    if start < 2:
        start = 2
    primes = [True for i in range(end+1)]
    p = 2
    while p * p <= end:
        if primes[p]:
            for i in range(p * p, end+1, p):
                primes[i] = False
        p += 1
    primes = [i for i, value in enumerate(primes) if value and i >= start]
    return primes
