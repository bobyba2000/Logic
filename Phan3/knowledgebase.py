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
    return [rule.copy() for rule in self.rules]

  def __repr__(self):
    facts_str = "\n".join([fact.__repr__() for fact in self.facts])
    rules_str = "\n".join([rule.__repr__() for rule in self.rules])
    if facts_str and rules_str: join_str = "\n"
    else: join_str = ""
    return join_str.join([facts_str, rules_str])
