# # ---------------- super() --------------------
# # # --------------- BASICS ---------------------

'''
The super() builtin returns a proxy object 
that allows you to refer parent class by 'super'.

>>> super (type[, object-or-type])

super() is useful for accessing inherited methods 
that have been overridden in a class. The search order is same as 
that used by getattr() except that the type itself is skipped.

The __mro__ attribute of the type lists the method resolution 
search order used by both getattr() and super(). 
The attribute is dynamic and can change whenever the inheritance 
hierarchy is updated.
'''


# class Base(object):
# 	"""docstring for Base"""
# 	def __init__(self):
# 		print(f'{Base.__name__} class Evoked for {self}')

# class Child1(Base):
# 	"""docstring for Child1"""
# 	def __init__(self):
# 		Base.__init__(self)
# 		print(f'{Child1.__name__} class Evoked for {self}')

# class Child2(Base):
# 	"""docstring for Child2"""
# 	def __init__(self):
# 		Base.__init__(self)
# 		print(f'{Child2.__name__} class Evoked for {self}')


# class Child3(Child1 , Child2):
# 	"""docstring for Child3"""
# 	def __init__(self):
# 		Child1.__init__(self)
# 		Child2.__init__(self)
# 		print(f'{Child3.__name__} class Evoked for {self}')
# c = Child3()

# b = Base()

# # --------- output here is repeated----------

'''
**** here Base class is called twice ****

PS E:\Py\Basics> python super.py
Base class Evoked for <__main__.Child3 object at 0x00EAEE90>
Child1 class Evoked for <__main__.Child3 object at 0x00EAEE90>
Base class Evoked for <__main__.Child3 object at 0x00EAEE90>
Child2 class Evoked for <__main__.Child3 object at 0x00EAEE90>
Child3 class Evoked for <__main__.Child3 object at 0x00EAEE90>
--------
To avoid this situation super() is used
code is given bellow
'''

# class Base(object):
# 	"""docstring for Base"""
# 	def __init__(self):
# 		print(f'{Base.__name__} class Evoked for {self}')

# class Child1(Base):
# 	"""docstring for Child1"""
# 	def __init__(self):
# 		super().__init__()
# 		print(f'{Child1.__name__} class Evoked for {self}')

# class Child2(Base):
# 	"""docstring for Child2"""
# 	def __init__(self):
# 		super().__init__()
# 		print(f'{Child2.__name__} class Evoked for {self}')


# class Child3(Child1 , Child2):
# 	"""docstring for Child3"""
# 	def __init__(self):
# 		super().__init__()
# 		print(f'{Child3.__name__} class Evoked for {self}')


# c = Child3()
# print(Child3.__mro__)

''' ------ OUTPUT--------
PS E:\Py\Basics> python super.py
Base class Evoked for <__main__.Child3 object at 0x02C7EB90>
Child2 class Evoked for <__main__.Child3 object at 0x02C7EB90>
Child1 class Evoked for <__main__.Child3 object at 0x02C7EB90>
Child3 class Evoked for <__main__.Child3 object at 0x02C7EB90>
(<class '__main__.Child3'>, <class '__main__.Child1'>, <class '__main__.Child2'>, <class '__main__.Base'>, <class 'object'>)
'''



# # ------super() in a class with no DIRECT parent-------

# class Ten(object):
# 	"""docstring for Ten"""
# 	def adder(self , *args):
# 		print(sum(args)+10)
# 		super().adder()

# class Hundred(object):
# 	"""docstring for Hundrea"""
# 	def adder(self , *args):
# 		print(sum(args)+100)
		

# class Expirement(Ten , Hundred):
# 	pass

# e = Expirement()
# e.adder(1 , 2 , 3 , 4 , 5)
# print(Expirement.__mro__)


'''
output ** WITHOUT super() in first adder()

== here due to inheritance only Ten's Adder() in hit==

PS E:\Py\Basics> python super.py
25
(<class '__main__.Expirement'>, <class '__main__.Ten'>,
 <class '__main__.Hundred'>, <class 'object'>)
'''


'''
output ** WITH super() in first adder()

== here due to inheritance only Ten's Adder() in hit BUT
wiht super Hundreds's adder() also ran==

PS E:\Py\Basics> python super.py
PS E:\Py\Basics> python super.py
25
100
(<class '__main__.Expirement'>, <class '__main__.Ten'>, 
<class '__main__.Hundred'>, <class 'object'>)
'''
	