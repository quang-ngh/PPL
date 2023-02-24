# Generated from /home/quangngcs/Desktop/Github/PPL/assignment1/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'inherit'", 
                     "'void'", "'return'", "'function'", "'true'", "'false'", 
                     "'if'", "'else'", "'while'", "'for'", "'do'", "'break'", 
                     "'continue'", "'integer'", "'float'", "'string'", "'boolean'", 
                     "'array'", "'auto'", "'of'", "'+'", "'-'", "'/'", "'*'", 
                     "'%'", "'!='", "'=='", "'&&'", "'||'", "'!'", "'<'", 
                     "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "BLOCKCOMMENT", "INLINECOMMENT", "INHERIT", 
                      "VOID", "RETURN", "FUNCTION", "TRUE", "FALSE", "IF", 
                      "ELSE", "WHILE", "FOR", "DO", "BREAK", "CONTINUE", 
                      "INTEGER", "FLOAT", "STRING", "BOOLEAN", "ARRAY", 
                      "AUTO", "OF", "ADD", "SUBSTRACT", "DIVIDE", "MULTIPLY", 
                      "MODULO", "NOTEQUAL", "EQUAL", "AND", "OR", "NOT", 
                      "LESS", "LEQ", "GREATER", "GEQ", "STRING_CONCAT", 
                      "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", 
                      "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                      "ASSIGN", "INTLIT", "BOOLIT", "IDENTIFIERS", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    BLOCKCOMMENT=1
    INLINECOMMENT=2
    INHERIT=3
    VOID=4
    RETURN=5
    FUNCTION=6
    TRUE=7
    FALSE=8
    IF=9
    ELSE=10
    WHILE=11
    FOR=12
    DO=13
    BREAK=14
    CONTINUE=15
    INTEGER=16
    FLOAT=17
    STRING=18
    BOOLEAN=19
    ARRAY=20
    AUTO=21
    OF=22
    ADD=23
    SUBSTRACT=24
    DIVIDE=25
    MULTIPLY=26
    MODULO=27
    NOTEQUAL=28
    EQUAL=29
    AND=30
    OR=31
    NOT=32
    LESS=33
    LEQ=34
    GREATER=35
    GEQ=36
    STRING_CONCAT=37
    LEFT_PARENTHESIS=38
    RIGHT_PARENTHESIS=39
    LEFT_SQUARE_BRACKET=40
    RIGHT_SQUARE_BRACKET=41
    LEFT_CURLY_BRACKET=42
    RIGHT_CURLY_BRACKET=43
    ASSIGN=44
    INTLIT=45
    BOOLIT=46
    IDENTIFIERS=47
    WS=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





