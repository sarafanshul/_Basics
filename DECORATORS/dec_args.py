import functools
def prefix_Time(argument):
    def tim_e(func):
        import time
        @functools.wraps(func)
        def wrapper(*args):
            print('prefix_Time function passed {}'.format(argument))
            s=time.time()
            res=func(*args)
            print('{} Returned {}\r\n in time : {} ms'.format(func.__name__,res,(time.time()-s)*1000))
            return res
        return wrapper
    return tim_e

import logging
logging.basicConfig(filename='1.txt',level=logging.DEBUG)
def prefix_Log(argument):
    def log(func):
        @functools.wraps(func)
        def wrapper(*args):
            print('prefix_Log function passed {}'.format(argument))
            res=func(*args)
            logging.debug('{} returned {}\r\n'.format(func.__name__,res))
            return res
        return wrapper
    return log

@prefix_Log('Log')
@prefix_Time('TIME:')
def arms(n):
    logging.info('Value Entered : {}'.format(n))
    x=n
    count=0
    arr=[]
    while x > 0:
        a = x % 10
        arr.append(a)
        x = x//10
        count +=1
    asum=0
    for i in arr:
        asum+= (i**count)
    if asum ==n or n==0 :
        return True
    return False
if __name__=="__main__":
    try:
        n=int(input('Enter the Value to Check : '))
        arms(n)
    except ValueError:
        logging.critical('Enter only INTEGERS')
    except NameError:
        logging.critical('Enter only INTEGERS')