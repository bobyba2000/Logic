from enum import Enum
import argparse
import sys
import re
from fact import Fact
from rule import Rule
from knowledgebase import KnowledgeBase
from resolution import resolution

class Inferring(Enum):
    FORWARD = 0
    BACKWARD = 1
    RESOLUTION = 2

knowledgeBase = KnowledgeBase()
infertype = Inferring.BACKWARD.value

parser = argparse.ArgumentParser(description="Simple Prolog Implementation.")
parser.add_argument("files", nargs='*', metavar='file', type=str)
parser.add_argument("--infertype", nargs=1, default=Inferring.BACKWARD, type=int, metavar='i', help="{}: forward; {}: backward; {}: resolution".format(Inferring.FORWARD.value, Inferring.BACKWARD.value, Inferring.RESOLUTION.value))

def query():
    global infertype
    pass

def process(file, isInput = False):
    global knowledgeBase
    cmds = []
    while True:
        if isInput:
            sys.stdout.write('? ' if len(cmds) == 0 else '|    ')
            sys.stdout.flush()
        line = file.readline()
        if line == "": break
        s = re.sub("#.*", "", line[:-1]) # ignore comments
        s = re.sub(" ", "", s) # remove white spaces
        if s == "": continue
        if s[-1] == '.': 
            s=s[:-1]
            cmds.append(s)
        # if punc == '.': print(s)
            for cmd in cmds:
                if cmd == "": continue
                if cmd == 'printKB':
                    print(knowledgeBase)
                elif cmd == 'halt': sys.exit(0)
                else: 
                    if isInput:
                        if (infertype == Inferring.FORWARD.value):
                            continue
                        elif (infertype == Inferring.BACKWARD.value):
                            continue
                        elif (infertype == Inferring.RESOLUTION.value):
                            print(resolution(knowledgeBase, Fact.parse(cmd)))
                    else:
                        if (cmd.find(":-") == -1):
                            knowledgeBase.appendFact(Fact.parse(s))
                        else:
                            knowledgeBase.appendRule(Rule.parse(s))
            cmds = []
        else: cmds.append(s)

def main():
    global infertype
    args = vars(parser.parse_args(sys.argv[1:]))
    infertype = args['infertype']
    if args['files']:
        for file in args['files']:
            process(open(file))
    process(sys.stdin, isInput = True)

if __name__ == "__main__":
    main()