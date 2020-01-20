# One can create a pool of processes which will carry out tasks submitted to
# it with the Pool class.

# A process pool object which controls a pool of worker processes to which
# jobs can be submitted. It supports asynchronous results with timeouts and
# callbacks and has a parallel map implementation.

import time
from multiprocessing import Pool

def sum_square(num):
	s=0
	# for i in range(1000):
	for i in range(10):
		s += i*i
	return s
	

if __name__ == '__main__':
 	# Pool takes all the cpu(s). 
 	# ie,it defaults to cpu-count to max-cpu-count 
 	start = time.time()
 	# p = Pool(processes = 2)
 	
 	p = Pool()
 	results = p.map(sum_square , list(range(100))) 
 	p.close()
 	# print(f'(Pool) for all cores (4)- iterations = {len(results)*1000}, \n time taken = {time.time() - start}')
 	
 	p.join()
 	# # print(len(results))
 	# star = time.time()
 	# res = []
 	# for j in range(100000):
 	# 	res.append(sum_square(j))
 	# print(f'for default core (1)- iterations = {len(res)*1000}, \n time taken = {time.time() - star}' ) 

''' results = 
(Pool) for all cores (4)- iterations = 100000000,
 time taken = 6.873302221298218
for default core (1)- iterations = 100000000,
 time taken = 37.51958703994751'''