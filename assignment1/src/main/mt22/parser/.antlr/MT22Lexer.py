# Generated from /home/quangngcs/Desktop/Github/PPL/assignment1/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\u01c2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\7\4\u0098\n\4\f\4\16\4\u009b\13\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5\u00a6\n\5\f\5\16\5\u00a9")
        buf.write("\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3")
        buf.write("&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\7\61\u0156\n")
        buf.write("\61\f\61\16\61\u0159\13\61\3\61\5\61\u015c\n\61\3\62\3")
        buf.write("\62\3\62\3\62\5\62\u0162\n\62\5\62\u0164\n\62\3\62\7\62")
        buf.write("\u0167\n\62\f\62\16\62\u016a\13\62\3\62\3\62\3\62\3\62")
        buf.write("\5\62\u0170\n\62\3\62\7\62\u0173\n\62\f\62\16\62\u0176")
        buf.write("\13\62\3\63\3\63\7\63\u017a\n\63\f\63\16\63\u017d\13\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\5\64\u018b\n\64\3\65\3\65\7\65\u018f\n\65\f\65\16")
        buf.write("\65\u0192\13\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:")
        buf.write("\3:\3;\3;\3<\3<\3=\3=\5=\u01a5\n=\3>\3>\3>\3?\6?\u01ab")
        buf.write("\n?\r?\16?\u01ac\3?\3?\3@\3@\3@\3A\3A\7A\u01b6\nA\fA\16")
        buf.write("A\u01b9\13A\3A\5A\u01bc\nA\3A\3A\3B\3B\3B\3\u0099\2C\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\2q\2s\2")
        buf.write("u\2w\2y\2{\2}\67\1778\u00819\u0083:\3\2\16\4\2\f\f\17")
        buf.write("\17\3\2\62\62\3\2\63;\4\2--//\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\4\2GGgg\3\2\62;\t\2$$^^ddhhppttvv\6\2\n\f\16\17$$^")
        buf.write("^\5\2\n\f\16\17\"\"\6\3\n\f\16\17$$^^\2\u01c9\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\3\u0085\3\2\2\2\5\u008e\3\2\2\2\7\u0093\3\2\2")
        buf.write("\2\t\u00a1\3\2\2\2\13\u00ac\3\2\2\2\r\u00b4\3\2\2\2\17")
        buf.write("\u00b9\3\2\2\2\21\u00c0\3\2\2\2\23\u00c9\3\2\2\2\25\u00cc")
        buf.write("\3\2\2\2\27\u00d1\3\2\2\2\31\u00d7\3\2\2\2\33\u00db\3")
        buf.write("\2\2\2\35\u00de\3\2\2\2\37\u00e4\3\2\2\2!\u00ed\3\2\2")
        buf.write("\2#\u00f5\3\2\2\2%\u00fb\3\2\2\2\'\u0102\3\2\2\2)\u010a")
        buf.write("\3\2\2\2+\u0110\3\2\2\2-\u0115\3\2\2\2/\u0118\3\2\2\2")
        buf.write("\61\u011a\3\2\2\2\63\u011c\3\2\2\2\65\u011e\3\2\2\2\67")
        buf.write("\u0120\3\2\2\29\u0122\3\2\2\2;\u0125\3\2\2\2=\u0128\3")
        buf.write("\2\2\2?\u012b\3\2\2\2A\u012e\3\2\2\2C\u0130\3\2\2\2E\u0132")
        buf.write("\3\2\2\2G\u0135\3\2\2\2I\u0137\3\2\2\2K\u013a\3\2\2\2")
        buf.write("M\u013d\3\2\2\2O\u013f\3\2\2\2Q\u0141\3\2\2\2S\u0143\3")
        buf.write("\2\2\2U\u0145\3\2\2\2W\u0147\3\2\2\2Y\u0149\3\2\2\2[\u014b")
        buf.write("\3\2\2\2]\u014d\3\2\2\2_\u014f\3\2\2\2a\u015b\3\2\2\2")
        buf.write("c\u015d\3\2\2\2e\u0177\3\2\2\2g\u018a\3\2\2\2i\u018c\3")
        buf.write("\2\2\2k\u0193\3\2\2\2m\u0195\3\2\2\2o\u0197\3\2\2\2q\u0199")
        buf.write("\3\2\2\2s\u019b\3\2\2\2u\u019e\3\2\2\2w\u01a0\3\2\2\2")
        buf.write("y\u01a4\3\2\2\2{\u01a6\3\2\2\2}\u01aa\3\2\2\2\177\u01b0")
        buf.write("\3\2\2\2\u0081\u01b3\3\2\2\2\u0083\u01bf\3\2\2\2\u0085")
        buf.write("\u0086\7h\2\2\u0086\u0087\7w\2\2\u0087\u0088\7p\2\2\u0088")
        buf.write("\u0089\7e\2\2\u0089\u008a\7f\2\2\u008a\u008b\7g\2\2\u008b")
        buf.write("\u008c\7e\2\2\u008c\u008d\7n\2\2\u008d\4\3\2\2\2\u008e")
        buf.write("\u008f\7G\2\2\u008f\u0090\7z\2\2\u0090\u0091\7r\2\2\u0091")
        buf.write("\u0092\7t\2\2\u0092\6\3\2\2\2\u0093\u0094\7\61\2\2\u0094")
        buf.write("\u0095\7,\2\2\u0095\u0099\3\2\2\2\u0096\u0098\13\2\2\2")
        buf.write("\u0097\u0096\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u009a\3")
        buf.write("\2\2\2\u0099\u0097\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099")
        buf.write("\3\2\2\2\u009c\u009d\7,\2\2\u009d\u009e\7\61\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\b\4\2\2\u00a0\b\3\2\2\2\u00a1")
        buf.write("\u00a2\7\61\2\2\u00a2\u00a3\7\61\2\2\u00a3\u00a7\3\2\2")
        buf.write("\2\u00a4\u00a6\n\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9")
        buf.write("\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\b\5\2\2")
        buf.write("\u00ab\n\3\2\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7p\2\2")
        buf.write("\u00ae\u00af\7j\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1\7t")
        buf.write("\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7v\2\2\u00b3\f\3\2")
        buf.write("\2\2\u00b4\u00b5\7x\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7f\2\2\u00b8\16\3\2\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd")
        buf.write("\7w\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7p\2\2\u00bf\20")
        buf.write("\3\2\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6")
        buf.write("\7k\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7p\2\2\u00c8\22")
        buf.write("\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7h\2\2\u00cb\24")
        buf.write("\3\2\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf")
        buf.write("\7u\2\2\u00cf\u00d0\7g\2\2\u00d0\26\3\2\2\2\u00d1\u00d2")
        buf.write("\7y\2\2\u00d2\u00d3\7j\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5")
        buf.write("\7n\2\2\u00d5\u00d6\7g\2\2\u00d6\30\3\2\2\2\u00d7\u00d8")
        buf.write("\7h\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7t\2\2\u00da\32")
        buf.write("\3\2\2\2\u00db\u00dc\7f\2\2\u00dc\u00dd\7q\2\2\u00dd\34")
        buf.write("\3\2\2\2\u00de\u00df\7d\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7m\2\2\u00e3\36")
        buf.write("\3\2\2\2\u00e4\u00e5\7e\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec\7g\2\2\u00ec \3")
        buf.write("\2\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7v\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7i\2\2\u00f2\u00f3")
        buf.write("\7g\2\2\u00f3\u00f4\7t\2\2\u00f4\"\3\2\2\2\u00f5\u00f6")
        buf.write("\7h\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7c\2\2\u00f9\u00fa\7v\2\2\u00fa$\3\2\2\2\u00fb\u00fc")
        buf.write("\7u\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7i\2\2\u0101&\3")
        buf.write("\2\2\2\u0102\u0103\7d\2\2\u0103\u0104\7q\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105\u0106\7n\2\2\u0106\u0107\7g\2\2\u0107\u0108")
        buf.write("\7c\2\2\u0108\u0109\7p\2\2\u0109(\3\2\2\2\u010a\u010b")
        buf.write("\7c\2\2\u010b\u010c\7t\2\2\u010c\u010d\7t\2\2\u010d\u010e")
        buf.write("\7c\2\2\u010e\u010f\7{\2\2\u010f*\3\2\2\2\u0110\u0111")
        buf.write("\7c\2\2\u0111\u0112\7w\2\2\u0112\u0113\7v\2\2\u0113\u0114")
        buf.write("\7q\2\2\u0114,\3\2\2\2\u0115\u0116\7q\2\2\u0116\u0117")
        buf.write("\7h\2\2\u0117.\3\2\2\2\u0118\u0119\7-\2\2\u0119\60\3\2")
        buf.write("\2\2\u011a\u011b\7/\2\2\u011b\62\3\2\2\2\u011c\u011d\7")
        buf.write("\61\2\2\u011d\64\3\2\2\2\u011e\u011f\7,\2\2\u011f\66\3")
        buf.write("\2\2\2\u0120\u0121\7\'\2\2\u01218\3\2\2\2\u0122\u0123")
        buf.write("\7#\2\2\u0123\u0124\7?\2\2\u0124:\3\2\2\2\u0125\u0126")
        buf.write("\7?\2\2\u0126\u0127\7?\2\2\u0127<\3\2\2\2\u0128\u0129")
        buf.write("\7(\2\2\u0129\u012a\7(\2\2\u012a>\3\2\2\2\u012b\u012c")
        buf.write("\7~\2\2\u012c\u012d\7~\2\2\u012d@\3\2\2\2\u012e\u012f")
        buf.write("\7#\2\2\u012fB\3\2\2\2\u0130\u0131\7>\2\2\u0131D\3\2\2")
        buf.write("\2\u0132\u0133\7>\2\2\u0133\u0134\7?\2\2\u0134F\3\2\2")
        buf.write("\2\u0135\u0136\7@\2\2\u0136H\3\2\2\2\u0137\u0138\7@\2")
        buf.write("\2\u0138\u0139\7?\2\2\u0139J\3\2\2\2\u013a\u013b\7<\2")
        buf.write("\2\u013b\u013c\7<\2\2\u013cL\3\2\2\2\u013d\u013e\7*\2")
        buf.write("\2\u013eN\3\2\2\2\u013f\u0140\7+\2\2\u0140P\3\2\2\2\u0141")
        buf.write("\u0142\7]\2\2\u0142R\3\2\2\2\u0143\u0144\7_\2\2\u0144")
        buf.write("T\3\2\2\2\u0145\u0146\7}\2\2\u0146V\3\2\2\2\u0147\u0148")
        buf.write("\7\177\2\2\u0148X\3\2\2\2\u0149\u014a\7?\2\2\u014aZ\3")
        buf.write("\2\2\2\u014b\u014c\7<\2\2\u014c\\\3\2\2\2\u014d\u014e")
        buf.write("\7.\2\2\u014e^\3\2\2\2\u014f\u0150\7=\2\2\u0150`\3\2\2")
        buf.write("\2\u0151\u015c\t\3\2\2\u0152\u0157\t\4\2\2\u0153\u0156")
        buf.write("\5q9\2\u0154\u0156\7a\2\2\u0155\u0153\3\2\2\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u015a\u015c\b\61\3\2\u015b\u0151\3\2\2\2\u015b\u0152")
        buf.write("\3\2\2\2\u015cb\3\2\2\2\u015d\u0163\5a\61\2\u015e\u0164")
        buf.write("\5m\67\2\u015f\u0161\5o8\2\u0160\u0162\t\5\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164\3\2\2\2\u0163")
        buf.write("\u015e\3\2\2\2\u0163\u015f\3\2\2\2\u0164\u0168\3\2\2\2")
        buf.write("\u0165\u0167\5q9\2\u0166\u0165\3\2\2\2\u0167\u016a\3\2")
        buf.write("\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016f")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u0170\5m\67\2\u016c")
        buf.write("\u016d\5o8\2\u016d\u016e\t\5\2\2\u016e\u0170\3\2\2\2\u016f")
        buf.write("\u016b\3\2\2\2\u016f\u016c\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0174\3\2\2\2\u0171\u0173\5q9\2\u0172\u0171\3\2")
        buf.write("\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175d\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u017b")
        buf.write("\5w<\2\u0178\u017a\5y=\2\u0179\u0178\3\2\2\2\u017a\u017d")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017e\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\5w<\2\u017f")
        buf.write("\u0180\b\63\4\2\u0180f\3\2\2\2\u0181\u0182\7v\2\2\u0182")
        buf.write("\u0183\7t\2\2\u0183\u0184\7w\2\2\u0184\u018b\7g\2\2\u0185")
        buf.write("\u0186\7h\2\2\u0186\u0187\7c\2\2\u0187\u0188\7n\2\2\u0188")
        buf.write("\u0189\7u\2\2\u0189\u018b\7g\2\2\u018a\u0181\3\2\2\2\u018a")
        buf.write("\u0185\3\2\2\2\u018bh\3\2\2\2\u018c\u0190\t\6\2\2\u018d")
        buf.write("\u018f\t\7\2\2\u018e\u018d\3\2\2\2\u018f\u0192\3\2\2\2")
        buf.write("\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191j\3\2\2")
        buf.write("\2\u0192\u0190\3\2\2\2\u0193\u0194\5a\61\2\u0194l\3\2")
        buf.write("\2\2\u0195\u0196\7\60\2\2\u0196n\3\2\2\2\u0197\u0198\t")
        buf.write("\b\2\2\u0198p\3\2\2\2\u0199\u019a\t\t\2\2\u019ar\3\2\2")
        buf.write("\2\u019b\u019c\7^\2\2\u019c\u019d\t\n\2\2\u019dt\3\2\2")
        buf.write("\2\u019e\u019f\t\b\2\2\u019fv\3\2\2\2\u01a0\u01a1\7$\2")
        buf.write("\2\u01a1x\3\2\2\2\u01a2\u01a5\n\13\2\2\u01a3\u01a5\5{")
        buf.write(">\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5z\3\2")
        buf.write("\2\2\u01a6\u01a7\7^\2\2\u01a7\u01a8\t\n\2\2\u01a8|\3\2")
        buf.write("\2\2\u01a9\u01ab\t\f\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac")
        buf.write("\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("\u01ae\3\2\2\2\u01ae\u01af\b?\2\2\u01af~\3\2\2\2\u01b0")
        buf.write("\u01b1\13\2\2\2\u01b1\u01b2\b@\5\2\u01b2\u0080\3\2\2\2")
        buf.write("\u01b3\u01b7\5w<\2\u01b4\u01b6\5y=\2\u01b5\u01b4\3\2\2")
        buf.write("\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba")
        buf.write("\u01bc\t\r\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01be\bA\6\2\u01be\u0082\3\2\2\2\u01bf\u01c0\13")
        buf.write("\2\2\2\u01c0\u01c1\bB\7\2\u01c1\u0084\3\2\2\2\24\2\u0099")
        buf.write("\u00a7\u0155\u0157\u015b\u0161\u0163\u0168\u016f\u0174")
        buf.write("\u017b\u018a\u0190\u01a4\u01ac\u01b7\u01bb\b\b\2\2\3\61")
        buf.write("\2\3\63\3\3@\4\3A\5\3B\6")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    BLOCKCOMMENT = 3
    INLINECOMMENT = 4
    INHERIT = 5
    VOID = 6
    RETURN = 7
    FUNCTION = 8
    IF = 9
    ELSE = 10
    WHILE = 11
    FOR = 12
    DO = 13
    BREAK = 14
    CONTINUE = 15
    INTEGER = 16
    FLOAT = 17
    STRING = 18
    BOOLEAN = 19
    ARRAY = 20
    AUTO = 21
    OF = 22
    ADD = 23
    SUBSTRACT = 24
    DIVIDE = 25
    MULTIPLY = 26
    MODULO = 27
    NOTEQUAL = 28
    EQUAL = 29
    AND = 30
    OR = 31
    NOT = 32
    LESS = 33
    LEQ = 34
    GREATER = 35
    GEQ = 36
    STRING_CONCAT = 37
    LEFT_PARENTHESIS = 38
    RIGHT_PARENTHESIS = 39
    LEFT_SQUARE_BRACKET = 40
    RIGHT_SQUARE_BRACKET = 41
    LEFT_CURLY_BRACKET = 42
    RIGHT_CURLY_BRACKET = 43
    ASSIGN = 44
    COLON = 45
    COMMA = 46
    SEMI = 47
    INTLIT = 48
    FLOATLIT = 49
    STRINGLIT = 50
    BOOLIT = 51
    IDENTIFIERS = 52
    WS = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'funcdecl'", "'Expr'", "'inherit'", "'void'", "'return'", "'function'", 
            "'if'", "'else'", "'while'", "'for'", "'do'", "'break'", "'continue'", 
            "'integer'", "'float'", "'string'", "'boolean'", "'array'", 
            "'auto'", "'of'", "'+'", "'-'", "'/'", "'*'", "'%'", "'!='", 
            "'=='", "'&&'", "'||'", "'!'", "'<'", "'<='", "'>'", "'>='", 
            "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'='", "':'", 
            "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCKCOMMENT", "INLINECOMMENT", "INHERIT", "VOID", "RETURN", 
            "FUNCTION", "IF", "ELSE", "WHILE", "FOR", "DO", "BREAK", "CONTINUE", 
            "INTEGER", "FLOAT", "STRING", "BOOLEAN", "ARRAY", "AUTO", "OF", 
            "ADD", "SUBSTRACT", "DIVIDE", "MULTIPLY", "MODULO", "NOTEQUAL", 
            "EQUAL", "AND", "OR", "NOT", "LESS", "LEQ", "GREATER", "GEQ", 
            "STRING_CONCAT", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", 
            "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
            "ASSIGN", "COLON", "COMMA", "SEMI", "INTLIT", "FLOATLIT", "STRINGLIT", 
            "BOOLIT", "IDENTIFIERS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "BLOCKCOMMENT", "INLINECOMMENT", "INHERIT", 
                  "VOID", "RETURN", "FUNCTION", "IF", "ELSE", "WHILE", "FOR", 
                  "DO", "BREAK", "CONTINUE", "INTEGER", "FLOAT", "STRING", 
                  "BOOLEAN", "ARRAY", "AUTO", "OF", "ADD", "SUBSTRACT", 
                  "DIVIDE", "MULTIPLY", "MODULO", "NOTEQUAL", "EQUAL", "AND", 
                  "OR", "NOT", "LESS", "LEQ", "GREATER", "GEQ", "STRING_CONCAT", 
                  "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", 
                  "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                  "ASSIGN", "COLON", "COMMA", "SEMI", "INTLIT", "FLOATLIT", 
                  "STRINGLIT", "BOOLIT", "IDENTIFIERS", "IntPart", "DOT", 
                  "ExpPart", "ZeroDigits", "EscapeSeqs", "Exp", "DoubleQuote", 
                  "StringChar", "ESCSeq", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[49] = self.STRINGLIT_action 
            actions[62] = self.ERROR_CHAR_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	string = str(self.text)
            	self.text = string[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    unclose_str = str(self.text)
                    possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
                    if unclose_str[-1] in possible:
                        raise UncloseString(unclose_str[1:-1])
                    else:
                        raise UncloseString(unclose_str[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise IllegalEscape(self.text)

     


