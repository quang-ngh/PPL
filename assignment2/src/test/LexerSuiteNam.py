import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # def test_lowercase_identifier(self):
    def test(self):
        testcases = [
            # Test INTLIT
            (#1
            """0""",
            """0,<EOF>"""
            ),
            (#2
            """123""",
            """123,<EOF>"""
            ),
            (#3
            """12_34""",
            """1234,<EOF>"""
            ),
            (#4
            """0_123""",
            """0,_123,<EOF>"""
            ),
            (#5
            """123_23_33""",
            """1232333,<EOF>"""
            ),
            # Test FLOATLIT
            (#6
            """7e-10""",
            """7e-10,<EOF>"""
            ),
            (#7
            """12_3.98""",
            """123.98,<EOF>"""
            ),
            (#8
            """12_3.98_""",
            """123.98,_,<EOF>"""
            ),
            (#9
            """.987e-1""",
            """.987e-1,<EOF>"""
            ),
            (#10
            """12_3e+10""",
            """123e+10,<EOF>"""
            ),
            (#11
            """1.8_5e+1_0""",
            """1.8,_5e,+,10,<EOF>"""
            ),
            # Test IDENTIFIER
            (#12
            """aBcD""",
            """aBcD,<EOF>"""
            ),
            (#13
            """_""",
            """_,<EOF>"""
            ),
            (#14
            """_a_c""",
            """_a_c,<EOF>"""
            ),
            (#15
            """___""",
            """___,<EOF>"""
            ),
            (#16
            """0_1_2""",
            """0,_1_2,<EOF>"""
            ),
            # Test STRINGLIT
            (#17
            """ "He asked me: \\\"Where is John?\\\"" """,
            """He asked me: \\\"Where is John?\\\",<EOF>"""
            ),
            (#18
            """ "He asked me \: " """,
            """Illegal Escape In String: He asked me \:"""
            ),
            (#19
            """ "He asked me!\n" """,
            """Unclosed String: He asked me!\n\n"""
            ),
            (#20
            """ "He asked me: \\" """,
            """Unclosed String: He asked me: \\" """
            ),
            (#21
            """ "Hello, World!\\n..." """,
            """Hello, World!\\n...,<EOF>"""
            ),
            (#22
            """ "Double quote test " " """,
            """Double quote test ,Unclosed String:  """
            ),
            # Test COMMENT_CSTYLE
            (#23
            """ // Comment
            a: integer = 5 """,
            """a,:,integer,=,5,<EOF>"""
            ),
            (#24
            """a: integer = 5 //This code assign a = 5""",
            """a,:,integer,=,5,/,/,This,code,assign,a,=,5,<EOF>"""
            ),
            (#25
            """a: integer = 5 //This code assign a = 5
            """,
            """a,:,integer,=,5,<EOF>"""
            ),
            (#26
            """sum: function integer (a: integer, b: integer)
            //This function received 2 args a: int and b: int
            {
                return a + b;
            }""",
            """sum,:,function,integer,(,a,:,integer,,,b,:,integer,),{,return,a,+,b,;,},<EOF>"""
            ),
            (#27
            """a: float = // Float a
            3.0;
            b: float = //  Float b 5.0;
            """,
            """a,:,float,=,3.0,;,b,:,float,=,<EOF>"""
            ),
            # Test COMMENT_CPPSTYLE
            (#28
            """/* Comment */""",
            """<EOF>"""
            ),
            (#29
            """a: integer = 5 /* Declare a = 5 */""",
            """a,:,integer,=,5,<EOF>"""
            ),
            (#30
            """/* a:integer; /*""",
            """Unterminated Comment: /* a:integer; /*"""
            ),
            (#31
            """*/a:integer;/*""",
            """*,/,a,:,integer,;,Unterminated Comment: /*"""
            ),
            (#32
            """a:integer;""",
            """a,:,integer,;,<EOF>"""
            ),
            (#33
            """/* // */a:integer;""",
            """a,:,integer,;,<EOF>"""
            ),
            (#34
            """a:integer;
            // This is C Comment
            /* This is C++ Comment */
            # This is Python comment""",
            """a,:,integer,;,Error Token #"""
            ),
            (#35
            """/* Unterminated comment""",
            """Unterminated Comment: /* Unterminated comment"""
            ),
            # Test ALL
            (#36
            """\"Hello \\a \"""",
            """Illegal Escape In String: Hello \\a"""
            ),
            (#37
            """\c""",
            """\,c,<EOF>"""
            ),
            (#38
            """/* Terminated comment /**/""",
            """<EOF>"""
            ),
            (#39
            """
            main: function void()
            {
                {
                    a = 5;
                    {
                        b = 6; 
                        {
                            c = 7;
                        }
                    }
                }
            }
            """,
            """main,:,function,void,(,),{,{,a,=,5,;,{,b,=,6,;,{,c,=,7,;,},},},},<EOF>"""
            ),
            (#40
            """
            main: function void()
            {
                a[0, 2] = b[1, 2, 3];
            }
            """,
            """main,:,function,void,(,),{,a,[,0,,,2,],=,b,[,1,,,2,,,3,],;,},<EOF>"""
            ),
            (#41
            """
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
            """,
            """main,:,function,void,(,),{,{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,float,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},},<EOF>"""
            ),
            (#42
            """foo(2 + x, 4.0 / y);""",
            """foo,(,2,+,x,,,4.0,/,y,),;,<EOF>"""
            ),
            (#43
            """a_mess = 1+2*3-4/5*6+7-_[12, 0 + x]*b-0.32E-1;""",
            """a_mess,=,1,+,2,*,3,-,4,/,5,*,6,+,7,-,_,[,12,,,0,+,x,],*,b,-,0.32E-1,;,<EOF>"""
            ),
            (#44
            """
            fact: function integer(x: integer)
            {
                res: integer = 1;
                for (i = 1, i <= x, i + 1) res = res * i;
                return res;
            }
            """,
            """fact,:,function,integer,(,x,:,integer,),{,res,:,integer,=,1,;,for,(,i,=,1,,,i,<=,x,,,i,+,1,),res,=,res,*,i,;,return,res,;,},<EOF>"""
            ),
            (#45
            """printString("Please input x: ");""",
            """printString,(,Please input x: ,),;,<EOF>"""
            ),
            (#46
            """a:onteger;""",
            """a,:,onteger,;,<EOF>"""
            ),
            (#47
            """for (i = 3; i < 5; i + 1)
            {
                x = x + i;
            }
            """,
            """for,(,i,=,3,;,i,<,5,;,i,+,1,),{,x,=,x,+,i,;,},<EOF>"""
            ),
            (#48
            """sum: function integer (a: integer, b: integer)
            {
                return a + b;
            }
            """,
            """sum,:,function,integer,(,a,:,integer,,,b,:,integer,),{,return,a,+,b,;,},<EOF>"""
            ),
            (#49
            """,""",
            """,,<EOF>"""
            ),
            (#50
            """.""",
            """.,<EOF>"""
            ),
            (#51
            """@""",
            """Error Token @"""
            ),
            (#52
            """a: integer @b""",
            """a,:,integer,Error Token @"""
            ),
            (#53
            """main: function void() {}""", 
            """main,:,function,void,(,),{,},<EOF>"""
            ),
            (#54
            """writeln Writeln WRITELN""",
            """writeln,Writeln,WRITELN,<EOF>"""
            ),
            (#55
            """abc""",
            """abc,<EOF>"""
            ),
            (#56
            """Integer Integer""",
            """Integer,Integer,<EOF>"""
            ),
            (#57
            """
            /* Guess the result /**//***///*
            """,
            """<EOF>"""
            ),
            (#58
            """
            if (len(s) <= 1) return true;
            """,
            """if,(,len,(,s,),<=,1,),return,true,;,<EOF>"""
            ),
            (#59
            """
            if (s[0] == s[-1]) return isPalindrome(slice(s, 1, -2));
            else return false;
            """,
            """if,(,s,[,0,],==,s,[,-,1,],),return,isPalindrome,(,slice,(,s,,,1,,,-,2,),),;,else,return,false,;,<EOF>"""
            ),
            (#60
            """
            print(isPalindrome("abba"));
            """,
            """print,(,isPalindrome,(,abba,),),;,<EOF>"""
            ),
            (#61
            """
            res: float = A[0];
            """,
            """res,:,float,=,A,[,0,],;,<EOF>"""
            ),
            (#62
            """
            for (i = 1, i < len(A), i + 1)
            {
                if (res < A[i]) res = A[i];
            }
            """,
            """for,(,i,=,1,,,i,<,len,(,A,),,,i,+,1,),{,if,(,res,<,A,[,i,],),res,=,A,[,i,],;,},<EOF>"""
            ),
            (#63
            """
            A: array[4] of float;
            """,
            """A,:,array,[,4,],of,float,;,<EOF>"""
            ),
            (#64
            """
            printInteger(max(A));
            """,
            """printInteger,(,max,(,A,),),;,<EOF>"""
            ),
            (#65
            """
            inc: function void(out x: integer)
            // Increase input by 1
            {
                x = x + 1;
            }
            """,
            """inc,:,function,void,(,out,x,:,integer,),{,x,=,x,+,1,;,},<EOF>"""
            ),
            (#66
            """
            {
                {
                    {
                        my_static_var = a - 1;
                    }
                }
            }
            """,
            """{,{,{,my_static_var,=,a,-,1,;,},},},<EOF>"""
            ),
            (#67
            """
            main: function void(narg, agrvs)
            {
                while x < 3
                {
                    x = x + 1;
                }
            }
            """,
            """main,:,function,void,(,narg,,,agrvs,),{,while,x,<,3,{,x,=,x,+,1,;,},},<EOF>"""
            ),
            (#68
            """
            main: function void()
            {
                if (x > 3) x = 3;
                else x = 4;
                else x = 5;
            }
            """,
            """main,:,function,void,(,),{,if,(,x,>,3,),x,=,3,;,else,x,=,4,;,else,x,=,5,;,},<EOF>"""
            ),
            (#69
            """
            for (i = 1; i < n; i + 1)
            {
                continue;
            }
            """,
            """for,(,i,=,1,;,i,<,n,;,i,+,1,),{,continue,;,},<EOF>"""
            ),
            (#70
            """
            return x = 1;
            """,
            """return,x,=,1,;,<EOF>"""
            ),
            (#71
            """
            foo(x = 1, x);
            """,
            """foo,(,x,=,1,,,x,),;,<EOF>"""
            ),
            (#72
            """
            1__2
            """,
            """1,__2,<EOF>"""
            ),
            (#73
            """
            foo(x) - 1;
            """,
            """foo,(,x,),-,1,;,<EOF>"""
            ),
            (#74
            """
            sum: function integer(a: integer, b: integer)
            {
                return a + b;
            }
            """,
            """sum,:,function,integer,(,a,:,integer,,,b,:,integer,),{,return,a,+,b,;,},<EOF>"""
            ),
            (#75
            """
            foo(3) = x + 2;
            """,
            """foo,(,3,),=,x,+,2,;,<EOF>"""
            ),
            (#76
            """
            a = (2 && 3 || 4);
            """,
            """a,=,(,2,&&,3,||,4,),;,<EOF>"""
            ),
            (#77
            """
            a: void = 3;
            """,
            """a,:,void,=,3,;,<EOF>"""
            ),
            (#78
            """
            while(a != b && b != c && c != d) 
            {
                doSomething();
            }
            """,
            """while,(,a,!=,b,&&,b,!=,c,&&,c,!=,d,),{,doSomething,(,),;,},<EOF>"""
            ),
            (#79
            """
            x: integer* = 0Xffffffff;
            """,
            """x,:,integer,*,=,0,Xffffffff,;,<EOF>"""
            ),
            (#80
            """
            x += 1;
            """,
            """x,+,=,1,;,<EOF>"""
            ),
            (#81
            """
            foo(3) = x + 2;
            """,
            """foo,(,3,),=,x,+,2,;,<EOF>"""
            ),
            (#82
            """
            a: integer(5);
            """,
            """a,:,integer,(,5,),;,<EOF>"""
            ),
            (#83
            """
            continue();
            """,
            """continue,(,),;,<EOF>"""
            ),
            (#84
            """
            do  
            {
                a = a - 1;
            }
            while (a != 10) 
            {
                a = a * 2;
            }
            """,
            """do,{,a,=,a,-,1,;,},while,(,a,!=,10,),{,a,=,a,*,2,;,},<EOF>"""
            ),
            (#85
            """
            x: integer, y: string;
            """,
            """x,:,integer,,,y,:,string,;,<EOF>"""
            ),
            (#86
            """
            x := 3;
            """,
            """x,:,=,3,;,<EOF>"""
            ),
            (#87
            """
            inherit: integer = 1;
            """,
            """inherit,:,integer,=,1,;,<EOF>"""
            ),
            (#88
            """
            a(3, 2) = 3;
            """,
            """a,(,3,,,2,),=,3,;,<EOF>"""
            ),
            (#89
            """
            a = .12;
            """,
            """a,=,.,12,;,<EOF>"""
            ),
            (#90
            """
            my_ip = 192.168.0.0;
            """,
            """my_ip,=,192.168,.,0.0,;,<EOF>"""
            ),
            (#91
            """
            fact: function integer(out a: integer) {}
            """,
            """fact,:,function,integer,(,out,a,:,integer,),{,},<EOF>"""
            ),
            (#92
            """
            main: function void(arg: integer = 5)
            {
                
            }
            """,
            """main,:,function,void,(,arg,:,integer,=,5,),{,},<EOF>"""
            ),
            (#93
            """
            return sum(sum());
            """,
            """return,sum,(,sum,(,),),;,<EOF>"""
            ),
            (#94
            """
            return "A string";
            """,
            """return,A string,;,<EOF>"""
            ),
            (#95
            """
            main: void function() {}
            """,
            """main,:,void,function,(,),{,},<EOF>"""
            ),
            (#96
            """
            if (i == 10) printInteger(i);
            """,
            """if,(,i,==,10,),printInteger,(,i,),;,<EOF>"""
            ),
            (#97
            """
            if (i > x)
            {
                printString("i > x");
            }
            else
            {
                printString("x >= i");
            }
            """,
            """if,(,i,>,x,),{,printString,(,i > x,),;,},else,{,printString,(,x >= i,),;,},<EOF>"""
            ),
            (#98
            """
            if (x < b) if (x > a) print("\\\"Hello World!\\\""); else print("Hello"); else print("No Hello!");
            """,
            """if,(,x,<,b,),if,(,x,>,a,),print,(,\\\"Hello World!\\\",),;,else,print,(,Hello,),;,else,print,(,No Hello!,),;,<EOF>"""
            ),
            (#99
            """
            for (i = 0, i < 10, i + 1) sum = sum + i;
            """,
            """for,(,i,=,0,,,i,<,10,,,i,+,1,),sum,=,sum,+,i,;,<EOF>"""
            ),
            (#100
            """
            while (foo(x) >= 10) x = (x + 2) / 3;
            """,
            """while,(,foo,(,x,),>=,10,),x,=,(,x,+,2,),/,3,;,<EOF>"""
            )
        ]
        test_id = 100
        for test, expected in testcases:
            self.assertTrue(TestLexer.test(test, expected, test_id))
            test_id += 1
