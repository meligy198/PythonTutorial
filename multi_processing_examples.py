from multiprocessing import Process, Value, Array, Lock, Queue #to share data between processes and prevent race conditions
from multiprocessing import Pool
import os
import time


def add_100(number, lock):
    for i in range(100):
        with lock:
            number.value += 1
        #processing
        time.sleep(0.01)

def add_100_array(array, lock):
    for j in range(100):
        for i in range(len(array)):
            lock.acquire()
            array[i] += 1
            lock.release()

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)
    
def make_negative(numbers, queue):
    for i in numbers:
        queue.put(i*-1)

def cube(number):
    return number*number*number

if __name__ == "__main__":
    lock = Lock()
    shared_number = Value('i', 0) #integer type, staring value
    shared_array = Array('d', [0.0, 100.0, 200.0]) #double type, starting values
    print(f'Number at beginning is {shared_number.value}')
    print(f'Array at beginning is {shared_array[:]}')

    process1 = Process(target=add_100, args=(shared_number, lock))
    process2 = Process(target=add_100, args=(shared_number, lock))
    process3 = Process(target=add_100_array, args=(shared_array, lock))
    process4 = Process(target=add_100_array, args=(shared_array, lock))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print(f'Number at end is {shared_number.value}')
    print(f'Array at end is {shared_array[:]}')

    #using Queues
    q = Queue()
    numbers = range(1, 6)
    process5 = Process(target=square, args=(numbers, q))
    process6 = Process(target=make_negative, args=(numbers, q))

    process5.start()
    process6.start()

    process5.join()
    process6.join()

    while not q.empty():
        print(q.get()) #returns and removes the first element in the queue

    #process pools object controls a pool of worker processes to which chops can be submitted
    #an manages the available processes and can split data in parallel chunks
    pool = Pool()
    #there are 4 important methods: map, apply, join, close
    numbers = range(10)
    result = pool.map(cube, numbers) #automatically allocate the max number of avaiable processes and split this iterable into equal sized chunks and execute it in parallel
    result = pool.apply(cube, numbers[1]) #to process 1 value of the array
    pool.close()
    pool.join() #wait for pool to process all applications
    print(result)

