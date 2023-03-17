# Generated from /home/quangngcs/Desktop/Github/PPL/assignment1/target/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\7.\u012f\n.\f.\16.\u0132\13.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\5\60\u0144\n\60\3\60\3\60\3\61\3\61\3\61\7\61\u014b")
        buf.write("\n\61\f\61\16\61\u014e\13\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u015c\n\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\38\39\39\39\39\59\u016f\n9\3:\3:\5:\u0173\n:\3:\6:\u0176")
        buf.write("\n:\r:\16:\u0177\3;\3;\7;\u017c\n;\f;\16;\u017f\13;\3")
        buf.write("<\3<\3<\7<\u0184\n<\f<\16<\u0187\13<\3<\5<\u018a\n<\3")
        buf.write("<\7<\u018d\n<\f<\16<\u0190\13<\5<\u0192\n<\3=\6=\u0195")
        buf.write("\n=\r=\16=\u0196\3=\3=\3>\3>\3>\3>\7>\u019f\n>\f>\16>")
        buf.write("\u01a2\13>\3>\3>\3>\3>\3>\3?\3?\3?\3?\7?\u01ad\n?\f?\16")
        buf.write("?\u01b0\13?\3?\3?\3@\3@\3@\7@\u01b7\n@\f@\16@\u01ba\13")
        buf.write("@\3@\3@\3@\3A\3A\3A\7A\u01c2\nA\fA\16A\u01c5\13A\3A\5")
        buf.write("A\u01c8\nA\3A\3A\3B\3B\3B\3\u01a0\2C\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y\64{\65}\66")
        buf.write("\177\67\u00818\u00839\3\2\20\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\3\2\62;\3\2\63;\5\2\f\f$$^^\n\2$$))^^ddhhppttvv\3\2")
        buf.write("$$\4\2GGgg\4\2--//\3\2\60\60\3\2\62\62\5\2\n\f\16\17\"")
        buf.write("\"\4\2\f\f\17\17\3\3\f\f\2\u01d9\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2")
        buf.write("\2\5\u008d\3\2\2\2\7\u0093\3\2\2\2\t\u009a\3\2\2\2\13")
        buf.write("\u00a2\3\2\2\2\r\u00a8\3\2\2\2\17\u00ad\3\2\2\2\21\u00b0")
        buf.write("\3\2\2\2\23\u00b8\3\2\2\2\25\u00bd\3\2\2\2\27\u00c4\3")
        buf.write("\2\2\2\31\u00cd\3\2\2\2\33\u00d0\3\2\2\2\35\u00d5\3\2")
        buf.write("\2\2\37\u00db\3\2\2\2!\u00df\3\2\2\2#\u00e2\3\2\2\2%\u00e8")
        buf.write("\3\2\2\2\'\u00f1\3\2\2\2)\u00f3\3\2\2\2+\u00f5\3\2\2\2")
        buf.write("-\u00f7\3\2\2\2/\u00f9\3\2\2\2\61\u00fb\3\2\2\2\63\u00fe")
        buf.write("\3\2\2\2\65\u0101\3\2\2\2\67\u0104\3\2\2\29\u0107\3\2")
        buf.write("\2\2;\u0109\3\2\2\2=\u010b\3\2\2\2?\u010e\3\2\2\2A\u0110")
        buf.write("\3\2\2\2C\u0113\3\2\2\2E\u0116\3\2\2\2G\u0118\3\2\2\2")
        buf.write("I\u011a\3\2\2\2K\u011c\3\2\2\2M\u011e\3\2\2\2O\u0120\3")
        buf.write("\2\2\2Q\u0122\3\2\2\2S\u0124\3\2\2\2U\u0126\3\2\2\2W\u0128")
        buf.write("\3\2\2\2Y\u012a\3\2\2\2[\u012c\3\2\2\2]\u0133\3\2\2\2")
        buf.write("_\u0143\3\2\2\2a\u0147\3\2\2\2c\u015b\3\2\2\2e\u015d\3")
        buf.write("\2\2\2g\u015f\3\2\2\2i\u0161\3\2\2\2k\u0163\3\2\2\2m\u0165")
        buf.write("\3\2\2\2o\u0167\3\2\2\2q\u016e\3\2\2\2s\u0170\3\2\2\2")
        buf.write("u\u0179\3\2\2\2w\u0191\3\2\2\2y\u0194\3\2\2\2{\u019a\3")
        buf.write("\2\2\2}\u01a8\3\2\2\2\177\u01b3\3\2\2\2\u0081\u01be\3")
        buf.write("\2\2\2\u0083\u01cb\3\2\2\2\u0085\u0086\7k\2\2\u0086\u0087")
        buf.write("\7p\2\2\u0087\u0088\7v\2\2\u0088\u0089\7g\2\2\u0089\u008a")
        buf.write("\7i\2\2\u008a\u008b\7g\2\2\u008b\u008c\7t\2\2\u008c\4")
        buf.write("\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f\7n\2\2\u008f\u0090")
        buf.write("\7q\2\2\u0090\u0091\7c\2\2\u0091\u0092\7v\2\2\u0092\6")
        buf.write("\3\2\2\2\u0093\u0094\7u\2\2\u0094\u0095\7v\2\2\u0095\u0096")
        buf.write("\7t\2\2\u0096\u0097\7k\2\2\u0097\u0098\7p\2\2\u0098\u0099")
        buf.write("\7i\2\2\u0099\b\3\2\2\2\u009a\u009b\7d\2\2\u009b\u009c")
        buf.write("\7q\2\2\u009c\u009d\7q\2\2\u009d\u009e\7n\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7p\2\2\u00a1\n")
        buf.write("\3\2\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7{\2\2\u00a7\f")
        buf.write("\3\2\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7q\2\2\u00ac\16\3\2\2\2\u00ad\u00ae")
        buf.write("\7q\2\2\u00ae\u00af\7h\2\2\u00af\20\3\2\2\2\u00b0\u00b1")
        buf.write("\7k\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7j\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\22\3\2\2\2\u00b8\u00b9\7x\2\2\u00b9\u00ba")
        buf.write("\7q\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7f\2\2\u00bc\24")
        buf.write("\3\2\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\26\3\2\2\2\u00c4\u00c5\7h\2\2\u00c5\u00c6")
        buf.write("\7w\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8\7e\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\30\3\2\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7h\2\2\u00cf\32\3\2\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2")
        buf.write("\7n\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4\7g\2\2\u00d4\34")
        buf.write("\3\2\2\2\u00d5\u00d6\7y\2\2\u00d6\u00d7\7j\2\2\u00d7\u00d8")
        buf.write("\7k\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da\7g\2\2\u00da\36")
        buf.write("\3\2\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de \3\2\2\2\u00df\u00e0\7f\2\2\u00e0\u00e1")
        buf.write("\7q\2\2\u00e1\"\3\2\2\2\u00e2\u00e3\7d\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7m\2\2\u00e7$\3\2\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7w\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0&\3\2\2\2\u00f1\u00f2\7-\2\2\u00f2(\3\2\2")
        buf.write("\2\u00f3\u00f4\7/\2\2\u00f4*\3\2\2\2\u00f5\u00f6\7\61")
        buf.write("\2\2\u00f6,\3\2\2\2\u00f7\u00f8\7,\2\2\u00f8.\3\2\2\2")
        buf.write("\u00f9\u00fa\7\'\2\2\u00fa\60\3\2\2\2\u00fb\u00fc\7#\2")
        buf.write("\2\u00fc\u00fd\7?\2\2\u00fd\62\3\2\2\2\u00fe\u00ff\7?")
        buf.write("\2\2\u00ff\u0100\7?\2\2\u0100\64\3\2\2\2\u0101\u0102\7")
        buf.write("(\2\2\u0102\u0103\7(\2\2\u0103\66\3\2\2\2\u0104\u0105")
        buf.write("\7~\2\2\u0105\u0106\7~\2\2\u01068\3\2\2\2\u0107\u0108")
        buf.write("\7#\2\2\u0108:\3\2\2\2\u0109\u010a\7>\2\2\u010a<\3\2\2")
        buf.write("\2\u010b\u010c\7>\2\2\u010c\u010d\7?\2\2\u010d>\3\2\2")
        buf.write("\2\u010e\u010f\7@\2\2\u010f@\3\2\2\2\u0110\u0111\7@\2")
        buf.write("\2\u0111\u0112\7?\2\2\u0112B\3\2\2\2\u0113\u0114\7<\2")
        buf.write("\2\u0114\u0115\7<\2\2\u0115D\3\2\2\2\u0116\u0117\7*\2")
        buf.write("\2\u0117F\3\2\2\2\u0118\u0119\7+\2\2\u0119H\3\2\2\2\u011a")
        buf.write("\u011b\7]\2\2\u011bJ\3\2\2\2\u011c\u011d\7_\2\2\u011d")
        buf.write("L\3\2\2\2\u011e\u011f\7}\2\2\u011fN\3\2\2\2\u0120\u0121")
        buf.write("\7\177\2\2\u0121P\3\2\2\2\u0122\u0123\7?\2\2\u0123R\3")
        buf.write("\2\2\2\u0124\u0125\7<\2\2\u0125T\3\2\2\2\u0126\u0127\7")
        buf.write(".\2\2\u0127V\3\2\2\2\u0128\u0129\7=\2\2\u0129X\3\2\2\2")
        buf.write("\u012a\u012b\7\60\2\2\u012bZ\3\2\2\2\u012c\u0130\t\2\2")
        buf.write("\2\u012d\u012f\t\3\2\2\u012e\u012d\3\2\2\2\u012f\u0132")
        buf.write("\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write("\\\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0134\5w<\2\u0134")
        buf.write("\u0135\b/\2\2\u0135^\3\2\2\2\u0136\u0137\5w<\2\u0137\u0138")
        buf.write("\5u;\2\u0138\u0144\3\2\2\2\u0139\u013a\5w<\2\u013a\u013b")
        buf.write("\5s:\2\u013b\u0144\3\2\2\2\u013c\u013d\5u;\2\u013d\u013e")
        buf.write("\5s:\2\u013e\u0144\3\2\2\2\u013f\u0140\5w<\2\u0140\u0141")
        buf.write("\5u;\2\u0141\u0142\5s:\2\u0142\u0144\3\2\2\2\u0143\u0136")
        buf.write("\3\2\2\2\u0143\u0139\3\2\2\2\u0143\u013c\3\2\2\2\u0143")
        buf.write("\u013f\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\b\60\3")
        buf.write("\2\u0146`\3\2\2\2\u0147\u014c\7$\2\2\u0148\u014b\5m\67")
        buf.write("\2\u0149\u014b\5o8\2\u014a\u0148\3\2\2\2\u014a\u0149\3")
        buf.write("\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d")
        buf.write("\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2\u014f")
        buf.write("\u0150\7$\2\2\u0150\u0151\b\61\4\2\u0151b\3\2\2\2\u0152")
        buf.write("\u0153\7v\2\2\u0153\u0154\7t\2\2\u0154\u0155\7w\2\2\u0155")
        buf.write("\u015c\7g\2\2\u0156\u0157\7h\2\2\u0157\u0158\7c\2\2\u0158")
        buf.write("\u0159\7n\2\2\u0159\u015a\7u\2\2\u015a\u015c\7g\2\2\u015b")
        buf.write("\u0152\3\2\2\2\u015b\u0156\3\2\2\2\u015cd\3\2\2\2\u015d")
        buf.write("\u015e\t\4\2\2\u015ef\3\2\2\2\u015f\u0160\t\5\2\2\u0160")
        buf.write("h\3\2\2\2\u0161\u0162\7a\2\2\u0162j\3\2\2\2\u0163\u0164")
        buf.write("\7$\2\2\u0164l\3\2\2\2\u0165\u0166\n\6\2\2\u0166n\3\2")
        buf.write("\2\2\u0167\u0168\7^\2\2\u0168\u0169\t\7\2\2\u0169p\3\2")
        buf.write("\2\2\u016a\u016b\7^\2\2\u016b\u016f\n\7\2\2\u016c\u016d")
        buf.write("\7)\2\2\u016d\u016f\n\b\2\2\u016e\u016a\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016fr\3\2\2\2\u0170\u0172\t\t\2\2\u0171")
        buf.write("\u0173\t\n\2\2\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0175\3\2\2\2\u0174\u0176\5e\63\2\u0175\u0174\3")
        buf.write("\2\2\2\u0176\u0177\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u0178t\3\2\2\2\u0179\u017d\t\13\2\2\u017a\u017c")
        buf.write("\5e\63\2\u017b\u017a\3\2\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017ev\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0192\t\f\2\2\u0181\u0185\5g\64\2")
        buf.write("\u0182\u0184\5e\63\2\u0183\u0182\3\2\2\2\u0184\u0187\3")
        buf.write("\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u018e")
        buf.write("\3\2\2\2\u0187\u0185\3\2\2\2\u0188\u018a\5i\65\2\u0189")
        buf.write("\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u018d\5e\63\2\u018c\u0189\3\2\2\2\u018d\u0190\3")
        buf.write("\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0192")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0180\3\2\2\2\u0191")
        buf.write("\u0181\3\2\2\2\u0192x\3\2\2\2\u0193\u0195\t\r\2\2\u0194")
        buf.write("\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0194\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\b")
        buf.write("=\5\2\u0199z\3\2\2\2\u019a\u019b\7\61\2\2\u019b\u019c")
        buf.write("\7,\2\2\u019c\u01a0\3\2\2\2\u019d\u019f\13\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u01a1\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a1\u01a3\3\2\2\2\u01a2\u01a0\3")
        buf.write("\2\2\2\u01a3\u01a4\7,\2\2\u01a4\u01a5\7\61\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01a7\b>\5\2\u01a7|\3\2\2\2\u01a8\u01a9")
        buf.write("\7\61\2\2\u01a9\u01aa\7\61\2\2\u01aa\u01ae\3\2\2\2\u01ab")
        buf.write("\u01ad\n\16\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01b0\3\2\2")
        buf.write("\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\b?\5\2\u01b2")
        buf.write("~\3\2\2\2\u01b3\u01b8\5k\66\2\u01b4\u01b7\5m\67\2\u01b5")
        buf.write("\u01b7\5o8\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7")
        buf.write("\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2")
        buf.write("\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\5")
        buf.write("q9\2\u01bc\u01bd\b@\6\2\u01bd\u0080\3\2\2\2\u01be\u01c3")
        buf.write("\7$\2\2\u01bf\u01c2\5m\67\2\u01c0\u01c2\5o8\2\u01c1\u01bf")
        buf.write("\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c7\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c8\t\17\2\2\u01c7\u01c6")
        buf.write("\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\bA\7\2\u01ca")
        buf.write("\u0082\3\2\2\2\u01cb\u01cc\13\2\2\2\u01cc\u01cd\bB\b\2")
        buf.write("\u01cd\u0084\3\2\2\2\30\2\u0130\u0143\u014a\u014c\u015b")
        buf.write("\u016e\u0172\u0177\u017d\u0185\u0189\u018e\u0191\u0196")
        buf.write("\u01a0\u01ae\u01b6\u01b8\u01c1\u01c3\u01c7\t\3/\2\3\60")
        buf.write("\3\3\61\4\b\2\2\3@\5\3A\6\3B\7")
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
    VOID = 9
    RETURN = 10
    FUNCTION = 11
    IF = 12
    ELSE = 13
    WHILE = 14
    FOR = 15
    DO = 16
    BREAK = 17
    CONTINUE = 18
    ADD = 19
    SUBSTRACT = 20
    DIVIDE = 21
    MULTIPLY = 22
    MODULO = 23
    NOTEQUAL = 24
    EQUAL = 25
    AND = 26
    OR = 27
    NOT = 28
    LESS = 29
    LEQ = 30
    GREATER = 31
    GEQ = 32
    STRING_CONCAT = 33
    LEFT_PARENTHESIS = 34
    RIGHT_PARENTHESIS = 35
    LEFT_SQUARE_BRACKET = 36
    RIGHT_SQUARE_BRACKET = 37
    LEFT_CURLY_BRACKET = 38
    RIGHT_CURLY_BRACKET = 39
    ASSIGN = 40
    COLON = 41
    COMMA = 42
    SEMI = 43
    DOT = 44
    IDENTIFIERS = 45
    INTLIT = 46
    FLOATLIT = 47
    STRINGLIT = 48
    BOOLIT = 49
    WS = 50
    BLOCKCOMMENT = 51
    INLINECOMMENT = 52
    ILLEGAL_ESCAPE = 53
    UNCLOSE_STRING = 54
    ERROR_CHAR = 55

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
            "INTEGER", "FLOAT", "STRING", "BOOLEAN", "ARRAY", "AUTO", "OF", 
            "INHERIT", "VOID", "RETURN", "FUNCTION", "IF", "ELSE", "WHILE", 
            "FOR", "DO", "BREAK", "CONTINUE", "ADD", "SUBSTRACT", "DIVIDE", 
            "MULTIPLY", "MODULO", "NOTEQUAL", "EQUAL", "AND", "OR", "NOT", 
            "LESS", "LEQ", "GREATER", "GEQ", "STRING_CONCAT", "LEFT_PARENTHESIS", 
            "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
            "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "ASSIGN", "COLON", 
            "COMMA", "SEMI", "DOT", "IDENTIFIERS", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "BOOLIT", "WS", "BLOCKCOMMENT", "INLINECOMMENT", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "INTEGER", "FLOAT", "STRING", "BOOLEAN", "ARRAY", "AUTO", 
                  "OF", "INHERIT", "VOID", "RETURN", "FUNCTION", "IF", "ELSE", 
                  "WHILE", "FOR", "DO", "BREAK", "CONTINUE", "ADD", "SUBSTRACT", 
                  "DIVIDE", "MULTIPLY", "MODULO", "NOTEQUAL", "EQUAL", "AND", 
                  "OR", "NOT", "LESS", "LEQ", "GREATER", "GEQ", "STRING_CONCAT", 
                  "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_SQUARE_BRACKET", 
                  "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                  "ASSIGN", "COLON", "COMMA", "SEMI", "DOT", "IDENTIFIERS", 
                  "INTLIT", "FLOATLIT", "STRINGLIT", "BOOLIT", "ZeroDigits", 
                  "NonZeroDigits", "UNDERSCORED", "DoubleQuote", "StringChar", 
                  "EscapeSeqs", "Illegal_ESCSeq", "ExpPart", "DecPart", 
                  "IntPart", "WS", "BLOCKCOMMENT", "INLINECOMMENT", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

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
            actions[45] = self.INTLIT_action 
            actions[46] = self.FLOATLIT_action 
            actions[47] = self.STRINGLIT_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ERROR_CHAR_action 
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

     


