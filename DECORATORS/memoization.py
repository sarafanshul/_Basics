class Memoization(object):
    def __init__(self,func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        ret = self.func(*args)
        self.cache[args] = ret
        return ret

@Memoization
def fib(n):
    if n < 2 :
        return 1
    return fib(n-1) + fib(n-2)

@Memoization
def fact(f,*args,**kwargs):
    if f==0:
        return 1
    return f*fact(f-1)

#print(fact(100))