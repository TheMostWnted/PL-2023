import ply.lex as lex

# tokens
tokens = [
    'ID',
    'INT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMA',
    'LT',
    'GT',
    'LTE',
    'GTE',
    'EQ',
    'NEQ',
    'FUNCTION',
    'PROGRAM',
    'FOR',
    'IN',
    'RANGE',
    'PRINT',
    'WS',
    'COMMENT'
]

# Expressões regulares dos tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_SEMICOLON = r';'
t_COMMA = r','
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_EQ = r'=='
t_NEQ = r'!='

# Função que detecta identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Função que identifica os números inteiros
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# palavras reservadas
reserved = {
    'int': 'INT',
    'function': 'FUNCTION',
    'program': 'PROGRAM',
    'for': 'FOR',
    'in': 'IN',
    'range': 'RANGE',
    'print': 'PRINT'
}

# Função para ignorar espaços em branco
def t_WS(t):
    r'\s+'
    pass

# Função para ignorar linha de comentários
def t_COMMENT(t):
    r'//.*'
    pass

# Função que lida com erros de tokenização
def t_error(t):
    print(f"Caracter ilegal {t.value[0]}")
    t.lexer.skip(1)

# Criação do analisador léxico
lexer = lex.lex()

# Código fornecido para teste
code = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/
program myFact {
  for i in [1..10] {
    print(i, fact(i))
  }
}

function fact(n) {
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1
  }
}

int i;
"""

# Passagem do código para o analisador léxico
lexer.input(code)

# Impressão dos tokens encontrados
for token in lexer:
    print(token)
