import unittest
from TestUtils import TestLexer


#   Another file
class LexerSuite(unittest.TestCase):

    def test_identifier_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_identifier_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Abc", "Abc,<EOF>", 102))

    def test_identifier_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_abc", "_abc,<EOF>", 103))

    def test_identifier_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_aBc1_2_3", "_aBc1_2_3,<EOF>", 104))

    def test_identifier_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_aB^1_2_3", "_aB,Error Token ^", 105))

    def test_identifier_6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_aB0000_____1_2_3", "_aB0000_____1_2_3,<EOF>", 106))

    def test_identifier_7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("2abc", "2,abc,<EOF>", 107))

    def test_identifier_8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("*abc", "*,abc,<EOF>", 108))

    #####

    def test_comment_1(self):
        """test comments"""
        self.assertTrue(TestLexer.test("/*abc*/", "<EOF>", 109))

    def test_comment_2(self):
        """test comments"""
        self.assertTrue(TestLexer.test("//abc", "<EOF>", 110))

    def test_comment_3(self):
        """test comments"""
        self.assertTrue(TestLexer.test("abc/*ab\nc*/ABC", "abc,ABC,<EOF>", 111))

    def test_comment_4(self):
        """test comments"""
        self.assertTrue(TestLexer.test("abc//de", "abc,<EOF>", 112))

    def test_comment_5(self):
        """test comments"""
        self.assertTrue(TestLexer.test("abc//abc\r\nABC", "abc,ABC,<EOF>", 113))

    def test_comment_6(self):
        """test comments"""
        self.assertTrue(TestLexer.test("123//456//789", "123,<EOF>", 114))

    def test_comment_7(self):
        """test comments"""
        self.assertTrue(TestLexer.test("/*hello*/*hello*/", "*,hello,*,/,<EOF>", 115))

    #####

    def test_integer_1(self):
        """test integer"""
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 116))

    def test_integer_2(self):
        """test integer"""
        self.assertTrue(TestLexer.test("1230", "1230,<EOF>", 117))

    def test_integer_3(self):
        """test integer"""
        self.assertTrue(TestLexer.test("1_2_3", "123,<EOF>", 118))

    def test_integer_4(self):
        """test integer"""
        self.assertTrue(TestLexer.test("0123456", "0,123456,<EOF>", 119))

    def test_integer_5(self):
        """test integer"""
        self.assertTrue(TestLexer.test("123__456", "123,__456,<EOF>", 120))

    def test_integer_6(self):
        """test integer"""
        self.assertTrue(TestLexer.test("-123456", "-,123456,<EOF>", 121))

    #####

    def test_float_1(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.1e-10", "1.1e-10,<EOF>", 122))

    def test_float_2(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.1e+10", "1.1e+10,<EOF>", 123))

    def test_float_3(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.1E-10", "1.1E-10,<EOF>", 124))

    def test_float_4(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.1E+10", "1.1E+10,<EOF>", 125))

    def test_float_5(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.1000", "1.1000,<EOF>", 126))

    def test_float_6(self):
        """test float"""
        self.assertTrue(TestLexer.test("1E0", "1E0,<EOF>", 127))

    def test_float_7(self):
        """test float"""
        self.assertTrue(TestLexer.test(".1e+10", ".1e+10,<EOF>", 128))

    def test_float_8(self):
        """test float"""
        self.assertTrue(TestLexer.test(".E-10", ".E-10,<EOF>", 129))

    def test_float_9(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.00E", "1.00,E,<EOF>", 130))

    def test_float_10(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.00E +123", "1.00,E,+,123,<EOF>", 131))

    def test_float_11(self):
        """test float"""
        self.assertTrue(TestLexer.test("1_111.11e11", "1111.11e11,<EOF>", 132))

    def test_float_12(self):
        """test float"""
        self.assertTrue(TestLexer.test("1_111.11e11_1", "1111.11e11,_1,<EOF>", 133))

    def test_float_13(self):
        """test float"""
        self.assertTrue(TestLexer.test("1_111.1_1e11_1", "1111.1,_1e11_1,<EOF>", 134))

    def test_float_14(self):
        """test float"""
        self.assertTrue(TestLexer.test(".111", ".,111,<EOF>", 135))

    def test_float_15(self):
        """test float"""
        self.assertTrue(TestLexer.test("E-12", "E,-,12,<EOF>", 136))

    def test_float_16(self):
        """test float"""
        self.assertTrue(TestLexer.test("-1.111e-111", "-,1.111e-111,<EOF>", 137))

    #####

    def test_string_1(self):
        """test string"""
        self.assertTrue(TestLexer.test(""" "hello 123" """, "hello 123,<EOF>", 138))

    def test_string_2(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\tworld\"", "hello\tworld,<EOF>", 139))

    def test_string_3(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\bworld\"", "hello\bworld,<EOF>", 140))

    def test_string_4(self):
        """test string"""
        self.assertTrue(TestLexer.test(""" "hello\\nworld" """, "hello\\nworld,<EOF>", 141))

    def test_string_5(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\\"world\"", "hello\\\"world,<EOF>", 142))

    def test_string_6(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\\'world\"", "hello\\\'world,<EOF>", 143))

    def test_string_7(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\bworld\"", "hello\\bworld,<EOF>", 144))

    def test_string_8(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\fworld\"", "hello\\fworld,<EOF>", 145))

    def test_string_9(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\rworld\"", "hello\\rworld,<EOF>", 146))

    def test_string_10(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\tworld\"", "hello\\tworld,<EOF>", 147))

    def test_string_11(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\yworld\"", "Illegal Escape In String: hello\\y", 148))

    def test_string_12(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\2world\"", "Illegal Escape In String: hello\\2", 149))

    def test_string_13(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\hworld\"", "Illegal Escape In String: hello\\h", 150))

    def test_string_14(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\aworld\"", "Illegal Escape In String: hello\\a", 151))

    def test_string_15(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\nworld\"", "Unclosed String: hello", 152))

    def test_string_16(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello", "Unclosed String: hello", 153))

    def test_string_17(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"hello\\\"", "Unclosed String: hello\\\"", 154))

    #####

    def test_error_token_1(self):
        """test error token"""
        self.assertTrue(TestLexer.test("$hello", "Error Token $", 155))

    def test_error_token_2(self):
        """test error token"""
        self.assertTrue(TestLexer.test("~123", "Error Token ~", 156))

    def test_error_token_3(self):
        """test error token"""
        self.assertTrue(TestLexer.test("hello`world", "hello,Error Token `", 157))

    def test_error_token_4(self):
        """test error token"""
        self.assertTrue(TestLexer.test("a&b", "a,Error Token &", 158))

    def test_error_token_5(self):
        """test error token"""
        self.assertTrue(TestLexer.test("a|b", "a,Error Token |", 159))

    def test_error_token_6(self):
        """test error token"""
        self.assertTrue(TestLexer.test("a.b", "a,.,b,<EOF>", 160))

    def test_error_token_7(self):
        """test error token"""
        self.assertTrue(TestLexer.test("a?b", "a,Error Token ?", 161))

    ##### 

    def test_operator_1(self):
        """test operator"""
        self.assertTrue(TestLexer.test("+++", "+,+,+,<EOF>", 162))

    def test_operator_2(self):
        """test operator"""
        self.assertTrue(TestLexer.test("---", "-,-,-,<EOF>", 163))

    def test_operator_3(self):
        """test operator"""
        self.assertTrue(TestLexer.test("***", "*,*,*,<EOF>", 164))

    def test_operator_4(self):
        """test operator"""
        self.assertTrue(TestLexer.test("/", "/,<EOF>", 165))

    def test_operator_5(self):
        """test operator"""
        self.assertTrue(TestLexer.test("%%%", "%,%,%,<EOF>", 166))

    def test_operator_6(self):
        """test operator"""
        self.assertTrue(TestLexer.test("===", "==,=,<EOF>", 167))

    def test_operator_7(self):
        """test operator"""
        self.assertTrue(TestLexer.test("!!!==", "!,!,!=,=,<EOF>", 168))
    
    def test_operator_8(self):
        """test operator"""
        self.assertTrue(TestLexer.test("<===>=", "<=,==,>=,<EOF>", 169))

    def test_operator_9(self):
        """test operator"""
        self.assertTrue(TestLexer.test("2:2", "2,:,2,<EOF>", 170))

    def test_operator_10(self):
        """test operator"""
        self.assertTrue(TestLexer.test("&&&", "&&,Error Token &", 171))

    def test_operator_11(self):
        """test operator"""
        self.assertTrue(TestLexer.test("|||", "||,Error Token |", 172))

    def test_operator_12(self):
        """test operator"""
        self.assertTrue(TestLexer.test("<><>>><", "<,>,<,>,>,>,<,<EOF>", 173))

    #####

    def test_separator_1(self):
        """test separator"""
        self.assertTrue(TestLexer.test("hello(world)", "hello,(,world,),<EOF>", 174))
    
    def test_separator_2(self):
        """test separator"""
        self.assertTrue(TestLexer.test("[]", "[,],<EOF>", 175))

    def test_separator_3(self):
        """test separator"""
        self.assertTrue(TestLexer.test("{}", "{,},<EOF>", 176))

    def test_separator_4(self):
        """test separator"""
        self.assertTrue(TestLexer.test(";;;", ";,;,;,<EOF>", 177))

    def test_separator_5(self):
        """test separator"""
        self.assertTrue(TestLexer.test(":::", "::,:,<EOF>", 178))

    def test_separator_6(self):
        """test separator"""
        self.assertTrue(TestLexer.test(",,,", ",,,,,,<EOF>", 179) )
        
    def test_separator_7(self):
        """test separator"""
        self.assertTrue(TestLexer.test("...", ".,.,.,<EOF>", 180))

    #####

    def test_ws_1(self):
        """test ws"""
        self.assertTrue(TestLexer.test("", "<EOF>", 181))

    def test_ws_2(self):
        """test ws"""
        self.assertTrue(TestLexer.test("   ", "<EOF>", 182))

    def test_ws_3(self):
        """test ws"""
        self.assertTrue(TestLexer.test("\t", "<EOF>", 183))

    def test_ws_4(self):
        """test ws"""
        self.assertTrue(TestLexer.test("\n", "<EOF>", 184))

    def test_ws_5(self):
        """test ws"""
        self.assertTrue(TestLexer.test("\r", "<EOF>", 185))

    #####

    def test_all_1(self):
        """test all"""
        self.assertTrue(TestLexer.test("{1, 5, 7, 12}", "{,1,,,5,,,7,,,12,},<EOF>", 186))

    def test_all_2(self):
        """test all"""
        self.assertTrue(TestLexer.test("{\"Le\", \"Hong\", \"Hanh\"}", "{,Le,,,Hong,,,Hanh,},<EOF>", 187))

    def test_all_3(self):
        """test all"""
        self.assertTrue(TestLexer.test("a,b:array [2, 2] of integer", "a,,,b,:,array,[,2,,,2,],of,integer,<EOF>", 188))

    def test_all_4(self):
        """test all"""
        self.assertTrue(TestLexer.test("a,b,__c:array [0,100] of boolean", "a,,,b,,,__c,:,array,[,0,,,100,],of,boolean,<EOF>", 189))

    def test_all_5(self):
        """test all"""
        self.assertTrue(TestLexer.test("a,b,c:float = 65-15", "a,,,b,,,c,:,float,=,65,-,15,<EOF>", 190))

    def test_all_6(self):
        """test all"""
        self.assertTrue(TestLexer.test("a:string = \"hello\"::\"world\"", "a,:,string,=,hello,::,world,<EOF>", 191))

    def test_all_7(self):
        """test all"""
        self.assertTrue(TestLexer.test("a[1,0]", "a,[,1,,,0,],<EOF>", 192))

    def test_all_8(self):
        """test all"""
        self.assertTrue(TestLexer.test("a[1, 0]", "a,[,1,,,0,],<EOF>", 193))  

    def test_all_9(self):
        """test all"""
        self.assertTrue(TestLexer.test("inherit out _a1 : integer", "inherit,out,_a1,:,integer,<EOF>", 194))

    def test_all_10(self):
        """test all"""
        self.assertTrue(TestLexer.test("inherit out _a1 : integer", "inherit,out,_a1,:,integer,<EOF>", 195))

    def test_all_11(self):
        """test all"""
        self.assertTrue(TestLexer.test(
            "sumOfAll:function integer(n:integer){return n}",
            "sumOfAll,:,function,integer,(,n,:,integer,),{,return,n,},<EOF>", 196))

    def test_all_12(self):
        """test all"""
        self.assertTrue(TestLexer.test("sum(123)", "sum,(,123,),<EOF>", 197))

    def test_all_13(self):
        """test all"""
        self.assertTrue(TestLexer.test(
            "if(a==b) array[0,9]=100; else array[0,9]=200;", 
            "if,(,a,==,b,),array,[,0,,,9,],=,100,;,else,array,[,0,,,9,],=,200,;,<EOF>", 198))

    def test_all_14(self):
        """test all"""
        self.assertTrue(TestLexer.test(
            "if(a==b) array[0,9]=100; else array[0,9]=200;", 
            "if,(,a,==,b,),array,[,0,,,9,],=,100,;,else,array,[,0,,,9,],=,200,;,<EOF>", 199))
    
    def test_all_15(self):
        """test all"""
        self.assertTrue(TestLexer.test(
            "\\", 
            "Error Token \\", 200))
