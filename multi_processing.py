from multiprocessing import Process
import os


def square_numbers():
    for i in range(1000):
        result = i * i


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count() #to find the number of CPUs in my computer

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers) #the target is a function executed by the process
        #process = Process(target=square_numbers, args=(tuple with args)) #If function requires arguments
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        process.join()

    print('all processes are done')