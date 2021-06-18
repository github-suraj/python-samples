from string import ascii_lowercase
from reverse import reverse_string, reverse_number

def is_string_palindrome(string):
    '''
        Method to check if a string is palindrome or not
        (actual string and it's reverse is equal or not)
    '''
    _string = reverse_string(string)
    if string.lower() == _string.lower():
        return True
    return False

def is_phrase_palindrome(phrase):
    '''
        Method to check if a phrase/sentence is palindrome or not
            *** Only alphabets will be considered ***
        (actual phrase and it's reverse is equal or not)
    '''
    phrase = ''.join(filter(lambda c: c in ascii_lowercase, phrase.lower()))
    for i in range(len(phrase)//2):
        if phrase[i] != phrase[-1-i]:
            return False
    return True

def is_number_palindrome(num):
    '''
        Function to check if a number is palindrome or not
        (actual number and it's reverse is equal or not)
    '''
    _num = reverse_number(num)
    if num == _num:
        return True
    return False
