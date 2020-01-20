
#____________________NOT WORKING_________

import re
from pprint import pprint

#pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]')
#pattern = re.compile(r'Dave')
#pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{3,4}')
with open(r'C:\Users\win10\PycharmProjects\untitled\venv\data_TXT\info.txt','r') as info:
    content = info.read()
    pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{3,4}')
    matches = pattern.finditer(content)
    #pprint(list(matches))
    for match in matches:
        print(match)
