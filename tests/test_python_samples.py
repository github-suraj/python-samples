import pytest
from generators import inclusive_range as inclusive_range_gen
from iterators import inclusive_range as inclusive_range_itr
from max_subarray_sum import max_subarray_sum1, max_subarray_sum2
from reverse import reverse_string, reverse_number, reverse_phrase, reverse_list
from is_palindrome import is_string_palindrome, is_phrase_palindrome, is_number_palindrome
from is_armstrong import is_armstrong_number
from factorial import factorial, factorial_using_itr, factorial_using_reduce

def test_generators():
    with pytest.raises(TypeError) as err:
        list(inclusive_range_gen())
        assert err.exception == "inclusive_range expected at least 1 argument, got 0", "Test Failed"
    with pytest.raises(TypeError) as err:
        list(inclusive_range_gen(1, 100, 2, 2))
        assert err.exception == "inclusive_range expected at most 3 arguments, got 4", "Test Failed"
    assert tuple(inclusive_range_gen(10)) == tuple(range(10)) + (10,), "Test Failed"
    assert tuple(inclusive_range_gen(5, 10)) == tuple(range(5, 10)) + (10,), "Test Failed"
    assert tuple(inclusive_range_gen(1, 11, 2)) == tuple(range(1, 11, 2)) + (11, ), "Test Failed"

def test_iterators():
    with pytest.raises(TypeError) as err:
        list(inclusive_range_itr())
        assert err.exception == "inclusive_range expected at least 1 argument, got 0", "Test Failed"
    with pytest.raises(TypeError) as err:
        list(inclusive_range_itr(1, 100, 2, 2))
        assert err.exception == "inclusive_range expected at most 3 arguments, got 4", "Test Failed"
    assert tuple(inclusive_range_itr(10)) == tuple(range(10)) + (10,), "Test Failed"
    assert tuple(inclusive_range_itr(5, 10)) == tuple(range(5, 10)) + (10,), "Test Failed"
    assert tuple(inclusive_range_itr(1, 11, 2)) == tuple(range(1, 11, 2)) + (11, ), "Test Failed"

def test_max_subarray_sum():
    with pytest.raises(TypeError) as err:
        max_subarray_sum1(list())
        assert err.exception == "iterable expected to have at least 1 element", "Test Failed"
    with pytest.raises(TypeError) as err:
        max_subarray_sum2(list())
        assert err.exception == "iterable expected to have at least 1 element", "Test Failed"
    mylist = [-2, -3, 4, -1, -2, 1, 5, -3]
    assert max_subarray_sum1(mylist) == max_subarray_sum2(mylist) == 7, "Test Failed"

def test_reverse():
    _str = 'Python is easy'
    _list = ['welcome', 'to', 'perfect', 'plan', 'b']
    expected = ['b', 'plan', 'perfect', 'to', 'welcome']
    assert reverse_string(_str) == 'ysae si nohtyP', "Test Failed"
    assert reverse_phrase(_str) == 'easy is Python', "Test Failed"
    assert reverse_number(123456789) == 987654321, "Test Failed"
    assert reverse_list(_list) == _list[::-1] == expected, "Test Failed"

def test_is_palindrome_string():
    string1 = 'hello world'
    string2 = 'malayalAM'
    phrase = 'Too hot to hoot.'
    assert is_string_palindrome(string1) == is_phrase_palindrome(string1) == False, "Test Failed"
    assert is_string_palindrome(string2) == is_phrase_palindrome(string2) == True, "Test Failed"
    assert is_phrase_palindrome(phrase) == True, "Test Failed"

def test_is_palindrome_numbers():
    assert is_number_palindrome(123456789) == False, "Test Failed"
    assert is_number_palindrome(12345678987654321) == True, "Test Failed"

def test_is_armstrong_number():
    assert is_armstrong_number(1634) == True, "Test Failed"
    assert is_armstrong_number(720) == False, "Test Failed"

def test_factorial():
    # Negative numbers
    with pytest.raises(TypeError) as err:
        result = factorial(-10)
        assert err.exception == "Expected value equal to or greater than zero(0), but got -10"
    with pytest.raises(TypeError) as err:
        result = factorial_using_itr(-10)
        assert err.exception == "Expected value equal to or greater than zero(0), but got -10"
    with pytest.raises(TypeError) as err:
        result = factorial_using_reduce(-10)
        assert err.exception == "Expected value equal to or greater than zero(0), but got -10"
    # Zero
    assert factorial(0) == factorial_using_itr(0) == factorial_using_reduce(0) == 1, "Test Failed"
    # One
    assert factorial(1) == factorial_using_itr(1) == factorial_using_reduce(1) == 1, "Test Failed"
    # any number > 1
    assert factorial(8) == factorial_using_itr(8) == factorial_using_reduce(8) == 40320, "Test Failed"
