class inclusive_range(object):
    '''Class to get iterator object, including the stop number'''
    def __init__(self, *argv):
        (self._start, self._step) = (0, 1)
        if len(argv) == 0:
            raise TypeError("inclusive_range expected at least 1 argument, got 0")
        elif len(argv) == 1:
            self._stop = argv[0]
        elif len(argv) == 2:
            (self._start, self._stop) = argv
        elif len(argv) == 3:
            (self._start, self._stop, self._step) = argv
        else:
            raise TypeError(f"inclusive_range expected at most 3 arguments, got {len(argv)}")
        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        rval = self._next
        self._next += self._step
        return rval
