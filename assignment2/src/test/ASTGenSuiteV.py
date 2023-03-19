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
    def test_full_vardecl2(self):
        input = """x, y, z, t, u: integer = 1, 2, 3, 4, a && t;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(t, IntegerType, IntegerLit(4))
	VarDecl(u, IntegerType, BinExpr(&&, Id(a), Id(t)))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_vardecl3(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
    def testVarDecl1(self):
        """More complex program"""
        input = """a: string  = "abc";
b: string = "abc";"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(abc))
	VarDecl(b, StringType, StringLit(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    def testVarDecl2(self):
        """More complex program"""
        input = """a: string  = "abc";
b: void = 1;
c: auto = a&&t+c+d;"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(abc))
	VarDecl(b, VoidType, IntegerLit(1))
	VarDecl(c, AutoType, BinExpr(&&, Id(a), BinExpr(+, BinExpr(+, Id(t), Id(c)), Id(d))))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
    def testVarDeclPrecedenceNotAndMinus(self):
        """More complex program"""
        input = """a: string  = "abc";
b: string = "abc";
c: auto = !b-c;"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(abc))
	VarDecl(b, StringType, StringLit(abc))
	VarDecl(c, AutoType, BinExpr(-, UnExpr(!, Id(b)), Id(c)))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    def testVarDeclPrecedenceAddMultiply(self):
        """More complex program"""
        input = """a: integer  = a + b * c * d * (c + (e*f));"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, Id(a), BinExpr(*, BinExpr(*, BinExpr(*, Id(b), Id(c)), Id(d)), BinExpr(+, Id(c), BinExpr(*, Id(e), Id(f))))))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
    def testVarDeclPrecedenceAddModulo(self):
        input = """a : string = a + b % c % c + 1 % c;"""
        expect = """Program([
	VarDecl(a, StringType, BinExpr(+, BinExpr(+, Id(a), BinExpr(%, BinExpr(%, Id(b), Id(c)), Id(c))), BinExpr(%, IntegerLit(1), Id(c))))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    def testVarDeclPrecedenceMultiplyModulo(self):
        input = """a : string = a * b % c % c * 1 % c * abc;"""
        expect = """Program([
	VarDecl(a, StringType, BinExpr(*, BinExpr(%, BinExpr(*, BinExpr(%, BinExpr(%, BinExpr(*, Id(a), Id(b)), Id(c)), Id(c)), IntegerLit(1)), Id(c)), Id(abc)))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
    def testVarDeclPrecedenceColonColon(self):
        input = """a : string = a : b % c % c * 1 + c > abc;"""
        expect = """Program([
        VarDecl(a, StringType, BinExpr(:, Id(a), BinExpr(+, BinExpr(*, BinExpr(%, BinExpr(%, Id(b), Id(c)), Id(c)), IntegerLit(1)), Id(c)), BinExpr(>, Id(c), Id(abc))))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    def testVarDeclPrecedenceColonColon(self):
        input = """main: function integer()
{
    a, b: integer  = 5, 10;
    temp: integer;

    temp = a;
    a = b;
    b = temp;
    
    return 0;
}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(5)), VarDecl(b, IntegerType, IntegerLit(10)), VarDecl(temp, IntegerType), AssignStmt(Id(temp), Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(temp)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
    def test2(self):
        input = """main:function void()
{
    a: string = "abc";
    b: string = "abc \\t";
    return;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(abc)), VarDecl(b, StringType, StringLit(abc \\t)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
    def test3(self):
        input = """main: function void()
{
    t: integer; 
    a: boolean = t && 1 > t && 2;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(t, IntegerType), VarDecl(a, BooleanType, BinExpr(>, BinExpr(&&, Id(t), IntegerLit(1)), BinExpr(&&, Id(t), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
    def test4(self):
        input = """a: string = "abc";
b: string = "cde";
main: function void()
{
    a[0] = b[0] + d;
    return;
}"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(abc))
	VarDecl(b, StringType, StringLit(cde))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(+, ArrayCell(b, [IntegerLit(0)]), Id(d))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
    def test5(self):
        input = """main: function void() { printString("Hello, World!\\n"); }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(Hello, World!\\n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
    def test6(self):
        input = """a: string = "a";
b: array [2] of string = {"abc", "cde"};"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(a))
	VarDecl(b, ArrayType([2], StringType), ArrayLit([StringLit(abc), StringLit(cde)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
    def test7(self):
        input = """main: function void()
{
    a[1,2] = a[2];
    return a[1,2] + a[1,2];
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), ArrayCell(a, [IntegerLit(2)])), ReturnStmt(BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
    def test8(self):
        input = """a: integer = 1;
b,c,
c,e : float = .3e12, .1e14, 1.15, 4e9;
main:function void()
{
    a = b + c + c + e;
    a = !e;
    return a == e;

}"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, FloatType, FloatLit(300000000000.0))
	VarDecl(c, FloatType, FloatLit(10000000000000.0))
	VarDecl(c, FloatType, FloatLit(1.15))
	VarDecl(e, FloatType, FloatLit(4000000000.0))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, BinExpr(+, Id(b), Id(c)), Id(c)), Id(e))), AssignStmt(Id(a), UnExpr(!, Id(e))), ReturnStmt(BinExpr(==, Id(a), Id(e)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    def test9(self):
        input = """/* A C-style comment */
c: auto = "abc";
d,e,f : auto = "abc", "bce", "I ask \\t \\f \\n \\b John \\'where are you going\\' \\\\?";
"""
        expect = """Program([
	VarDecl(c, AutoType, StringLit(abc))
	VarDecl(d, AutoType, StringLit(abc))
	VarDecl(e, AutoType, StringLit(bce))
	VarDecl(f, AutoType, StringLit(I ask \\t \\f \\n \\b John \\'where are you going\\' \\\\?))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
    def test10(self):
        input = """a: integer = 1_129219.2112123;
b: integer = 1_129192e12;
deh12121212: function string()
{
    a: integer = 43 --- 42;
}"""
        expect = """Program([
	VarDecl(a, IntegerType, FloatLit(1129219.2112123))
	VarDecl(b, IntegerType, FloatLit(1.129192e+18))
	FuncDecl(deh12121212, StringType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, IntegerLit(43), UnExpr(-, UnExpr(-, IntegerLit(42)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
    def test11(self):
        input = """main: function void()
{
    for (i = 0, i < 1, i+1)
    {
        if (i > 0) {
            a = a + 1;
            b = b[b[b[b[b[b[12]]]]]] + 2;
            b[b[b[12]]] = ----12;
            c[12] = 12;
            continue;
        }
        break;
    }
    do
    {
        i = i + 1;
    }
    while (i < 120);
    return;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(b), BinExpr(+, ArrayCell(b, [ArrayCell(b, [ArrayCell(b, [ArrayCell(b, [ArrayCell(b, [ArrayCell(b, [IntegerLit(12)])])])])])]), IntegerLit(2))), AssignStmt(ArrayCell(b, [ArrayCell(b, [ArrayCell(b, [IntegerLit(12)])])]), UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(12)))))), AssignStmt(ArrayCell(c, [IntegerLit(12)]), IntegerLit(12)), ContinueStmt()])), BreakStmt()])), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(120)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
    def test12(self):
        input = """a,b: array[12] of string;
main: function void()
{
    if (a == 0)
        return;
    else
        if ((a < 0) && (b > 0))
            return a + b;
    
    while (i < 12)
    {
        i = i + 12;
    }
}"""
        expect = """Program([
	VarDecl(a, ArrayType([12], StringType))
	VarDecl(b, ArrayType([12], StringType))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), ReturnStmt(), IfStmt(BinExpr(&&, BinExpr(<, Id(a), IntegerLit(0)), BinExpr(>, Id(b), IntegerLit(0))), ReturnStmt(BinExpr(+, Id(a), Id(b))))), WhileStmt(BinExpr(<, Id(i), IntegerLit(12)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(12)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
    def test13(self):
        input = """a: array[2,3] of integer = {{1,2,3}, {1,2,3}};
main: function void()
{
    a: integer = 1;
    b: string = "\\'Where is John\\',whereareyouwhereareyoutoday\\t";
    c = b + (b + (b + (c + a)));
    return;
}"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, StringType, StringLit(\\'Where is John\\',whereareyouwhereareyoutoday\\t)), AssignStmt(Id(c), BinExpr(+, Id(b), BinExpr(+, Id(b), BinExpr(+, Id(b), BinExpr(+, Id(c), Id(a)))))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
    def test14(self):
        input = """main: function void() {
    /*Multiple lines comment!
    ~~~&$$$*/
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
    def test15(self):
        input = """//This is a line comment
/* Multi-line comment */"""
        expect = """Program([
	
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
    def test16(self):
        input = """//however this is not something that you should joke about;\\
/* YOu are &@^!%#^$3(#9#@()) */"""
        expect = """Program([
	
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    def test17(self):
        input = """a: array[2,3,4] of string = {{{123,123,123,123}, {0,0,0,0}, {1,1,1,1}},{{1,1,23,4}, {1,2,3,4}, {12,3,3,1}}};"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 3, 4], StringType), ArrayLit([ArrayLit([ArrayLit([IntegerLit(123), IntegerLit(123), IntegerLit(123), IntegerLit(123)]), ArrayLit([IntegerLit(0), IntegerLit(0), IntegerLit(0), IntegerLit(0)]), ArrayLit([IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(1)])]), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1), IntegerLit(23), IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(12), IntegerLit(3), IntegerLit(3), IntegerLit(1)])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
    def test18(self):
        input = """a: string = "abc\\t\\r\\f";
main: function void()
{
    a = a + b + c;
    re = re * a + b * c / d + a[129+abc+dds+9012+ace + re*a + 129_938280120 /*hello*/];
    return a[a[a[a[a[a[a[a[9*8*12*abc*deu*art/1238]]]]]]]];
}
"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(abc\\t\\r\\f))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c))), AssignStmt(Id(re), BinExpr(+, BinExpr(+, BinExpr(*, Id(re), Id(a)), BinExpr(/, BinExpr(*, Id(b), Id(c)), Id(d))), ArrayCell(a, [BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(129), Id(abc)), Id(dds)), IntegerLit(9012)), Id(ace)), BinExpr(*, Id(re), Id(a))), IntegerLit(129938280120))]))), ReturnStmt(ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [BinExpr(/, BinExpr(*, BinExpr(*, BinExpr(*, BinExpr(*, BinExpr(*, IntegerLit(9), IntegerLit(8)), IntegerLit(12)), Id(abc)), Id(deu)), Id(art)), IntegerLit(1238))])])])])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
    def test19(self):
        input = """a: string = "abc\\t\\r\\f\\'";
main: function void()
{
    a = a + b + c;
    re = re * a + b * c / d + a[129+abc+dds+9012+ace + re*a + 129_938280120 /*hello*/];
    return a[a[a[a[a[a[a[a[9*8*12*abc*deu*art/1238]]]]]]]];
}
"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(abc\\t\\r\\f\\'))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c))), AssignStmt(Id(re), BinExpr(+, BinExpr(+, BinExpr(*, Id(re), Id(a)), BinExpr(/, BinExpr(*, Id(b), Id(c)), Id(d))), ArrayCell(a, [BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(129), Id(abc)), Id(dds)), IntegerLit(9012)), Id(ace)), BinExpr(*, Id(re), Id(a))), IntegerLit(129938280120))]))), ReturnStmt(ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [BinExpr(/, BinExpr(*, BinExpr(*, BinExpr(*, BinExpr(*, BinExpr(*, IntegerLit(9), IntegerLit(8)), IntegerLit(12)), Id(abc)), Id(deu)), Id(art)), IntegerLit(1238))])])])])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
    def test20(self):
        input = """a: integer = a + b + c;
b: boolean = a * b / c % d || a * b && b * d;
gcd: function integer(out n: integer, out c: float)
{
    return gcd(gcd(gcd(gcd(1.2))));
}"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c)))
	VarDecl(b, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(%, BinExpr(/, BinExpr(*, Id(a), Id(b)), Id(c)), Id(d)), BinExpr(*, Id(a), Id(b))), BinExpr(*, Id(b), Id(d))))
	FuncDecl(gcd, IntegerType, [OutParam(n, IntegerType), OutParam(c, FloatType)], None, BlockStmt([ReturnStmt(FuncCall(gcd, [FuncCall(gcd, [FuncCall(gcd, [FuncCall(gcd, [FloatLit(1.2)])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
    def test21(self):
        input = """b: boolean = a * b / c % d || a * b && b * d;
gcd: function integer(out n: integer, out c: float)
{
    return gcd(gcd(gcd(gcd(1.2))));
}"""
        expect = """Program([
	VarDecl(b, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(%, BinExpr(/, BinExpr(*, Id(a), Id(b)), Id(c)), Id(d)), BinExpr(*, Id(a), Id(b))), BinExpr(*, Id(b), Id(d))))
	FuncDecl(gcd, IntegerType, [OutParam(n, IntegerType), OutParam(c, FloatType)], None, BlockStmt([ReturnStmt(FuncCall(gcd, [FuncCall(gcd, [FuncCall(gcd, [FuncCall(gcd, [FloatLit(1.2)])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
    def test22(self):
        input = """c:boolean = true;
d:boolean = false;
inc: function boolean(out c:integer, d: integer)
{
    return c && d;
}"""
        expect = """Program([
	VarDecl(c, BooleanType, BooleanLit(True))
	VarDecl(d, BooleanType, BooleanLit(False))
	FuncDecl(inc, BooleanType, [OutParam(c, IntegerType), Param(d, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, Id(c), Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
    def test23(self):
        input = """a: array[3] of integer = {0, 1,2,3};"""
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(0), IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
    def test24(self):
        input = """inc: function integer(inherit out n: integer, out x: string)
{
    t: integer = inc(12, "abc\\t\\f");
    return t;
}"""
        expect = """Program([
	FuncDecl(inc, IntegerType, [InheritOutParam(n, IntegerType), OutParam(x, StringType)], None, BlockStmt([VarDecl(t, IntegerType, FuncCall(inc, [IntegerLit(12), StringLit(abc\\t\\f)])), ReturnStmt(Id(t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
    def test25(self):
        input = """inc: function integer(inherit out n: integer, out x: string)
{
    t: integer = inc(12, "abc\\t\\f");

}"""
        expect = """Program([
	FuncDecl(inc, IntegerType, [InheritOutParam(n, IntegerType), OutParam(x, StringType)], None, BlockStmt([VarDecl(t, IntegerType, FuncCall(inc, [IntegerLit(12), StringLit(abc\\t\\f)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
    def test26(self):
        input = """delta: function integer(out x : integer)
{
    x = x + delta;
}
main: function void()
{
    return i(0);
}
inc: function integer(inherit out n: string, a1: integer) inherit main
{
    x = inc(3);
    x[inc(3), inc(3), inc(3)] = 3;
    return inc(a[1]);    
}"""
        expect = """Program([
	FuncDecl(delta, IntegerType, [OutParam(x, IntegerType)], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(FuncCall(i, [IntegerLit(0)]))]))
	FuncDecl(inc, IntegerType, [InheritOutParam(n, StringType), Param(a1, IntegerType)], main, BlockStmt([AssignStmt(Id(x), FuncCall(inc, [IntegerLit(3)])), AssignStmt(ArrayCell(x, [FuncCall(inc, [IntegerLit(3)]), FuncCall(inc, [IntegerLit(3)]), FuncCall(inc, [IntegerLit(3)])]), IntegerLit(3)), ReturnStmt(FuncCall(inc, [ArrayCell(a, [IntegerLit(1)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
    def test27(self):
        input = """"""
        expect = """Program([
	
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
    def test28(self):
        input = """main: function void()
{
    x = !(-x + y + z * m * a[0,2,1] / a[3] :: "abc" > a[3] && true);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(::, BinExpr(+, BinExpr(+, UnExpr(-, Id(x)), Id(y)), BinExpr(/, BinExpr(*, BinExpr(*, Id(z), Id(m)), ArrayCell(a, [IntegerLit(0), IntegerLit(2), IntegerLit(1)])), ArrayCell(a, [IntegerLit(3)]))), BinExpr(>, StringLit(abc), BinExpr(&&, ArrayCell(a, [IntegerLit(3)]), BooleanLit(True))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
    def test29(self):
        input = """b,c,c,e : float = 2.3e12, 1e14, 2e5, 4e9;
main:function void()
{
    a = b && c != e;
    a = !e;
    return a == e;

}"""
        expect = """Program([
	VarDecl(b, FloatType, FloatLit(2300000000000.0))
	VarDecl(c, FloatType, FloatLit(100000000000000.0))
	VarDecl(c, FloatType, FloatLit(200000.0))
	VarDecl(e, FloatType, FloatLit(4000000000.0))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(!=, BinExpr(&&, Id(b), Id(c)), Id(e))), AssignStmt(Id(a), UnExpr(!, Id(e))), ReturnStmt(BinExpr(==, Id(a), Id(e)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
    def test30(self):
        input = """main: function void()
{
    x = !(x+y+z+t+g+i+a);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)), Id(t)), Id(g)), Id(i)), Id(a))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
    def test31(self):
        input = """main: function void()
{
    x = !(x+y-z+t-g-i+a);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(+, BinExpr(-, BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, Id(x), Id(y)), Id(z)), Id(t)), Id(g)), Id(i)), Id(a))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
    def test32(self):
        input = """main: function void()
{
    x = !(x+y-z*t-g-i+a);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(+, BinExpr(-, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), Id(g)), Id(i)), Id(a))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
    def test33(self):
        input = """main: function void()
{
    x = !(x+y-z*t-g/i+a%z + l);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(+, BinExpr(+, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, Id(g), Id(i))), BinExpr(%, Id(a), Id(z))), Id(l))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
    def test34(self):
        input = """main: function void()
{
    x = !(x+y-z*t-g/i && true :: "cde" || a%z + l > "abc"  || false);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, Id(g), Id(i))), BooleanLit(True)), BinExpr(>, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, StringLit(abc), BooleanLit(False))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
    def test35(self):
        input = """main: function void()
{
    x = !(x+y-z*t-g/i && true :: "cde" || a%z + l >= "abc"  || false);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, Id(g), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, StringLit(abc), BooleanLit(False))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
    def test36(self):
        input = """main: function void()
{
    x = !(x+y-z*t-g/i && true :: "cde" || "abc" != 123 + 1 * a || false);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, Id(g), Id(i))), BooleanLit(True)), BinExpr(!=, BinExpr(||, StringLit(cde), StringLit(abc)), BinExpr(||, BinExpr(+, IntegerLit(123), BinExpr(*, IntegerLit(1), Id(a))), BooleanLit(False))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
    def test37(self):
        input = """main: function void()
{
    x = !(x+y-z*t-g/i && true :: "cde" || a%z + l >= "abc" - 1 && a || false);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, Id(g), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(-, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
    def test38(self):
        input = """main: function void()
{
    x = !(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc"  * (1 && a) || false);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(*, StringLit(abc), BinExpr(&&, IntegerLit(1), Id(a))), BooleanLit(False))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
    def test39(self):
        input = """main: function void()
{
    x = !(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    def test40(self):
        input = """main: function void()
{
    f(!(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false));
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f, UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))
    def test41(self):
        input = """main: function void()
{
    f(!(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false));
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f, UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
    def test42(self):
        input = """main: function void()
{
    x = f(!(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false)) + 
    g(!(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false))-
    g(1,2,3,false)
    +h(1,2,2,3,32,1,2,3,4,5,"abc");
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, BinExpr(-, BinExpr(+, FuncCall(f, [UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False)))))]), FuncCall(g, [UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False)))))])), FuncCall(g, [IntegerLit(1), IntegerLit(2), IntegerLit(3), BooleanLit(False)])), FuncCall(h, [IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(3), IntegerLit(32), IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), StringLit(abc)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
    def test43(self):
        input = """main: function void()
{
    f(!(y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false));
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f, UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, Id(y), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
    def test44(self):
        input = """main: function void()
{
    x = f(!(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false)) + 
    g(!(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false))-
    g(1,2,3,false)
    +h(1,2,2,3,32,1,2,3,4,5,"abc");
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, BinExpr(-, BinExpr(+, FuncCall(f, [UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False)))))]), FuncCall(g, [UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False)))))])), FuncCall(g, [IntegerLit(1), IntegerLit(2), IntegerLit(3), BooleanLit(False)])), FuncCall(h, [IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(3), IntegerLit(32), IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), StringLit(abc)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test45(self):
        input = """main: function void()
{
    x = f() + f(!(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false)) + 
    g(!(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false))-
    g(1,2,3,false)
    +h(1,2,2,3,32,1,2,3,4,5,"abc");
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(+, FuncCall(f, []), FuncCall(f, [UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False)))))])), FuncCall(g, [UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False)))))])), FuncCall(g, [IntegerLit(1), IntegerLit(2), IntegerLit(3), BooleanLit(False)])), FuncCall(h, [IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(3), IntegerLit(32), IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), StringLit(abc)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
    def test46(self):
        input = """main: function void()
{
    for (i = 0, i < 12, i+1)
    x = f() / f(!(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false)) + 
    g(!(x+y-z*t-a[1,2,3,2,2,1,1,1,2]/i && true :: "cde" || a%z + l >= "abc" + 1 && a || false))-
    g(1,2,3,false)
    +h(1,2,2,3,32,1,2,3,4,5,"abc");
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(x), BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(/, FuncCall(f, []), FuncCall(f, [UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False)))))])), FuncCall(g, [UnExpr(!, BinExpr(::, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(x), Id(y)), BinExpr(*, Id(z), Id(t))), BinExpr(/, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2)]), Id(i))), BooleanLit(True)), BinExpr(>=, BinExpr(||, StringLit(cde), BinExpr(+, BinExpr(%, Id(a), Id(z)), Id(l))), BinExpr(||, BinExpr(&&, BinExpr(+, StringLit(abc), IntegerLit(1)), Id(a)), BooleanLit(False)))))])), FuncCall(g, [IntegerLit(1), IntegerLit(2), IntegerLit(3), BooleanLit(False)])), FuncCall(h, [IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(3), IntegerLit(32), IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), StringLit(abc)]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
    def test47(self):
        input = """main: function void()
{
    for (i = 0, i < 12, i+a())
        x = f();
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), FuncCall(a, [])), AssignStmt(Id(x), FuncCall(f, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    def test48(self):
        input = """main: function void()
{
    for (i = 0, i < 12, i+1)
        x = f();
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(x), FuncCall(f, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
    def test49(self):
        input = """main: function void()
{
    for (i = 0, i < a(i + 3- !a), i+1)
        x = f();
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(a, [BinExpr(-, BinExpr(+, Id(i), IntegerLit(3)), UnExpr(!, Id(a)))])), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(x), FuncCall(f, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))
    def test50(self):
        input = """main: function void()
{
    for (i = 0, i <= 12, i+1){
        x = main(main(main()));
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(12)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), FuncCall(main, [FuncCall(main, [FuncCall(main, [])])]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    def test51(self):
        input = """main: function void()
{
    for (i = 0, i <= 12, i+1)
        x = main(main(main()));
        x = main();
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(12)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(x), FuncCall(main, [FuncCall(main, [FuncCall(main, [])])]))), AssignStmt(Id(x), FuncCall(main, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))
    def test52(self):
        input = """main: function void()
{
    for (i = main()-1-21, i <= 12, i+1+2-123939-1) {
        x = main(main(main()));
        x = main();
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(-, FuncCall(main, []), IntegerLit(1)), IntegerLit(21))), BinExpr(<=, Id(i), IntegerLit(12)), BinExpr(-, BinExpr(-, BinExpr(+, BinExpr(+, Id(i), IntegerLit(1)), IntegerLit(2)), IntegerLit(123939)), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), FuncCall(main, [FuncCall(main, [FuncCall(main, [])])])), AssignStmt(Id(x), FuncCall(main, []))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
    def test53(self):
        input = """main: function void()
{
    for (i = main()-1-21, i < 1, i + "abc" /*i <= 12, i+1+2-123939-1*/) {
        x = main(main(main()));
        x = main();
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(-, FuncCall(main, []), IntegerLit(1)), IntegerLit(21))), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(+, Id(i), StringLit(abc)), BlockStmt([AssignStmt(Id(x), FuncCall(main, [FuncCall(main, [FuncCall(main, [])])])), AssignStmt(Id(x), FuncCall(main, []))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    def test54(self):
        input = """main: function void()
{
    for (i = main()-1-21, i < 1, i + "abc" /*i <= 12, i+1+2-123939-1*/) {
        x = main(main(main()));
        x = main();
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(-, FuncCall(main, []), IntegerLit(1)), IntegerLit(21))), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(+, Id(i), StringLit(abc)), BlockStmt([AssignStmt(Id(x), FuncCall(main, [FuncCall(main, [FuncCall(main, [])])])), AssignStmt(Id(x), FuncCall(main, []))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))
    def test55(self):
        input = """main: function void()
{
    for (i = main()-1-21, i < 1, i + "abc" /*i <= 12, i+1+2-123939-1*/) {
        x = main(main(main()));
        x = main();
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(-, FuncCall(main, []), IntegerLit(1)), IntegerLit(21))), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(+, Id(i), StringLit(abc)), BlockStmt([AssignStmt(Id(x), FuncCall(main, [FuncCall(main, [FuncCall(main, [])])])), AssignStmt(Id(x), FuncCall(main, []))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
    def test56(self):
        input = """main: function void()
{
    if (i > 0) 
        if (i > 2)
            i = i + 1;
    else
        i = i + 2;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), IfStmt(BinExpr(>, Id(i), IntegerLit(2)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))
    def test57(self):
        input ="""main: function void()
{
    if (i > 0) { 
        if (i > 2)
            i = i + 1;
    }
    else
    {
        i = i + 2;
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(2)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
    def test58(self):
        input ="""main: function void()
{
    if (i > 0)
        if (i > 2){
            i = i + 1;
    }
    else{
        i = i + 2;
        }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), IfStmt(BinExpr(>, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))
    def test59(self):
        input ="""main: function void()
{
    if (i > 0)
        if (i > 2) {
            if (i > 3)
                i = i + 1;
    }
    else{
        i = i + 2;
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), IfStmt(BinExpr(>, Id(i), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(3)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
    def test60(self):
        input ="""main: function void()
{
    if (i > 0)
        if (i > 2) {
            if (i > 3)
                for (i = 0, i < 12, i + 1)
                    i = i + 1;
        }
        else {
            i = i + 2;
        }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), IfStmt(BinExpr(>, Id(i), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(3)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))
    def test61(self):
        input ="""main: function void()
{
    if (i > 0)
        if (i > 2) {
            if (i > 3)
                for (i = 0, i < 12, i+"abc")
                    i = i + 1;
        }
        else {
            i = i + 2;
        }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), IfStmt(BinExpr(>, Id(i), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(3)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), StringLit(abc)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
    def test62(self):
        input ="""main: function void()
{
    if (i > 0)
        if (i > 2) {
            if (i > 3)
                for (i = 0, i < 12, i+"abc")
                {
                     i = i + 1;

                }
                
        }
        else {
            i = i + 2;
        }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), IfStmt(BinExpr(>, Id(i), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(3)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), StringLit(abc)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
    def test63(self):
        input ="""main: function void()
{
    if (i > 0)
        if (i > 2) {
            if (i > 3)
                for (i = 0, i < 12, i+"abc")
                {
                }
                
        }
        else {
            i = i + 2;
        }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), IfStmt(BinExpr(>, Id(i), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(3)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), StringLit(abc)), BlockStmt([])))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
    def test64(self):
        input ="""main: function void()
{
    if (i > 0)
        if (i > 2) 
            if (i > 3)
                for (i = 0, i < 12, i+"abc")
                {
                }
        else {
            i = i + 2;
        }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), IfStmt(BinExpr(>, Id(i), IntegerLit(2)), IfStmt(BinExpr(>, Id(i), IntegerLit(3)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), StringLit(abc)), BlockStmt([])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
    def test65(self):
        input ="""main: function void()
{
    if (i > 0)
        if (i > 2) 
            if (i > 3)
                for (i = 0, i < 12, i+"abc")
                {
                }
        else {
            i = i + 2;
        }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), IfStmt(BinExpr(>, Id(i), IntegerLit(2)), IfStmt(BinExpr(>, Id(i), IntegerLit(3)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), StringLit(abc)), BlockStmt([])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
    def test66(self):
        input ="""main: function void()
{
    if (i > 0)
        if (i > 2) 
            if (i > 3)
                for (i = 0, i < 12, i+"abc")
                {
                    i =  i +19129129;
                    i = a[1,2,3,45];
                    i = "abc";
                }
        else {
            i = i + 2;
        }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(0)), IfStmt(BinExpr(>, Id(i), IntegerLit(2)), IfStmt(BinExpr(>, Id(i), IntegerLit(3)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), StringLit(abc)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(19129129))), AssignStmt(Id(i), ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(45)])), AssignStmt(Id(i), StringLit(abc))])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
    def test67(self):
        input ="""main: function void()
{
    while (i < 1){
        i = a + 1;
        i = i + 2;
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))
    def test68(self):
        input ="""main: function void()
{
    while (i < 1){
        i = a[1,2,3] + 1;
        i = i + 2;
        if (a[1,2,3]> 1)
            a[1,2,3] = a[1,2,3] + 1;
        else
            a[1,2,3] = -a[1,2,3];
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2))), IfStmt(BinExpr(>, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), UnExpr(-, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
    def test69(self):
        input ="""main: function void()
{
    while (i < 1){
        i = a[1,2,3] + 1;
        i = i + 2;
        if (a[1,2,3]> 1)
            a[1,2,3] = a[1,2,3] + 1;
        else
            a[1,2,3] = -a[1,2,3];
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2))), IfStmt(BinExpr(>, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), UnExpr(-, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))
    def test70(self):
        input ="""main: function void()
{
    while (i < 1 && i && 2){
        i = a[1,2,3] + 1;
        i = i + 2;
        if (a[1,2,3]> 1)
            a[1,2,3] = a[1,2,3] + 1;
        else
            a[1,2,3] = -a[1,2,3];
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), BinExpr(&&, BinExpr(&&, IntegerLit(1), Id(i)), IntegerLit(2))), BlockStmt([AssignStmt(Id(i), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2))), IfStmt(BinExpr(>, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), UnExpr(-, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))
    def test71(self):
        input ="""main: function void()
{
    while (i + 1 && i + 2){
        i = a[1,2,3] + 1;
        i = i + 2;
        if (a[1,2,3]> 1)
            a[1,2,3] = a[1,2,3] + 1;
        else
            a[1,2,3] = -a[1,2,3];
        while(true){}
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(&&, BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(2))), BlockStmt([AssignStmt(Id(i), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2))), IfStmt(BinExpr(>, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), UnExpr(-, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])))), WhileStmt(BooleanLit(True), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
    def test72(self):
        input ="""main: function void()
{
    while (!(i + 1 && i + 2)){
        i = a[1,2,3] + 1;
        i = i + 2;
        if (a[1,2,3]> 1)
            a[1,2,3] = a[1,2,3] + 1;
        else
            a[1,2,3] = -a[1,2,3];
        while(true){}
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(UnExpr(!, BinExpr(&&, BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(2)))), BlockStmt([AssignStmt(Id(i), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2))), IfStmt(BinExpr(>, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), UnExpr(-, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])))), WhileStmt(BooleanLit(True), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
    def test73(self):
        input ="""main: function void() inherit main
{
    while (!(i + 1 && i + 2)){
        i = a[1,2,3] + 1;
        i = i + 2;
        if (a[1,2,3]> 1)
            a[1,2,3] = a[1,2,3] + 1;
        else
            a[1,2,3] = -a[1,2,3];
        while(true){}
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([WhileStmt(UnExpr(!, BinExpr(&&, BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(2)))), BlockStmt([AssignStmt(Id(i), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2))), IfStmt(BinExpr(>, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), UnExpr(-, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])))), WhileStmt(BooleanLit(True), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
    def test74(self):
        input ="""main: function void() inherit main
{
    while (!(i + 1 && i + 2)){
        i = a[1,2,3] + 1;
        i = i + 2;
        if (a[1,2,3]> 1)
            a[1,2,3] = a[1,2,3] + 1;
        else
            a[1,2,3] = -a[1,2,3];
        while(true){}
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([WhileStmt(UnExpr(!, BinExpr(&&, BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(2)))), BlockStmt([AssignStmt(Id(i), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2))), IfStmt(BinExpr(>, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), UnExpr(-, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])))), WhileStmt(BooleanLit(True), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))
    def test75(self):
        input ="""main: function void() inherit main
{
    while (!(i + 1 && i + 2)){
        while (!i + 1 && i > 3){
        i = a[1,2,3] + 1;
        i = i + 2;
        if (a[1,2,3]> 1)
            a[1,2,3] = a[1,2,3] + 1;
        else
            a[1,2,3] = -a[1,2,3];
        while(true){}
        }
    }
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([WhileStmt(UnExpr(!, BinExpr(&&, BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(2)))), BlockStmt([WhileStmt(BinExpr(>, BinExpr(&&, BinExpr(+, UnExpr(!, Id(i)), IntegerLit(1)), Id(i)), IntegerLit(3)), BlockStmt([AssignStmt(Id(i), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2))), IfStmt(BinExpr(>, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), UnExpr(-, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])))), WhileStmt(BooleanLit(True), BlockStmt([]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
    def test76(self):
        input ="""main: function void() inherit main
{
    do {x = x + 1;}
    while (x < 1);
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))
    def test77(self):
        input ="""main: function void() inherit main
{
    do 
    {x = x + 1;
    while(x<1)
        x = 12 + x;
        x = main();
    }
    while (x < 1);
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), WhileStmt(BinExpr(<, Id(x), IntegerLit(1)), AssignStmt(Id(x), BinExpr(+, IntegerLit(12), Id(x)))), AssignStmt(Id(x), FuncCall(main, []))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
    def test78(self):
        input ="""main: function void() inherit main
{
    do 
    {x = x + 1 + main(1+x+2);
    }
    while (x < 1);
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, BinExpr(+, Id(x), IntegerLit(1)), FuncCall(main, [BinExpr(+, BinExpr(+, IntegerLit(1), Id(x)), IntegerLit(2))])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    def test79(self):
        input ="""main: function void() inherit main
{
    do 
    {x = x + 1;
    }
    while (x < 1);
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
    def test80(self):
        input ="""main: function void() inherit main
{
    do 
    {
        do
        {
            x = a[a[x[b[434]]]] + 1;
            for (i = 0, i < 129129, i==true){}

        }
        while(x > 1);
    }
    while (x < 1);
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, ArrayCell(a, [ArrayCell(a, [ArrayCell(x, [ArrayCell(b, [IntegerLit(434)])])])]), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(129129)), BinExpr(==, Id(i), BooleanLit(True)), BlockStmt([]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))
    def test81(self):
        input ="""main: function void() inherit main{
    do 
    {
        do
        {
            x = a[a[a[a[434]]]] + 1;
            for (i = 0, i < 129129, i==true){}
        }
        while(x > 1);
    }
    while (x < 1);
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(434)])])])]), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(129129)), BinExpr(==, Id(i), BooleanLit(True)), BlockStmt([]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
    def test82(self):
        input ="""main: function void() inherit main
{
    do 
    {
        do
        {
            x = a[a[a[a[434]]]] + 1;
            for (i = 0, i < 129129, i==true){}
            while (i < 1)
            {
                i = i + 1;
                l = l + 2;
                for (i = 0, i < 12, i+1)
                    x = x[12] + 2;
            }
        }
        while(x > 1);
    }
    while (x < 1);
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(434)])])])]), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(129129)), BinExpr(==, Id(i), BooleanLit(True)), BlockStmt([])), WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(l), BinExpr(+, Id(l), IntegerLit(2))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(x), BinExpr(+, ArrayCell(x, [IntegerLit(12)]), IntegerLit(2))))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
    def test83(self):
        input ="""main: function void() inherit main
{
    do 
    {
        do
        {
            x = a[a[a[a[434]]]] + 1;
            for (i = 0, i < 129129, i==true){}
            while (i < 1)
            {
                i = i + 1;
                l = l + 2;
                for (i = 0, i < 12, i+1)
                    x = x[12] + 2;
                break;
            }
        }
        while(x > 1);
    }
    while (x < 1);
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(434)])])])]), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(129129)), BinExpr(==, Id(i), BooleanLit(True)), BlockStmt([])), WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(l), BinExpr(+, Id(l), IntegerLit(2))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(x), BinExpr(+, ArrayCell(x, [IntegerLit(12)]), IntegerLit(2)))), BreakStmt()]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
    def test84(self):
        input ="""main: function void() inherit main
{
    do 
    {
        do
        {
            x = a[a[a[a[434]]]] + 1;
            for (i = 0, i < 129129, i==true){}
            while (i < 1)
            {
                i = i + 1;
                l = l + 2;
                for (i = 0, i < 12, i+1)
                    x = x[12] + 2;
                continue;
            }
        }
        while(x > 1);
    }
    while (x < 1);
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(x), BinExpr(+, ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(434)])])])]), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(129129)), BinExpr(==, Id(i), BooleanLit(True)), BlockStmt([])), WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(l), BinExpr(+, Id(l), IntegerLit(2))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(12)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(x), BinExpr(+, ArrayCell(x, [IntegerLit(12)]), IntegerLit(2)))), ContinueStmt()]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    def test85(self):
        input ="""main: function void() inherit main
{
    a: string = "ac+v\\\\";
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([VarDecl(a, StringType, StringLit(ac+v\\\\))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
    def test86(self):
        input ="""main: function void() inherit main
{
    a: string = "acf(a + b)";
    b : boolean = a + vc /*ssjaaisjai*/ -jajsjasjj;
    main(f(g(f())));
    ohyeah = ssanajns();
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([VarDecl(a, StringType, StringLit(acf(a + b))), VarDecl(b, BooleanType, BinExpr(-, BinExpr(+, Id(a), Id(vc)), Id(jajsjasjj))), CallStmt(main, FuncCall(f, [FuncCall(g, [FuncCall(f, [])])])), AssignStmt(Id(ohyeah), FuncCall(ssanajns, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
    def test87(self):
        input ="""main: function void() inherit main
{
    a: string = "ac\\t\\'";
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([VarDecl(a, StringType, StringLit(ac\\t\\'))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
    def test88(self):
        input ="""main: function void() inherit main
{
    a: string = "\\\\a";
}"""
        expect ="""Program([
	FuncDecl(main, VoidType, [], main, BlockStmt([VarDecl(a, StringType, StringLit(\\\\a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
def test1(self):
        input = """main: function integer()
{
}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 401))