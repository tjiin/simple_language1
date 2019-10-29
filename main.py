from lexer import lexer
from parser1 import parser
from pprint import *
from ast import data_dict

"""
TODO: Implicit multiplication kind of works but '(1) (2)' would be incorrectly parsed as multiplying...
"""


def f(code):
    return parser.parse(lexer.lex(code)).eval()


def gen_tokens(code):
    return lexer.lex(code)


def main():
    statements = ['-1+1','-0.1+1','-0-1.0','-1.2*(0.001)/(-4-1)','1+1000.0/2',
                  '2.45*(1-0.89)/(4-1)*((7.1))*(((-1)))',
                  '(-1)*(-1 )/( 1 - 1*(-1))', '2(5+1)', '(3-7)2',
                  '(-5)(-5)', '(1)*(2)/(3)', '2(9)',
                   'let x = 10', 'x+1', 'let x = 2*532']



    # BREAKING CASES: '((-4/2)(2)(-100))+1', '(-4/2)(2)(100)+1

    for i,x in enumerate(statements):
        print(x, '=', f(x))
        for y in gen_tokens(x):
            print(y)
        pprint(data_dict)
    print('Finished')



if __name__ == '__main__':
    main()