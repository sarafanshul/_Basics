# A lock or mutex is a sychronization mechanism for enforcing
# limits on access to a resource in an environment where there
# are many threads of execution.

import time
from multiprocessing import Process , Lock , Value


def lock_dec(func):
	lock = Lock()
	def wrapper(*args , **kwargs):
		lock.acquire()
		func(args)
		lock.release()

	return wrapper


# def add_no_mp(total):
# 	for i in range(100):
# 		time.sleep(0.01)
# 		total += 5
# 	return total

# def sub_no_mp(total):
# 	for i in range(100):
# 		time.sleep(0.01)
# 		total -= 5
# 	return total

# ---------------this works fine with no errors---------------------
# def add_no_lock(total):
# 	lock.acquire()
# 	for i in range(100):
# 		time.sleep(0.01)
# 		total.value += 5
# 	lock.release()
#-------------------------------------------------------------------

@lock_dec # with decorator errors
def add_no_lock(total):
	for i in range(100):
		time.sleep(0.01)
		total.value += 5
# no return because we are modifiying a Shared Variable

# @lock_dec
# def sub_no_lock(total):
# 	for i in range(100):
# 		time.sleep(0.01)
# 		total.value -= 5

# def add_lock(total):
# 	for i in range(100):
# 		time.sleep(0.01)
# 		lock.acquire()
# 		total.value += 5
# 		lock.release()
# # no return because we are modifiying a Shared Variable

# def sub_lock(total):
# 	for i in range(100):
# 		time.sleep(0.01)
# 		lock.acquire()
# 		total.value -= 5
# 		lock.release()

if __name__ =='__main__':
	# total = 500
	total = Value( 'i' , 500)
	# print(total)
	# total = add_no_mp(total)
	# print(total)
	# total = sub_no_mp(total)
	# print(total)


	add_process = Process(target = add_no_lock , args = (total , ))
	# sub_process = Process(target = sub_no_lock , args = (total , ))
	# add_process = Process(target = add_lock , args = (total , ))
	# sub_process = Process(target = sub_lock , args = (total , ))

	add_process.start()
	# sub_process.start()

	add_process.join()
	# sub_process.join()

	print(total.value)

# # Idealy lock needs to be passed as an argument to the function