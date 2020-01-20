# write output in same place on the console

import sys
import time

for i in range(100):
	# print(i , flush= True)
	# sys.stdout.write(f'{i}')
	# sys.stdout.flush()
	time.sleep(0.1+(i*10)//1000)  # for time constraints
	# print('Downloading [%d%%]\r'%i, end="")
	print(f'testing [{i}%]\r', end='')
