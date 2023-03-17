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

program:  (vardecl | funcdecl) + EOF;

/*	=============================== Grammar - Parser - Declarations */

// Variables declarations
// Bugs: cannot check compatible of values init and number of variables
vardecl: (vardecl_with_init | vardecl_no_init | vardecl_array) SEMI; 

vardecl_with_init: IDENTIFIERS COMMA vardecl_with_init COMMA expr
					|IDENTIFIERS COLON primitive_type ASSIGN expr;
vardecl_no_init: list_of_ids COLON  primitive_type; 
list_of_ids: IDENTIFIERS another_id_list | IDENTIFIERS;
another_id_list: COMMA list_of_ids;

vardecl_array: 'vardecl_array';

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
FLOATLIT: IntPart (DecPart ExpPart * | ExpPart) 
				{
					self.text = self.text.replace('_', '')
				};
STRINGLIT: DoubleQuote (StringChar*) DoubleQuote {
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
fragment StringChar: ~[\t\b\n\r\f"\\]
					| ESCSeq;
fragment ESCSeq: '\\'[tbnrf"\\];
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

ILLEGAL_ESCAPE: .{
	raise IllegalEscape(self.text)
};
