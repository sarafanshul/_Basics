'''
What is "argparse"

	The argparse module makes it easy to write 
	user-friendly command-line interfaces. 
	The program defines what arguments it requires, 
	and argparse will figure out how to parse those 
	out of sys.argv. 
	The argparse module also 
	automatically generates help and usage messages 
	and issues errors when users give the 
	program invalid arguments.
'''

'''
Points
# <type> = <class 'argparse.Namespace'>
# .__dict__ = {'x': 1, 'y': 2}
--- # use sys.stdout for buffer issues
--- # args.__dict__ for help with object attributes
--- # print works too but buffer issues "?"
'''

'''
creating objects
parser = argparse.ArgumentParser(prog=None, usage=None, 
						description=None, epilog=None, 
						parents=[], formatter_class=argparse.HelpFormatter, 
						prefix_chars='-', fromfile_prefix_chars=None, 
						argument_default=None, conflict_handler='error', 
						add_help=True, allow_abbrev=True)

# parser = argparse.ArgumentParser() # will also work LOL

ArgumentParser.add_argument(name or flags...[, action]
						[, nargs][, const][, default][, type]
						[, choices][, required][, help][, metavar]
						[, dest])  
'''
'''
usage: argparse_1.py [-h] [--x X] [--y Y] [--op OP]

optional arguments:
  -h, --help  show this help message and exit
  --x X       First Number here
  --y Y       Second Number here
  --op OP     Type of operation
'''
# example

import argparse
import sys

def calculate(args:object) -> int:
	if args.op == 'add': 
		return args.x + args.y
	elif args.op == 'sub': 
		return args.x - args.y
	elif args.op == 'div': 
		return args.x // args.y
	elif args.op == 'mul': 
		return args.x * args.y

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--x' , 
		type = int ,
		default = 1 ,
		help = 'First Number here')

	parser.add_argument('--y' ,
		type = int ,
		default = 1 ,
		help = 'Second Number here')

	parser.add_argument('--op' ,
		type = str ,
		default = 'add' ,
		help = 'Type of operation')

	args = parser.parse_args()
	# sys.stdout.write(str(type(args))) # use sys.stdout for buffer issues
	# print(args.__dict__)
	sys.stdout.write(str(calculate(args)))

if __name__ == '__main__':
	main()