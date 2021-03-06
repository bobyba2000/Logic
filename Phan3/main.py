from enum import Enum
import argparse
import sys
import re
from fact import Fact
from rule import Rule
from knowledgebase import KnowledgeBase
from resolution import resolution_search
from backwardchaining import BackwardChaining
from fol_fc_ask import fol_fc_ask

class Inferring(Enum):
    FORWARD = 0
    BACKWARD = 1
    RESOLUTION = 2

knowledgeBase = KnowledgeBase()
infertype = -1

parser = argparse.ArgumentParser(description="Simple Prolog Implementation.")
parser.add_argument("files", nargs='*', metavar='file', type=str)
parser.add_argument("--infertype", nargs=1, default=Inferring.BACKWARD.value, type=int, metavar='i', help="{}: forward; {}: backward; {}: resolution".format(Inferring.FORWARD.value, Inferring.BACKWARD.value, Inferring.RESOLUTION.value))

def process(file, isInput = False):
    global knowledgeBase, infertype
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
                            print(fol_fc_ask(knowledgeBase, Fact.parse(cmd)))
                        elif (infertype == Inferring.BACKWARD.value):
                            bc = BackwardChaining(knowledgeBase, Fact.parse(cmd))
                            print(bc.answer())
                        elif (infertype == Inferring.RESOLUTION.value):
                            print(resolution_search(knowledgeBase, Fact.parse(cmd)))
                    else:
                        if (cmd.find(":-") == -1):
                            knowledgeBase.appendFact(Fact.parse(s))
                        else:
                            knowledgeBase.appendRule(Rule.parse(s))
            cmds = []
        else: cmds.append(s)
    if not isInput:
        file.close()

def main():
    global infertype
    args = vars(parser.parse_args(sys.argv[1:]))
    infertype = args['infertype'][0]
    if args['files']:
        for file in args['files']:
            process(open(file))
    process(sys.stdin, isInput = True)

if __name__ == "__main__":
    main()
