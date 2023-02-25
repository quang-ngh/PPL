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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29")
        buf.write("\u01ce\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\2\7\2\u008c\n\2\f\2\16\2\u008f\13\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009a\n\3\f\3\16")
        buf.write("\3\u009d\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*")
        buf.write("\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\7\60\u014a")
        buf.write("\n\60\f\60\16\60\u014d\13\60\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\7\62\u0155\n\62\f\62\16\62\u0158\13\62\3\62\5\62")
        buf.write("\u015b\n\62\3\62\3\62\3\63\3\63\3\63\7\63\u0162\n\63\f")
        buf.write("\63\16\63\u0165\13\63\3\63\3\63\3\63\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\5\64\u0173\n\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\3")
        buf.write("<\3<\3<\3<\5<\u0189\n<\3=\3=\5=\u018d\n=\3=\6=\u0190\n")
        buf.write("=\r=\16=\u0191\3>\3>\7>\u0196\n>\f>\16>\u0199\13>\3?\3")
        buf.write("?\3?\7?\u019e\n?\f?\16?\u01a1\13?\3?\5?\u01a4\n?\3?\7")
        buf.write("?\u01a7\n?\f?\16?\u01aa\13?\5?\u01ac\n?\3@\6@\u01af\n")
        buf.write("@\r@\16@\u01b0\3@\3@\3A\3A\3A\3B\3B\7B\u01ba\nB\fB\16")
        buf.write("B\u01bd\13B\3B\5B\u01c0\nB\3B\3B\3C\3C\3C\7C\u01c7\nC")
        buf.write("\fC\16C\u01ca\13C\3C\3C\3C\3\u008d\2D\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2")
        buf.write("\177\66\u0081\67\u00838\u00859\3\2\21\4\2\f\f\17\17\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\t\2$$^^ddhhp")
        buf.write("pttvv\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2$$\4")
        buf.write("\2GGgg\4\2--//\3\2\60\60\3\2\62\62\5\2\n\f\16\17\"\"\6")
        buf.write("\3\n\f\16\17$$^^\2\u01d6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\3\u0087\3\2\2\2")
        buf.write("\5\u0095\3\2\2\2\7\u00a0\3\2\2\2\t\u00a8\3\2\2\2\13\u00ae")
        buf.write("\3\2\2\2\r\u00b5\3\2\2\2\17\u00bd\3\2\2\2\21\u00c3\3\2")
        buf.write("\2\2\23\u00c8\3\2\2\2\25\u00cb\3\2\2\2\27\u00d3\3\2\2")
        buf.write("\2\31\u00d8\3\2\2\2\33\u00df\3\2\2\2\35\u00e8\3\2\2\2")
        buf.write("\37\u00eb\3\2\2\2!\u00f0\3\2\2\2#\u00f6\3\2\2\2%\u00fa")
        buf.write("\3\2\2\2\'\u00fd\3\2\2\2)\u0103\3\2\2\2+\u010c\3\2\2\2")
        buf.write("-\u010e\3\2\2\2/\u0110\3\2\2\2\61\u0112\3\2\2\2\63\u0114")
        buf.write("\3\2\2\2\65\u0116\3\2\2\2\67\u0119\3\2\2\29\u011c\3\2")
        buf.write("\2\2;\u011f\3\2\2\2=\u0122\3\2\2\2?\u0124\3\2\2\2A\u0126")
        buf.write("\3\2\2\2C\u0129\3\2\2\2E\u012b\3\2\2\2G\u012e\3\2\2\2")
        buf.write("I\u0131\3\2\2\2K\u0133\3\2\2\2M\u0135\3\2\2\2O\u0137\3")
        buf.write("\2\2\2Q\u0139\3\2\2\2S\u013b\3\2\2\2U\u013d\3\2\2\2W\u013f")
        buf.write("\3\2\2\2Y\u0141\3\2\2\2[\u0143\3\2\2\2]\u0145\3\2\2\2")
        buf.write("_\u0147\3\2\2\2a\u014e\3\2\2\2c\u0151\3\2\2\2e\u015e\3")
        buf.write("\2\2\2g\u0172\3\2\2\2i\u0174\3\2\2\2k\u0176\3\2\2\2m\u0178")
        buf.write("\3\2\2\2o\u017b\3\2\2\2q\u017d\3\2\2\2s\u017f\3\2\2\2")
        buf.write("u\u0181\3\2\2\2w\u0188\3\2\2\2y\u018a\3\2\2\2{\u0193\3")
        buf.write("\2\2\2}\u01ab\3\2\2\2\177\u01ae\3\2\2\2\u0081\u01b4\3")
        buf.write("\2\2\2\u0083\u01b7\3\2\2\2\u0085\u01c3\3\2\2\2\u0087\u0088")
        buf.write("\7\61\2\2\u0088\u0089\7,\2\2\u0089\u008d\3\2\2\2\u008a")
        buf.write("\u008c\13\2\2\2\u008b\u008a\3\2\2\2\u008c\u008f\3\2\2")
        buf.write("\2\u008d\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u0090")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\7,\2\2\u0091")
        buf.write("\u0092\7\61\2\2\u0092\u0093\3\2\2\2\u0093\u0094\b\2\2")
        buf.write("\2\u0094\4\3\2\2\2\u0095\u0096\7\61\2\2\u0096\u0097\7")
        buf.write("\61\2\2\u0097\u009b\3\2\2\2\u0098\u009a\n\2\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009e\u009f\b\3\2\2\u009f\6\3\2\2\2\u00a0\u00a1")
        buf.write("\7k\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\7i\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\b\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa")
        buf.write("\7n\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\n\3\2\2\2\u00ae\u00af\7u\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3\u00b4\7i\2\2\u00b4\f\3\2\2\2\u00b5\u00b6")
        buf.write("\7d\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9")
        buf.write("\7n\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\16\3\2\2\2\u00bd\u00be\7c\2\2\u00be\u00bf")
        buf.write("\7t\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2")
        buf.write("\7{\2\2\u00c2\20\3\2\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5")
        buf.write("\7w\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7q\2\2\u00c7\22")
        buf.write("\3\2\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca\7h\2\2\u00ca\24")
        buf.write("\3\2\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7j\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1")
        buf.write("\7k\2\2\u00d1\u00d2\7v\2\2\u00d2\26\3\2\2\2\u00d3\u00d4")
        buf.write("\7x\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7f\2\2\u00d7\30\3\2\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd")
        buf.write("\7t\2\2\u00dd\u00de\7p\2\2\u00de\32\3\2\2\2\u00df\u00e0")
        buf.write("\7h\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7e\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6")
        buf.write("\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\34\3\2\2\2\u00e8\u00e9")
        buf.write("\7k\2\2\u00e9\u00ea\7h\2\2\u00ea\36\3\2\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef \3\2\2\2\u00f0\u00f1\7y\2\2\u00f1\u00f2")
        buf.write("\7j\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7n\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5\"\3\2\2\2\u00f6\u00f7\7h\2\2\u00f7\u00f8")
        buf.write("\7q\2\2\u00f8\u00f9\7t\2\2\u00f9$\3\2\2\2\u00fa\u00fb")
        buf.write("\7f\2\2\u00fb\u00fc\7q\2\2\u00fc&\3\2\2\2\u00fd\u00fe")
        buf.write("\7d\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7c\2\2\u0101\u0102\7m\2\2\u0102(\3\2\2\2\u0103\u0104")
        buf.write("\7e\2\2\u0104\u0105\7q\2\2\u0105\u0106\7p\2\2\u0106\u0107")
        buf.write("\7v\2\2\u0107\u0108\7k\2\2\u0108\u0109\7p\2\2\u0109\u010a")
        buf.write("\7w\2\2\u010a\u010b\7g\2\2\u010b*\3\2\2\2\u010c\u010d")
        buf.write("\7-\2\2\u010d,\3\2\2\2\u010e\u010f\7/\2\2\u010f.\3\2\2")
        buf.write("\2\u0110\u0111\7\61\2\2\u0111\60\3\2\2\2\u0112\u0113\7")
        buf.write(",\2\2\u0113\62\3\2\2\2\u0114\u0115\7\'\2\2\u0115\64\3")
        buf.write("\2\2\2\u0116\u0117\7#\2\2\u0117\u0118\7?\2\2\u0118\66")
        buf.write("\3\2\2\2\u0119\u011a\7?\2\2\u011a\u011b\7?\2\2\u011b8")
        buf.write("\3\2\2\2\u011c\u011d\7(\2\2\u011d\u011e\7(\2\2\u011e:")
        buf.write("\3\2\2\2\u011f\u0120\7~\2\2\u0120\u0121\7~\2\2\u0121<")
        buf.write("\3\2\2\2\u0122\u0123\7#\2\2\u0123>\3\2\2\2\u0124\u0125")
        buf.write("\7>\2\2\u0125@\3\2\2\2\u0126\u0127\7>\2\2\u0127\u0128")
        buf.write("\7?\2\2\u0128B\3\2\2\2\u0129\u012a\7@\2\2\u012aD\3\2\2")
        buf.write("\2\u012b\u012c\7@\2\2\u012c\u012d\7?\2\2\u012dF\3\2\2")
        buf.write("\2\u012e\u012f\7<\2\2\u012f\u0130\7<\2\2\u0130H\3\2\2")
        buf.write("\2\u0131\u0132\7*\2\2\u0132J\3\2\2\2\u0133\u0134\7+\2")
        buf.write("\2\u0134L\3\2\2\2\u0135\u0136\7]\2\2\u0136N\3\2\2\2\u0137")
        buf.write("\u0138\7_\2\2\u0138P\3\2\2\2\u0139\u013a\7}\2\2\u013a")
        buf.write("R\3\2\2\2\u013b\u013c\7\177\2\2\u013cT\3\2\2\2\u013d\u013e")
        buf.write("\7?\2\2\u013eV\3\2\2\2\u013f\u0140\7<\2\2\u0140X\3\2\2")
        buf.write("\2\u0141\u0142\7.\2\2\u0142Z\3\2\2\2\u0143\u0144\7=\2")
        buf.write("\2\u0144\\\3\2\2\2\u0145\u0146\7\60\2\2\u0146^\3\2\2\2")
        buf.write("\u0147\u014b\t\3\2\2\u0148\u014a\t\4\2\2\u0149\u0148\3")
        buf.write("\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014c`\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f")
        buf.write("\5}?\2\u014f\u0150\b\61\3\2\u0150b\3\2\2\2\u0151\u015a")
        buf.write("\5}?\2\u0152\u0156\5{>\2\u0153\u0155\5y=\2\u0154\u0153")
        buf.write("\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157\u015b\3\2\2\2\u0158\u0156\3\2\2\2")
        buf.write("\u0159\u015b\5y=\2\u015a\u0152\3\2\2\2\u015a\u0159\3\2")
        buf.write("\2\2\u015b\u015c\3\2\2\2\u015c\u015d\b\62\4\2\u015dd\3")
        buf.write("\2\2\2\u015e\u0163\5q9\2\u015f\u0162\5s:\2\u0160\u0162")
        buf.write("\5m\67\2\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0164\u0166\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0167\5")
        buf.write("q9\2\u0167\u0168\b\63\5\2\u0168f\3\2\2\2\u0169\u016a\7")
        buf.write("v\2\2\u016a\u016b\7t\2\2\u016b\u016c\7w\2\2\u016c\u0173")
        buf.write("\7g\2\2\u016d\u016e\7h\2\2\u016e\u016f\7c\2\2\u016f\u0170")
        buf.write("\7n\2\2\u0170\u0171\7u\2\2\u0171\u0173\7g\2\2\u0172\u0169")
        buf.write("\3\2\2\2\u0172\u016d\3\2\2\2\u0173h\3\2\2\2\u0174\u0175")
        buf.write("\t\5\2\2\u0175j\3\2\2\2\u0176\u0177\t\6\2\2\u0177l\3\2")
        buf.write("\2\2\u0178\u0179\7^\2\2\u0179\u017a\t\7\2\2\u017an\3\2")
        buf.write("\2\2\u017b\u017c\7a\2\2\u017cp\3\2\2\2\u017d\u017e\7$")
        buf.write("\2\2\u017er\3\2\2\2\u017f\u0180\n\b\2\2\u0180t\3\2\2\2")
        buf.write("\u0181\u0182\7^\2\2\u0182\u0183\t\t\2\2\u0183v\3\2\2\2")
        buf.write("\u0184\u0185\7^\2\2\u0185\u0189\n\t\2\2\u0186\u0187\7")
        buf.write(")\2\2\u0187\u0189\n\n\2\2\u0188\u0184\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0189x\3\2\2\2\u018a\u018c\t\13\2\2\u018b\u018d")
        buf.write("\t\f\2\2\u018c\u018b\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("\u018f\3\2\2\2\u018e\u0190\5i\65\2\u018f\u018e\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3")
        buf.write("\2\2\2\u0192z\3\2\2\2\u0193\u0197\t\r\2\2\u0194\u0196")
        buf.write("\5i\65\2\u0195\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197")
        buf.write("\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198|\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u019a\u01ac\t\16\2\2\u019b\u019f\5k\66")
        buf.write("\2\u019c\u019e\5i\65\2\u019d\u019c\3\2\2\2\u019e\u01a1")
        buf.write("\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u01a8\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a4\5o8\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5\u01a7\5i\65\2\u01a6\u01a3\3\2\2\2\u01a7\u01aa\3")
        buf.write("\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ac")
        buf.write("\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u019a\3\2\2\2\u01ab")
        buf.write("\u019b\3\2\2\2\u01ac~\3\2\2\2\u01ad\u01af\t\17\2\2\u01ae")
        buf.write("\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b0\u01b1\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\b")
        buf.write("@\2\2\u01b3\u0080\3\2\2\2\u01b4\u01b5\13\2\2\2\u01b5\u01b6")
        buf.write("\bA\6\2\u01b6\u0082\3\2\2\2\u01b7\u01bb\5q9\2\u01b8\u01ba")
        buf.write("\5s:\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01be\u01c0\t\20\2\2\u01bf\u01be\3\2\2")
        buf.write("\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\bB\7\2\u01c2\u0084")
        buf.write("\3\2\2\2\u01c3\u01c8\5q9\2\u01c4\u01c7\5s:\2\u01c5\u01c7")
        buf.write("\5m\67\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7")
        buf.write("\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9\u01cb\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\5")
        buf.write("w<\2\u01cc\u01cd\bC\b\2\u01cd\u0086\3\2\2\2\30\2\u008d")
        buf.write("\u009b\u014b\u0156\u015a\u0161\u0163\u0172\u0188\u018c")
        buf.write("\u0191\u0197\u019f\u01a3\u01a8\u01ab\u01b0\u01bb\u01bf")
        buf.write("\u01c6\u01c8\t\b\2\2\3\61\2\3\62\3\3\63\4\3A\5\3B\6\3")
        buf.write("C\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCKCOMMENT = 1
    INLINECOMMENT = 2
    INTEGER = 3
    FLOAT = 4
    STRING = 5
    BOOLEAN = 6
    ARRAY = 7
    AUTO = 8
    OF = 9
    INHERIT = 10
    VOID = 11
    RETURN = 12
    FUNCTION = 13
    IF = 14
    ELSE = 15
    WHILE = 16
    FOR = 17
    DO = 18
    BREAK = 19
    CONTINUE = 20
    ADD = 21
    SUBSTRACT = 22
    DIVIDE = 23
    MULTIPLY = 24
    MODULO = 25
    NOTEQUAL = 26
    EQUAL = 27
    AND = 28
    OR = 29
    NOT = 30
    LESS = 31
    LEQ = 32
    GREATER = 33
    GEQ = 34
    STRING_CONCAT = 35
    LEFT_PARENTHESIS = 36
    RIGHT_PARENTHESIS = 37
    LEFT_SQUARE_BRACKET = 38
    RIGHT_SQUARE_BRACKET = 39
    LEFT_CURLY_BRACKET = 40
    RIGHT_CURLY_BRACKET = 41
    ASSIGN = 42
    COLON = 43
    COMMA = 44
    SEMI = 45
    DOT = 46
    IDENTIFIERS = 47
    INTLIT = 48
    FLOATLIT = 49
    STRINGLIT = 50
    BOOLIT = 51
    WS = 52
    ERROR_CHAR = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'integer'", "'float'", "'string'", "'boolean'", "'array'", 
            "'auto'", "'of'", "'inherit'", "'void'", "'return'", "'function'", 
            "'if'", "'else'", "'while'", "'for'", "'do'", "'break'", "'continue'", 
            "'+'", "'-'", "'/'", "'*'", "'%'", "'!='", "'=='", "'&&'", "'||'", 
            "'!'", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "'='", "':'", "','", "';'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCKCOMMENT", "INLINECOMMENT", "INTEGER", "FLOAT", "STRING", 
            "BOOLEAN", "ARRAY", "AUTO", "OF", "INHERIT", "VOID", "RETURN", 
            "FUNCTION", "IF", "ELSE", "WHILE", "FOR", "DO", "BREAK", "CONTINUE", 
            "ADD", "SUBSTRACT", "DIVIDE", "MULTIPLY", "MODULO", "NOTEQUAL", 
            "EQUAL", "AND", "OR", "NOT", "LESS", "LEQ", "GREATER", "GEQ", 
            "STRING_CONCAT", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", 
            "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
            "ASSIGN", "COLON", "COMMA", "SEMI", "DOT", "IDENTIFIERS", "INTLIT", 
            "FLOATLIT", "STRINGLIT", "BOOLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BLOCKCOMMENT", "INLINECOMMENT", "INTEGER", "FLOAT", "STRING", 
                  "BOOLEAN", "ARRAY", "AUTO", "OF", "INHERIT", "VOID", "RETURN", 
                  "FUNCTION", "IF", "ELSE", "WHILE", "FOR", "DO", "BREAK", 
                  "CONTINUE", "ADD", "SUBSTRACT", "DIVIDE", "MULTIPLY", 
                  "MODULO", "NOTEQUAL", "EQUAL", "AND", "OR", "NOT", "LESS", 
                  "LEQ", "GREATER", "GEQ", "STRING_CONCAT", "LEFT_PARENTHESIS", 
                  "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "ASSIGN", 
                  "COLON", "COMMA", "SEMI", "DOT", "IDENTIFIERS", "INTLIT", 
                  "FLOATLIT", "STRINGLIT", "BOOLIT", "ZeroDigits", "NonZeroDigits", 
                  "EscapeSeqs", "UNDERSCORED", "DoubleQuote", "StringChar", 
                  "ESCSeq", "Illegal_ESCSeq", "ExpPart", "DecPart", "IntPart", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[63] = self.ERROR_CHAR_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
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

            	string = str(self.text)
            	self.text = string[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    unclose_str = str(self.text)
                    possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
                    if unclose_str[-1] in possible:
                        raise UncloseString(unclose_str[1:-1])
                    else:
                        raise UncloseString(unclose_str[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	text = str(self.text)
            	raise IllegalEscape(text[1:])

     


