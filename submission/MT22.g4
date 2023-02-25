/*
	Principle of Programming Languages
	Assignment 1 - Lexer and  Recognizer
	AUTHOR: Ho Quang Nguyen - 2052666
	
	""" MT22 is a case sensitive programming language """
*/
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl EOF;
decl: (vardecl | funcdecl | vardecl_array) decl | (vardecl | funcdecl | vardecl_array);
/*	=============================== Grammar - Parser - Declarations */
//	Types of program

atomic_type: BOOLEAN | INTEGER | FLOAT | STRING;						// Atomic type
function_type: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | VOID;		// Types that functions can return
include_auto_type: BOOLEAN | INTEGER | FLOAT | STRING | AUTO;			// Atomic but include auto type

// Variables declarations
// Bugs: cannot check compatible of values init and number of variables
vardecl: (vardecl_with_init | vardecl_no_init | vardecl_array) SEMI; 

vardecl_with_init: IDENTIFIERS COMMA vardecl_with_init COMMA expr
					|IDENTIFIERS COLON include_auto_type ASSIGN expr;
vardecl_no_init: list_of_ids COLON  include_auto_type; 
list_of_ids: IDENTIFIERS another_id_list | IDENTIFIERS;
another_id_list: COMMA list_of_ids;

//	Array declarations
// Format: ID {<dimensions>} of primitive_type
vardecl_array: ARRAY LEFT_SQUARE_BRACKET dimensions RIGHT_SQUARE_BRACKET OF atomic_type;
dimensions: INTLIT COMMA dimensions | INTLIT;

//Format: {<nullable-comma separated list of expressions>}
array_literal: LEFT_CURLY_BRACKET expr_list RIGHT_CURLY_BRACKET;
expr_list: list_of_exprs |;
list_of_exprs: expr COMMA list_of_exprs | expr;

// Format: ID [<comma-separated list of expressions>]
array_indexing: IDENTIFIERS LEFT_SQUARE_BRACKET indexop_expr RIGHT_SQUARE_BRACKET;
indexop_expr: expr COMMA indexop_expr | expr;


//	Function declarations
//	Format: <function prototype> <function body>
funcdecl: function_prototype function_body;

//	Function prototype
//	Format: ID : <function keyword> <return type> (<param list>) [<inherit keyword> <function name>]?
function_prototype: IDENTIFIERS COLON FUNCTION function_type LEFT_PARENTHESIS func_params RIGHT_PARENTHESIS
					| IDENTIFIERS COLON FUNCTION function_type LEFT_PARENTHESIS func_params RIGHT_PARENTHESIS INHERIT IDENTIFIERS;
function_body: block_stmt;
func_params: paramlist |;
paramlist: paramone COMMA paramlist | paramone;
paramone: INHERIT? IDENTIFIERS? IDENTIFIERS COLON include_auto_type;
function_call: IDENTIFIERS LEFT_PARENTHESIS arg_list RIGHT_PARENTHESIS;
arg_list: arg_list_params | ;
arg_list_params: (IDENTIFIERS | expr) COMMA arg_list_params | (IDENTIFIERS | expr);


literal: INTLIT | FLOATLIT | BOOLIT | STRINGLIT | array_literal;
sub_expr: (LEFT_PARENTHESIS expr RIGHT_PARENTHESIS);

//	Expressions
// 	The orders of the expr is from bottom-to-top 
//  respective to the table provided in section 6.7
expr : expr1 STRING_CONCAT expr1 | expr1;  									// Concat string
expr1: expr2 (EQUAL | NOTEQUAL | GREATER | GEQ | LESS | LEQ) expr2 | expr2; // Relational
expr2: expr2 (AND | OR) expr3 | expr3; 										// Logical 
expr3: expr3 (ADD | SUBSTRACT) expr4 | expr4; 								// Add or substract expression
expr4: expr4 (MULTIPLY | DIVIDE |MODULO) expr5 | expr5; 					// Multiply, divide, modulo
expr5: NOT expr5 | expr6; 													// Logical not
expr6: SUBSTRACT expr6 | expr7;												// Sign
expr7: literal | sub_expr | IDENTIFIERS | array_indexing | function_call; 					// Index operator

//	Statments
stmt: 			assign_stmt
				| if_stmt
				| for_stmt
				| while_stmt
				| do_while_stmt
				| break_stmt
				| continue_stmt
				| return_stmt
				| block_stmt
				| call_stmt; 

noblock_stmt:   
				assign_stmt
				| if_stmt
				| for_stmt
				| while_stmt
				| do_while_stmt
				| break_stmt
				| continue_stmt
				| return_stmt
				| call_stmt;

assign_stmt: (IDENTIFIERS | array_indexing) ASSIGN expr SEMI; // MISSING INDEX EXPRESSION

// if_stmt: match_if | unmatch_if;
// match_if: IF LB exp RB match_if
if_stmt: IF LEFT_PARENTHESIS expr RIGHT_PARENTHESIS stmt
		|IF LEFT_PARENTHESIS expr RIGHT_PARENTHESIS stmt ELSE stmt;

for_stmt: FOR LEFT_PARENTHESIS (IDENTIFIERS | array_indexing) ASSIGN expr COMMA expr COMMA expr RIGHT_PARENTHESIS stmt;

while_stmt: WHILE LEFT_PARENTHESIS expr RIGHT_PARENTHESIS stmt;

do_while_stmt: DO block_stmt WHILE LEFT_PARENTHESIS expr RIGHT_PARENTHESIS;

break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI; 
return_stmt: RETURN expr SEMI;
call_stmt: function_call SEMI;
block_stmt: LEFT_CURLY_BRACKET (noblock_stmt | vardecl)* RIGHT_CURLY_BRACKET;

/*	=============================== LEXER ================================== */
//	Comments
BLOCKCOMMENT: 
				'/*' .*? '*/' -> skip;
INLINECOMMENT: 
				'//' ~[\r\n]* -> skip;

//	Singular types
INTEGER: 	'integer';
FLOAT: 		'float';
STRING: 	'string';
BOOLEAN: 	'boolean';

//	Compound types
ARRAY: 		'array';
AUTO: 		'auto';
OF: 		'of';

//	KEYWORDS - Methods 
INHERIT: 	'inherit';
VOID: 		'void';
RETURN:  	'return';
FUNCTION: 	'function';

//	Flow Statements
IF: 		'if';
ELSE: 		'else';


//	Loop Statements
WHILE: 		'while';
FOR: 		'for';
DO: 		'do';
BREAK: 		'break';
CONTINUE: 	'continue';

//	OPERATORS
ADD: 						'+';
SUBSTRACT: 					'-';
DIVIDE:						'/';
MULTIPLY:					'*';
MODULO:						'%';

NOTEQUAL:					'!=';
EQUAL:						'==';
AND:						'&&';
OR:							'||';
NOT:						'!';

LESS:						'<';
LEQ:						'<=';
GREATER:					'>';
GEQ:						'>=';
STRING_CONCAT: 				'::';

// SEPARATORS	
LEFT_PARENTHESIS: 			'(';
RIGHT_PARENTHESIS: 			')';
LEFT_SQUARE_BRACKET: 		'[';
RIGHT_SQUARE_BRACKET: 		']';
LEFT_CURLY_BRACKET:			'{';
RIGHT_CURLY_BRACKET:		'}';
ASSIGN:						'=';
COLON:						':';											// May not sure whether the colon is counted as one token in vardecl
COMMA: 						',';											// May not sure whether the comma is counted as one token in vardecl
SEMI: 						';';
DOT:						'.';

IDENTIFIERS: [_a-zA-Z][_a-zA-Z0-9]*;

//	LITERALS
INTLIT: IntPart {
					self.text = self.text.replace('_', '')
				};
FLOATLIT: IntPart (DecPart ExpPart? | ExpPart) 
				{
					self.text = self.text.replace('_', '')
				};
STRINGLIT: DoubleQuote (StringChar | EscapeSeqs)* DoubleQuote {
	string = str(self.text)
	self.text = string[1:-1]
};
BOOLIT: 'true' | 'false';


//	IDENTIFIERS



/*=========================	 Fragments =====================================*/

fragment ZeroDigits: [0-9];
fragment NonZeroDigits: [1-9];
fragment EscapeSeqs: '\\'[tbfrn"\\];
fragment UNDERSCORED: '_';
fragment DoubleQuote: '"';
fragment StringChar: (~[\\"'\t\b\n\r\f]);
fragment ESCSeq: '\\'[tbnrf'"\\];
fragment Illegal_ESCSeq: '\\' ~[tbnrf'"\\] | '\'' ~'"';
fragment ExpPart: [eE][+-]? ZeroDigits+;
fragment DecPart: [.] ZeroDigits*;
fragment IntPart: [0] | NonZeroDigits ZeroDigits* (UNDERSCORED? ZeroDigits)*;


//	Raise Error
WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, backspace, form feed, carriage return, newline

ERROR_CHAR: .{
	raise ErrorToken(self.text)
};
UNCLOSE_STRING: DoubleQuote StringChar* ([\b\t\f\n\r"\\] | EOF)
    {
        unclose_str = str(self.text)
        possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
        if unclose_str[-1] in possible:
            raise UncloseString(unclose_str[1:-1])
        else:
            raise UncloseString(unclose_str[1:])
};

ILLEGAL_ESCAPE: DoubleQuote (StringChar | EscapeSeqs)* Illegal_ESCSeq 
{
	text = str(self.text)
	raise IllegalEscape(text[1:])
};
