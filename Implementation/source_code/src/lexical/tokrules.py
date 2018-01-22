# Reserved words
reserved = [
    'class', 'in', 'inherits', 'isvoid', 'let', 'new', 'of', 'not',
    'loop', 'pool', 'case', 'esac', 'if', 'then', 'else', 'fi', 'while'
]

tokens = [
   'COMMENTINLINE', 'DARROW', 'CLASS', 'IN', 'INHERITS', 'ISVOID', 'LET',
   'NEW', 'OF', 'NOT', 'LOOP', 'POOL', 'CASE', 'ESAC', 'IF', 'THEN', 'ELSE',
   'FI', 'WHILE', 'ASSIGN', 'LE', 'PLUS', 'MINUS', 'MULT', 'DIV', 'LPAREN',
   'RPAREN', 'LBRACE', 'RBRACE', 'DOT', 'COLON', 'COMMA', 'SEMI', 'EQ',
   'NEG', 'LT', 'AT', 'TYPEID', 'OBJECTID', 'INT_CONST', 'STR_CONST',
   'COMMENT', 'BOOL_CONST'
]

# Regex dos Tokens
t_DARROW = '=>'
t_ASSIGN = '<-'
t_LE = '<='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_COLON = ':'
t_COMMA = ','
t_SEMI = ';'
t_EQ = '='
t_NEG = '~'
t_LT = '<'
t_AT = '@'

t_ignore = ' \t\r\f'


# Handle objects_types_and_reserved_words
def t_ID(t):
    # regular expression for all type of characters could be happen 
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # checking if it's boolean value
    if t.value == 'true':
        t.type = 'BOOL_CONST'
        t.value = True
        return t
    if t.value == 'false':
        t.type = 'BOOL_CONST'
        t.value = False
        return t
    # if the lower value of word is in the reserved set,
    # capitalize it and take it as a reserved word
    if t.value.lower() in reserved:
        t.type = t.value.upper()
    else:
        if t.value[0].islower():
            # if the first character of word is lower case,
            # and it's notin the reserved words which defined above...
            # it's a id of an object (variable name)
            t.type = 'OBJECTID'
        else:
            # it's an type ID
            t.type = 'TYPEID'
    return t

# comment or not ! that's the question...
def t_COMMENT(t):
    r'--.* | \(\*.+[\n\*\w\s]*\*\)'
    pass


def t_STRING(t):
    # we wanna detect a pure string
    # so special characters like ' ^ ' and ' " ' is not allowed
    #  ' *\ ' string could be repeated as many as it wants !
    r'\"[^"]*\"'
    # ignoring string-escape (every special and reserved letter in the language)
    t.value = t.value[1:-1].decode("string-escape")
    #  assigning the type of the produced string as a constant string
    t.type = 'STR_CONST'
    # and returning...
    return t


def t_INT_CONST(t):
    # simple integer we got here
    r'\d+'
    t.value = int(t.value)
    return t


def t_NEWLINE(t):
    # ' \n ' means new line !
    # just in case of you didn't know that !
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# a list for collecting the lexical errors
lerror = []

# collecting the lexical errors...
def t_error(t):
    # creating a set for recording the details of the lexical error
    #  value , line number and position of the token in line
    lr = (t.value[0], t.lineno, t.lexpos)
    # appending the error in the list of lexical errors
    lerror.append(lr)
    # skip the mistaken token
    t.lexer.skip(1)
