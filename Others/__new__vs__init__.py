#Usual class declaration and instantiation
class Foo(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def bar(self):
        pass

#A class implementation with __new__ method overridden
class bar(object):
    def __new__(cls, *args, **kwargs):
        print ("Creating Instance")
        instance = super(bar, cls).__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def bar(self):
        pass


'''If __new__ return instance of  it’s own class, then the __init__ method 
    of newly created instance will be invoked with instance 
    as first (like __init__(self, [, ….]) argument following by arguments 
    passed to __new__ or call of class.

So, __init__ will called implicitly

If __new__ method return something else other than instance of class,  
    then instances __init__ method will not be invoked. 

In this case you have to call __init__ method yourself.
'''

#APPLICATIONS
#SINGELTON
class Singleton(object):
    _instance = None  # Keep instance reference

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


#Limiting total number of instances can be created using __new__Python
class LimitedInstances(object):
    _instances = []  # Keep track of instance reference
    limit = 5

    def __new__(cls, *args, **kwargs):
        if not len(cls._instances) <= cls.limit:
            raise RuntimeError, "Count not create instance. Limit %s reached" % cls.limit
        instance = object.__new__(cls, *args, **kwargs)
        cls._instances.append(instance)
        return instance

    def __del__(self):
        # Remove instance from _instances
        self._instance.remove(self)
