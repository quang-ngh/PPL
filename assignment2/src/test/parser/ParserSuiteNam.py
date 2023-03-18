import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test(self):
        testcases = [
            (#1
            """
            a: integer;
            """,
            """successful"""
            ),
            (#2
            """
            a: integer = 5;
            """,
            """successful"""
            ),
            (#3
            """
            a: integer = 1.2e-1;
            """,
            """successful"""
            ),
            (#4
            """
            a: string;
            """,
            """successful"""
            ),
            (#5
            """
            a: string = 0.2;
            """,
            """successful"""
            ),
            (#6
            """
            a: string = \"Hello World!\";
            """,
            """successful"""
            ),
            (#7
            """
            a, b: integer;
            """,
            """successful"""
            ),
            (#8
            """
            a, b, sum: integer = 1, 2, 3;
            """,
            """successful"""
            ),
            (#9
            """
            a, b, sum: integer = 1, "string", 3.0;
            """,
            """successful"""
            ),
            (#10
            """
            _: boolean = true;
            """,
            """successful"""
            ),
            (#11
            """
            main: function void () {}""",
            """successful"""
            ),
            (#12
            """
            main: function void (argv: auto) {}""",
            """successful"""
            ),
            (#13
            """
            main: function void (argv: auto) 
            {
                a: integer = 5;
            }
            """,
            """successful"""
            ),
            (#14
            """
            sum: function integer (a: integer, c: float) {}
            """,
            """successful"""
            ),
            (#15
            """
            sum: function integer (a: integer, c: float) 
            {
                return a + b;
            }
            """,
            """successful"""
            ),
            (#16
            """
            sum: function integer (a: integer, b: float) 
            {
                a = a + 1;
                return a + b;
            }
            """,
            """successful"""
            ),
            (#17
            """
            main: function void()
            {
                while (x < 3)
                {
                    a = a + x;
                    x = x + 1;
                }
            }
            """,
            """successful"""
            ),
            (#18
            """
            main: function void()
            {
                while (!x)
                {
                    a = a / 2;
                    x = a % 2 == 0;
                }
            }
            """,
            """successful"""
            ),
            (#19
            """
            main: function void()
            {
                x: float = 0.2;
                while (foo(x) >= 10) x = (x + 2) / 3;
                printInteger(foo(x));
            }
            """,
            """successful"""
            ),
            (#20
            """
            main: function void()
            {
                for (i = 0, i < 10, i + 1)
                {
                    sum = sum + i;
                }
            }
            """,
            """successful"""
            ),
            (#21
            """
            main: function void()
            {
                for (i = 0, i < 10, i + 1) sum = sum + i;
            }
            """,
            """successful"""
            ),
            (#22
            """
            main: function void()
            {
                do
                {
                    i = i + 1;
                } 
                while (i < 10);
            }
            """,
            """successful"""
            ),
            (#23
            """
            main: function void()
            {
                do
                {
                    writeInteger(i + 1);
                } 
                while (i != a + b);
            }
            """,
            """successful"""
            ),
            (#24
            """
            main: function void()
            {
                break;
            }
            """,
            """successful"""
            ),
            (#25
            """
            main: function void()
            {
                if (i == 10) printInteger(i);
            }
            """,
            """successful"""
            ),
            (#26
            """
            main: function void()
            {
                if (i == 10)
                {
                    writeInteger(i + 5);
                }
            }
            """,
            """successful"""
            ),
            (#27
            """
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
            """,
            """successful"""
            ),
            (#28
            """
            main: function void()
            {
                if (i > x) printString("i > x");
                else
                {
                    printString("x >= i");
                    x = x - 1;
                }
            }
            """,
            """successful"""
            ),
            (#29
            """
            main: function void()
            {
                if (x < b) if (x > a) print("\\\"Hello World!\\\""); else print("Hello"); else print("No Hello!");
            }
            """,
            """successful"""
            ),
            (#30
            """
            main: function void()
            {
                while (x < 3)
                {
                    x = x + 1;
                    if (x % 2 == 0) break;
                }
            }
            """,
            """successful"""
            ),
            (#31
            """
            main: function void()
            {
                for (i = true, i != false, true)
                {
                    if (!i) break;
                }
            }
            """,
            """successful"""
            ),
            (#32
            """
            main: function void()
            {
                while (x < 3)
                {
                    x = x + 1;
                    if (x % 2 == 0) continue;
                }
            }
            """,
            """successful"""
            ),
            (#33
            """
            main: function void()
            {
                for (i = true, i != false, true)
                {
                    if (!i) continue;
                }
            }
            """,
            """successful"""
            ),
            (#34
            """
            main: function void()
            {
                sum(a + b, b / c);
            }
            """,
            """successful"""
            ),
            (#35
            """
            main: function void()
            {
                if (a % b == 0) a = reduce(a, b); 
                else b = reduce(b, a);
            }
            """,
            """successful"""
            ),
            (#36
            """
            main: function void()
            {
                a: array[10] of float;
            }
            """,
            """successful"""
            ),
            (#37
            """
            main: function void()
            {
                a = {1, 2, 3, 4};
            }
            """,
            """successful"""
            ),
            (#38
            """
            main: function void()
            {
                a, b, c: array[10, 10] of string;
            }
            """,
            """successful"""
            ),
            (#39
            """
            main: function void()
            {
                {}
            }
            """,
            """successful"""
            ),
            (#40
            """
            main: function void()
            {
                {
                    a = a - 1;
                }
            }
            """,
            """successful"""
            ),
            (#41
            """
            main: function void()
            {
                {{{}}}
            }
            """,
            """successful"""
            ),
            (#42
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
            """successful"""
            ),
            (#43
            """
            main: function void()
            {
                a[0, 2] = b[1, 2, 3];
            }
            """,
            """successful"""
            ),
            (#44
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
            """successful"""
            ),
            (#45
            """
            main: function void()
            {
                foo(2 + x, 4.0 / y);
            }
            """,
            """successful"""
            ),
            (#46
            """
            main: function void()
            {
                a_mess = 1+2*3-4/5*6+7-_[12, 0 + x]*b-0.32E-1;
            }
            """,
            """successful"""
            ),
            (#47
            """
            // 300 bai code thieu nhi
            // Bai 1: Viet ham tinh giai thua
        
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
            
            """,
            """successful"""
            ),
            (#48
            """
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
            """,
            """successful"""
            ),
            (#49
            """
            // 300 bai code thieu nhi
            /* Bai 3: Tim max trong mang */
            ///////////////////////////////

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
            """,
            """successful"""
            ),
            (#50
            """
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
            """,
            """successful"""
            ),
            (#51
            """
            a: onteger;
            """,
            """Error on line 2 col 15: onteger"""
            ),
            (#52
            """
            a, b, sum: integer = 1, 2, 3
            """,
            """Error on line 3 col 12: <EOF>"""
            ),
            (#53
            """
            a, b: float 1.0;
            """,
            """Error on line 2 col 24: 1.0"""
            ),
            (#54
            """
            a, b: float = 1.0, -2.0, 3.4;
            """,
            """Error on line 2 col 35: ,"""
            ),
            (#55
            """
            0a, 0b: integer = 1, 2, 3;
            """,
            """Error on line 2 col 12: 0"""
            ),
            (#56
            """
            a, b: float = 3, integer = 4;
            """,
            """Error on line 2 col 29: integer"""
            ),
            (#57
            """
            a = integer: 5;
            """,
            """Error on line 2 col 14: ="""
            ),
            (#58
            """
            a: float 3;
            """,
            """Error on line 2 col 21: 3"""
            ),
            (#59
            """
            a - b: float = 3;
            """,
            """Error on line 2 col 14: -"""
            ),
            (#60
            """
            a, b: array of boolean;
            """,
            """Error on line 2 col 24: of"""
            ),
            (#61
            """
            main = func void() {}
            """,
            """Error on line 2 col 17: ="""
            ),
            (#62
            """
            main: function void();
            """,
            """Error on line 2 col 33: ;"""
            ),
            (#63
            """
            a = b + 2;
            main: function void() {}
            """,
            """Error on line 2 col 14: ="""
            ),
            (#64
            """
            main: function void()
            {
                while x < 3
                {
                    x = x + 1;
                }
            }
            """,
            """Error on line 4 col 22: x"""
            ),
            (#65
            """
            main: function void(narg, agrvs)
            {
                while x < 3
                {
                    x = x + 1;
                }
            }
            """,
            """Error on line 2 col 36: ,"""
            ),
            (#66
            """
            main: function void()
            {
                while (x = 3)
                {
                    x = x + 1;
                }
            }
            """,
            """Error on line 4 col 25: ="""
            ),
            (#67
            """
            main: function void()
            {
                while (x = 3) x - 1;
            }
            """,
            """Error on line 4 col 25: ="""
            ),
            (#68
            """
            main: function void()
            {
                do x = x - 2;
                while (x > 1);
            }
            """,
            """Error on line 4 col 19: x"""
            ),
            (#69
            """
            main: function void()
            {
                if x > 3
                {
                    x = 3;
                }
            }
            """,
            """Error on line 4 col 19: x"""
            ),
            (#70
            """
            main: function void()
            {
                if (x > 3) x = 3;
                else x = 4;
                else x = 5;
            }
            """,
            """Error on line 6 col 16: else"""
            ),
            (#71
            """
            main: function void()
            {
                for (integer i = 1, i < n, i + 1)
                {
                    continue;
                }
            }
            """,
            """Error on line 4 col 21: integer"""
            ),
            (#72
            """
            main: function void()
            {
                for (i = 1; i < n; i + 1)
                {
                    continue;
                }
            }
            """,
            """Error on line 4 col 26: ;"""
            ),
            (#73
            """
            main: function void()
            {
                for (i = 1, i < n, i = i + 1)
                {
                    continue;
                }
            }
            """,
            """Error on line 4 col 37: ="""
            ),
            (#74
            """
            main: function void()
            {
                return x = 1;
            }
            """,
            """Error on line 4 col 25: ="""
            ),
            (#75
            """
            main: function void()
            {
                {
                    {
                        {
                        
                    }
                }
            }
            """,
            """Error on line 11 col 12: <EOF>"""
            ),
            (#76
            """
            main: function void()
            {
                foo(x = 1, x)
            }
            """,
            """Error on line 4 col 22: ="""
            ),
            (#77
            """
            main: function void()
            {
                foo();
                1();
            }
            """,
            """Error on line 5 col 16: 1"""
            ),
            (#78
            """
            main: function void()
            {
                foo(x) - 1;
            }
            """,
            """Error on line 4 col 23: -"""
            ),
            (#79
            """
            main: function void()
            {
                sum: function integer(a: integer, b: integer)
                {
                    return a + b;
                }
            }
            """,
            """Error on line 4 col 21: function"""
            ),
            (#80
            """
            main: function void()
            {
                foo(3) = x + 2;
            }
            """,
            """Error on line 4 col 23: ="""
            ),
            (#81
            """
            main: function void()
            {
                a = (&& 3);
            }
            """,
            """Error on line 4 col 21: &&"""
            ),
            (#82
            """
            main: function void()
            {
                a: void = 3;
            }
            """,
            """Error on line 4 col 19: void"""
            ),
            (#83
            """
            main: function void() 
            {
                while(a != b && b != c && c != d) 
                {
                    doSomething();
                }
            }
            """,
            """Error on line 4 col 34: !="""
            ),
            (#84
            """
            main: function void()
            {
                x: integer* = 0Xffffffff;
            }
            """,
            """Error on line 4 col 26: *"""
            ),
            (#85
            """
            main: function void()
            {
                x += 1;
            }
            """,
            """Error on line 4 col 18: +"""
            ),
            (#86
            """
            foo(3, 4);
            main: function void()
            {
                foo(3) = x + 2;
            }
            """,
            """Error on line 2 col 15: ("""
            ),
            (#87
            """
            main: function void()
            {
                a: integer(5);
            }
            """,
            """Error on line 4 col 26: ("""
            ),
            (#88
            """
            main: function void()
            {
                continue();
            }
            """,
            """Error on line 4 col 24: ("""
            ),
            (#89
            """
            main: function void()
            {
                a: integer;
            }
            break;
            """,
            """Error on line 6 col 12: break"""
            ),
            (#90
            """
            main: function void() 
            {
                do  
                {
                    a = a - 1;
                }
                while (a != 10) 
                {
                    a = a * 2;
                }
            }
            """,
            """Error on line 9 col 16: {"""
            ),
            (#91
            """
            main: function void()
            {
                x: integer, y: string;
            }
            """,
            """Error on line 4 col 26: ,"""
            ),
            (#92
            """
            main: function void()
            {
                x := 3;
            }
            """,
            """Error on line 4 col 19: ="""
            ),
            (#93
            """
            main: function void()
            {
                inherit: integer = 1;
            }
            """,
            """Error on line 4 col 16: inherit"""
            ),
            (#94
            """
            main: function void()
            {
                a(3, 2) = 3;
            }
            """,
            """Error on line 4 col 24: ="""
            ),
            (#95
            """
            main: function void()
            {
                a = .12;
            }
            """,
            """Error on line 4 col 20: ."""
            ),
            (#96
            """
            main: function void()
            {
                my_ip = 192.168.0.0;
            }
            """,
            """Error on line 4 col 31: ."""
            ),
            (#97
            """
            fact: function integer(out a: integer) {
            """,
            """Error on line 3 col 12: <EOF>"""
            ),
            (#98
            """
            main: function void(arg: integer = 5)
            {
                
            }
            """,
            """Error on line 2 col 45: ="""
            ),
            (#99
            """
            main: function void() inherit sum
            {
                return sum(sum());
            }
            sum = function void()
            {
                return "Nothing";
            }
            """,
            """Error on line 6 col 16: ="""
            ),
            (#100
            """
            main: void function()
            {
                while (x < 3)
                {
                
                }
            }
            """,
            """Error on line 2 col 18: void"""
            )
        ]
        test_id = 200
        for test, expected in testcases:
            self.assertTrue(TestParser.test(test, expected, test_id))
            test_id += 1
