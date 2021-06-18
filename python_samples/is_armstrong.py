from functools import reduce

def is_armstrong_number(num):
    '''
        Function to check if a number is a armstrong number or not
        Ex.- num = 1634
            number of digits = 4
            new_num = 1**4 + 6**4 + 3**4 + 4**4
            num == new_num
    '''
    digits = list()
    n = num
    while n:
        (n, r) = divmod(n, 10)
        digits.append(r)
    numlen = len(digits)
    _num = reduce(lambda a, b: a + b, map(lambda a: a ** numlen, digits))
    if num == _num:
        return True
    return False
