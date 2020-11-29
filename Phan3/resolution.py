from fact import Fact
from rule import Rule
from cnf import CNF
from knowledgebase import KnowledgeBase
from unify import unify
from substitution import Substitution

def is_suitable(rgoal, clause):
    if len(rgoal.get_terms()) > len(clause.get_terms()):
        return is_suitable(clause, rgoal)
    for goal_term in rgoal.get_terms():
        op = goal_term.get_op()
        suitable_term = clause.find_term_by_op(op)
        if suitable_term == False:
            continue
        elif goal_term.isNegative == suitable_term.isNegative:
            continue
        else:
            theta = Substitution()
            if unify(goal_term, suitable_term, theta) is not False:
                return True
    return False
            
def resolve(rgoal, clause):
    rgoal = rgoal.copy()
    clause = clause.copy()
    if len(rgoal.get_terms()) > len(clause.get_terms()):
        return resolve(clause, rgoal)
    if not is_suitable(rgoal, clause):
        return False
    theta = Substitution()
    for goal_term in rgoal.get_terms():
        op = goal_term.get_op()
        suitable_term = clause.find_term_by_op(op)
        if suitable_term == False:
            continue
        theta = Substitution()
        unify(goal_term, suitable_term, theta)
        clause.remove(suitable_term)
        rgoal.remove(goal_term)
    result = CNF(rgoal.get_terms() + clause.get_terms())
    for term in result.terms:
        theta.SUBST(term)
    return result


def resolution(kb, goal):
    kbCNF = [CNF.parse(fact) for fact in kb.getFacts()]
    kbCNF += [CNF.parse(rule) for rule in kb.getRules()]
    if not isinstance(goal, Fact):
        return
    rgoal = CNF.parse(goal.get_negated())
    kbCNF.append(rgoal)
    while True:
        suitableFound = False
        for term in kbCNF:
            if is_suitable(term, rgoal):
                rgoal = resolve(term, rgoal)
                suitableFound = True
        if len(rgoal.get_terms()) == 0:
            return True
        if not suitableFound: return False
        