#!/usr/bin/env python3
import re
import argparse

from interpreter import Interpreter


parser = argparse.ArgumentParser()

parser.add_argument('-c', '--code', help='frainfuck code')
parser.add_argument('-f', '--file', help='frainfuck code file')

args = parser.parse_args()

if args.code:
    i = Interpreter(args.code)
elif args.file:
    with open(args.file, 'r') as f:
        code = re.sub(r'\s+', '', f.read())
        i = Interpreter(code)

i.run()
