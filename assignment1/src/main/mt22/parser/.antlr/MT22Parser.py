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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'/'", "'*'", "'%'", "'!='", "'=='", 
                     "'&&'", "'||'", "'!'", "'<'", "'<='", "'>'", "'>='", 
                     "'::'" ]

    symbolicNames = [ "<INVALID>", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "BLOCKCOMMENTS", "INLINECOMMENT", 
                      "IDENTIFIERS", "INHERIT", "VOID", "RETURN", "FUNCTION", 
                      "TRUE", "FALSE", "IF", "ELSE", "WHILE", "FOR", "DO", 
                      "BREAK", "CONTINUE", "INTEGER", "FLOAT", "STRING", 
                      "BOOLEAN", "ARRAY", "AUTO", "OF", "ADD", "SUBSTRACT", 
                      "DIVIDE", "MULTIPLY", "MODULO", "NOTEQUAL", "EQUAL", 
                      "AND", "OR", "NOT", "LESS", "LEQ", "GREATER", "GEQ", 
                      "GLOBAL", "A", "B", "C", "D", "E", "F", "G", "H", 
                      "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
                      "S", "T", "U", "V", "W", "X", "Y", "Z" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    WS=1
    ERROR_CHAR=2
    UNCLOSE_STRING=3
    ILLEGAL_ESCAPE=4
    BLOCKCOMMENTS=5
    INLINECOMMENT=6
    IDENTIFIERS=7
    INHERIT=8
    VOID=9
    RETURN=10
    FUNCTION=11
    TRUE=12
    FALSE=13
    IF=14
    ELSE=15
    WHILE=16
    FOR=17
    DO=18
    BREAK=19
    CONTINUE=20
    INTEGER=21
    FLOAT=22
    STRING=23
    BOOLEAN=24
    ARRAY=25
    AUTO=26
    OF=27
    ADD=28
    SUBSTRACT=29
    DIVIDE=30
    MULTIPLY=31
    MODULO=32
    NOTEQUAL=33
    EQUAL=34
    AND=35
    OR=36
    NOT=37
    LESS=38
    LEQ=39
    GREATER=40
    GEQ=41
    GLOBAL=42
    A=43
    B=44
    C=45
    D=46
    E=47
    F=48
    G=49
    H=50
    I=51
    J=52
    K=53
    L=54
    M=55
    N=56
    O=57
    P=58
    Q=59
    R=60
    S=61
    T=62
    U=63
    V=64
    W=65
    X=66
    Y=67
    Z=68

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





