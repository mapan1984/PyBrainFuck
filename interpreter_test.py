import io
import sys
import unittest

from interpreter import Interpreter


class TestInterpreter(unittest.TestCase):

    def setUp(self):
        self.old_out = sys.stdout

    def test_A(self):
        sys.stdout = io.StringIO('')
        code = '+++++[>+++++++++++++<-]>.'
        Interpreter(code).run()
        self.assertEqual(sys.stdout.getvalue(), 'A')

    def test_hello(self):
        sys.stdout = io.StringIO('')
        code = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
        Interpreter(code).run()
        self.assertEqual(sys.stdout.getvalue(), 'Hello World!\n')

    def test_nested_loop(self):
        sys.stdout = io.StringIO('')
        code = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
        Interpreter(code).run()
        self.assertEqual(sys.stdout.getvalue(), 'Hello World!\n')

    def tearDown(self):
        sys.stdout = self.old_out


if __name__ == '__main__':
    unittest.main()
