import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_redeclared_variable1(self):
        """test_redeclared_variable1"""
        input = """
main: function void(){
    a: integer  = 3;
    a: integer;
}"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_variable2(self):
        """test_redeclared_variable2"""
        input = """
        main: function void(){
            a,b : integer = 1,2;
            a: float = 3.5;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_variable3(self):
        """test_redeclared_variable3"""
        input = """
main function void(){
    // do something
    a, b: integer = 3,2;
}
main: auto = 3;
"""
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_variable4(self):
        """test_redeclared_variable4"""
        input = """
main: function integer(){
    a: integer = 3;
    b: integer = a + 3;
    return a+b;
}
foo: string = "hello world";
main: float = 3.5;"""

        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_variable5(self):
        """test_redeclared_variable5"""
        input = """
foo: function integer(a:float){}
A: integer;  // error
goo : function float(a: float){}

A: function string(b: string, c: string){
    x : float = 0.5;
    y : integer = foo(x);
}
"""
        expect = "Redeclared Variable: A"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_variable6(self):
        """test_redeclared_variable6"""
        input = """
main: function void();
{

        a,b:integer;
        b = 1;
        a:string;  // error
        b = 0;
}
"""
        expect = "Redeclared Variable: A"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_variable7(self):
        """test_redeclared_variable7"""
        input = """
            main : function void {
                doNothing();
            }
            a: integer = 3;

            main: function integer()    
            {
                a, Main:integer;
                b, MAIN:float;
                Main: integer;  // error
                return 1;
            }
            """
        expect = "Redeclared Variable: Main"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_variable8(self):
        """test_redeclared_variable8"""
        input = """
        main: function void(){
            for (i = 0, i < 10, i + 1){
                doNothing();
                count = 1;
                count = count + 1;
            }
        }
        arrFloat: array[3] of float;
        arrFloat: float;  // error
"""
        expect = "Redeclared Variable: arrFloat"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_function1(self):
        """test_redeclared_function1"""
        input = """
        main: function void(){
            arrInt: array[3] of integer;
            while(true){
                count = arrInt[0] / 3;
                printIntteger(count);
            }
        }

        doNothing: function void(){
            printString("Do nothing bleble!")
        } 

        main: function float(a: integer, b: integer);  // error
        {
            return 1.1;
        }
        
"""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_procedure1(self):
        """test_redeclared_procedure1"""
        input = """

main: function void(){

        a:  integer;
        a:  string;
}
main: function integer(){
    return 13e-2;
}
"""
        expect = "Redeclared Procedure: MAIN"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_undeclared_identifier1(self):
        """test_undeclared_identifier1"""
        input = """
main(): function integer(){

    printInteger(1);
    a =  1998;
    b = 1998;  // error
};

"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_undeclared_identifier2(self):
        """test_undeclared_identifier2"""
        input = """
x:integer;
foo: function float(x: integer){
    return x;
}    

main: function void(x: integer){
    y : float = 3.5;
    x = foo()
    y = x + foo - 1;
};
"""
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclared_function1(self):
        """test_undeclared_function1"""
        input = """
        main: function void(){
            x: integer;
            x = foo(1, 2.2, x , y);
        }
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclared_function2(self):
        """test_undeclared_function2"""
        input = """
boolFuncc: function boolean(x: integer){
    if ( x > 3){return truel;}
    else {return false;}
};

main: function void(){
    if boolFunc(){
        printString("Hello world")
    }
    else {
        printString("Oivkl")
    }
}
"""
        expect = "Undeclared Function: boolFunc"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclared_procedure(self):
        """test_undeclared_procedure"""
        input = """
main: function void () {
    y: integer = 3;
    y = y /3;
    x = x + y;
}
"""
        expect = "Undeclared Procedure: x"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_if_condition_must_be_boolean(self):
        """test_if_condition_must_be_boolean"""
        input = """
        main: function void() {
            x: float = 3.3;
            if (false) {
                if (x) {
                    printString("Parser m sai roi hehe")
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(Id(x),[],[])"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_id_in_for_must_be_integer(self):
        """test_id_in_for_must_be_integer"""
        input = """
        main: function void() {
            x: float;
            y: integer;
            for (y = 0, y < 100, y + 1){
                for (x = 1, x < 10, x + 1){
                    printString("Chay duoc dong nay thi loi roi")
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(x)IntLiteral(0),IntLiteral(10),True,[])"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_expr1_in_for_must_be_integer(self):
        """test_expr1_in_for_must_be_integer"""
        input = """
        main : function void ()  {
            x: integer = 5;
            for (x = 0, x < 10, x + 1){
                for (x = 0.1, x < 10, x+1){
                    printString("Chay duoc dong nay thi loi roi cu")
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(x)FloatLiteral(0.5),IntLiteral(10),True,[])"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_expr2_in_for_must_be_integer(self):
        """test_expr2_in_for_must_be_integer"""
        input = """
        main: function integer() {
            x: integer = 0;
            for (x = 1, x < 10, x + 1){
                for(x = x + 1, x < 10.5, x + 1){
                    printString("Cai nay phai ra loi la do float")
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(x)IntLiteral(0),FloatLiteral(10.5),True,[])"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_id_in_for_must_be_local(self):
        """test_id_in_for_must_be_local"""
        input = """
        x: integer;
        main: function void() {
            y: integer;
            z: float;
            for (y = 0, y < 10, y + 1){
                for (x = 0, x < 10, x + 1){
                    for (y = z, y < x, y + 1){
                        printString("Chay duoc den day thi loi roi ")
                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(y)Id(z),Id(x),True,[])"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_condition_in_while_must_be_boolean(self):
        """test_condition_in_while_must_be_boolean"""
        input = """
        main: function void() {
            while (true) {
                printString("hehe")
                break;
            }
            while (1) {
                printString("Khong biet chay duoc khong")
            }
        }
        """
        expect = "Type Mismatch In Statement: While(IntLiteral(1),[])"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_return_proc_must_no_expr(self):
        """test_return_proc_must_no_expr"""
        input = """
        func1: function void(){
            doNothing();
        }
        main: function void() {
            func1();
            return 0; // error
        }
        """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_return_func_must_expr_with_proper_type1(self):
        """test_return_func_must_expr_with_proper_type1"""
        input = """
        main: function void(){
            ret: integer = 1;
            ret = foo();
            ret = foo1();
        }

        foo1: function integer() { 
            a : integer = 3;
            for(i = 0, i < 10, i + 1){
                a = a + i;
            }
            return a;
        }

        foo: function float(){
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_return_func_must_expr_with_proper_type2(self):
        """test_return_func_must_expr_with_proper_type2"""
        input = """
        main: function void() {
            ret: float;
            b : boolean;
            ret = foo();
            b = foo1();
        }

        foo: function float(){
            return 3 / 5;
        }

        foo1: function boolean(x: integer){
            return x;
        }
        """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_assign_stmt_lhs_must_not_string_type(self):
        """test_assign_stmt_lhs_must_not_string_type"""
        input = """
        main: function void() {
            s: string;
            a: integer;

            a = 1;
            s = "random string";

        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(s),StringLiteral(random string))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_assign_stmt_lhs_must_not_arr_type(self):
        """test_assign_stmt_lhs_must_not_arr_type"""
        input = """
        foo: function array[5] of string{
            arr: array[5] of string;
            return arr;
        }

        main: function void(){
            s: string;
            s = foo();
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(arr),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_assign_stmt_type_lhs_and_rhs_must_be_compa(self):
        """test_assign_stmt_type_lhs_and_rhs_must_be_compa"""
        input = """
        main: function void(){
            a: integer;
            b : float;
            a = b;
            c = a;      // Can float be assigned integer?
            a = c;
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_assign_stmt_type_lhs_and_rhs_must_be_compa2(self):
        """test_assign_stmt_type_lhs_and_rhs_must_be_compa2"""
        input = """
        main: function void()
        {
            a, b: integer;
            c: float;
            str: string;
            a = b;
            c = a;
            str = b;
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_call_stmt_id_must_be_proc(self):
        """test_call_stmt_id_must_be_proc"""
        input = """
        foo: function integer(a: integer)
        {
            return a + 3;
        }

        proc: function void()
        {
            a: integer;
        }
        
        main: function void(){
            proc();
            foo1();
        }
        """
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_call_stmt_param_len_must_be_the_same(self):
        """test_call_stmt_param_len_must_be_the_same"""
        input = """
        proc: function void (a: integer, b: integer)
        {
            printInteger(a + b);
        }

        main: function void(){
            proc(1,0);
            proc(1);
        }
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(proc),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_call_stmt_param_list_must_be_type_comp(self):
        """test_call_stmt_param_list_must_be_type_comp"""
        input = """
        proc: function void(a: float, b: float)
        {
            printFloat(a + b);
        }

        main: function void() {
            proc(1.2, 3.0);
            proc(1.1, "hello man");
        } 
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(proc),[FloatLiteral(1.2),StringLiteral(string)])"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_expr1_arr_must_be_array_type(self):
        """test_expr1_arr_must_be_array_type"""
        input = """
        main: function void()
        {
            a: integer = 0;
            arr: array[4] of integer;
            arr[0] = a;
            a[0] = 1;
        } 
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_expr2_arr_must_be_int_type(self):
        """test_expr2_arr_must_be_int_type"""
        input = """
        main: function void()
        {
            a: array[4] of float;
            a[0] = 1.1;
            a[1/2] = 1.2;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(0.5))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_type_binary_expr1(self):
        """test_type_operand_expr1"""
        input = """
        main: function void()
        {
            b,c : boolean;
            b = (true and false);
            c = true;
            b = (!b) and c;
            c = (b or 0);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,Id(b),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_type_binary_expr2(self):
        """test_type_operand_expr2"""
        input = """
        main: function void()
        {
            a,b : integer;
            c: float;
            d: boolean;

            c = b + 1.0;
            b = 5-1;
            c = b * c;
            d = (a > b) and(b < c);
            a = d + 09;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(d),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_type_binary_expr3(self):
        """test_type_operand_expr3"""
        input = """
        main: function void()
        {
            b: integer;
            c: float;

            b = b div c;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(div,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_type_binary_expr4(self):
        """test_type_operand_expr4"""
        input = """
        foo: function void(s: string){
            printString(s);
        }

        main: function void()
        {
            foo("ss");
            foo("s" * 2);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,StringLiteral(s),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_type_unary_expr1(self):
        """test_type_unary_expr1"""
        input = """
        main: function void()
        {
            s: string;
            a: integer;
            printString(s);
            printString(a);
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(s))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_type_unary_expr2(self):
        """test_type_unary_expr2"""
        input = """
        main: function void()
        {
            b: boolean;
            a: integer;

            a = -a;
            b = b;
            b = -b;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(b))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_type_unary_expr3(self):
        """test_type_unary_expr3"""
        input = """
        main: function void()
        {
            b: boolean;
            a: integer;

            b = (!b);
            a = (!a);
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(not,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_type_unary_expr4(self):
        """test_type_unary_expr4"""
        input = """
        main: function void(){
            b: boolean;
            s: string;

            b = (!b);
            printString((!s))
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(not,Id(S))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_call_expr_id_must_be_func(self):
        """test_call_expr_id_must_be_func"""
        input = """
        foo: function integer(){
            return 1;
        }

        main: function void(){
            a: integer = foo();
            a = foo1();
        }
        """
        expect = "Undeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_call_expr_param_len_must_be_the_same(self):
        """test_call_expr_param_len_must_be_the_same"""
        input = """
        foo: function float()
        {
            a: float = 5.5;
            return a + 1;
        }

        main: function void()
        {
            a: float;
            a = foo();
            a = foo(1,2,3);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_call_expr_param_list_must_be_type_comp(self):
        """test_call_expr_param_list_must_be_type_comp"""
        input = """
        foo: function boolean(a:integer, b:float, c:string)
        {
            return (a*b - a/b) <= ((b / a+1) * 3);
        }
        main: function void(){
            a = foo(1,2,"hello");
            a = foo(1,2,3);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_func_not_return1(self):
        """test_func_not_return1"""
        input = """
        foo: function boolean()
        {
            return 5 * 12 / 123 >= 182.1;
        }
        main: function void()
        {
            a: boolean;
            a = foo();
        }
        foo1: function boolean()
        {

        }
        """
        expect = "Function foo1Not Return "
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_func_not_return2(self):
        """test_func_not_return2"""
        input = """
        main: function void()
        {
            a: boolean;
            a = foo();
            a = foo2();
        }

        foo: function boolean()
        {
            if (true){
                return true;
            }
            else{
                return False;
            }
        }
        """
        expect = "Function foo2Not Return "
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_func_not_return3(self):
        """test_func_not_return3"""
        input = """
        main: function void()
        {
            a : boolean();
            a = foo();
            a = foo3();
        }

        foo: function boolean()
        {
            if (true){
                return false;
            }
            else{
                return true;
            }
        }

        foo3: function boolean()
        {
            if (true){
            
            }
            else{
                return true;
            }
        }
        """
        expect = "Function foo3Not Return "
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_func_not_return4(self):
        """test_func_not_return4"""
        input = """
        main: function void()
        {
            a: boolean;
            a = foo();
            a = foo4();
        }

        foo: function boolean()
        {
            if (true){
                
            }
            else{
                a = 1;
            }
            return (true and false and (!true));
        }
        """
        expect = "Function foo4Not Return "
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_func_not_return5(self):
        """test_func_not_return5"""
        input = """
        main : function void()
        {
            a : boolean();
            a = foo();
            a = foo5();
        }

        foo: function boolean()
        {
            a: integer = 2;
            return a < 4/a;
        }

        foo5: function boolean(a: integer)
        {
            if (a > 5){
                a = 5 * 10
            }
            if ((a< 5) and (a > 10))
            {
                a = a + 1;
            }
        }
        """
        expect = "Function foo5Not Return "
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_func_not_return6(self):
        """test_func_not_return6"""
        input = """
        main: function void()
        {
            a: boolean;
            a = foo();
            a = foo6();
        }

        foo: function boolean()
        {
            a,b : float;
            c: string;
            a = b;
            c = "hello"::"world";
        }

        foo6: function boolean()
        {
            a,b : float;
            c: string;
        }
        """
        expect = "Function foo6Not Return "
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_func_not_return7(self):
        """test_func_not_return7"""
        input = """
        main: function void()
        {
            a,b: boolean;
            a = foo();
            b = foo7();
        }

        foo: function boolean()
        {
            while (foo())
            {
                return true;
            }
            return (a and false);
        }

        foo: function boolean()
        {
            a: float;
            while(true)
            {
                printString("No return");
            }
        }
        """
        expect = "Function foo7Not Return "
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_func_not_return8(self):
        """test_func_not_return8"""
        input = """
        main: function string()
        {
            a : string;
            a = foo() :: " hello world";
            a = goo() :: "";
        }

        foo: function string()
        {
            return "cmm";
        }

        goo: function string()
        {
            for( i = 0, i < 10, i + 1)
            {
                printString("Hehee");
            }
        }
        """
        expect = "Function foo8Not Return "
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_func_not_return9(self):
        """test_func_not_return9"""
        input = """
        main: function void()
        {
            a,b: float();
            a = foo();
            b = goo();
        }

        foo: function float()
        {
            a: integer = 2;
            c = a / 2.0;
            return c + 1.0;
        }

        goo: function float()
        {
            while(true)
            {
                printString("hello world");
            }
        }
        """
        expect = "Function foo9Not Return "
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_func_not_return10(self):
        """test_func_not_return10"""
 
        input = """
        main: function void()
        {
            a,b : boolean;
            a = foo();
            b = goo();
        }

        foo: function boolean()
        {
            a: integer = 0;
            if (true){
                a = readInteger();
                while (true)
                {
                    break;
                }
                return true;
            }
            return (a <= 0);
        }

        goo: function boolean()
        {
            while(true)
            {
                printString("Hello bros");
            } 
        }
        """
        expect = "Function foo10Not Return "
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_func_not_return11(self):
        """test_func_not_return11"""
        input = """
        main: function void()
        {
            a,b : boolean();
            a = foo();
            b = goo();
        }

        foo: function boolean()
        {
            a: integer = -10;
            while(a < 0)
            {
                print("hello world");
                if ((a % 2) == 0)
                {
                    return true;
                }
            }
            return false;
        }

        goo: function boolean()
        {
            a : integer;
            a = 3; 
        }
        """
        expect = "Function foo11Not Return "
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_func_not_return12(self):
        """test_func_not_return12"""
        input = """
        main: function void()
        {
            a: boolean;
            a = foo();
            a = foo12();
        }

        foo: function boolean(b: integer)
        {
            a: integer = 23;
            {
                for(i = 0, i < 10, i + 1)
                {
                    a = 0;
                    if (a != 0)
                    {
                        return false;
                    }
                    else
                    {
                        return (true or false);
                    }
                }
            }
            return true;
        }

        foo12: function boolean()
        {
            a,b : integer = 1, 2;
            {
                while(true)
                {
                    printString("Cannot out");
                    if (1 > 2)
                    {
                        printString("hello man");
                    }
                }
            }
        }
        """
        expect = "Function foo12Not Return "
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_func_not_return13(self):
        """test_func_not_return13"""
        input = """
        main: function void()
        {
            a: boolean = foo();
            a = foo13();
        }

        foo: function boolean(a: integer)
        {
            for(a = a, a <= a, a + 1)
            {
                for (a = a + 1, a <= a + 2, a + 1)
                {
                    while(true)
                    {
                        if ( (foo13() and foo()))
                        {
                            break;
                        }
                        else
                        {
                            continue;
                        }
                    }
                }
                return true;
            }
            return false;
        }

        foo13: function boolean()
        {
            a: integer = 3;
            for (a = a, a <= a, a + 1)
            {
                for (a = a + 1, a <= a + 2, a + 1)
                {
                    while(true)
                    {
                        if( foo13())
                        {
                            break;
                        }
                        else
                        {
                            continue;
                        }
                    }
                }
                return false;
            }
        }
        """
        expect = "Function foo13Not Return "
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_break_not_in_loop1(self):
        """test_break_not_in_loop1"""
        input = """
        foo: function  void()
        {
            a: integer;
            while(true){
                break;
            }
            for ( a= 0 , a < 5, a + 1)
            {
                printString("hello world");
                break;
            }
        }

        main: function integer()
        {
            foo();
            break;
            return 1;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_break_not_in_loop2(self):
        """test_break_not_in_loop2"""
        input = """

        foo: function void()
        {
            a:integer;
            a = 1 - 1e-1;
            while (true){

                if ((1=2) or (a>=0.000000001000000000001)){
                    break;
                }
            }    
        }
                
        main: function void()
        {
            foo();
            if (0.6 > 5/7 ){
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_break_not_in_loop3(self):
        """test_break_not_in_loop3"""
        input = """
        foo: function void()
        {
            a: integer;
            while(true){
                a: boolean;
                a = (a and (a % 2 == 0));
                break;
            }

            for ( a = 0, a < 10, a + 2){
                break;
            }
        }

        main: function void()
        {
            foo();
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_break_not_in_loop4(self):
        """test_break_not_in_loop4"""
        input = """
        foo: function void()
        {
            a : integer = 3;
            while(true)
            {
                if ( a * 7 - 42 > 1){
                    break;
                }
                else{
                    a = a * 2;
                }
            }
        }

        main: function void()
        {
            for (a = 0, a < 10, a + 1)
            {
                if (a % 3 == 0){
                    break;
                }
            }
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,460))

    ############################ 61 - 80 #######################################
    def test_break_not_in_loop5(self):
        """test_break_not_in_loop5"""
        input = """
        main: function void()
        {
            if(-5=0-5/1*3.14/ 3.14)
            {
                while(readInteger() == 1.988){
                    printString("hello man");
                    break;
                }
            }
            else
            {
                a: integer;
                for(a = 0, a < 10, a + 1)
                {
                    a = readInteger();
                    a = a + 2;
                }
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_continue_not_in_loop1(self):
        """test_continue_not_in_loop1"""
        input = """
        foo: function void()
        {
            a: integer = 0;
            while(true){
                a = a + 1;
                if(a < 10){
                    break;
                }
                continue;
            }

            for (a = 0, a < 10, a + 1){
                break;
            }
        }

        main: function void()
        {
            foo();
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_continue_not_in_loop2(self):
        """test_continue_not_in_loop2"""
        input = """
        foo: function void()
        {
            a: integer = 0;
            while(true)
            {
                if((1==2) or (a >= 0.0000001))
                {
                    continue;
                }
            }
            for(a = 0, a < 10, a + 1){
                if( true and !false){
                    continue
                }
            }
        }

        main: function void()
        {
            foo();
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_continue_not_in_loop3(self):
        """test_continue_not_in_loop3"""
        input = """
        foo: function void()
        {
            a: integer = 3;
            while(true)
            {
                if (a > 3){
                    continue;
                }
                else{
                    break;
                }
            }
        }

        main: function void()
        {
            a,b: integer  = 3, 4;
            foo();
            continue;               // Error
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_continue_not_in_loop4(self):
        """test_continue_not_in_loop4"""
        input = """
        foo: function void()
        {   
            a: integer;
            while(true)
            {
                if( 6* 7 -42 < 3){
                    continue;
                }
                else{
                    break;
                }
            }
            for(a = 0, a < 3, a + 1)
            {
                if (a % 2 == 0)
                {
                    continue;
                }
            }
        }

        main: function integer(a: integer)
        {
            foo();
            if (a > 3){
                continue;           // error
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_continue_not_in_loop5(self):
        """test_continue_not_in_loop5"""
        input = """
        Main: function void()
        {
            if(-5=0-5/1*3.14/ 3.14)
            {
                while(true)
                {
                    continue;
                }
            }
            else
            {
                {
                    {
                        for (a = 3, a < 10, a + 1)
                        {
                            printInteger(a);
                        }
                    }
                }
                continue;           // Error
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_continue_not_in_loop6(self):
        """test_continue_not_in_loop6"""
        input = """
        main2: function integer()
        {
            while(true)
            {
                if( a == 6.9)
                {
                    a, b: float;
                    C: array[100] of integer;
                    d: integer;
                    {
                        a = b / 3;
                        b = -b;
                        for(i = C[d], i > 0, i - 1)
                        {
                            break;
                        }
                    }
                }
                continue;
            }
            return 1;
        }

        main1: function float()
        {
            while(true)
            {
                if( a == 6.9)
                {
                    a, b: float;
                    C: array[100] of integer;
                    d: integer;
                    {
                        a = b / 3;
                        b = -b;
                        for(i = C[d], i > 0, i - 1)
                        {
                            break;
                        }
                    }
                }
                break;
            }
            return 1123_123.1;
            
        }

        main: function void()
        {
            a: integer = main2();
            b : float = main1();
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_no_entry_point1(self):
        """test_no_entry_point1"""
        input = """
        a : boolean = true;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_no_entry_point2(self):
        """test_no_entry_point2"""
        input = """
        a: boolean = true;

        foo: function boolean(a: integer)
        {
            return foo(a + 1);
        }

        foo2: function boolean(b: integer)
        {
            return b + 1;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_no_entry_point3(self):
        """test_no_entry_point3"""
        input = """
        a: boolean = true;

        main: function boolean(a: integer)
        {
            return main3(a);
        }

        main3: function boolean(a: integer)
        {
            if ( a > 3)
            {
                return true;
            }
            return false;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_no_entry_point4(self):
        """test_no_entry_point4"""
        input = """
        a: boolean = true;
        main: functiom integer();
        {
            return main_next(a);
        }

        main_next: boolean(a: integer)
        {
            if (a > 3 and a < 8)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_no_entry_point5(self):
        """test_no_entry_point5"""
        input = """
        a: boolean;
        arr: array[1999] of string;

        main: function void(a: araay[100] of string)
        {
            for (item < 0, item < void , item + 1)
            {
                printString(a[item]);
            } 
        }

        main5: function integer(b: array[1999] of string)
        {
            main(function);
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_no_entry_point6(self):
        """test_no_entry_point6"""
        input = """
        main: boolean;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_no_entry_point7(self):
        """test_no_entry_point7"""
        input = """
        main : integer = 3;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_no_entry_point8(self):
        """test_no_entry_point8"""
        input = """
        main1: integer;

        foo: function integer(a: array[1998] of string)
        {
            main: float;
            {
                main: string;
                {
                    main: array[1] of integer;
                    {
                        main: boolean;
                        {
                            return foo(foo8());
                        }
                    }
                }
            }
        }

        foo8: function array[1998] of string()      // Prototype maybe wrong
        {
            main: float;
            {
                main: string;
                {
                    main: array[1] of integer ;
                    {
                        main: boolean();
                        {
                            return foo(foo8());
                        }
                    }
                }
            }
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_no_entry_point9(self):
        """test_no_entry_point9"""
        input = """
        main: function string(a: integer)
        {
            main: string;
            {
                main: boolean;
                {
                    main: array[1998] of string;
                    {
                        return call(main[1]);
                    }
                }
            }
        }

        calling: function string(str: string)
        {
            main: string = str;
            {
                main: array[19] of string;
                {
                    return main[12];
                }
            }
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_func_not_return14(self):
        """test_func_not_return14"""
        input = """
        main: function void()
        {
            i: float = 0.0;
            i = foo();
            i = foo14();    
        }

        foo: function float()
        {
           if (true)
           {
                return 1.1;
           } 
           return 1.2;
        }

        foo14: function float()
        {
            if(false)
            {
                return 3.2;
            }
        }
        """
        expect = "Function foo14Not Return "
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_unreachable_stmt1(self):
        """test_unreachable_stmt1"""
        input = """
        main: function void()
        {
            a: boolean;
            a = foo();
            a = foo1();
        }

        foo: function boolean()
        {
            return true;
        }

        foo1: function boolean()
        {
            return 5 * 123;
            return false;           // Error
        }
        """
        expect = "Unreachable statement: Return(Some(BooleanLiteral(False)))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_unreachable_stmt2(self):
        """test_unreachable_stmt2"""
        input = """
        main: function void()
        {
            a:  boolean; 
            foo();
            foo2();
        }

        foo: function void()
        {
            if (true)
            {
                return;
            }
            else{}
            while(true)
            {
                foo2();
                return ;
            }
        }

        foo2: function void()
        {
            if(true){return;}
            else{return;}

            while(false)
            {
                foo();
                return;
            }
        }
        """
        expect = "Unreachable statement: While(BooleanLiteral(False),[CallStmt(Id(foo),[]),Return(None)])"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_unreachable_stmt3(self):
        """test_unreachable_stmt3"""
        input = """
        main: function void()
        {
            a : boolean;
            foo();
            foo3();
        }

        foo: function boolean()
        {
            if(true){}
            else{return true;}
            {
                a: integer;
                b, c: float = 3.2, 2.2;
                d: boolean = false;
                {
                    a = 1;
                    b = a + c;
                    d = (a == c);
                    return false;
                }
            }
        }

        foo3: function boolean()
        {
            if (true){return false;}
            else{return true;}
            {                                   // Unreachable stmt
                a: integer;
                b, c: float = 3.2, 2.2;
                d: boolean = false;
                {
                    a = 1;
                    b = a + c;
                    d = (a == c);
                    return false;
                }
            }

        }
        """
        expect = "Unreachable statement: With([VarDecl(Id(A),IntType),VarDecl(Id(B),FloatType),VarDecl(Id(C),FloatType),VarDecl(Id(d),BoolType)],[AssignStmt(Id(a),IntLiteral(1)),AssignStmt(Id(b),BinaryOp(+,Id(a),Id(c))),AssignStmt(Id(d),BinaryOp(=,Id(a),Id(c))),Return(Some(BooleanLiteral(False)))])"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_unreachable_stmt4(self):
        """test_unreachable_stmt4"""
        input = """
        main: function void()
        {
            a: boolean = false;
            a = foo();
            a = foo4();
        }

        foo: function boolean()
        {
            a: integer = 3;
            if (true)
            {
                
            }
            else
            {
                
            }
            a = 1;
            {
                return (true and false);
            }
        }

        foo4: function boolean()
        {
            a: integer;
            if (true)
            {
            
            }
            else
            {
                
            }
            a = -1;
            return (true or false);
            {
                return true;
            }
        }
        """
        expect = "Unreachable statement: Return(Some(BooleanLiteral(True)))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_unreachable_stmt5(self):
        """test_unreachable_stmt5"""
        input = """
        main: function void()
        {
            a: boolean = false;
            foo();
            foo5();
        }

        foo: function boolean()
        {
            a: integer = -1;
            if(true)
            {
                a = -a;
                printInteger(a);
                return true;
            }
            else
            {
                a = 0;
                printInteger(a);
            }
            a = 0;
            return false;
        }

        foo5: function boolean()
        {
            a : integer = 3;
            if(true)
            {
                a = a; 
                printInteger(a);
                return true;
            }
            else
            {
                a = 0;
                return false;
            }
            A: float = 3.5;                 // Error
        }
        """
        expect = "Unreachable statement: AssignStmt(Id(A),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_unreachable_stmt6(self):
        """test_unreachable_stmt6"""
        input = """
        main: function void()
        {
            a: boolean;
            a = foo();
            a = foo6();
        }

        foo: function boolean()
        {
            a: integer; 
            {
                a, b: float;
                a = 10.1;
                c: string;
                {
                    a, b : integer;
                    a = 3.5;
                    b = 3;
                    {
                        if(a > 9.0){
                            return true;
                        }   
                    }
                    return false;
                }
            }
        }

        foo6: function boolean()
        {
            a: integer = 3;
            {
                a,b : float = 3.3, 12.2;
                c: string = "hello world"
                {
                    a = b;
                    printString(c);
                    return true;
                }
            }
            {
                printString(c);
                return false;
            }
            a  = 3;
        }
        """
        expect = "Unreachable statement: AssignStmt(Id(A),CallExpr(Id(GETint),[]))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_unreachable_stmt7(self):
        """test_unreachable_stmt7"""
        input = """
        main: function void()
        {
            foo();
            foo7();
        }

        foo: function void()
        {
            a : float = 3.5;
            b: integer = 3;
            c: string = "hello" :: " world";
            {
                while(true)
                {
                    return;
                }
                for (i = 0, i < 10, i+1)
                {
                    i = -(-(i-1));
                }
                return ;
            }
        }

        foo7: function void()
        {
            i : integer = 3;
            while(false){return;}
            return ;

            for(I = 0, I < 10, I + 1)           // Error
            {
                printIntger(I + 1);
                return ;
            }
        }
        """
        expect = "Unreachable statement: For(Id(I)IntLiteral(0),IntLiteral(10),True,[AssignStmt(Id(i),UnaryOp(-,UnaryOp(-,BinaryOp(-,Id(i),IntLiteral(1))))),Return(None)])"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_unreachable_stmt8(self):
        """test_unreachable_stmt8"""
        input = """
        main: function void()
        {
            a: boolean = false;
            {
                a = foo();
                a = foo8();
            }
        }

        foo: function boolean()
        {
            i: integer = 3;
            f: float = 3.3;

            {
                while(foo())
                {
                    i = i =1;
                    f = i / 2;
                    return (true or (i > 3));
                }
            }
            return false;
        }
        
        foo8: function boolean()
        {
            i : integer;
            f: float();

            while(foo())
            {
                i = 3;
                f = i/3.5;
                return (true of false);
            }
            return true;
            f = 0.123;                  // Error
        }
        """
        expect = "Unreachable statement: AssignStmt(Id(f),BinaryOp(/,IntLiteral(0),FloatLiteral(0.0)))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_unreachable_stmt9(self):
        """test_unreachable_stmt9"""
        input = """
        main: function void()
        {
            foo();
            foo9();
        }

        foo: function void()
        {
            i: integer = 3;
            f: float = 3.2;

            if ( i == f){
                for(i = 0, i < 10, i + 1)
                {
                    return;
                }
            }
            else{
                f  = i + 12;
            }
        }

        foo9: function void(){
            i: integer = 3;
            f: float = 3.2;

            {
                while(true)
                {
                    return;
                }
            }
            return ;
            A : integer = 3;
        }
        """
        expect = "Unreachable statement: If(BinaryOp(=,Id(I),Id(F)),[AssignStmt(Id(f),BinaryOp(+,Id(i),IntLiteral(1))),Return(None)],[AssignStmt(Id(f),BinaryOp(+,Id(i),IntLiteral(12)))])"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_unreachable_stmt10(self):
        """test_unreachable_stmt10"""
        input = """
procedure MaIn();
begin
    foo();
    foo10();
end

procedure foo();  // error
var a:integer;
begin
    if True then  //# no return
        begin
            a:=a;
            putintln(a);
            while True do
                return;

            for a:=0 downto a do
                begin
                    return;
                end
        end
    else
        begin
            a:=0;
            putintln(69);
            return;
        end

    main();
end

procedure foo10();
var a:integer;
begin
    if True then
        begin
            a:=a;
            putintln(a);
            while True do
                break;
                
            return;  //# return here
        end
    else
        begin
            a:=0;
            putintln(69);
            return;  //# return here
        end
        
    MAIN();  // error
end
"""
        expect = "Unreachable statement: CallStmt(Id(MAIN),[])"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_unreachable_stmt11(self):
        """test_unreachable_stmt11"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo11();
end

function foo():boolean;
var a:float;
begin
    while a = 1 do  //# no return
        begin
            a:=0;
            if not (a=0) then
                return falSE;
            else
                return false or false;
        end

    a:=a+1.0;
    return foo();  //# return here
end

function foo11():boolean;
var a:float;
begin
    while a = 1 do
        begin
            a:=0;
            if not (a=0) THEn
                begin
                    return falSE;
                    a:=1447;  // error
                end
            else
                return false or false;
        end

    a:=a+1.0;
    return foo();  //# return here
end
"""
        expect = "Unreachable statement: AssignStmt(Id(a),IntLiteral(1447))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_unreachable_stmt12(self):
        """test_unreachable_stmt12"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo12();
end

function foo():boolean;
var a:integer;
    b:float;
begin
    for a:=a to a do  //# no return
        begin
            a:=0;
            if not (a=0) then
                return falSE;
            else
                return false or false;
        end

    b:=a+1.0;
    return foo();  //# return here
end

function foo12():boolean;
var a:integer;
    b:float;
begin
    for a:=a to a do
        begin
            a:=0;
            if not (a=0) then
                return falSE;
            else
                begin
                    return false or false;
                    a:=1998;  // error
                end
        end

    b:=a+1.0;
    return foo();  //# return here
end
"""
        expect = "Unreachable statement: AssignStmt(Id(a),IntLiteral(1998))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_unreachable_stmt13(self):
        """test_unreachable_stmt13"""
        input = """
procedure MaIn();
var a:boolean;
begin
    a:=foo();
    a:=foo13();
end

function foo():boolean;
var a:integer;
    b:float;
begin
    for a:=a to a do  //# no return
        begin
            for a:=a+1 downTO a+2 do
                begin
                    while true and then true do
                        begin
                            if foo13() and foo() then
                                break;
                            else
                                break;
                        end
                end
            return trUE;
        end
    
    b:=a+1.0;
    return FALsE;  //# return here
end

function foo13():boolean;
var a:integer;
    b:float;

begin
    for a:=a to a do
        begin
            for a:=a+1 downTO a+2 do
                begin
                    while true and then true do
                        begin
                            if foo13() and foo() then
                                break;
                            else
                                break;
                            return fALSE or false;  // error
                        end
                end
            return trUE;
        end

    b:=a+1.0;
    return FALsE;  //# return here
end
"""
        expect = "Unreachable statement: Return(Some(BinaryOp(or,BooleanLiteral(False),BooleanLiteral(False))))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_unreachable_stmt14(self):
        """test_unreachable_stmt14"""
        input = """
procedure main();
var i:float;
begin
    i:=foo();
    i:=foo14();
end

function foo():integer;
begin
    if true then
        return - 0;
    return - 0 - 1;  //# return here
end

function foo14():integer;
var bool:float;
begin
    if true then
        return - 0;
    return - 0 - 0;  //# return here
    bool  :=   foo();  // error
end
"""
        expect = "Unreachable statement: AssignStmt(Id(bool),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_unreachable_stmt15(self):
        """test_unreachable_stmt15"""
        input = """
procedure MaIn();
begin
    foo();
    foo15();
end

procedure foo();
var a:integer;
begin
    for a:=a to a do  //# no return
        begin
            with
                b,c,d:float;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                return;
                        end
                end
            putfloatln(0.000) ;
        end

    a := 1;
end

procedure foo15();
var a:integer;
begin
    for a:=a to a do
        begin
            with
                b,c,d:float;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                return;
                        end
                    return;
                end
            putintln(0) ;  // error
        end

    a := 1;
end
"""
        expect = "Unreachable statement: CallStmt(Id(putintln),[IntLiteral(0)])"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_unreachable_stmt16(self):
        """test_unreachable_stmt16"""
        input = """
procedure MaIn();
begin
    foo();
    foo16();
end

procedure foo();
var a:integer;
begin
    for a:=a to a do  //# no return
        begin
            with
                b,c,d:float;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                continue;
                        end
                    else
                        putfloatLN(1.3);
                end
        end

    a := 1;
end

procedure foo16();
var a:integer;
begin
    for a:=a to a do
        begin
            with
                b,c,d:float;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                continue;
                        end
                    else
                        return;
                end
            putfloatLN(1.9) ;  // error
        end

    a := 1;
end
"""
        expect = "Unreachable statement: CallStmt(Id(putfloatLN),[FloatLiteral(1.9)])"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_unreachable_stmt17(self):
        """test_unreachable_stmt17"""
        input = """
procedure MaIn();
begin
    foo();
    foo17();
end

procedure foo();
var a:integer;
begin
    for a:=a to a do  //# no return
        begin
            with
                b,c,d:float;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                continue;
                        end
                    else
                        putfloatLN(1.3);
                end
        end

    a := 1;
end

procedure foo17();
var a:integer;
begin
    for a:=a to a do
        begin
            with
                b,c,d:float;
            do
                begin
                    if b=c+d/a then
                        begin
                            if true and False then
                                break;
                            else
                                return;
                        end
                    else
                        continue;
                    putfloatLN(1.998) ;  // error
                end
        end

    a := 1;
end
"""
        expect = "Unreachable statement: CallStmt(Id(putfloatLN),[FloatLiteral(1.998)])"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_undeclared_identifier3(self):
        """test_undeclared_identifier3"""
        input = """
procedure main();
var x:integer;
begin
    with
        x,y: float;
    do
        X:= 1998;
    X:= y;  // error
end
"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_unreachable_function1(self):
        """test_unreachable_function1"""
        input = """
var a:integer;
    b:boolean;

procedure main();
begin
end

function poor():integer;
begin
    b := fair();
    return -1;
end

function fair():boolean;
begin
    a := poor();
    return false;
end

function rich():string;
begin
    return "falSE";
end
"""
        expect = "Unreachable Function: rich"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_unreachable_function2(self):
        """test_unreachable_function2"""
        input = """
procedure main();
begin
end

function rich(b:boolean):boolean;
begin
    b:=rich(False);
    return false;
end
"""
        expect = "Unreachable Function: rich"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_unreachable_procedure1(self):
        """test_unreachable_procedure1"""
        input = """
procedure main();
begin
end

procedure poor();
begin
    fair();
end

procedure fair();
begin
    poor();
end

procedure rich();
begin
    return;
end
"""
        expect = "Unreachable Procedure: rich"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_unreachable_procedure2(self):
        """test_unreachable_procedure2"""
        input = """
procedure main();
begin
end

procedure poor();
begin
    poor();
end
"""
        expect = "Unreachable Procedure: poor"
        self.assertTrue(TestChecker.test(input,expect,499))

 