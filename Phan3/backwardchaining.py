from fact import Fact
from unify import unify
from unify import unifyVar
from substitution import Substitution
from knowledgebase import KnowledgeBase
from rule import Rule

class BackwardChaining:
  def __init__(self, KB, query, root = True):
    self.KB = KB
    self.query = query
    self.root = root
  
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
      if (self.KB.checkFact(premise) is True):
        continue
      else:
        newQuery = BackwardChaining(self.KB, premise, False)
        if (newQuery.answerTrueFalse() is False):
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
          newQuery = self.query.copy();
          newQuery.args[i] = const
          bc = BackwardChaining(self.KB, newQuery, False)
          ans = bc.answer()
          if (ans is True):
            theta.vars.append(args[i])
            theta.vals.append(const)
            temp.append(theta)
          elif (ans is not False):
            theta.vars.append(args[i])
            theta.vals.append(const)
            for t in ans:
              t = theta.compose(t)
              temp.append(t)
        break

    if (temp == []):
      return False
    return temp
 
  def answer(self):
    if (self.query.haveVariablesInArgs()):
      if (self.root is not True):
        return self.answerList()
      else:
        temp = []
        res = self.answerList()
        if (res is False):
          return False
        for theta in res:
          s = ""
          for i in range(len(theta.vars)):
            s += "{0}: {1}".format(theta.vars[i], theta.vals[i])
            if (i!=len(theta.vars)-1):
              s += ", "
          temp.append(s)
        return temp
    else:
      return self.answerTrueFalse()
