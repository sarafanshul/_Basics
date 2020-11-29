import hashlib
import argparse
import sys ,os
import random
from cryptography.fernet import Fernet

def check(filename):
	import codecs
	try:
		f = codecs.open(filename, encoding='utf-8', errors='strict')
		for line in f:
			pass
		print( "Valid UTF-8")
	except UnicodeDecodeError:
		print( "invalid utf-8")
		exit()

def _genrate() -> str:
	key = Fernet.generate_key()
	print(key)
	with open("p.txt" , "wb") as opt:
		opt.write(key)
	return key

# rot -> md5;

def __decrypt(f:str ,o:str ,k) -> None:
	key = bytes(k ,"UTF-8")

	def decrypt(s):
		cipher_suite = Fernet(key)
		# encoded_text = cipher_suite.encrypt(s)
		decoded_text = cipher_suite.decrypt(s)
		return decoded_text

	inp = []
	with open(f ,'rb') as F:
		for l in F:
			inp.append(l)

	out = []

	for i in inp:
		out.append( decrypt(i) )

	with open(o ,"wb") as F:
		for l in out:
			F.write(l)


def __encrypt(f:str ,o:str) -> None:

	check(f)

	key = _genrate()
	def encrypt(s):
		cipher_suite = Fernet(key)
		encoded_text = cipher_suite.encrypt(s)
		# decoded_text = cipher_suite.decrypt(encoded_text)
		return encoded_text

	inp = []
	with open(f ,'r') as F:
		for l in F:
			inp.append( bytes( l ,"UTF-8" ) )

	out = []
	for i in inp:
		out.append( encrypt( i ) )

	# writes utf - 8 
	with open(o ,"wb") as F:
		for b in out :
			F.write(b)
			F.write(b"\n")


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t' ,
		type = int ,
		default = 0 ,
		help = 'Encrypt:0 / Decrypt:1')
	parser.add_argument('--same' ,
		type = str ,
		default = None ,
		help = 'File to Encrytp')
	parser.add_argument('-e' ,
		type = str ,
		default = '1.txt' ,
		help = 'File to Encrytp')
	parser.add_argument('-d' ,
		type = str ,
		default = '1.txt' ,
		help = 'File to Decrypt')
	parser.add_argument('-o' ,
		type = str ,
		default = 'a.out' ,
		help = 'where to store')
	parser.add_argument('-k' ,
		type = str ,
		default = None ,
		help = 'key')
	args = parser.parse_args()

	if(args.same != None):
		if(not bool(args.t)):__encrypt(args.same ,args.same)
		else :__decrypt(args.same ,args.same ,args.k)
	else :
		if(not bool(args.t)):__encrypt(args.e ,args.o)
		else : __decrypt(args.d ,args.o ,args.k)

if __name__ == '__main__':
	print("NOTE - THIS WORKS FOR  UTF-8 ONLY")
	main()