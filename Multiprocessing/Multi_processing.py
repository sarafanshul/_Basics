#MULTIPROCESSING LOCK
import time
import multiprocessing
def deposit(balence , lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balence.value = balence.value + 1
        lock.release()

def withdraw(balence , lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balence.value = balence.value - 1
        lock.release()

if __name__=="__main__":
    balence = multiprocessing.Value('i',200)

    lock = multiprocessing.Lock()

    d = multiprocessing.Process(target = deposit,args = (balence,lock))
    w = multiprocessing.Process(target=withdraw , args=(balence ,lock))

    d.start()
    w.start()
    d.join()
    w.join()
    print(balence.value)