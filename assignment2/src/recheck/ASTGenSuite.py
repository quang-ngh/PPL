
import unittest
from TestUtils import TestAST
from AST import *

"""
Nguyen Ho Quang - 2052666
"""

class ASTGenSuite(unittest.TestCase):
    """Test suite for assignment 2
    Programming Language Principle
    """

    def test_main_function(self):
        """Simple program with only empty main function"""
        prog = """main: function void() {
}"""
        expect = str(Program([FuncDecl("main", VoidType(), [], None, BlockStmt([]))]))
        self.assertTrue(TestAST.test(prog, expect, 300), f"Correct: \n{expect}")
   
    def test_vardecl_1(self):
        input   =   """x, y, z: integer = 1,2,3;
                    a, b: float = 3.2, 2.2;
                    isTrue, isFale : boolean = true, false;"""
        expect  =   """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType, FloatLit(3.2))
	VarDecl(b, FloatType, FloatLit(2.2))
	VarDecl(isTrue, BooleanType, BooleanLit(True))
	VarDecl(isFale, BooleanType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecl_2(self):
        input   =   """x,y,z: float = 1.2, 1e-3, 1e-2;
                    a,b: integer;
                    a_aas : auto = -2;
                    string1, string2: auto = "helo world", "diffusion models";"""
        expect  =   """Program([
	VarDecl(x, FloatType, FloatLit(1.2))
	VarDecl(y, FloatType, FloatLit(0.001))
	VarDecl(z, FloatType, FloatLit(0.01))
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(a_aas, AutoType, UnExpr(-, IntegerLit(2)))
	VarDecl(string1, AutoType, StringLit(helo world))
	VarDecl(string2, AutoType, StringLit(diffusion models))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_vardecl_3(self):
        input   =   """a: array[3,3] of integer;
                    b, c: array[100] of integer;
                    x, y: array[4] of float;"""
        expect  =   """Program([
	VarDecl(a, ArrayType([3, 3], IntegerType))
	VarDecl(b, ArrayType([100], IntegerType))
	VarDecl(c, ArrayType([100], IntegerType))
	VarDecl(x, ArrayType([4], FloatType))
	VarDecl(y, ArrayType([4], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_vardecl_4(self):
        input   =   """a : integer = 3;
                    b : float = 4.2;
                    x, y: auto = "hello world", " my name is";
                    concatt : auto = x :: y;"""
        expect  =   """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, FloatType, FloatLit(4.2))
	VarDecl(x, AutoType, StringLit(hello world))
	VarDecl(y, AutoType, StringLit( my name is))
	VarDecl(concatt, AutoType, BinExpr(::, Id(x), Id(y)))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_vardecl_5(self):
        input   =   """a,b,c : auto = false, true, true;
                    arr1 : array[4] of integer;
                    arr2:   array[3,3] of float;"""
        expect  =   """Program([
	VarDecl(a, AutoType, BooleanLit(False))
	VarDecl(b, AutoType, BooleanLit(True))
	VarDecl(c, AutoType, BooleanLit(True))
	VarDecl(arr1, ArrayType([4], IntegerType))
	VarDecl(arr2, ArrayType([3, 3], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_vardecl_6(self):
        input   =   """a,b,c: float;
                    x,y,z: integer;"""
        expect  =   """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_vardecl_7(self):
        input   =   """x,y : auto = 1,23;
                    z,t: integer = x + y, x-y;"""
        expect  =   """Program([
	VarDecl(x, AutoType, IntegerLit(1))
	VarDecl(y, AutoType, IntegerLit(23))
	VarDecl(z, IntegerType, BinExpr(+, Id(x), Id(y)))
	VarDecl(t, IntegerType, BinExpr(-, Id(x), Id(y)))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_vardecl_8(self):
        input   =   """x,a : integer = 1,2;
                    b: string = "hello"::" world";"""
        expect  =   """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(a, IntegerType, IntegerLit(2))
	VarDecl(b, StringType, BinExpr(::, StringLit(hello), StringLit( world)))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_vardecl_9(self):
        input   =   """a,b : integer = 2,3;
                    x: auto       = 1.2;
                    arrr    : array[3] of string;
                    """
        expect  =   """Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	VarDecl(b, IntegerType, IntegerLit(3))
	VarDecl(x, AutoType, FloatLit(1.2))
	VarDecl(arrr, ArrayType([3], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_vardecl_10(self):
        input   =   """a,b : auto = "hello world", "hello";
                    a : boolean;
                    main : function void(a: boolean){
                        a = (1 >= 3) && (!true);
                    }
                    """
        expect  =   """Program([
	VarDecl(a, AutoType, StringLit(hello world))
	VarDecl(b, AutoType, StringLit(hello))
	VarDecl(a, BooleanType)
	FuncDecl(main, VoidType, [Param(a, BooleanType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, BinExpr(>=, IntegerLit(1), IntegerLit(3)), UnExpr(!, BooleanLit(True))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    
    ############################ END TEST VARDECL ##################################
    
    def test_vardecl_full_1(self):
        input   =   """fact: function integer(num: integer){
                        if (num == 1){
                            return 1;
                        }
                        return num * fact(num-1);
                    }"""
        expect  =   """Program([
	FuncDecl(fact, IntegerType, [Param(num, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(num), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))])), ReturnStmt(BinExpr(*, Id(num), FuncCall(fact, [BinExpr(-, Id(num), IntegerLit(1))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_vardecl_full_2(self):
        input   =   """sum: auto = 0;
                    arr : array[10] of integer;
                    num_iter : integer = len(arr);
                    main : function void(){
                        for (i = 0, i < num_iters, i + 1)
                        {
                            sum = sum + arr[idx];
                        }
                    }"""
        expect="""Program([
	VarDecl(sum, AutoType, IntegerLit(0))
	VarDecl(arr, ArrayType([10], IntegerType))
	VarDecl(num_iter, IntegerType, FuncCall(len, [Id(arr)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(num_iters)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(idx)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_vardecl_full_3(self):
        input   =   """GCD: function integer(a: integer, b: integer){
                        while(a != b){
                            if (a< b){
                                b = b-a;
                            }
                            if (a>b){
                                a = a - b;
                            }
                        }
                        return a;
                    }
                    simplify: function void(out a: integer, out b: integer)
                    {
                        d = GCD(a, b);
                        a = a / d;
                        b = b / d;
                    }"""
        expect  =   """Program([
	FuncDecl(GCD, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(!=, Id(a), Id(b)), BlockStmt([IfStmt(BinExpr(<, Id(a), Id(b)), BlockStmt([AssignStmt(Id(b), BinExpr(-, Id(b), Id(a)))])), IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), Id(b)))]))])), ReturnStmt(Id(a))]))
	FuncDecl(simplify, VoidType, [OutParam(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([AssignStmt(Id(d), FuncCall(GCD, [Id(a), Id(b)])), AssignStmt(Id(a), BinExpr(/, Id(a), Id(d))), AssignStmt(Id(b), BinExpr(/, Id(b), Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_vardecl_full_4(self):
        input   =   """money_type: array[9] of integer = {1, 2, 5, 10, 20 ,50 ,100, 200, 500};
                    withdraw: function void(cond: integer, out money: array[9] of integer)
                    {
                        i: integer = 8;
                        while (cond > 0)
                        {
                            if (cond > money_type[i])
                            {
                                cond = cond - money_type[i];
                                money[i] = money[i] + 1;
                            }
                            else
                            {
                                i = i - 1;
                            }
                            if (i == -1) break;
                        }
                    }"""
        expect  =   """Program([
	VarDecl(money_type, ArrayType([9], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(5), IntegerLit(10), IntegerLit(20), IntegerLit(50), IntegerLit(100), IntegerLit(200), IntegerLit(500)]))
	FuncDecl(withdraw, VoidType, [Param(cond, IntegerType), OutParam(money, ArrayType([9], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(8)), WhileStmt(BinExpr(>, Id(cond), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(>, Id(cond), ArrayCell(money_type, [Id(i)])), BlockStmt([AssignStmt(Id(cond), BinExpr(-, Id(cond), ArrayCell(money_type, [Id(i)]))), AssignStmt(ArrayCell(money, [Id(i)]), BinExpr(+, ArrayCell(money, [Id(i)]), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), IfStmt(BinExpr(==, Id(i), UnExpr(-, IntegerLit(1))), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_vardecl_full_5(self):
        input   ="""fanControl: function void()
                {
                    t: float = getTemperature();
                    if (t > 30)
                    {
                        set_fanspeed(100);
                    }
                    else if (t > 25)
                    {
                        set_fanspeed(75);
                    }
                    else if (t > 20)
                    {
                        set_fanspeed(50);
                    }
                    else turnoff();
                }"""
        expect="""Program([
	FuncDecl(fanControl, VoidType, [], None, BlockStmt([VarDecl(t, FloatType, FuncCall(getTemperature, [])), IfStmt(BinExpr(>, Id(t), IntegerLit(30)), BlockStmt([CallStmt(set_fanspeed, IntegerLit(100))]), IfStmt(BinExpr(>, Id(t), IntegerLit(25)), BlockStmt([CallStmt(set_fanspeed, IntegerLit(75))]), IfStmt(BinExpr(>, Id(t), IntegerLit(20)), BlockStmt([CallStmt(set_fanspeed, IntegerLit(50))]), CallStmt(turnoff, ))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_vardecl_full_6(self):
        input="""getCandS: function void(r: float, out c: float, out s: float)
        {
            pi: float = 3.14;
            c = r * 2 * pi;
            s = c * r / 2;
        }"""
        expect="""Program([
	FuncDecl(getCandS, VoidType, [Param(r, FloatType), OutParam(c, FloatType), OutParam(s, FloatType)], None, BlockStmt([VarDecl(pi, FloatType, FloatLit(3.14)), AssignStmt(Id(c), BinExpr(*, BinExpr(*, Id(r), IntegerLit(2)), Id(pi))), AssignStmt(Id(s), BinExpr(/, BinExpr(*, Id(c), Id(r)), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_vardecl_full_7(self):
        input="""main: function void()
        {
            arr1: array[10] of integer;
            arr1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            for (idx = 0, idx < 10, idx + 1)
            {
                if (arr[idx] % 3 == 0) printInteger(arr[idx]);
            }
        }"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr1, ArrayType([10], IntegerType)), AssignStmt(Id(arr1), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), ForStmt(AssignStmt(Id(idx), IntegerLit(0)), BinExpr(<, Id(idx), IntegerLit(10)), BinExpr(+, Id(idx), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(idx)]), IntegerLit(3)), IntegerLit(0)), CallStmt(printInteger, ArrayCell(arr, [Id(idx)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_vardecl_full_8(self):
        input="""isPrime: function boolean(num: integer)
        {
            for (i = 2, i < sqrt(num), i + 1)
            {
                if (num % i == 0) return false;
            }
            
            return true;
        }"""
        expect="""Program([
	FuncDecl(isPrime, BooleanType, [Param(num, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), FuncCall(sqrt, [Id(num)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(num), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_vardecl_full_9(self):
        input   =   """main: function void()
                {
                n: integer;
                n = getInteger();

                printInteger(n / 10, n - n / 100 * 100);
                }"""
        expect  =   """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(getInteger, [])), CallStmt(printInteger, BinExpr(/, Id(n), IntegerLit(10)), BinExpr(-, Id(n), BinExpr(*, BinExpr(/, Id(n), IntegerLit(100)), IntegerLit(100))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_vardecl_full_10(self):
        input="""main: function void()
        {
            arr: array[10, 10] of integer;
            for (row = 0, row < 10, row + 1)
            {
                for (col = 0, col < 10, col + 1)
                {
                    if (isPrime(arr[row, col])) printInteger(arr[row, col]);
                }
            }
        }"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10, 10], IntegerType)), ForStmt(AssignStmt(Id(row), IntegerLit(0)), BinExpr(<, Id(row), IntegerLit(10)), BinExpr(+, Id(row), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(col), IntegerLit(0)), BinExpr(<, Id(col), IntegerLit(10)), BinExpr(+, Id(col), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(isPrime, [ArrayCell(arr, [Id(row), Id(col)])]), CallStmt(printInteger, ArrayCell(arr, [Id(row), Id(col)])))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    ############################## END TEST FULLFORMAT #############################


    def test_func_1(self):
        input = """
        main: function void () {}
        sum: function auto () {}
        ab: integer = 3;
        _ab: string = "string";
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(sum, AutoType, [], None, BlockStmt([]))
	VarDecl(ab, IntegerType, IntegerLit(3))
	VarDecl(_ab, StringType, StringLit(string))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_func_2(self):
        input = """
        asd, abc: integer = 123, 123_123;
        a: string = "string";
    """
        expect = """Program([
	VarDecl(asd, IntegerType, IntegerLit(123))
	VarDecl(abc, IntegerType, IntegerLit(123123))
	VarDecl(a, StringType, StringLit(string))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_func_3(self):
        input = """
        main: function boolean(inherit out var1: auto) {}
    """
        expect = """Program([
	FuncDecl(main, BooleanType, [InheritOutParam(var1, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_func_4(self):
        input = """
        main: function string(out a: array[0,1] of boolean, b: integer, inherit c: boolean) {}
    """
        expect = """Program([
	FuncDecl(main, StringType, [OutParam(a, ArrayType([0, 1], BooleanType)), Param(b, IntegerType), InheritParam(c, BooleanType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_func_5(self):
        input = """
        main: function integer(){}
        funcname: function float() inherit main {}
    """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([]))
	FuncDecl(funcname, FloatType, [], main, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_func_6(self):
        input = """
        main: function array[1,1] of string() {
            var1[0,0] = "hello world";
        }
    """
        expect = """Program([
	FuncDecl(main, ArrayType([1, 1], StringType), [], None, BlockStmt([AssignStmt(ArrayCell(var1, [IntegerLit(0), IntegerLit(0)]), StringLit(hello world))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_func_7(self):
        input = """
        main: function void() {
            if(asd==asda) 
                if(asda==abc) {
                    asda = abc;
                } 
                else abc = asd;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(asd), Id(asda)), IfStmt(BinExpr(==, Id(asda), Id(abc)), BlockStmt([AssignStmt(Id(asda), Id(abc))]), AssignStmt(Id(abc), Id(asd))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_func_8(self):
        input = """
        main: function void() {
            if(a==b) 
                if(b==c) {
                    a = b;
                } else a = c;
            else a = d;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), IfStmt(BinExpr(==, Id(b), Id(c)), BlockStmt([AssignStmt(Id(a), Id(b))]), AssignStmt(Id(a), Id(c))), AssignStmt(Id(a), Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_func_9(self):
        input = """
        main: function void() {
            for(i = 0, i <= 1, i+1)
                printf(i);
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printf, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_func_10(self):
        input = """
        main: function void() {
            for(i[1, 1+(foo("string"::"string")+i[0])] = 0, i <= 1, i+1)
                for(j = 0, j <= i, j+1) {
                    printf(j);
                }
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(i, [IntegerLit(1), BinExpr(+, IntegerLit(1), BinExpr(+, FuncCall(foo, [BinExpr(::, StringLit(string), StringLit(string))]), ArrayCell(i, [IntegerLit(0)])))]), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<=, Id(j), Id(i)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, Id(j))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_func_11(self):
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
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([VarDecl(a, StringType, StringLit(string))])])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_func_12(self):
        input = """
        main: function void() {
            {{ }}
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_func_13(self):
        input = """
        goo: function void() {
            do {
                do {

                } while(false);
            } while (true);
        }
    """
        expect = """Program([
	FuncDecl(goo, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_func_14(self):
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
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(123)), VarDecl(b, StringType, StringLit(string)), VarDecl(c, BooleanType, BooleanLit(True)), VarDecl(d, FloatType, FloatLit(1.234)), VarDecl(e, AutoType, Id(var)), VarDecl(f, StringType, FuncCall(foo, [])), VarDecl(g, IntegerType, ArrayCell(var2, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])), VarDecl(f, AutoType, BinExpr(-, IntegerLit(123), IntegerLit(123)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_func_15(self):
        input = """
        main: function void() {
            a: boolean = c||(d||g);
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, BinExpr(||, Id(c), BinExpr(||, Id(d), Id(g))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_func_16(self):
        input = """
        main: function void() {
            a: auto = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, BinExpr(::, StringLit(string), BinExpr(==, BinExpr(&&, Id(a), BinExpr(+, Id(c), BinExpr(*, IntegerLit(2), IntegerLit(3)))), BinExpr(||, BinExpr(-, Id(b), BinExpr(*, IntegerLit(2), UnExpr(!, UnExpr(-, ArrayCell(b, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))))), Id(d)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_func_17(self):
        input = """main: function void() {
        foo((foo(foo((foo)), foo, foo(foo(foo, foo(foo, foo(foo,foo,foo,foo,(foo()))))))));
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, FuncCall(foo, [FuncCall(foo, [Id(foo)]), Id(foo), FuncCall(foo, [FuncCall(foo, [Id(foo), FuncCall(foo, [Id(foo), FuncCall(foo, [Id(foo), Id(foo), Id(foo), Id(foo), FuncCall(foo, [])])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_func_18(self):
        input = """
    main: function void() {
        for (cond = 0, cond < 10, cond + 1) {
            donothing();
        }
        for (b = 9, b < 139023, b * 2)
            fck();
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(cond), IntegerLit(0)), BinExpr(<, Id(cond), IntegerLit(10)), BinExpr(+, Id(cond), IntegerLit(1)), BlockStmt([CallStmt(donothing, )])), ForStmt(AssignStmt(Id(b), IntegerLit(9)), BinExpr(<, Id(b), IntegerLit(139023)), BinExpr(*, Id(b), IntegerLit(2)), CallStmt(fck, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_func_19(self):
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
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(4)), BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(5)), BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(6)), BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(7)), BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(8)), BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(9)), BlockStmt([AssignStmt(Id(a), IntegerLit(11))]))]))]))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_func_20(self):
        input = """main: function void() {
            if(true) {
                y = b + 29.99;
                b = x && true;
            } else {
                _xyz();
            }
        }"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(y), BinExpr(+, Id(b), FloatLit(29.99))), AssignStmt(Id(b), BinExpr(&&, Id(x), BooleanLit(True)))]), BlockStmt([CallStmt(_xyz, )]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_func_21(self):
        input = """main: function array [6,6,6,6] of integer() {
            i: integer;
            for(i = i::i, i != i, i / i) {
                i("i");
                i = i + 3;
                if(i < i) break;
            }
        }"""
        expect="""Program([
	FuncDecl(main, ArrayType([6, 6, 6, 6], IntegerType), [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), BinExpr(::, Id(i), Id(i))), BinExpr(!=, Id(i), Id(i)), BinExpr(/, Id(i), Id(i)), BlockStmt([CallStmt(i, StringLit(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(3))), IfStmt(BinExpr(<, Id(i), Id(i)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_func_22(self):
        input = """foo: function string() {
            if(true) {
                arr1[5] = arr1[1] + 2;
                arr2[9] = arr2[5] || false;
            }
        }"""
        expect="""Program([
	FuncDecl(foo, StringType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([AssignStmt(ArrayCell(arr1, [IntegerLit(5)]), BinExpr(+, ArrayCell(arr1, [IntegerLit(1)]), IntegerLit(2))), AssignStmt(ArrayCell(arr2, [IntegerLit(9)]), BinExpr(||, ArrayCell(arr2, [IntegerLit(5)]), BooleanLit(False)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_func_23(self):
        input = """
        max: function auto(A: array[10] of integer)
        {
            max_ele, i: integer = A[0], 0;
            for (i = 1, i < 10, i + 1)
            {
                if (max_ele < A[i]) max_ele = A[i];
            }

            return max_ele;
        }
        """
        expect="""Program([
	FuncDecl(max, AutoType, [Param(A, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(max_ele, IntegerType, ArrayCell(A, [IntegerLit(0)])), VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(max_ele), ArrayCell(A, [Id(i)])), AssignStmt(Id(max_ele), ArrayCell(A, [Id(i)])))])), ReturnStmt(Id(max_ele))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_func_24(self):
        input = """
        main: function void()
        {
            while (true)
            {
                x = x + 2;
                a = a + x;
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(2))), AssignStmt(Id(a), BinExpr(+, Id(a), Id(x)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_func_25(self):
        input = """
        main: function void()
        {
            while (!x)
            {
                x = x % 2 == 0;
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(UnExpr(!, Id(x)), BlockStmt([AssignStmt(Id(x), BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_func_26(self):
        input = """
        main: function void()
        {
            x: float = 0.2;
            while (foo(x) >= 10) x = (x + 2) / 3;
            printInteger(foo(x));
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(0.2)), WhileStmt(BinExpr(>=, FuncCall(foo, [Id(x)]), IntegerLit(10)), AssignStmt(Id(x), BinExpr(/, BinExpr(+, Id(x), IntegerLit(2)), IntegerLit(3)))), CallStmt(printInteger, FuncCall(foo, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_func_27(self):
        input = """
        main: function integer()
        {
            while (x < 3)
            {
                x = x + 1;
            }
            return x;
        }
        """
        expect="""Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))])), ReturnStmt(Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_func_28(self):
        input = """
        main: function void()
            {
                {
                    r, s: integer;
                    r = 2.0;
                    a, b: array [5] of integer;
                    s = r * r * myPI;
                    a[0] = a * s;
                }
            } 
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(*, Id(a), Id(s)))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_func_29(self):
        input = """
        fact: function integer(x: integer)
            {
                ans: integer = 1;
                for (i = 1, i <= x, i + 1) ans = ans * i;
                return ans;
            }

            main: function void()
            {
                x: integer;
                printString("x = ");
                readInteger(x);
                printString("x! = ");
                printInteger(fact(x));
            }
        """
        expect="""Program([
	FuncDecl(fact, IntegerType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(ans, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(x)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(ans), BinExpr(*, Id(ans), Id(i)))), ReturnStmt(Id(ans))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), CallStmt(printString, StringLit(x = )), CallStmt(readInteger, Id(x)), CallStmt(printString, StringLit(x! = )), CallStmt(printInteger, FuncCall(fact, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_func_30(self):
        input = """
        max: function float(arr: auto)
            {
                ans: float = arr[0];
                for (i = 1, i < len(arr), i + 1)
                {
                    if (ans < arr[i]) ans = arr[i];
                }

                return ans;
            }

            A: array[4] of float;
            main: function void()
            {
                A = {-1.0, 3e-4, 3_22.55, -5};
                printInteger(max(A));
            }
        """
        expect="""Program([
	FuncDecl(max, FloatType, [Param(arr, AutoType)], None, BlockStmt([VarDecl(ans, FloatType, ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(len, [Id(arr)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(ans), ArrayCell(arr, [Id(i)])), AssignStmt(Id(ans), ArrayCell(arr, [Id(i)])))])), ReturnStmt(Id(ans))]))
	VarDecl(A, ArrayType([4], FloatType))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(A), ArrayLit([UnExpr(-, FloatLit(1.0)), FloatLit(0.0003), FloatLit(322.55), UnExpr(-, IntegerLit(5))])), CallStmt(printInteger, FuncCall(max, [Id(A)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_func_31(self):
        input = """
        /* Some useless code here */
            // Static variables
            my_stactic_var: integer;

            inc: function void(out x: integer)
            // Increase input by 1
            {
                x = x + 1;
            }

            main: function void()
            {
                a, b: integer = 1, 2;
                inc(a);
                if (a == b) inc(b);
                else inc(a);

                for (_var = 0, _var < 5, _var + 1)
                {
                    inc(a);
                    a = a - b * 2;
                }

                /* My useless block */
                {
                    {
                        {
                            _var = a - 1;
                        }
                    }
                }
            }
        """
        expect="""Program([
	VarDecl(my_stactic_var, IntegerType)
	FuncDecl(inc, VoidType, [OutParam(x, IntegerType)], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), CallStmt(inc, Id(a)), IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(inc, Id(b)), CallStmt(inc, Id(a))), ForStmt(AssignStmt(Id(_var), IntegerLit(0)), BinExpr(<, Id(_var), IntegerLit(5)), BinExpr(+, Id(_var), IntegerLit(1)), BlockStmt([CallStmt(inc, Id(a)), AssignStmt(Id(a), BinExpr(-, Id(a), BinExpr(*, Id(b), IntegerLit(2))))])), BlockStmt([BlockStmt([BlockStmt([AssignStmt(Id(_var), BinExpr(-, Id(a), IntegerLit(1)))])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_func_32(self):
        input = """
        main: function void(n : integer, A: array[10] of integer)
        {
            x, y: integer;
            for (x = 0, x < n, x + 1)
            {
                for (y = 0, y < n, y + 1)
                {
                    printInteger(A[x, y]);
                }
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [Param(n, IntegerType), Param(A, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(n)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(0)), BinExpr(<, Id(y), Id(n)), BinExpr(+, Id(y), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(A, [Id(x), Id(y)]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_func_33(self):
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
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([VarDecl(a, StringType, StringLit(string))])])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_func_34(self):
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
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(123)), VarDecl(b, StringType, StringLit(string)), VarDecl(c, BooleanType, BooleanLit(True)), VarDecl(d, FloatType, FloatLit(1.234)), VarDecl(e, AutoType, Id(var)), VarDecl(f, StringType, FuncCall(foo, [])), VarDecl(g, IntegerType, ArrayCell(var2, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])), VarDecl(f, AutoType, BinExpr(-, IntegerLit(123), IntegerLit(123)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_func_35(self):
        input = """
            main: function void() {
                a: auto = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
            }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, BinExpr(::, StringLit(string), BinExpr(==, BinExpr(&&, Id(a), BinExpr(+, Id(c), BinExpr(*, IntegerLit(2), IntegerLit(3)))), BinExpr(||, BinExpr(-, Id(b), BinExpr(*, IntegerLit(2), UnExpr(!, UnExpr(-, ArrayCell(b, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))))), Id(d)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_func_36(self):
        input = """
            main: function void() {
                a: auto = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
            }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, BinExpr(::, StringLit(string), BinExpr(==, BinExpr(&&, Id(a), BinExpr(+, Id(c), BinExpr(*, IntegerLit(2), IntegerLit(3)))), BinExpr(||, BinExpr(-, Id(b), BinExpr(*, IntegerLit(2), UnExpr(!, UnExpr(-, ArrayCell(b, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))))), Id(d)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_func_37(self):
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
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([WhileStmt(Id(foo), BlockStmt([WhileStmt(FuncCall(bar, []), BlockStmt([WhileStmt(ArrayCell(stat, [IntegerLit(2)]), BlockStmt([AssignStmt(Id(fa), IntegerLit(9))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_func_38(self):
        input = """
        main: function void() {
            for (cond = 0, cond < 10, cond + 1) {
                donothing();
            }
            for (b = 9, b < 139023, b * 2)
                fck();
        }"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(cond), IntegerLit(0)), BinExpr(<, Id(cond), IntegerLit(10)), BinExpr(+, Id(cond), IntegerLit(1)), BlockStmt([CallStmt(donothing, )])), ForStmt(AssignStmt(Id(b), IntegerLit(9)), BinExpr(<, Id(b), IntegerLit(139023)), BinExpr(*, Id(b), IntegerLit(2)), CallStmt(fck, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_func_39(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = 75 * i + d / 830;
            i = -487 * 0.253 + 32;
            d = -943 % p * i;
        }"""
        expect="""Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, IntegerLit(75), Id(i)), BinExpr(/, Id(d), IntegerLit(830)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, UnExpr(-, IntegerLit(487)), FloatLit(0.253)), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, UnExpr(-, IntegerLit(943)), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_func_40(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = 43 * i + d / 328;
            i = 483 * -0.232 + 32;
            d = 423 % p * i;
        }"""
        expect="""Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, IntegerLit(43), Id(i)), BinExpr(/, Id(d), IntegerLit(328)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, IntegerLit(483), UnExpr(-, FloatLit(0.232))), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, IntegerLit(423), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_func_41(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
            p = -12 * i + d / 871;
            i = -637 * 0.214 + 32;
            d = -824 % p * i;
        }"""
        expect="""Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, UnExpr(-, IntegerLit(12)), Id(i)), BinExpr(/, Id(d), IntegerLit(871)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, UnExpr(-, IntegerLit(637)), FloatLit(0.214)), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, UnExpr(-, IntegerLit(824)), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_func_42(self):
        input =  """// This is the line comment
            degreeOfFreedom: auto = 1024;
            batteryLevel: integer = 100;
            main: function void() {
                prinf("Degree of freedom is");
                prinf(degreeOfFreedom);
                prinf("\\n");

                p: float = 0.328;
                i: integer = 0.0;
                d: auto = 1.3;

                while ((checkCompleted()) && (batteryLevel > 10))
                    run(p, i, d);
            }
            run: function void(inherit out p: float, out i: float, out d: float) inherit func{
                p = 43 * i + d / 328;
                i = 483 * -0.232 + 32;
                d = 423 % p * i;
            }"""
        expect = """Program([
	VarDecl(degreeOfFreedom, AutoType, IntegerLit(1024))
	VarDecl(batteryLevel, IntegerType, IntegerLit(100))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(prinf, StringLit(Degree of freedom is)), CallStmt(prinf, Id(degreeOfFreedom)), CallStmt(prinf, StringLit(\\n)), VarDecl(p, FloatType, FloatLit(0.328)), VarDecl(i, IntegerType, FloatLit(0.0)), VarDecl(d, AutoType, FloatLit(1.3)), WhileStmt(BinExpr(&&, FuncCall(checkCompleted, []), BinExpr(>, Id(batteryLevel), IntegerLit(10))), CallStmt(run, Id(p), Id(i), Id(d)))]))
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, IntegerLit(43), Id(i)), BinExpr(/, Id(d), IntegerLit(328)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, IntegerLit(483), UnExpr(-, FloatLit(0.232))), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, IntegerLit(423), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_func_43(self):
        input = """
        main: function void()
        {
            x, y: integer = 0, 0;
            for (x = 0, x < n, x + 1)
            {
                y = 0;
                while (true)
                {
                    if (y == n)
                    {
                        break;
                    }
                    else
                    {
                        printInteger(A[x, y]);
                        y = y + 1;
                    }
                }
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), VarDecl(y, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(n)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(y), IntegerLit(0)), WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(==, Id(y), Id(n)), BlockStmt([BreakStmt()]), BlockStmt([CallStmt(printInteger, ArrayCell(A, [Id(x), Id(y)])), AssignStmt(Id(y), BinExpr(+, Id(y), IntegerLit(1)))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_func_44(self):
        input = """
        main: function void()
        {
            S: array[50] of string;
            concatenated_s: string = "";
            for (i = 0, i < len(S), i + 1)
            {
                concatenated_s = concatenated_s::S[i];
            }
            printString(concatenated_s);
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(S, ArrayType([50], StringType)), VarDecl(concatenated_s, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(S)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(concatenated_s), BinExpr(::, Id(concatenated_s), ArrayCell(S, [Id(i)])))])), CallStmt(printString, Id(concatenated_s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_func_45(self):
        input = """
        sum: function integer(arr: array[10, 10] of integer) inherit previous_sum
        {
            x, y: integer;
            ans: integer = 0;
            for (i = 0, i < 10, i + 1)
            {
                for (j = 0, j < 10, j + 1)
                {
                    ans = ans + arr[i, j];
                }
            }
            return ans;
        }
        main: function void()
        {
            A: array[10, 10] of integer;
            printInteger(sum(A));
        }
        """
        expect="""Program([
	FuncDecl(sum, IntegerType, [Param(arr, ArrayType([10, 10], IntegerType))], previous_sum, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(ans, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), ArrayCell(arr, [Id(i), Id(j)])))]))])), ReturnStmt(Id(ans))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(A, ArrayType([10, 10], IntegerType)), CallStmt(printInteger, FuncCall(sum, [Id(A)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_func_46(self):
        input = """
        test_func: function integer(arr1: array[10] of integer)
        {
            i, ans: integer = 0, 0;
            tmp: array[10000] of integer;
            for (i = 0, i < 10, i + 1)
            {
                tmp[arr1[i]] = tmp[arr1[i]] + 1;
            }

            for (i = 0, i < 10000, i + 1)
            {
                if (tmp[i] != 0) ans = ans + 1;
            }

            return ans;
        }
        main: function void()
        {
            arr: array[10] of integer;
            arr = random(10);
            printInteger(test_func(A));
        }
        """
        expect="""Program([
	FuncDecl(test_func, IntegerType, [Param(arr1, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(ans, IntegerType, IntegerLit(0)), VarDecl(tmp, ArrayType([10000], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(tmp, [ArrayCell(arr1, [Id(i)])]), BinExpr(+, ArrayCell(tmp, [ArrayCell(arr1, [Id(i)])]), IntegerLit(1)))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10000)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(tmp, [Id(i)]), IntegerLit(0)), AssignStmt(Id(ans), BinExpr(+, Id(ans), IntegerLit(1))))])), ReturnStmt(Id(ans))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType)), AssignStmt(Id(arr), FuncCall(random, [IntegerLit(10)])), CallStmt(printInteger, FuncCall(test_func, [Id(A)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_func_47(self):
        input = """
        area: function float(a: float, b: float, c: float)
        {
            p: float = a + b + c;

            return sqrt(p * (p - a) * (p - b) * (p - c));
        }
        """
        expect="""Program([
	FuncDecl(area, FloatType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([VarDecl(p, FloatType, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c))), ReturnStmt(FuncCall(sqrt, [BinExpr(*, BinExpr(*, BinExpr(*, Id(p), BinExpr(-, Id(p), Id(a))), BinExpr(-, Id(p), Id(b))), BinExpr(-, Id(p), Id(c)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_func_48(self):
        input = """
        triple: function auto(x: auto)
        {
            return x * 3;
        }
        """
        expect="""Program([
	FuncDecl(triple, AutoType, [Param(x, AutoType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_func_49(self):
        input = """
        fact: function auto(x: auto, n: integer)
        {
            if (n == 1) return x;
            else return x * pow(x, n - 1);
        }
        main: function void(x: integer){
            printInteger(fact(3));
        }
        """
        expect="""Program([
	FuncDecl(fact, AutoType, [Param(x, AutoType), Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(Id(x)), ReturnStmt(BinExpr(*, Id(x), FuncCall(pow, [Id(x), BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(main, VoidType, [Param(x, IntegerType)], None, BlockStmt([CallStmt(printInteger, FuncCall(fact, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_func_50(self):
        input = """main: function void () {
            printInteger(4);
        }"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_func_51(self):
        input = """a: integer = 2;
                       b: integer = 3;
                       mulfunc: function integer(x: integer, y: integer){
                            return x*y;
                    }"""
        expect="""Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	VarDecl(b, IntegerType, IntegerLit(3))
	FuncDecl(mulfunc, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_func_52(self):
        input = """func: function void(){if(a || b){
                        if(a)
                            print(a);
                        else
                            print(c);
                        }
                        else
                        print(d);}"""
        expect="""Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(||, Id(a), Id(b)), BlockStmt([IfStmt(Id(a), CallStmt(print, Id(a)), CallStmt(print, Id(c)))]), CallStmt(print, Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_func_53(self):
        input = """func: function void(a: integer){if(a%2==0)
                            print("Even");
                        else
                            print("Odd");}"""
        expect="""Program([
	FuncDecl(func, VoidType, [Param(a, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(0)), CallStmt(print, StringLit(Even)), CallStmt(print, StringLit(Odd)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_func_54(self):
        input = """func: function void(flag: boolean){do{
                            donothing();
                    }while(flag == true); }"""
        expect="""Program([
	FuncDecl(func, VoidType, [Param(flag, BooleanType)], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(flag), BooleanLit(True)), BlockStmt([CallStmt(donothing, )]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_func_55(self):
        input = """main : function void()
{
    a: string = "Quang dep trai v";
    b: string = "asfasfsaf \\t";
    return;
}"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(Quang dep trai v)), VarDecl(b, StringType, StringLit(asfasfsaf \\t)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_func_56(self):
        input = """
        main: function void()
        {
            x: float = 0.2;
            while (foo(x) >= 10) x = (x + 2) / 3;
            printInteger(foo(x));
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(0.2)), WhileStmt(BinExpr(>=, FuncCall(foo, [Id(x)]), IntegerLit(10)), AssignStmt(Id(x), BinExpr(/, BinExpr(+, Id(x), IntegerLit(2)), IntegerLit(3)))), CallStmt(printInteger, FuncCall(foo, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_func_57(self):
        input = """
        writeInt: function void(a: integer, b: auto, i: auto)
        {
            do
            {
                writeInteger(i + 1);
            } 
            while (i != a + b);
        }
        """
        expect="""Program([
	FuncDecl(writeInt, VoidType, [Param(a, IntegerType), Param(b, AutoType), Param(i, AutoType)], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(i), BinExpr(+, Id(a), Id(b))), BlockStmt([CallStmt(writeInteger, BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_func_58(self):
        input = """main: function integer(){
            m,n : integer;
            i: auto = 0;
            printf("Enter m: ");
            Get(m);
            printf("Enter n: ");
            Get(n);
            if (n<m){
                printf("Numbers from n to m: ");
                for(i=n, i<=m, i+1){
                    printf(i);
                }
            }
            return 0;
        }"""
        expect="""Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(m, IntegerType), VarDecl(n, IntegerType), VarDecl(i, AutoType, IntegerLit(0)), CallStmt(printf, StringLit(Enter m: )), CallStmt(Get, Id(m)), CallStmt(printf, StringLit(Enter n: )), CallStmt(Get, Id(n)), IfStmt(BinExpr(<, Id(n), Id(m)), BlockStmt([CallStmt(printf, StringLit(Numbers from n to m: )), ForStmt(AssignStmt(Id(i), Id(n)), BinExpr(<=, Id(i), Id(m)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printf, Id(i))]))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_func_59(self):
        input = """
        main: function void(){ 
            i : integer = 0;
            if (a){
                if(b){
                    if(c){
                        a = a+i;
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), IfStmt(Id(a), BlockStmt([IfStmt(Id(b), BlockStmt([IfStmt(Id(c), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_func_60(self):
        input = """count: function string(money: array[10] of integer){
                    sum, i : auto = 0, 0;
                    do{
                        sum = sum+money[i+1];
                    }
                    while(i<=100);
                }
                main: function integer(argv: integer , kwargs: string)
                {
                    c: boolean ;
                    count(argc);
                    print(str);
                    return i ;
                }"""
        expect="""Program([
	FuncDecl(count, StringType, [Param(money, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(sum, AutoType, IntegerLit(0)), VarDecl(i, AutoType, IntegerLit(0)), DoWhileStmt(BinExpr(<=, Id(i), IntegerLit(100)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(money, [BinExpr(+, Id(i), IntegerLit(1))])))]))]))
	FuncDecl(main, IntegerType, [Param(argv, IntegerType), Param(kwargs, StringType)], None, BlockStmt([VarDecl(c, BooleanType), CallStmt(count, Id(argc)), CallStmt(print, Id(str)), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    ################################ END TEST FUNCTIONS #################################

    ################################ TEST RANDOM ################################# 
    def test_random_1(self):
        input = """test_complex_EQUAL_operator: function string(){
            arr: array[3] of integer;
            arr[0]=2; 
            arr[1]=4; 
            arr[2]=5;
            if( (arr[0] >= 3) || (arr[1]==1))
            {
                do
                {
                    push(True);
                    continue;
                }
                while(i==(arr[1]+arr[2]+arr[0]));
            }
            else
            {
                return false;
            }
        }"""
        expect="""Program([
	FuncDecl(test_complex_EQUAL_operator, StringType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], IntegerType)), AssignStmt(ArrayCell(arr, [IntegerLit(0)]), IntegerLit(2)), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), IntegerLit(4)), AssignStmt(ArrayCell(arr, [IntegerLit(2)]), IntegerLit(5)), IfStmt(BinExpr(||, BinExpr(>=, ArrayCell(arr, [IntegerLit(0)]), IntegerLit(3)), BinExpr(==, ArrayCell(arr, [IntegerLit(1)]), IntegerLit(1))), BlockStmt([DoWhileStmt(BinExpr(==, Id(i), BinExpr(+, BinExpr(+, ArrayCell(arr, [IntegerLit(1)]), ArrayCell(arr, [IntegerLit(2)])), ArrayCell(arr, [IntegerLit(0)]))), BlockStmt([CallStmt(push, Id(True)), ContinueStmt()]))]), BlockStmt([ReturnStmt(BooleanLit(False))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_random_2(self):
        input = """test_LESS_operator: function string(){
            arr: array[3] of boolean;
            arr[0]=true; arr[1]=true; arr[2]=false;
            if(((arr[0]<arr[1]) && arr[2])< true || (arr[1]<false) && (true<false))
                return "True";
            else
                return "False";
        }"""
        expect="""Program([
	FuncDecl(test_LESS_operator, StringType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], BooleanType)), AssignStmt(ArrayCell(arr, [IntegerLit(0)]), BooleanLit(True)), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), BooleanLit(True)), AssignStmt(ArrayCell(arr, [IntegerLit(2)]), BooleanLit(False)), IfStmt(BinExpr(<, BinExpr(&&, BinExpr(<, ArrayCell(arr, [IntegerLit(0)]), ArrayCell(arr, [IntegerLit(1)])), ArrayCell(arr, [IntegerLit(2)])), BinExpr(&&, BinExpr(||, BooleanLit(True), BinExpr(<, ArrayCell(arr, [IntegerLit(1)]), BooleanLit(False))), BinExpr(<, BooleanLit(True), BooleanLit(False)))), ReturnStmt(StringLit(True)), ReturnStmt(StringLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_random_3(self):
        input = """test_complex_GREATER_operator: function float(){
            arr: array[3] of float;
            arr[0]=0.1; arr[1]=0.2; arr[2]=0.3;
            if((arr[0]>arr[1]) && (arr[2]> true) || (arr[1]>false) && (true>false)){
                return arr[0];
            }
            else{
                return arr[1];
            }
        }"""
        expect="""Program([
	FuncDecl(test_complex_GREATER_operator, FloatType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], FloatType)), AssignStmt(ArrayCell(arr, [IntegerLit(0)]), FloatLit(0.1)), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), FloatLit(0.2)), AssignStmt(ArrayCell(arr, [IntegerLit(2)]), FloatLit(0.3)), IfStmt(BinExpr(&&, BinExpr(||, BinExpr(&&, BinExpr(>, ArrayCell(arr, [IntegerLit(0)]), ArrayCell(arr, [IntegerLit(1)])), BinExpr(>, ArrayCell(arr, [IntegerLit(2)]), BooleanLit(True))), BinExpr(>, ArrayCell(arr, [IntegerLit(1)]), BooleanLit(False))), BinExpr(>, BooleanLit(True), BooleanLit(False))), BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]), BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(1)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_random_4(self):
        input = """main: function integer()
            {
                for (a=1, a<10, a*2){
                    for(b=2, b==10, b*2){
                        a: integer;
                        b: string;
                        b = a + 1;
                    }
                }
                for(d=1, d!=1, d+1){
                    e: integer;
                    e = d;
                }
                for(c=100, c!=0, c%2){
                    for(d=1000, d>0, d%10){
                        e: integer;
                        e = d;
                        d: string;
                        d = e;
                    }
                }
                return 1;
            }"""
        expect="""Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(<, Id(a), IntegerLit(10)), BinExpr(*, Id(a), IntegerLit(2)), BlockStmt([ForStmt(AssignStmt(Id(b), IntegerLit(2)), BinExpr(==, Id(b), IntegerLit(10)), BinExpr(*, Id(b), IntegerLit(2)), BlockStmt([VarDecl(a, IntegerType), VarDecl(b, StringType), AssignStmt(Id(b), BinExpr(+, Id(a), IntegerLit(1)))]))])), ForStmt(AssignStmt(Id(d), IntegerLit(1)), BinExpr(!=, Id(d), IntegerLit(1)), BinExpr(+, Id(d), IntegerLit(1)), BlockStmt([VarDecl(e, IntegerType), AssignStmt(Id(e), Id(d))])), ForStmt(AssignStmt(Id(c), IntegerLit(100)), BinExpr(!=, Id(c), IntegerLit(0)), BinExpr(%, Id(c), IntegerLit(2)), BlockStmt([ForStmt(AssignStmt(Id(d), IntegerLit(1000)), BinExpr(>, Id(d), IntegerLit(0)), BinExpr(%, Id(d), IntegerLit(10)), BlockStmt([VarDecl(e, IntegerType), AssignStmt(Id(e), Id(d)), VarDecl(d, StringType), AssignStmt(Id(d), Id(e))]))])), ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_random_5(self):
        input = """plusFuncInt: function integer(x: integer, y: integer) {
                sum : integer;
                sum = x*567 + y/1234;
                return sum-45673;
            }
            float plusFuncDouble(x: float, y: float) {
                if(x>=y){
                    return x;
                }
                else{
                    return y;
                }
            }"""
        expect="""Program([
	FuncDecl(plusFuncInt, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType), AssignStmt(Id(sum), BinExpr(+, BinExpr(*, Id(x), IntegerLit(567)), BinExpr(/, Id(y), IntegerLit(1234)))), ReturnStmt(BinExpr(-, Id(sum), IntegerLit(45673)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_random_6(self):
        input = """main: function integer(){
                x, y, i : integer;
                arr: array[10] of integer;
                x = 0;
                y = 0;
                for(i=0, i<10, i+1){
                    arr[i]=i;
                }
                for(i=0, i<10, i+1){
                    if(arr[i]%2==0)
                        x = x + arr[i];
                    else
                        return y + arr[i];
                }        
            }"""
        expect="""Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(i, IntegerType), VarDecl(arr, ArrayType([10], IntegerType)), AssignStmt(Id(x), IntegerLit(0)), AssignStmt(Id(y), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i)]), Id(i))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(x), BinExpr(+, Id(x), ArrayCell(arr, [Id(i)]))), ReturnStmt(BinExpr(+, Id(y), ArrayCell(arr, [Id(i)]))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_random_7(self):
        input = """fact: function integer(x: integer)
            {
                x: float = 2.0;
                res: integer = 1;
                for (i = 1, i <= x, i + 1) res = res * i;
                return res;
            }

            main: function void()
            {
                x: integer;
                printString("Please input x: ");
                readInteger(x);
                printString("x! = ");
                printInteger(fact(x));
            }"""
        expect="""Program([
	FuncDecl(fact, IntegerType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(x, FloatType, FloatLit(2.0)), VarDecl(res, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(x)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(res), BinExpr(*, Id(res), Id(i)))), ReturnStmt(Id(res))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), CallStmt(printString, StringLit(Please input x: )), CallStmt(readInteger, Id(x)), CallStmt(printString, StringLit(x! = )), CallStmt(printInteger, FuncCall(fact, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_random_8(self):
        input = """
            /* 300 bai code thieu nhi
            Bai 2: Viet ham kiem tra xau doi xung*/

            isPalindrome: function boolean(s: string)
            {
                if (len(s) <= 1) return true;
                if (s[0] == s[-1]) return isPalindrome(slice(s, 1, -2));
                else return false;
            }

            main: function void()
            {
                print(isPalindrome("abba"));
            }
            """
        expect="""Program([
	FuncDecl(isPalindrome, BooleanType, [Param(s, StringType)], None, BlockStmt([IfStmt(BinExpr(<=, FuncCall(len, [Id(s)]), IntegerLit(1)), ReturnStmt(BooleanLit(True))), IfStmt(BinExpr(==, ArrayCell(s, [IntegerLit(0)]), ArrayCell(s, [UnExpr(-, IntegerLit(1))])), ReturnStmt(FuncCall(isPalindrome, [FuncCall(slice, [Id(s), IntegerLit(1), UnExpr(-, IntegerLit(2))])])), ReturnStmt(BooleanLit(False)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(isPalindrome, [StringLit(abba)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_random_9(self):
        input = """

           _var: integer;

            inc: function void(out x: integer)
            // Increase input by 1
            {
                x = x + 1;
            }

            main: function void()
            {
                a, b: integer = 1, 2;
                inc(a);
                if (a == b) inc(b);
                else inc(a);

                for (_var = 0, _var < 5, _var + 1)
                {
                    inc(a);
                    a = a - b * 2;
                }

                /* My useless block */
                {
                    {
                        {
                            _var = a - 1;
                        }
                    }
                }
            }"""
        expect="""Program([
	VarDecl(_var, IntegerType)
	FuncDecl(inc, VoidType, [OutParam(x, IntegerType)], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), CallStmt(inc, Id(a)), IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(inc, Id(b)), CallStmt(inc, Id(a))), ForStmt(AssignStmt(Id(_var), IntegerLit(0)), BinExpr(<, Id(_var), IntegerLit(5)), BinExpr(+, Id(_var), IntegerLit(1)), BlockStmt([CallStmt(inc, Id(a)), AssignStmt(Id(a), BinExpr(-, Id(a), BinExpr(*, Id(b), IntegerLit(2))))])), BlockStmt([BlockStmt([BlockStmt([AssignStmt(Id(_var), BinExpr(-, Id(a), IntegerLit(1)))])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_random_10(self):
        input = """main : function void(){
            x: float;
            a: integer = 0;
            x = 2.0;
            while(((x * 3) >= 1000)){
                a = a + x;
            }
            printInteger(a);
        }"""
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType), VarDecl(a, IntegerType, IntegerLit(0)), AssignStmt(Id(x), FloatLit(2.0)), WhileStmt(BinExpr(>=, BinExpr(*, Id(x), IntegerLit(3)), IntegerLit(1000)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(x)))])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_random_11(self):
        input = """
            main: function void()
            {
                do
                {
                    writeInteger(i + 1);
                } 
                while (i != a + b);
            }
            """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(i), BinExpr(+, Id(a), Id(b))), BlockStmt([CallStmt(writeInteger, BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_random_12(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect="""Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_random_13(self):
        input = """x: integer = 123;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        increase: function void(out n: integer, delta: integer) {
            n = n + delta;
            printBoolean(n);
        }
        main: function void() {
            delta: integer = fact(3);
            increase(x, delta);
            printInteger(x);
            preventDefault();
        }"""
        expect="""Program([
	VarDecl(x, IntegerType, IntegerLit(123))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(increase, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), CallStmt(printBoolean, Id(n))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(increase, Id(x), Id(delta)), CallStmt(printInteger, Id(x)), CallStmt(preventDefault, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_random_14(self):
        input = """
        a, b, c: float;
        x, y, z: boolean;
        g, h, y: integer;
        nty: function float(){}
        x, y, z:integer;
        a,w,q:string; 
        /*
        =======================================
            I don't think this is the comment:))
        =======================================
        */
        """
        expect="""Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	VarDecl(x, BooleanType)
	VarDecl(y, BooleanType)
	VarDecl(z, BooleanType)
	VarDecl(g, IntegerType)
	VarDecl(h, IntegerType)
	VarDecl(y, IntegerType)
	FuncDecl(nty, FloatType, [], None, BlockStmt([]))
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
	VarDecl(a, StringType)
	VarDecl(w, StringType)
	VarDecl(q, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_random_15(self):
        input = """
        test_str : string;
        randomfunc: function integer(x:integer, y:integer) {
            sum:integer;
            sum = x*567 + y/1234;
            return sum-45673;
        }
        plusFuncDouble:function float(x:float, y:float) {
            if(x>=y)
                return x;
            else
                return y;
        }       
        """
        expect="""Program([
	VarDecl(test_str, StringType)
	FuncDecl(randomfunc, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType), AssignStmt(Id(sum), BinExpr(+, BinExpr(*, Id(x), IntegerLit(567)), BinExpr(/, Id(y), IntegerLit(1234)))), ReturnStmt(BinExpr(-, Id(sum), IntegerLit(45673)))]))
	FuncDecl(plusFuncDouble, FloatType, [Param(x, FloatType), Param(y, FloatType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(x), Id(y)), ReturnStmt(Id(x)), ReturnStmt(Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_random_16(self):
        input = """
        goo:function integer ( a:integer , b:float )
        {
            c:boolean ;
            i:integer ;
            i = a + 3 ;
            if( i >0) {
                d:integer ;
                d = i + 3 ;
                printInteger(d) ;
            }
            return i ;
        }
        """
        expect="""Program([
	FuncDecl(goo, IntegerType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(c, BooleanType), VarDecl(i, IntegerType), AssignStmt(Id(i), BinExpr(+, Id(a), IntegerLit(3))), IfStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([VarDecl(d, IntegerType), AssignStmt(Id(d), BinExpr(+, Id(i), IntegerLit(3))), CallStmt(printInteger, Id(d))])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_random_17(self):
        input = """main:function integer() {
            if (a> 3){
                return 3;
            }
            return 3-1;
        }"""
        expect="""Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(3)), BlockStmt([ReturnStmt(IntegerLit(3))])), ReturnStmt(BinExpr(-, IntegerLit(3), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_random_18(self):
        input = """
            main: function void() {
                for(i[1, 1+(foo("string"::"string")+i[0])] = 0, i <= 1, i+1)
                    for(j = 0, j <= i, j+1) {
                        printf(j);
                    }
            }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(i, [IntegerLit(1), BinExpr(+, IntegerLit(1), BinExpr(+, FuncCall(foo, [BinExpr(::, StringLit(string), StringLit(string))]), ArrayCell(i, [IntegerLit(0)])))]), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<=, Id(j), Id(i)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, Id(j))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_random_19(self):
        input = """train: function float(epochs: integer, optimizer: auto){
            loss : float;
            output: float;
            losses: array[10] of float; 
            for (i = 0, i <= epochs, i+1){
                output = model(tensor);
                zero_grad(optimizer);
                loss = backward(output, loss_fn);
                step(optimizer);
            }
            append(losses, item(loss));
            return losses;
        }"""
        expect="""Program([
	FuncDecl(train, FloatType, [Param(epochs, IntegerType), Param(optimizer, AutoType)], None, BlockStmt([VarDecl(loss, FloatType), VarDecl(output, FloatType), VarDecl(losses, ArrayType([10], FloatType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), Id(epochs)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(output), FuncCall(model, [Id(tensor)])), CallStmt(zero_grad, Id(optimizer)), AssignStmt(Id(loss), FuncCall(backward, [Id(output), Id(loss_fn)])), CallStmt(step, Id(optimizer))])), CallStmt(append, Id(losses), FuncCall(item, [Id(loss)])), ReturnStmt(Id(losses))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_random_20(self):
        input = """count: function string(money: array[10] of integer){
                    sum, i : auto = 0, 0;
                    do{
                        sum = sum+money[i+1];
                    }
                    while(i<=100);
                }
                main: function integer(argv: integer , kwargs: string)
                {
                    c: integer;
                    count(argc);
                    print(str);
                    return i ;
                }"""
        expect="""Program([
	FuncDecl(count, StringType, [Param(money, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(sum, AutoType, IntegerLit(0)), VarDecl(i, AutoType, IntegerLit(0)), DoWhileStmt(BinExpr(<=, Id(i), IntegerLit(100)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(money, [BinExpr(+, Id(i), IntegerLit(1))])))]))]))
	FuncDecl(main, IntegerType, [Param(argv, IntegerType), Param(kwargs, StringType)], None, BlockStmt([VarDecl(c, IntegerType), CallStmt(count, Id(argc)), CallStmt(print, Id(str)), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))

