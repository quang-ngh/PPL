import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    #SIMPLE TEST
    def test_simple_program(self):
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_simple_program2(self):
        input = "delta: integer = 3;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_simple_program3(self):
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_simple_program4(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_simple_program5(self):
        input = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_simple_program6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_simple_program7(self):
        input = """preventDefault();"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_simple_program8(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
            printBoolean(n);
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
            preventDefault();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_simple_program9(self):
        """Declare Variable"""
        input = "x: array [1, 2] of integer;"
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_simple_program10(self):
        """Declare Variable"""
        input = """x: array [1, \"hello\"] of integer;"""
        expect = "Error on line 1 col 13: hello"
        self.assertTrue(TestParser.test(input,expect,210))


    #FUNCTION TEST
    def test_special_function1(self):
        input = """
        main: function void() {
            readInteger();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_special_function2(self):
        input = """
        main: function void() {
            readFloat();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_special_function3(self):
        input = """
        main: function void() {
            readBoolean();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_special_function4(self):
        input = """
        main: function void() {
            readString();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_special_function5(self):
        input = """
        main: function void() {
            x: integer = 3;
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_special_function6(self):
        input = """
        main: function void() {
            x: float = 3.2;
            writeFloat(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_special_function7(self):
        input = """
        main: function void() {
            x: boolean = true;
            printBoolean(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_special_function8(self):
        input = """
        main: function void() {
            x: string = "hello";
            printString(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_special_function9(self):
        input = """
        main: function void() {
            x: integer = 3;
            y: integer = 35;
            super(3+35,35/3);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_special_function10(self):
        input = """
        main: function void() {
            x: integer = 3_234;
            preventDefault();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    #STATEMENT TEST
    def test_statement1(self):
        input = """
        main: function void() {
            x: integer = 3_234;
            if(x==2)    x=4;
            else    x=56;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_statement2(self):
        input = """
        main: function void() {
            for (i = 1, i < 10, i + 1) {
                printInteger(i);
            }

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_statement3(self):
        input = """
        main: function void() {
            while (x==2)
                x=x+3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_statement4(self):
        input = """
        main: function void() {
            do {
                x: integer = 3;
                x=x+2;
            }
            while (x>0);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_statement5(self):
        input = """
        main: function void() {
            for (i = 1, i < 10, i + 1) {
                printInteger(i);
                if(i==5)    break;
                else    continue;
            }

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_statement6(self):
        input = """
        main: function integer() {
            for (i = 1, i < 10, i + 1) {
                printInteger(i);
                if(i==5)    break;
                else    continue;
            }
            return x;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_statement7(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        main: function void() {
            delta: integer = fact(3);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_statement8(self):
        input = """
        main: function void() {
            r, s: integer = 2, 3;
            a, b: integer;
            a, b : array [4] of integer ;
            s = r*r*s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))


    #DECLARATION TEST
    def test_declaration1(self):
        input = """
        main: function void() {
            a,b,c: float = 1.2,2.3,4.;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_declaration2(self):
        input = """
        main: function void() {
            a,b: float = 1.2,2.3,4.;
        }"""
        expect = "Error on line 3 col 32: ,"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_declaration3(self):
        input = """
        main: function void() {
            a: string = "hello";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_declaration4(self):
        input = """
        main: function void() {
            a,b: string = "hello","xinchao";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_declaration5(self):
        input = """
        main: function void() {
            a: string;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_declaration6(self):
        input = """
        main: function void() {
            inherit a: string;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_declaration7(self):
        input = """
        main: function void() {
            out a: string;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_declaration8(self):
        input = """
        main: function void() {
            inherit out a: string;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_declaration9(self):
        input = """
        main: function void() {
            out inherit a: string;
        }"""
        expect = "Error on line 3 col 16: inherit"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_declaration10(self):
        input = """
        main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_declaration11(self):
        input = """
        x: function string() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_declaration12(self):
        input = """
        main: function integer(a:integer,b:string,c:array[2]of integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_declaration13(self):
        input = """
        main: function integer(out a:integer,inherit c:array[2]of integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_declaration14(self):
        input = """
        main: function integer(a:integer,inherit out c:array[2]of integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_declaration15(self):
        input = """
        main: function integer(a:integer,c:array[2]of integer) {
            goo();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_declaration16(self):
        input = """
        main: function auto(a:integer,c:array[2]of integer) {
            goo(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_declaration17(self):
        input = """
        main: function auto(a:integer,c:array[2]of integer) {
            goo();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_declaration18(self):
        input = """
        main: function auto(a:integer,c:array[2]of integer) {
            goo(foo(noo(x)));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_declaration19(self):
        input = """
        main: function auto(a:integer,c:array[2]of integer) {
            goo(x+y*s/12==2);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_declaration20(self):
        input = """
        main: function auto(a:integer,c:array[2]of integer) {
            goo(a>b==c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_declaration21(self):
        input = """
        main: function auto(a:integer,c:array[2]of integer) {
            goo(a[0]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_declaration22(self):
        input = """
        main: function auto(a:integer,c:array[2]of integer) {
            goo(a[0, 1] + a[1, 0], a>b==c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    #EXPRESSION TEST
    def test_expression1(self):
        input = """
        main: function auto() {
            x : integer = 1+2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_expression2(self):
        input = """
        main: function auto() {
            x : string = "hello"::"xinchao";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_expression3(self):
        input = """
        main: function auto() {
            x : integer = x+y > y+z;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_expression4(self):
        input = """
        main: function auto() {
            x : integer = x+ds+sdf+5 == (sadf+12) && s12hello ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_expression5(self):
        input = """
        main: function auto() {
            x : integer = (x+ds+sdf+5 || (sadf+12) != s12hello) >=3 ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_expression6(self):
        input = """
        main: function auto() {
            x : integer = ((3>5)>6)>7;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_expression7(self):
        input = """
        main: function auto() {
            x : integer = 1>2>3 ;
        }"""
        expect = "Error on line 3 col 29: >"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_expression8(self):
        input = """
        main: function auto() {
            x : integer = ((3>5)>6)>7 + 12 + 12&&53 + "Hello"::"Xinchao";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_expression9(self):
        input = """
        main: function auto() {
            x : integer = ((3>5)>6)>7 + 12 + 12&&53 + "Hell\\r2"::"Xinchao";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_expression10(self):
        input = """
        main: function auto() {
            x : integer = !(23 && ab || cd ) / 2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_expression11(self):
            input = """
            main: function auto() {
                x : integer = (11+12)*13%14;
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,261))
            
    def test_expression12(self):
            input = """
            main: function auto() {
                x : float = (31.0-3.0)*3.14/2.2;
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,262))

    def test_expression13(self):
            input = """
            main: function auto() {
                x : string = "this is a string";
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,263))

    def test_expression14(self):
            input = """
            main: function auto() {
                x : boolean = (1<2)<3 || ((4>=5)>6);
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,264))

    def test_expression15(self):
            input = """
            main: function auto() {
                x : boolean = !(((3>5)>6)>7);
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,265))

    def test_expression16(self):
            input = """
            main: function auto() {
                x : integer = (20-2)*4-4/2;
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,266))

    def test_expression17(self):
            input = """
            main: function auto() {
                x : float= (3.0+2.0)*(2.2-1.2);
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,267))

    def test_expression18(self):
            input = """
            main: function auto() {
                x : string = "Hello\\r2"::"Xinchao";
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,268))

    def test_expression19(self):
            input = """
            main: function auto() {
                x : integer = ((3>5)>6)>7 + 12 + 12&&53 + "Hell\\r2"::"Xinchao";
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,269))
    def test_expression20(self):
            input = """
            main: function auto() {
                x : integer = (("Nahhhh")) + "Hell\\r2"::"Xinchao";
            }"""
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,270))






    def test_more_complex_program_11(self):
        """More complex program"""
        input = """
        PRINT: function integer(a: integer){
            Date=9;
            i: integer;
            for(i=0,i<8,i=i+1)
                Date=Date+1;
            return 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))        

    def test_more_complex_program_12(self):
        """More complex program"""
        input = """
        PRINT: function void(a: integer){
            Date=9;
            i :integer;
            i=10;
            if(i>8)
                Date=Date+3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))  

    def test_more_complex_program_13(self):
        """More complex program"""
        input = """Date : integer;
        PRINT: function boolean(a: integer){
            n: boolean;
            n=true;
            return true;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_more_complex_program_14(self):
        """More complex program"""
        input = """
        Month: function float(date: integer){}
        PRINT: function void(a: integer){
            x: integer;
            x=date;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_more_complex_program_15(self):
        """More complex program"""
        input = """date,month: integer;
        Year: function integer(month:array[12] of integer, date: array[365] of integer){}
        PRINT: function boolean(a: integer){}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_more_complex_program_16(self):
        """More complex program"""
        input = """main: function string() {
        printString("Hello World!!!");
        return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_more_complex_program_17(self):
        """More complex program"""
        input = """main: function integer(argc: integer){ 
        name: array[20] of string; 
        printString("Hay nhap ten cua ban:");  
        readString();
        printString("Xin chao name");          
        return 0; }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_more_complex_program_18(self):
        """More complex program"""
        input = """operator: function integer(num: integer){   
            x: integer;
            x = 12;
            y: integer;
            y = 5;
            tong, hieu, tich, thuong : integer;
            tong = x + y;
            hieu= x - y;
            tich = x * y;
        }
        main: function integer(){
            operator(10);
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))        

    def test_more_complex_program_19(self):
        """More complex program"""
        input = """  
        x,y: integer;
        tong, hieu, tich, thuong: integer;
        main: function integer(){
            tong = x + y;
            hieu= x - y;
            tich = x * y;
            average: float;
            average = tong/2;
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))        

    def test_more_complex_program_20(self):
        """More complex program"""
        input = """  
        main: function integer(){
            m,n: integer = 1,2;
            i: integer; //counter
            printString("Enter m: ");
            Nhap(m);
            printString("Enter n: ");
            Nhap(n);
            if (n<m){
                printString("Numbers from n to m: ");
                for(i=n,i<=m,i=i+1){
                    printString(i);
                }
            }
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280)) 

    def test_more_complex_program_21(self):
        """More complex program"""
        input = """operator: function integer(num: integer){   
            x: integer;
            x = 12;
            y: integer;
            y = 5;
            tong, hieu, tich, thuong: integer = 0,0,0,0;
            tong = x + y;
            hieu= x - y;
            tich = x * y;
        }
        compute: function integer(x:integer,y:integer,tong:integer){
            operator(10);
            return tong;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))        

    def test_more_complex_program_22(self):
        """More complex program"""
        input = """Array: function integer(num: integer){   
            for(i=0,i<100,i=i+1){
                arr[i]=num;
            }
        }
        compute: function float(x:float,y:float,tong:float){
            for(i=0,i<100,i=i+1){
                tong=tong+arr;
            }
            return tong;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))        

    def test_more_complex_program_23(self):
        """More complex program"""
        input = """
        arr: array[10] of boolean;
        print: function void(arr: array[2] of boolean){}
        compute: function void(x:integer,y:integer,tong: array[2] of integer){
            for(i=0,i<100,i=i+1){
                arr=true;
                printInteger(arr);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))                

    def test_more_complex_program_24(self):
        """More complex program"""
        input = """
        print: function void(arr: array[12] of boolean){}
        test_prog: function void(){
            arr: array[10] of boolean;
            printBoolean(arr);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_more_complex_program_25(self):
        """More complex program"""
        input = """
        a:string;
        printsss:function void(a:string){
            printString(a);
        }
        test_program:function void(){
            a = "dfghjkfg";
            printsss(a);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))        

    def test_more_complex_program_26(self):
        """More complex program"""
        input = """
        a, b, c: float;
        x, y, z: boolean;
        g, h, y: integer;
        nty: function float(){}
        x, y, z:integer;
        a,w,q:string; 
        /*
        =======================================
        Comment here
        =======================================
        */
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))        

    def test_more_complex_program_27(self):
        """More complex program"""
        input = """
        a:string;
        plusFuncInt: function integer(x:integer, y:integer) {
            return x + y;
        }
        plusFuncDouble:function float(x:float, y:float) {
            return x + y;
        }       
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))        

    def test_more_complex_program_28(self):
        """More complex program"""
        input = """
        a:string;
        plusFuncInt: function integer(x:integer, y:integer) {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))        

    def test_more_complex_program_29(self):
        """More complex program"""
        input = """
        a:string;
        plusFuncInt: function integer(x:integer, y:integer) {
            sum:integer;
            for(x=1,x<10,x=y+1){
                if(x==5)
                    break;
            }
            return x;
        }       
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))                

    def test_more_complex_program_30(self):
        """More complex program"""
        input = """
        a:string;
        plusFuncDouble: function float(x:float, y:float) {
            for(y=0,y<=x,y=y+1)
            if(y<x)
                continue;
            else
                return y;
        }       
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))        

    def test_more_complex_program_31(self):
        """More complex program"""
        input = """
        main: function integer(){
            foo(2);
            (3+x) = a(b(2)) + 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))        

    def test_more_complex_program_32(self):
        """More complex program"""
        input = """
        c:function string(){
            3[3+x] = true[b[2]] +3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))        

    def test_more_complex_program_33(self):
        """More complex program"""
        input = """
        c:function string(){
            arr: array[3] of boolean;
            crr[3+x-y*342];
            drr(2,4)[3+x-y*342];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))        

    def test_more_complex_program_34(self):
        """More complex program"""
        input = """
        foo:function integer ( a:integer , b:float )
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))        

    def test_more_complex_program_35(self):
        """More complex program"""
        input = """
        main:function integer( argc:integer , argv:float )
        {
            c:boolean ;
            i:integer ;
            for(i=0,i<100,i=a+3){
                d:integer ;
                d = i + 3 ;
                readInteger() ;
            }
            printInteger(d);
            return i ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))                

    def test_more_complex_program_36(self):
        """More complex program"""
        input = """
        main: function integer( argc:integer , str:string )
        {
            c:boolean ;
            i:integer ;
            i=10;
            if(i>=argc && c==true){
                d:integer ;
                str = "Hello World";
                pritnInteger(d ) ;
            }
            printString(str);
            return i ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_more_complex_program_37(self):
        """More complex program"""
        input = """
        count:function void(money: array[12] of integer){
            sum,i:integer = 0,0;
            sum=0;
            i=0;
            do
            sum=sum+money[i+1];
            while(i<=100);
        }
        main:function integer( argc:integer , str:string )
        {
            c:boolean ;
            printInteger(argc);
            printString(str);
            return i ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))        

    def test_more_complex_program_38(self):
        """More complex program"""
        input = """main: function void( ){ if (a) if (b) if (c) for(i=0,i<9,i=i+1) foo(2,4); else a; else for(i=0,i<9,i=i+1) foo(2,4);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_more_complex_program_39(self):
        """More complex program"""
        input = """main: function void( ){ if (a) if (b) if (c) a; else a; else a;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def test_more_complex_program_40(self):
        """More complex program"""
        input = """main:function integer() {
            (a+b)+(c+d)==(a+b)+(c+d);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))