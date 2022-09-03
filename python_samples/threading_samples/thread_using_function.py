'''
    Module file for Threading Sample using function
'''

from threading import Thread, current_thread, main_thread
from time import sleep

def greet(msg, num, wait=2):
    '''
        Function to run in threads
    '''
    for i in range(num):
        print(current_thread().name, i+1 ,msg)
        sleep(wait)
    print('End Of Thread', current_thread().name)


def main():
    '''
        Runner Function for creating threads
    '''
    greets = [
        ('Hi All!', 4, 0.03),
        ('Hello World!', 3, 0.01),
        ('Hey, How are you?', 5, 0.05)
    ]
    threads = []

    for msg, num, wait in greets:
        _thread = Thread(
                name=f'Thread-{msg.split()[0]}',
                target=greet,
                args=(msg, num),
                kwargs={'wait': wait}
            )
        threads.append(_thread)
        _thread.start()

    for _thread in threads:
        _thread.join()

    print('\nProgram ::', main_thread().name, ':: Completed')


if __name__ == '__main__':
    main()
