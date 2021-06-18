def star_pattern(rows):
    ''' 
        *
        **
        ***
        ****
        *****
    '''
    for i in range(rows):
        print('*'*(i+1))

def star_pattern_rjust(rows):
    ''' 
            *
           **
          ***
         ****
        *****
    '''
    for i in range(rows):
        print(('*'*(i+1)).rjust(rows))

def inverted_star_pattern(rows):
    ''' 
        *****
        ****
        ***
        **
        *
    '''
    for i in range(rows):
        print('*'*(rows-i))

def inverted_star_pattern_rjust(rows):
    ''' 
        *****
         ****
          ***
           **
            *
    '''
    for i in range(rows):
        print(('*'*(rows-i)).rjust(rows))
    
def star_pattern_block(rows):
    '''
        **********
        ****  ****
        ***    ***
        **      **
        *        *
        *        *
        **      **
        ***    ***
        ****  ****
        **********
    '''
    for i in range(rows):
        print(('*'*(rows-i)).ljust(rows) + ('*'*(rows-i)).rjust(rows))
    for i in range(rows):
        print(('*'*(i+1)).ljust(rows) + ('*'*(i+1)).rjust(rows))
