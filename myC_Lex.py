import ply.lex as lex

#List of reserved tokens
reserved = {
	'program'	: 'PROGRAM',
	'var' 		: 'VAR',
	'int' 		: 'INT',
	'float' 	: 'FLOAT',
	'char' 		: 'CHAR',
	'bool' 		: 'BOOL',
	'void' 		: 'VOID',
	'func' 		: 'FUNC',
	'return'	: 'RETURN',
#	'null' 		: 'NULL',
	'if' 		: 'IF',
	'else' 		: 'ELSE',
	'while' 	: 'WHILE',
	'from' 		: 'FROM',
	'to' 		: 'TO',
	'main' 		: 'MAIN',
	'end'		: 'END',
	'read' 		: 'READ',
	'write' 	: 'WRITE',

	'hist'		: 'HIST',
	'mean'		: 'MEAN',	
	'median'	: 'MEDIAN',
	'mode'		: 'MODE',
	'variance'	: 'VARIANCE',
	'sd'		: 'SD',
	'scale'		: 'SCALE',
	'avg'		: 'AVG',
}

#List of tokens
tokens = [
	'COMMA',
#	'DOT',
	'COL',
	'SEMICOL',
	'LCURLY',
	'RCURLY',
	'LBRACK',
	'RBRACK',
	'LPAR',
	'RPAR',
	'ISEQUAL',
	'EQUAL',
	'NOTEQUAL',
	'GREATERTHAN',
	'GREATERORQUAL',
	'LESSTHAN',
	'LESSOREQUAL',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIV',
	'AND',
	'OR',
	'COMMENT',
	'ID',
	'CTEI',
	'CTEF',
	'CTEC',
	'CTES',
	'CTEB'
]  + list(reserved.values())

#Regular expresions for simple tokens
t_COMMA				= r'\,'
# t_DOT				= r'\.'
t_COL				= r'\:'
t_SEMICOL			= r'\;'
t_LCURLY			= r'\{'
t_RCURLY			= r'\}'
t_LBRACK			= r'\['
t_RBRACK			= r'\]'
t_LPAR				= r'\('
t_RPAR				= r'\)'
t_ISEQUAL			= r'\=\='
t_EQUAL				= r'\='
t_NOTEQUAL			= r'\!\='
t_GREATERTHAN		= r'\>'
t_GREATERORQUAL		= r'\>\='
t_LESSTHAN			= r'\<'
t_LESSOREQUAL		= r'\<\='
t_PLUS				= r'\+'
t_MINUS				= r'\-'
t_TIMES				= r'\*'
t_DIV				= r'\/'
t_AND				= r'\&\&'
t_OR				= r'\|\|'

def t_CTEB(t):
	r'([Tt][Rr][Uu][Ee])|([Ff][Aa][Ll][Ss][Ee])'
	t.value = bool(t.value)
	return t

def t_ID(t):
	r'[a-zA-Z][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'ID')
	return t

def t_CTEF(t):
	r'[-+]?[0-9]+\.[0-9]+(e[\-\+]?[0-9]+(\.[0-9]+)?)?'
	t.value = float(t.value)
	return t

def t_CTEI(t):
	#r'[-+]?[0-9]+(e[\-\+][0-9]+(\.[0-9]+)?)?'
	r'[-+]?[0-9]+'
	t.value = int(t.value)
	return t

def t_CTEC(t):
	# r'\'[a-zA-Z0-9(\n)(\t)]\''
	r'\'([^\\\n]|(\\.))\''
	t.value = t.value[1:-1]
	return t

def t_CTES(t):
	r'\"([^\\\n]|(\\.))*?\"'
	t.value = t.value[1:-1]
	return t

def t_COMMENT(t):
	r'\#.*'
	pass

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)



# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)


lexer = lex.lex()

# data = 'hello'

# while (data != "0"):


# 	data = input("$> ")

# 	lexer.input(data)

# 	# Tokenize
# 	while True:
# 		tok = lexer.token()
# 		if not tok:
# 			break      # No more input
# 		print(tok)