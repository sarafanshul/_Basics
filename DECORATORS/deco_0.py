import time,functools
def time_func(func):
    @functools.wraps(func)
    def inner(*args):
        s=time.time()
        r=func(*args)
        result=print('{} ran in {} milisec '.format(func.__name__, (time.time()-s)*1000))
        return result
    return inner

def log(func):
    import logging
    logging.basicConfig(level=logging.DEBUG
                        ,format=('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))

    @functools.wraps(func)
    def inner(*args):
        logging.debug('{} ran with output {}'.format(func.__name__ ,func(*args)))
    return inner

#@functools.lru_cache(maxsize=1000)
def fib(a):
    if a==1 or a==2:
        return 1
    if a>2:
        return fib(a-1) + fib(a-2)

if __name__=='__main__':
    r=time_func(log(fib))
    #r=log(time_func(fib))
    r(30)
#functools.lru_cache is DISABLED for BETTER working



























