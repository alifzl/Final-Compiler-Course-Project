# coding: utf-8
import sys
import ply.lex as lex

from commom import find_column
import tokrules


class MyLex(object):

    def __init__(self, module=tokrules):
        self.module = module
        self.lexer = None
        self.llex = []

        self._build_lexer()

    def _build_lexer(self):
        self.lexer = lex.lex(module=self.module)

    def tokenize(self, newString):
        self.lexer.input(str(newString))

        while True:
            tok = self.lexer.token()
            if not tok:
                break
            lt = (tok.type, tok.value, tok.lineno, find_column(newString, tok))
            self.llex.append(lt)

        return tuple(self.llex), tuple(tokrules.lerror)


if __name__ == '__main__':
    entered_expression = 0
    if len(sys.argv) != 2:
        print('Choose a appropriate cool file to read. (excepting a .cl file)')
        sys.exit(1)

    with open(sys.argv[1]) as file:
        entered_expression = file.read()
    l = MyLex()
    llex, lerror = l.tokenize(entered_expression)

    for l in llex:
        print(l)

    print('ERROR')
    for e in lerror:
        print(e)
