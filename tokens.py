import ply.lex as lex

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE'
}

tokens = [
             # Define your tokens here, e.g., NUMBER, STRING, IDENTIFIER, KEYWORDS:
             'NUMBER',
             'STRING',
             'PLUS',
             'MINUS',
             'DIVIDE',
             'MULTIPLY',
             'LPAREN',
             'RPAREN',
             'ID',
             'COMMENT'
         ] + list(reserved.values())


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token Discarded


# Regular expressions to match each token type:
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# ... regular expressions for other tokens

# A regular expression rule with some action code:
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\b\w+\b'
    t.value = str(t.value)


# Define a rule so we can track line numbers:
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Compute column.
# input is the input text string
# token is a token instance
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# A string containing ignored characters (spaces and tabs):
t_ignore = ' \t'  # Ignore whitespace


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer:
lexer = lex.lex()

# Test it out:
data = '''3 + 4 * 10 + -20 * 2'''

# Give the lexer some input:
lexer.input(data)

# Tokenize:
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
