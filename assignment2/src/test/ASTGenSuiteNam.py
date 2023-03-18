import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """
        sum: function integer(x: integer, y: integer)
        {
            return x + y;
        }

        main: function void()
        {
            a, b: integer = 3, 4;
            c: integer = a + b;
            printInteger(c);
        }
        """
        expect="""Program([
	FuncDecl(sum, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(x), Id(y)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(3)), VarDecl(b, IntegerType, IntegerLit(4)), VarDecl(c, IntegerType, BinExpr(+, Id(a), Id(b))), CallStmt(printInteger, Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """
        main: function void()
        {
            A: array[3, 3] of integer;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(A, ArrayType([3, 3], IntegerType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """
        main: function void()
        {
           A = {1, 2, 3};
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(A), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
    
    def test_308(self):
        input = """
        main: function void()
        {
           A, B: array[1, 2] of float;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(A, ArrayType([1, 2], FloatType)), VarDecl(B, ArrayType([1, 2], FloatType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = """
        main: function void()
        {
           A[0, 2] = 3;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(A, [IntegerLit(0), IntegerLit(2)]), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = """
        main: function void()
        {
           A[i + 1, j - 1] = 0;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(A, [BinExpr(+, Id(i), IntegerLit(1)), BinExpr(-, Id(j), IntegerLit(1))]), IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = """
        main: function void()
        {
           A[i + 1, -j] = 1_2;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(A, [BinExpr(+, Id(i), IntegerLit(1)), UnExpr(-, Id(j))]), IntegerLit(12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """
        main: function void()
        {
            A[i == 2, !j] = 1_2.3e-07;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(A, [BinExpr(==, Id(i), IntegerLit(2)), UnExpr(!, Id(j))]), FloatLit(1.23e-06))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """
        main: function void()
        {
           A[i, j] = A[i + 1, j - 1];
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(A, [Id(i), Id(j)]), ArrayCell(A, [BinExpr(+, Id(i), IntegerLit(1)), BinExpr(-, Id(j), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """
        main: function void()
        {
           my_str = "Hello World!";
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(my_str), StringLit(Hello World!))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """
        main: function void()
        {
            my_str = a::b;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(my_str), BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """
        main: function void()
        {
            arr[0, arr[1, arr[2, 3]]] = "H";
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0), ArrayCell(arr, [IntegerLit(1), ArrayCell(arr, [IntegerLit(2), IntegerLit(3)])])]), StringLit(H))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = """
        main: function void()
        {
            a, b, c: auto;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType), VarDecl(b, AutoType), VarDecl(c, AutoType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """
        main: function void()
        {
           x, y: string = "Hello ", "World!";
           hello: string = x::y;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit(Hello )), VarDecl(y, StringType, StringLit(World!)), VarDecl(hello, StringType, BinExpr(::, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """
        main: function void()
        {
           x, y: integer = 1, 2;
           z, t: integer = x + y + 1, x + y + z;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(y, IntegerType, IntegerLit(2)), VarDecl(z, IntegerType, BinExpr(+, BinExpr(+, Id(x), Id(y)), IntegerLit(1))), VarDecl(t, IntegerType, BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """
        main: function void()
        {
           flag: boolean = true;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(flag, BooleanType, BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """
        inc: function auto(x: auto)
        {
            return x + 1;
        }
        """
        expect="""Program([
	FuncDecl(inc, AutoType, [Param(x, AutoType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(x), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """
        inc: function auto(out x: auto)
        {
            x = x + 1;
        }
        """
        expect="""Program([
	FuncDecl(inc, AutoType, [OutParam(x, AutoType)], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """
        inc: function float(out x: auto, val: float)
        {
            x = x + val;
        }
        """
        expect="""Program([
	FuncDecl(inc, FloatType, [OutParam(x, AutoType), Param(val, FloatType)], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), Id(val)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = """
        inc: function float(out x: auto, val: float) inherit inc_ancestor
        {
            x = x + val;
        }
        """
        expect="""Program([
	FuncDecl(inc, FloatType, [OutParam(x, AutoType), Param(val, FloatType)], inc_ancestor, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), Id(val)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """
        main: function void()
        {
            x, y: string = "Hello", "World!";
            my_str = (x::"")::y;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit(Hello)), VarDecl(y, StringType, StringLit(World!)), AssignStmt(Id(my_str), BinExpr(::, BinExpr(::, Id(x), StringLit()), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input = """
        max: function auto(A: array[10] of integer)
        {
            for (i = 0, i < 10, i + 1)
            {
                //Do something
            }
        }
        """
        expect="""Program([
	FuncDecl(max, AutoType, [Param(A, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = """
        max: function auto(A: array[10] of integer)
        {
            for (i = 0, i != 10, i * 2)
            {
                //Do something
            }
        }
        """
        expect="""Program([
	FuncDecl(max, AutoType, [Param(A, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(!=, Id(i), IntegerLit(10)), BinExpr(*, Id(i), IntegerLit(2)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = """
        max: function auto(A: array[10] of integer)
        {
            i: integer;
            for (i = len(A), i >= 0, i - 1)
            {
                //Do something
            }
        }
        """
        expect="""Program([
	FuncDecl(max, AutoType, [Param(A, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), FuncCall(len, [Id(A)])), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input = """
        max: function auto(A: array[10] of integer)
        {
            i: integer = 0;
            while (i < 10)
            {
                /*Do something*/
            }
        }
        """
        expect="""Program([
	FuncDecl(max, AutoType, [Param(A, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = """
        max: function auto(A: array[10] of integer)
        {
            i: integer = 0;
            do
            {
                /*Do something*/
                i = i + 1;
            }
            while (i < 10);
        }
        """
        expect="""Program([
	FuncDecl(max, AutoType, [Param(A, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
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
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = """
        a_mess: auto = 1+2*3-4/5*6+7-_[12, 0 + x]*b-0.32E-1;
        """
        expect="""Program([
	VarDecl(a_mess, AutoType, BinExpr(-, BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(2), IntegerLit(3))), BinExpr(*, BinExpr(/, IntegerLit(4), IntegerLit(5)), IntegerLit(6))), IntegerLit(7)), BinExpr(*, ArrayCell(_, [IntegerLit(12), BinExpr(+, IntegerLit(0), Id(x))]), Id(b))), FloatLit(0.032)))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = """
        main: function void()
        {
            while (x < 3)
            {
                a = a + x;
                x = x + 1;
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(x))), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = """
        main: function void()
        {
            while (!x)
            {
                a = a / 2;
                x = a % 2 == 0;
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(UnExpr(!, Id(x)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(2))), AssignStmt(Id(x), BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(0)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
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
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        input = """
        main: function void()
        {
            for (i = 0, i < 10, i + 1)
            {
                sum = sum + i;
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
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
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input = """
        sum: function auto()
        {
            break;
        }
        """
        expect="""Program([
	FuncDecl(sum, AutoType, [], None, BlockStmt([BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input = """
        main: function void()
        {
            if (i > x)
            {
                printString("i > x");
            }
            else
            {
                printString("x >= i");
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), Id(x)), BlockStmt([CallStmt(printString, StringLit(i > x))]), BlockStmt([CallStmt(printString, StringLit(x >= i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = """
        main: function void()
        {
            if (i > x) printString("i > x");
            else
            {
                printString("x >= i");
                x = x - 1;
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), Id(x)), CallStmt(printString, StringLit(i > x)), BlockStmt([CallStmt(printString, StringLit(x >= i)), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        input = """
        main: function void()
        {
            if (x < b) if (x > a) print("\\\"Hello World!\\\""); else print("Hello"); else print("No Hello!");
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, Id(x), Id(b)), IfStmt(BinExpr(>, Id(x), Id(a)), CallStmt(print, StringLit(\\\"Hello World!\\\")), CallStmt(print, StringLit(Hello))), CallStmt(print, StringLit(No Hello!)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
        input = """
       main: function void()
            {
                while (x < 3)
                {
                    x = x + 1;
                    if (x % 2 == 0) break;
                }
            }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
        input = """
        main: function void()
        {
            for (i = true, i != false, true)
            {
                if (!i) break;
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BooleanLit(True)), BinExpr(!=, Id(i), BooleanLit(False)), BooleanLit(True), BlockStmt([IfStmt(UnExpr(!, Id(i)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
        input = """
        main: function void()
        {
            while (x < 3)
            {
                x = x + 1;
                if (x % 2 == 0) continue;
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input = """
        main: function void()
        {
            for (i = true, i != false, true)
            {
                if (!i) continue;
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BooleanLit(True)), BinExpr(!=, Id(i), BooleanLit(False)), BooleanLit(True), BlockStmt([IfStmt(UnExpr(!, Id(i)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input = """
        main: function void()
        {
            if (a % b == 0) a = reduce(a, b); 
            else b = reduce(b, a);
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), Id(b)), IntegerLit(0)), AssignStmt(Id(a), FuncCall(reduce, [Id(a), Id(b)])), AssignStmt(Id(b), FuncCall(reduce, [Id(b), Id(a)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        input = """
        main: function void()
        {
            a, b, c: array[10, 10] of string;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([10, 10], StringType)), VarDecl(b, ArrayType([10, 10], StringType)), VarDecl(c, ArrayType([10, 10], StringType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        input = """
        main: function void()
        {
            {}
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        input = """
        main: function void()
            {
                {
                    r, s: integer;
                    r = 2.0;
                    a, b: array [5] of float;
                    s = r * r * myPI;
                    a[0] = s;
                }
            } 
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], FloatType)), VarDecl(b, ArrayType([5], FloatType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
        input = """
        main: function void()
        {
           a: integer;
           a = 1 + 2 * 3;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(2), IntegerLit(3))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
        input = """
        main: function void()
        {
           a: integer;
           a = (1 + 2) * 3;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(*, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input = """
        main: function void()
        {
           a: integer;
           a = 1 * 3 == 4 + 2 * 3;
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(==, BinExpr(*, IntegerLit(1), IntegerLit(3)), BinExpr(+, IntegerLit(4), BinExpr(*, IntegerLit(2), IntegerLit(3)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input = """
        fact: function integer(x: integer)
            {
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
            }
        """
        expect="""Program([
	FuncDecl(fact, IntegerType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(x)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(res), BinExpr(*, Id(res), Id(i)))), ReturnStmt(Id(res))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), CallStmt(printString, StringLit(Please input x: )), CallStmt(readInteger, Id(x)), CallStmt(printString, StringLit(x! = )), CallStmt(printInteger, FuncCall(fact, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = """
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
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
        input = """
        max: function float(A: auto)
            {
                res: float = A[0];
                for (i = 1, i < len(A), i + 1)
                {
                    if (res < A[i]) res = A[i];
                }

                return res;
            }

            A: array[4] of float;
            main: function void()
            {
                A = {-1.0, 3e-4, 3_22.55, -5};
                printInteger(max(A));
            }
        """
        expect="""Program([
	FuncDecl(max, FloatType, [Param(A, AutoType)], None, BlockStmt([VarDecl(res, FloatType, ArrayCell(A, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(len, [Id(A)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(res), ArrayCell(A, [Id(i)])), AssignStmt(Id(res), ArrayCell(A, [Id(i)])))])), ReturnStmt(Id(res))]))
	VarDecl(A, ArrayType([4], FloatType))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(A), ArrayLit([UnExpr(-, FloatLit(1.0)), FloatLit(0.0003), FloatLit(322.55), UnExpr(-, IntegerLit(5))])), CallStmt(printInteger, FuncCall(max, [Id(A)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
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

                for (my_static_var = 0, my_static_var < 5, my_static_var + 1)
                {
                    inc(a);
                    a = a - b * 2;
                }

                /* My useless block */
                {
                    {
                        {
                            my_static_var = a - 1;
                        }
                    }
                }
            }
        """
        expect="""Program([
	VarDecl(my_stactic_var, IntegerType)
	FuncDecl(inc, VoidType, [OutParam(x, IntegerType)], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), CallStmt(inc, Id(a)), IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(inc, Id(b)), CallStmt(inc, Id(a))), ForStmt(AssignStmt(Id(my_static_var), IntegerLit(0)), BinExpr(<, Id(my_static_var), IntegerLit(5)), BinExpr(+, Id(my_static_var), IntegerLit(1)), BlockStmt([CallStmt(inc, Id(a)), AssignStmt(Id(a), BinExpr(-, Id(a), BinExpr(*, Id(b), IntegerLit(2))))])), BlockStmt([BlockStmt([BlockStmt([AssignStmt(Id(my_static_var), BinExpr(-, Id(a), IntegerLit(1)))])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input = """
        main: function void() inherit sum
            {
                return sum(sum());
            }
            sum: function void()
            {
                return "Nothing";
            }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], sum, BlockStmt([ReturnStmt(FuncCall(sum, [FuncCall(sum, [])]))]))
	FuncDecl(sum, VoidType, [], None, BlockStmt([ReturnStmt(StringLit(Nothing))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = """
        a: integer;
        b: float = 5.1;
        c: boolean = false;
        sum: function auto() inherit sum
        {}
        """
        expect="""Program([
	VarDecl(a, IntegerType)
	VarDecl(b, FloatType, FloatLit(5.1))
	VarDecl(c, BooleanType, BooleanLit(False))
	FuncDecl(sum, AutoType, [], sum, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input = """
        main: function void() 
            {
                while (((a != b) && (b != c)) && (c != d)) 
                {
                    doSomething();
                }
            }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(&&, BinExpr(&&, BinExpr(!=, Id(a), Id(b)), BinExpr(!=, Id(b), Id(c))), BinExpr(!=, Id(c), Id(d))), BlockStmt([CallStmt(doSomething, )]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
        input = """
        main: function void()
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
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(n)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(0)), BinExpr(<, Id(y), Id(n)), BinExpr(+, Id(y), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(A, [Id(x), Id(y)]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = """
        main: function void()
        {
            x, y: integer = 0, 0;
            for (x = 0, x < n, x + 1)
            {
                while (y < n)
                {
                    printInteger(A[x, y]);
                    y = y + 1;
                }
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), VarDecl(y, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(n)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(<, Id(y), Id(n)), BlockStmt([CallStmt(printInteger, ArrayCell(A, [Id(x), Id(y)])), AssignStmt(Id(y), BinExpr(+, Id(y), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = """
        main: function void()
        {
            x, y: integer = 0, 0;
            for (x = 0, x < n, x + 1)
            {
                do
                {
                    printInteger(A[x, y]);
                    y = y + 1;
                }
                while (y < n - 1);
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), VarDecl(y, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(n)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(<, Id(y), BinExpr(-, Id(n), IntegerLit(1))), BlockStmt([CallStmt(printInteger, ArrayCell(A, [Id(x), Id(y)])), AssignStmt(Id(y), BinExpr(+, Id(y), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """
        main: function void()
        {
            x, y: integer = 0, 0;
            for (x = 0, x < n, x + 1)
            {
                do
                {
                    printInteger(A[x, y]);
                    y = y + 1;
                    if (y == n - 1) break;
                }
                while (true);
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), VarDecl(y, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(n)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([CallStmt(printInteger, ArrayCell(A, [Id(x), Id(y)])), AssignStmt(Id(y), BinExpr(+, Id(y), IntegerLit(1))), IfStmt(BinExpr(==, Id(y), BinExpr(-, Id(n), IntegerLit(1))), BreakStmt())]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
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
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = """
        main: function void()
        {
            x, y: integer;
            for (x = 0, x < n, x + 1)
            {
                for (y = 0, y < n, y + 1)
                {
                    if (y % 2 == 0) printInteger(A[x, y]);
                    else continue;
                }
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(n)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(0)), BinExpr(<, Id(y), Id(n)), BinExpr(+, Id(y), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(y), IntegerLit(2)), IntegerLit(0)), CallStmt(printInteger, ArrayCell(A, [Id(x), Id(y)])), ContinueStmt())]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input = """
        main: function void()
        {
            x, y: integer;
            if (!false)
            for (x = 0, x < n, x + 1)
            {
                for (y = 0, y < n, y + 1)
                {
                    if (y % 2 == 0) printInteger(A[x, y]);
                    else continue;
                }
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), IfStmt(UnExpr(!, BooleanLit(False)), ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), Id(n)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(0)), BinExpr(<, Id(y), Id(n)), BinExpr(+, Id(y), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(y), IntegerLit(2)), IntegerLit(0)), CallStmt(printInteger, ArrayCell(A, [Id(x), Id(y)])), ContinueStmt())]))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
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
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input = """
        sum: function auto(A: array[10, 10] of integer) inherit old_sum
        {
            x, y: integer;
            ans: integer = 0;
            for (i = 0, i < 10, i + 1)
            {
                for (j = 0, j < 10, j + 1)
                {
                    ans = ans + A[i, j];
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
	FuncDecl(sum, AutoType, [Param(A, ArrayType([10, 10], IntegerType))], old_sum, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(ans, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), ArrayCell(A, [Id(i), Id(j)])))]))])), ReturnStmt(Id(ans))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(A, ArrayType([10, 10], IntegerType)), CallStmt(printInteger, FuncCall(sum, [Id(A)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = """
        main: function void()
        {
           A = {1, 2, 3};
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(A), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = """
        a: auto = 1 + 2 - 3 / 4 * 5 % 6 == 7;
        """
        expect="""Program([
	VarDecl(a, AutoType, BinExpr(==, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(%, BinExpr(*, BinExpr(/, IntegerLit(3), IntegerLit(4)), IntegerLit(5)), IntegerLit(6))), IntegerLit(7)))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = """
        a: boolean = (1 != 2) - 3 + (4::5) % 6 >= 7;
        """
        expect="""Program([
	VarDecl(a, BooleanType, BinExpr(>=, BinExpr(+, BinExpr(-, BinExpr(!=, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(%, BinExpr(::, IntegerLit(4), IntegerLit(5)), IntegerLit(6))), IntegerLit(7)))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = """
        a: float = (true - "Hello"::"Hi" && 4 / 5) == 6 + 7;
        """
        expect="""Program([
	VarDecl(a, FloatType, BinExpr(==, BinExpr(::, BinExpr(-, BooleanLit(True), StringLit(Hello)), BinExpr(&&, StringLit(Hi), BinExpr(/, IntegerLit(4), IntegerLit(5)))), BinExpr(+, IntegerLit(6), IntegerLit(7))))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = """
        a: string = ("1"::("2"::"3"))::(("4" && "5")::("6"::"7"));
        """
        expect="""Program([
	VarDecl(a, StringType, BinExpr(::, BinExpr(::, StringLit(1), BinExpr(::, StringLit(2), StringLit(3))), BinExpr(::, BinExpr(&&, StringLit(4), StringLit(5)), BinExpr(::, StringLit(6), StringLit(7)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = """
        a: boolean = true || false >= false && true;
        """
        expect="""Program([
	VarDecl(a, BooleanType, BinExpr(>=, BinExpr(||, BooleanLit(True), BooleanLit(False)), BinExpr(&&, BooleanLit(False), BooleanLit(True))))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = """
        main: function void()
        {
           n: integer;
           n = getInteger();

           printInteger(n / 10, n - n / 100 * 100);
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(getInteger, [])), CallStmt(printInteger, BinExpr(/, Id(n), IntegerLit(10)), BinExpr(-, Id(n), BinExpr(*, BinExpr(/, Id(n), IntegerLit(100)), IntegerLit(100))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = """
        max: function integer(a: integer, b: integer)
        {
            if (a > b) return a;
            else return b;
        }

        main: function void()
        {
            n1, n2, n3: integer = 0, 1, 2;
            printInteger(max(max(n1, n2), n3));
        }
        """
        expect="""Program([
	FuncDecl(max, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), ReturnStmt(Id(a)), ReturnStmt(Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n1, IntegerType, IntegerLit(0)), VarDecl(n2, IntegerType, IntegerLit(1)), VarDecl(n3, IntegerType, IntegerLit(2)), CallStmt(printInteger, FuncCall(max, [FuncCall(max, [Id(n1), Id(n2)]), Id(n3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = """
        nDistinct: function integer(A: array[10] of integer)
        {
            i, ans: integer = 0, 0;
            B: array[10000] of integer;
            for (i = 0, i < 10, i + 1)
            {
                B[A[i]] = B[A[i]] + 1;
            }

            for (i = 0, i < 10000, i + 1)
            {
                if (B[i] != 0) ans = ans + 1;
            }

            return ans;
        }
        main: function void()
        {
            A: array[10] of integer;
            A = random(10);
            printInteger(nDistinct(A));
        }
        """
        expect="""Program([
	FuncDecl(nDistinct, IntegerType, [Param(A, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(ans, IntegerType, IntegerLit(0)), VarDecl(B, ArrayType([10000], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(B, [ArrayCell(A, [Id(i)])]), BinExpr(+, ArrayCell(B, [ArrayCell(A, [Id(i)])]), IntegerLit(1)))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10000)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(B, [Id(i)]), IntegerLit(0)), AssignStmt(Id(ans), BinExpr(+, Id(ans), IntegerLit(1))))])), ReturnStmt(Id(ans))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(A, ArrayType([10], IntegerType)), AssignStmt(Id(A), FuncCall(random, [IntegerLit(10)])), CallStmt(printInteger, FuncCall(nDistinct, [Id(A)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = """
        firstAppear: function string(s: string, x: string)
        {
            while (!eos(s))
            {
                i = moveIter(s);
                if (s[i] == x) return getIter(i);
            }

            return -1;
        }

        main: function void()
        {
            printInteger(firstAppear("Hello", "o"));
        }
        """
        expect="""Program([
	FuncDecl(firstAppear, StringType, [Param(s, StringType), Param(x, StringType)], None, BlockStmt([WhileStmt(UnExpr(!, FuncCall(eos, [Id(s)])), BlockStmt([AssignStmt(Id(i), FuncCall(moveIter, [Id(s)])), IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), Id(x)), ReturnStmt(FuncCall(getIter, [Id(i)])))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(firstAppear, [StringLit(Hello), StringLit(o)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = """
        isPrime: function boolean(n: integer)
        {
            for (i = 2, i < sqrt(n), i + 1)
            {
                if (n % i == 0) return false;
            }
            
            return true;
        }

        main: function void()
        {
            if (isPrime(3)) print(\"3 is a prime number\");
        }
        """
        expect="""Program([
	FuncDecl(isPrime, BooleanType, [Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), FuncCall(sqrt, [Id(n)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(FuncCall(isPrime, [IntegerLit(3)]), CallStmt(print, StringLit(3 is a prime number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input = """
        main: function void()
        {
            Number: array[10, 10] of integer;
            for (i = 0, i < 10, i + 1)
            {
                for (j = 0, j < 10, j + 1)
                {
                    if (isPrime(Number[i, j])) printInteger(Number[i, j]);
                }
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(Number, ArrayType([10, 10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(isPrime, [ArrayCell(Number, [Id(i), Id(j)])]), CallStmt(printInteger, ArrayCell(Number, [Id(i), Id(j)])))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = """
        lowercaseCount: function integer(s: string)
        {
            i, ans: integer = 0, 0;
            while (i < len(s))
            {
                if (ASCII(s[i]) >= 97) ans = ans + 1;
            }
            return ans;
        }
        """
        expect="""Program([
	FuncDecl(lowercaseCount, IntegerType, [Param(s, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(ans, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), FuncCall(len, [Id(s)])), BlockStmt([IfStmt(BinExpr(>=, FuncCall(ASCII, [ArrayCell(s, [Id(i)])]), IntegerLit(97)), AssignStmt(Id(ans), BinExpr(+, Id(ans), IntegerLit(1))))])), ReturnStmt(Id(ans))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = """
        sumEven: function integer(A: array[10] of integer, out sum: integer)
        {
            sum = 0;
            for (i = A[0], i != eoa(A), advance(i))
            {
                if (i % 2 == 0) sum = sum + i;
            }
        }
        """
        expect="""Program([
	FuncDecl(sumEven, IntegerType, [Param(A, ArrayType([10], IntegerType)), OutParam(sum, IntegerType)], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), ArrayCell(A, [IntegerLit(0)])), BinExpr(!=, Id(i), FuncCall(eoa, [Id(A)])), FuncCall(advance, [Id(i)]), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
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
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = """
        getSumAndProduct: function float(a: float, b: float, out sum: float, out product: float)
        {
            sum = a + b;
            product = a * b;
        }
        """
        expect="""Program([
	FuncDecl(getSumAndProduct, FloatType, [Param(a, FloatType), Param(b, FloatType), OutParam(sum, FloatType), OutParam(product, FloatType)], None, BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(a), Id(b))), AssignStmt(Id(product), BinExpr(*, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input = """
        main: function void()
        {
            A: array[10] of integer;
            A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            for (i = 0, i < 10, i + 1)
            {
                if (A[i] % 3 == 0) printInteger(A[i]);
            }
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(A, ArrayType([10], IntegerType)), AssignStmt(Id(A), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(A, [Id(i)]), IntegerLit(3)), IntegerLit(0)), CallStmt(printInteger, ArrayCell(A, [Id(i)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input = """
        main: function void()
        {
           A = {1, 2, 3};
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(A), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input = """
        drawRectangle: function void(width: integer, height: integer)
        {
            for (i = 0, i < height, i + 1)
            {
                for (j = 0, j < width, j + 1)
                {
                    print("*");
                }
                print(\"\\n\");
            }
        }
        """
        expect="""Program([
	FuncDecl(drawRectangle, VoidType, [Param(width, IntegerType), Param(height, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(height)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(width)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(print, StringLit(*))])), CallStmt(print, StringLit(\\n))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
        input = """
        isTriangle: function boolean(a: float, b: float, c: float)
        {
            return (((a + b > c) && (a + c > b)) && (b + c > a));
        }
        """
        expect="""Program([
	FuncDecl(isTriangle, BooleanType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(&&, BinExpr(>, BinExpr(+, Id(a), Id(b)), Id(c)), BinExpr(>, BinExpr(+, Id(a), Id(c)), Id(b))), BinExpr(>, BinExpr(+, Id(b), Id(c)), Id(a))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = """
        getPrime: function void(m: integer, n: integer)
        {
            for (i = m, i <= n, i + 1)
            {
                if (isPrime(i)) print(str(i)::\" \");
            }
        }
        """
        expect="""Program([
	FuncDecl(getPrime, VoidType, [Param(m, IntegerType), Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), Id(m)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(isPrime, [Id(i)]), CallStmt(print, BinExpr(::, FuncCall(str, [Id(i)]), StringLit( ))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = """
        getCandS: function void(r: float, out c: float, out s: float)
        {
            pi: float = 3.14;
            c = r * 2 * pi;
            s = c * r / 2;
        }
        """
        expect="""Program([
	FuncDecl(getCandS, VoidType, [Param(r, FloatType), OutParam(c, FloatType), OutParam(s, FloatType)], None, BlockStmt([VarDecl(pi, FloatType, FloatLit(3.14)), AssignStmt(Id(c), BinExpr(*, BinExpr(*, Id(r), IntegerLit(2)), Id(pi))), AssignStmt(Id(s), BinExpr(/, BinExpr(*, Id(c), Id(r)), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = """
        main: function void()
        {
            t: float = getTemperature();
            if (t > 30)
            {
                adjustFan(100);
            }
            else if (t > 25)
            {
                adjustFan(75);
            }
            else if (t > 20)
            {
                adjustFan(50);
            }
            else turnOffFan();
        }
        """
        expect="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(t, FloatType, FuncCall(getTemperature, [])), IfStmt(BinExpr(>, Id(t), IntegerLit(30)), BlockStmt([CallStmt(adjustFan, IntegerLit(100))]), IfStmt(BinExpr(>, Id(t), IntegerLit(25)), BlockStmt([CallStmt(adjustFan, IntegerLit(75))]), IfStmt(BinExpr(>, Id(t), IntegerLit(20)), BlockStmt([CallStmt(adjustFan, IntegerLit(50))]), CallStmt(turnOffFan, ))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """
        money_type: array[9] of integer = {1, 2, 5, 10, 20 ,50 ,100, 200, 500};
        withdraw: function void(amt: integer, out pocket: array[9] of integer)
        {
            i: integer = 8;
            while (amt > 0)
            {
                if (amt > money_type[i])
                {
                    amt = amt - money_type[i];
                    pocket[i] = pocket[i] + 1;
                }
                else
                {
                    i = i - 1;
                }
                if (i == -1) break;
            }
        }
        """
        expect="""Program([
	VarDecl(money_type, ArrayType([9], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(5), IntegerLit(10), IntegerLit(20), IntegerLit(50), IntegerLit(100), IntegerLit(200), IntegerLit(500)]))
	FuncDecl(withdraw, VoidType, [Param(amt, IntegerType), OutParam(pocket, ArrayType([9], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(8)), WhileStmt(BinExpr(>, Id(amt), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(>, Id(amt), ArrayCell(money_type, [Id(i)])), BlockStmt([AssignStmt(Id(amt), BinExpr(-, Id(amt), ArrayCell(money_type, [Id(i)]))), AssignStmt(ArrayCell(pocket, [Id(i)]), BinExpr(+, ArrayCell(pocket, [Id(i)]), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), IfStmt(BinExpr(==, Id(i), UnExpr(-, IntegerLit(1))), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = """
        fact: function integer(n: integer)
        {
            if ((n == 1) || (n == 0)) return 1;
            else return n * fact(n - 1);
        }
        """
        expect="""Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(1)), BinExpr(==, Id(n), IntegerLit(0))), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = """
        double: function auto(x: auto)
        {
            return x * 2;
        }
        """
        expect="""Program([
	FuncDecl(double, AutoType, [Param(x, AutoType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = """
        pow: function auto(x: auto, n: integer)
        {
            if (n == 1) return x;
            else return x * pow(x, n - 1);
        }
        """
        expect="""Program([
	FuncDecl(pow, AutoType, [Param(x, AutoType), Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(Id(x)), ReturnStmt(BinExpr(*, Id(x), FuncCall(pow, [Id(x), BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = """
        simplify: function void(out a: integer, out b: integer)
        {
            d = GCD(a, b);
            a = a / d;
            b = b / d;
        }
        """
        expect="""Program([
	FuncDecl(simplify, VoidType, [OutParam(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([AssignStmt(Id(d), FuncCall(GCD, [Id(a), Id(b)])), AssignStmt(Id(a), BinExpr(/, Id(a), Id(d))), AssignStmt(Id(b), BinExpr(/, Id(b), Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = """
        hello: function void(name: string)
        {
            print("Hello, "::name);
        }
        """
        expect="""Program([
	FuncDecl(hello, VoidType, [Param(name, StringType)], None, BlockStmt([CallStmt(print, BinExpr(::, StringLit(Hello, ), Id(name)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = """
        isOutOfIdea: boolean = true;
        main: function void()
        {
            if (isOutOfIdea)
            {
                print("Take a rest!");
            }
            else
            {
                makeTest399();
            }
        }
        """
        expect="""Program([
	VarDecl(isOutOfIdea, BooleanType, BooleanLit(True))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(isOutOfIdea), BlockStmt([CallStmt(print, StringLit(Take a rest!))]), BlockStmt([CallStmt(makeTest399, )]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input = """
        makeTest399: function void()
        {
            if (thisIsTheFinalTest())
            {
                print("Yeahh!");
            }
        }

        main: function void()
        {
            makeTest399();
        }
        """
        expect="""Program([
	FuncDecl(makeTest399, VoidType, [], None, BlockStmt([IfStmt(FuncCall(thisIsTheFinalTest, []), BlockStmt([CallStmt(print, StringLit(Yeahh!))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(makeTest399, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
