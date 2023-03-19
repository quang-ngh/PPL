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
        input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
}"""
        expect = """Program([
\tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    ################# NEW CONTENT ###############
    

        
    def test_305(self):
        input = """ main: function void(){
                    a,b: integer;
        } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
                
            
        
    def test_306(self):
        input = """ a,b: string = 1,2; """
        expect = """Program([
	VarDecl(a, StringType, IntegerLit(1))
	VarDecl(b, StringType, IntegerLit(2))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
                
            
        
    def test_307(self):
        input = """ a: array [2,2,3] of boolean ; """
        expect = """Program([
	VarDecl(a, ArrayType([2, 2, 3], BooleanType))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
                
            
        
    def test_308(self):
        input = """ a,b,c: float = 2+2, 8*3-2+12, true; """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, IntegerLit(2), IntegerLit(2)))
	VarDecl(b, FloatType, BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(8), IntegerLit(3)), IntegerLit(2)), IntegerLit(12)))
	VarDecl(c, FloatType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
                
            
        
    def test_309(self):
        input = """ b,a: boolean = true || false :: "a", {1,2}; """
        expect = """Program([
	VarDecl(b, BooleanType, BinExpr(::, BinExpr(||, BooleanLit(True), BooleanLit(False)), StringLit(a)))
	VarDecl(a, BooleanType, ArrayLit([IntegerLit(1), IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
                
            
        
    def test_310(self):
        input = """ a: array [2] of float = {2.12,2.e12}; """
        expect = """Program([
	VarDecl(a, ArrayType([2], FloatType), ArrayLit([FloatLit(2.12), FloatLit(2000000000000.0)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
                
            
        
    def test_311(self):
        input = """ aA_2, A23: auto = "abc\\n", bcd; """
        expect = """Program([
	VarDecl(aA_2, AutoType, StringLit(abc\\n))
	VarDecl(A23, AutoType, Id(bcd))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
                
            
        
    def test_312(self):
        input = """ a_2: string = "ab,v" :: "c,,d"; """
        expect = """Program([
	VarDecl(a_2, StringType, BinExpr(::, StringLit(ab,v), StringLit(c,,d)))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
                
            
        
    def test_313(self):
        input = """ abc : integer = 23e2 || true && false ; """
        expect = """Program([
	VarDecl(abc, IntegerType, BinExpr(&&, BinExpr(||, FloatLit(2300.0), BooleanLit(True)), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
                
            
        
    def test_314(self):
        input = """ abc : integer = 23e2 || true && false ;
                    abc: function integer (){
                        
                    }   
    """
        expect = """Program([
	VarDecl(abc, IntegerType, BinExpr(&&, BinExpr(||, FloatLit(2300.0), BooleanLit(True)), BooleanLit(False)))
	FuncDecl(abc, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
                
            
        
    def test_315(self):
        input = """ main: function boolean (abc: auto, abc: array[2] of integer){
                    n = (n + abc) * 12;
                    // heheh cmt ne
        } """
        expect = """Program([
	FuncDecl(main, BooleanType, [Param(abc, AutoType), Param(abc, ArrayType([2], IntegerType))], None, BlockStmt([AssignStmt(Id(n), BinExpr(*, BinExpr(+, Id(n), Id(abc)), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
                
            
        
    def test_316(self):
        input = """ abc: function void (a: auto, b: auto)
    {
                    funcall();
                    printacb();a = a==c;
                    // cmt ne
                    return abc + 5;
        }"""
        expect = """Program([
	FuncDecl(abc, VoidType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([CallStmt(funcall, ), CallStmt(printacb, ), AssignStmt(Id(a), BinExpr(==, Id(a), Id(c))), ReturnStmt(BinExpr(+, Id(abc), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
                
            
        
    def test_317(self):
        input = """ main: function void(a: array[1,2] of integer){
                    return ;
                    return a+b;
        } """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, ArrayType([1, 2], IntegerType))], None, BlockStmt([ReturnStmt(), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
                
            
        
    def test_318(self):
        input = """ main: function auto(out a:integer) inherit A_sdsn83_a{}
    main: function auto(a:integer){
        a=v;
        c=d==e-(d+4);
        return ;
    }
    main: function auto(a:integer){}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(a, IntegerType)], A_sdsn83_a, BlockStmt([]))
	FuncDecl(main, AutoType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(Id(a), Id(v)), AssignStmt(Id(c), BinExpr(==, Id(d), BinExpr(-, Id(e), BinExpr(+, Id(d), IntegerLit(4))))), ReturnStmt()]))
	FuncDecl(main, AutoType, [Param(a, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
                
            
        
    def test_319(self):
        input = """ ___abcA39_sdn: function void (inherit abcxys: integer){
                        break;
                        continue;
                        b[2,3] = 2932 + a[1,2] && _ABSK_S29[1];
        } """
        expect = """Program([
	FuncDecl(___abcA39_sdn, VoidType, [InheritParam(abcxys, IntegerType)], None, BlockStmt([BreakStmt(), ContinueStmt(), AssignStmt(ArrayCell(b, [IntegerLit(2), IntegerLit(3)]), BinExpr(&&, BinExpr(+, IntegerLit(2932), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])), ArrayCell(_ABSK_S29, [IntegerLit(1)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
                
            
        
    def test_320(self):
        input = """ main: function float(out x:integer){
                        fun_call(a_b, b);

        } """
        expect = """Program([
	FuncDecl(main, FloatType, [OutParam(x, IntegerType)], None, BlockStmt([CallStmt(fun_call, Id(a_b), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
                
            
        
    def test_321(self):
        input = """ a,b: integer = (3.E12+(12*5/22)) == (12*15-22.2), "string ne \\\\"; """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(==, BinExpr(+, FloatLit(3000000000000.0), BinExpr(/, BinExpr(*, IntegerLit(12), IntegerLit(5)), IntegerLit(22))), BinExpr(-, BinExpr(*, IntegerLit(12), IntegerLit(15)), FloatLit(22.2))))
	VarDecl(b, IntegerType, StringLit(string ne \\\\))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
                
            
        
    def test_322(self):
        input = """ a :float = (call_ne()-12%9) * 12; """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(*, BinExpr(-, FuncCall(call_ne, []), BinExpr(%, IntegerLit(12), IntegerLit(9))), IntegerLit(12)))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
                
            
        
    def test_323(self):
        input = """ a: string = "abc$(@$)"::"adnd"; """
        expect = """Program([
	VarDecl(a, StringType, BinExpr(::, StringLit(abc$(@$)), StringLit(adnd)))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
                
            
        
    def test_324(self):
        input = """ func: function float(){
                    if(a==(call_ne()-2+12)){
                        a = 2;
                    }
        } """
        expect = """Program([
	FuncDecl(func, FloatType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), BinExpr(+, BinExpr(-, FuncCall(call_ne, []), IntegerLit(2)), IntegerLit(12))), BlockStmt([AssignStmt(Id(a), IntegerLit(2))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
                
            
        
    def test_325(self):
        input = """ a:integer = call_ne(9-2*1 , 12-100+4::"a" - (a+b)); """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(call_ne, [BinExpr(-, IntegerLit(9), BinExpr(*, IntegerLit(2), IntegerLit(1))), BinExpr(::, BinExpr(+, BinExpr(-, IntegerLit(12), IntegerLit(100)), IntegerLit(4)), BinExpr(-, StringLit(a), BinExpr(+, Id(a), Id(b))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
                
            
        
    def test_326(self):
        input = """main: function void() {
        i : integer = 5;
        while(true) add(i, 1);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(5)), WhileStmt(BooleanLit(True), CallStmt(add, Id(i), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
                
            
        
    def test_327(self):
        input = """main: function void() {
        i : integer = 7 + 5;
        for(i = 1 :: 2, i < 6 - 1, a + 1) {
            continue;
        }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, IntegerLit(7), IntegerLit(5))), ForStmt(AssignStmt(Id(i), BinExpr(::, IntegerLit(1), IntegerLit(2))), BinExpr(<, Id(i), BinExpr(-, IntegerLit(6), IntegerLit(1))), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
                
            
        
    def test_328(self):
        input = """main: function void() { a = {2, 5} == "ehheeh"; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(==, ArrayLit([IntegerLit(2), IntegerLit(5)]), StringLit(ehheeh)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
                
            
        
    def test_329(self):
        input = """kurobarashi: function array[2] of boolean() inherit demo {}"""
        expect = """Program([
	FuncDecl(kurobarashi, ArrayType([2], BooleanType), [], demo, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
                
            
        
    def test_330(self):
        input = """main: function void(inherit out p: float, out i: float, out d: float) inherit func{
        a = a + 1;
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
                
            
        
    def test_331(self):
        input = """
    main: function void() {
        for (i = 0, i < 0, i + 1) {
            abcd();
        }
        for (a = 1, b < 23, a * 2)
            abcd();
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(0)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(abcd, )])), ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(<, Id(b), IntegerLit(23)), BinExpr(*, Id(a), IntegerLit(2)), CallStmt(abcd, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
                
            
        
    def test_332(self):
        input = """
        main: function void() {
            a: boolean = !!!a;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, UnExpr(!, UnExpr(!, UnExpr(!, Id(a)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
                
            
        
    def test_333(self):
        input = """ main: function auto(out a:integer) inherit A_sdsn83_a{}
    main: function auto(a:integer){
        a=v;
        c=d==e-(d+4);
        return ;
    }
    main: function auto(a:integer){}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(a, IntegerType)], A_sdsn83_a, BlockStmt([]))
	FuncDecl(main, AutoType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(Id(a), Id(v)), AssignStmt(Id(c), BinExpr(==, Id(d), BinExpr(-, Id(e), BinExpr(+, Id(d), IntegerLit(4))))), ReturnStmt()]))
	FuncDecl(main, AutoType, [Param(a, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
                
            
        
    def test_334(self):
        input = """ ___bcA39_sdn: function void (inherit abcxys: integer){
                        break;
                        continue;
                        b[2,3] = 2932 + a[1,2] && _ABSK_S29[1];
        } """
        expect = """Program([
	FuncDecl(___bcA39_sdn, VoidType, [InheritParam(abcxys, IntegerType)], None, BlockStmt([BreakStmt(), ContinueStmt(), AssignStmt(ArrayCell(b, [IntegerLit(2), IntegerLit(3)]), BinExpr(&&, BinExpr(+, IntegerLit(2932), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])), ArrayCell(_ABSK_S29, [IntegerLit(1)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
                
            
        
    def test_335(self):
        input = """ main: function float(out x:integer){
                        fun_call(a_b, b);

        } """
        expect = """Program([
	FuncDecl(main, FloatType, [OutParam(x, IntegerType)], None, BlockStmt([CallStmt(fun_call, Id(a_b), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
                
            
        
    def test_336(self):
        input = """ func: function float(){
                    if(a==(call_ne()-2+12)){
                        a = 2;
                    }
        } """
        expect = """Program([
	FuncDecl(func, FloatType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), BinExpr(+, BinExpr(-, FuncCall(call_ne, []), IntegerLit(2)), IntegerLit(12))), BlockStmt([AssignStmt(Id(a), IntegerLit(2))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
                
            
        
    def test_337(self):
        input = """ a:integer = call_ne(9-2*1 , 12-100+4::"a" - (a+b)); """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(call_ne, [BinExpr(-, IntegerLit(9), BinExpr(*, IntegerLit(2), IntegerLit(1))), BinExpr(::, BinExpr(+, BinExpr(-, IntegerLit(12), IntegerLit(100)), IntegerLit(4)), BinExpr(-, StringLit(a), BinExpr(+, Id(a), Id(b))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
                
            
        
    def test_338(self):
        input = """ b,a: boolean = true || false :: "a", {1,2}; """
        expect = """Program([
	VarDecl(b, BooleanType, BinExpr(::, BinExpr(||, BooleanLit(True), BooleanLit(False)), StringLit(a)))
	VarDecl(a, BooleanType, ArrayLit([IntegerLit(1), IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
                
            
        
    def test_339(self):
        input = """ aA_2, A23: auto = "abc\\n", bcd; """
        expect = """Program([
	VarDecl(aA_2, AutoType, StringLit(abc\\n))
	VarDecl(A23, AutoType, Id(bcd))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
                
            
        
    def test_340(self):
        input = """ a: array [2] of float = {2.12,2.e12}; """
        expect = """Program([
	VarDecl(a, ArrayType([2], FloatType), ArrayLit([FloatLit(2.12), FloatLit(2000000000000.0)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
                
            
        
    def test_341(self):
        input = """ abc : integer = 23e2 || true && false ;
                    abc: function integer (){
                        
                    }   
    """
        expect = """Program([
	VarDecl(abc, IntegerType, BinExpr(&&, BinExpr(||, FloatLit(2300.0), BooleanLit(True)), BooleanLit(False)))
	FuncDecl(abc, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
                
            
        
    def test_342(self):
        input = """ main: function boolean (abc: auto, abc: array[2] of integer){
                    n = (n + abc) * 12;
                    // heheh cmt ne
        } """
        expect = """Program([
	FuncDecl(main, BooleanType, [Param(abc, AutoType), Param(abc, ArrayType([2], IntegerType))], None, BlockStmt([AssignStmt(Id(n), BinExpr(*, BinExpr(+, Id(n), Id(abc)), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
                
            
        
    def test_343(self):
        input = """ main: function boolean (abc: auto, abc: array[2] of integer){
                    n = (n + abc) * 12;
                    // heheh cmt ne
        } """
        expect = """Program([
	FuncDecl(main, BooleanType, [Param(abc, AutoType), Param(abc, ArrayType([2], IntegerType))], None, BlockStmt([AssignStmt(Id(n), BinExpr(*, BinExpr(+, Id(n), Id(abc)), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
                
            
        
    def test_344(self):
        input = """
    hayy: function void() {
        do {
            a = 1;
        } while (true);
    }
    """
        expect = """Program([
	FuncDecl(hayy, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
                
            
        
    def test_345(self):
        input = """
        foo: function void() {
            do {
                do {

                } while(true);
            } while (true);
        }
    """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
                
            
        
    def test_346(self):
        input = """main: function integer(a: integer) {
        if(true) a[7] = 2;
        else continue;
    }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType)], None, BlockStmt([IfStmt(BooleanLit(True), AssignStmt(ArrayCell(a, [IntegerLit(7)]), IntegerLit(2)), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
                
            
        
    def test_347(self):
        input = """main: function string() {
        if(false) a[7,2] = 2;
        else break;
    }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([IfStmt(BooleanLit(False), AssignStmt(ArrayCell(a, [IntegerLit(7), IntegerLit(2)]), IntegerLit(2)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
                
            
        
    def test_348(self):
        input = """main: function auto() {
        if(!a==2) a[3,3,3] = 12;
        else continue;
    }"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([IfStmt(BinExpr(==, UnExpr(!, Id(a)), IntegerLit(2)), AssignStmt(ArrayCell(a, [IntegerLit(3), IntegerLit(3), IntegerLit(3)]), IntegerLit(12)), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
                
            
        
    def test_349(self):
        input = """main: function auto() {
        if(a == 0) return true;
        }"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), ReturnStmt(BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
                
            
        
    def test_350(self):
        input = """main: function void() {
        while(i < 1) funcne(i, 1);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), CallStmt(funcne, Id(i), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
                
            
        
    def test_351(self):
        input = """main: function void() {
        while(i < 1) functoionvp(i, 1);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), CallStmt(functoionvp, Id(i), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
                
            
        
    def test_352(self):
        input = """main: function auto() {
        while(a < 1) increase(i,a,3+1, 1);
        }"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(1)), CallStmt(increase, Id(i), Id(a), BinExpr(+, IntegerLit(3), IntegerLit(1)), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))
                
            
        
    def test_353(self):
        input = """x, y, z: auto;"""
        expect = """Program([
	VarDecl(x, AutoType)
	VarDecl(y, AutoType)
	VarDecl(z, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
                
            
        
    def test_354(self):
        input = """x, y, z: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
                
            
        
    def test_355(self):
        input = """x, y, z: float;"""
        expect = """Program([
	VarDecl(x, FloatType)
	VarDecl(y, FloatType)
	VarDecl(z, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
                
            
        
    def test_356(self):
        input = """x, y, z: string;"""
        expect = """Program([
	VarDecl(x, StringType)
	VarDecl(y, StringType)
	VarDecl(z, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
                
            
        
    def test_357(self):
        input = """x, y, z: array [3,2] of integer;"""
        expect = """Program([
	VarDecl(x, ArrayType([3, 2], IntegerType))
	VarDecl(y, ArrayType([3, 2], IntegerType))
	VarDecl(z, ArrayType([3, 2], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
                
            
        
    def test_358(self):
        input = """x, y, z: auto = 3,1,2;"""
        expect = """Program([
	VarDecl(x, AutoType, IntegerLit(3))
	VarDecl(y, AutoType, IntegerLit(1))
	VarDecl(z, AutoType, IntegerLit(2))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
                
            
        
    def test_359(self):
        input = """x, y, z: auto = 3,2,1-2-3-4;"""
        expect = """Program([
	VarDecl(x, AutoType, IntegerLit(3))
	VarDecl(y, AutoType, IntegerLit(2))
	VarDecl(z, AutoType, BinExpr(-, BinExpr(-, BinExpr(-, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
                
            
        
    def test_360(self):
        input = """main: function void() {
        // aloha maya
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
                
            
        
    def test_361(self):
        input = """main: function void() {
        /*aloha maya*/
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))
                
            
        
    def test_362(self):
        input = """main: function void() {
        i: float;
        for(i = 1 * b, i < 2, i + 1) {
            writeInt(i);
        }
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, FloatType), ForStmt(AssignStmt(Id(i), BinExpr(*, IntegerLit(1), Id(b))), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
                
            
        
    def test_363(self):
        input = """test: function auto() { b[1] = "abcdef \\t"; }"""
        expect = """Program([
	FuncDecl(test, AutoType, [], None, BlockStmt([AssignStmt(ArrayCell(b, [IntegerLit(1)]), StringLit(abcdef \\t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))
                
            
        
    def test_364(self):
        input = """a: array[1, 2] of boolean;"""
        expect = """Program([
	VarDecl(a, ArrayType([1, 2], BooleanType))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
                
            
        
    def test_365(self):
        input = """main: function float() {
        if(true) a[7] = 2;
        else continue;
    }"""
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([IfStmt(BooleanLit(True), AssignStmt(ArrayCell(a, [IntegerLit(7)]), IntegerLit(2)), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
                
            
        
    def test_366(self):
        input = """ a: string = "ac$(@$)"::"aadnd"; """
        expect = """Program([
	VarDecl(a, StringType, BinExpr(::, StringLit(ac$(@$)), StringLit(aadnd)))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))
                
            
        
    def test_367(self):
        input = """ a:float = call_ne(9-2*1 , 12-100+4::"a" - (a+b)); """
        expect = """Program([
	VarDecl(a, FloatType, FuncCall(call_ne, [BinExpr(-, IntegerLit(9), BinExpr(*, IntegerLit(2), IntegerLit(1))), BinExpr(::, BinExpr(+, BinExpr(-, IntegerLit(12), IntegerLit(100)), IntegerLit(4)), BinExpr(-, StringLit(a), BinExpr(+, Id(a), Id(b))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
                
            
        
    def test_368(self):
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
        self.assertTrue(TestAST.test(input, expect, 368))
                
            
        
    def test_369(self):
        input = """
        asd, abc: integer = 123, 123_123;
        a: string = "string";
    """
        expect = """Program([
	VarDecl(asd, IntegerType, IntegerLit(123))
	VarDecl(abc, IntegerType, IntegerLit(123123))
	VarDecl(a, StringType, StringLit(string))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
                
            
        
    def test_370(self):
        input = """
        a: array [1,2,3] of string = {"hello","world"};
    """
        expect = """Program([
	VarDecl(a, ArrayType([1, 2, 3], StringType), ArrayLit([StringLit(hello), StringLit(world)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))
                
            
        
    def test_371(self):
        input = """
        a,b: array [1,2,3] of string = {"hello","world"}, {};
    """
        expect = """Program([
	VarDecl(a, ArrayType([1, 2, 3], StringType), ArrayLit([StringLit(hello), StringLit(world)]))
	VarDecl(b, ArrayType([1, 2, 3], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
                
            
        
    def test_372(self):
        input = """
        a,b,c : integer = "asf","asf","asf";
    """
        expect = """Program([
	VarDecl(a, IntegerType, StringLit(asf))
	VarDecl(b, IntegerType, StringLit(asf))
	VarDecl(c, IntegerType, StringLit(asf))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))
                
            
        
    def test_373(self):
        input = """
        main: function boolean(inherit out var1: auto) {}
    """
        expect = """Program([
	FuncDecl(main, BooleanType, [InheritOutParam(var1, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
                
            
        
    def test_374(self):
        input = """
        main: function boolean(inherit a: array[1,1] of float) {}
    """
        expect = """Program([
	FuncDecl(main, BooleanType, [InheritParam(a, ArrayType([1, 1], FloatType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
                
            
        
    def test_375(self):
        input = """
        main: function string(out a: array[0,1] of boolean, b: integer, inherit c: boolean) {}
    """
        expect = """Program([
	FuncDecl(main, StringType, [OutParam(a, ArrayType([0, 1], BooleanType)), Param(b, IntegerType), InheritParam(c, BooleanType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
                
            
        
    def test_376(self):
        input = """
        main: function integer(){}
        funcname: function float() inherit main {}
    """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([]))
	FuncDecl(funcname, FloatType, [], main, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
                
            
        
    def test_377(self):
        input = """
        main: function array[1,1] of string() {
            var1 = 123;
        }
    """
        expect = """Program([
	FuncDecl(main, ArrayType([1, 1], StringType), [], None, BlockStmt([AssignStmt(Id(var1), IntegerLit(123))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
                
            
        
    def test_378(self):
        input = """
        main: function array[1,1] of string() {
            var1[0,0] = "hello world";
        }
    """
        expect = """Program([
	FuncDecl(main, ArrayType([1, 1], StringType), [], None, BlockStmt([AssignStmt(ArrayCell(var1, [IntegerLit(0), IntegerLit(0)]), StringLit(hello world))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
                
            
        
    def test_379(self):
        input = """
        main: function void() {
            if(cond==precond) printInteger(cond);
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(cond), Id(precond)), CallStmt(printInteger, Id(cond)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))
                
            
        
    def test_380(self):
        input = """
        main: function void() {
            if(a==b) if(b==c) printInteger(a);
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), IfStmt(BinExpr(==, Id(b), Id(c)), CallStmt(printInteger, Id(a))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
                
            
        
    def test_381(self):
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
        self.assertTrue(TestAST.test(input, expect, 381))
                
            
        
    def test_382(self):
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
        self.assertTrue(TestAST.test(input, expect, 382))
                
            
        
    def test_383(self):
        input = """
        main: function void() {
            for(i = 0, i <= 1, i+1)
                printf(i);
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printf, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
                
            
        
    def test_384(self):
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
        self.assertTrue(TestAST.test(input, expect, 384))
                
            
        
    def test_385(self):
        input = """
        main: function void() {
            do {
                cond = 1;
            } while (true);
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(cond), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
                
            
        
    def test_386(self):
        input = """
        main: function void() {
            return abc;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(Id(abc))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))
                
            
        
    def test_387(self): #fail
        input = """
        main: function void() {
            {

            }
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
                
            
        
    def test_388(self): #fail
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
        self.assertTrue(TestAST.test(input, expect, 388))
                
            
        
    def test_389(self):
        input = """
        main: function void() {
            {{ }}
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
                
            
        
    def test_390(self):
        input = """
    main: function void() {
        do {
            a = 1;
        } while (true);
    }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
                
            
        
    def test_391(self):
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
        self.assertTrue(TestAST.test(input, expect, 391))
                
            
        
    def test_392(self):
        input = """
        main: function void() {
            continue;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))
                
            
        
    def test_393(self):
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
        self.assertTrue(TestAST.test(input, expect, 393))
                
            
        
    def test_394(self):
        input = """
        main: function void() {
            a: boolean = !!!b;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, UnExpr(!, UnExpr(!, UnExpr(!, Id(b)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
                
            
        
    def test_395(self):
        input = """
        main: function void() {
            a: boolean = c||(d||g);
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, BinExpr(||, Id(c), BinExpr(||, Id(d), Id(g))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
                
            
        
    def test_396(self):
        input = """
        main: function void() {
            a: integer = a*6+b/5-c%4+d+e*f;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(+, BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(*, Id(a), IntegerLit(6)), BinExpr(/, Id(b), IntegerLit(5))), BinExpr(%, Id(c), IntegerLit(4))), Id(d)), BinExpr(*, Id(e), Id(f))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
                
            
        
    def test_397(self):
        input = """
        main: function void() {
            a: auto = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, BinExpr(::, StringLit(string), BinExpr(==, BinExpr(&&, Id(a), BinExpr(+, Id(c), BinExpr(*, IntegerLit(2), IntegerLit(3)))), BinExpr(||, BinExpr(-, Id(b), BinExpr(*, IntegerLit(2), UnExpr(!, UnExpr(-, ArrayCell(b, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))))), Id(d)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
                
            
        
    def test_398(self):
        input = """
        main: function void() {
            a: auto = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, BinExpr(::, StringLit(string), BinExpr(==, BinExpr(&&, Id(a), BinExpr(+, Id(c), BinExpr(*, IntegerLit(2), IntegerLit(3)))), BinExpr(||, BinExpr(-, Id(b), BinExpr(*, IntegerLit(2), UnExpr(!, UnExpr(-, ArrayCell(b, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))))), Id(d)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
                
            
        
    def test_399(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
        p = 43 * i + d / 328;
        i = 483 * -0.232 + 32;
        d = 423 % p * i;
    }"""
        expect = """Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, IntegerLit(43), Id(i)), BinExpr(/, Id(d), IntegerLit(328)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, IntegerLit(483), UnExpr(-, FloatLit(0.232))), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, IntegerLit(423), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
                
            
        
    def test_400(self):
        input = """main: function void() {
        foo((foo(foo((foo)), foo, foo(foo(foo, foo(foo, foo(foo,foo,foo,foo,(foo()))))))));
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, FuncCall(foo, [FuncCall(foo, [Id(foo)]), Id(foo), FuncCall(foo, [FuncCall(foo, [Id(foo), FuncCall(foo, [Id(foo), FuncCall(foo, [Id(foo), Id(foo), Id(foo), Id(foo), FuncCall(foo, [])])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
                
            
        
    def test_401(self):
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
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([WhileStmt(Id(foo), BlockStmt([WhileStmt(FuncCall(bar, []), BlockStmt([WhileStmt(ArrayCell(stat, [IntegerLit(2)]), BlockStmt([AssignStmt(Id(fa), IntegerLit(9))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 401))
                
            
        
    def test_402(self):
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
        self.assertTrue(TestAST.test(input, expect, 402))
                
            
        
    def test_403(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
        p = -24 * i + d / 128;
        i = -837 * 0.362 + 32;
        d = -823 % p * i;
    }"""
        expect = """Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, UnExpr(-, IntegerLit(24)), Id(i)), BinExpr(/, Id(d), IntegerLit(128)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, UnExpr(-, IntegerLit(837)), FloatLit(0.362)), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, UnExpr(-, IntegerLit(823)), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 403))
                
            
        
    def test_404(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
        p = 18 * i + d / 893;
        i = -873 * 0.673 + 32;
        d = -123 % p * i;
    }"""
        expect = """Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, IntegerLit(18), Id(i)), BinExpr(/, Id(d), IntegerLit(893)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, UnExpr(-, IntegerLit(873)), FloatLit(0.673)), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, UnExpr(-, IntegerLit(123)), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 404))
                
            
        
    def test_405(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
        p = 75 * i + d / 830;
        i = -487 * 0.253 + 32;
        d = -943 % p * i;
    }"""
        expect = """Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, IntegerLit(75), Id(i)), BinExpr(/, Id(d), IntegerLit(830)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, UnExpr(-, IntegerLit(487)), FloatLit(0.253)), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, UnExpr(-, IntegerLit(943)), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 405))
                
            
        
    def test_406(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
        p = 43 * i + d / 328;
        i = 483 * -0.232 + 32;
        d = 423 % p * i;
    }"""
        expect = """Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, IntegerLit(43), Id(i)), BinExpr(/, Id(d), IntegerLit(328)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, IntegerLit(483), UnExpr(-, FloatLit(0.232))), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, IntegerLit(423), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 406))
                
            
        
    def test_407(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
        p = 782 * i + d / 562;
        i = -983 * 0.312 + 32;
        d = -314 % p * i;
    }"""
        expect = """Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, IntegerLit(782), Id(i)), BinExpr(/, Id(d), IntegerLit(562)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, UnExpr(-, IntegerLit(983)), FloatLit(0.312)), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, UnExpr(-, IntegerLit(314)), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 407))
                
            
        
    def test_408(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
        p = -12 * i + d / 871;
        i = -637 * 0.214 + 32;
        d = -824 % p * i;
    }"""
        expect = """Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, UnExpr(-, IntegerLit(12)), Id(i)), BinExpr(/, Id(d), IntegerLit(871)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, UnExpr(-, IntegerLit(637)), FloatLit(0.214)), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, UnExpr(-, IntegerLit(824)), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 408))
                
            
        
    def test_409(self):
        input = """run: function void(inherit out p: float, out i: float, out d: float) inherit func{
        p = 434 * i + d / 478;
        i = 783 * 0.521 + 32;
        d = -873 % p * i;
    }"""
        expect = """Program([
	FuncDecl(run, VoidType, [InheritOutParam(p, FloatType), OutParam(i, FloatType), OutParam(d, FloatType)], func, BlockStmt([AssignStmt(Id(p), BinExpr(+, BinExpr(*, IntegerLit(434), Id(i)), BinExpr(/, Id(d), IntegerLit(478)))), AssignStmt(Id(i), BinExpr(+, BinExpr(*, IntegerLit(783), FloatLit(0.521)), IntegerLit(32))), AssignStmt(Id(d), BinExpr(*, BinExpr(%, UnExpr(-, IntegerLit(873)), Id(p)), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 409))
                
            
        
    def test_410(self):
        input = """a: auto = ((!true == ! false) * barz / 43 + 443 - -438 + --430 --- 439) :: (("Hello" > 3289) < 843 * ( 328 :: 483));"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(::, BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(/, BinExpr(*, BinExpr(==, UnExpr(!, BooleanLit(True)), UnExpr(!, BooleanLit(False))), Id(barz)), IntegerLit(43)), IntegerLit(443)), UnExpr(-, IntegerLit(438))), UnExpr(-, UnExpr(-, IntegerLit(430)))), UnExpr(-, UnExpr(-, IntegerLit(439)))), BinExpr(<, BinExpr(>, StringLit(Hello), IntegerLit(3289)), BinExpr(*, IntegerLit(843), BinExpr(::, IntegerLit(328), IntegerLit(483))))))
])"""
        self.assertTrue(TestAST.test(input, expect, 410))
                
            
        
    def test_411(self):
        input = """main: function void(/*This is the arg of main function */) {
        if (/* put condition here */ a == 43 ) /* after which is the code */ { // put code here
            a = 3490;
        }
    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(43)), BlockStmt([AssignStmt(Id(a), IntegerLit(3490))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 411))
                
            
        
    def test_412(self):
        input = """
    press: function void(inherit key: string) inherit touch {
        touch(key);
        doSomePressing(key);
    }"""
        expect = """Program([
	FuncDecl(press, VoidType, [InheritParam(key, StringType)], touch, BlockStmt([CallStmt(touch, Id(key)), CallStmt(doSomePressing, Id(key))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 412))
                
            
        
    def test_413(self):
        input = """main: function void() {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 413))
                
            
        
    def test_414(self):
        input = """f
:
integer
=
10
;"""
        expect = """Program([
	VarDecl(f, IntegerType, IntegerLit(10))
])"""
        self.assertTrue(TestAST.test(input, expect, 414))
                
            
        
    def test_415(self):
        input = """main
:
function
void
(
)
{
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 415))
                
            
        
    def test_416(self):
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
        self.assertTrue(TestAST.test(input, expect, 416))
                
            
        
    def test_417(self):
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
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([WhileStmt(Id(foo), BlockStmt([WhileStmt(FuncCall(bar, []), BlockStmt([WhileStmt(ArrayCell(stat, [IntegerLit(2)]), BlockStmt([AssignStmt(Id(fa), IntegerLit(9))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 417))
                
            
        
    def test_418(self):
        input = """
main: function void() {
do {
    jogging = true;
} while (x == 2);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(x), IntegerLit(2)), BlockStmt([AssignStmt(Id(jogging), BooleanLit(True))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 418))
                
            
        
    def test_419(self): #fail
        input = """
main: function void() {
{
    jogging = true;
    {
        walking = false;
    }
    
    a = 32;
}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([AssignStmt(Id(jogging), BooleanLit(True)), BlockStmt([AssignStmt(Id(walking), BooleanLit(False))]), AssignStmt(Id(a), IntegerLit(32))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 419))
                
            
        
    def test_420(self):
        input = """
main: function void() {
foo(job, is, hard, 13);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, Id(job), Id(is), Id(hard), IntegerLit(13))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 420))
                
            
        
    def test_421(self):
        input = """
main: function void() {
while (true)
    break;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 421))
                
            
        
    def test_422(self):
        input = """
main: function void() {
return;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 422))
                
            
        
    def test_423(self):
        input = """
main: function void() {
foo();
}

foo: function integer () {
return 138;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
	FuncDecl(foo, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(138))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 423))
                
            
        
    def test_424(self):
        input = """
main: function void() {
for (a = 0, a < 10, a + 1) {
    doSth();
}
for (b = 9, b < 139023, b * 2)
    dSth();
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(0)), BinExpr(<, Id(a), IntegerLit(10)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([CallStmt(doSth, )])), ForStmt(AssignStmt(Id(b), IntegerLit(9)), BinExpr(<, Id(b), IntegerLit(139023)), BinExpr(*, Id(b), IntegerLit(2)), CallStmt(dSth, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 424))
                
            
        
    def test_425(self):
        input = """main: function void() {
foo();
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 425))
                
            
        
    def test_426(self):
        input = """main: function void() {
foo(foo());
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, FuncCall(foo, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 426))
                
            
        
    def test_427(self):
        input = """main: function void() {
foo(foo(foo));
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, FuncCall(foo, [Id(foo)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 427))
                
            
        
    def test_428(self):
        input = """main: function void() {
foo(foo(foo(), foo));
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, FuncCall(foo, [FuncCall(foo, []), Id(foo)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 428))
                
            
        
    def test_429(self):
        input = """main: function void() {
foo(foo(foo(), foo, foo(foo(foo, foo(foo)))));
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, FuncCall(foo, [FuncCall(foo, []), Id(foo), FuncCall(foo, [FuncCall(foo, [Id(foo), FuncCall(foo, [Id(foo)])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 429))
                
            
        
    def test_430(self):
        input = """main: function void() {
foo((foo(foo(), foo, foo(foo(foo, foo(foo, foo(foo,foo,foo,foo,(foo()))))))));
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, FuncCall(foo, [FuncCall(foo, []), Id(foo), FuncCall(foo, [FuncCall(foo, [Id(foo), FuncCall(foo, [Id(foo), FuncCall(foo, [Id(foo), Id(foo), Id(foo), Id(foo), FuncCall(foo, [])])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 430))
                
            
        
    def test_431(self):
        input = """main: function void() {
foo((foo(foo((foo)), foo, foo(foo(foo, foo(foo, foo(foo,foo,foo,foo,(foo()))))))));
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, FuncCall(foo, [FuncCall(foo, [Id(foo)]), Id(foo), FuncCall(foo, [FuncCall(foo, [Id(foo), FuncCall(foo, [Id(foo), FuncCall(foo, [Id(foo), Id(foo), Id(foo), Id(foo), FuncCall(foo, [])])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 431))
                
            
        
    def test_432(self):
        input = """a: auto = foo();"""
        expect = """Program([
	VarDecl(a, AutoType, FuncCall(foo, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 432))
                
            
        
    def test_433(self):
        input = """a: auto = arr[932, 32];"""
        expect = """Program([
	VarDecl(a, AutoType, ArrayCell(arr, [IntegerLit(932), IntegerLit(32)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 433))
                
            
        
    def test_434(self):
        input = """a: auto = b;"""
        expect = """Program([
	VarDecl(a, AutoType, Id(b))
])"""
        self.assertTrue(TestAST.test(input, expect, 434))
                
            
        
    def test_435(self):
        input = """a: auto = 32;"""
        expect = """Program([
	VarDecl(a, AutoType, IntegerLit(32))
])"""
        self.assertTrue(TestAST.test(input, expect, 435))
                
            
        
    def test_436(self):
        input = """a: auto = 32_438;"""
        expect = """Program([
	VarDecl(a, AutoType, IntegerLit(32438))
])"""
        self.assertTrue(TestAST.test(input, expect, 436))
                
            
        
    def test_437(self):
        input = """a: auto = 32.32;"""
        expect = """Program([
	VarDecl(a, AutoType, FloatLit(32.32))
])"""
        self.assertTrue(TestAST.test(input, expect, 437))
                
            
        
    def test_438(self):
        input = """a: auto = true;"""
        expect = """Program([
	VarDecl(a, AutoType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 438))
                
            
        
    def test_439(self):
        input = """a: auto = false;"""
        expect = """Program([
	VarDecl(a, AutoType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 439))
                
            
        
    def test_440(self):
        input = """a: auto = "Foo bar is dub";"""
        expect = """Program([
	VarDecl(a, AutoType, StringLit(Foo bar is dub))
])"""
        self.assertTrue(TestAST.test(input, expect, 440))
                
            
        
    def test_441(self):
        input = """a: auto = -42;"""
        expect = """Program([
	VarDecl(a, AutoType, UnExpr(-, IntegerLit(42)))
])"""
        self.assertTrue(TestAST.test(input, expect, 441))
                
            
        
    def test_442(self):
        input = """a: auto = -bar;"""
        expect = """Program([
	VarDecl(a, AutoType, UnExpr(-, Id(bar)))
])"""
        self.assertTrue(TestAST.test(input, expect, 442))
                
            
        
    def test_443(self):
        input = """a: auto = ! true;"""
        expect = """Program([
	VarDecl(a, AutoType, UnExpr(!, BooleanLit(True)))
])"""
        self.assertTrue(TestAST.test(input, expect, 443))
                
            
        
    def test_444(self):
        input = """a: auto = ! barz;"""
        expect = """Program([
	VarDecl(a, AutoType, UnExpr(!, Id(barz)))
])"""
        self.assertTrue(TestAST.test(input, expect, 444))
                
            
        
    def test_445(self):
        input = """a: auto = --32;"""
        expect = """Program([
	VarDecl(a, AutoType, UnExpr(-, UnExpr(-, IntegerLit(32))))
])"""
        self.assertTrue(TestAST.test(input, expect, 445))
                
            
        
    def test_446(self):
        input = """a: auto = !!barz;"""
        expect = """Program([
	VarDecl(a, AutoType, UnExpr(!, UnExpr(!, Id(barz))))
])"""
        self.assertTrue(TestAST.test(input, expect, 446))
                
            
        
    def test_447(self):
        input = """a: auto = 32 * 32 * 32;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(*, BinExpr(*, IntegerLit(32), IntegerLit(32)), IntegerLit(32)))
])"""
        self.assertTrue(TestAST.test(input, expect, 447))
                
            
        
    def test_448(self):
        input = """a: auto = 32 / 32;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(/, IntegerLit(32), IntegerLit(32)))
])"""
        self.assertTrue(TestAST.test(input, expect, 448))
                
            
        
    def test_449(self):
        input = """a: auto = 32 % 32;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(%, IntegerLit(32), IntegerLit(32)))
])"""
        self.assertTrue(TestAST.test(input, expect, 449))
                
            
        
    def test_450(self):
        input = """a: auto = 3428 % 439 * 30 / 3428;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(/, BinExpr(*, BinExpr(%, IntegerLit(3428), IntegerLit(439)), IntegerLit(30)), IntegerLit(3428)))
])"""
        self.assertTrue(TestAST.test(input, expect, 450))
                
            
        
    def test_451(self):
        input = """a: auto = 3428 + 439;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(+, IntegerLit(3428), IntegerLit(439)))
])"""
        self.assertTrue(TestAST.test(input, expect, 451))
                
            
        
    def test_452(self):
        input = """a: auto = 4380 - 238;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(-, IntegerLit(4380), IntegerLit(238)))
])"""
        self.assertTrue(TestAST.test(input, expect, 452))
                
            
        
    def test_453(self):
        input = """a: auto = true && false;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(&&, BooleanLit(True), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 453))
                
            
        
    def test_454(self):
        input = """a: auto = true || false;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(||, BooleanLit(True), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 454))
                
            
        
    def test_455(self):
        input = """a: auto = true && false || true || false && true;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(&&, BinExpr(||, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), BooleanLit(True)), BooleanLit(False)), BooleanLit(True)))
])"""
        self.assertTrue(TestAST.test(input, expect, 455))
                
            
        
    def test_456(self):
        input = """a: auto = 13 == 32;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(==, IntegerLit(13), IntegerLit(32)))
])"""
        self.assertTrue(TestAST.test(input, expect, 456))
                
            
        
    def test_457(self):
        input = """a: auto = 13 == 32;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(==, IntegerLit(13), IntegerLit(32)))
])"""
        self.assertTrue(TestAST.test(input, expect, 457))
                
            
        
    def test_458(self):
        input = """a: auto = 13 < 32;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(<, IntegerLit(13), IntegerLit(32)))
])"""
        self.assertTrue(TestAST.test(input, expect, 458))
                
            
        
    def test_459(self):
        input = """a: auto = 13 > 32;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(>, IntegerLit(13), IntegerLit(32)))
])"""
        self.assertTrue(TestAST.test(input, expect, 459))
                
            
        
    def test_460(self):
        input = """a: auto = 13 < 32;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(<, IntegerLit(13), IntegerLit(32)))
])"""
        self.assertTrue(TestAST.test(input, expect, 460))
                
            
        
    def test_461(self):
        input = """a: auto = 13 >= 32;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(>=, IntegerLit(13), IntegerLit(32)))
])"""
        self.assertTrue(TestAST.test(input, expect, 461))
                
            
        
    def test_462(self):
        input = """a: auto = 13 <= 32;"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(<=, IntegerLit(13), IntegerLit(32)))
])"""
        self.assertTrue(TestAST.test(input, expect, 462))
                
            
        
    def test_463(self):
        input = """a: auto = "Hello world" :: "Foo";"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(::, StringLit(Hello world), StringLit(Foo)))
])"""
        self.assertTrue(TestAST.test(input, expect, 463))
                
            
        
    def test_464(self):
        input = """a: auto = ("Hello world" :: "John") :: foo; """
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(::, BinExpr(::, StringLit(Hello world), StringLit(John)), Id(foo)))
])"""
        self.assertTrue(TestAST.test(input, expect, 464))
                
            
        
    def test_465(self):
        input = """a: auto = "Hello world" :: ("John" :: foo); """
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(::, StringLit(Hello world), BinExpr(::, StringLit(John), Id(foo))))
])"""
        self.assertTrue(TestAST.test(input, expect, 465))
                
            
        
    def test_466(self):
        input = """a: auto = (a > 3) == (((3 != 2) < 3429) > (2 <= foo));"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(==, BinExpr(>, Id(a), IntegerLit(3)), BinExpr(>, BinExpr(<, BinExpr(!=, IntegerLit(3), IntegerLit(2)), IntegerLit(3429)), BinExpr(<=, IntegerLit(2), Id(foo)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 466))
                
            
        
    def test_467(self):
        input = """a: auto = ((!true == ! false) * barz / 43 + 443 - -438 + --430 --- 439) :: (("Hello" > 3289) < 843 * ( 328 :: 483));"""
        expect = """Program([
	VarDecl(a, AutoType, BinExpr(::, BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(/, BinExpr(*, BinExpr(==, UnExpr(!, BooleanLit(True)), UnExpr(!, BooleanLit(False))), Id(barz)), IntegerLit(43)), IntegerLit(443)), UnExpr(-, IntegerLit(438))), UnExpr(-, UnExpr(-, IntegerLit(430)))), UnExpr(-, UnExpr(-, IntegerLit(439)))), BinExpr(<, BinExpr(>, StringLit(Hello), IntegerLit(3289)), BinExpr(*, IntegerLit(843), BinExpr(::, IntegerLit(328), IntegerLit(483))))))
])"""
        self.assertTrue(TestAST.test(input, expect, 467))
                
            
        
    def test_468(self):
        input = """main: function void(/*This is the arg of main function */) {
if (/* put condition here */ a == 43 ) /* after which is the code */ { // put code here
    a = 3490;
}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(43)), BlockStmt([AssignStmt(Id(a), IntegerLit(3490))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 468))
                
            
        
    def test_469(self):
        input = """
press: function void(inherit key: string) inherit touch {
touch(key);
doSomePressing(key);
}"""
        expect = """Program([
	FuncDecl(press, VoidType, [InheritParam(key, StringType)], touch, BlockStmt([CallStmt(touch, Id(key)), CallStmt(doSomePressing, Id(key))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 469))
                
            
        
    def test_470(self):
        input = """press: function integer(inherit key: string, out status: integer, inherit out keyboard_id: integer) {}"""
        expect = """Program([
	FuncDecl(press, IntegerType, [InheritParam(key, StringType), OutParam(status, IntegerType), InheritOutParam(keyboard_id, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 470))
                
            