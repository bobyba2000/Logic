from fact import Fact

class Rule:
   def __init__(self, conclusion=Fact(), premises=[]):
      self.conclusion = conclusion        # Inferred fact
      self.premises = premises            # Conditions: list of facts
      self.ops = self.get_ops()           # List of related relations and functions


   def count_premises(self):
      return len(self.premises)

   def get_premises(self):
      return [premise.copy() for premise in self.premises]

   def get_conclusion(self):
      return self.conclusion.copy()

   def copy(self):
      return Rule(self.get_conclusion(), self.get_premises())

   def get_ops(self):
      ops = set()
      for premise in self.premises:
         ops.add(premise.op)
      return ops

   def __repr__(self):
      return self.conclusion.__repr__() + " :- " + ", ".join([premise.__repr__() for premise in self.premises])


   @staticmethod
   def parse(str_rule):  
    # Example: daughter(Person, Parent) :- female(Person), parent(Parent, Person).     
      str_rule = str_rule.strip().rstrip('.').replace(' ', '')
      idx = str_rule.find(':-')

      conclusion = Fact.parse(str_rule[:idx])
      premises = []
      list_fact = str_rule[idx + 2:].split('),')

      for idx, str_fact in enumerate(list_fact):
         if idx != len(list_fact) - 1:
            str_fact += ')'
         fact = Fact.parse(str_fact)
         premises.append(fact)

      return Rule(conclusion, premises)