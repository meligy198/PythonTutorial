#Note: The following example usually won't benefit from multiple threads since it is CPU-bound. It should just show the example of how to use threads.
from threading import Thread
import time

database_value = 0

def increase():
    global database_value
    # dummy code, get database_value and make a local copy
    local_copy = database_value
    # processing that take time
    local_copy += 1
    time.sleep(0.5)
    # copy the value back to the database
    database_value = local_copy
        
if __name__ == "__main__":        
    print('start value', database_value)

    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
        
    print('end value', database_value)
#the above code causes a race condition so the end value is 1 not 2, to correct use the lock object


from threading import Thread, Lock
import time

database_value = 0

def increase(lock): #lock prevents another thread from accessing the same piece of code
    global database_value
    # dummy code, get database_value and make a local copy
    lock.acquire() #must be released so we arent stuck
    local_copy = database_value
    # processing that take time
    local_copy += 1
    time.sleep(0.5)
    # copy the value back to the database
    database_value = local_copy
    lock.release()

    #another locking method
    with lock:
        local_copy = database_value
        # processing that take time
        local_copy += 1
        time.sleep(0.1)
        # copy the value back to the database
        database_value = local_copy
        
if __name__ == "__main__":        
    print('start value', database_value)
    lock = Lock()
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
        
    print('end value', database_value)

#Queues are used for thread safe and process safe data exchanges and processing
#linear data structure that follows the FIFO
from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available

        # do stuff...
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  # dies when the main thread dies
        t.start()
    
    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')






from threading import Thread, Lock, current_thread
from queue import Queue 
import time

def worker(q):
    while True:
        value = q.get() #will block and wait until items are available
        # processing..
        print(f'in {current_thread().name} got {value}')
        q.task_done() #must be used in threading

if __name__ == "__main__":        
    q = Queue()
    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,))
        thread.deamon=True
        thread.start()

    for i in range(1,20): #filling our queue with elements
        q.put(i)

    q.join() 

    # q.put(1)
    # q.put(2)
    # q.put(3)
    # # 3 2 1 -->
    # first = q.get() #get and removes the first item, which is 1 in this case
    # #when using get method in multithreading environment use q.task_done()
    # #q.join() #blocks until all items in the queue are gotten and processed
    # print(first)
    # q.empty() #returns true if queue is empty

    print('end main')