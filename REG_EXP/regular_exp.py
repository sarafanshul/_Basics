import re,pprint
text ='''
is a multilingual online encyclopedia, based on open collaboration through a wiki-based content editing system.
 It is the largest and most popular general reference work on the World Wide Web,[3][4][5] and is one of the
 most popular websites ranked by Alexa as of June 2019.[6] It features exclusively free content and no 
commercial ads, and is owned and supported by the Wikimedia Foundation, a non-profit organization funded 
primarily through donations'''

sentence='''
Python is an interpreted, high-level, general-purpose programming language.Created by Guido van Rossum and first
released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant 
whitespace. Its language constructs and object-oriented approach aims to help programmers write clear, logical code for
small and large-scale projects.[27]Python is dynamically typed and garbage-collected. It supports multiple programming 
paradigms, including procedural, object-oriented, and functional programming. Python is often described as a 
"batteries included" language due to its comprehensive standard library.[28]'''


#pattern = re.compile(r'anshul') #4 in 1.txt
#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
#pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}') # using Quantifiers
pattern = re.compile(r'df')
#pattern = re.compile(r'^START') # matches LITRALLY at the begnning of text


#matches = pattern.finditer(text)
#pprint.pprint(list(matches))

with open('1.txt','r') as f1:
    contents = f1.read()
    matches = pattern.finditer(contents)
    pprint.pprint(list(matches))
#print(text[1:10]) #returns first 10 characters
