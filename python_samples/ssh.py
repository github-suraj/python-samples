from paramiko import SSHClient, AutoAddPolicy

class Ssh:
    '''Class to create connection with some other machine'''
    def __init__(self, server):
        self.server = server

    def connect(self, retcode=0):
        try:
            self.client = SSHClient()
            self.client.set_missing_host_key_policy(AutoAddPolicy())
            self.client.connect(self.server, gss_auth=True)
            print(f"INFO: Successfully established SSH Connection for server {self.server}")
        except Exception as err:
            print(f"ERROR: {err.__class__.__name__} - Failed to establish SSH Connection for server {self.server} as {err}")
            retcode = 1
        return retcode

    def exec_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        retcode = stdout.channel.recv_exit_status()
        if retcode == 0:
            for line in stdout.readlines():
                print('INFO:',line.rstrip())
        else:
            for line in stderr.readlines():
                print('EORROR:', line.rstrip())
        return retcode
