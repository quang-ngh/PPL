
import unittest
from TestUtils import TestParser
 
 
class ParserSuite(unittest.TestCase):
    def testParser(self):
        input = """x, y, z, t: integer = false, true, 1;"""
        expect = "Error on line 1 col 36: ;"
        self.assertTrue(TestParser.test(input, expect, 201))

        input = """main: function void() {
            / This is a comment line
        }"""
        expect = "Error on line 2 col 12: /"
        self.assertTrue(TestParser.test(input, expect, 202))

        input = """_x6_yz, a69, XYZ: auto = !5, 7-69, "Hello String \\b" :: "I am another string \\t";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

        input = """_123, Yz, Aaa: auto = -5 || "Watch movie please", 5::7, {56 && false, 1, 7};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

        input = """Tai: array[2] of string = "I love watching films?" == "Hmmmm";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

        input = """X_yz, _121, dunno: floatint = 2, false, "true";"""
        expect = "Error on line 1 col 19: floatint"
        self.assertTrue(TestParser.test(input, expect, 206))

        input = """
            /*
                This is a block comment
            */
            X, y, z: boolean;;
            """
        expect = "Error on line 5 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 207))

        input = """main: function void() {
            // Line comment
            /*
                Block comment between line comments
            */
            // Line comment
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

        input = """// This is a comment
            X :: void;"""
        expect = "Error on line 2 col 14: ::"
        self.assertTrue(TestParser.test(input, expect, 209))

        input = """x: array[7, 8] of void;"""
        expect = "Error on line 1 col 18: void"
        self.assertTrue(TestParser.test(input, expect, 210))

        input = """taki: function void() {
            i : integer = 7 + 5;
            for(i = 1 :: 2 :: 3, i < 5 + 1, i + 1) {
                continue;
            }
            }"""
        expect = "Error on line 3 col 27: ::"
        self.assertTrue(TestParser.test(input, expect, 211))

        input = """main: function void() a: integer;"""
        expect = "Error on line 1 col 22: a"
        self.assertTrue(TestParser.test(input, expect, 212))

        input = """jowd: function void() {
            if(t - 4 == 0) return false;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

        input = """main: function void() {
            for(){
                a=a+1;
                if(b>f[4]) b=f[4];
            }
        }"""
        expect = "Error on line 2 col 16: )"
        self.assertTrue(TestParser.test(input, expect, 214))

        input = """main: function function() {}"""
        expect = "Error on line 1 col 15: function"
        self.assertTrue(TestParser.test(input, expect, 215))

        input = """integer: function boolean() {}"""
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input, expect, 216))

        input = """_55, 7a5: integer;"""
        expect = "Error on line 1 col 5: 7"
        self.assertTrue(TestParser.test(input, expect, 217))

        input = """demo: function void() {
            if(btl_ppl >= 7) dedung();
            else shout("desaitumlum");
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

        input = """main: function void() { a = {2, 3_44, 5} == "String"; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

        input = """: function integer() {}"""
        expect = "Error on line 1 col 0: :"
        self.assertTrue(TestParser.test(input, expect, 220))

        input = """main: function auto() { x: function = 57; }"""
        expect = "Error on line 1 col 27: function"
        self.assertTrue(TestParser.test(input, expect, 221))

        input = """empty: array[] of boolean;"""
        expect = "Error on line 1 col 13: ]"
        self.assertTrue(TestParser.test(input, expect, 222))

        input = """main: function void() {
            if(x || 7);
            }"""
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.test(input, expect, 223))

        input = """x: integer = +1234;"""
        expect = "Error on line 1 col 13: +"
        self.assertTrue(TestParser.test(input, expect, 224))

        input = """jowd: function string() {
            if(true) {
                a[5] = a[1] + 2;
                b[9] = b[5] || false;
            } else;
        }"""
        expect = "Error on line 5 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 225))

        input = """jowd: function integer() {
            if(Xyz == 2)
                if(Yzx == Xyz) jowd();
                else eliminate("PPL");
            else music = false;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

        input = """main: function void() {
            do increase(),
            while(i < 2);
            }"""
        expect = "Error on line 2 col 15: increase"
        self.assertTrue(TestParser.test(input, expect, 227))

        input = """cone: function out integer() {}"""
        expect = "Error on line 1 col 15: out"
        self.assertTrue(TestParser.test(input, expect, 228))

        input = """test(2, 3, 4);"""
        expect = "Error on line 1 col 4: ("
        self.assertTrue(TestParser.test(input, expect, 229))

        input = """main: function void() {
            for(i=0,i<5,i+1){
                if(i>1){
                    a=a+1;
                    b=true;
                    return a;
                }
                else return b;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

        input = """main: function auto() {
            i: integer;
            for(i = 11 * ab, i < 23, i + 1) {
                writeInt(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

        input = """main: function void() { a[1] = "A string \\t"; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

        input = """x, y, z: integer;;"""
        expect = "Error on line 1 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 233))

        input = """x: array[1, 2] of boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

        input = """main: function void() {
            if(false) {
                x = b + 29.99;
                b = x && true;
            } else {
                7_xyz();
            }
        }"""
        expect = "Error on line 6 col 16: 7"
        self.assertTrue(TestParser.test(input, expect, 235))

        input = """main: function float() {
            if(true) a[7] = 2;
            else continue;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

        input = """demo: function auto() {
            i: boolean;
            for(i = i == 4 && a == 2, x != i, x / x) {
                Chillies("GiacMoKhac");
                auto = auto + 3;
                if(auto < 3) continuebreak;
            }
        }"""
        expect = "Error on line 3 col 32: =="
        self.assertTrue(TestParser.test(input, expect, 237))

        input = """main: function void() {
            do increase();
            while(i < 2);
            }"""
        expect = "Error on line 2 col 15: increase"
        self.assertTrue(TestParser.test(input, expect, 238))

        input = """main: function void() { a = {2, 3_44, 5} == "String" <= 333; }"""
        expect = "Error on line 1 col 53: <="
        self.assertTrue(TestParser.test(input, expect, 239))

        input = """jowd: function void() {
            if(a ! 2) {} else {};
            }"""
        expect = "Error on line 2 col 17: !"
        self.assertTrue(TestParser.test(input, expect, 240))

        input = """main: function void() {
            do function();
            while(i < 2);
            }"""
        expect = "Error on line 2 col 15: function"
        self.assertTrue(TestParser.test(input, expect, 241))

        input = """main: function void() { do while(true); }"""
        expect = "Error on line 1 col 27: while"
        self.assertTrue(TestParser.test(input, expect, 242))

        input = """jowd: function void() {
            i: integer;
            for(12 = t && 75, x + y != 7, i / 0) {
                Call("\\t\\t\\t");
                a[75.5] = 7.8 + 0.9;
                break;
            }
        }"""
        expect = "Error on line 3 col 16: 12"
        self.assertTrue(TestParser.test(input, expect, 243))

        input = """Xyz, bct, _caA: float int = 20, 13, 74;"""
        expect = "Error on line 1 col 22: int"
        self.assertTrue(TestParser.test(input, expect, 244))

        input = """main: function void() { fact(integer, "999", "2222"); }"""
        expect = "Error on line 1 col 29: integer"
        self.assertTrue(TestParser.test(input, expect, 245))

        input = """x: integer = 5 :: 70;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

        input = """paper: function boolean(n: integer) {};"""
        expect = "Error on line 1 col 38: ;"
        self.assertTrue(TestParser.test(input, expect, 247))

        input = """Xyz, bct, _caA: float auto = 20, 13, 74;"""
        expect = "Error on line 1 col 22: auto"
        self.assertTrue(TestParser.test(input, expect, 248))

        input = """main: function void() { a = a :: 32 < "34" :: _randomF12(); }"""
        expect = "Error on line 1 col 43: ::"
        self.assertTrue(TestParser.test(input, expect, 249))

        input = """jowd: function void(jowd: integer, out jowd: float) inherit jowd {
            i: integer;
            for(i = attackOnTitan("Levi \\b"), i != 3, i / 4) {
                Eren("Roar");
                t = t - 4;
                if(x < 3) break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

        input = """main: function void() { "1"[23] = "Another random string \\t"; }"""
        expect = "Error on line 1 col 24: 1"
        self.assertTrue(TestParser.test(input, expect, 251))

        input = """kuro: function array[2] of boolean() inherit demo {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

        input = """X_yz, _121, var: floatfloat = 2, false, "true";"""
        expect = "Error on line 1 col 17: floatfloat"
        self.assertTrue(TestParser.test(input, expect, 253))

        input = """// This is a comment X:: void;"""
        expect = "Error on line 1 col 30: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 254))

        input = """main: function array [6,9,6,9] of integer() {
            i: integer;
            for(i = i::i::i, i != i, i / i) {
                i("i");
                i = i + 3;
                if(i < i) break;
            }
        }"""
        expect = "Error on line 3 col 24: ::"
        self.assertTrue(TestParser.test(input, expect, 255))

        input = """main: function void() { accuracy = "This string contains a tab symbol: \\t"; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

        input = """main: function void() { do {} while(true) }"""
        expect = "Error on line 1 col 42: }"
        self.assertTrue(TestParser.test(input, expect, 257))

        input = """x, y, z: auto;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

        input = """dsas: integer function() {}"""
        expect = "Error on line 1 col 14: function"
        self.assertTrue(TestParser.test(input, expect, 259))

        input = """function t: boolean() {}"""
        expect = "Error on line 1 col 0: function"
        self.assertTrue(TestParser.test(input, expect, 260))

        input = """main: function void() { a = "A string \\t" * 1_021.E+832 && a_12 ! arr[23]; }"""
        expect = "Error on line 1 col 64: !"
        self.assertTrue(TestParser.test(input, expect, 261))

        input = """jowd: function void() { jowd(1, 2, 3) }"""
        expect = "Error on line 1 col 38: }"
        self.assertTrue(TestParser.test(input, expect, 262))

        input = """main: function void() {
            while(i < 1) increase(i, 1);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

        input = """auto: function void(inherit n: boolean) {}"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 264))

        input = """main: function void() { a = a - 3 * 12 || b % 3e2 / "Siuuuuuuu \\b"; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

        input = """ltnc: function integer {}"""
        expect = "Error on line 1 col 23: {"
        self.assertTrue(TestParser.test(input, expect, 266))

        input = """joseph: function void() { alice(); }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

        input = """data: function void()"""
        expect = "Error on line 1 col 21: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 268))

        input = """main: function void() { 
        a = arr[23 :: "Concat tis \\f" && "Eeeee lol" :: 34]; 
        }"""
        expect = "Error on line 2 col 53: ::"
        self.assertTrue(TestParser.test(input, expect, 269))

        input = """main: function void() { lhs = "PPL" * [0, 4] && -33_9402.21 || {n, h, d}; }"""
        expect = "Error on line 1 col 38: ["
        self.assertTrue(TestParser.test(input, expect, 270))

        input = """main: function void() {
            while(true);
            }"""
        expect = "Error on line 2 col 23: ;"
        self.assertTrue(TestParser.test(input, expect, 271))

        input = """x: boolean = 5 = 70;"""
        expect = "Error on line 1 col 15: ="
        self.assertTrue(TestParser.test(input, expect, 272))

        input = """main: function void() { a = (a+b)[2]; }"""
        expect = "Error on line 1 col 33: ["
        self.assertTrue(TestParser.test(input, expect, 273))

        input = """main: function void() { a == "A random string"; }"""
        expect = "Error on line 1 col 26: =="
        self.assertTrue(TestParser.test(input, expect, 274))

        input = """demo: function integer() inherit 19 {}"""
        expect = "Error on line 1 col 33: 19"
        self.assertTrue(TestParser.test(input, expect, 275))

        input = """t: integer = -7 + 0 * 91;
            example: function integer(out test: integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

        input = """Y, z, d: auto = 1 * 2, foo(), 1 % 2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

        input = """main: function void() {
            while(i > 5) minus(i, 1);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

        input = """Tai: array[20] of float = "Float number" :: "is fun";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

        input = """x, y, z: void;"""
        expect = "Error on line 1 col 9: void"
        self.assertTrue(TestParser.test(input, expect, 280))

        input = """_Xyz, Ya, z09: integer = 5, 6, 7, integer"""
        expect = "Error on line 1 col 32: ,"
        self.assertTrue(TestParser.test(input, expect, 281))

        input = """a, b, x, y: boolean = 1, 2, 3, 4, 4, 5;"""
        expect = "Error on line 1 col 32: ,"
        self.assertTrue(TestParser.test(input, expect, 282))

        input = """main: function void() {
            i : integer = 5;
            while(true) add(i, 1);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

        input = """x: boolean = -5 * 9 + 6;
            example: function integer(out test: void) {}"""
        expect = "Error on line 2 col 48: void"
        self.assertTrue(TestParser.test(input, expect, 284))

        input = """taki: function void() {
            i : integer = 7 + 5;
            for(i = 1 :: 2, i < 5 + 1, i + 1) {
                continue;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

        input = """void: function void(inherit n: boolean) {}"""
        expect = "Error on line 1 col 0: void"
        self.assertTrue(TestParser.test(input, expect, 286))

        input = """_123, Yz, Aaa: auto = -5 || "Watch movie please", 5::7, {56 && false, 1, 7};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

        input = """_x6_yz, a69, XYZ: auto = 1 + 2, 3 - 4, "abc" :: "def";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

        input = """dsa: integer function() {}"""
        expect = "Error on line 1 col 13: function"
        self.assertTrue(TestParser.test(input, expect, 289))

        input = """g: array[] of boolean;"""
        expect = "Error on line 1 col 9: ]"
        self.assertTrue(TestParser.test(input, expect, 290))

        input = """_55, 6a5: integer;"""
        expect = "Error on line 1 col 5: 6"
        self.assertTrue(TestParser.test(input, expect, 291))

        input = """main: function void() {
                for(i = -1, i > -10, i - 1) {
                    print(i)
                }   
            }"""
        expect = "Error on line 4 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 292))

        input = """main: function void() {
            // This is a comment line
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

        input = """main: function void() {
            / This is a comment line
        }"""
        expect = "Error on line 2 col 12: /"
        self.assertTrue(TestParser.test(input, expect, 294))

        input = """main: function void() {
            This is a comment line
        }"""
        expect = "Error on line 2 col 17: is"
        self.assertTrue(TestParser.test(input, expect, 295))

        input = """main: function void() {
            // if(1 < 2) increase(i, 1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

        input = """main: function void() {
            /*
                This is a block comment
            */
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

        input = """main: function void() {
            /*
                This is a block comment
                if(1 < 2) increase(i, 1);
            */
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

        input = """Y, z, d: auto = 11*24, call(), 175%22;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

        input = """main: function void() {
            /*
                Block comment and then line comment
            */
            // Line comment
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))