class Tee:
    '''
        Class to create log file as well as print in terminal
        Usage:
            stdout_init = sys.stdout
            logfile = open(logfile_path, 'w')
            sys.stdout = Tee(sys.stdout, logfile)
            sys.stdout = stdout_init
    '''
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()
