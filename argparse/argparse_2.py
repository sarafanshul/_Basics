'''
using mutually exclusive
:only one

usage: argparse_2.py [-h] [-v | -q] [-o] num

positional arguments:
  num            Nth fibonacci

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet
  -o, --output   output to a file
'''
'''
for add_argument we can use
	1) directly insert Argument
		parser.add_argument('num' , ...etc
	>>> python argparse_2.py 100
	
	2) adding using "-"
		parser.add_argument('-o' , ...etc
	>>> python argparse_2.py -o

	3) adding using "--"
		parser.add_argument('--output', ..etc
	>>> python argparse_2.py --output

'''
import sys
import argparse

def fibonacci(n:int) -> int:
	a ,b = 0 ,1
	for i in range(n):
		a ,b = b ,a+b 
	return a

def main()-> None:
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	
	group.add_argument('-v' ,\
		'--verbose' ,\
		action = 'store_true')

	group.add_argument('-q',\
		'--quiet',\
		action = 'store_true')

	parser.add_argument('num' ,\
		default = 1 ,\
		type = int ,\
		help = 'Nth fibonacci')

	parser.add_argument('-o' ,\
		'--output',\
		help = 'output to a file', \
		action = 'store_true')

	args = parser.parse_args()
	result = fibonacci(args.num)

	if args.verbose:
		sys.stdout.write('Nth fibonacci = '+ str(result))
	if args.quiet:
		sys.stdout.write(str(result))

	if args.output:
		with open(str(args.num)+'th fibonacci.txt' , 'w') as file:
			file.write(str(result))
	else:
		sys.stdout.write(str(result))

if __name__ == '__main__':
	main()