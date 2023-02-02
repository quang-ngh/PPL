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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2M")
        buf.write("\u01a4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\6\2\u009b\n\2\r\2\16\2\u009c\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\6\3\6\7\6\u00ab\n\6\f\6\16\6\u00ae")
        buf.write("\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00b9\n")
        buf.write("\7\f\7\16\7\u00bc\13\7\3\7\3\7\3\b\3\b\7\b\u00c2\n\b\f")
        buf.write("\b\16\b\u00c5\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?")
        buf.write("\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3")
        buf.write("H\3I\3I\3J\3J\3K\3K\3L\3L\3\u00ac\2M\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091")
        buf.write("J\u0093K\u0095L\u0097M\3\2 \5\2\n\f\16\17\"\"\4\2\f\f")
        buf.write("\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2cc\3\2dd\3\2ee\3\2")
        buf.write("ff\3\2gg\3\2hh\3\2ii\3\2jj\3\2kk\3\2ll\3\2mm\3\2nn\3\2")
        buf.write("oo\3\2pp\3\2qq\3\2rr\3\2ss\3\2tt\3\2uu\3\2vv\3\2ww\3\2")
        buf.write("xx\3\2yy\3\2zz\3\2{{\3\2||\2\u01a7\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u009a\3\2\2")
        buf.write("\2\5\u00a0\3\2\2\2\7\u00a2\3\2\2\2\t\u00a4\3\2\2\2\13")
        buf.write("\u00a6\3\2\2\2\r\u00b4\3\2\2\2\17\u00bf\3\2\2\2\21\u00c6")
        buf.write("\3\2\2\2\23\u00ce\3\2\2\2\25\u00d3\3\2\2\2\27\u00da\3")
        buf.write("\2\2\2\31\u00e3\3\2\2\2\33\u00e8\3\2\2\2\35\u00ee\3\2")
        buf.write("\2\2\37\u00f1\3\2\2\2!\u00f6\3\2\2\2#\u00fc\3\2\2\2%\u0100")
        buf.write("\3\2\2\2\'\u0103\3\2\2\2)\u0109\3\2\2\2+\u0112\3\2\2\2")
        buf.write("-\u011a\3\2\2\2/\u0120\3\2\2\2\61\u0127\3\2\2\2\63\u012f")
        buf.write("\3\2\2\2\65\u0135\3\2\2\2\67\u013a\3\2\2\29\u013d\3\2")
        buf.write("\2\2;\u013f\3\2\2\2=\u0141\3\2\2\2?\u0143\3\2\2\2A\u0145")
        buf.write("\3\2\2\2C\u0147\3\2\2\2E\u014a\3\2\2\2G\u014d\3\2\2\2")
        buf.write("I\u0150\3\2\2\2K\u0153\3\2\2\2M\u0155\3\2\2\2O\u0157\3")
        buf.write("\2\2\2Q\u015a\3\2\2\2S\u015c\3\2\2\2U\u015f\3\2\2\2W\u0162")
        buf.write("\3\2\2\2Y\u0164\3\2\2\2[\u0166\3\2\2\2]\u0168\3\2\2\2")
        buf.write("_\u016a\3\2\2\2a\u016c\3\2\2\2c\u016e\3\2\2\2e\u0170\3")
        buf.write("\2\2\2g\u0172\3\2\2\2i\u0174\3\2\2\2k\u0176\3\2\2\2m\u0178")
        buf.write("\3\2\2\2o\u017a\3\2\2\2q\u017c\3\2\2\2s\u017e\3\2\2\2")
        buf.write("u\u0180\3\2\2\2w\u0182\3\2\2\2y\u0184\3\2\2\2{\u0186\3")
        buf.write("\2\2\2}\u0188\3\2\2\2\177\u018a\3\2\2\2\u0081\u018c\3")
        buf.write("\2\2\2\u0083\u018e\3\2\2\2\u0085\u0190\3\2\2\2\u0087\u0192")
        buf.write("\3\2\2\2\u0089\u0194\3\2\2\2\u008b\u0196\3\2\2\2\u008d")
        buf.write("\u0198\3\2\2\2\u008f\u019a\3\2\2\2\u0091\u019c\3\2\2\2")
        buf.write("\u0093\u019e\3\2\2\2\u0095\u01a0\3\2\2\2\u0097\u01a2\3")
        buf.write("\2\2\2\u0099\u009b\t\2\2\2\u009a\u0099\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009f\b\2\2\2\u009f\4\3\2\2\2\u00a0")
        buf.write("\u00a1\13\2\2\2\u00a1\6\3\2\2\2\u00a2\u00a3\13\2\2\2\u00a3")
        buf.write("\b\3\2\2\2\u00a4\u00a5\13\2\2\2\u00a5\n\3\2\2\2\u00a6")
        buf.write("\u00a7\7\61\2\2\u00a7\u00a8\7,\2\2\u00a8\u00ac\3\2\2\2")
        buf.write("\u00a9\u00ab\13\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ae")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad")
        buf.write("\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\7,\2\2")
        buf.write("\u00b0\u00b1\7\61\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3")
        buf.write("\b\6\2\2\u00b3\f\3\2\2\2\u00b4\u00b5\7\61\2\2\u00b5\u00b6")
        buf.write("\7\61\2\2\u00b6\u00ba\3\2\2\2\u00b7\u00b9\n\3\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2")
        buf.write("\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3")
        buf.write("\2\2\2\u00bd\u00be\b\7\2\2\u00be\16\3\2\2\2\u00bf\u00c3")
        buf.write("\t\4\2\2\u00c0\u00c2\t\5\2\2\u00c1\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4\20\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\5u;")
        buf.write("\2\u00c7\u00c8\5\177@\2\u00c8\u00c9\5s:\2\u00c9\u00ca")
        buf.write("\5m\67\2\u00ca\u00cb\5\u0087D\2\u00cb\u00cc\5u;\2\u00cc")
        buf.write("\u00cd\5\u008bF\2\u00cd\22\3\2\2\2\u00ce\u00cf\5\u008f")
        buf.write("H\2\u00cf\u00d0\5\u0081A\2\u00d0\u00d1\5u;\2\u00d1\u00d2")
        buf.write("\5k\66\2\u00d2\24\3\2\2\2\u00d3\u00d4\5\u0087D\2\u00d4")
        buf.write("\u00d5\5m\67\2\u00d5\u00d6\5\u008bF\2\u00d6\u00d7\5\u008d")
        buf.write("G\2\u00d7\u00d8\5\u0087D\2\u00d8\u00d9\5\177@\2\u00d9")
        buf.write("\26\3\2\2\2\u00da\u00db\5o8\2\u00db\u00dc\5\u008dG\2\u00dc")
        buf.write("\u00dd\5\177@\2\u00dd\u00de\5i\65\2\u00de\u00df\5\u008b")
        buf.write("F\2\u00df\u00e0\5u;\2\u00e0\u00e1\5\u0081A\2\u00e1\u00e2")
        buf.write("\5\177@\2\u00e2\30\3\2\2\2\u00e3\u00e4\5\u008bF\2\u00e4")
        buf.write("\u00e5\5\u0087D\2\u00e5\u00e6\5\u008dG\2\u00e6\u00e7\5")
        buf.write("m\67\2\u00e7\32\3\2\2\2\u00e8\u00e9\5o8\2\u00e9\u00ea")
        buf.write("\5e\63\2\u00ea\u00eb\5{>\2\u00eb\u00ec\5\u0089E\2\u00ec")
        buf.write("\u00ed\5m\67\2\u00ed\34\3\2\2\2\u00ee\u00ef\5u;\2\u00ef")
        buf.write("\u00f0\5o8\2\u00f0\36\3\2\2\2\u00f1\u00f2\5m\67\2\u00f2")
        buf.write("\u00f3\5{>\2\u00f3\u00f4\5\u0089E\2\u00f4\u00f5\5m\67")
        buf.write("\2\u00f5 \3\2\2\2\u00f6\u00f7\5\u0091I\2\u00f7\u00f8\5")
        buf.write("s:\2\u00f8\u00f9\5u;\2\u00f9\u00fa\5{>\2\u00fa\u00fb\5")
        buf.write("m\67\2\u00fb\"\3\2\2\2\u00fc\u00fd\5o8\2\u00fd\u00fe\5")
        buf.write("\u0081A\2\u00fe\u00ff\5\u0087D\2\u00ff$\3\2\2\2\u0100")
        buf.write("\u0101\5k\66\2\u0101\u0102\5\u0081A\2\u0102&\3\2\2\2\u0103")
        buf.write("\u0104\5g\64\2\u0104\u0105\5\u0087D\2\u0105\u0106\5m\67")
        buf.write("\2\u0106\u0107\5e\63\2\u0107\u0108\5y=\2\u0108(\3\2\2")
        buf.write("\2\u0109\u010a\5i\65\2\u010a\u010b\5\u0081A\2\u010b\u010c")
        buf.write("\5\177@\2\u010c\u010d\5\u008bF\2\u010d\u010e\5u;\2\u010e")
        buf.write("\u010f\5\177@\2\u010f\u0110\5\u008dG\2\u0110\u0111\5m")
        buf.write("\67\2\u0111*\3\2\2\2\u0112\u0113\5u;\2\u0113\u0114\5\177")
        buf.write("@\2\u0114\u0115\5\u008bF\2\u0115\u0116\5m\67\2\u0116\u0117")
        buf.write("\5q9\2\u0117\u0118\5m\67\2\u0118\u0119\5\u0087D\2\u0119")
        buf.write(",\3\2\2\2\u011a\u011b\5o8\2\u011b\u011c\5{>\2\u011c\u011d")
        buf.write("\5\u0081A\2\u011d\u011e\5e\63\2\u011e\u011f\5\u008bF\2")
        buf.write("\u011f.\3\2\2\2\u0120\u0121\5\u0089E\2\u0121\u0122\5\u008b")
        buf.write("F\2\u0122\u0123\5\u0087D\2\u0123\u0124\5u;\2\u0124\u0125")
        buf.write("\5\177@\2\u0125\u0126\5q9\2\u0126\60\3\2\2\2\u0127\u0128")
        buf.write("\5g\64\2\u0128\u0129\5\u0081A\2\u0129\u012a\5\u0081A\2")
        buf.write("\u012a\u012b\5{>\2\u012b\u012c\5m\67\2\u012c\u012d\5e")
        buf.write("\63\2\u012d\u012e\5\177@\2\u012e\62\3\2\2\2\u012f\u0130")
        buf.write("\5e\63\2\u0130\u0131\5\u0087D\2\u0131\u0132\5\u0087D\2")
        buf.write("\u0132\u0133\5e\63\2\u0133\u0134\5\u0095K\2\u0134\64\3")
        buf.write("\2\2\2\u0135\u0136\5e\63\2\u0136\u0137\5\u008dG\2\u0137")
        buf.write("\u0138\5\u008bF\2\u0138\u0139\5\u0081A\2\u0139\66\3\2")
        buf.write("\2\2\u013a\u013b\5\u0081A\2\u013b\u013c\5o8\2\u013c8\3")
        buf.write("\2\2\2\u013d\u013e\7-\2\2\u013e:\3\2\2\2\u013f\u0140\7")
        buf.write("/\2\2\u0140<\3\2\2\2\u0141\u0142\7\61\2\2\u0142>\3\2\2")
        buf.write("\2\u0143\u0144\7,\2\2\u0144@\3\2\2\2\u0145\u0146\7\'\2")
        buf.write("\2\u0146B\3\2\2\2\u0147\u0148\7#\2\2\u0148\u0149\7?\2")
        buf.write("\2\u0149D\3\2\2\2\u014a\u014b\7?\2\2\u014b\u014c\7?\2")
        buf.write("\2\u014cF\3\2\2\2\u014d\u014e\7(\2\2\u014e\u014f\7(\2")
        buf.write("\2\u014fH\3\2\2\2\u0150\u0151\7~\2\2\u0151\u0152\7~\2")
        buf.write("\2\u0152J\3\2\2\2\u0153\u0154\7#\2\2\u0154L\3\2\2\2\u0155")
        buf.write("\u0156\7>\2\2\u0156N\3\2\2\2\u0157\u0158\7>\2\2\u0158")
        buf.write("\u0159\7?\2\2\u0159P\3\2\2\2\u015a\u015b\7@\2\2\u015b")
        buf.write("R\3\2\2\2\u015c\u015d\7@\2\2\u015d\u015e\7?\2\2\u015e")
        buf.write("T\3\2\2\2\u015f\u0160\7<\2\2\u0160\u0161\7<\2\2\u0161")
        buf.write("V\3\2\2\2\u0162\u0163\7*\2\2\u0163X\3\2\2\2\u0164\u0165")
        buf.write("\7+\2\2\u0165Z\3\2\2\2\u0166\u0167\7]\2\2\u0167\\\3\2")
        buf.write("\2\2\u0168\u0169\7_\2\2\u0169^\3\2\2\2\u016a\u016b\7}")
        buf.write("\2\2\u016b`\3\2\2\2\u016c\u016d\7\177\2\2\u016db\3\2\2")
        buf.write("\2\u016e\u016f\7?\2\2\u016fd\3\2\2\2\u0170\u0171\t\6\2")
        buf.write("\2\u0171f\3\2\2\2\u0172\u0173\t\7\2\2\u0173h\3\2\2\2\u0174")
        buf.write("\u0175\t\b\2\2\u0175j\3\2\2\2\u0176\u0177\t\t\2\2\u0177")
        buf.write("l\3\2\2\2\u0178\u0179\t\n\2\2\u0179n\3\2\2\2\u017a\u017b")
        buf.write("\t\13\2\2\u017bp\3\2\2\2\u017c\u017d\t\f\2\2\u017dr\3")
        buf.write("\2\2\2\u017e\u017f\t\r\2\2\u017ft\3\2\2\2\u0180\u0181")
        buf.write("\t\16\2\2\u0181v\3\2\2\2\u0182\u0183\t\17\2\2\u0183x\3")
        buf.write("\2\2\2\u0184\u0185\t\20\2\2\u0185z\3\2\2\2\u0186\u0187")
        buf.write("\t\21\2\2\u0187|\3\2\2\2\u0188\u0189\t\22\2\2\u0189~\3")
        buf.write("\2\2\2\u018a\u018b\t\23\2\2\u018b\u0080\3\2\2\2\u018c")
        buf.write("\u018d\t\24\2\2\u018d\u0082\3\2\2\2\u018e\u018f\t\25\2")
        buf.write("\2\u018f\u0084\3\2\2\2\u0190\u0191\t\26\2\2\u0191\u0086")
        buf.write("\3\2\2\2\u0192\u0193\t\27\2\2\u0193\u0088\3\2\2\2\u0194")
        buf.write("\u0195\t\30\2\2\u0195\u008a\3\2\2\2\u0196\u0197\t\31\2")
        buf.write("\2\u0197\u008c\3\2\2\2\u0198\u0199\t\32\2\2\u0199\u008e")
        buf.write("\3\2\2\2\u019a\u019b\t\33\2\2\u019b\u0090\3\2\2\2\u019c")
        buf.write("\u019d\t\34\2\2\u019d\u0092\3\2\2\2\u019e\u019f\t\35\2")
        buf.write("\2\u019f\u0094\3\2\2\2\u01a0\u01a1\t\36\2\2\u01a1\u0096")
        buf.write("\3\2\2\2\u01a2\u01a3\t\37\2\2\u01a3\u0098\3\2\2\2\7\2")
        buf.write("\u009c\u00ac\u00ba\u00c3\3\b\2\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    ERROR_CHAR = 2
    UNCLOSE_STRING = 3
    ILLEGAL_ESCAPE = 4
    BLOCKCOMMENT = 5
    INLINECOMMENT = 6
    IDENTIFIERS = 7
    INHERIT = 8
    VOID = 9
    RETURN = 10
    FUNCTION = 11
    TRUE = 12
    FALSE = 13
    IF = 14
    ELSE = 15
    WHILE = 16
    FOR = 17
    DO = 18
    BREAK = 19
    CONTINUE = 20
    INTEGER = 21
    FLOAT = 22
    STRING = 23
    BOOLEAN = 24
    ARRAY = 25
    AUTO = 26
    OF = 27
    ADD = 28
    SUBSTRACT = 29
    DIVIDE = 30
    MULTIPLY = 31
    MODULO = 32
    NOTEQUAL = 33
    EQUAL = 34
    AND = 35
    OR = 36
    NOT = 37
    LESS = 38
    LEQ = 39
    GREATER = 40
    GEQ = 41
    STRING_CONCAT = 42
    LEFT_PARENTHESIS = 43
    RIGHT_PARENTHESIS = 44
    LEFT_SQUARE_BRACKET = 45
    RIGHT_SQUARE_BRACKET = 46
    LEFT_CURLY_BRACKET = 47
    RIGHT_CURLY_BRACKET = 48
    ASSIGN = 49
    A = 50
    B = 51
    C = 52
    D = 53
    E = 54
    F = 55
    G = 56
    H = 57
    I = 58
    J = 59
    K = 60
    L = 61
    M = 62
    N = 63
    O = 64
    P = 65
    Q = 66
    R = 67
    S = 68
    T = 69
    U = 70
    V = 71
    W = 72
    X = 73
    Y = 74
    Z = 75

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'/'", "'*'", "'%'", "'!='", "'=='", "'&&'", "'||'", 
            "'!'", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "BLOCKCOMMENT", 
            "INLINECOMMENT", "IDENTIFIERS", "INHERIT", "VOID", "RETURN", 
            "FUNCTION", "TRUE", "FALSE", "IF", "ELSE", "WHILE", "FOR", "DO", 
            "BREAK", "CONTINUE", "INTEGER", "FLOAT", "STRING", "BOOLEAN", 
            "ARRAY", "AUTO", "OF", "ADD", "SUBSTRACT", "DIVIDE", "MULTIPLY", 
            "MODULO", "NOTEQUAL", "EQUAL", "AND", "OR", "NOT", "LESS", "LEQ", 
            "GREATER", "GEQ", "STRING_CONCAT", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
            "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", 
            "RIGHT_CURLY_BRACKET", "ASSIGN", "A", "B", "C", "D", "E", "F", 
            "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
            "S", "T", "U", "V", "W", "X", "Y", "Z" ]

    ruleNames = [ "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "BLOCKCOMMENT", "INLINECOMMENT", "IDENTIFIERS", "INHERIT", 
                  "VOID", "RETURN", "FUNCTION", "TRUE", "FALSE", "IF", "ELSE", 
                  "WHILE", "FOR", "DO", "BREAK", "CONTINUE", "INTEGER", 
                  "FLOAT", "STRING", "BOOLEAN", "ARRAY", "AUTO", "OF", "ADD", 
                  "SUBSTRACT", "DIVIDE", "MULTIPLY", "MODULO", "NOTEQUAL", 
                  "EQUAL", "AND", "OR", "NOT", "LESS", "LEQ", "GREATER", 
                  "GEQ", "STRING_CONCAT", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                  "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", 
                  "RIGHT_CURLY_BRACKET", "ASSIGN", "A", "B", "C", "D", "E", 
                  "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
                  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


