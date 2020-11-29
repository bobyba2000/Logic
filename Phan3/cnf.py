from fact import Fact
from rule import Rule 

class CNF:
    def __init__(self, terms = []):
        self.terms = terms
    
    def __repr__(self):
        return "; ".join([term.__repr__() for term in self.terms])

    @staticmethod
    def parse(arg):
        if (isinstance(arg, Rule)):
            terms = []
            for premise in arg.get_premises():
                terms.append(premise.get_negated())
            terms.append(arg.get_conclusion())
            return CNF(terms=terms)
        if (isinstance(arg, Fact)):
            return CNF(terms=[arg])
        