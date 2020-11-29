from fact import Fact
from rule import Rule

class KnowledgeBase:
  def __init__(self):
    self.facts = []
    self.rules = []

  def __init__(self, facts, rules):
    self.facts = facts
    self.rules = rules

  def appendFact(self, fact):
    self.facts.append(fact)

  def appendRule(self, rule):
    self.rules.append(rule)

  def getFact(self):
    temp = []
    for fact in self.facts:
      temp.append(fact.copy())
    return temp
  
  def getRule(self):
    temp = []
    for rule in self.rules:
      temp.append(rule.copy())
    return temp
