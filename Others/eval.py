'''
https://www.youtube.com/watch?v=1NJpqi5pqoU

The eval() method parses the expression passed 
to it and runs python expression(code) within the program.

The syntax of eval is:

>>> eval(expression, globals=None, locals=None)


>>> list_str = '[1,2,34,5,6,]'
>>> list_str_eval =eval(list_str)
>>> type(list_str)
<class 'str'>
>>> type(list_str_eval)
<class 'list'>
>>> type(list_str_eval[3])
<class 'int'>
'''
