# As of 31-07 this is  WORKING
import time
from multiprocessing import Process , Lock , Value

# # # Idealy lock needs to be passed as an argument to the function

def add_no_lock(*args):
	args[1].acquire()
	for i in range(100):
		time.sleep(0.01)
		args[0].value += 5
	args[1].release()

def sub_no_lock(*args):
	args[1].acquire()
	for i in range(100):
		time.sleep(0.01)
		args[0].value -= 5
	args[1].release()

try:
	if __name__ =='__main__':
	
		total = Value( 'i' , 500)
		lock = Lock()
		add_process = Process(target = add_no_lock , args = (total , lock ))
		sub_process = Process(target = sub_no_lock , args = (total , lock ))

		add_process.start()
		sub_process.start()

		add_process.join()
		sub_process.join()
		print(total.value)

except:
	pass
