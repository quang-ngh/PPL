import argparse
def gen_test_lexer():
    for i in range(102, 201):
        print(f"""
            def test_lexer_{i}(self):
            \tmy_input = \"\"\"\"\"\"
            \tmy_expected_output = "successful"
            self.assertTrue(TestParser.test(my_input, my_expected_output, {i}))
        """)

def gen_test_parser():
    for i in range(202, 301):
        print(f"""
        def test_parser_{i}(self):
            \tmy_input = \"\"\"\"\"\"
            \tmy_expected_output = "successful"
            \tself.assertTrue(TestParser.test(my_input, my_expected_output, {i}))
        """)

if __name__ == '__main__':
    parser = argparse.ArgumentParser();
    parser.add_argument('--type', type=str)
    args = parser.parse_args()

    if args.type == "parser":
        gen_test_parser()
    else:
        gen_test_lexer()
