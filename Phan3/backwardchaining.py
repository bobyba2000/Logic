from fact import Fact
from unify import unify
from unify import unifyVar
from substitution import Substitution
from knowledgebase import KnowledgeBase
from rule import Rule

class BackwardChaining:
  def __init__(self, KB, query):
    self.KB = KB
    self.query = query
  
  def answerTrueFalse(self):
    res = []
    premises = self.KB.getRulePremisesFromConclusionOp(self.query.get_op())
    conclusion = self.KB.getRuleConclusionFromConclusionOp(self.query.get_op())
    if (conclusion == None):
      return self.KB.checkFact(query)
    theta = unify(conclusion, self.query, Substitution())
      
    if (theta == False):
      return False
    for premise in premises:
      theta.SUBST(premise)
      newQuery = BackwardChaining(self.KB, premise)
      if (newQuery.answerTrueFalse is False):
        return False
    return True
  
  def answerList(self):
    temp = []
    consts = self.KB.getAllConsts()
    args = self.query.get_args()
    for i in range(len(args)):
      if (Fact.is_variable(args[i])):
        for const in consts:
          theta = Substitution()
          newQuery = query.copy();
          newQuery.args[i] = const
          bc = BackwardChaining(self.KB, newQuery)
          ans = bc.answer()
          if (ans is True):
            theta.vars.append(args[i])
            theta.vals.append(const)
            temp.append(theta)
          elif (ans is not False):
            temp.append(ans)
    if (temp == []):
      return False
    return temp
