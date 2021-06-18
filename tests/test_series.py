from series.fibonacci_numbers import (is_fibonacci_number, nth_fibonacci_number,
            first_n_fibonacci_numbers1, first_n_fibonacci_numbers2)
from series.lucas_numbers import (nth_lucas_number,
            first_n_lucas_numbers1, first_n_lucas_numbers2)
from series.prime_numbers import (is_prime1, is_prime2,
            get_prime_numbers1, get_prime_numbers2)

def test_fibonacci_numbers():
    assert is_fibonacci_number(10) == False, "Test Failed"
    assert is_fibonacci_number(34) == True, "Test Failed"
    result1 = nth_fibonacci_number(9)
    result2 = first_n_fibonacci_numbers1(10)
    result3 = first_n_fibonacci_numbers2(10)
    assert result1 == result2[9] == result3[9] == 34, "Test Failed"
    assert len(result2) == len(result3) == 10, "Test Failed"
    assert result2 == result3, "Test Failed"

def test_lucas_numbers():
    result1 = nth_lucas_number(9)
    result2 = first_n_lucas_numbers1(10)
    result3 = first_n_lucas_numbers2(10)
    assert result1 == result2[9] == result3[9] == 76, "Test Failed"
    assert len(result2) == len(result3) == 10, "Test Failed"
    assert result2 == result3, "Test Failed"

def test_prime_numbers():
    primes1 = [i for i in range(1, 100) if is_prime1(i)]
    primes2 = [i for i in range(1, 100) if is_prime2(i)]
    primes3 = get_prime_numbers1(1, 100)
    primes4 = get_prime_numbers2(1, 100)
    assert len(primes1) == len(primes2) == len(primes3) == len(primes4) == 25, "Test Failed"
    assert primes1 == primes2 == primes3 == primes4, "Test Failed"
