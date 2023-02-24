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

program:  (vardecl | fundecl) + EOF;

/*	=============================== Grammar - Parser - Declarations */

// Variables declarations
vardecl: list_of_ids COLON  primitive_type SEMI 
		  | list_of_ids COLON primitive_type EQ expr SEMI;
list_of_ids: IDENTIFIERS another_id_list | IDENTIFIERS;
another_id_list: COMMA list_of_ids;

funcdecl: 'funcdecl';

expr: 'Expr';
primitive_type: INTEGER | FLOAT | BOOLEAN | STRING | AUTO | VOID | arraytype;
arraytype: ARRAY; 

//	Comments
BLOCKCOMMENT: 
				'/*' .*? '*/' -> skip;
INLINECOMMENT: 
				'//' ~[\r\n]* -> skip;


/*	=============================== LEXER ================================== */
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

//	Singular types
INTEGER: 	'integer';
FLOAT: 		'float';
STRING: 	'string';
BOOLEAN: 	'boolean';

//	Compound types
ARRAY: 		'array';
AUTO: 		'auto';
OF: 		'of';

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
//	LITERALS
INTLIT: [0] | ([1-9] (ZeroDigits | ('_'))*) {self.text = self.text.replace('_','')};
FLOATLIT: INTLIT (DOT | ExpPart ('-'|'+')?) ZeroDigits* (DOT | ExpPart ('-'|'+'))? ZeroDigits*;
STRINGLIT: DoubleQuote (StringChar*) DoubleQuote {
	string = str(self.text)
	self.text = string[1:-1]
};
BOOLIT: 'true' | 'false';


//	IDENTIFIERS
IDENTIFIERS: [_a-zA-Z][_a-zA-Z0-9]*;



/*=========================	 Fragments =====================================*/

fragment IntPart: INTLIT;
fragment DOT: '.';
fragment ExpPart: [eE];
fragment ZeroDigits: [0-9];
fragment EscapeSeqs: '\\'[tbfrn"\\];
fragment Exp: [eE];

fragment DoubleQuote: '"';
fragment StringChar: ~[\t\b\n\r\f"\\]
					| ESCSeq;
fragment ESCSeq: '\\'[tbnrf"\\];


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

ILLEGAL_ESCAPE: .{
	raise IllegalEscape(self.text)
};
