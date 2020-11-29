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

  def getFact(self):
    return [fact.copy() for fact in self.facts]
  
  def getRule(self):
    return [rule.copy for rule in self.rules]
