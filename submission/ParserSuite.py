import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_parser_202(self):
        """test declaration"""
        input = """
            main: function void () {}
            sum: function auto () {}
            ab: integer = 3;
            _ab: string = "string";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        

    def test_parser_203(self):
        """test declaration"""
        input = """
            main: function void () {}
            sum: function auto () {}
            _abc: integer;
            as_123, a: string = "string", "asd";
            return 123;
        """
        expect = "Error on line 6 col 12: return"
        self.assertTrue(TestParser.test(input, expect, 203))


    def test_parser_204(self):
        """test declaration"""
        input = """
            asd, abc: integer = 123, 123_123;
            a: string = "string";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    

    def test_parser_205(self):
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 205))
    

    def test_parser_206(self):
        """test declaration"""
        input = """
            main: function void(){}
            a[1] = 123; 
        """
        expect = "Error on line 3 col 13: ["
        self.assertTrue(TestParser.test(input, expect, 206))
    

    def test_parser_207(self):
        """test declaration"""
        input = """
            asd(123,123,"string");      
            main: function void(){}
        """
        expect = "Error on line 2 col 15: ("
        self.assertTrue(TestParser.test(input, expect, 207))
    

    def test_parser_208(self):
        """test variable declaration"""
        input = """
            aasd_: integer;
            123: array [1,2] of boolean;
        """
        expect = "Error on line 3 col 12: 123"
        self.assertTrue(TestParser.test(input, expect, 208))
    

    def test_parser_209(self):
        input = """
            a,b,c,d : integer = 1, 2;
        """
        expect = "Error on line 2 col 36: ;"
        self.assertTrue(TestParser.test(input, expect, 209))
    

    def test_parser_210(self):
        """test variable declaration"""
        input = """
            a,b,c : float = 1, 2, 3, 4;
        """
        expect = "Error on line 2 col 35: ,"
        self.assertTrue(TestParser.test(input, expect, 210))
    

    def test_parser_211(self):
        """test variable declaration"""
        input = """
            a,b,c : void = 1, 2, 3;
        """
        expect = "Error on line 2 col 20: void"
        self.assertTrue(TestParser.test(input, expect, 211))
    

    def test_parser_212(self):
        """test variable declaration"""
        input = """
            asd, asd, asd : array = 1, 2, 3;
        """
        expect = "Error on line 2 col 37: ="
        self.assertTrue(TestParser.test(input, expect, 212))
    

    def test_parser_213(self):
        """test variable declaration"""
        input = """
            var1 : array [1] of auto;
        """
        expect = "Error on line 2 col 32: auto"
        self.assertTrue(TestParser.test(input, expect, 213))


    def test_parser_214(self):
        """test variable declaration"""
        input = """
            abc_ : array [1] of void;
        """
        expect = "Error on line 2 col 32: void"
        self.assertTrue(TestParser.test(input, expect, 214))
    

    def test_parser_215(self):
        """test variable declaration"""
        input = """
            string: function void(){}
        """
        expect = "Error on line 2 col 12: string"
        self.assertTrue(TestParser.test(input, expect, 215))
    

    def test_parser_216(self):
        """test variable declaration"""
        input = """
            a: array = 12;
        """
        expect = "Error on line 2 col 21: ="
        self.assertTrue(TestParser.test(input, expect, 216))
    

    def test_parser_217(self):
        input = """
            a: array [1,2,3] of string = {"hello","world"};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))


    def test_parser_218(self):
        input = """
            a,b: array [1,2,3] of string = {"hello","world"}, {};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    

    def test_parser_219(self):
        input = """
            a,b,c, : string = 1,2,3,;
        """
        expect = "Error on line 2 col 19: :"
        self.assertTrue(TestParser.test(input, expect, 219))
    

    def test_parser_220(self):
        input = """
            a,b,c : int = "asf","asf","asf";
        """
        expect = "Error on line 2 col 31: 2"
        self.assertTrue(TestParser.test(input, expect, 220))
    

    def test_parser_221(self):
        input = """
            main: function boolean(inherit out var1: auto) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))


    def test_parser_222(self):
        """test param"""
        input = """
            main: function boolean(inherit a: array[1,1] of float) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))


    def test_parser_223(self):
        input = """
            main: function string(out a: array[0,1] of boolean, b: integer, inherit c: boolean) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))


    def test_parser_224(self):
        input = """
            main: function string(out a: array[1,1] of float, b: void, inherit c: int) {}
        """
        expect = "Error on line 2 col 66: void"
        self.assertTrue(TestParser.test(input, expect, 224))


    def test_parser_225(self):
        """test param"""
        input = """
            main: function string(out avc: array, asd: auto, inherit casd_: boolean,) {}
        """
        expect = "Error on line 2 col 46: ,"
        self.assertTrue(TestParser.test(input, expect, 225))
    

    def test_parser_226(self):
        input = """
            main: function string(out a: array b: auto) {}
        """
        expect = "Error on line 2 col 47: b"
        self.assertTrue(TestParser.test(input, expect, 226))
    

    def test_parser_227(self):
        input = """
            main: string() {}
        """
        expect = "Error on line 2 col 24: ("
        self.assertTrue(TestParser.test(input, expect, 227))
    

    def test_parser_228(self):
        input = """
            main: function array[1,1] of string() {
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 228))
    

    def test_parser_229(self):
        input = """
            main: function array[1,1] of string()
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 229))


    def test_parser_230(self):
        input = """
            main: function(){}
        """
        expect = "Error on line 2 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_parser_231(self):
        input = """
            main: function integer(){}
            funcname: function float() inherit main {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))


    def test_parser_232(self):
        input = """
            main: function array[1,1] of string() {
                var1 = 123;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))


    def test_parser_233(self):
        input = """
            main: function array[1,1] of string() {
                var1[0,0] = "hello world";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    

    def test_parser_234(self):
        input = """
            main: function void() {
                num1, num2 = 123, 123;
            }
        """
        expect = "Error on line 3 col 21: ="
        self.assertTrue(TestParser.test(input, expect, 234))
    

    def test_parser_235(self):
        input = """
            main: function void() {
                if(cond==precond) printInteger(cond);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))


    def test_parser_236(self):
        input = """
            main: function void() {
                if(a==b) if(b==c) printInteger(a);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))


    def test_parser_237(self):
        input = """
            main: function void() {
                if(asd==asda) 
                    if(asda==abc) {
                        asda = abc;
                    } 
                    else abc = asd;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    

    def test_parser_238(self):
        input = """
            main: function void() {
                if(a==b) 
                    if(b==c) {
                        a = b;
                    } else a = c;
                else a = d;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))


    def test_parser_239(self):
        input = """
            main: function void() {
                if(cond==precond)
            }
        """
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 239))
    

    def test_parser_240(self):
        input = """
            main: function void() {
                for(i = 0, i <= 1, i+1)
                    printf(i);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    

    def test_parser_241(self):
        input = """
            main: function void() {
                for(i[1, 1+(foo("string"::"string")+i[0])] = 0, i <= 1, i+1)
                    for(j = 0, j <= i, j+1) {
                        printf(j);
                    }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    

    def test_parser_242(self):
        input = """
            main: function void() {
                for(i = 0, i <= 1, i+1)
            }
        """
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 242))
    

    def test_parser_243(self):
        input = """
            main: function void() {
                while(1)
            }
        """
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 243))


    def test_parser_244(self):
        input = """
            main: function void() {
                while(){

                }
            }
        """
        expect = "Error on line 3 col 22: )"
        self.assertTrue(TestParser.test(input, expect, 244))
    

    def test_parser_245(self):
        input = """
            main: function void() {
                do {
                    cond = 1;
                } while (true);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    

    def test_parser_246(self):
        input = """
            main: function void() {
                testfunc(123,123,);
            }
        """
        expect = "Error on line 3 col 28: )"
        self.assertTrue(TestParser.test(input, expect, 246))
    

    def test_parser_247(self):
        input = """
            main: function void() {
                return abc;
            }
        """
        expect = "successful"    
        self.assertTrue(TestParser.test(input, expect, 247))
    

    def test_parser_248(self):
        input = """
            main: function void() {
                {

                }
            }
        """
        expect = "successful"    
        self.assertTrue(TestParser.test(input, expect, 248))
    

    def test_parser_249(self):
        input = """
            main: function void() {
                {
                    {
                        {
                            {
                                a: string = "string";
                                }
                        }
                    }
                }
            }
        """
        expect = "successful"   
        self.assertTrue(TestParser.test(input, expect, 249))
    
    def test_parser_250(self):
        input = """
            main: function void() {
                {{{}}
            }
        """
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 250))
    

#     def test_parser_251(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 251))
    

#     def test_parser_252(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 252))
    

#     def test_parser_253(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 253))
    

#     def test_parser_254(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 254))
    

#     def test_parser_255(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 255))
    

#     def test_parser_256(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 256))
    

#     def test_parser_257(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 257))
    

#     def test_parser_258(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 258))
    

#     def test_parser_259(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 259))
    

#     def test_parser_260(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 260))
    

#     def test_parser_261(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 261))
    

#     def test_parser_262(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 262))
    

#     def test_parser_263(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 263))
    

#     def test_parser_264(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 264))
    

#     def test_parser_265(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 265))
    

#     def test_parser_266(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 266))
    

#     def test_parser_267(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 267))
    

#     def test_parser_268(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 268))
    

#     def test_parser_269(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 269))
    

#     def test_parser_270(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 270))
    

#     def test_parser_271(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 271))
    

#     def test_parser_272(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 272))
    

#     def test_parser_273(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 273))
    

#     def test_parser_274(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 274))
    

#     def test_parser_275(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 275))
    

#     def test_parser_276(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 276))
    

#     def test_parser_277(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 277))
    

#     def test_parser_278(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 278))
    

#     def test_parser_279(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 279))
    

#     def test_parser_280(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 280))
    

#     def test_parser_281(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 281))
    

#     def test_parser_282(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 282))
    

#     def test_parser_283(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 283))
    

#     def test_parser_284(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 284))
    

#     def test_parser_285(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 285))
    

#     def test_parser_286(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 286))
    

#     def test_parser_287(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 287))
    

#     def test_parser_288(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 288))
    

#     def test_parser_289(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 289))
    

#     def test_parser_290(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 290))
    

#     def test_parser_291(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 291))
    

#     def test_parser_292(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 292))
    

#     def test_parser_293(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 293))
    

#     def test_parser_294(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 294))
    

#     def test_parser_295(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 295))
    

#     def test_parser_296(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 296))
    

#     def test_parser_297(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 297))
    

#     def test_parser_298(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 298))
    

#     def test_parser_299(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 299))
    

#     def test_parser_300(self):
#             input = """"""
#             expect = "successful"
#             self.assertTrue(TestParser.test(input, expect, 300))