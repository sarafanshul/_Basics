import logging,log
logger= logging.getLogger(__name__)

f_handler = logging.FileHandler('2.txt','w')
logger.addHandler(f_handler)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
f_handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)

class Employee:

    num_e=0
    raise_amt = 1.4
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        Employee.num_e += 1
        logger.debug('Employee Added : {} ; {}'.format(self.fullname(),self.email))

    def fullname (self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int( self.pay * self.raise_amt)
        return self.pay
e_1=Employee('Anshul','saraf',600000)
e_2=Employee('tom','hanks',700000)
e_3=Employee('tom','holland',500000)
e_4=Employee('peter','hanks',650000)