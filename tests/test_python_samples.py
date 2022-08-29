import pytest
from generators import inclusive_range as inclusive_range_gen
from iterators import inclusive_range as inclusive_range_itr

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
