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

/*========================= IDENTIFIERS ==============================*/
