import shlex
import subprocess

def _subprocess(command):
    '''Function to run system command (CMD/SHELL)'''
    try:
        ps = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, shell=False)
        out, err = ps.communicate()
        out = out.strip().decode("utf-8") if isinstance(out, bytes) else out
        err = err.strip().decode("utf-8") if isinstance(err, bytes) else err
        retcode = ps.returncode
    except Exception as error:
        out = f"Command {command} failure"
        err = str(error)
        retcode = 1
    return out, err, retcode
