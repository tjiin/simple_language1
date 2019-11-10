from lexer import lexer
from parser33 import Compile
import sys
import os


def interpret(code):
	return Compile(code)


def main():
	n = len(sys.argv)
	a = sys.argv[1]
	if n > 1:
		if os.path.exists(a): 
			with open(a, 'r') as f: code = f.read()
		else: 
			code = sys.argv[1]
		try:
			print(interpret(code))
		except Exception as e:
			print(e)
			if n == 3 and sys.argv[2] == 'a':
				for t in lexer.lex(code): 
					print(t)
			print('\n')


if __name__ == '__main__':
	main()
