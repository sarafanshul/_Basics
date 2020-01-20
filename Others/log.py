import logging,sys
logger= logging.getLogger(__name__)

f_handler = logging.FileHandler('1.txt','w')
logger.addHandler(f_handler)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
f_handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 20
num_2 = 10
logger.debug('{}+{}={}'.format(num_1,num_2,add(num_1,num_2)))
logger.debug('{}-{}={}'.format(num_1,num_2,subtract(num_1,num_2)))
logger.debug('{}*{}={}'.format(num_1,num_2,multiply(num_1,num_2)))
logger.debug('{}/{}={}'.format(num_1,num_2,divide(num_1,num_2)))
