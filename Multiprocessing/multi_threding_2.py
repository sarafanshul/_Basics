import time,threading

def square(arr):
    print('square function executed')
    for a in arr:
        print('square is : ',a**2)
        time.sleep(0.2)


def cube(arr):
    print('cube function executed')
    for a in arr:
        print('cube is : ',a**3)
        time.sleep(0.2)

a=[2,3,8,9]
s=time.time()


#initializing A THREAD
t1=threading.Thread(target=square,args=(a,))
t2=threading.Thread(target=cube,args=(a,))

t1.start()
t2.start()

t1.join()
t2.join()

print("time elapssed = {}".format(time.time()-s))
print("COMPLETED")