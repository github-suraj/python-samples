'''
    Example to catch command line arguments using argparse
'''

import argparse

def argparse_example():
    '''
        Simple Example of argparse usage
        Ex. -
            python argparse_argv.py 1 2 3 4 5 --sum
    '''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
        'integers',
        metavar='N',
        type=int,
        nargs='+',
        help='an integer for the accumulator'
    )
    parser.add_argument(
        '--sum',
        dest='accumulate',
        action='store_const',
        const=sum,
        default=max,
        help='sum the integers (default: find the max)'
    )
    args = parser.parse_args()
    print('Sum of Numbers:', args.accumulate(args.integers))


def argparse_sub_commands():
    '''
        Example of argparse Sub-Commands
        Ex. -
            python argparse_argv.py 1 2 3 4 5 6 7 8 MAX-MIN --min
                OR
            python argparse_argv.py 1 2 3 4 5 6 7 8 MAX-MIN --max
                OR
            python argparse_argv.py 1 2 3 4 5 SUM --sum
    '''
    parser = argparse.ArgumentParser(
        prog='NUMBER',
        description='Get Max/Min of Numbers',
        epilog='This is the last line of Help'
    )
    parser.add_argument(
        'integers',
        metavar='N',
        type=int,
        nargs='+',
        help='Integers'
    )
    subparsers = parser.add_subparsers(help='sub-command help')
    parser_mm = subparsers.add_parser('MAX-MIN', help='Max-Min help')
    parser_mm.add_argument(
        '--max',
        dest='accumulate',
        action='store_const',
        const=max,
        help='Maximum of Integers'
    )
    parser_mm.add_argument(
        '--min',
        dest='accumulate',
        action='store_const',
        const=min,
        help='Minimum of Integers'
    )
    parser_su = subparsers.add_parser('SUM', help='Min help')
    parser_su.add_argument(
        '--sum',
        dest='accumulate',
        action='store_const',
        const=sum,
        help='Sum of Integers'
    )
    args = parser.parse_args()
    print('Result:', args.accumulate(args.integers))


def argparse_grouping():
    '''
        Example of argparse Grouping
        Ex. -
            python argparse_argv.py 1 2 3 4 5 --max
                OR
            python argparse_argv.py 1 2 3 4 5 --min
    '''
    parser = argparse.ArgumentParser(prog='PROG', add_help=False)
    parser.add_argument(
        'integers',
        metavar='N',
        type=int,
        nargs='+',
        help='Integers'
    )
    group = parser.add_argument_group('Max-Min Grop')
    group.add_argument(
        '--max',
        dest='accumulate',
        action='store_const',
        const=max,
        help='Maximum of Integers')
    group.add_argument(
        '--min',
        dest='accumulate',
        action='store_const',
        const=min,
        help='Minimum of Integers'
    )
    args = parser.parse_args()
    print('Result:', args.accumulate(args.integers))


def argparse_mutual_exclusive():
    '''
        Example of argparse Mutual-Exclusive Group
        Ex. -
            python argparse_argv.py --skip
                OR
            python argparse_argv.py --force
    '''
    parser = argparse.ArgumentParser(prog='PROG', add_help=False)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--skip', action='store_true', help='Skipping')
    group.add_argument('--force', action='store_true', help='Forcing')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    # argparse_example()
    # argparse_sub_commands()
    # argparse_grouping()
    argparse_mutual_exclusive()
