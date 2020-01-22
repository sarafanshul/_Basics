# for cli
'''
>>> import fputs
>>> fputs.__doc__
'Python interface for the fputs C library function'
>>> fputs.__name__
'fputs'
>>> # Write to an empty file named `write.txt`
>>> fputs.fputs("it WORKS?", "write.txt")
>>> with open("write.txt", "r") as f:
>>>     print(f.read())
'''
import fputs
fputs.fputs('Anshul Saraf' , 'test.txt') # welll it works

