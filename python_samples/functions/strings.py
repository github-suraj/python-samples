from string import ascii_letters

def is_substring(_string, _substring):
    '''
        Check if a Substring is Present in a Given String
            return _substring in _string
    '''
    if _string.find(_substring) == -1:
        return False
    return True

def get_even_length_words(phrase):
    '''Python program to print even length words in a string'''
    words = list()
    for word in phrase.split():
        if len(word) % 2 == 0:
            words.append(word)
    return words

def all_vowels_present(_string):
    '''Program to accept the strings which contains all vowels'''
    vowels = set('aeiou')
    diff = vowels - set(_string.lower())
    if len(diff) > 0:
        print(sorted(list(diff)), 'are not present')
        return 'Not Accepted'
    print('All vowels are present')
    return 'Accepted'

def remove_duplicates(_string):
    '''
        Remove all duplicates from a given string in Python
             *** Only alphabets will be considered ***
    '''
    unique = ''
    for c in _string:
        if c not in ascii_letters:
            continue
        if c.lower() not in unique.lower():
            unique += c
    return unique

def contains_all_unique(_string):
    '''Python program to check if a string contains all unique characters'''
    if len(set(_string)) == len(_string):
        return True
    return False
