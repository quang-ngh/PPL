import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # Testcase  300
    def testcase300(self):
        testno= 300
        testcase = """x: integer = 1;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  301
    def testcase301(self):
        testno= 301
        testcase = """y: float = 10.3;"""
        expect = """Program([
	VarDecl(y, FloatType, FloatLit(10.3))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  302
    def testcase302(self):
        testno= 302
        testcase = """flag: boolean = false;"""
        expect = """Program([
	VarDecl(flag, BooleanType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  303
    def testcase303(self):
        testno= 303
        testcase = """newArr: array[4,5] of float = {1,2,3,4,5};"""
        expect = """Program([
	VarDecl(newArr, ArrayType([4, 5], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  304
    def testcase304(self):
        testno= 304
        testcase = """autoVar: auto = 123;"""
        expect = """Program([
	VarDecl(autoVar, AutoType, IntegerLit(123))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  305
    def testcase305(self):
        testno= 305
        testcase = """a,b,c : float = 10.3, 20.2, 5.678;"""
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(10.3))
	VarDecl(b, FloatType, FloatLit(20.2))
	VarDecl(c, FloatType, FloatLit(5.678))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  306
    def testcase306(self):
        testno= 306
        testcase = """arr1, arr2, arr3: array[1,2] of integer = {1,2}, {3,4}, {5,6};"""
        expect = """Program([
	VarDecl(arr1, ArrayType([1, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(arr2, ArrayType([1, 2], IntegerType), ArrayLit([IntegerLit(3), IntegerLit(4)]))
	VarDecl(arr3, ArrayType([1, 2], IntegerType), ArrayLit([IntegerLit(5), IntegerLit(6)]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  307
    def testcase307(self):
        testno= 307
        testcase = """str1, str2, str3: string = "kha", "dep", "trai";"""
        testcase1 = """a,b,c : float = 10.3, 20.2, 5.678;"""
        expect = """Program([
	VarDecl(str1, StringType, StringLit(kha))
	VarDecl(str2, StringType, StringLit(dep))
	VarDecl(str3, StringType, StringLit(trai))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  308
    def testcase308(self):
        testno= 308
        testcase = """print: function integer (){}"""
        expect = """Program([
	FuncDecl(print, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  309
    def testcase309(self):
        testno= 309
        testcase = """add: function integer(a:integer, b:integer){
                            return a+b;
                    }"""
        expect = """Program([
	FuncDecl(add, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  310
    def testcase310(self):
        testno= 310
        testcase = """foo: function void(x: integer){
                            if(x>=10)
                                print("kha dep trai");
                            else{
                                if(x%2==0)
                                    print("kha xau trai");
                                else{
                                    print("kha vjp pro");
                                    print("kha dep trai x10");
                                }
                            }
                    }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(x), IntegerLit(10)), CallStmt(print, StringLit(kha dep trai)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), CallStmt(print, StringLit(kha xau trai)), BlockStmt([CallStmt(print, StringLit(kha vjp pro)), CallStmt(print, StringLit(kha dep trai x10))]))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  311
    def testcase311(self):
        testno= 311
        testcase = """ageCalculate: function integer(){
                            print("nhap so tuoi cua ban: ");
                            ageVar = readInput();
                            print("so tuoi cua ban la: ", ageVar);
                    }"""
        expect = """Program([
	FuncDecl(ageCalculate, IntegerType, [], None, BlockStmt([CallStmt(print, StringLit(nhap so tuoi cua ban: )), AssignStmt(Id(ageVar), FuncCall(readInput, [])), CallStmt(print, StringLit(so tuoi cua ban la: ), Id(ageVar))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  312
    def testcase312(self):
        testno= 312
        testcase = """fact: function integer (n: integer){
                        if (n==0)
                            return 1;
                        else
                            return n*fact(n-1);
                    }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  313
    def testcase313(self):
        testno= 313
        testcase = """simpleFunc1: function auto(){
                        return 1+1;
                    }"""
        expect = """Program([
	FuncDecl(simpleFunc1, AutoType, [], None, BlockStmt([ReturnStmt(BinExpr(+, IntegerLit(1), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  314
    def testcase314(self):
        testno= 314
        testcase = """simpleFunc2: function void(){
                        print("hehehe");
                    }"""
        expect = """Program([
	FuncDecl(simpleFunc2, VoidType, [], None, BlockStmt([CallStmt(print, StringLit(hehehe))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  315
    def testcase315(self):
        testno= 315
        testcase = """a: integer = 2;
                       b: integer = 3;
                       mulfunc: function integer(x: integer, y: integer){
                            return x*y;
                    }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	VarDecl(b, IntegerType, IntegerLit(3))
	FuncDecl(mulfunc, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  316
    def testcase316(self):
        testno= 316
        testcase = """func: function void(){
                        x=2;
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(x), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  317
    def testcase317(self):
        testno= 317
        testcase = """func: function void(){
                        kha="deptrai";
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(kha), StringLit(deptrai))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  318
    def testcase318(self):
        testno= 318
        testcase = """func: function void(){
                        arr[0,1]=6.9;
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), FloatLit(6.9))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  319
    def testcase319(self):
        testno= 319
        testcase = """func: function void(){
                        varA = varB;
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(varA), Id(varB))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  320
    def testcase320(self):
        testno= 320
        testcase = """func: function void(){
                        cars = {"honda","toyota","nissan"};
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(cars), ArrayLit([StringLit(honda), StringLit(toyota), StringLit(nissan)]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  321
    def testcase321(self):
        testno= 321
        testcase = """func: function void(){
                        myCar = cars[1];
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(myCar), ArrayCell(cars, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  322
    def testcase322(self):
        testno= 322
        testcase = """func: function void(){
                        result = calculate(a, b);
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(result), FuncCall(calculate, [Id(a), Id(b)]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  323
    def testcase323(self):
        testno= 323
        testcase = """func: function void(){
                        flag = false;
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(flag), BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  324
    def testcase324(self):
        testno= 324
        testcase = """func: function void(){if(thoiTietHomNay == "mua")
                            nghiHoc();}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(thoiTietHomNay), StringLit(mua)), CallStmt(nghiHoc, ))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  325
    def testcase325(self):
        testno= 325
        testcase = """func: function void(){if(thoiTietHomNay == "nang")
                            nghiHoc();}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(thoiTietHomNay), StringLit(nang)), CallStmt(nghiHoc, ))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  326
    def testcase326(self):
        testno= 326
        testcase = """func: function void(){if(emDongY == true)
                            print("To tinh thanh cong");
                        else
                            print("Mai lam ban nhe");
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(emDongY), BooleanLit(True)), CallStmt(print, StringLit(To tinh thanh cong)), CallStmt(print, StringLit(Mai lam ban nhe)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  327
    def testcase327(self):
        testno= 327
        testcase = """func: function void(){if(a || b){
                        if(a)
                            print(a);
                        else
                            print(c);
                        }
                        else
                        print(d);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(||, Id(a), Id(b)), BlockStmt([IfStmt(Id(a), CallStmt(print, Id(a)), CallStmt(print, Id(c)))]), CallStmt(print, Id(d)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  328
    def testcase328(self):
        testno= 328
        testcase = """func: function void(){if(today < deadline)
                            hanNop = "dunghan";
                        else
                            hanNop = "trehan";
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, Id(today), Id(deadline)), AssignStmt(Id(hanNop), StringLit(dunghan)), AssignStmt(Id(hanNop), StringLit(trehan)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  329
    def testcase329(self):
        testno= 329
        testcase = """func: function void(){if(!troimua)
                            diBay();}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(UnExpr(!, Id(troimua)), CallStmt(diBay, ))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  330
    def testcase330(self):
        testno= 330
        testcase = """func: function void(){if(a%2==0)
                            print("a la so chan");
                        else
                            print("a la so le");}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(0)), CallStmt(print, StringLit(a la so chan)), CallStmt(print, StringLit(a la so le)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  331
    def testcase331(self):
        testno= 331
        testcase = """func: function void(){if(1==2)
                            print("kho bau one piece");
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, IntegerLit(1), IntegerLit(2)), CallStmt(print, StringLit(kho bau one piece)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  332
    def testcase332(self):
        testno= 332
        testcase = """func: function void(){for(x=1, x<=100, x+1){
                        print("chep phat 100 lan");
                    }
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(<=, Id(x), IntegerLit(100)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([CallStmt(print, StringLit(chep phat 100 lan))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  333
    def testcase333(self):
        testno= 333
        testcase = """func: function void(){for(i=1, i<=10,i+1)
                        chayMotVongSanTruong();
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(chayMotVongSanTruong, ))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  334
    def testcase334(self):
        testno= 334
        testcase = """func: function void(){for(i=0, i < arrayLength, i+1){
                            arr[i]=arr[i]*2;
                    }
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(arrayLength)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i)]), BinExpr(*, ArrayCell(arr, [Id(i)]), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  335
    def testcase335(self):
        testno= 335
        testcase = """func: function void(){for(i=0, i < verticalSize, i+1){
                            for(j=0, j < horizontalSize, j+1)
                                arr[i, j] = 13; 
                            
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(verticalSize)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(horizontalSize)), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(ArrayCell(arr, [Id(i), Id(j)]), IntegerLit(13)))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  336
    def testcase336(self):
        testno= 336
        testcase = """func: function void(){for(i = 0, i < 100, i+1){
                            if(i%2==0)
                                print(i);
                    }
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), CallStmt(print, Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  337
    def testcase337(self):
        testno= 337
        testcase = """func: function void(){for(i=0,i<100,i+1){
                            if(i%2==0)
                                continue;
                            print(i);
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), ContinueStmt()), CallStmt(print, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  338
    def testcase338(self):
        testno= 338
        testcase = """func: function void(){for(i=100, i > 0, i-1){
                            doSomething();
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(100)), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(doSomething, )]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  339
    def testcase339(self):
        testno= 339
        testcase = """func: function void(){for(i=0,i<69,i+1){
                            doAnotherThing();
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(69)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(doAnotherThing, )]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  340
    def testcase340(self):
        testno= 340
        testcase = """func: function void(){while(true)
                            diNgu();}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), CallStmt(diNgu, ))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  341
    def testcase341(self):
        testno= 341
        testcase = """func: function void(){while(x>0){
                        print("i love you");
                        x = x - 1;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([CallStmt(print, StringLit(i love you)), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  342
    def testcase342(self):
        testno= 342
        testcase = """func: function void(){while(x<100){
                        if(x%2==0)
                            continue;
                        print(x);
                        x=x+1;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(100)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), ContinueStmt()), CallStmt(print, Id(x)), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  343
    def testcase343(self):
        testno= 343
        testcase = """func: function void(){while(a!=b){
                        a = arr[x];
                        b = arr[arrSize-x];
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), ArrayCell(arr, [Id(x)])), AssignStmt(Id(b), ArrayCell(arr, [BinExpr(-, Id(arrSize), Id(x))]))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  344
    def testcase344(self):
        testno= 344
        testcase = """func: function void(){while(a<100){
                            while(b<100){
                                arr[a,b] = 10;
                                b = b+1;
                            }
                            a = a + 1;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(100)), BlockStmt([WhileStmt(BinExpr(<, Id(b), IntegerLit(100)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(a), Id(b)]), IntegerLit(10)), AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1)))])), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  345
    def testcase345(self):
        testno= 345
        testcase = """func: function void(){while(!flag){
                            print("world cup");
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(UnExpr(!, Id(flag)), BlockStmt([CallStmt(print, StringLit(world cup))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  346
    def testcase346(self):
        testno= 346
        testcase = """func: function void(){while(state)
                            funcCall();
                        while(taste)
                            callFunc();
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(Id(state), CallStmt(funcCall, )), WhileStmt(Id(taste), CallStmt(callFunc, ))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  347
    def testcase347(self):
        testno= 347
        testcase = """func: function void(){while(mood == "happy"){
                            study();
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(mood), StringLit(happy)), BlockStmt([CallStmt(study, )]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  348
    def testcase348(self):
        testno= 348
        testcase = """func: function void(){do{sleep();}
                        while(everybodyStudying());}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(FuncCall(everybodyStudying, []), BlockStmt([CallStmt(sleep, )]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  349
    def testcase349(self):
        testno= 349
        testcase = """func: function void(){do{
                            study();
                            eat();
                            x = 1;
                    }while(everybodySleeping());}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(FuncCall(everybodySleeping, []), BlockStmt([CallStmt(study, ), CallStmt(eat, ), AssignStmt(Id(x), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  350
    def testcase350(self):
        testno= 350
        testcase = """func: function void(){do{
                            x = x + 1;
                    }while (x<100);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(100)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  351
    def testcase351(self):
        testno= 351
        testcase = """func: function void(){do{
                            dostuff();
                    }
                    while(homeAlone == true);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(homeAlone), BooleanLit(True)), BlockStmt([CallStmt(dostuff, )]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  352
    def testcase352(self):
        testno= 352
        testcase = """func: function void(){do{
                            toInfinity();
                    }while(flag == true); }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(flag), BooleanLit(True)), BlockStmt([CallStmt(toInfinity, )]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  353
    def testcase353(self):
        testno= 353
        testcase = """func: function void(){do{
                        laugh();
                        eat();
                        hehe = 123;
                    } while(hotFood);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(Id(hotFood), BlockStmt([CallStmt(laugh, ), CallStmt(eat, ), AssignStmt(Id(hehe), IntegerLit(123))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  354
    def testcase354(self):
        testno= 354
        testcase = """func: function void(){do{
                        takeExercise();
                        x = a + b;
                        print(x);
                    }while(systemLoading);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(Id(systemLoading), BlockStmt([CallStmt(takeExercise, ), AssignStmt(Id(x), BinExpr(+, Id(a), Id(b))), CallStmt(print, Id(x))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  355
    def testcase355(self):
        testno= 355
        testcase = """func: function void(){do{
                        wakeUp();
                    }while(!troiToi);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(UnExpr(!, Id(troiToi)), BlockStmt([CallStmt(wakeUp, )]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  356
    def testcase356(self):
        testno= 356
        testcase = """func: function void(){for(i=1,i<100,i+1){
                        print(i);
                        if(i == a)
                            break;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, Id(i)), IfStmt(BinExpr(==, Id(i), Id(a)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  357
    def testcase357(self):
        testno= 357
        testcase = """func: function void(){while(i<100){
                        print(i);
                        if(i==a)
                            break;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(100)), BlockStmt([CallStmt(print, Id(i)), IfStmt(BinExpr(==, Id(i), Id(a)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  358
    def testcase358(self):
        testno= 358
        testcase = """func: function void(){do{
                            print(i);
                            if(i==a)
                                break;
                    }while(i<100);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(100)), BlockStmt([CallStmt(print, Id(i)), IfStmt(BinExpr(==, Id(i), Id(a)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  359
    def testcase359(self):
        testno= 359
        testcase = """func: function void(){for(x=1,x<100,x+1){
                        print(x);
                        if(x == a)
                            break;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(<, Id(x), IntegerLit(100)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([CallStmt(print, Id(x)), IfStmt(BinExpr(==, Id(x), Id(a)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  360
    def testcase360(self):
        testno= 360
        testcase = """func: function void(){while(x<100){
                        print(x);
                        if(x==a)
                            break;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(100)), BlockStmt([CallStmt(print, Id(x)), IfStmt(BinExpr(==, Id(x), Id(a)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  361
    def testcase361(self):
        testno= 361
        testcase = """func: function void(){do{
                            print(x);
                            if(x==a)
                                break;
                    }while(y<100);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(y), IntegerLit(100)), BlockStmt([CallStmt(print, Id(x)), IfStmt(BinExpr(==, Id(x), Id(a)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  362
    def testcase362(self):
        testno= 362
        testcase = """func: function void(){for(y=1,y<100,y+1){
                        print(y);
                        if(y == a)
                            break;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(1)), BinExpr(<, Id(y), IntegerLit(100)), BinExpr(+, Id(y), IntegerLit(1)), BlockStmt([CallStmt(print, Id(y)), IfStmt(BinExpr(==, Id(y), Id(a)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  363
    def testcase363(self):
        testno= 363
        testcase = """func: function void(){while(y<100){
                        print(y);
                        if(y==a)
                            break;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(y), IntegerLit(100)), BlockStmt([CallStmt(print, Id(y)), IfStmt(BinExpr(==, Id(y), Id(a)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  364
    def testcase364(self):
        testno= 364
        testcase = """func: function void(){for(i=1,i<100,i+1){
                        print(i);
                        if(i == a)
                            continue;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, Id(i)), IfStmt(BinExpr(==, Id(i), Id(a)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  365
    def testcase365(self):
        testno= 365
        testcase = """func: function void(){while(i<100){
                        print(i);
                        if(i==a)
                            continue;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(100)), BlockStmt([CallStmt(print, Id(i)), IfStmt(BinExpr(==, Id(i), Id(a)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  366
    def testcase366(self):
        testno= 366
        testcase = """func: function void(){do{
                            print(i);
                            if(i==a)
                                continue;
                    }while(i<100);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(100)), BlockStmt([CallStmt(print, Id(i)), IfStmt(BinExpr(==, Id(i), Id(a)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  367
    def testcase367(self):
        testno= 367
        testcase = """func: function void(){for(x=1,x<100,x+1){
                        print(x);
                        if(x == a)
                            continue;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(<, Id(x), IntegerLit(100)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([CallStmt(print, Id(x)), IfStmt(BinExpr(==, Id(x), Id(a)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  368
    def testcase368(self):
        testno= 368
        testcase = """func: function void(){while(x<100){
                        print(x);
                        if(x==a)
                            continue;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(100)), BlockStmt([CallStmt(print, Id(x)), IfStmt(BinExpr(==, Id(x), Id(a)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  369
    def testcase369(self):
        testno= 369
        testcase = """func: function void(){do{
                            print(x);
                            if(x==a)
                                continue;
                    }while(y<100);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(y), IntegerLit(100)), BlockStmt([CallStmt(print, Id(x)), IfStmt(BinExpr(==, Id(x), Id(a)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  370
    def testcase370(self):
        testno= 370
        testcase = """func: function void(){for(y=1,y<100,y+1){
                        print(y);
                        if(y == a)
                            continue;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(1)), BinExpr(<, Id(y), IntegerLit(100)), BinExpr(+, Id(y), IntegerLit(1)), BlockStmt([CallStmt(print, Id(y)), IfStmt(BinExpr(==, Id(y), Id(a)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  371
    def testcase371(self):
        testno= 371
        testcase = """func: function void(){while(y<100){
                        print(y);
                        if(y==a)
                            continue;
                    }}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(y), IntegerLit(100)), BlockStmt([CallStmt(print, Id(y)), IfStmt(BinExpr(==, Id(y), Id(a)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  372
    def testcase372(self):
        testno= 372
        testcase = """intFunc1: function integer(a: integer, b:integer){
                        return a + b;
                    }"""
        expect = """Program([
	FuncDecl(intFunc1, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  373
    def testcase373(self):
        testno= 373
        testcase = """floatFunc1: function float(a: float, b:float){
                        return a * b;
                    }"""
        expect = """Program([
	FuncDecl(floatFunc1, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  374
    def testcase374(self):
        testno= 374
        testcase = """autoFunc1: function auto(a: string, b: string){
                        return a::b;
                    }"""
        expect = """Program([
	FuncDecl(autoFunc1, AutoType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  375
    def testcase375(self):
        testno= 375
        testcase = """intFunc2: function integer(a: integer, b:integer){
                        return a + b;
                    }"""
        expect = """Program([
	FuncDecl(intFunc2, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  376
    def testcase376(self):
        testno= 376
        testcase = """floatFunc2: function float(a: float, b:float){
                        return a * b;
                    }"""
        expect = """Program([
	FuncDecl(floatFunc2, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  377
    def testcase377(self):
        testno= 377
        testcase = """autoFunc2: function auto(a: string, b: string){
                        return a::b;
                    }"""
        expect = """Program([
	FuncDecl(autoFunc2, AutoType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  378
    def testcase378(self):
        testno= 378
        testcase = """intFunc3: function integer(a: integer, b:integer){
                        return a + b;
                    }"""
        expect = """Program([
	FuncDecl(intFunc3, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  379
    def testcase379(self):
        testno= 379
        testcase = """floatFunc3: function float(a: float, b:float){
                        return a * b;
                    }"""
        expect = """Program([
	FuncDecl(floatFunc3, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  380
    def testcase380(self):
        testno= 380
        testcase = """func: function void(){addAndPrint(a,b);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(addAndPrint, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  381
    def testcase381(self):
        testno= 381
        testcase = """func: function void(){mulAndPrint(a,b);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(mulAndPrint, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  382
    def testcase382(self):
        testno= 382
        testcase = """func: function void(){subAndPrint(a,b);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(subAndPrint, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  383
    def testcase383(self):
        testno= 383
        testcase = """func: function void(){divAndPrint(a,b);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(divAndPrint, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  384
    def testcase384(self):
        testno= 384
        testcase = """func: function void(){print("kha dep trai");}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(print, StringLit(kha dep trai))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  385
    def testcase385(self):
        testno= 385
        testcase = """func: function void(){goo();}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(goo, )]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  386
    def testcase386(self):
        testno= 386
        testcase = """func: function void(){printFraction(2,3);}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(printFraction, IntegerLit(2), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  387
    def testcase387(self):
        testno= 387
        testcase = """func: function void(){sleep();}"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(sleep, )]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  388
    def testcase388(self):
        testno= 388
        testcase = """func: function void(){
                            doSomething();
                            add();
                            sleep();
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(doSomething, ), CallStmt(add, ), CallStmt(sleep, )]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  389
    def testcase389(self):
        testno= 389
        testcase = """func: function void(){
                            x: integer = 1;
                            a: integer = 2;
                            b: integer;
                            b = a + x;
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(a, IntegerType, IntegerLit(2)), VarDecl(b, IntegerType), AssignStmt(Id(b), BinExpr(+, Id(a), Id(x)))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  390
    def testcase390(self):
        testno= 390
        testcase = """func: function void(){
                            add(1,2);
                            sleep();
                        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(add, IntegerLit(1), IntegerLit(2)), CallStmt(sleep, )]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  391
    def testcase391(self):
        testno= 391
        testcase = """func: function void(){
                        if(troiNang == true){
                            rangoaichoi();
                        }
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(troiNang), BooleanLit(True)), BlockStmt([CallStmt(rangoaichoi, )]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  392
    def testcase392(self):
        testno= 392
        testcase = """func: function void(){
                        getCookie();
                        drinkMilk();
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(getCookie, ), CallStmt(drinkMilk, )]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  393
    def testcase393(self):
        testno= 393
        testcase = """func: function void(){
                        getCookie();
                        drinkMilk();
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(getCookie, ), CallStmt(drinkMilk, )]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  394
    def testcase394(self):
        testno= 394
        testcase = """func: function void(){
                        print("hehehe", my);
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(print, StringLit(hehehe), Id(my))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  395
    def testcase395(self):
        testno= 395
        testcase = """func: function void(){
                        foo(a,b);
                    }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([CallStmt(foo, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  396
    def testcase396(self):
        testno= 396
        testcase = """x:integer = 1;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  397
    def testcase397(self):
        testno= 397
        testcase = """add: function integer(a: integer, b: integer){}"""
        expect = """Program([
	FuncDecl(add, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  398
    def testcase398(self):
        testno= 398
        testcase = """func: function void(){
                        if(x>2){
                            print("hehehe");
                        }
                      }
                    """
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(x), IntegerLit(2)), BlockStmt([CallStmt(print, StringLit(hehehe))]))]))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
    
    # Testcase  399
    def testcase399(self):
        testno= 399
        testcase = """a,b,c: integer = 1,2,3;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(testcase, expect, testno))
#############################################################
    
    # # Testcase  39x
    # def testcase39x(self):
    #     testno= 390
    #     testcase = """"""
    #     expect = """successfull"""
    #     self.assertTrue(TestAST.test(testcase, expect, testno))
    
    
    
    
    
    