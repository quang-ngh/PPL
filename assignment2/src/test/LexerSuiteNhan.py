import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_empty_input(self):
        self.assertTrue(TestLexer.test("", "<EOF>", 100))

    def test_skip_space(self):
        self.assertTrue(TestLexer.test(" ", "<EOF>", 101))

    def test_skip_all_whitespace_char(self):
        self.assertTrue(TestLexer.test(" \r \n \t \f \b ", "<EOF>", 102))

    def test_skip_comment(self):
        self.assertTrue(TestLexer.test(
            "//Hello world\n/* John cena */", "<EOF>", 103))

    def test_skip_line_comment_inside_block_comment(self):
        self.assertTrue(TestLexer.test(
            "/* // Hello world */", "<EOF>", 104))

    def test_skip_block_comment_inside_line_comment(self):
        self.assertTrue(TestLexer.test(
            "// /* John cena */ //fa", "<EOF>", 105))

    def test_skip_line_comment_after_block_comment_end(self):
        self.assertTrue(TestLexer.test('/* Test */ //fa', "<EOF>", 106))

    def test_multiple_line_block_comment(self):
        self.assertTrue(TestLexer.test(
            '/* John \n Cena */\n//fa', "<EOF>", 107))

    def test_multiple_line_block_and_line_comment(self):
        self.assertTrue(TestLexer.test(
            '/* John \n Cena */\n//fa\n//*^&%$""', "<EOF>", 108))

    def test_keyword_auto(self):
        self.assertTrue(TestLexer.test('auto', 'auto,<EOF>', 109))

    def test_keyword_break(self):
        self.assertTrue(TestLexer.test('break', 'break,<EOF>', 110))

    def test_keyword_boolean(self):
        self.assertTrue(TestLexer.test('boolean', 'boolean,<EOF>', 111))

    def test_keyword_do(self):
        self.assertTrue(TestLexer.test('do', 'do,<EOF>', 112))

    def test_keyword_else(self):
        self.assertTrue(TestLexer.test('else', 'else,<EOF>', 113))

    def test_keyword_false(self):
        self.assertTrue(TestLexer.test('false', 'false,<EOF>', 114))

    def test_keyword_float(self):
        self.assertTrue(TestLexer.test('float', 'float,<EOF>', 115))

    def test_keyword_for(self):
        self.assertTrue(TestLexer.test('for', 'for,<EOF>', 116))

    def test_keyword_function(self):
        self.assertTrue(TestLexer.test('function', 'function,<EOF>', 117))

    def test_keyword_if(self):
        self.assertTrue(TestLexer.test('if', 'if,<EOF>', 118))

    def test_keyword_integer(self):
        self.assertTrue(TestLexer.test('integer', 'integer,<EOF>', 119))

    def test_keyword_return(self):
        self.assertTrue(TestLexer.test('return', 'return,<EOF>', 120))

    def test_keyword_string(self):
        self.assertTrue(TestLexer.test('string', 'string,<EOF>', 121))

    def test_keyword_true(self):
        self.assertTrue(TestLexer.test('true', 'true,<EOF>', 122))

    def test_keyword_void(self):
        self.assertTrue(TestLexer.test('void', 'void,<EOF>', 123))

    def test_keyword_while(self):
        self.assertTrue(TestLexer.test('while', 'while,<EOF>', 124))

    def test_keyword_out(self):
        self.assertTrue(TestLexer.test('out', 'out,<EOF>', 125))

    def test_keyword_continue(self):
        self.assertTrue(TestLexer.test('continue', 'continue,<EOF>', 126))

    def test_keyword_of(self):
        self.assertTrue(TestLexer.test('of', 'of,<EOF>', 127))

    def test_keyword_inherit(self):
        self.assertTrue(TestLexer.test('inherit', 'inherit,<EOF>', 128))

    def test_keyword_array(self):
        self.assertTrue(TestLexer.test('array', 'array,<EOF>', 129))

    def test_simple_identifier(self):
        self.assertTrue(
            TestLexer.test(
                """ X""",
                """X,<EOF>""",
                130
            )
        )

    def test_underscore_identifier(self):
        self.assertTrue(
            TestLexer.test(
                """_""",
                """_,<EOF>""",
                131
            ))

    def test_complex_identifier(self):
        self.assertTrue(
            TestLexer.test(
                """_userName29""",
                """_userName29,<EOF>""",
                132
            )
        )

    def test_undescore_number_indentifier(self):
        self.assertTrue(
            TestLexer.test(
                """_18""",
                """_18,<EOF>""",
                133
            )
        )

    def test_multiple_identifier(self):
        self.assertTrue(
            TestLexer.test(
                """_jbo fa_""",
                """_jbo,fa_,<EOF>""",
                134
            )
        )

    def test_add_op(self):
        self.assertTrue(TestLexer.test("+", "+,<EOF>", 135))

    def test_sub_op(self):
        self.assertTrue(TestLexer.test("-", "-,<EOF>", 136))

    def test_mul_op(self):
        self.assertTrue(TestLexer.test("*", "*,<EOF>", 137))

    def test_div_op(self):
        self.assertTrue(TestLexer.test("/", "/,<EOF>", 138))

    def test_mod_op(self):
        self.assertTrue(TestLexer.test("%", "%,<EOF>", 139))

    def test_not_op(self):
        self.assertTrue(TestLexer.test("!", "!,<EOF>", 140))

    def test_logical_and_op(self):
        self.assertTrue(TestLexer.test("&&", "&&,<EOF>", 141))

    def test_logical_or_op(self):
        self.assertTrue(TestLexer.test("||", "||,<EOF>", 142))

    def test_eq_op(self):
        self.assertTrue(TestLexer.test("==", "==,<EOF>", 143))

    def test_not_eq_op(self):
        self.assertTrue(TestLexer.test("!=", "!=,<EOF>", 144))

    def test_greater_op(self):
        self.assertTrue(TestLexer.test("<", "<,<EOF>", 145))

    def test_greater_eq_op(self):
        self.assertTrue(TestLexer.test("<=", "<=,<EOF>", 146))

    def test_less_op(self):
        self.assertTrue(TestLexer.test(">", ">,<EOF>", 147))

    def test_less_eq_op(self):
        self.assertTrue(TestLexer.test(">=", ">=,<EOF>", 148))

    def test_concat_op(self):
        self.assertTrue(TestLexer.test("::", "::,<EOF>", 149))

    def test_multiple_op_1(self):
        self.assertTrue(TestLexer.test(">=>", ">=,>,<EOF>", 150))

    def test_multiple_op_2(self):
        self.assertTrue(TestLexer.test("!===", "!=,==,<EOF>", 151))

    def test_multiple_op_3(self):
        self.assertTrue(TestLexer.test("<<=", "<,<=,<EOF>", 152))

    def test_multiple_op_4(self):
        self.assertTrue(TestLexer.test("===", "==,=,<EOF>", 153))

    def test_multiple_op_5(self):
        self.assertTrue(TestLexer.test(">====!=", ">=,==,=,!=,<EOF>", 154))

    def test_integer_with_underscore(self):
        self.assertTrue(TestLexer.test("1_23", "123,<EOF>", 155))

    def test_integer_without_underscore(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 156))

    def test_integer_with_trailing_underscore(self):
        self.assertTrue(TestLexer.test("123_", "123,_,<EOF>", 157))

    def test_integer_with_underscore_2(self):
        self.assertTrue(TestLexer.test("123_4", "1234,<EOF>", 158))

    def test_integer_zero(self):
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 159))

    def test_integer_many_zero(self):
        self.assertTrue(TestLexer.test("0000", "0,0,0,0,<EOF>", 160))

    def test_float_int_dec(self):
        self.assertTrue(TestLexer.test("482.94", "482.94,<EOF>", 161))

    def test_float_int_exp(self):
        self.assertTrue(TestLexer.test("482e94", "482e94,<EOF>", 162))

    def test_float_int_with_underscore_dec_exp(self):
        self.assertTrue(TestLexer.test("4_82.94e+2", "482.94e+2,<EOF>", 163))

    def test_float_int_with_underscore_dec(self):
        self.assertTrue(TestLexer.test("48_2.94", "482.94,<EOF>", 164))

    def test_float_dec_exp(self):
        self.assertTrue(TestLexer.test(".94e-2", ".94e-2,<EOF>", 165))

    def test_float_invalid(self):
        self.assertTrue(TestLexer.test("12.11.1", "12.11,.,1,<EOF>", 166))

    def test_true_boolean(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 167))

    def test_false_boolean(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 168))

    def test_string(self):
        self.assertTrue(TestLexer.test(
            R'"Hello world"', R"Hello world,<EOF>", 169))

    def test_string_valid_escape(self):
        self.assertTrue(TestLexer.test(
            R'"Hello\tworld"', R"Hello\tworld,<EOF>", 170))

    def test_empty_string(self):
        self.assertTrue(TestLexer.test(R'""', ',<EOF>', 171))

    def test_string_escape_double_quote(self):
        self.assertTrue(TestLexer.test(R'"\""', R'\",<EOF>', 172))

    def test_all_escape(self):
        self.assertTrue(TestLexer.test(
            R'"Hello\b\f\r\n\t\\\'\", world!"', R'Hello\b\f\r\n\t\\\'\", world!,<EOF>', 173))

    def test_illegal_escape(self):
        self.assertTrue(TestLexer.test(
            R'"Hello\xworld"', R'Illegal Escape In String: Hello\x', 174))

    def test_unclosed_string_by_newline(self):
        self.assertTrue(TestLexer.test(
            '"Hello\nworld"', R'Unclosed String: Hello', 175))

    def test_unclosed_string_on_oneline(self):
        self.assertTrue(TestLexer.test(
            '"Hello world', "Unclosed String: Hello world", 176))

    def test_both_unclosed_and_illegal_escape(self):
        self.assertTrue(TestLexer.test(R'"Hello\kworld',
                        R'Illegal Escape In String: Hello\k', 177))

    def test_error_char(self):
        self.assertTrue(TestLexer.test("$", "Error Token $", 178))

    def test_error_char_2(self):
        self.assertTrue(TestLexer.test("#^", "Error Token #", 179))

    # ( ) [ ] . , ; : { } =
    def test_separator_open_paranthesis(self):
        self.assertTrue(TestLexer.test("(", "(,<EOF>", 180))

    def test_separator_close_paranthesis(self):
        self.assertTrue(TestLexer.test(")", "),<EOF>", 181))

    def test_separator_dot(self):
        self.assertTrue(TestLexer.test('.', '.,<EOF>', 182))

    def test_separator_comma(self):
        self.assertTrue(TestLexer.test(',', ',,<EOF>', 183))

    def test_separator_semi_colon(self):
        self.assertTrue(TestLexer.test(';', ';,<EOF>', 184))

    def test_separator_colon(self):
        self.assertTrue(TestLexer.test(':', ':,<EOF>', 185))

    def test_separator_open_curly_brace(self):
        self.assertTrue(TestLexer.test('{', '{,<EOF>', 186))

    def test_separator_close_curly_brace(self):
        self.assertTrue(TestLexer.test('}', '},<EOF>', 187))

    def test_separator_eq(self):
        self.assertTrue(TestLexer.test('=', '=,<EOF>', 188))

    def test_multiple_eq(self):
        self.assertTrue(TestLexer.test('==', '==,<EOF>', 189))

    def test_multiple_3_eq(self):
        self.assertTrue(TestLexer.test('===', '==,=,<EOF>', 190))

    def test_multiple_4_eq(self):
        self.assertTrue(TestLexer.test('====', '==,==,<EOF>', 191))

    def test_invalid_char(self):
        self.assertTrue(TestLexer.test('^', "Error Token ^", 192))

    def test_invalid_char_2(self):
        self.assertTrue(TestLexer.test('@', "Error Token @", 193))

    def test_invalid_char_3(self):
        self.assertTrue(TestLexer.test('#', "Error Token #", 194))

    def test_invalid_char_4(self):
        self.assertTrue(TestLexer.test('&', "Error Token &", 195))

    def test_invalid_char_5(self):
        self.assertTrue(TestLexer.test('\\', "Error Token \\", 196))

    def test_invalid_char_6(self):
        self.assertTrue(TestLexer.test('\0', "Error Token \0", 197))

    def test_invalid_char_7(self):
        self.assertTrue(TestLexer.test(""" "Endline symbol endline \\n" ""","Endline symbol endline \\n,<EOF>",198))

    def test_multiple_underscore_integer_literal(self):
        self.assertTrue(TestLexer.test("1__2", "1,__2,<EOF>", 199))

    def test_custom(self):
        self.assertTrue(TestLexer.test(r'"%^&*(\n\"|\"|b6783\")&*', r'Unclosed String: %^&*(\n\"|\"|b6783\")&*',300))
        
    def test_lexer_125(self):
        my_input = "1.1e-10"
        my_expected_output = "1.1e-10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 301))

    def test_lexer_126(self):
        my_input =  "1.123_123e+10"
        my_expected_output = "1.123,_123e,+,10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 302))


    def test_lexer_127(self):
        my_input = "1.1E-10"
        my_expected_output = "1.1E-10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 303))


    def test_lexer_128(self):
        my_input =  "1.1E+10"
        my_expected_output = "1.1E+10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 304))


    def test_lexer_129(self):
        my_input = "1.1000"
        my_expected_output = "1.1000,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 305))


    def test_lexer_130(self):
        my_input = "112E1"
        my_expected_output = "112E1,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 306))


    def test_lexer_131(self):
        my_input = ".1e+10"
        my_expected_output = ".1e+10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 307))


    def test_lexer_132(self):
        my_input = ".E-10"
        my_expected_output = ".E-10,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 308))


    def test_lexer_133(self):
        my_input = "1.00E"
        my_expected_output = "1.00,E,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 309))


    def test_lexer_134(self):
        my_input = "2.13E +123"
        my_expected_output = "2.13,E,+,123,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 310))


    def test_lexer_135(self):
        my_input = "1_111.11e11"
        my_expected_output = "1111.11e11,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 311))


    def test_lexer_136(self):
        my_input = "1_111.11e11_1"
        my_expected_output = "1111.11e11,_1,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 312))


    def test_lexer_137(self):
        my_input = "1_111.1_1e11_1"
        my_expected_output = "1111.1,_1e11_1,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 313))


    def test_lexer_138(self):
        my_input = ".123_22"
        my_expected_output = ".,12322,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 314))


    def test_lexer_139(self):
        my_input = "e-123"
        my_expected_output = "e,-,123,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 315))


    def test_lexer_140(self):
        my_input = "-1.123e-123"
        my_expected_output = "-,1.123e-123,<EOF>"
        self.assertTrue(TestLexer.test(my_input, my_expected_output, 316))

    def test_unclosed_string_hoa(self):     
        input = """ "Test unclosing string \n\";" """
        expect = "Unclosed String: Test unclosing string "
        self.assertTrue(TestLexer.test(input, expect, 317))
        
    def test_error_char_hoa(self):
        input = """1131\\212"""
        expect = "1131,Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 318))