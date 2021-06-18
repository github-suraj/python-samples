import logging

class MultilineFormatter(logging.Formatter):
    '''Class for customized logging output formatter for multiline string'''
    def format(self, record=logging.LogRecord):
        save_msg = record.msg
        msg_list = record.msg.splitlines()
        if len(msg_list) > 1:
            output = ''
            for idx, line in enumerate(msg_list):
                record.msg = line
                output += super().format(record)
                if idx < len(msg_list) - 1:
                    output += "\n"
        else:
            output = super().format(record)
        record.msg = save_msg
        return output

def setup_logging(debug=False, logfile=None, mode='w'):
    '''
        Function to setup logging
        debug=False, debug mode is off,
            Can be made on by providing debug=True while calling
        logfile=None, no file will be created,
            If need to create a log file too, logfile=<some_file_path>
            File open mode can be controlled by `mode` argument
    '''
    def set_handler(handler):
        handler.setFormatter(formatter)
        if debug:
            handler.setLevel(logging.DEBUG)
        else:
            handler.setLevel(logging.INFO)
        logger.addHandler(handler)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = MultilineFormatter(("%(asctime)s - %(levelname)s - %(message)s"))
    sh = logging.StreamHandler()
    set_handler(sh)
    if logfile:
        fh = logging.FileHandler(logfile, mode=mode)
        set_handler(fh)
