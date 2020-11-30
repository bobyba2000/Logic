from substitution import Substitution
from rule import Rule
from fact import Fact
from unify import unify
from knowledgebase import KnowledgeBase
import itertools

def fol_fc_ask(kb, alpha):
    res = set()

    while True:
        new_facts = set()

        for rule in KnowledgeBase.getRule():
            count_premises = rule.count_premises()

            facts = kb.getFact()

            premises = itertools.permutations(facts, count_premises)

            for tuple_premises in premises:
                premises_ = [premise for premise in tuple_premises]

                theta = unify(rule.premise, premises_, Substitution())

                if not theta:
                    continue

                new_fact = rule.get_conclusion()
                theta.SUBST(new_fact)

                if new_fact not in new_facts and new_fact not in kb.getFact():
                    new_facts.add(new_fact)
                    phi = unify(new_fact, alpha, Substitution())
                    if phi:
                        if phi.empty():
                            for f in new_facts:
                                kb.appendFact(f)
                            res.add('true')
                            return res
                        res.add(phi)
            if not new_facts:
                if not res:
                    res.add('false')
                return res
            for f in new_facts:
                kb.appendFact(f)
