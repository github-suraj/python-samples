'''
    Module file for Threading Sample with Pool
'''

import concurrent.futures
import time

def greet(msg, wait):
    '''
        Function to run in threads
    '''
    print(f'Start Of Thread for -> {msg}')
    for i in range(2):
        print(f'Thread {msg} -> Count {i}')
        time.sleep(wait)
    print(f'End Of Thread for -> {msg}')


def main():
    '''
        Runner Function for creating thread pool
    '''
    greets = [
        ('Hi', 0.02),
        ('Hello', 0.01),
        ('Hey', 0.03),
        ('Bye', 0.03)
    ]
    time_start = time.time()

    ## Starting Thread Pool with Max Worker 2
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for _greet in greets:
            executor.submit(greet, *_greet)
    print(f'Program Completed in {time.time() - time_start} Seconds')


if __name__ == '__main__':
    main()
