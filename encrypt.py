from Crypto.Cipher import AES    
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
import argparse
import sys ,os
import random

password = ("anything")

def __out(ret:list , o:str ,typ:str) -> None:
	with open(o , typ) as opt: opt.write(ret)

def _genrate() -> str:
	password = "".join([str(random.randint(0 ,9)) for _ in range(100)])
	__out(password ,"p.txt" ,'w')
	return password

def enc(r:str) -> str:
	global password
	password = _genrate()
	hash_obj = SHA256.new(password.encode('utf-8'))    
	hkey = hash_obj.digest()
	def encUtil(info):
		msg = info
		BLOCK_SIZE = 16
		PAD = "{"
		padding = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PAD
		cipher = AES.new(hkey, AES.MODE_ECB)
		result = cipher.encrypt(padding(msg).encode('utf-8'))
		return result
	return encUtil(r)

def dec(a:list) -> str:
	global password
	hash_obj = SHA256.new(password.encode('utf-8'))    
	hkey = hash_obj.digest()
	def decUtil(info):
		msg = info
		PAD = "{"
		decipher = AES.new(hkey, AES.MODE_ECB)
		pt = decipher.decrypt(msg).decode('utf-8')
		pad_index = pt.find(PAD)
		result = pt[: pad_index]
		return result
	return decUtil(a)

def __decrypt(f:str ,o:str ,k) -> None:
	global password
	password = k
	with open(f ,'rb') as fi:
		ret = fi.read()
	__out(dec(ret) ,o ,'w')

def __encrypt(f:str ,o:str) -> None:
	ret = ""
	with open(f ,'r') as fi:
		for i in fi:ret+=(i.strip())+"\n"
	__out(enc(ret) ,o ,'wb')
	print(password)

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

	# args.k = args.k.strip()
	if(args.same != None):
		if(not bool(args.t)):__encrypt(args.same ,args.same)
		else :__decrypt(args.same ,args.same ,args.k)
	else :
		if(not bool(args.t)):__encrypt(args.e ,args.o)
		else : __decrypt(args.d ,args.o ,args.k)

if __name__ == '__main__':
	main()