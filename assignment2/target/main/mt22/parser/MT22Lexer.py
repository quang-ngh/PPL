# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01d4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\7/\u0135\n/\f/\16/\u0138")
        buf.write("\13/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u014a\n\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\7\62\u0151\n\62\f\62\16\62\u0154\13")
        buf.write("\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\5\63\u0162\n\63\3\64\3\64\3\65\3\65\3\66\3")
        buf.write("\66\3\67\3\67\38\38\39\39\39\3:\3:\3:\3:\5:\u0175\n:\3")
        buf.write(";\3;\5;\u0179\n;\3;\6;\u017c\n;\r;\16;\u017d\3<\3<\7<")
        buf.write("\u0182\n<\f<\16<\u0185\13<\3=\3=\3=\7=\u018a\n=\f=\16")
        buf.write("=\u018d\13=\3=\5=\u0190\n=\3=\7=\u0193\n=\f=\16=\u0196")
        buf.write("\13=\5=\u0198\n=\3>\6>\u019b\n>\r>\16>\u019c\3>\3>\3?")
        buf.write("\3?\3?\3?\7?\u01a5\n?\f?\16?\u01a8\13?\3?\3?\3?\3?\3?")
        buf.write("\3@\3@\3@\3@\7@\u01b3\n@\f@\16@\u01b6\13@\3@\3@\3A\3A")
        buf.write("\3A\7A\u01bd\nA\fA\16A\u01c0\13A\3A\3A\3A\3B\3B\3B\7B")
        buf.write("\u01c8\nB\fB\16B\u01cb\13B\3B\5B\u01ce\nB\3B\3B\3C\3C")
        buf.write("\3C\3\u01a6\2D\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\2i\2k\2")
        buf.write("m\2o\2q\2s\2u\2w\2y\2{\65}\66\177\67\u00818\u00839\u0085")
        buf.write(":\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\5\2")
        buf.write("\f\f$$^^\n\2$$))^^ddhhppttvv\3\2$$\4\2GGgg\4\2--//\3\2")
        buf.write("\60\60\3\2\62\62\5\2\n\f\16\17\"\"\4\2\f\f\17\17\3\3\f")
        buf.write("\f\2\u01df\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\3\u0087\3\2\2\2")
        buf.write("\5\u008f\3\2\2\2\7\u0095\3\2\2\2\t\u009c\3\2\2\2\13\u00a4")
        buf.write("\3\2\2\2\r\u00aa\3\2\2\2\17\u00af\3\2\2\2\21\u00b2\3\2")
        buf.write("\2\2\23\u00ba\3\2\2\2\25\u00be\3\2\2\2\27\u00c3\3\2\2")
        buf.write("\2\31\u00ca\3\2\2\2\33\u00d3\3\2\2\2\35\u00d6\3\2\2\2")
        buf.write("\37\u00db\3\2\2\2!\u00e1\3\2\2\2#\u00e5\3\2\2\2%\u00e8")
        buf.write("\3\2\2\2\'\u00ee\3\2\2\2)\u00f7\3\2\2\2+\u00f9\3\2\2\2")
        buf.write("-\u00fb\3\2\2\2/\u00fd\3\2\2\2\61\u00ff\3\2\2\2\63\u0101")
        buf.write("\3\2\2\2\65\u0104\3\2\2\2\67\u0107\3\2\2\29\u010a\3\2")
        buf.write("\2\2;\u010d\3\2\2\2=\u010f\3\2\2\2?\u0111\3\2\2\2A\u0114")
        buf.write("\3\2\2\2C\u0116\3\2\2\2E\u0119\3\2\2\2G\u011c\3\2\2\2")
        buf.write("I\u011e\3\2\2\2K\u0120\3\2\2\2M\u0122\3\2\2\2O\u0124\3")
        buf.write("\2\2\2Q\u0126\3\2\2\2S\u0128\3\2\2\2U\u012a\3\2\2\2W\u012c")
        buf.write("\3\2\2\2Y\u012e\3\2\2\2[\u0130\3\2\2\2]\u0132\3\2\2\2")
        buf.write("_\u0139\3\2\2\2a\u0149\3\2\2\2c\u014d\3\2\2\2e\u0161\3")
        buf.write("\2\2\2g\u0163\3\2\2\2i\u0165\3\2\2\2k\u0167\3\2\2\2m\u0169")
        buf.write("\3\2\2\2o\u016b\3\2\2\2q\u016d\3\2\2\2s\u0174\3\2\2\2")
        buf.write("u\u0176\3\2\2\2w\u017f\3\2\2\2y\u0197\3\2\2\2{\u019a\3")
        buf.write("\2\2\2}\u01a0\3\2\2\2\177\u01ae\3\2\2\2\u0081\u01b9\3")
        buf.write("\2\2\2\u0083\u01c4\3\2\2\2\u0085\u01d1\3\2\2\2\u0087\u0088")
        buf.write("\7k\2\2\u0088\u0089\7p\2\2\u0089\u008a\7v\2\2\u008a\u008b")
        buf.write("\7g\2\2\u008b\u008c\7i\2\2\u008c\u008d\7g\2\2\u008d\u008e")
        buf.write("\7t\2\2\u008e\4\3\2\2\2\u008f\u0090\7h\2\2\u0090\u0091")
        buf.write("\7n\2\2\u0091\u0092\7q\2\2\u0092\u0093\7c\2\2\u0093\u0094")
        buf.write("\7v\2\2\u0094\6\3\2\2\2\u0095\u0096\7u\2\2\u0096\u0097")
        buf.write("\7v\2\2\u0097\u0098\7t\2\2\u0098\u0099\7k\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\u009b\7i\2\2\u009b\b\3\2\2\2\u009c\u009d")
        buf.write("\7d\2\2\u009d\u009e\7q\2\2\u009e\u009f\7q\2\2\u009f\u00a0")
        buf.write("\7n\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3")
        buf.write("\7p\2\2\u00a3\n\3\2\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7t\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9")
        buf.write("\7{\2\2\u00a9\f\3\2\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac")
        buf.write("\7w\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae\7q\2\2\u00ae\16")
        buf.write("\3\2\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7h\2\2\u00b1\20")
        buf.write("\3\2\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5")
        buf.write("\7j\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8")
        buf.write("\7k\2\2\u00b8\u00b9\7v\2\2\u00b9\22\3\2\2\2\u00ba\u00bb")
        buf.write("\7q\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd\7v\2\2\u00bd\24")
        buf.write("\3\2\2\2\u00be\u00bf\7x\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1")
        buf.write("\7k\2\2\u00c1\u00c2\7f\2\2\u00c2\26\3\2\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7")
        buf.write("\7w\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7p\2\2\u00c9\30")
        buf.write("\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7e\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0")
        buf.write("\7k\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7p\2\2\u00d2\32")
        buf.write("\3\2\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7h\2\2\u00d5\34")
        buf.write("\3\2\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9")
        buf.write("\7u\2\2\u00d9\u00da\7g\2\2\u00da\36\3\2\2\2\u00db\u00dc")
        buf.write("\7y\2\2\u00dc\u00dd\7j\2\2\u00dd\u00de\7k\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7g\2\2\u00e0 \3\2\2\2\u00e1\u00e2")
        buf.write("\7h\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4\"")
        buf.write("\3\2\2\2\u00e5\u00e6\7f\2\2\u00e6\u00e7\7q\2\2\u00e7$")
        buf.write("\3\2\2\2\u00e8\u00e9\7d\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7m\2\2\u00ed&\3")
        buf.write("\2\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6\7g\2\2\u00f6(\3")
        buf.write("\2\2\2\u00f7\u00f8\7-\2\2\u00f8*\3\2\2\2\u00f9\u00fa\7")
        buf.write("/\2\2\u00fa,\3\2\2\2\u00fb\u00fc\7\61\2\2\u00fc.\3\2\2")
        buf.write("\2\u00fd\u00fe\7,\2\2\u00fe\60\3\2\2\2\u00ff\u0100\7\'")
        buf.write("\2\2\u0100\62\3\2\2\2\u0101\u0102\7#\2\2\u0102\u0103\7")
        buf.write("?\2\2\u0103\64\3\2\2\2\u0104\u0105\7?\2\2\u0105\u0106")
        buf.write("\7?\2\2\u0106\66\3\2\2\2\u0107\u0108\7(\2\2\u0108\u0109")
        buf.write("\7(\2\2\u01098\3\2\2\2\u010a\u010b\7~\2\2\u010b\u010c")
        buf.write("\7~\2\2\u010c:\3\2\2\2\u010d\u010e\7#\2\2\u010e<\3\2\2")
        buf.write("\2\u010f\u0110\7>\2\2\u0110>\3\2\2\2\u0111\u0112\7>\2")
        buf.write("\2\u0112\u0113\7?\2\2\u0113@\3\2\2\2\u0114\u0115\7@\2")
        buf.write("\2\u0115B\3\2\2\2\u0116\u0117\7@\2\2\u0117\u0118\7?\2")
        buf.write("\2\u0118D\3\2\2\2\u0119\u011a\7<\2\2\u011a\u011b\7<\2")
        buf.write("\2\u011bF\3\2\2\2\u011c\u011d\7*\2\2\u011dH\3\2\2\2\u011e")
        buf.write("\u011f\7+\2\2\u011fJ\3\2\2\2\u0120\u0121\7]\2\2\u0121")
        buf.write("L\3\2\2\2\u0122\u0123\7_\2\2\u0123N\3\2\2\2\u0124\u0125")
        buf.write("\7}\2\2\u0125P\3\2\2\2\u0126\u0127\7\177\2\2\u0127R\3")
        buf.write("\2\2\2\u0128\u0129\7?\2\2\u0129T\3\2\2\2\u012a\u012b\7")
        buf.write("<\2\2\u012bV\3\2\2\2\u012c\u012d\7.\2\2\u012dX\3\2\2\2")
        buf.write("\u012e\u012f\7=\2\2\u012fZ\3\2\2\2\u0130\u0131\7\60\2")
        buf.write("\2\u0131\\\3\2\2\2\u0132\u0136\t\2\2\2\u0133\u0135\t\3")
        buf.write("\2\2\u0134\u0133\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137^\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0139\u013a\5y=\2\u013a\u013b\b\60\2\2\u013b")
        buf.write("`\3\2\2\2\u013c\u013d\5y=\2\u013d\u013e\5w<\2\u013e\u014a")
        buf.write("\3\2\2\2\u013f\u0140\5y=\2\u0140\u0141\5u;\2\u0141\u014a")
        buf.write("\3\2\2\2\u0142\u0143\5w<\2\u0143\u0144\5u;\2\u0144\u014a")
        buf.write("\3\2\2\2\u0145\u0146\5y=\2\u0146\u0147\5w<\2\u0147\u0148")
        buf.write("\5u;\2\u0148\u014a\3\2\2\2\u0149\u013c\3\2\2\2\u0149\u013f")
        buf.write("\3\2\2\2\u0149\u0142\3\2\2\2\u0149\u0145\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b\u014c\b\61\3\2\u014cb\3\2\2\2\u014d")
        buf.write("\u0152\7$\2\2\u014e\u0151\5o8\2\u014f\u0151\5q9\2\u0150")
        buf.write("\u014e\3\2\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2")
        buf.write("\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155\3")
        buf.write("\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156\7$\2\2\u0156\u0157")
        buf.write("\b\62\4\2\u0157d\3\2\2\2\u0158\u0159\7v\2\2\u0159\u015a")
        buf.write("\7t\2\2\u015a\u015b\7w\2\2\u015b\u0162\7g\2\2\u015c\u015d")
        buf.write("\7h\2\2\u015d\u015e\7c\2\2\u015e\u015f\7n\2\2\u015f\u0160")
        buf.write("\7u\2\2\u0160\u0162\7g\2\2\u0161\u0158\3\2\2\2\u0161\u015c")
        buf.write("\3\2\2\2\u0162f\3\2\2\2\u0163\u0164\t\4\2\2\u0164h\3\2")
        buf.write("\2\2\u0165\u0166\t\5\2\2\u0166j\3\2\2\2\u0167\u0168\7")
        buf.write("a\2\2\u0168l\3\2\2\2\u0169\u016a\7$\2\2\u016an\3\2\2\2")
        buf.write("\u016b\u016c\n\6\2\2\u016cp\3\2\2\2\u016d\u016e\7^\2\2")
        buf.write("\u016e\u016f\t\7\2\2\u016fr\3\2\2\2\u0170\u0171\7^\2\2")
        buf.write("\u0171\u0175\n\7\2\2\u0172\u0173\7)\2\2\u0173\u0175\n")
        buf.write("\b\2\2\u0174\u0170\3\2\2\2\u0174\u0172\3\2\2\2\u0175t")
        buf.write("\3\2\2\2\u0176\u0178\t\t\2\2\u0177\u0179\t\n\2\2\u0178")
        buf.write("\u0177\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017b\3\2\2\2")
        buf.write("\u017a\u017c\5g\64\2\u017b\u017a\3\2\2\2\u017c\u017d\3")
        buf.write("\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017ev")
        buf.write("\3\2\2\2\u017f\u0183\t\13\2\2\u0180\u0182\5g\64\2\u0181")
        buf.write("\u0180\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0183\u0184\3\2\2\2\u0184x\3\2\2\2\u0185\u0183\3\2\2")
        buf.write("\2\u0186\u0198\t\f\2\2\u0187\u018b\5i\65\2\u0188\u018a")
        buf.write("\5g\64\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u0194\3\2\2\2")
        buf.write("\u018d\u018b\3\2\2\2\u018e\u0190\5k\66\2\u018f\u018e\3")
        buf.write("\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0193")
        buf.write("\5g\64\2\u0192\u018f\3\2\2\2\u0193\u0196\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0198\3\2\2\2")
        buf.write("\u0196\u0194\3\2\2\2\u0197\u0186\3\2\2\2\u0197\u0187\3")
        buf.write("\2\2\2\u0198z\3\2\2\2\u0199\u019b\t\r\2\2\u019a\u0199")
        buf.write("\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\b>\5\2")
        buf.write("\u019f|\3\2\2\2\u01a0\u01a1\7\61\2\2\u01a1\u01a2\7,\2")
        buf.write("\2\u01a2\u01a6\3\2\2\2\u01a3\u01a5\13\2\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01a6\3\2\2\2")
        buf.write("\u01a9\u01aa\7,\2\2\u01aa\u01ab\7\61\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01ac\u01ad\b?\5\2\u01ad~\3\2\2\2\u01ae\u01af\7")
        buf.write("\61\2\2\u01af\u01b0\7\61\2\2\u01b0\u01b4\3\2\2\2\u01b1")
        buf.write("\u01b3\n\16\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b6\3\2\2")
        buf.write("\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b7")
        buf.write("\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b8\b@\5\2\u01b8")
        buf.write("\u0080\3\2\2\2\u01b9\u01be\5m\67\2\u01ba\u01bd\5o8\2\u01bb")
        buf.write("\u01bd\5q9\2\u01bc\u01ba\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bd")
        buf.write("\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c2\5")
        buf.write("s:\2\u01c2\u01c3\bA\6\2\u01c3\u0082\3\2\2\2\u01c4\u01c9")
        buf.write("\7$\2\2\u01c5\u01c8\5o8\2\u01c6\u01c8\5q9\2\u01c7\u01c5")
        buf.write("\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cd\3\2\2\2")
        buf.write("\u01cb\u01c9\3\2\2\2\u01cc\u01ce\t\17\2\2\u01cd\u01cc")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\bB\7\2\u01d0")
        buf.write("\u0084\3\2\2\2\u01d1\u01d2\13\2\2\2\u01d2\u01d3\bC\b\2")
        buf.write("\u01d3\u0086\3\2\2\2\30\2\u0136\u0149\u0150\u0152\u0161")
        buf.write("\u0174\u0178\u017d\u0183\u018b\u018f\u0194\u0197\u019c")
        buf.write("\u01a6\u01b4\u01bc\u01be\u01c7\u01c9\u01cd\t\3\60\2\3")
        buf.write("\61\3\3\62\4\b\2\2\3A\5\3B\6\3C\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER = 1
    FLOAT = 2
    STRING = 3
    BOOLEAN = 4
    ARRAY = 5
    AUTO = 6
    OF = 7
    INHERIT = 8
    OUT = 9
    VOID = 10
    RETURN = 11
    FUNCTION = 12
    IF = 13
    ELSE = 14
    WHILE = 15
    FOR = 16
    DO = 17
    BREAK = 18
    CONTINUE = 19
    ADD = 20
    SUBSTRACT = 21
    DIVIDE = 22
    MULTIPLY = 23
    MODULO = 24
    NOTEQUAL = 25
    EQUAL = 26
    AND = 27
    OR = 28
    NOT = 29
    LESS = 30
    LEQ = 31
    GREATER = 32
    GEQ = 33
    STRING_CONCAT = 34
    LEFT_PARENTHESIS = 35
    RIGHT_PARENTHESIS = 36
    LEFT_SQUARE_BRACKET = 37
    RIGHT_SQUARE_BRACKET = 38
    LEFT_CURLY_BRACKET = 39
    RIGHT_CURLY_BRACKET = 40
    ASSIGN = 41
    COLON = 42
    COMMA = 43
    SEMI = 44
    DOT = 45
    IDENTIFIERS = 46
    INTLIT = 47
    FLOATLIT = 48
    STRINGLIT = 49
    BOOLIT = 50
    WS = 51
    BLOCKCOMMENT = 52
    INLINECOMMENT = 53
    ILLEGAL_ESCAPE = 54
    UNCLOSE_STRING = 55
    ERROR_CHAR = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'integer'", "'float'", "'string'", "'boolean'", "'array'", 
            "'auto'", "'of'", "'inherit'", "'out'", "'void'", "'return'", 
            "'function'", "'if'", "'else'", "'while'", "'for'", "'do'", 
            "'break'", "'continue'", "'+'", "'-'", "'/'", "'*'", "'%'", 
            "'!='", "'=='", "'&&'", "'||'", "'!'", "'<'", "'<='", "'>'", 
            "'>='", "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'='", 
            "':'", "','", "';'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "FLOAT", "STRING", "BOOLEAN", "ARRAY", "AUTO", "OF", 
            "INHERIT", "OUT", "VOID", "RETURN", "FUNCTION", "IF", "ELSE", 
            "WHILE", "FOR", "DO", "BREAK", "CONTINUE", "ADD", "SUBSTRACT", 
            "DIVIDE", "MULTIPLY", "MODULO", "NOTEQUAL", "EQUAL", "AND", 
            "OR", "NOT", "LESS", "LEQ", "GREATER", "GEQ", "STRING_CONCAT", 
            "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", 
            "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
            "ASSIGN", "COLON", "COMMA", "SEMI", "DOT", "IDENTIFIERS", "INTLIT", 
            "FLOATLIT", "STRINGLIT", "BOOLIT", "WS", "BLOCKCOMMENT", "INLINECOMMENT", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "INTEGER", "FLOAT", "STRING", "BOOLEAN", "ARRAY", "AUTO", 
                  "OF", "INHERIT", "OUT", "VOID", "RETURN", "FUNCTION", 
                  "IF", "ELSE", "WHILE", "FOR", "DO", "BREAK", "CONTINUE", 
                  "ADD", "SUBSTRACT", "DIVIDE", "MULTIPLY", "MODULO", "NOTEQUAL", 
                  "EQUAL", "AND", "OR", "NOT", "LESS", "LEQ", "GREATER", 
                  "GEQ", "STRING_CONCAT", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                  "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", 
                  "RIGHT_CURLY_BRACKET", "ASSIGN", "COLON", "COMMA", "SEMI", 
                  "DOT", "IDENTIFIERS", "INTLIT", "FLOATLIT", "STRINGLIT", 
                  "BOOLIT", "ZeroDigits", "NonZeroDigits", "UNDERSCORED", 
                  "DoubleQuote", "StringChar", "EscapeSeqs", "Illegal_ESCSeq", 
                  "ExpPart", "DecPart", "IntPart", "WS", "BLOCKCOMMENT", 
                  "INLINECOMMENT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[46] = self.INTLIT_action 
            actions[47] = self.FLOATLIT_action 
            actions[48] = self.STRINGLIT_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            					self.text = self.text.replace('_', '')
            				
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            					self.text = self.text.replace('_', '')
            				
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	text = str(self.text)
            	raise IllegalEscape(text[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    unclose_str = str(self.text)
                    possible = '\n'
                    if unclose_str[-1] in possible:
                        raise UncloseString(unclose_str[1:-1])
                    else:
                        raise UncloseString(unclose_str[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise ErrorToken(self.text)

     


