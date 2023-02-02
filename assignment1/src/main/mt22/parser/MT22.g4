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

WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, backspace, form feed, carriage return, newline


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;

/*=========================	COMMENTS	============================== */
BLOCKCOMMENTS: '/*' .*? '*/' -> skip;
INLINECOMMENT: '//' ~[\r\n]* -> skip;

/*=========================	VARIABLE DECLARE =========================*/


/*=========================	FUNCTION DECLARE ========================= */

//	IDENTIFIERS
IDENTIFIERS: [_a-zA-Z][_a-zA-Z0-9]*;

/*=========================	KEYWORDS	==============================*/

//	Methods 
INHERIT: I N H E R I T;
VOID: V O I D;
RETURN: R E T U R N;
FUNCTION: F U N C T I O N;

//	Values
TRUE: T R U E;
FALSE: F A L S E;

//	Flow Statements
IF: I F;
ELSE: E L S E;

//	Loop Statements
WHILE: W H I L E;
FOR: F O R;
DO: D O;
BREAK: B R E A K;
CONTINUE: C O N T I N U E;

//	Singular types
INTEGER: I N T E G E R;
FLOAT: F L O A T;
STRING: S T R I N G;
BOOLEAN: B O O L E A N;

//	Compound types
ARRAY: A R R A Y;

AUTO: A U T O;
OF: O F;

/*=========================	OPERATORS	============================== */
ADD: 		'+';
SUBSTRACT: 	'-';
DIVIDE:		'/';
MULTIPLY:	'*';
MODULO:		'%';

NOTEQUAL:	'!=';
EQUAL:		'==';
AND:		'&&';
OR:			'||';
NOT:		'!';

LESS:		'<';
LEQ:		'<=';
GREATER:	'>';
GEQ:		'>=';
GLOBAL: 	'::';

/*=========================	SEPERATORS	============================== */


/*=========================	LITERALS	============================== */



/*=========================	 */

/* */
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