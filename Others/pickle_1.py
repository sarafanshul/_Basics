'''
------------------------PICKLE----------------------
The pickle module implements binary protocols for serializing 
and de-serializing a Python object structure. 
“Pickling” is the process whereby a Python object hierarchy 
is converted into a byte stream, and “unpickling” is the 
inverse operation, whereby a byte stream (from a binary file or 
bytes-like object) is converted back into an object hierarchy. 
Pickling (and unpickling) is alternatively known as “serialization”,
 “marshalling,” 1 or “flattening”; however, to avoid confusion, 
the terms used here are “pickling” and “unpickling”. 
'''

import pickle

data = {1:list(range(100)) , 2:list(range(100 , -1 ,-1)) , 'a':'SERILIAZING'}
# ----------------Serializing Data------------------------

with open('test.pkl' , 'wb') as file:
	pickle.dump( data , file)

# --------------------Protocols-------------------

# pickle.dump( data , file , protocol = pickle.HIGHEST_PROTOCOL)
# >>>
# highest protocol - i.e. V-4 Protocol(GENERALLY FOR LARGE AMOUNTS OF DATA)
# default protocol = V-3 Protocol

# -------------------Deseriliazing Data-------------------

with open('test.pkl' , 'wb') as file:
	data1 = pickle.load(file)

# --------------Outputs Comparision-----------------
'''
>>> type(data)
<class 'dict'>
type(data[1])
<class 'list'>
>>> type(data[1][2])
<class 'int'>
>>> type(type(data[1][2]))
<class 'type'>
>>>

>>> type(data1)
<class 'dict'>
type(data1[1])
<class 'list'>
>>> type(data1[1][2])
<class 'int'>
>>> type(type(data1[1][2]))
<class 'type'>
>>>

'''