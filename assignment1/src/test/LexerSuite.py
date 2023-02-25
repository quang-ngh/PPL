import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    #   --------------------------- TEST IDs ------------------------------
    def test_lexer_101(self):
        my_input = "abcasd_"
        my_expected_output = "abcasd_,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 102))
        
    def test_lexer_102(self):
        my_input = "abc"
        my_expected_output = "abc,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 102))


    def test_lexer_103(self):
        my_input = "_Abc_" 
        my_expected_output = "_Abc_,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 103))


    def test_lexer_104(self):
        my_input = "_abc"
        my_expected_output = "_abc,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 104))


    def test_lexer_105(self):
        my_input = "__asdc1_2_3"
        my_expected_output = "__asdc1_2_3,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 105))


    def test_lexer_106(self):
        my_input = "__a_B^1_2_3"
        my_expected_output = "__a_B,Error Token ^"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 106))


    def test_lexer_107(self):
        my_input = "_aB0000_____1_2_3"
        my_expected_output = "_aB0000_____1_2_3,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 107))


    def test_lexer_108(self):
        my_input = "31aaa"
        my_expected_output = "31,aaa,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 108))


    def test_lexer_109(self):
        my_input = "**abc*"
        my_expected_output =  "*,*,abc,*,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 109))

    #   ------------------------- END OF TEST IDs ------------------------

    #   -------------------------- TEST COMMENTS ------------------------
    def test_lexer_110(self):
        my_input = "/*abc*/"
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 110))


    def test_lexer_111(self):
        my_input = "// Hello my name is quang __- @!#"
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 111))


    def test_lexer_112(self):
        my_input = "123abc/*ab\nc*/ABC_"
        my_expected_output = "123,abc,ABC_,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 112))


    def test_lexer_113(self):
        my_input = "123_abc//abc//de"
        my_expected_output = "123,_abc,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 113))


    def test_lexer_114(self):
        my_input = "abc//abc\r\nABC"
        my_expected_output = "abc,ABC,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 114))


    def test_lexer_115(self):
        my_input = "/*hello*/*hello*/"
        my_expected_output = "*,hello,*,/,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 115))


    def test_lexer_116(self):
        my_input = "/* /asfasf* /*aaa */123"
        my_expected_output = "123,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 116))
    #   -------------------------- END OF TEST COMMENTS ------------------------

    #   -------------------------- START OF TEST INTEGERS ------------------------
    def test_lexer_117(self):
        my_input = '123123__123_123'
        my_expected_output = "123123,__123_123,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 117))


    def test_lexer_118(self):
        my_input = "1230"
        my_expected_output = "1230,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 118))


    def test_lexer_119(self):
        my_input = "1_2_3"
        my_expected_output = "123,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 119))


    def test_lexer_120(self):
        my_input = "0123456"
        my_expected_output = "0,123456,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 120))

    def test_lexer_121(self):
        my_input = "123__456"
        my_expected_output = "123,__456,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 121))


    def test_lexer_122(self):
        my_input = "-123456"
        my_expected_output = "-,123456,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 122))


    def test_lexer_123(self):
        my_input = "+123_123_32_212"
        my_expected_output = "+,12312332212,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 123))


    def test_lexer_124(self):
        my_input = "123-123_123_45_6"
        my_expected_output = "123,-,123123456,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 124))
    #   ------------------------- END OF TEST INTEGERS ------------------------

    #   ------------------------- START OF TEST FLOAT ------------------------
    def test_lexer_125(self):
        my_input = "1.1e-10"
        my_expected_output = "1.1e-10<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 125))


    def test_lexer_126(self):
        my_input =  "1.123_123e+10"
        my_expected_output = "1.123123e+10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 126))


    def test_lexer_127(self):
        my_input = "1.1E-10"
        my_expected_output = "1.1E-10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 127))


    def test_lexer_128(self):
        my_input =  "1.1E+10"
        my_expected_output = "1.1E+10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 128))


    def test_lexer_129(self):
        my_input = "1.1000"
        my_expected_output = "1.1000,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 129))


    def test_lexer_130(self):
        my_input = "112E1"
        my_expected_output = "123E1,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 130))


    def test_lexer_131(self):
        my_input = ".1e+10"
        my_expected_output = ".1e+10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 131))


    def test_lexer_132(self):
        my_input = ".E-10"
        my_expected_output = ".E-10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 132))


    def test_lexer_133(self):
        my_input = "1.00E"
        my_expected_output = "1.00,E,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 133))


    def test_lexer_134(self):
        my_input = "2.13E +123"
        my_expected_output = "2.13,E,+,123,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 134))


    def test_lexer_135(self):
        my_input = "1_111.11e11"
        my_expected_output = "1111.11e11,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 135))


    def test_lexer_136(self):
        my_input = "1_111.11e11_1"
        my_expected_output = "<1111.11e11,_1,EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 136))


    def test_lexer_137(self):
        my_input = "1_111.1_1e11_1"
        my_expected_output = "1111.1,_1e11_1,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 137))


    def test_lexer_138(self):
        my_input = ".123_22"
        my_expected_output = ".,12322,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 138))


    def test_lexer_139(self):
        my_input = "e-123"
        my_expected_output = "e,-,123<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 139))


    def test_lexer_140(self):
        my_input = "-1.123e-123"
        my_expected_output = "-,1.123e-123,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 140))

    # --------------------------- END OF TEST FLOATS ---------------------------

    # --------------------------- START OF TEST ERROR TOKENS -------------------
    def test_lexer_141(self):
        my_input = "$quang"
        my_expected_output = "Error Token $"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 141))


    def test_lexer_142(self):
        my_input = "~1231"
        my_expected_output = "Error Token ~"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 142))


    def test_lexer_143(self):
        my_input = "hellomyname`is"
        my_expected_output = "hellomyname,Error Token `"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 143))


    def test_lexer_144(self):
        my_input = "a&2"
        my_expected_output = "a,Error Token &"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 144))


    def test_lexer_145(self):
        my_input = "a||b&b"
        my_expected_output = "a,||,b,Error Token &"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 145))


    def test_lexer_146(self):
        my_input = "asd_>b?1"
        my_expected_output = "asd_,>,b,Error Token ?"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 146))


    def test_lexer_147(self):
        my_input = "abc.ad1>123?"
        my_expected_output = "abc,.,ad1,>,123,Error Token ?"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 147))

    #   ----------------------------- END OF TEST ERROR TOKENS --------------------------------

    #   ----------------------------- START OF TEST OPERATORS --------------------------------
    def test_lexer_148(self):
        my_input = "+++"
        my_expected_output = "+,+,+,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 148))


    def test_lexer_149(self):
        my_input = "---"
        my_expected_output = "-,-,-,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 149))


    def test_lexer_150(self):
        my_input = "***"
        my_expected_output = "*,*,*,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 150))

    def test_lexer_151(self):
        my_input = "/*+"
        my_expected_output = "/,*,+,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 151))


    def test_lexer_152(self):
        my_input = "%%||&&&"
        my_expected_output = "%,%,||,&&,Error Token &"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 152))


    def test_lexer_153(self):
        my_input = "==="
        my_expected_output = "==,=,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 153))


    def test_lexer_154(self):
        my_input = "!!!=="
        my_expected_output = "!,!,!=,=,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 154))


    def test_lexer_155(self):
        my_input = "<===>="
        my_expected_output = "<=,==,>=,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 155))


    def test_lexer_156(self):
        my_input = "123:123"
        my_expected_output = "123,:,123,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 156))


    def test_lexer_157(self):
        my_input = "&&&"
        my_expected_output = "&&,Error Token &"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 157))


    def test_lexer_158(self):
        my_input = "|||||"
        my_expected_output = "||,||,Error Token |"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 158))


    def test_lexer_159(self):
        my_input = "><><><==><><"
        my_expected_output = ">,<,>,<,>,<=,=,>,<,>,<,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 159))
    #   --------------------------- END OF TEST OPERATORS --------------------------

    #   --------------------------- START OF TEST SEPARATORS ------------------------
    def test_lexer_160(self):
        my_input = "hello(world)"
        my_expected_output = "hello,(,world,),<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 160))

    def test_lexer_161(self):
        my_input = "[]()||"
        my_expected_output = "[,],(,),||,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 161))


    def test_lexer_162(self):
        my_input = "{}{)()"
        my_expected_output = "{,},{,),(,),<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 162))


    def test_lexer_163(self):
        my_input = ";;;{}@"
        my_expected_output = ";,;,;,{,},Error Token @"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 163))


    def test_lexer_164(self):
        my_input = ":::::({})"
        my_expected_output = "::,::,:,(,{,},),<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 164))


    def test_lexer_165(self):
        my_input = ",,,,"
        my_expected_output = ",,,,,,,,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 165))


    def test_lexer_166(self):
        my_input = "..."
        my_expected_output = ".,.,.,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 166))


    def test_lexer_167(self):
        my_input = ",.,.,"
        my_expected_output = ",,.,,,.,,,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 167))
    #   ------------------------------ END OF TEST SEPARATORS ------------------------------

    #   ------------------------------ START OF TEST WS ------------------------------
    def test_lexer_168(self):
        my_input = "    "
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 168))


    def test_lexer_169(self):
        my_input = "\t\t\t"
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 169))


    def test_lexer_170(self):
        my_input = "\n\t \f \f \f "
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 170))

    def test_lexer_171(self):
        my_input = "\r\n   \t\t"
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 171))


    def test_lexer_172(self):
        my_input = "\t\t\b  \f   \t \t \t"
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 172))


    def test_lexer_173(self):
        my_input = "\n"
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 173))


    def test_lexer_174(self):
        my_input = "\r"
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 174))

    def test_lexer_175(self):
        my_input = "\t"
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 175))


    def test_lexer_176(self):
        my_input = "\f"
        my_expected_output = "<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 176))
    #   --------------------------- END OF TEST WS ---------------------------

    #   --------------------------- START OF TEST KEYWORDS ----------------------
    def test_lexer_177(self):
        my_input = "auto break boolean do else"
        my_expected_output = "auto,break,boolean,do,else,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 177))


    def test_lexer_178(self):
        my_input = "float for function if integer Return"
        my_expected_output = "float,for,function,if,integer,Return,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 178))


    def test_lexer_179(self):
        my_input = "string true false while void out continue"
        my_expected_output = "string,true,false,while,void,out,continue,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 179))


    def test_lexer_180(self):
        my_input = "inherit\t\tarray\bof\r\n"
        my_expected_output = "inherit,array,of,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 180))
    #   -------------------------- END OF TEST KEYWORDS -------------------------

    #   -------------------------- START OF TEST STRING -------------------------
    def test_lexer_181(self):
        my_input = """ "abc123aabc" """
        my_expected_output = """abc123aabc,<EOF>"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 181))


    def test_lexer_182(self):
        my_input = """ "//This is the inline comment" """
        my_expected_output = """//This is the inline comment,<EOF>"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 182))


    def test_lexer_183(self):
        my_input = """ 123AbC874-536"count=89-79=10" """
        my_expected_output = """123,AbC874,-,536,count=89-79=10,<EOF>"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 183))


    def test_lexer_184(self):
        my_input = """ "" "String" " ""?""-""#""Mulitiple Characters" """
        my_expected_output = """,String, ,?,-,#,Mulitiple Characters,<EOF>"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 184))

    def test_lexer_185(self):
        my_input = """ " hello lexer \\t \\b\\n\\""     asdf  """
        my_expected_output = """ hello lexer \t \b\n\\",asdf,<EOF>"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 185))

    def test_lexer_186(self):
        my_input = "\"hello\tworld\""
        my_expected_output = "hello\tworld,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 186))

    def test_lexer_187(self):
        my_input = "\"hello\bworld\""
        my_expected_output = "hello\bworld,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 187))

    def test_lexer_188(self):
        my_input = """ "hello\\nworld" """
        my_expected_output = "hello\\nworld,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 188))

    def test_lexer_189(self):
        my_input = """ "   Test\""escape\\" in \\tString"\" Literal\\""   __rtcvbn  """
        my_expected_output = """   Test,escape\\" in \\tString, Literal\\",__rtcvbn,<EOF>"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 189))


    def test_lexer_190(self):
        my_input = """ "Backspace\\b""Formfeed\\f""Return\\r\"\"Newline\\n""Tab\\t""Double quote\\"" "Backslash\\\\ "  """
        my_expected_output = """Backspace\\b,Formfeed\\f,Return\\r,Newline\\n,Tab\\t,Double quote\\",Backslash\\\\ ,<EOF>"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 190))

    def test_lexer_191(self):
        my_input = """ "abc123aasf\gabc" """
        my_expected_output = """Illegal Escape In String: abc123aasf\g"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 191))


    def test_lexer_192(self):
        my_input = """ 123-4"abc123a\\b\\iasVm" """
        my_expected_output = """123,-,4,Illegal Escape In String: abc123a\\b\\i"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 192))


    def test_lexer_193(self):
        my_input = """ " abc\\s  " "vbnMHHj" """
        my_expected_output ="""Illegal Escape In String:  abc\\s"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 193))


    def test_lexer_194(self):
        my_input = """ "ABC-abc+xYz \\ "" " """
        my_expected_output = """Illegal Escape In String: ABC-abc+xYz \\ """
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 194))


    def test_lexer_195(self):
        my_input = """ "     " "" "" "\\t\\b\\g" """
        my_expected_output = """     ,,,Illegal Escape In String: \\t\\b\\g"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 195))


    def test_lexer_196(self):
        my_input = """ "#$342%\\t\\#^&*((*&^%$#\\"))*768" """
        my_expected_output = """Illegal Escape In String: #$342%\\t\\#"""
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 196))
    #   ------------------------------ END OF TEST STRING ----------------------------------------------------------------

    def test_lexer_197(self):
        my_input = "a,b,c:array [2, 2] of integer"
        my_expected_output = "a,,,b,,,c,:,array,[,2,,,2,],of,integer,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 197))


    def test_lexer_198(self):
        my_input = "a,b,c:float = 65-15, 123_123-2"
        my_expected_output = "a,,,b,,,c,:,float,=,65,-,15,,,123123,-,2,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 198))


    def test_lexer_199(self):
        my_input = "if(cond1==precond) array[0,9]=1; else array[0,9]=0;"
        my_expected_output = "if,(,cond1,==,precond,),array,[,0,,,9,],=,1,;,else,array,[,0,,,9,],=,0,;,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 199))


    def test_lexer_200(self):
        my_input = "isChange,notChange,make_decision:array [0,100] of boolean;"
        my_expected_output = "isChange,,,notChange,,,make_decision,:,array,[,0,,,100,],of,boolean,;,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 200))
