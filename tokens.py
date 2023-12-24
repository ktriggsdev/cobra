import ply.lex as lex
import time

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE'
}

tokens = [
             # Define your tokens here, e.g., NUMBER, STRING, IDENTIFIER, KEYWORDS:
             'NUMBER',
             'FLOAT',
             'STRING',
             'PLUS',
             'MINUS',
             'DIVIDE',
             'MULTIPLY',
             'MODULO',
             'LPAREN',
             'RPAREN',
             'LBRACE',
             'RBRACE',
             'BLOCKSTART',
             'BLOCKEND',
             'NOT',
             'EQUALS',
             'LT',
             'GT',
             'LTE',
             'GTE',
             'DOUBLEEQUAL',
             'NE',
             'AND',
             'OR',
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
t_MODULO = r'%'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_BLOCKSTART = r'\{'
t_BLOCKEND = r'\}'
t_NOT = r'\~'
t_EQUALS = r'\='
t_GT = r'\>'
t_LT = r'\<'
t_LTE = r'\<\='
t_GTE = r'\>\='
t_DOUBLEEQUAL = r'\=\='
t_NE = r'\!\='
t_AND = r'\&'
t_OR = r'\|'
t_STRING = r'\w'

# ... regular expressions for other tokens

# A regular expression rule with some action code:
num_count = 0


def t_NUMBER(t):
    r'\d+'
    global num_count
    num_count += 1
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t


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
data = '''[25/(3*40) + {300-20} -16.5]
{(300-250)<(400-500)}
20 & 30 | 50
hello world
# This is a comment'''

# Give the lexer some input:
lexer.input(data)

# Start the timer before tokenization
start_time = time.time()

# Tokenize:
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(f"token_type: {tok.type}, token_value: {tok.value}, token_line_number: {tok.lineno}, "
          f"token_lex_position: {tok.lexpos}")
    print(f"num_count: {num_count}")

# Stop the timer after tokenization
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time
print(f"\nCompilation time: {elapsed_time:.4f} seconds")

