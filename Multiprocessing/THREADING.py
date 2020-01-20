from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(10):
            print('hello')
            sleep(0.5)

class hi(Thread):
    def run(self):
        for i in range(10):
            print('hi')
            sleep(0.5)

h1=hello()
h2=hi()

h1.start()
sleep(0.2)
h2.start()
#waiting for t1 and t2 to complete
h1.join()
h2.join()

print('bye')