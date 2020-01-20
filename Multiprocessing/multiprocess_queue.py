# # Making use of Multiprocessing Queue Class 
# # to communicate between Processes
from multiprocessing import ( Process , Queue ,
							 log_to_stderr , get_logger )

import logging

def square(numbers , queue):
	for i in numbers:
		queue.put(i*i)

def cube(numbers , queue):
	for i in numbers:
		queue.put(i*i*i)

if __name__ == '__main__':

	# log_to_stderr()
	# logger = get_logger()
	# logger.setLevel(logging.DEBUG)	

	numbers = list(range(10))
	queue = Queue()

	square_process = Process(target = square , args = (numbers , queue))
	cube_process = Process(target = cube , args = (numbers , queue))

	square_process.start()
	cube_process.start()

	square_process.join()
	cube_process.join()

	while not queue.empty():
		print(queue.get())

	# print('Completed')