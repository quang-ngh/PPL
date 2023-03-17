import unittest
from TestUtils import TestParser
import binascii

#   Nguyen Ho Quang - 2052666 - Submission 3
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
        expect = "Error on line 2 col 34: ="
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
            a,b,c : integer = "asf","asf","asf";
        """
        expect = "successful"
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
        expect = "Error on line 2 col 65: void"
        self.assertTrue(TestParser.test(input, expect, 224))


    def test_parser_225(self):
        """test param"""
        input = """
            main: function string(out avc: array, asd: auto, inherit casd_: boolean,) {}
        """
        expect = "Error on line 2 col 48: ,"
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
        expect = "Error on line 3 col 27: ="
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
        expect = "Error on line 3 col 33: )"
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
                {{ }}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))


    def test_parser_251(self):
        input  = """
            testfunction: function void() {
            while(false);
        }
        """
        expect = "Error on line 3 col 24: ;"
        self.assertTrue(TestParser.test(input, expect, 251))


    def test_parser_252(self):
        input = """
        main: function int() {
            while(1){

            }
        }
        """
        expect = "Error on line 2 col 23: int"
        self.assertTrue(TestParser.test(input, expect, 252))


    def test_parser_253(self):
        input = """
        foo: function void() {
            while(0)
        }
        """
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 253))


    def test_parser_254(self):
        input = """
        main: function void() {
            do {
                a = 1;
            } while (true);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))


    def test_parser_255(self):
        input = """
            goo: function void() {
                do {
                    do {

                    } while(false);
                } while (true);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))


    def test_parser_256(self):
        input = input = """
            main: function void() {
                do 
                    a = 1;
                while (true);
            }
        """
        expect = "Error on line 4 col 20: a"
        self.assertTrue(TestParser.test(input, expect, 256))


    def test_parser_257(self):
        input = """
            main: function void() {
                do {a = 1;}
                while (a < b && b % 2 == 0)
            }
        """
        expect = "Error on line 4 col 38: =="
        self.assertTrue(TestParser.test(input, expect, 257))


    def test_parser_258(self):
        input = """
        main: function void() {
            do {a = 1;}
            while(a == b || a >= 2 || a*b >= 18 && (a-b==0)){
                printf("hello world");
            }
        }
        """
        expect = "Error on line 4 col 30: >="
        self.assertTrue(TestParser.test(input, expect, 258))


    def test_parser_259(self):
        input = input = """
            main: callback void() {
                foo(inherit out a: string);
            }
        """
        expect = "Error on line 2 col 18: callback"
        self.assertTrue(TestParser.test(input, expect, 259))


    def test_parser_260(self):
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 260))


    def test_parser_261(self):
        input = """
            main: function void() {
                foo(123,123,);
                function_callbac: function int(){
                
                }
            }
        """
        expect = "Error on line 3 col 28: )"
        self.assertTrue(TestParser.test(input, expect, 261))


    def test_parser_262(self):
        input = """
            main: function void() {
                continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))


    def test_parser_263(self):
        input = """
            main: function void() {
                a: integer = 123;
                b: string = "string";
                c: boolean = true;
                d: float = 1.234;
                e: auto = var;
                f: string = foo();
                g: integer = var2[1,2,3];
                f: auto = (123)-(123);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    

    def test_parser_264(self):
        input = """
            main: function array[3] of integer(){
                return array{1,2,3};
            }
        """
        expect = "Error on line 3 col 23: array"
        self.assertTrue(TestParser.test(input, expect, 264))


    def test_parser_265(self):
        input = """
            main: function void() {
                a: boolean = !!!b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))


    def test_parser_266(self):
        input = input = """
            main: function void() {
                a: boolean = c||(d||g);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))


    def test_parser_267(self):
        input = """
            main: function void() {
                a: integer = a*6+b/5-c%4+d+e*f;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))


    def test_parser_268(self):
        input = """
            main: function void() {
                a: boolean = a == b && f != r || c == foo() && d != var[0];
            }
        """
        expect = "Error on line 3 col 41: !="
        self.assertTrue(TestParser.test(input, expect, 268))
    

    def test_parser_269(self):
        input = """
            main: function void() {
                a: auto = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))


    def test_parser_270(self):
        input = """if (a < 2) return 5;"""
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 270))


    def test_parser_271(self):
        input = """
            main: function void() {
                a = (a < b) < c < d;
            }
        """
        expect = "Error on line 3 col 32: <"
        self.assertTrue(TestParser.test(input, expect, 271))


    def test_parser_272(self):
        input = """
            main: function void() {
                a: auto = a::a==b::b;
            }
        """
        expect = "Error on line 3 col 33: ::"
        self.assertTrue(TestParser.test(input, expect, 272))


    def test_parser_273(self):
        input = """
            main: function void() {
                a: auto = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    

    def test_parser_274(self):
        input = """
            main: function void() {
                a: boolean = a == b && f != r || c == foo() && d != var[0];
            }
        """
        expect = "Error on line 3 col 41: !="
        self.assertTrue(TestParser.test(input, expect, 274))


    def test_parser_275(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = 43 * i + d / 328;
            i = 483 * -0.232 + 32;
            d = 423 % p * i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))


    def test_parser_276(self):
        input = """main: function void() {
            foo((foo(foo((foo)), foo, foo(foo(foo, foo(foo, foo(foo,foo,foo,foo,(foo()))))))));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    

    def test_parser_277(self):
        input = """
            main: function void () {
                while (true) {
                    while (foo) {
                        while (bar()) {
                            while(stat[2]) {
                                fa = 9;
                            }
                        }
                    }
                }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    

    def test_parser_278(self):
        input = """
        main: function void() {
            for (cond = 0, cond < 10, cond + 1) {
                donothing();
            }
            for (b = 9, b < 139023, b * 2)
                fck();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))


    def test_parser_279(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = -24 * i + d / 128;
            i = -837 * 0.362 + 32;
            d = -823 % p * i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_parser_280(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = 18 * i + d / 893;
            i = -873 * 0.673 + 32;
            d = -123 % p * i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_parser_281(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = 75 * i + d / 830;
            i = -487 * 0.253 + 32;
            d = -943 % p * i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_parser_282(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = 43 * i + d / 328;
            i = 483 * -0.232 + 32;
            d = 423 % p * i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_parser_283(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = 782 * i + d / 562;
            i = -983 * 0.312 + 32;
            d = -314 % p * i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_parser_284(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = -12 * i + d / 871;
            i = -637 * 0.214 + 32;
            d = -824 % p * i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_parser_285(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = 434 * i + d / 478;
            i = 783 * 0.521 + 32;
            d = -873 % p * i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_parser_286(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = -24 * i + d / 839;"""
        expect = "Error on line 2 col 34: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 286))


    def test_parser_287(self):
        input = """a: auto = ((!true == ! false) * barz / 43 + 443 - -438 + --430 --- 439) :: (("Hello" > 3289) < 843 * ( 328 :: 483));"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
    

    def test_parser_288(self):
        input = """main: function void(/*This is the arg of main function */) {
            if (/* put condition here */ a == 43 ) /* after which is the code */ { // put code here
                a = 3490;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
    

    def test_parser_289(self):
        input = """
        press: function void(inherit key: string) inherit touch {
            touch(key);
            doSomePressing(key);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
    

    def test_parser_290(self):
        input = str(binascii.unhexlify(
        b'67203a2066756e6374696f6e206172726179205b203020205d206f6620626f6f6c65616e202020202820696e6865726974206f75742042203a20737472696e67202020202c20696e6865726974206f7574204641203a20696e7465676572202020202c2079203a206175746f20202020202920696e6865726974206444207b207b20636f6e74696e7565203b2020207d202020666f722028204754203d2071202020202a2028206c202020202f207339202020202020262620652020202020207c7c202120222220202020202025207b207d202020202020202d206a31202820292020202020202020202920202020202d2028207b207d20202020202020202626207472756520202020202020207c7c206420202020202d207b207d2020202020202f20643420202020202d2021206720202020202a2021204b202820292020202020202020202029202020202f202d2022222020202020202a2021202d2021202120302e36202020202020202020202d2028204a2020202025207333202020202f20442028202920202020202020262620222220202020202f2041312020202025202d202d20762020202020202a204f7343672020202020207c7c2021202d2021206c20202020202020202d20734c20282029202020202020207c7c20792028202920202020202a20486b74202020202020203a3a207965372028202920202020202a2068202820292020202020202b2021205420202020202f20212021202120212047202020202020202025202120212077202820292020202020202020203e202d20772020202020252021202d20302e38202020202020202a20462020202020207c7c2030202020202025202d207120202020202520212021207b207d2020202020202020202d203320202020202f20302e343220202020202a20225c275c66222020202020202b206d2020202025202d20302020202020202a2021202d205a2020202020202a20513020282029202020202025202d202120632028202920202020202020202d202120212066616c7365202020202020202020202020292020202020207c7c2048314a202020202a205a205b206c4978302020202020203e2021207820202020202f20342e3331363937202020202020202020205d20202020202a20212030452b3137202020202020202d202d202d206832205b205320202020202d204f65202020202020203a3a20302020202020202d2069202020202f202d205f2020202020202b20222220202020202f20222220202020202f202d20212049202020202020202020202c2068202020202a202d202222202020202020202b202120302e392020202020202020203a3a207b207d2020202020202a202222202020202020207c7c2036333820202020202a202d20732020202020202020202c20792020202020207c7c207b207d2020202020202f205120282029202020202020207c7c202120212054202020202020202020202c20512020202020202626203020202020202a2031202020202020207c7c202d20212022222020202020202020203e3d207120202020202d2046202020202a202d2070202020202020202626206720202020202b203020202020202f20392020202020202d204139202020202f20302e3220202020202020203a3a2063202020202a206f2028202920202020202f202d2021206e20202020202020203e207020202020202d206b202820292020202020202b2068202020202f20212022222020202020202a20423720282029202020202020202020205d2020202020202020202626202d2021202d202d20782020202020202020202026262050202020202f20212063205b203020202020202520632028202920202020202a202d20572020202020252021202d205120282029202020202020202a205537202820292020202020202d20705439202020202020203a3a204645347155712020202020203e3d2021207b207d2020202020202020207c7c2063202020202520747275652020202020202a2021202d206c2020202020202a20342e3030652d353231393420202020202a20612020202020207c7c202d20682020202020202d2021202d207472756520202020202020202f202120212021202d2021207b207d202020202020202020202020202020205d20202020202020202020202c2058444c202820762020202020203d3d20222220202020202020203a3a2030202020202020203c207b207d202020202020202020202c207b207d2020202020202020203a3a207b207d20202020202020203c3d2022222020202020202020202c2030202020202020203c3d205020202020202020202c202222202020202020202020202920202020202a2073332020202020207c7c202d202d202d203720202020202020202a20212066616c736520202020202020202b2028207b207d202020202020202020202920202020202b202d2066616c736520202020202020202d202d202d2063363020282029202020202020202f204e20202020202b204e205b207b207d20202020202020202626207b207d2020202020202a207b207d20202020202020203d3d204220202020202026262067202020202a2021204820202020202020203a3a204b2020202020207c7c2022222020202020202d20682020202025202d204620202020202020213d202d207b207d20202020202020202020202c2022222020202020202026262071202020202a202d207b207d20202020202020202020202c20752020202020202626202d206d202020202020203c207b207d20202020202020202626202222202020202025205a202820292020202020202020202c20302020202020202b204931202020202020203a3a206d2020202020207c7c207b207d202020202020202b20302e37393030363733202020202020203d3d202222202020202025202d20422020202020202020202c206120202020202d2066312020202020202020205d2020202020202d2077342020202020202626206c20202020252021202120634820282029202020202020202a2021207634202820292020202020202a207836362028202120222220202020202020202020202920202020202f207531202020202f202d202d2021202222202020202020202020207c7c2021202d202d207b207d2020202020202020202a20282022222020202020202d205f20202020252021205f2020202020202b206b202020202f20302e35393037202020202025202d20302e31202020202020202d20622028202920202020202a202d202d2073342020202020202020262620504c202020202f20212077202820292020202020202f206e2028202920202020202020202029202020202a2021206844205b202d20302020202020202f202d2021207b207d2020202020202020202020202c207b207d202020202020202d20613330302020202020207c7c205837323520282029202020202020203c204a20202020202b205220282029202020202020202626202d20302020202020202a20793931362028202920202020202020203a3a20442020202025205f393831202020202f20502020202020202020205d202020202020202d205653202020202a20212048662028202920202020202020207c7c2073205b203420202020202a202d204f3636392028202920202020202020202626202d204a20282029202020202020202d204820202020202d2021206736202020202020207c7c204f202020202a20356535363738372020202020202020202c206f2020202020203e3d2021206a2020202020202b204a32383935383620282029202020202020207c7c2077784e20282029202020202020207c7c202d2074727565202020202020202020262620735420282029202020202020202020205d2020202020202026262028207120202020202026262077202020202f202d20302020202020202020262620543220282029202020202020207c7c20302e39393837352020202020202d2021202120222220202020202020202b202d206a202820292020202020202020213d202d203020202020202020207c7c204820202020202b2071202820292020202020202d202d20302e362020202020202020262620302020202020252066616c736520202020202025202120302e3432363038202020202020202b202120212021203020202020202020202020202029202020202f202d202d20212021204f383831313520202020202020202f207a5f2028202120532028202920202020202020207c7c204420202020202d20432020202025205320282029202020202020203e20212021205436202020202020202020202c202d202120222220202020202020202b202d20723920202020202a202d20747275652020202020202020203d3d207b207d202020202020202d202d2030202020202020202d20222220202020202520542028202920202020202520335f325f3230202020202020202626202d204220202020202520355f362020202020202d204a383932202020202f2073202020202a20302e3434652d343034352020202020202020202c2073202020202f202d20302020202020202f205434372028202920202020202f207b207d2020202020202020203a3a2046202020202a202d20702020202020202b20212021203020202020202020202d20212021202d206e202020202020202020202020292020202020202d2021206b4c6a68362020202020202d202d20282021204f4e2028202920202020202025205820282029202020202020203d3d202d202120302e3320202020202020202b2041354761202020202a2058565120282029202020202020207c7c202120382e393337352020202020202f20382020202020202d2074202020202a204c38342020202025202d20212066616c73652020202020202020202020202920202020202f2028202d20212021202d202d20212022222020202020202020202020202b2021202d2056383020282029202020202020202f202d20212037202020202020202a205932362028202920202020202020203a3a20612028202920202020202f206939202820292020202020202d2079202020202f206f202820292020202020202020202920202020202b202d2021202d2038202020202020202020207c7c2043205b20553138202820292020202020202d204c2028202920202020202a2057202020202f20444e355535202820292020202020202b202d2021202d202d20512020202020202020202d2068777a20202020202d2066616c73652020202020202a202d202222202020202020202b20345f312e3920202020202020213d20212069202820292020202020202a207b207d202020202020202d207838202820292020202020202b202d20385f315f33202020202020202b2021205a20282029202020202020202d20642020202020202020205d2020202020202020202c202d202820212066616c7365202020202020202a206d20282029202020202020207c7c202d205f694f395032202820292020202020202f2021202d202d20212021204b20282029202020202020202020202f20772028202920202020202a20282022222020202020202026262066352020202020203e3d2022222020202020202d2051202020202520552028202920202020202020203a3a207b207d20202020202020202626204e20202020202b207b207d2020202020202f20552028202920202020202020202029202020202020203a3a202120315f383920202020202020207c7c202d202120583120282029202020202020202a202120582020202020202020202920202020202020213d202d2021202d206b3179202020202020202a2021202d20442028207b207d2020202020202020203a3a206a20202020202020202c207b207d20202020202020203c3d20302020202020202020202c202222202020202020203d3d2041202020202020203a3a20692020202020202020202920202020202020202d202d2028204c202020202f202d2057202020202025202d20782028202920202020202025202222202020202020202020292020202020252050202820292020202020202d2021202222202020202020202d2066616c736520202020202020207c7c2057316834632028202920202020202f2021207820282029202020202020202b206a205b204f202020202f202120302020202020202a20212022222020202020202a202d20227e48624d765a472220202020202020207c7c20687966326e20202020202d207a65202020202f2022445c277b3b5c225c74222020202020202d20212021204c32323920282029202020202020202020203a3a202222202020202020207c7c2022222020202020202b2042202020202f2048382020202020207c7c204e6e64342020202020207c7c207b207d20202020202020207c7c202d202d206332202020202020202b2051422020202020202020205d20202020202f202120212021202d2021204e5734383339202020202020202020202b2065202020202a206a58384a205b202d202120782020202020202a2021205320282029202020202020202d20734520202020202d2021202222202020202020252021202d202222202020202020202a202120523620282029202020202020252046202020202a202d2021202d202d20512028202920202020202020202020207c7c202d206420202020202a2078333220282029202020202025206533202820292020202020202d207020202020202b2066202820292020202020202b202d202d2021202d204539202020202020202020202020205d20202020202020262620212030453333372020202020202a202d202d202d202d2021202d202e333538393535452d3220202020202020202020202020203a3a202d2028205634202020202a20633856396a642020202020202626207663543220202020202d202d2056202020202020207c7c2021202d2021206320282029202020202020202020207c7c207520202020202b2021207b207d202020202020202f2033452d37202020202025207b207d2020202020202f202d2042202020202020203e3d202222202020202020207c7c204a2020202025204e20282029202020202020207c7c204a2028202920202020202a202d2021204520202020202020207c7c2032335f30362e3736372020202020202b20302e373120202020202a204c2028202920202020202a202d2021205020202020202020207c7c20212075202020202020207c7c202d203420202020202025202d202d2021207b207d2020202020202020202f205437202820292020202020252021202120212021202d202222202020202020202020202020203a3a207472756520202020202020203c20222220202020202a206f202020202f202120632020202020202d20212021207b207d2020202020202020252021207472756520202020202020202b20672020202025202d20673230372028202920202020202025202d202d202d2075202820292020202020202020202d2047202020202f2063202820292020202020202020202920202020202f207b2055344b5620202020202026262021205f422020202020202d20476f3438326e35202020202f2065202020202020213d202222202020202020202626205220202020202b204d202020202a2021204d202020202020207c7c204a2020202025205a202820292020202020202d202d2021205520202020202020207c7c204b202020202a2053202820292020202020202d202d206120282029202020202020202b204f323320282029202020202020202626204b202020202520652020202025206b202020202f2062353532202020202f202d20372e372020202020202020203a3a204437343030342028202920202020202a205a202820292020202020202b20597920202020202020202c2069202020202f2066616c7365202020202020202b207732202020202020262620552020202020207c7c20222220202020202520642028202920202020202f207320202020202d207b207d2020202020202f20212022222020202020202a207472756520202020202025202d207b207d20202020202020202b20502020202020203c207b207d20202020202025202d207b207d202020202020202f202d202120222220202020202020202b204e312028202920202020202a2021202120792028202920202020202020202b20212074727565202020202020202020203a3a2021202d20222220202020202020202b20222220202020202f202120302e33202020202020202d202d2021202d20492020202020202025206d692020202020203c3d204f20202020202d20212030202020202020202d202120212071202020202020202d205520202020202b202120432020202020202020202c202d202d2068202020202020202026262048553035682028202920202020202520212075322028202920202020202020203c20422028202920202020202f202d2049325920202020202020203a3a206120202020202d2045202020202f202d20492020202020202d207b207d2020202020202a206b202020202a207334202820292020202020202d203420202020202a202d20212049202020202020252021202120212030202020202020202020207c7c207b207d202020202020202d2066453254504520202020202020202c20752020202025206b202820292020202020202d202d202d203020202020202020202b20502020202025202120302020202020202a2021202d207320202020202025202d2064343020282029202020202020202d202d202d207b207d202020202020202025202d2021202d204c20282029202020202020202020203e2021202120432028202920202020202020202b202120623120202020202020203a3a20552028202920202020202a207020282029202020202020202626202d20782020202020202b202d202d20212065202020202020202020262620302020202020202b20772020202025204a20202020202d20462028202920202020202520302e322020202020202d2021202d20762020202020202f206b20202020202d2066616c736520202020202020202020207d2020202020202a20302e3736333135652d362020202020202b2028202d20723020282029202020202020252063307120202020202d20302020202020202d20212021206c3320202020202020207c7c205120202020202b2046202020202a2021207a7446202020202025204f20202020202d202d20592028202920202020202020207c7c207b207d202020202020202d20443637202020202a202d2021206b202020202020202b20225c7222202020202020203e20747275652020202020202f20225c22542220202020202020202029202020202f202d202d206e202020202020202020202920666f7220282059203d202d20212021202d20212021206538394f20282029202020202020202020202020202626205720282021206e20202020202a202120212030202020202020202020203a3a2067202020202f2021206f2020202020202d207b207d202020202020252021207720202020202f205130362020202020203d3d2048202020202a207b207d202020202020202b2049202020202f20302e38333720202020202f2061202820292020202020202020202c207b207d202020202020202b20302e3835202020202020207c7c2064202820292020202020202d20212030202020202020252021202120752020202020202020203a3a207b207d202020202020202d206e202020202520302e39202020202020202626205474532020202020203e3d207b207d202020202020202b203020202020202a202d20222220202020202020202626206320202020202b206f2020202025207a202820292020202020202d2066616c736520202020202025202d205220202020202020202020292020202020202d2021202d2021202820776420202020202020202920202020202020202d206b62205b2071202020202a20212030202020202020202b202d202120302020202020202020203d3d207b207d20202020202025204d2020202020207c7c206d202820292020202020202d207b207d20202020202025202120772020202020252021202d20552020202020202020203a3a20302020202020202d2070202820292020202020202d202d2021207b207d20202020202020202020213d2054202020202f20452028202920202020202a202d204135202020202020202020205d20202020202a20212028206820202020252021205420202020202f204220282029202020202025202120312020202020202f202d206c202020202020203c3d207472756520202020202020207c7c203020202020202a202d207b207d20202020202020202b2021202222202020202020252052202820292020202020202026262022222020202020202d20212030202020202020202d20302e373620202020202f2021205720282029202020202020202b20222220202020202f202d205520202020202a20212021207b207d2020202020202020252021205852302020202020202026262021204920202020202a20212074202820292020202020202020203a3a202d20662020202020202020202920202020202f206d2020202020202020202c202120212062642020202020202520325f3720202020202520432020202025202120212021202d202d2021202d2021202d206d202020202020202020202020202a20302020202020202b202d2028202d202d206b202820292020202020202020203e2022222020202020202d20302020202020252076202820292020202020202b20502028202920202020202a206f202820292020202020202b20362020202020202b20302e333665323331202020202020202626206e20202020202b207b207d2020202020202020203a3a2021202d2022222020202020202020202626202d202d20212069202020202020202f202d206c2020202020202d202d202d20325f365f305f3032202020202020202020202029202020202020207c7c2028202d2063202820292020202020202520282059202020202020203a3a206e2020202020202020292020202020203c3d2021204420202020202a202d202d202d20747275652020202020202020202f2021202d204c307820282029202020202020202520443020282029202020202020202020292020202020203d3d206d202020202a2021202820702020202020202626205a20202020202020202920202020202520222220202020202f20302e3535452d322020202020202d202d206737202820292020202020202a203020202020202f2079202020202a2075202020202a202d20223c5d2220202020202025202d2021202d2021206720202020202020202a202d207b207d2020202020202025202120212021202820452020202020203c3d206b202020202020203a3a207b207d20202020202020203c3d203020202020202020202029202020202020202a20212021203630375f36653136333935202020202020202f2021206a2028203020202020202f202d20652020202020202d20762028202920202020202520302020202020202020202029202020202020202d2021206533626c77205b2071202020202a2065202020202f20212057202820292020202020202520212065686662633920202020202020203a3a20222220202020202f2021207b207d20202020202020202b204b20202020252021205820202020202a20222220202020202020262620222220202020202f202d207b207d2020202020202025202d20632020202020252062364c4b20282029202020202020203c3d202d2021206330303620202020202020202020205d20202020202020202626202d20553620202020202f206a4b20202020202d20682028203020202020202f20782020202020207c7c205620202020202d206a373820202020202b202120302e35332020202020202020262620492028202920202020202a2068775520282029202020202020207c7c202d202d203020202020202020202b20212035355f32202020202020202b202d207b207d202020202020202f206b33372028202920202020202a202d2021202d2030202020202020202025202d202d204a383931323231202820292020202020202020207c7c2066616c736520202020202025202d202222202020202020252061352028202920202020202f20212021202d2021206b202820292020202020202020202020203a3a202d206234202820292020202020202520212042202820292020202020202a207220282029202020202020203c3d202d20212021204a2020202020202020202020202920202020202020203a3a207b207d2020202020202a202d207b207d202020202020202f206e20202020252021202d2021205720202020202020202d2021202d20422020202020202f207535342028202920202020202f2021202d20652028202920202020202020202b20212021202d2021202120222220202020202020202020202d204835202020202a20302e353639393333202020202020202626204e20282029202020202025202d2021202120513145576632304d5a20202020202020252021202d206a6a392020202020202520212066616c7365202020202020202020262620532028202920202020202020262620282045202820292020202020202b2021206e202020202025202d202d20612020202020202020203a3a207520202020202d20222220202020202a206d2020202020207c7c204b20202020202b206b202020202f2021207b207d20202020202020202b20222220202020202a202d207a202020202025202d20747275652020202020202020203e20302020202020252021207b207d2020202020202020207c7c202d20773634202020202020202020292020202020202626202d207b207d2020202020202025202120212028202222202020202020203d3d203020202020202020203a3a207b207d2020202020202020202029202020202020202d20212021202d20747275652020202020202020202020262620212021202120212021207b207d2020202020202020202020202026262053365920282029202020202020202626207738205b20212021204d2020202020202020213d202d202120222220202020202020202020202c20302e33202020202020203c204420202020202d206e202020202a202120562020202020202b20502028202920202020202a202d202d204e202020202020202020202c20302020202020202b203020202020202520212062202020202020202626204420202020202d207b207d202020202020202d206639202020202a20393420202020202020203a3a2030202020202020202626205a20202020202d204720282029202020202020207c7c204120202020202d202120572020202020202b202d207b207d2020202020202020202020205d20202020202a20212021202d204a205b2030202020202020202020205d2020202020202020202b202d202d2072202820292020202020202020207c7c2062205b204a2020202020203c205820202020202b207a20202020252066616c7365202020202020202b202d2070352020202020202d20362e3938452d3420202020202020203a3a2022222020202020202b204420202020252021207b207d20202020202020202d202d20222220202020202025204c332028202920202020202020262620497520282029202020202020203e207b207d20202020202020207c7c20222220202020202a204720282029202020202020207c7c202222202020202025204935202020202f2021204a33393733202020202020202626202d207b207d20202020202020252041202020202a202d20323620202020202020202020205d2020202020202b206f6c352028202920202020202a202d202d20612028202920202020202020202d2021202d20212041205b207b207d202020202020202b20572020202025207120282029202020202020203d3d20512020202020207c7c207b207d202020202020202d2021207320202020202020203a3a207620202020202b20222220202020202f202d2049202020202020203c20302020202020202d20592020202025202d206a2020202020202020202c206920202020202d206d202020202a20222220202020202020213d20302020202020202d202d207b207d202020202020202020203a3a206f20202020202b205120282029202020202020203c207b207d20202020202020202626207b207d2020202020202a205420202020202020202c20302020202020202b20422020202025202222202020202020203e205a2020202020207c7c207020202020202d205020202020202020202c202d207a202020202020203d3d2030202020202020207c7c206220202020202b20302e372020202020202020202c2030202020202020207c7c207620202020202d207b207d2020202020202a2021207b207d2020202020202020202020205d202020202020202025202d2021204e20202020202020203e20282054202820292020202020202b2074727565202020202020202d204836362028202920202020202a202120312020202020202f202d2074376a3920282029202020202020252021204f2028202920202020202025207120282029202020202020203d3d204f20282029202020202020202626202d20732020202020202d202d20302020202020202a202d206130382020202020202d205736202020202f202d2021202222202020202020202f2042393520202020202d202d20302e3020202020202020207c7c2021204f6920202020202f20212021202d202120302e3620202020202020202020207c7c20553433202020202a20222220202020202520212066616c736520202020202020202b202120743620282029202020202020202020202920202020202d207320202020202020202c202d205534205b2021202d202d204420202020202020202b203020202020202a202d20302020202020202a2021202d20692020202020202a202d206d20202020202520542020202020203d3d2021202d207b207d20202020202020202f207120202020202b206a386737322028202920202020202020203a3a202120642020202020252073323732202820292020202020202b202d2021202d20452020202020202020207c7c206962202020202f2021202d20747275652020202020202020252066616c73652020202020202020213d2030202020202020207c7c20523432352020202020202626202d207b207d20202020202020202d2021202d207b207d202020202020202020207c7c2065202820292020202020202b2021202120212079202020202020202020262620225c225c5c5c622220202020202f207220282029202020202020202020205d20202020202020203e3d202d2066616c7365202020202020202a2021204b6a38202820292020202020202a2021202820302020202020202d202d207b207d2020202020202020202626205920202020202b207b207d2020202020202f202d204720202020202a2059782020202020202020292020202020252043202020202f206931326471205b202d202222202020202020202d20222220202020202f204436202020202f206c372028202920202020202a20596e6d2028202920202020202020203a3a2073202020202a20442020202020207c7c20302020202020202b204420202020202b2021207320202020202f202120222220202020202020202626206232326339316820202020202d202d207331382028202920202020202020202020205d202020202025202d2055205b207b207d20202020202020207c7c20222220202020202a20302e32343731202020202020207c7c207b207d202020202020202b206c20202020202b202d2077202020202020207c7c206e20202020202b20212030202020202020252073673633202020202a204773202020202020203a3a2022222020202020202b202d203020202020202020202626206420202020202d2046202820292020202020202d207a202020202a202d206220202020202520212066616c73652020202020202020207c7c2021202d203020202020202020202b205a343236332028202920202020202a20212077332020202020202020202c202222202020202020207c7c20743020202020202026262022222020202020202b2021205f202020202020207c7c20212074727565202020202020202020213d2042202020202520212022222020202020202f202d20212049202020202020202d20754220282029202020202020202020205d2020202020202a2021202d202d202d202d20655120282029202020202020202020202020203a3a202d20225c66222020202020202a202d202d2021202d2021206333205b207b207d2020202020202020213d202222202020202020202020205d2020202020202020202020203d3d2068314658202020202a202d202d206b7520202020202025204c3620282029202020202025202120212064205b2022222020202020202b2072202820292020202020202d2041202020202a202d2022222020202020202a207b207d2020202020202020203a3a205720202020202d2021206e202020202020207c7c202120212072202020202020202020202c207b207d20202020202020207c7c202d202120482020202020202020203a3a206c20202020202d20222220202020202520362020202020202b202d207b207d202020202020202a207b207d20202020202020202020205d20202020202020202b2069202820302020202020202d203020202020202a202d20562020202020202b202120662028202920202020202020207c7c204637202020202f20302020202020202026262044202020202f202120443120202020202f202d2074727565202020202020202f20462020202020207c7c202d206b69202820292020202020202020203a3a20666920282029202020202020207c7c2021202120225d22202020202020202a20572020202020203e207a32202820292020202020202020202c20644c202820292020202020202d202d20642020202020202b202d204c722020202020252021202d202d202d203020202020202020202025207220282029202020202020203e3d207b207d20202020202025202d202d20302020202020202020207c7c2079202020202a202d20482020202020202d206d705920202020202d205a3020202020202b2021202d20432028202920202020202020202b20225c62222020202020202020202029202020202020202020292074205b202120432020202020202d202d202d20212021206420282029202020202020202020202d202d202d2021202d20302e336533343920202020202020202020207c7c202d2021202d2057202020202020202a202d207b207d2020202020202020203e3d20212075307720202020202f202120302e37653030373620202020202020202626206e205b2067202020202020203a3a202222202020202020203d3d207b207d202020202020202020202c204220202020202020202c20432020202020203c3d205f20202020202020202c207b207d20202020202020203e2054202020202020203a3a204f2020202020203c2022222020202020202020202c206d2020202020203c3d20222220202020202020203a3a2022222020202020202020202c205220202020202020202c207b207d2020202020202020213d207b207d2020202020202020203a3a207b207d20202020202020202020205d2020202020202026262028205f2020202020203d3d2074202020202020203a3a2059202020202020202029202020202a20212021207b207d20202020202020202f204e35202820302020202020202020202c20222220202020202020202020292020202020202b202d2041202020202020202020205d20203d202d20335f345f3036312020202020202f207177202020202a202e38453620202020202020203a3a2028202d207b207d20202020202020202d2050202020202a202120512020202020252061202020202f206f2028202920202020202f202d20385f3320202020202020203e20223f222020202020202d2069793520202020202b20302e35453220202020202020202029202020202a2021202d203020202020202020202020203b20202020202020666f7220282049203d2046302020202025205f353520202020252021204120202020202f20282021202120693169202020202020202b202e383345372020202020202d202d204a2028202920202020202020207c7c207220202020202b202d204420202020202020213d207a20282029202020202020202626202d202d20717320202020202020202020292020202025204e202020202020203a3a202120302020202020202520212022545522202020202020202b202d2021202d20222220202020202020202a2021205477342028202920202020202020202020202c203933653835342020202020202b202d20282049202820292020202020202d205a202020202a202e303437333545323720202020202a204b4e202820292020202020202b2021207a20202020202f205f303738372028202920202020202f202120643420202020202f202120212053202820292020202020202025204c364c6b202020202a2071375735202020202020213d207b207d2020202020202a202d2022222020202020202f202d202d207b207d20202020202020202f2021204233383920202020202f2079343920202020202d202120212022222020202020202020207c7c202d204720282029202020202020202d2021202d2030202020202020202020202029202020202020207c7c202d20282022222020202020202b203020202020202f2021203020202020202020207c7c2021202d203020202020202020202020202920202020202f202d207520202020202a2059205b207b207d20202020202025202d204e202020202020202626202d202d2030202020202020202020262620436a642020202020203c202d2077202820292020202020202f202d202d20302e3130202020202020202020203a3a207b207d202020202020202d202d20582020202020202d203020202020202f2021204120202020202f2021202120302020202020202020207c7c207a202020202f202120512020202020202b202d202222202020202020202b2038202020202025202120222220202020202020203c2021207b207d2020202020202025202d202d204220202020202020207c7c20302020202020202b202d207b207d20202020202020202b206720202020202d202120212066616c73652020202020202020202020202c20302020202020202b206c202020202a202d202222202020202020202d2021207b207d202020202020202a20302e322020202020202d20702028202920202020202520534a202020202a20212021202120442020202020202020203e3d202d204920202020202020203a3a202e3532353832652d3133202020202020202020205d2020202020202d202d204f312028207b207d2020202020202a20302e3420202020202a207b207d2020202020202f202d202d20683037322020202020202020213d204520202020202d2067202020202a205a343820202020202d2056202020202a2052202020202a204420282029202020202020207c7c207920202020252021206620202020202f202d202d2079202020202020202d2021207020202020202020203a3a207220202020202020202c207b207d202020202020202b2022222020202020202b202d204620202020202a2021202d207b207d202020202020202020202626205a39376c324e52644f3420202020202d2021203020202020202020203c3d204a20202020202020202c202d2049202020202020207c7c207b207d20202020202025206e202820292020202020202d2051202820292020202020202d204b202020202a202120302020202020202a20222220202020202a2047202020202020213d202d202d206e2020202020202f202d204a20282029202020202020202020202c206630202820292020202020202b202d2021202222202020202020202a20747275652020202020202020203a3a207b207d20202020202020207c7c207920202020202b206e2020202025202d207b207d2020202020202020207c7c207b207d20202020202025207b207d2020202020202a202d202d207b207d202020202020202020207c7c203020202020202f207b207d202020202020202b20302020202020252021202d204f202020202020202b2021202d206634202020202020202020202029202020202020202d20212021202d2021202222202020202020202020202d2058202020202520577320282051202820292020202020202b202d202d2074727565202020202020202020207c7c202d20563439202820292020202020202f202d202120463720282029202020202020202a2066616c7365202020202020202b204220282029202020202020203e3d2021206f2020202020202d2021206e3620202020202a20414820202020202b20626a202020202a2066202020202f207b207d20202020202020207c7c202d20735f2020202020202d20642020202025202d205220202020202f202d2067202820292020202020202a205a7553622028202920202020202a202d2021202d20212030202020202020202020202d20212021202d2030202020202020202020207c7c2063742028202920202020202f2061343836323231202020202020203a3a202222202020202025202d2022222020202020202f2021207b207d202020202020202520762028202920202020202a202120212021202120222220202020202020202025202d20574b795131373220202020202f207b207d20202020202020203c2068364d20202020202020202c206720202020202b202d2021204c382020202020202f20484e20202020202d205020282029202020202025204c657041202820292020202020202d20212021206d34202820292020202020202020203e3d207472756520202020202025206e202020202520726b303320202020202020202c20222220202020202a2066616c736520202020202025202d20352020202020202f202120526220202020202a20395f375f3520202020202f2074202020202f2021202d2030202020202020202020213d206d2028202920202020202020203a3a202d202d202d207b207d20202020202020202025207b207d20202020202025204a20202020202d20776e202820292020202020202020202029202020202020202626202120793734202820292020202020202020203a3a202d20282076202020202a202d207b207d202020202020202f2021206a20282029202020202020202b2051372020202020202626207320202020202d20714b77202820292020202020202020202920202020202f202120282068202020202f204720282029202020202025205220202020202b205220202020202b2021206a20202020202f202d202d2021207b207d2020202020202020202a204975202820292020202020202b20523765202020202f202d2021202d20212066616c736520202020202020202020202020202920202020202f202d202d207b20553731323133302020202020207c7c2064202820292020202020252021207b207d202020202020202020203a3a204d20202020202d203020202020202f202d20552020202020202b2021206a2020202020252021202d207720202020202020202020207d20202020202020202a202120393020202020202025205a3920282029202020202020203d3d202d20212074727565202020202020202020207c7c202d202d2021202120212059362028206420202020252021206520202020202020213d202222202020202020202626207b207d202020202020202d20222220202020202a204920202020202020202c202222202020202020202626206d20202020202b2030202020202025202d207b207d20202020202020202020202029202020202020202020202f2021202d2021202d202d202d202d20212021202d2021202d2030452d302020202020202020202020202020202020202020202c2021206a32202820653968202020202f207b207d202020202020202d207b207d20202020202020203d3d207b207d2020202020202f2021202120572020202020202f202d20713637202820292020202020202f2021206220202020202a2021205830333820202020202020203a3a206520202020202b202d20526d4632334b7020202020202f20512020202020203e2066616c7365202020202020202b207b207d202020202020202d2052202820292020202020202020202c2021202d2041302028202920202020202020202026262021207b207d202020202020202a2052306620202020202b2021204533202820292020202020202f20212074202820292020202020202a207b207d20202020202020203e202d20444c764c4530434e39202020202020207c7c204a20202020252021207472756520202020202020202d202d202d20227d22202020202020202a202d2021203020202020202020202020202c20332020202020202b2052202020202f20212042202020202025202120302020202020202f20632028202920202020202a20462020202020207c7c202d206a2020202020202020202c205220202020202b204e2020202025207b207d202020202020202d202222202020202025202d207b207d202020202020202a2066202820292020202020202b20566d616132375a31202820292020202020202d2021202d2021207534353020202020202020202d2021206b472028202920202020202020203d3d20302020202020202b207a2020202025202d20672020202020202b202d204c20282029202020202020202b202d2022222020202020202f202d20212044202020202020252065762028202920202020202020262620714e6f20202020202b202222202020202025205f4520282029202020202020207c7c20212066616c7365202020202020202a206d202820292020202020202d20753020282029202020202025203020202020202a202d202e36652d36362020202020202020202020292020202020202f20302e30653320202020202020203a3a2021205020282029202020202020202b202d202d20212021206f20282029202020202020202020252066616c73652020202020202f2066616c7365202020202020202b207b207d2020202020202f20335f353732345f3834302e383520202020202f202120212021204a3620282046303739342020202020203e20612020202020202626204d20202020202b202d204720202020202020203a3a20462020202020202626207b207d202020202020202b20772028202920202020202020202020292020202020202020202d2053205b20225c6222202020202020203d3d2048202020202a20662028202920202020202520583337372028202920202020202520453720282029202020202020202020205d20202020202f202d2074727565202020202020202520282021202120363520202020202020202d207a79202820292020202020202b20222220202020202f2021205620202020202f205a2028202920202020202f202d207b207d202020202020202520225c6622202020202025202d2022222020202020202a207a303420282029202020202020207c7c202d205835202020202020203e3d202d20723920282029202020202020202020202920202020202b2073205b207b207d20202020202020207c7c2065202020202f202d207b207d2020202020202020202626202222202020202025202d2030202020202020202b2070202020202020203a3a20443333202820292020202020202020202c20212021204720202020202020202020205d202020202025202d207b207d202020202020202f20533330205b207420202020202b202d205f202020202020207c7c20302020202020202d20683920202020202b20592020202025205a2028202920202020202a206320282029202020202020207c7c206f202820292020202020202b207b207d2020202020202f20582028202920202020202a2021202d206c202020202020202b202d202d2074727565202020202020202020202626204a372028202920202020202f20212077202020202020203d3d202d202d204120202020202020202626202d202d2021202222202020202020202020207c7c2066202020202a202d2022222020202020202a20212045202020202025202120302e35202020202020202b202d2038395f362e342020202020202020203a3a2048202020202f202d20302020202020202a20395f352e3232392020202020202d20302020202020202d202d2021207b207d20202020202020202020213d2067202020202a202d207b207d2020202020202025202d204232312020202020202d20643220202020202b202d204e3737202020202020202020205d20202020202f202e36652d34353720202020202a2021204f35205b2021207532202820292020202020202020203a3a2021202d20472020202020202a202d202d202d206920202020202020202d202d2021206320202020202020202020205d20202020202020207c7c2028204c202020202a207b207d2020202020202f2050382028202920202020202f202d202d20302e3820202020202020252021202d20212021207b207d202020202020202020202020202029202020202a205f322028202920202020202520212028204d202020202f20747275652020202020202020262620575f5120202020202b202d20332020202020202f20222220202020202f20777720202020202020202920202020202f2077663749205b202120212021202d20732020202020202020252021202d2021202120593238202020202020202020203c3d202d202d202d2030202020202020202025207320202020202026262074727565202020202020202b2066616c73652020202020202a20412028202920202020202f2021202d202d2022222020202020202020202d2021206a3020282029202020202020202d2041364d202020202520645f35312020202020202020205d20202020202f204420202020202b202d207a2028207b207d202020202020202b203130322020202020202b20782028202920202020202f2021202d20212070554e53202020202020202a2066616c736520202020202020203e3d2022222020202020202d205f20202020252021204d2020202020202d2066616c73652020202020202a2022222020202020202b20675446202820292020202020202b2071202820292020202020202b202d20302e38323137652d3020202020202020207c7c206e334f34202020202520225c225c22222020202020202b20322020202020202d202d2071783634413538202820292020202020202020203a3a204b5420282029202020202025202120432020202020252021203020202020202020202626202d2021205520202020202020203e3d20676b71393020202020202b20225c72222020202020202b2078202820292020202020202b20442028202920202020202a20212021205220202020202020202020202920202020202020203e20282046202020202f2048202020202f204420202020202b2021202d2065323020202020202025202d20465320202020202a20432020202020203e202120302020202020202020202029202020202a2066616c7365202020202020202b202d2055754843324e20282021202d205237202020202020202d2021204c2028202920202020202020203c3d2021202d203133332e343920202020202020202b202d202d2021206c202020202020202020203a3a205920202020202020202c2021202d206d2028202920202020202020202d206f2020202025206d3220202020252021207472756520202020202020252030652b35372020202020252021202d20342e3420202020202020202b2021202e35363135452b37393420202020202020203c3d202d2045202820292020202020202f202d2049393320282029202020202020202b204a2020202020207c7c2022222020202020202020202c2021207b207d20202020202020202b204b202020202a202120302020202020202a202d205020282029202020202020202d20302e353837324535202020202020207c7c20212022222020202020202f202d202d2030202020202020202a206d202020202a207742382020202020207c7c2021202120382e3530202020202020202f204120282029202020202020203c20375f312020202020202026262066616c73652020202020202a2021207220282029202020202020202d202d202d2021207420202020202020202d2021207b207d2020202020202020207c7c202d202d2022675c5c582220202020202020202020202029202020202020202b202d206c447a4933205b204e202020202a2077202820292020202020202d206d3230353339202820292020202020202d202222202020202025207133202020202f2053202020202f202d207135323620282029202020202020202b202120222220202020202025207920282029202020202025202120392020202020202a204f39202820292020202020202b205f356a31666b202020202020203a3a20302020202020202d2051202020202f2066202820292020202020202d20212021206e202020202020202d202d2021202120302020202020202020202026262021207220202020202020262620212069302020202020202b20712020202025202230222020202020202b202d2055534a494c42202020202020202020205d20202020202025202d2066616c736520202020202020202020202920666f722028205f203d202d202d20212021202d20653520282029202020202020202020202a20212021202d20792028202920202020202020202f20212021202d207a41205b205f2020202020207c7c206720202020202b2075352020202020203d3d202222202020202020207c7c2055202020202a20212022222020202020202020203a3a2076202020202020262620302e31202020202020203c204d2020202020202626207b207d202020202020202d2030202020202025202d207b207d20202020202020202020202c206720202020202d207b207d2020202020202520442028202920202020202020203a3a2030202020202020207c7c203020202020202f20212057202020202020203d3d20642020202020207c7c206d20202020202b203020202020202f2044392020202020202020205d202020202020202020203e3d202120212021206b4e2028202920202020202020202f2021202d202120702028202920202020202020202a206e2028202920202020202f202820222220202020202020262620222220202020202520222220202020202f20222220202020202f202d202d20522020202020202f2036302020202020202020202920202020202d202d20212021207a2020202020202025202d2028202222202020202025202120412020202020202d2021202d206b20202020202020207c7c20503320202020202d20582028202920202020202a2021202d203020202020202020202b207120202020202026262061463846202020202f202120662020202020202d203020202020202f202d2021205f323631202820292020202020202020203e3d2066616c73652020202020202f2021202d20783674312020202020202020202029202020202020207c7c202d207b207d20202020202020202d2021202120212021202d202d20503035386d2020202020202020202020202020202c202d2032202020202020202d2054202820222220202020202020213d2047202020202020203a3a20792020202020203c3d202222202020202020202020202920202020202a202d20712028203020202020202020213d20522020202020202020202920202020202025202d20574420282030202020202020207c7c204820202020202b202d207b207d2020202020202020203c202222202020202020202626206220202020252063312020202020202020202920202020202025202d20212021206e2028206a202020202020202020292020202020202020202b2028204320202020202b202d202d202d20672020202020202025202d2069202820292020202020202a20302e39382020202020202d207135322028202920202020202520515f30202020202a2021207b207d202020202020202a20723520202020252021202120212046202820292020202020202020202020202920202020202b2069302028207b207d202020202020202026262030202020202020207c7c207b207d202020202020202b207b207d202020202020202b202d2066616c73652020202020202020207c7c2021207520282029202020202020202b206e6e3842585720282029202020202020202626205720282029202020202020207c7c20212071202020202020203d3d202d202d202d204c20202020202020202d202d20212065202020202020202b202d2078202020202025202d202d206f3420282029202020202020202a202d202d2021202d205120202020202020202020203a3a202d2021202120212021206e20202020202020202020202020202920202020202020213d20225c665f222020202020202b202d207b207d20202020202020202d2022222020202020202b204f2028202920202020202a203620202020202a202120222220202020202020202626206e20282029202020202020207c7c202d20212034202020202020202020203a3a207b207d2020202020202f202d205a202820292020202020202a202e363330653320202020202020262620212021204c202820292020202020202020207c7c202d202d20315f375f303220202020202020202d20592020202025202d202d2053302020202020202520747275652020202020202a20212021202d20212021202d20593320202020202020202020202b202d206c20282029202020202020202d202d2056202020202020207c7c20282021203020202020202020203c20422020202020202626206520202020202d2047202020202f20375f31335f395f355f345f343820202020202020203a3a205120202020202d207b207d2020202020202f202d203020202020202020203c3d20752020202020202626207b207d202020202020202b2021207520202020202020202029202020202f20227a70222020202020202b20417a205b20422028202920202020202020203a3a20302020202020202020202c2052202020202020262620222220202020202f204b202020202020203a3a204320202020202d207b207d2020202020202a206d20282029202020202020203c204420202020202020202c20632020202020207c7c207b207d202020202020202d2072202020202a202d207b207d202020202020202020203a3a207b207d20202020202025202d2074202020202020202020205d2020202020202026262022222020202020252066326337202820292020202020202d202d2030202020202020202d2021204d205b202222202020202020202626205f20202020202d20452028202920202020202020203a3a20222220202020202020262620302020202020202d203020202020202a2043202820292020202020202020202c207b207d20202020202020207c7c204d202020202f20752020202020202020205d20202020202020202626202120212073202820292020202020202020207c7c207430205b202120302020202020202f20212021205220202020202020203c20782020202025204520202020202d202120362020202020202020203a3a20732020202025204f37382020202020207c7c202d2066616c736520202020202020202020202c2022222020202020202d2053202820292020202020202026262021207720202020202a20302e3132202020202020202020205d20202020202f206e4e6b303620202020202d202d202d20212028207b207d20202020202020203e3d204b20202020252067313120202020202d207632363538372028202920202020202020203a3a202d20522020202020202d207a2020202025207b207d20202020202025202d2021202222202020202020202020202029202020202020202a2077205b205131362020202020207c7c205155202020202f202120512020202020202d202d20713558202020202020202020205d202020202020207c7c20212028202d2021206620202020202020207c7c202d2074727565202020202020202a2074727565202020202020202d206b333953202020202a20212021202d205a202820292020202020202020202020202920202020202f2051306d3475205b202120622020202020202b2043202020202f202d206420202020202f202120742020202020202d2074202020202f2022222020202020252066616c73652020202020202f202d207a742020202020202b202d2021207b207d20202020202020202a203432355f302e36653620202020202f20302020202020202b20572028202920202020202f20732020202020202020205d202020202020203d3d2021206c3550303739205b205120202020202d202222202020202020207c7c20302020202020202b206f3220202020202d205f202020202f202222202020202025202255236622202020202020203c3d2064202020202f20212030202020202020202d20446b3736574834202020202020203a3a2072202020202020262620302020202020202b2021203020202020202020207c7c203020202020202f2066202020202a20224f2f222020202020202020202c2022222020202020202d2066202020202f202d202222202020202020202026262030202020202020202020205d2020202020202520562020202020202626202d207020202020202f202d204935202820292020202020202f202d202d205520282029202020202020202f202d2021202d202d202d202d20723320202020202020202020252021202d207620282029202020202020202f206a3836205b20212066616c736520202020202020202d207b207d20202020202020203e2021204e2028202920202020202025205331392028202920202020202020203a3a20302020202020202b206920282029202020202020202626204b20202020202d202d20742020202020202d207b207d2020202020202a20212022222020202020202f202d202d2056202020202020202026262066616c73652020202020202520382e353533652b3534353438202020202020202020205d20202020202a2054202020202a202d204b5138205b20212065322020202020252021205537363520202020202020213d206538202820292020202020202d202d2021207032333638202020202020202026262044652028202920202020202020203a3a204b202020202f2021202222202020202020252061202820292020202020202b2021207632352020202020202b2021204320202020202f20222220202020202f204c202020202f2021203020202020202020203d3d207b207d202020202020202b20473420202020202020202c202d207b207d20202020202020202d20212022222020202020202a202d2063342020202020202b202d206b2020202020202b20222220202020202a202d2021206a202820292020202020202020203c3d2021202120365f372020202020202020202020205d202020202020202020202c20654e2028202920202020202f202d205134202820292020202020202a20212022222020202020202a202d2055202020202020203c3d2021202d20222220202020202020202020202920627265616b203b202020202020207d2020202020'
        ), encoding='ascii')
        expect = "Error on line 1 col 351: !"
        self.assertTrue(TestParser.test(input, expect, 290))
    

    def test_parser_291(self):
        input = """
        main: function void() {
            if (a > 3) {
                if (a > 4) {
                    if (a > 5) {
                        if (a > 6) {
                            if (a > 7) {
                                if (a > 8) {
                                    if (a > 9) {
                                        a = 11;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    

    def test_parser_292(self):
            input = input = str(binascii.unhexlify(b'5753203a2066756e6374696f6e20766f69642020282029207b20627265616b203b2020207d2020202020'), encoding='ascii')
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 292))
    

    def test_parser_293(self):
            input = input = """main: function void() {
                while(i == i && i == i) 
                randomFunc(100, i > 5, i - 2);
            }"""
            expect = "Error on line 2 col 34: =="
            self.assertTrue(TestParser.test(input, expect, 293))
    

    def test_parser_294(self):
            input = "a: integer = - ! - foo();"
            expect = "Error on line 1 col 15: !"
            self.assertTrue(TestParser.test(input, expect, 294))
    

    def test_parser_295(self):
            input = input = """
            // This is the line comment
            degreeOfFreedom: auto = 1024;
            batteryLevel: integer = 100;

            main: function void() {
                prinf("Degree of freedom is");
                prinf(degreeOfFreedom);
                prinf("\\n");

                p: float = 0.328;
                i: int = 0.0;
                d: auto = 1.3;

                while ((checkCompleted()) && (batteryLevel > 10))
                    run(p, i, d);
            }

            run: function void(inherit out p: float, out i: float, out d: float) inherit func{
                p = 43 * i + d / 328;
                i = 483 * -0.232 + 32;
                d = 423 % p * i;
            }
            """
            expect = "Error on line 12 col 19: int"
            self.assertTrue(TestParser.test(input, expect, 295))
    

    def test_parser_296(self):
            input = """main: function void()
            {
                if (x > 3) x = 3;
                else x = 4;
                else x = 5;
            }
            """
            expect =  "Error on line 5 col 16: else"
            self.assertTrue(TestParser.test(input, expect, 296))
    

    def test_parser_297(self):
            input = """
            main: function void()
            {
                for (integer i = 1, i < n, i + 1)
                {
                    continue;
                }
            }
            """
            expect = "Error on line 4 col 21: integer"
            self.assertTrue(TestParser.test(input, expect, 297))
    

    def test_parser_298(self):
            input = """
            main: function void() inherit sum
            {
                return sum(sum());
            }
            sum = function void()
            {
                return "Nothing";
            }
            """
            expect = "Error on line 6 col 16: ="
            self.assertTrue(TestParser.test(input, expect, 298))
    

    def test_parser_299(self):
            input = """"""
            expect = "Error on line 1 col 0: <EOF>"
            self.assertTrue(TestParser.test(input, expect, 299))
    

    def test_parser_300(self):
        input = """main: function void()
        {
            x = !(x+y-z*t-g/i && true :: "cde" || a%z + l :: "abc"  || false);
        }"""
        expect = "Error on line 3 col 58: ::"
        self.assertTrue(TestParser.test(input, expect, 300))

    
