from multiprocessing import Process , current_process
import os
def square(number):
	# we can print out PROCESS ID by using os module , ID assigned to the call  
	# of this function  assigned by operating system > "os.getpid" method
    # print(f'process Id = {os.getpid()}')
    
    # we can also use current process to get the name to the current process.
    # current_process().name method
    print(f'process Id = {current_process().name}')
    print(f'the square of {number} is {number*number}')

if __name__ == '__main__':    
    processes = []
    numbers = [1,2,3,4]
    print()
    for number in numbers:
		# initializing a process object
        process = Process(target = square , args=(number ,))
        processes.append(process) 
        process.start()
		# processes are spawned/created by 'Process object' and 
		# we call it using '.start' method.
		