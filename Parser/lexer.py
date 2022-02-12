import ply.lex as lexer


class LexParser:
    def __init__(self):
        self.lexer = lexer.lex(module=self)

    reserved = {
        r'true': 'TRUE',
        r'false': 'FALSE',
        r'boolean': 'BOOLEAN',
        r'int': 'INT',
        r'sizeof': 'SIZEOF',
        r'map': 'MAP',
        r'inc': 'INC',
        r'dec': 'DEC',
        r'or': 'OR',
        r'not': 'NOT',
        r'gt': 'GT',
        r'lt': 'LT',
        r'while': 'WHILE',
        r'do': 'DO',
        r'if': 'IF',
        r'else': 'ELSE',
        r'print': 'PRINT',
        r'step': 'STEP',
        r'right': 'RIGHT',
        r'left': 'LEFT',
        r'back': 'BACK',
        r'look': 'LOOK',
        r'proc': 'PROC',
        r'bar': 'BAR',
        r'emp': 'EMP',
        r'set': 'SET',
        r'clr': 'CLR'
    }

    special = [
        'NUM', 'VARIABLE',
        'OPBR', 'CLBR', 'OPSQBR', 'CLSQBR',
        'ASSIGN', 'EQUAL',
        'EOS', 'MULT', 'DIV'
    ]
    tokens = special + list(reserved.values())
    t_ignore = ' \t'

    def input(self, d):
        return self.lexer.input(d)

    def token(self):
        return self.lexer.token()

    t_MULT = r'\*'
    t_DIV = r'/'

    @staticmethod
    def t_NUM(t):
        r"""\-?\d+"""
        t.value = int(t.value)
        return t

    def t_VARIABLE(self, t):
        r"""[a-zA-Z][a-zA-Z\d\_]*"""
        t.value = t.value.lower()
        t.type = self.reserved.get(t.value, 'VARIABLE')
        return t

    @staticmethod
    def t_OPBR(t):
        r"""\("""
        return t

    @staticmethod
    def t_CLBR(t):
        r"""\)"""
        return t

    @staticmethod
    def t_OPSQBR(t):
        r"""\["""
        return t

    @staticmethod
    def t_CLSQBR(t):
        r"""\]"""
        return t

    @staticmethod
    def t_ASSIGN(t):
        r"""\:\="""
        return t

    @staticmethod
    def t_EQUAL(t):
        r"""\="""
        return t

    @staticmethod
    def t_EOS(t):
        r"""\n+"""
        t.lexer.lineno += t.value.count('\n')
        return t

    @staticmethod
    def t_error(t):
        print(f"Invalid character {t.value[0]}")
        t.lexer.skip(1)
        t.value = t.value[0]
        return t


if __name__ == '__main__':
    with open('check.txt', 'r') as f:
        data = f.read()
    lex = LexParser()
    lex.input(data)
    while True:
        tok = lex.token()
        if not tok:
            break
        print(tok)
