import random
from algorithms.search.linear_search import linear_search
from algorithms.search.binary_search_recursive import binary_search
from algorithms.search.binary_search_iterative import binary_search as binary_search_itr
from algorithms.sort.bubble_sort import bubble_sort
from algorithms.sort.selection_sort import selection_sort
from algorithms.sort.insertion_sort import insertion_sort
from algorithms.sort.heap_sort import heap_sort
from algorithms.sort.merge_sort import merge_sort
from algorithms.sort.quick_sort import quick_sort
from algorithms.tower_of_hanoi import tower_of_hanoi

def test_linear_search(num=596, num1=1000):
    array = list(range(num1))
    random.shuffle(array)
    idx1 = array.index(num)
    idx2 = linear_search(array, num)
    assert idx1 == idx2, "Test Failed"
    idx = linear_search(array, num1)
    assert idx == -1, "Test Failed"

def test_binary_search(num=596, num1=1000):
    array = list(range(num1))
    random.shuffle(array)
    idx1 = binary_search(array, num)
    idx2 = binary_search_itr(array, num)
    assert idx1 == idx2 == num, "Test Failed"
    idx1 = binary_search(array, num1)
    idx2 = binary_search_itr(array, num1)
    assert idx1 == idx2 == -1, "Test Failed"

def test_sorting():
    _array = list(range(9001, 10001))
    array = _array.copy()
    random.shuffle(array)
    results = [_array, _array, _array, [], [10]]
    cases = [array, _array, sorted(_array, reverse=True), [], [10]]
    for i, arr in enumerate(cases):
        assert results[i] == bubble_sort(arr), "Test Failed"
        assert results[i] == selection_sort(arr), "Test Failed"
        assert results[i] == insertion_sort(arr), "Test Failed"
        assert results[i] == heap_sort(arr), "Test Failed"
        assert results[i] == merge_sort(arr), "Test Failed"
        assert results[i] == quick_sort(arr), "Test Failed"

def test_tower_of_hanoi(capsys):
    expected = ['Moving disk 1 from A to C', 'Moving disk 2 from A to B', 'Moving disk 1 from C to B','Moving disk 3 from A to C', 'Moving disk 1 from B to A', 'Moving disk 2 from B to C', 'Moving disk 1 from A to C']
    tower_of_hanoi(3, 'A', 'C', 'B')
    cap = capsys.readouterr()
    assert cap.out.splitlines() == expected
