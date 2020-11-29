from enum import Enum
import argparse
import sys
import re
from fact import Fact
from rule import Rule

class Inferring(Enum):
    FORWARD = 0
    BACKWARD = 1
    RESOLUTION = 2

rules = list()
infertype = Inferring.BACKWARD.value

parser = argparse.ArgumentParser(description="Simple Prolog Implementation.")
parser.add_argument("files", nargs='?', metavar='file')
parser.add_argument("--infertype", nargs=1, default=Inferring.BACKWARD, type=int, metavar='i', help="{}: forward; {}: backward; {}: resolution".format(Inferring.FORWARD.value, Inferring.BACKWARD.value, Inferring.RESOLUTION.value))

def query():
    global infertype
    pass

def process(file, isInput = False):
    global rules
    while True:
        if isInput:
            sys.stdout.write('? ')
            sys.stdout.flush()
        line = file.readline()
        if line == "": break
        s = re.sub("#.*", "", line[:-1]) # ignore comments
        s = re.sub(" ", "", s) # remove white spaces
        if s == "": continue
        if s[-1] == '.': s=s[:-1]
        # if punc == '.': print(s)
        if s == 'quit': sys.exit(0)
        else: 
            if isInput:
                query()
            else:
                rules.append(Rule.parse(s))

def main():
    global infertype
    args = vars(parser.parse_args(sys.argv[1:]))
    print(args)
    infertype = args['infertype']
    if args['files']:
        for file in args['files']:
            process(file)
    process(sys.stdin, isInput = True)

if __name__ == "__main__":
    main()