'''
    Module file for Threading Sample with Queue
'''

import threading
import queue

def worker():
    '''
        Worker Function to do something for an item
    '''
    while True:
        item = _queue.get()
        print(f'Working on item: {item}')
        print(f'Finished item: {item}')
        _queue.task_done()


def main():
    '''
        Runner Function for creating queue
    '''
    # turn-on the worker thread
    threading.Thread(target=worker, daemon=True).start()

    # send thirty task requests to the worker
    for item in range(6):
        _queue.put(item)
    print('All task requests sent\n', end='')

    # block until all tasks are done
    _queue.join()
    print('All work completed')


if __name__ == '__main__':
    _queue = queue.Queue(maxsize=3)
    main()
