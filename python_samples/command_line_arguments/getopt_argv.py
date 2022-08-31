'''
    Example to catch command line arguments using getopt
'''

import sys
import getopt

def main():
    '''
        Function storing values from command line arguments

        getopt.gnu_getopt(args, shortopts, longopts=[])
            This function works like getopt(),
            except that GNU style scanning mode is used by default.
            This means that option and non-option arguments may be intermixed.
        The getopt() function stops processing options as soon as
            a non-option argument is encountered.
    '''
    script_name = sys.argv[0]
    # options, remainder = getopt.getopt(
    #                           sys.argv[1:], 'n:a:vd',
    #                           ['name=', 'age=', 'verbose', 'debug']
    #                       )

    options, remainder = getopt.gnu_getopt(
                            sys.argv[1:], 'n:a:vd',
                            ['name=', 'age=', 'verbose', 'debug']
                        )

    name, age, verbose, debug = None, None, False, False
    for opt, arg in options:
        if opt in ('-n', '--name'):
            name = arg
        if opt in ('-a', '--age'):
            age = arg
        if opt in ('-v', '--verbose'):
            verbose = True
        if opt in ('-d', '--debug'):
            debug = True

    print('Script:', script_name)
    print('Name:', name, '\nAge:', age, '\nVerbose:', verbose, '\nDebug:', debug)

if __name__ == '__main__':
    main()
