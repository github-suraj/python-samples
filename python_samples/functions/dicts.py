def list_of_tuple_to_dict(list_of_tup):
    '''
        Convert a list of Tuples into Dictionary
            _dict = dict(list_of_tup)
    '''
    _dict = dict()
    for ele1, ele2 in list_of_tup:
        _dict[ele1] = ele2
    return _dict

def add_two_dicts(d1, d2):
    '''
        Python program to two dictionary
            _dict = dict(d1, **d2)
    '''
    _dict = dict()
    for key, val in d1.items():
        _dict[key] = val
    for key, val in d2.items():
        _dict[key] = val
    return _dict
