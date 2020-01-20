# this is WORKING------HURRAH!!!!---
import time,logging
from multiprocessing import ( Process , Lock ,
							 Value ,log_to_stderr , get_logger) 

from functools import wraps
# # # Idealy lock needs to be passed as an argument to the function
def loc_dec_parent(*args , **kwargs):
	def lock_dec(func):
		@wraps(func)	
		def wrapper(*arg , **kwarg):
			kwargs['lock'].acquire()
			func(*arg)
			kwargs['lock'].release()
		return wrapper
	return lock_dec	


@loc_dec_parent(lock = Lock())
def add_no_lock(total):
	for i in range(100):
		time.sleep(0.01)
		total.value += 5

@loc_dec_parent(lock = Lock())
def sub_no_lock(total):
	for i in range(100):
		time.sleep(0.01)
		total.value -= 5


total = Value( 'i' , 500)
try:
	if __name__ =='__main__':
		
		log_to_stderr()
		logger = get_logger()
		logger.setLevel(logging.INFO)

		add_process = Process(target = add_no_lock , args = (total , ))
		sub_process = Process(target = sub_no_lock , args = (total , ))

		add_process.start()
		sub_process.start()

		add_process.join()
		sub_process.join()
		print(total.value)
except:
	pass

