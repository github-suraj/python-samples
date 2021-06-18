from functions.dicts import list_of_tuple_to_dict, add_two_dicts
from functions.strings import (is_substring, get_even_length_words, 
        all_vowels_present, remove_duplicates, contains_all_unique)
from functions.lists import (swap_elements, swap_elements1, numbers_square,
        numbers_cube, remove_nth_occurrence, list_length, is_element_exists)

def test_functions_for_dict():
    dict1 = {'A': 72, 'B': 27, 'C': 7, 'D': 53}
    dict2 = {'C': 53, 'D': 42, 'E': 92, 'F': 94}
    list_of_tup = (('A', 72), ('B', 27), ('C', 7), ('D', 53))
    assert list_of_tuple_to_dict(list_of_tup) == dict(list_of_tup) == dict1, "Test Failed"
    expected = {'A': 72, 'B': 27, 'C': 53, 'D': 42, 'E': 92, 'F': 94}
    assert add_two_dicts(dict1, dict2) == dict(dict1, **dict2) == expected, "Test Failed"

def test_functions_for_string(capsys):
    _str = 'Python is easy'
    substr1 = 'is'
    substr2 = 'hello'
    assert is_substring(_str, substr1) == (substr1 in _str) == True, "Test Failed"
    assert is_substring(_str, substr2) == (substr2 in _str) == False, "Test Failed"
    assert get_even_length_words(_str) == ['Python', 'is', 'easy'], "Test Failed"
    assert all_vowels_present('hello world!') == 'Not Accepted', "Test Failed"
    assert capsys.readouterr().out.rstrip() == "['a', 'i', 'u'] are not present"
    assert all_vowels_present('Hi, how are you?') == 'Accepted', "Test Failed"
    assert capsys.readouterr().out.rstrip() == "All vowels are present"
    assert remove_duplicates('Malayalam') == 'Maly', "Test Failed"
    assert contains_all_unique('malayalam') == False, "Test Failed"
    assert contains_all_unique('python') == True, "Test Failed"

def test_functions_for_list():
    _list = [6, 9, 3, 7, 1, 2, 8]
    expected = [1, 9, 3, 7, 6, 2, 8]
    assert swap_elements(_list[:], 0, 4) == swap_elements1(_list[:], 0, 4) == expected, "Test Failed"
    _list = [1, 2, 3, 4]
    assert numbers_square(_list) == [(1, 1), (2, 4), (3, 9), (4, 16)], "Test Failed"
    assert numbers_cube(_list) == [(1, 1), (2, 8), (3, 27), (4, 64)], "Test Failed"
    _list = ['python', 'is', 'easy', 'is', 'english', 'is', 'best']
    expected = ['python', 'is', 'easy', 'english', 'is', 'best']
    assert remove_nth_occurrence(_list[:], 'is', n=2) == expected,  "Test Failed"
    assert list_length(_list) == 7, "Test, Failed"
    assert is_element_exists(_list, 'easy') == True, "Test Failed"
    assert is_element_exists(_list, 'Easy') == False, "Test Failed"
