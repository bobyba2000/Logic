from fact import Fact
from rule import Rule

class KnowledgeBase:
  def __init__(self, facts = [], rules = []):
    self.facts = facts
    self.rules = rules

  def appendFact(self, fact):
    self.facts.append(fact)

  def appendRule(self, rule):
    self.rules.append(rule)

  def getFacts(self):
    return [fact.copy() for fact in self.facts]
  
  def getRules(self):
    return [rule.copy() for rule in self.rules]

  def __repr__(self):
    facts_str = "\n".join([fact.__repr__() for fact in self.facts])
    rules_str = "\n".join([rule.__repr__() for rule in self.rules])
    if facts_str and rules_str: join_str = "\n"
    else: join_str = ""
    return join_str.join([facts_str, rules_str])
  
  def getRulePremisesFromConclusionOp(self, op):
    for rule in self.rules:
      if (rule.get_conclusion().get_op() == op):
        return rule.get_premises()
    
  def getRuleConclusionFromConclusionOp(self, op):
    for rule in self.rules:
      if (rule.get_conclusion().get_op() == op):
        return rule.get_conclusion()

  def checkFact(self, fact):
    for f in self.facts:
      if (fact == f):
        return True
    return False

  def getAllConsts(self):
    temp = []
    for fact in self.facts:
      for arg in fact.get_args():
        if (arg not in temp):
          temp.append(arg)
    return temp
  
