# creating a custom context managers
# using a class based method

import time

class Open_File(object):
    '''
        custom context manager for file handling
    '''

    def __init__(self , filename , mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename , self.mode)
        return self.file

    def __exit__(self , exc_type , exc_val , traceback):
        self.file.close()

if __name__ == "__main__":

    with Open_File('test_contextManager.txt' , 'w+') as tst:
        tst.write(time.time())
    
    print(tst.closed) # for checking if it is closed or NOT