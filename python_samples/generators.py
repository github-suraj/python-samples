def inclusive_range(*argv):
    '''Function to get generator object, including the stop number'''
    (start, step) = (0, 1)
    if len(argv) == 0:
        raise TypeError("inclusive_range expected at least 1 argument, got 0")
    elif len(argv) == 1:
        stop = argv[0]
    elif len(argv) == 2:
        (start, stop) = argv
    elif len(argv) == 3:
        (start, stop, step) = argv
    else:
        raise TypeError(f"inclusive_range expected at most 3 arguments, got {len(argv)}")

    _next = start
    while _next <= stop:
        yield _next
        _next += step
