
# This processes can be seen in Task amnager under Powershell or Python Promt

from multiprocessing import Process , current_process
import os , time
def square(numbers):
    time.sleep(20)
    print([number*number for number  in numbers][-1])#for last iterable

if __name__ == '__main__':    
    processes = []
    numbers = list(range(100))
    print()
    for _ in range(30):
        process = Process(target = square , args=(numbers ,))
        processes.append(process) 
        process.start()
        '''if we use sleep here it works fine but if we use 
        in function it does not because due to multi threading 
        function gets executed on different threads 
        at a same time and only ony sleeptime is seen'''
        # time.sleep(0.2)
    
    for proc in processes:
        proc.join()
    # this only executes next command when 
    # all previous processes are completed
    
    print('Multiprocessing Complete')