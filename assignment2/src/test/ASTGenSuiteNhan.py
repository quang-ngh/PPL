import unittest
from TestUtils import TestAST
from AST import *



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

    def test_global_var(self):
        """Test simple variable integer"""
        prog = """a: integer;"""
        expect = str(Program([VarDecl("a", typ=IntegerType())]))
        self.assertTrue(TestAST.test(prog, expect, 301))

    def test_multi_global_vars(self):
        """Test multiple variable declaration"""
        prog = """a, b, c, d: integer;"""
        expect = str(
            Program(
                [
                    VarDecl("a", typ=IntegerType()),
                    VarDecl("b", typ=IntegerType()),
                    VarDecl("c", typ=IntegerType()),
                    VarDecl("d", typ=IntegerType()),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 302))

    def test_global_var_with_init(self):
        """Test simple variable declaration with init"""
        prog = """a: integer = 34;"""
        expect = str(Program([VarDecl("a", typ=IntegerType(), init=IntegerLit(34))]))
        self.assertTrue(TestAST.test(prog, expect, 303))

    def test_multi_global_var_with_init(self):
        """Test multiple variable declarations with init"""
        prog = """a, b, c, d: integer = 1, 2, 3, 4;"""
        expect = str(
            Program(
                [
                    VarDecl("a", typ=IntegerType(), init=IntegerLit(1)),
                    VarDecl("b", typ=IntegerType(), init=IntegerLit(2)),
                    VarDecl("c", typ=IntegerType(), init=IntegerLit(3)),
                    VarDecl("d", typ=IntegerType(), init=IntegerLit(4)),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 304), f"Correct: \n{expect}")

    def test_primary_expression_0(self):
        """Test boolean literal"""
        prog = """a: auto = true;"""
        expect = str(
            Program([VarDecl(name="a", typ=AutoType(), init=BooleanLit(True))])
        )
        self.assertTrue(TestAST.test(prog, expect, 305), f"Correct {expect}")

    def test_primary_expression_1(self):
        """Test int literal"""
        prog = """a: integer = 239; b: auto = 0;"""
        expect = str(
            Program(
                [
                    VarDecl(name="a", typ=IntegerType(), init=IntegerLit(239)),
                    VarDecl(name="b", typ=AutoType(), init=IntegerLit(0)),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 306), f"Correct {expect}")

    def test_primary_expression_2(self):
        """Test String literal"""
        prog = """a: string = \"Hello world!\";"""
        expect = str(Program([VarDecl("a", StringType(), StringLit("Hello world!"))]))
        self.assertTrue(TestAST.test(prog, expect, 307), f"Correct {expect}")

    def test_primary_expression_3(self):
        """Test float literal"""
        prog = """a: float = 1.4;
b: float = .3e2;
c: float = 1e43;"""
        expect = str(
            Program(
                [
                    VarDecl("a", FloatType(), FloatLit(1.4)),
                    VarDecl("b", FloatType(), FloatLit(0.3e2)),
                    VarDecl("c", FloatType(), FloatLit(1e43)),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 308), f"Correct {expect}")

    def test_primary_expression_4(self):
        """Test array literal"""
        prog = "a: array[3] of integer = {1, 2, 3};"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        ArrayType([3], IntegerType()),
                        ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 309), f"Correct {expect}")

    def test_primary_expression_5(self):
        """Test bracketed expression"""
        prog = "a: auto = (1);"
        expect = str(Program([VarDecl("a", AutoType(), IntegerLit(1))]))
        self.assertTrue(TestAST.test(prog, expect, 310), f"Correct {expect}")

    def test_primary_expression_6(self):
        """Test array access expression"""
        prog = "a: auto = arr[12];"
        expect = str(
            Program([VarDecl("a", AutoType(), ArrayCell("arr", [IntegerLit(12)]))])
        )
        self.assertTrue(TestAST.test(prog, expect, 311), f"Correct {expect}")

    def test_primary_expression_7(self):
        """Test array access expression multi-dimensional"""
        prog = "a: auto = arr[12, foo(), 48, barz, 192, 192 * 2];"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        ArrayCell(
                            "arr",
                            [
                                IntegerLit(12),
                                FuncCall("foo", []),
                                IntegerLit(48),
                                Id("barz"),
                                IntegerLit(192),
                                BinExpr("*", IntegerLit(192), IntegerLit(2)),
                            ],
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 312), f"Correct {expect}")

    def test_unary_expression(self):
        """Test Negation and Not operator"""
        prog = """a: integer = -1;
b: boolean = !true;"""
        expect = str(
            Program(
                [
                    VarDecl("a", typ=IntegerType(), init=UnExpr("-", IntegerLit(1))),
                    VarDecl("b", typ=BooleanType(), init=UnExpr("!", BooleanLit(True))),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 313), f"Correct: \n{expect}")

    def test_multiplicative_expression_0(self):
        """Test muliplication operator"""
        prog = """a: integer = -2 * -4;"""
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        typ=IntegerType(),
                        init=BinExpr(
                            "*", UnExpr("-", IntegerLit(2)), UnExpr("-", IntegerLit(4))
                        ),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 314), f"Correct: \n{expect}")

    def test_multiplicative_expression_1(self):
        """Test division operator"""
        prog = """b: float = 42 / 4.0;"""
        expect = str(
            Program(
                [
                    VarDecl(
                        name="b",
                        typ=FloatType(),
                        init=BinExpr(op="/", left=IntegerLit(42), right=FloatLit(4.0)),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, str(expect), 315), f"Correct: \n{expect}")

    def test_multiplicative_expression_2(self):
        """Test mod operator"""
        prog = """c: float = 87 % foo;"""
        expect = str(
            Program(
                [
                    VarDecl(
                        name="c",
                        typ=FloatType(),
                        init=BinExpr(op="%", left=IntegerLit(87), right=Id("foo")),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, str(expect), 316), f"Correct: \n{expect}")

    def test_multiplicative_expression_3(self):
        """Test Multiple multiplicative operators with unary"""
        prog = """d: float = 95 * -24 % 42 / foo;"""
        expect = str(
            Program(
                [
                    VarDecl(
                        name="d",
                        typ=FloatType(),
                        init=BinExpr(
                            op="/",
                            left=BinExpr(
                                op="%",
                                left=BinExpr(
                                    op="*",
                                    left=IntegerLit(95),
                                    right=UnExpr("-", IntegerLit(24)),
                                ),
                                right=IntegerLit(42),
                            ),
                            right=Id("foo"),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 317), f"Correct: {expect}")

    def test_additive_expression_0(self):
        """Test Addition opreator"""
        prog = "a: integer = 1 + 2;"
        expect = str(
            Program(
                [
                    VarDecl(
                        name="a",
                        typ=IntegerType(),
                        init=BinExpr(op="+", left=IntegerLit(1), right=IntegerLit(2)),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 318), f"Correct: {expect}")

    def test_additive_expression_1(self):
        """Test Subtraction operator"""
        prog = "a: integer = 1 - 2;"
        expect = str(
            Program(
                [
                    VarDecl(
                        name="a",
                        typ=IntegerType(),
                        init=BinExpr(op="-", left=IntegerLit(1), right=IntegerLit(2)),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 319), f"Correct: {expect}")

    def test_additive_expression_2(self):
        """Test Addition with Negation operator"""
        prog = "a: integer = 1 + - 2;"
        expect = str(
            Program(
                [
                    VarDecl(
                        name="a",
                        typ=IntegerType(),
                        init=BinExpr(
                            op="+",
                            left=IntegerLit(1),
                            right=UnExpr(op="-", val=IntegerLit(2)),
                        ),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 320), f"Correct {expect}")

    def test_additive_expression_3(self):
        """Test multiple additive and unary operator"""
        prog = "a: integer = 1 + 423 - - 348 + - 34;"
        expect = str(
            Program(
                [
                    VarDecl(
                        name="a",
                        typ=IntegerType(),
                        init=BinExpr(
                            op="+",
                            left=BinExpr(
                                op="-",
                                left=BinExpr(
                                    op="+", left=IntegerLit(1), right=IntegerLit(423)
                                ),
                                right=UnExpr("-", IntegerLit(348)),
                            ),
                            right=UnExpr("-", IntegerLit(34)),
                        ),
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 321), f"Correct {expect}")

    def test_additive_multiplicative_expression_0(self):
        """Test multiplicative and additive precedence"""
        prog = "a: integer = 1 + 43 * -43 - 439 / 43 + 43 % 42;"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        IntegerType(),
                        init=BinExpr(
                            op="+",
                            left=BinExpr(
                                op="-",
                                left=BinExpr(
                                    op="+",
                                    left=IntegerLit(1),
                                    right=BinExpr(
                                        op="*",
                                        left=IntegerLit(43),
                                        right=UnExpr(op="-", val=IntegerLit(43)),
                                    ),
                                ),
                                right=BinExpr(
                                    op="/", left=IntegerLit(439), right=IntegerLit(43)
                                ),
                            ),
                            right=BinExpr(
                                op="%", left=IntegerLit(43), right=IntegerLit(42)
                            ),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 322), f"Correct: {expect}")

    def test_logical_expression_0(self):
        """Test && operator"""
        prog = "a: integer = foo() && bar;"
        expect = str(
            Program(
                [
                    VarDecl(
                        name="a",
                        typ=IntegerType(),
                        init=BinExpr(
                            op="&&", left=FuncCall("foo", []), right=Id("bar")
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 323), f"Correct {expect}")

    def test_logical_expression_1(self):
        """Test || operator"""
        prog = "a: integer = foo() || bar;"
        expect = str(
            Program(
                [
                    VarDecl(
                        name="a",
                        typ=IntegerType(),
                        init=BinExpr(
                            op="||", left=FuncCall("foo", []), right=Id("bar")
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 324), f"Correct {expect}")

    def test_logical_expression_2(self):
        """Test multiple logical expression"""
        prog = "a: integer = foo() || bar && barz && foobar() || barzr;"
        expect = str(
            Program(
                [
                    VarDecl(
                        name="a",
                        typ=IntegerType(),
                        init=BinExpr(
                            op="||",
                            left=BinExpr(
                                op="&&",
                                left=BinExpr(
                                    op="&&",
                                    left=BinExpr(
                                        op="||",
                                        left=FuncCall("foo", []),
                                        right=Id("bar"),
                                    ),
                                    right=Id("barz"),
                                ),
                                right=FuncCall("foobar", []),
                            ),
                            right=Id("barzr"),
                        ),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 325), f"Correct {expect}")

    def test_comparative_expression_0(self):
        """Test equal"""
        prog = "a: auto = foo() == bar;"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        init=BinExpr("==", FuncCall("foo", []), Id("bar")),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 326), f"Correct {expect}")

    def test_comparative_expression_1(self):
        """Test !="""
        prog = "a: auto = foo() != bar;"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        init=BinExpr("!=", FuncCall("foo", []), Id("bar")),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 327), f"Correct {expect}")

    def test_comparative_expression_2(self):
        """Test <"""
        prog = "a: auto = foo() < bar;"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        init=BinExpr("<", FuncCall("foo", []), Id("bar")),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 328), f"Correct {expect}")

    def test_comparative_expression_3(self):
        """Test <="""
        prog = "a: auto = foo() <= bar;"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        init=BinExpr("<=", FuncCall("foo", []), Id("bar")),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 329), f"Correct {expect}")

    def test_comparative_expression_4(self):
        """Test >"""
        prog = "a: auto = foo() > bar;"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        init=BinExpr(">", FuncCall("foo", []), Id("bar")),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 330), f"Correct {expect}")

    def test_comparative_expression_5(self):
        """Test >="""
        prog = "a: auto = foo() >= bar;"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        init=BinExpr(">=", FuncCall("foo", []), Id("bar")),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 331), f"Correct {expect}")

    def test_comparative_expression_6(self):
        """Test complex_comparative_expression"""
        prog = "a: auto = foo(barz) + 3 == 438 * bar;"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        BinExpr(
                            "==",
                            BinExpr("+", FuncCall("foo", [Id("barz")]), IntegerLit(3)),
                            BinExpr("*", IntegerLit(438), Id("bar")),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 332), f"Correct {expect}")

    def test_string_concatenation_expression_0(self):
        "Test ::"
        prog = 'a: auto = "Hello" :: bar;'
        expect = str(
            Program(
                [VarDecl("a", AutoType(), BinExpr("::", StringLit("Hello"), Id("bar")))]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 333), f"Correct {expect}")

    def test_string_concatenation_expression_1(self):
        "Test ::"
        prog = 'a: auto = ("Hello" :: bar) :: foo();'
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        BinExpr(
                            "::",
                            BinExpr("::", StringLit("Hello"), Id("bar")),
                            FuncCall("foo", []),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 334), f"Correct {expect}")

    def test_call_statement_0(self):
        """Test call statement"""
        prog = """main: function void() {
callSomething();
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt([CallStmt("callSomething", [])]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 335), f"Correct {expect}")

    def test_call_statement_1(self):
        """Test call statement with parameters"""
        prog = """main: function void() {
callSomething(1, "String", foo());
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                CallStmt(
                                    "callSomething",
                                    [
                                        IntegerLit(1),
                                        StringLit("String"),
                                        FuncCall("foo", []),
                                    ],
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 336), f"Correct {expect}")

    def test_if_statement_0(self):
        """Test if statement without else"""
        prog = """main: function void() {
    if (foo == barz)
        turn();
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                IfStmt(
                                    BinExpr("==", Id("foo"), Id("barz")),
                                    CallStmt("turn", []),
                                    None,
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 337), f"Correct {expect}")

    def test_if_statement_1(self):
        """Test if statement with else"""
        prog = """main: function void() {
    if (foo == barz)
        turn();
    else
        dontTurn();
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                IfStmt(
                                    BinExpr("==", Id("foo"), Id("barz")),
                                    CallStmt("turn", []),
                                    CallStmt("dontTurn", []),
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 338), f"Correct {expect}")

    def test_if_statement_2(self):
        """test nested if statement"""
        prog = """main: function void() {
    if (foo == barz)
        if (barz == bar)
            call();
        else
            dontCall();
    else
        callAPI();
}"""

        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                IfStmt(
                                    BinExpr("==", Id("foo"), Id("barz")),
                                    IfStmt(
                                        BinExpr("==", Id("barz"), Id("bar")),
                                        CallStmt("call", []),
                                        CallStmt("dontCall", []),
                                    ),
                                    CallStmt("callAPI", []),
                                )
                            ]
                        ),
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 339), f"Correct {expect}")

    def test_for_statement_0(self):
        """test for statement"""
        prog = """main: function void() {
    for (a = foo(), a == 3, a + 1)
        hello();
}"""

        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                ForStmt(
                                    AssignStmt(Id("a"), FuncCall("foo", [])),
                                    BinExpr("==", Id("a"), IntegerLit(3)),
                                    BinExpr("+", Id("a"), IntegerLit(1)),
                                    CallStmt("hello", []),
                                )
                            ]
                        ),
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 340), f"Correct {expect}")

    def test_for_statement_1(self):
        """Test for statement with block statement body"""
        prog = """main: function void() {
    for (a = 3 + 34, a == 43, a - 3) {
        hello();
        tomcruise = true;
    }
}"""

        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                ForStmt(
                                    AssignStmt(
                                        Id("a"),
                                        BinExpr("+", IntegerLit(3), IntegerLit(34)),
                                    ),
                                    BinExpr("==", Id("a"), IntegerLit(43)),
                                    BinExpr("-", Id("a"), IntegerLit(3)),
                                    BlockStmt(
                                        [
                                            CallStmt("hello", []),
                                            AssignStmt(
                                                Id("tomcruise"), BooleanLit(True)
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 341), f"Correct {expect}")

    def test_while_statement_0(self):
        """Test while statement"""
        prog = """main: function void() {
    while (a == 3) {
        hello();
        tomcruise = true;
    }
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                WhileStmt(
                                    BinExpr("==", Id("a"), IntegerLit(3)),
                                    BlockStmt(
                                        [
                                            CallStmt("hello", []),
                                            AssignStmt(
                                                Id("tomcruise"), BooleanLit(True)
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 342), f"Correct {expect}")

    def test_while_statement_1(self):
        """Test empty_while statement"""
        prog = """main: function void() {
    a: integer = 4;
    while (a == 3) {}
    a = 3;
}
"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                VarDecl("a", IntegerType(), IntegerLit(4)),
                                WhileStmt(
                                    BinExpr("==", Id("a"), IntegerLit(3)), BlockStmt([])
                                ),
                                AssignStmt(Id("a"), IntegerLit(3)),
                            ]
                        ),
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 343), f"Correct {expect}")

    def test_do_while_statement_0(self):
        """Test do-while statement"""
        prog = """main: function void() {
    do {} while (true);
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [DoWhileStmt(cond=BooleanLit(True), stmt=BlockStmt([]))]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 344), f"Correct {expect}")

    def test_return_statement_0(self):
        """Test empty return"""
        prog = """
returnVoid: function void() {
    return;
}

main: function void() {
    returnVoid();
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "returnVoid", VoidType(), [], None, BlockStmt([ReturnStmt()])
                    ),
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt([CallStmt("returnVoid", [])]),
                    ),
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 345), f"Correct {expect}")

    def test_return_statement_1(self):
        """Test return value integer"""
        prog = """returnInt: function integer () {
    return 123;
}
main: function void () {
    returnInt();
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "returnInt",
                        IntegerType(),
                        [],
                        None,
                        BlockStmt([ReturnStmt(IntegerLit(123))]),
                    ),
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt([CallStmt("returnInt", [])]),
                    ),
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 346), f"Correct {expect}")

    def test_return_statement_2(self):
        """Test return value float"""
        prog = """returnFloat: function float () {
    return 123.e3;
}
main: function void () {
    returnFloat();
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "returnFloat",
                        FloatType(),
                        [],
                        None,
                        BlockStmt([ReturnStmt(FloatLit(123.0e3))]),
                    ),
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt([CallStmt("returnFloat", [])]),
                    ),
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 347), f"Correct {expect}")

    def test_return_statement_3(self):
        """Test return value string"""
        prog = """returnSomething: function string () {
    return "Hello world";
}
main: function void () {
    returnSomething();
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "returnSomething",
                        StringType(),
                        [],
                        None,
                        BlockStmt([ReturnStmt(StringLit("Hello world"))]),
                    ),
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt([CallStmt("returnSomething", [])]),
                    ),
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 348), f"Correct {expect}")

    def test_return_statement_4(self):
        """Test return value boolean"""
        prog = """returnSomething: function boolean () {
    return true;
}
main: function void () {
    returnSomething();
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "returnSomething",
                        BooleanType(),
                        [],
                        None,
                        BlockStmt([ReturnStmt(BooleanLit(True))]),
                    ),
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt([CallStmt("returnSomething", [])]),
                    ),
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 349), f"Correct {expect}")

    def test_return_statement_5(self):
        """Test return value float"""
        prog = """returnSomething: function array [3, 3] of integer () {
    return {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
}
main: function void () {
    returnSomething();
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "returnSomething",
                        ArrayType([3, 3], IntegerType()),
                        [],
                        None,
                        BlockStmt(
                            [
                                ReturnStmt(
                                    ArrayLit(
                                        [
                                            ArrayLit(
                                                [
                                                    IntegerLit(1),
                                                    IntegerLit(2),
                                                    IntegerLit(3),
                                                ]
                                            ),
                                            ArrayLit(
                                                [
                                                    IntegerLit(4),
                                                    IntegerLit(5),
                                                    IntegerLit(6),
                                                ]
                                            ),
                                            ArrayLit(
                                                [
                                                    IntegerLit(7),
                                                    IntegerLit(8),
                                                    IntegerLit(9),
                                                ]
                                            ),
                                        ]
                                    )
                                )
                            ]
                        ),
                    ),
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt([CallStmt("returnSomething", [])]),
                    ),
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 350), f"Correct {expect}")

    def test_return_statement_6(self):
        """Test return value float"""
        prog = """returnSomething: function auto () {
    return foo(temp);
}
main: function void () {
    returnSomething();
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "returnSomething",
                        AutoType(),
                        [],
                        None,
                        BlockStmt([ReturnStmt(FuncCall("foo", [Id("temp")]))]),
                    ),
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt([CallStmt("returnSomething", [])]),
                    ),
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 351), f"Correct {expect}")

    def test_continue_statement(self):
        """Test continue statement"""
        prog = """main: function void() {
while(true)
    continue;
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt([WhileStmt(BooleanLit(True), ContinueStmt())]),
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 352), f"Correct {expect}")

    def test_break_statement(self):
        """Test break statement"""
        prog = """main: function void() {
while(true)
    break;
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt([WhileStmt(BooleanLit(True), BreakStmt())]),
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 353), f"Correct {expect}")

    def test_function_with_parameter_0(self):
        """Test function with parameter"""
        prog = """foo: function void(foobar: integer) {
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "foo",
                        VoidType(),
                        [ParamDecl(name="foobar", typ=IntegerType())],
                        None,
                        BlockStmt([]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 354), f"Correct {expect}")

    def test_function_with_parameters_1(self):
        """Test function with multiple parameter"""
        prog = """foo: function void(foobar: integer, barz: string) {
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "foo",
                        VoidType(),
                        [
                            ParamDecl(name="foobar", typ=IntegerType()),
                            ParamDecl(name="barz", typ=StringType()),
                        ],
                        None,
                        BlockStmt([]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 355), f"Correct {expect}")

    def test_function_with_parameters_2(self):
        """Test function with out parameter"""
        prog = """foo: function void(out foobar: integer) {
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "foo",
                        VoidType(),
                        [
                            ParamDecl(name="foobar", typ=IntegerType(), out=True),
                        ],
                        None,
                        BlockStmt([]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 356), f"Correct {expect}")

    def test_function_with_parameters_3(self):
        """Test function with multiple out parameter"""
        prog = """foo: function void(out foobar: integer,
                                     bar: string,
                                     out arr: array [3, 2] of integer) {}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "foo",
                        VoidType(),
                        [
                            ParamDecl(name="foobar", typ=IntegerType(), out=True),
                            ParamDecl(name="bar", typ=StringType(), out=False),
                            ParamDecl(
                                name="arr",
                                typ=ArrayType([3, 2], IntegerType()),
                                out=True,
                            ),
                        ],
                        None,
                        BlockStmt([]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 357), f"Correct {expect}")

    def test_function_with_parameters_4(self):
        """Test function with inherit parameter"""
        prog = """foo: function void(inherit foobar: integer) {
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "foo",
                        VoidType(),
                        [
                            ParamDecl(
                                name="foobar",
                                typ=IntegerType(),
                                out=False,
                                inherit=True,
                            ),
                        ],
                        None,
                        BlockStmt([]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 358), f"Correct {expect}")

    def test_function_with_parameters_5(self):
        """Test function with inherit parameter"""
        prog = """foo: function void(inherit foobar: integer, fooz: string, inherit job_2: float) {
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "foo",
                        VoidType(),
                        [
                            ParamDecl(
                                name="foobar",
                                typ=IntegerType(),
                                out=False,
                                inherit=True,
                            ),
                            ParamDecl(
                                name="fooz",
                                typ=StringType(),
                                out=False,
                                inherit=False,
                            ),
                            ParamDecl(
                                name="job_2",
                                typ=FloatType(),
                                out=False,
                                inherit=True,
                            ),
                        ],
                        None,
                        BlockStmt([]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 359), f"Correct {expect}")

    def test_function_with_parameters_6(self):
        """Test function with out inherit parameter"""
        prog = """foo: function void(
            inherit out foobar: integer,
            out fooz: string,
            inherit job_2: float,
            job_3: string) {}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "foo",
                        VoidType(),
                        [
                            ParamDecl(
                                name="foobar",
                                typ=IntegerType(),
                                out=True,
                                inherit=True,
                            ),
                            ParamDecl(
                                name="fooz",
                                typ=StringType(),
                                out=True,
                                inherit=False,
                            ),
                            ParamDecl(
                                name="job_2",
                                typ=FloatType(),
                                out=False,
                                inherit=True,
                            ),
                            ParamDecl(
                                name="job_3",
                                typ=StringType(),
                                out=False,
                                inherit=False,
                            ),
                        ],
                        None,
                        BlockStmt([]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 360), f"Correct {expect}")

    def test_inherited_function_0(self):
        """Test function that is inherit another function"""
        prog = """foo: function void() inherit bar {
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "foo",
                        VoidType(),
                        [],
                        "bar",
                        BlockStmt([]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 361), f"Correct {expect}")

    def test_inherited_function_1(self):
        """Test function that is inherit another function"""
        prog = """foo: function void(a: integer) inherit bar {
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "foo",
                        VoidType(),
                        [ParamDecl("a", IntegerType())],
                        "bar",
                        BlockStmt([]),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 362), f"Correct {expect}")

    def test_complex_program(self):
        "Test a complex program"
        prog = """
main: function void() {
    p: integer = 43;
    i: integer = 39;
    d: integer = 43;
    pid_arr: auto = getPid();
    p = pid_arr[0];
    i = pid_arr[1];
    d = pid_arr[2];
    if ((p > 3) && (i < 200)) {
        print("Pid value is ok");
        if (d > 300)
            print("D value is skewed, please fix");

    } else {
        print("Do not run!");
    }
    for (i = 0, i < 3, i + 1) {
        if (pid_arr[i] % 2 == 3)
            break;
        if (pid_arr[i + 1] % 3 == 1) {
            continue;
        }
        pid_arr[i] = 0;
    }

    while (true) {
        doPidLoop(p, i, d);
    }
}
getPid: function array [3] of integer() {
    return {32, 22, 12};
}
"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        name="main",
                        return_type=VoidType(),
                        params=[],
                        inherit=None,
                        body=BlockStmt(
                            [
                                VarDecl("p", IntegerType(), IntegerLit(43)),
                                VarDecl("i", IntegerType(), IntegerLit(39)),
                                VarDecl("d", IntegerType(), IntegerLit(43)),
                                VarDecl("pid_arr", AutoType(), FuncCall("getPid", [])),
                                AssignStmt(
                                    Id("p"), ArrayCell("pid_arr", [IntegerLit(0)])
                                ),
                                AssignStmt(
                                    Id("i"), ArrayCell("pid_arr", [IntegerLit(1)])
                                ),
                                AssignStmt(
                                    Id("d"), ArrayCell("pid_arr", [IntegerLit(2)])
                                ),
                                IfStmt(
                                    BinExpr(
                                        "&&",
                                        BinExpr(">", Id("p"), IntegerLit(3)),
                                        BinExpr("<", Id("i"), IntegerLit(200)),
                                    ),
                                    BlockStmt(
                                        [
                                            CallStmt(
                                                "print", [StringLit("Pid value is ok")]
                                            ),
                                            IfStmt(
                                                BinExpr(">", Id("d"), IntegerLit(300)),
                                                CallStmt(
                                                    "print",
                                                    [
                                                        StringLit(
                                                            "D value is skewed, please fix"
                                                        )
                                                    ],
                                                ),
                                            ),
                                        ]
                                    ),
                                    BlockStmt(
                                        [CallStmt("print", [StringLit("Do not run!")])]
                                    ),
                                ),
                                ForStmt(
                                    AssignStmt(Id("i"), IntegerLit(0)),
                                    BinExpr("<", Id("i"), IntegerLit(3)),
                                    BinExpr("+", Id("i"), IntegerLit(1)),
                                    BlockStmt(
                                        [
                                            IfStmt(
                                                BinExpr(
                                                    "==",
                                                    BinExpr(
                                                        "%",
                                                        ArrayCell(
                                                            "pid_arr",
                                                            [Id("i")],
                                                        ),
                                                        IntegerLit(2),
                                                    ),
                                                    IntegerLit(3),
                                                ),
                                                BreakStmt(),
                                            ),
                                            IfStmt(
                                                BinExpr(
                                                    "==",
                                                    BinExpr(
                                                        "%",
                                                        ArrayCell(
                                                            "pid_arr",
                                                            [
                                                                BinExpr(
                                                                    "+",
                                                                    Id("i"),
                                                                    IntegerLit(1),
                                                                )
                                                            ],
                                                        ),
                                                        IntegerLit(3),
                                                    ),
                                                    IntegerLit(1),
                                                ),
                                                BlockStmt(
                                                    [
                                                        ContinueStmt(),
                                                    ]
                                                ),
                                            ),
                                            AssignStmt(
                                                ArrayCell("pid_arr", [Id("i")]),
                                                IntegerLit(0),
                                            ),
                                        ]
                                    ),
                                ),
                                WhileStmt(
                                    BooleanLit(True),
                                    BlockStmt(
                                        [
                                            CallStmt(
                                                "doPidLoop", [Id("p"), Id("i"), Id("d")]
                                            )
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    FuncDecl(
                        "getPid",
                        ArrayType([3], IntegerType()),
                        [],
                        None,
                        BlockStmt(
                            [
                                ReturnStmt(
                                    ArrayLit(
                                        [IntegerLit(32), IntegerLit(22), IntegerLit(12)]
                                    )
                                )
                            ]
                        ),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 363), f"Correct\n{expect}")

    def test_false_boolean(self):
        """Test if generate correct boolean literal"""
        prog = """a: boolean = false;
main: function void() {
}"""
        expect = str(
            Program(
                [
                    VarDecl("a", BooleanType(), BooleanLit(False)),
                    FuncDecl("main", VoidType(), [], None, BlockStmt([])),
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 364), f"Correct\n{expect}")

    def test_nested_array(self):
        """Test nested array"""
        prog = """a: array[5] of string = {{1,2,3,4,5},{1,2,3,4,5,6}};"""

        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        ArrayType([5], StringType()),
                        ArrayLit(
                            [
                                ArrayLit(
                                    [
                                        IntegerLit(1),
                                        IntegerLit(2),
                                        IntegerLit(3),
                                        IntegerLit(4),
                                        IntegerLit(5),
                                    ]
                                ),
                                ArrayLit(
                                    [
                                        IntegerLit(1),
                                        IntegerLit(2),
                                        IntegerLit(3),
                                        IntegerLit(4),
                                        IntegerLit(5),
                                        IntegerLit(6),
                                    ]
                                ),
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 365), f"Correct\n{expect}")

    def test_test_in_MT22(self):
        prog = """
test_test_in_MT22: function void() {
    prog: auto = "Some string input for program";

    expect: auto = "Some output string for AST";

    if (runTest(prog, expect) != true) {
        print("Test failed");
    } else
        print("Test successfully ok");
}
"""

        expect = str(
            Program(
                [
                    FuncDecl(
                        "test_test_in_MT22",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                VarDecl(
                                    "prog",
                                    AutoType(),
                                    StringLit("Some string input for program"),
                                ),
                                VarDecl(
                                    "expect",
                                    AutoType(),
                                    StringLit("Some output string for AST"),
                                ),
                                IfStmt(
                                    BinExpr(
                                        "!=",
                                        FuncCall("runTest", [Id("prog"), Id("expect")]),
                                        BooleanLit(True),
                                    ),
                                    BlockStmt(
                                        [
                                            CallStmt(
                                                "print", [StringLit("Test failed")]
                                            ),
                                        ]
                                    ),
                                    CallStmt(
                                        "print", [StringLit("Test successfully ok")]
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 366), f"Correct\n{expect}")

    def test_if_comment_is_excluded(self):
        prog = """
// a: integer = true;
b: boolean = false;
main: function void() {
}
/* main2: function void() {
}*/
"""
        expect = str(
            Program(
                [
                    VarDecl("b", BooleanType(), BooleanLit(False)),
                    FuncDecl("main", VoidType(), [], None, BlockStmt([])),
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 367), f"Correct\n{expect}")

    def test_nested_expression(self):
        prog = """
a: auto = foo() + bar[2 + 4] * 3 - -2 * 4 / 3;
"""
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        BinExpr(
                            "-",
                            BinExpr(
                                "+",
                                FuncCall("foo", []),
                                BinExpr(
                                    "*",
                                    ArrayCell(
                                        "bar",
                                        [BinExpr("+", IntegerLit(2), IntegerLit(4))],
                                    ),
                                    IntegerLit(3),
                                ),
                            ),
                            BinExpr(
                                "/",
                                BinExpr("*", UnExpr("-", IntegerLit(2)), IntegerLit(4)),
                                IntegerLit(3),
                            ),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 368), f"Correct\n{expect}")

    def test_huge_program(self):
        prog = """
main: function void() {
    srand(time(NULL));
    random: integer = rand();
    printInteger(random);
}"""

        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                CallStmt("srand", [FuncCall("time", [Id("NULL")])]),
                                VarDecl("random", IntegerType(), FuncCall("rand", [])),
                                CallStmt("printInteger", [Id("random")]),
                            ]
                        ),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 369), f"Correct\n{expect}")

    def test_random_stuff(self):
        prog = """
a, b, c, d, e, f, g, h, j, k,  l,  m,  n,  o,  p,  q,  r,  s,  t,  u,  v,  w,  x,  y,  z: auto = 
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25;
"""
        expect = str(
            Program(
                [
                    VarDecl("a", AutoType(), IntegerLit(1)),
                    VarDecl("b", AutoType(), IntegerLit(2)),
                    VarDecl("c", AutoType(), IntegerLit(3)),
                    VarDecl("d", AutoType(), IntegerLit(4)),
                    VarDecl("e", AutoType(), IntegerLit(5)),
                    VarDecl("f", AutoType(), IntegerLit(6)),
                    VarDecl("g", AutoType(), IntegerLit(7)),
                    VarDecl("h", AutoType(), IntegerLit(8)),
                    VarDecl("j", AutoType(), IntegerLit(9)),
                    VarDecl("k", AutoType(), IntegerLit(10)),
                    VarDecl("l", AutoType(), IntegerLit(11)),
                    VarDecl("m", AutoType(), IntegerLit(12)),
                    VarDecl("n", AutoType(), IntegerLit(13)),
                    VarDecl("o", AutoType(), IntegerLit(14)),
                    VarDecl("p", AutoType(), IntegerLit(15)),
                    VarDecl("q", AutoType(), IntegerLit(16)),
                    VarDecl("r", AutoType(), IntegerLit(17)),
                    VarDecl("s", AutoType(), IntegerLit(18)),
                    VarDecl("t", AutoType(), IntegerLit(19)),
                    VarDecl("u", AutoType(), IntegerLit(20)),
                    VarDecl("v", AutoType(), IntegerLit(21)),
                    VarDecl("w", AutoType(), IntegerLit(22)),
                    VarDecl("x", AutoType(), IntegerLit(23)),
                    VarDecl("y", AutoType(), IntegerLit(24)),
                    VarDecl("z", AutoType(), IntegerLit(25)),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 370), f"Correct\n{expect}")
