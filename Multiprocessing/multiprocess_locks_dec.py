import time
from multiprocessing import Process , Lock , Value

def loc_dec_parent(*args , **kwargs):
	
	def lock_dec(func):
		
		def wrapper(*args , **kwargs):
			# lock = Lock()
			kwargs['lock'].acquire()
			func(*args)
			kwargs['lock'].release()
			print('dec executed')
		return wrapper
	return lock_dec	

# ---------------this works fine with no errors---------------------
# def add_no_lock(total):
# 	lock.acquire()
# 	for i in range(100):
# 		time.sleep(0.01)
# 		total.value += 5
# 	lock.release()
#-------------------------------------------------------------------

# @lock_dec(lock = Lock()) # with decorator errors
@loc_dec_parent(lock = Lock())
def add_no_lock(total):
	for i in range(100):
		time.sleep(0.01)
		total.value += 5

# @lock_dec
# def sub_no_lock(total):
# 	for i in range(100):
# 		time.sleep(0.01)
# 		total.value -= 5


# if __name__ =='__main__':
	
# 	total = Value( 'i' , 500)

# 	add_process = Process(target = add_no_lock , args = (total , ))
# 	# sub_process = Process(target = sub_no_lock , args = (total , ))

# 	add_process.start()
# 	# sub_process.start()

# 	# add_process.join()
# 	# sub_process.join()

# 	print(total.value)

# # # Idealy lock needs to be passed as an argument to the function
try:
	if __name__ =='__main__':
	
		total = Value( 'i' , 500)

		add_process = Process(target = add_no_lock , args = (total , ))
		# sub_process = Process(target = sub_no_lock , args = (total , ))

		add_process.start()
		# sub_process.start()

		# add_process.join()
		# sub_process.join()

		print(total.value)

# # Idealy lock needs to be passed as an argument to the function
except:
	pass
