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

program:  EOF ;





/*=========================	COMMENTS	============================== */
BLOCKCOMMENT: 
				'/*' .*? '*/' -> skip;
INLINECOMMENT: 
				'//' ~[\r\n]* -> skip;

/*=========================	VARIABLE DECLARE =========================*/


/*=========================	FUNCTION DECLARE ========================= */

/*	=============================== LEXER ================================== */
//	IDENTIFIERS
IDENTIFIERS: [_a-zA-Z][_a-zA-Z0-9]*;


//	KEYWORDS - Methods 
INHERIT: 'inherit';
VOID: 'void';
RETURN:  'return';
FUNCTION: 'function';

//	KEYWORDS - Values
TRUE: 'true';
FALSE: 'false';

//	Flow Statements
IF: 'if';
ELSE: 'else';


//	Loop Statements
WHILE: 'while';
FOR: 'for';
DO: 'do';
BREAK: 'break';
CONTINUE: 'continue';

//	Singular types
INTEGER: 'integer';
FLOAT: 'float';
STRING: 'string';
BOOLEAN: 'boolean';

//	Compound types
ARRAY: 'array';
AUTO: 'auto';
OF: 'of';

//	OPERATORS
ADD: 				'+';
SUBSTRACT: 			'-';
DIVIDE:				'/';
MULTIPLY:			'*';
MODULO:				'%';

NOTEQUAL:			'!=';
EQUAL:				'==';
AND:				'&&';
OR:					'||';
NOT:				'!';

LESS:				'<';
LEQ:				'<=';
GREATER:			'>';
GEQ:				'>=';
STRING_CONCAT: 		'::';

// SEPARATORS	
LEFT_PARENTHESIS: 		'(';
RIGHT_PARENTHESIS: 		')';
LEFT_SQUARE_BRACKET: 	'[';
RIGHT_SQUARE_BRACKET: 	']';
LEFT_CURLY_BRACKET:		'{';
RIGHT_CURLY_BRACKET:	'}';
ASSIGN:					'=';


//	LITERALS
INTLIT: [0] | ([1-9] (ZeroDigits | ('_'))*) {self.text = self.text.replace('_','')};
BOOLIT:
		TRUE
		| FALSE;

//	Raise Error

WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, backspace, form feed, carriage return, newline

ERROR_CHAR: .{
	raise ErrorToken(self.text)
};
UNCLOSE_STRING: .{
	raise UncloseString(self.text)	
};
ILLEGAL_ESCAPE: .{
	raise IllegalEscape(self.text)
};

/*=========================	 Fragments =====================================*/

fragment ZeroDigits: [0-9];
fragment DoubleQuote: '"';
fragment EscapeSeqs: '\\'[tbfrn"\\];
fragment StringChar: 
					~[\t\b\f\r\n"\\]
					| ( (~[DoubleQuote]) | ([DoubleQuote][DoubleQuote]))*
					| EscapeSeqs;
fragment Exp: [E];
fragment Minus: '-';
A:[a];
B:[b];
C:[c];
D:[d];
E:[e];
F:[f];
G:[g];
H:[h];
I:[i];
J:[j];
K:[k];
L:[l];
M:[m];
N:[n];
O:[o];
P:[p];
Q:[q];
R:[r];
S:[s];
T:[t];
U:[u];
V:[v];
W:[w];
X:[x];
Y:[y];
Z:[z];
