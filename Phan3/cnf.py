from fact import Fact
from rule import Rule 

class CNF:
    def __init__(self, terms = []):
        self.terms = terms
        self.ops = self.get_ops()
    
    def __repr__(self):
        return "; ".join([term.__repr__() for term in self.terms])

    def copy(self):
        return CNF([term.copy() for term in self.terms])

    def get_ops(self):
        ops = []
        for term in self.terms:
            ops.append(term.get_op())
        return ops

    def append(self, fact):
        self.terms.append(fact)

    def get_terms(self):
        return [term.copy() for term in self.terms]

    def find_term_by_op(self, op):
        for term in self.terms:
            if term.get_op() == op:
                return term.copy()
        return False

    def remove(self, del_term):
        for term in self.terms:
            if (term == del_term):
                self.terms.remove(term)
                return

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
        