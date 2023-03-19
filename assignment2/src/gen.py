def gen_prototype(func, num):
    
    for i in range(1, num+1):
        print(f'def {func}_{i}(self):\n\tinput=""""""\n\texpect="""Program([])"""\n\tself.assertTrue(TestAST.test(input, expect, {300+i+80}))\n')

if __name__ == '__main__':


    gen_prototype("test_random", 20)
