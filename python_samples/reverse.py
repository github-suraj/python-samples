def reverse_string(string):
    '''Function to reverse a string'''
    _string = ''
    for i in range(len(string)):
        _string += string[len(string) - i - 1]
    return _string

def reverse_number(num):
    '''Function to reverse a number'''
    _num = 0
    while num:
        (num, r) = divmod(num, 10)
        _num = _num * 10 + r
    return _num

def reverse_phrase(phrase):
    '''Function to reverse words in a given phrase/sentence'''
    phrase = phrase.split()
    _phrase = ' '.join(phrase[::-1])
    return _phrase

def reverse_list(arr):
    '''
        Function to reverse elements of array
            _arr = arr[::-1]                                        # Using negative indexing
                or
            _arr = list(reversed(arr))                              # Using reversed function
                or
            arr.reverse()                                           # Using reverse method
                or 
            _arr = [arr[len(arr)-1-i] for i in range(len(arr))]     # Using Comprehension
    '''
    _arr = list()
    arr_size = len(arr)
    for i in range(arr_size):
        _arr.append(arr[arr_size - i - 1])
    return _arr
