'''
    Module file for Threading Sample using class
'''

from threading import Thread, current_thread, main_thread
from time import sleep

class Greet(Thread):
    '''
        Class to run in threads
    '''
    def __init__(self, msg, num, wait):
        Thread.__init__(self)
        self.msg = msg
        self.num = num
        self.wait = wait

    def run(self):
        for i in range(self.num):
            print(current_thread().name, i+1 ,self.msg)
            sleep(self.wait)
        print('End Of Thread', current_thread().name)


def main():
    '''
        Runner Function for creating threads
    '''
    greets = [
        ('Hi', 4, 0.03),
        ('Hello', 3, 0.01),
        ('Hey', 5, 0.05)
    ]
    threads = []

    for msg, num, wait in greets:
        _thread = Greet(msg, num, wait)
        threads.append(_thread)
        _thread.start()

    for _thread in threads:
        _thread.join()

    print('\nProgram ::', main_thread().name, ':: Completed')


if __name__ == '__main__':
    main()
