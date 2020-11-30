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
        suitable_terms = clause.find_term_by_op(op)
        if suitable_terms == False:
            continue
        else: 
            for suitable_term in suitable_terms:
                if goal_term.isNegative == suitable_term.isNegative:
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
        suitable_terms = clause.find_term_by_op(op)
        if suitable_terms == False:
            continue
        for suitable_term in suitable_terms:
            if goal_term.isNegative == suitable_term.isNegative:
                continue
            theta = Substitution()
            unify(goal_term, suitable_term, theta)
            if theta is not False:
                clause.remove(suitable_term)
                rgoal.remove(goal_term)
                break
    result = CNF(rgoal.get_terms() + clause.get_terms())
    for term in result.terms:
        theta.SUBST(term)
    return result


def resolution(kb, goal):
    if goal.isNegative:
        return not resolution(kb, goal.get_negated())
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
                kbCNF.append(rgoal)
                suitableFound = True
        if len(rgoal.get_terms()) == 0:
            return True
        if not suitableFound: return False

def set_variable(var_loc, index, kb, newGoal, consts, theta):
    if index == len(var_loc):
        if resolution(kb, newGoal):
            for i in range(index):
                theta[i].append(newGoal.get_args()[var_loc[i]])
            return True
        else: return False
    hasSuccess = False
    for const in consts:
        newGoal.args[var_loc[index]] = const
        if set_variable(var_loc, index + 1, kb, newGoal, consts, theta):
            hasSuccess = True
    return hasSuccess

def resolution_search(kb, goal): 
    consts = kb.getAllConsts()
    args = goal.get_args()
    var_loc = []
    for i in range(len(args)):
        if Fact.is_variable(args[i]):
            var_loc.append(i)
    if len(var_loc) == 0:
        return resolution(kb, goal)
    theta = [list() for i in range(len(var_loc))]
    newGoal = goal.copy()
    if set_variable(var_loc, 0, kb, newGoal, consts, theta) is not False:
        string = str()
        for i in range(len(theta[0])):
            line = "{"
            for j in range(len(var_loc)):
                line += "{} = {}, ".format(goal.get_args()[var_loc[j]], theta[j][i])
            string += line.rstrip(", ") + "}; "
        return string.rstrip("; ")
    return False

