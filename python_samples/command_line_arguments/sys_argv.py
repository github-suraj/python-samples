'''
    Example to catch command line arguments using sys.argv
'''

import sys

def main():
    '''
        Function storing values from command line arguments
    '''
    argv = sys.argv
    if len(argv) >= 4:
        script_name, first, last, age, *rest = argv
        print('Script:', script_name)
        print('First Name:', first)
        print('Last Name:', last)
        print('Age:', age)
    else:
        print(f"""Error:
            Script Required at least 3 arguments
                1. first_name
                2. last_name
                3. age
            You have passed {len(argv) - 1} arguments
        """)

if __name__ == '__main__':
    main()
