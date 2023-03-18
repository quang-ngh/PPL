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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01d6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0150")
        buf.write("\n\62\3\62\3\62\3\63\3\63\3\63\7\63\u0157\n\63\f\63\16")
        buf.write("\63\u015a\13\63\3\63\3\63\3\63\3\64\3\64\7\64\u0161\n")
        buf.write("\64\f\64\16\64\u0164\13\64\3\65\3\65\3\66\3\66\3\67\3")
        buf.write("\67\38\38\39\39\3:\3:\3:\3;\3;\3;\3;\5;\u0177\n;\3<\3")
        buf.write("<\5<\u017b\n<\3<\6<\u017e\n<\r<\16<\u017f\3=\3=\7=\u0184")
        buf.write("\n=\f=\16=\u0187\13=\3>\3>\3>\7>\u018c\n>\f>\16>\u018f")
        buf.write("\13>\3>\5>\u0192\n>\3>\7>\u0195\n>\f>\16>\u0198\13>\5")
        buf.write(">\u019a\n>\3?\6?\u019d\n?\r?\16?\u019e\3?\3?\3@\3@\3@")
        buf.write("\3@\7@\u01a7\n@\f@\16@\u01aa\13@\3@\3@\3@\3@\3@\3A\3A")
        buf.write("\3A\3A\7A\u01b5\nA\fA\16A\u01b8\13A\3A\3A\3B\3B\3B\7B")
        buf.write("\u01bf\nB\fB\16B\u01c2\13B\3B\3B\3B\3C\3C\3C\7C\u01ca")
        buf.write("\nC\fC\16C\u01cd\13C\3C\5C\u01d0\nC\3C\3C\3D\3D\3D\3\u01a8")
        buf.write("\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\2k\2m\2o\2q")
        buf.write("\2s\2u\2w\2y\2{\2}\66\177\67\u00818\u00839\u0085:\u0087")
        buf.write(";\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\5\2")
        buf.write("\f\f$$^^\n\2$$))^^ddhhppttvv\3\2$$\4\2GGgg\4\2--//\3\2")
        buf.write("\60\60\3\2\62\62\5\2\n\f\16\17\"\"\4\2\f\f\17\17\3\3\f")
        buf.write("\f\2\u01e0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
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
        buf.write("\3\2\2\2\2g\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2")
        buf.write("\3\u0089\3\2\2\2\5\u0091\3\2\2\2\7\u0097\3\2\2\2\t\u009e")
        buf.write("\3\2\2\2\13\u00a6\3\2\2\2\r\u00ac\3\2\2\2\17\u00b1\3\2")
        buf.write("\2\2\21\u00b4\3\2\2\2\23\u00bc\3\2\2\2\25\u00c0\3\2\2")
        buf.write("\2\27\u00c5\3\2\2\2\31\u00cc\3\2\2\2\33\u00d5\3\2\2\2")
        buf.write("\35\u00d8\3\2\2\2\37\u00dd\3\2\2\2!\u00e3\3\2\2\2#\u00e7")
        buf.write("\3\2\2\2%\u00ea\3\2\2\2\'\u00f0\3\2\2\2)\u00f9\3\2\2\2")
        buf.write("+\u00fb\3\2\2\2-\u00fd\3\2\2\2/\u00ff\3\2\2\2\61\u0101")
        buf.write("\3\2\2\2\63\u0103\3\2\2\2\65\u0106\3\2\2\2\67\u0109\3")
        buf.write("\2\2\29\u010c\3\2\2\2;\u010f\3\2\2\2=\u0111\3\2\2\2?\u0113")
        buf.write("\3\2\2\2A\u0116\3\2\2\2C\u0118\3\2\2\2E\u011b\3\2\2\2")
        buf.write("G\u011e\3\2\2\2I\u0120\3\2\2\2K\u0122\3\2\2\2M\u0124\3")
        buf.write("\2\2\2O\u0126\3\2\2\2Q\u0128\3\2\2\2S\u012a\3\2\2\2U\u012c")
        buf.write("\3\2\2\2W\u012e\3\2\2\2Y\u0130\3\2\2\2[\u0132\3\2\2\2")
        buf.write("]\u0134\3\2\2\2_\u0139\3\2\2\2a\u013f\3\2\2\2c\u014f\3")
        buf.write("\2\2\2e\u0153\3\2\2\2g\u015e\3\2\2\2i\u0165\3\2\2\2k\u0167")
        buf.write("\3\2\2\2m\u0169\3\2\2\2o\u016b\3\2\2\2q\u016d\3\2\2\2")
        buf.write("s\u016f\3\2\2\2u\u0176\3\2\2\2w\u0178\3\2\2\2y\u0181\3")
        buf.write("\2\2\2{\u0199\3\2\2\2}\u019c\3\2\2\2\177\u01a2\3\2\2\2")
        buf.write("\u0081\u01b0\3\2\2\2\u0083\u01bb\3\2\2\2\u0085\u01c6\3")
        buf.write("\2\2\2\u0087\u01d3\3\2\2\2\u0089\u008a\7k\2\2\u008a\u008b")
        buf.write("\7p\2\2\u008b\u008c\7v\2\2\u008c\u008d\7g\2\2\u008d\u008e")
        buf.write("\7i\2\2\u008e\u008f\7g\2\2\u008f\u0090\7t\2\2\u0090\4")
        buf.write("\3\2\2\2\u0091\u0092\7h\2\2\u0092\u0093\7n\2\2\u0093\u0094")
        buf.write("\7q\2\2\u0094\u0095\7c\2\2\u0095\u0096\7v\2\2\u0096\6")
        buf.write("\3\2\2\2\u0097\u0098\7u\2\2\u0098\u0099\7v\2\2\u0099\u009a")
        buf.write("\7t\2\2\u009a\u009b\7k\2\2\u009b\u009c\7p\2\2\u009c\u009d")
        buf.write("\7i\2\2\u009d\b\3\2\2\2\u009e\u009f\7d\2\2\u009f\u00a0")
        buf.write("\7q\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3")
        buf.write("\7g\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5\7p\2\2\u00a5\n")
        buf.write("\3\2\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9")
        buf.write("\7t\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7{\2\2\u00ab\f")
        buf.write("\3\2\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af")
        buf.write("\7v\2\2\u00af\u00b0\7q\2\2\u00b0\16\3\2\2\2\u00b1\u00b2")
        buf.write("\7q\2\2\u00b2\u00b3\7h\2\2\u00b3\20\3\2\2\2\u00b4\u00b5")
        buf.write("\7k\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7\7j\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\22\3\2\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be")
        buf.write("\7w\2\2\u00be\u00bf\7v\2\2\u00bf\24\3\2\2\2\u00c0\u00c1")
        buf.write("\7x\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7f\2\2\u00c4\26\3\2\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7p\2\2\u00cb\30\3\2\2\2\u00cc\u00cd")
        buf.write("\7h\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7e\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\u00d4\7p\2\2\u00d4\32\3\2\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7h\2\2\u00d7\34\3\2\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7u\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\36\3\2\2\2\u00dd\u00de\7y\2\2\u00de\u00df")
        buf.write("\7j\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2")
        buf.write("\7g\2\2\u00e2 \3\2\2\2\u00e3\u00e4\7h\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7t\2\2\u00e6\"\3\2\2\2\u00e7\u00e8")
        buf.write("\7f\2\2\u00e8\u00e9\7q\2\2\u00e9$\3\2\2\2\u00ea\u00eb")
        buf.write("\7d\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee")
        buf.write("\7c\2\2\u00ee\u00ef\7m\2\2\u00ef&\3\2\2\2\u00f0\u00f1")
        buf.write("\7e\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7w\2\2\u00f7\u00f8\7g\2\2\u00f8(\3\2\2\2\u00f9\u00fa")
        buf.write("\7-\2\2\u00fa*\3\2\2\2\u00fb\u00fc\7/\2\2\u00fc,\3\2\2")
        buf.write("\2\u00fd\u00fe\7\61\2\2\u00fe.\3\2\2\2\u00ff\u0100\7,")
        buf.write("\2\2\u0100\60\3\2\2\2\u0101\u0102\7\'\2\2\u0102\62\3\2")
        buf.write("\2\2\u0103\u0104\7#\2\2\u0104\u0105\7?\2\2\u0105\64\3")
        buf.write("\2\2\2\u0106\u0107\7?\2\2\u0107\u0108\7?\2\2\u0108\66")
        buf.write("\3\2\2\2\u0109\u010a\7(\2\2\u010a\u010b\7(\2\2\u010b8")
        buf.write("\3\2\2\2\u010c\u010d\7~\2\2\u010d\u010e\7~\2\2\u010e:")
        buf.write("\3\2\2\2\u010f\u0110\7#\2\2\u0110<\3\2\2\2\u0111\u0112")
        buf.write("\7>\2\2\u0112>\3\2\2\2\u0113\u0114\7>\2\2\u0114\u0115")
        buf.write("\7?\2\2\u0115@\3\2\2\2\u0116\u0117\7@\2\2\u0117B\3\2\2")
        buf.write("\2\u0118\u0119\7@\2\2\u0119\u011a\7?\2\2\u011aD\3\2\2")
        buf.write("\2\u011b\u011c\7<\2\2\u011c\u011d\7<\2\2\u011dF\3\2\2")
        buf.write("\2\u011e\u011f\7*\2\2\u011fH\3\2\2\2\u0120\u0121\7+\2")
        buf.write("\2\u0121J\3\2\2\2\u0122\u0123\7]\2\2\u0123L\3\2\2\2\u0124")
        buf.write("\u0125\7_\2\2\u0125N\3\2\2\2\u0126\u0127\7}\2\2\u0127")
        buf.write("P\3\2\2\2\u0128\u0129\7\177\2\2\u0129R\3\2\2\2\u012a\u012b")
        buf.write("\7?\2\2\u012bT\3\2\2\2\u012c\u012d\7<\2\2\u012dV\3\2\2")
        buf.write("\2\u012e\u012f\7.\2\2\u012fX\3\2\2\2\u0130\u0131\7=\2")
        buf.write("\2\u0131Z\3\2\2\2\u0132\u0133\7\60\2\2\u0133\\\3\2\2\2")
        buf.write("\u0134\u0135\7v\2\2\u0135\u0136\7t\2\2\u0136\u0137\7w")
        buf.write("\2\2\u0137\u0138\7g\2\2\u0138^\3\2\2\2\u0139\u013a\7h")
        buf.write("\2\2\u013a\u013b\7c\2\2\u013b\u013c\7n\2\2\u013c\u013d")
        buf.write("\7u\2\2\u013d\u013e\7g\2\2\u013e`\3\2\2\2\u013f\u0140")
        buf.write("\5{>\2\u0140\u0141\b\61\2\2\u0141b\3\2\2\2\u0142\u0143")
        buf.write("\5{>\2\u0143\u0144\5y=\2\u0144\u0150\3\2\2\2\u0145\u0146")
        buf.write("\5{>\2\u0146\u0147\5w<\2\u0147\u0150\3\2\2\2\u0148\u0149")
        buf.write("\5y=\2\u0149\u014a\5w<\2\u014a\u0150\3\2\2\2\u014b\u014c")
        buf.write("\5{>\2\u014c\u014d\5y=\2\u014d\u014e\5w<\2\u014e\u0150")
        buf.write("\3\2\2\2\u014f\u0142\3\2\2\2\u014f\u0145\3\2\2\2\u014f")
        buf.write("\u0148\3\2\2\2\u014f\u014b\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151\u0152\b\62\3\2\u0152d\3\2\2\2\u0153\u0158\7$\2")
        buf.write("\2\u0154\u0157\5q9\2\u0155\u0157\5s:\2\u0156\u0154\3\2")
        buf.write("\2\2\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b\3\2\2\2\u015a")
        buf.write("\u0158\3\2\2\2\u015b\u015c\7$\2\2\u015c\u015d\b\63\4\2")
        buf.write("\u015df\3\2\2\2\u015e\u0162\t\2\2\2\u015f\u0161\t\3\2")
        buf.write("\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163h\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0165\u0166\t\4\2\2\u0166j\3\2\2\2\u0167\u0168")
        buf.write("\t\5\2\2\u0168l\3\2\2\2\u0169\u016a\7a\2\2\u016an\3\2")
        buf.write("\2\2\u016b\u016c\7$\2\2\u016cp\3\2\2\2\u016d\u016e\n\6")
        buf.write("\2\2\u016er\3\2\2\2\u016f\u0170\7^\2\2\u0170\u0171\t\7")
        buf.write("\2\2\u0171t\3\2\2\2\u0172\u0173\7^\2\2\u0173\u0177\n\7")
        buf.write("\2\2\u0174\u0175\7)\2\2\u0175\u0177\n\b\2\2\u0176\u0172")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0177v\3\2\2\2\u0178\u017a")
        buf.write("\t\t\2\2\u0179\u017b\t\n\2\2\u017a\u0179\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u017e\5i\65\2")
        buf.write("\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d\3")
        buf.write("\2\2\2\u017f\u0180\3\2\2\2\u0180x\3\2\2\2\u0181\u0185")
        buf.write("\t\13\2\2\u0182\u0184\5i\65\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186z\3\2\2\2\u0187\u0185\3\2\2\2\u0188\u019a\t\f\2")
        buf.write("\2\u0189\u018d\5k\66\2\u018a\u018c\5i\65\2\u018b\u018a")
        buf.write("\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018e\u0196\3\2\2\2\u018f\u018d\3\2\2\2")
        buf.write("\u0190\u0192\5m\67\2\u0191\u0190\3\2\2\2\u0191\u0192\3")
        buf.write("\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195\5i\65\2\u0194\u0191")
        buf.write("\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196")
        buf.write("\u0197\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2")
        buf.write("\u0199\u0188\3\2\2\2\u0199\u0189\3\2\2\2\u019a|\3\2\2")
        buf.write("\2\u019b\u019d\t\r\2\2\u019c\u019b\3\2\2\2\u019d\u019e")
        buf.write("\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a1\b?\5\2\u01a1~\3\2\2\2\u01a2")
        buf.write("\u01a3\7\61\2\2\u01a3\u01a4\7,\2\2\u01a4\u01a8\3\2\2\2")
        buf.write("\u01a5\u01a7\13\2\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9")
        buf.write("\u01ab\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\7,\2\2")
        buf.write("\u01ac\u01ad\7\61\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af")
        buf.write("\b@\5\2\u01af\u0080\3\2\2\2\u01b0\u01b1\7\61\2\2\u01b1")
        buf.write("\u01b2\7\61\2\2\u01b2\u01b6\3\2\2\2\u01b3\u01b5\n\16\2")
        buf.write("\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b9\3\2\2\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b9\u01ba\bA\5\2\u01ba\u0082\3\2\2\2")
        buf.write("\u01bb\u01c0\5o8\2\u01bc\u01bf\5q9\2\u01bd\u01bf\5s:\2")
        buf.write("\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c2\3")
        buf.write("\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c3")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c4\5u;\2\u01c4\u01c5")
        buf.write("\bB\6\2\u01c5\u0084\3\2\2\2\u01c6\u01cb\7$\2\2\u01c7\u01ca")
        buf.write("\5q9\2\u01c8\u01ca\5s:\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01ce\u01d0\t\17\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1")
        buf.write("\3\2\2\2\u01d1\u01d2\bC\7\2\u01d2\u0086\3\2\2\2\u01d3")
        buf.write("\u01d4\13\2\2\2\u01d4\u01d5\bD\b\2\u01d5\u0088\3\2\2\2")
        buf.write("\27\2\u014f\u0156\u0158\u0162\u0176\u017a\u017f\u0185")
        buf.write("\u018d\u0191\u0196\u0199\u019e\u01a8\u01b6\u01be\u01c0")
        buf.write("\u01c9\u01cb\u01cf\t\3\61\2\3\62\3\3\63\4\b\2\2\3B\5\3")
        buf.write("C\6\3D\7")
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
    TRUE = 46
    FALSE = 47
    INTLIT = 48
    FLOATLIT = 49
    STRINGLIT = 50
    IDENTIFIERS = 51
    WS = 52
    BLOCKCOMMENT = 53
    INLINECOMMENT = 54
    ILLEGAL_ESCAPE = 55
    UNCLOSE_STRING = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'integer'", "'float'", "'string'", "'boolean'", "'array'", 
            "'auto'", "'of'", "'inherit'", "'out'", "'void'", "'return'", 
            "'function'", "'if'", "'else'", "'while'", "'for'", "'do'", 
            "'break'", "'continue'", "'+'", "'-'", "'/'", "'*'", "'%'", 
            "'!='", "'=='", "'&&'", "'||'", "'!'", "'<'", "'<='", "'>'", 
            "'>='", "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'='", 
            "':'", "','", "';'", "'.'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "FLOAT", "STRING", "BOOLEAN", "ARRAY", "AUTO", "OF", 
            "INHERIT", "OUT", "VOID", "RETURN", "FUNCTION", "IF", "ELSE", 
            "WHILE", "FOR", "DO", "BREAK", "CONTINUE", "ADD", "SUBSTRACT", 
            "DIVIDE", "MULTIPLY", "MODULO", "NOTEQUAL", "EQUAL", "AND", 
            "OR", "NOT", "LESS", "LEQ", "GREATER", "GEQ", "STRING_CONCAT", 
            "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", 
            "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
            "ASSIGN", "COLON", "COMMA", "SEMI", "DOT", "TRUE", "FALSE", 
            "INTLIT", "FLOATLIT", "STRINGLIT", "IDENTIFIERS", "WS", "BLOCKCOMMENT", 
            "INLINECOMMENT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "INTEGER", "FLOAT", "STRING", "BOOLEAN", "ARRAY", "AUTO", 
                  "OF", "INHERIT", "OUT", "VOID", "RETURN", "FUNCTION", 
                  "IF", "ELSE", "WHILE", "FOR", "DO", "BREAK", "CONTINUE", 
                  "ADD", "SUBSTRACT", "DIVIDE", "MULTIPLY", "MODULO", "NOTEQUAL", 
                  "EQUAL", "AND", "OR", "NOT", "LESS", "LEQ", "GREATER", 
                  "GEQ", "STRING_CONCAT", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                  "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", 
                  "RIGHT_CURLY_BRACKET", "ASSIGN", "COLON", "COMMA", "SEMI", 
                  "DOT", "TRUE", "FALSE", "INTLIT", "FLOATLIT", "STRINGLIT", 
                  "IDENTIFIERS", "ZeroDigits", "NonZeroDigits", "UNDERSCORED", 
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
            actions[47] = self.INTLIT_action 
            actions[48] = self.FLOATLIT_action 
            actions[49] = self.STRINGLIT_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ERROR_CHAR_action 
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

     


