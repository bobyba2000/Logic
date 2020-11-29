class Fact:
   def __init__(self, op='', args=[], isNegative=False):
      self.op = op               # Relation or function
      self.args = args           # Varibles and constants
      self.isNegative = isNegative   # Not

   def equal(self, other):
      if not isinstance(other, Fact):
         return False
      if self.op != other.op:
         return False
      if self.isNegative != other.isNegative:
         return False
      return self.args == other.args

   def __eq__(self, other):
      return self.equal(other)

   def negate(self):
      self.isNegative = 1 - self.isNegative
   
   def get_negated(self):
      return Fact(self.op, self.args, 1 - self.isNegative)

   def copy(self):
      return Fact(self.get_op(), self.get_args(), self.isNegative)

   def get_args(self):
      return [arg.copy() if not isinstance(arg, str) else arg for arg in self.args]

   def get_op(self):
      return self.op
   
   def haveVariablesInArgs(self):
      for arg in self.args:
        if (is_variable(arg)):
          return True
      return False

   def __repr__(self):
      string = ""
      if len(self.args) > 0: 
         string = self.op + "(" + ", ".join(self.args) + ")"
      else: string = self.op
      if self.isNegative:
         string = "not({})".format(string)
      return string

   @staticmethod
   def parse(str_fact):
      # Example: female(princess_diana).
      str_fact = str_fact.strip().rstrip('.').replace(' ', '')
      idx = str_fact.index('(')

      op = str_fact[:idx]
      args = str_fact[idx + 1 : -1].split(',')
      return Fact(op, args)

   @staticmethod
   def is_variable(x):
      return isinstance(x, str) and x[0].isupper()

   @staticmethod
   def is_fact(x):
      return isinstance(x, Fact)

   @staticmethod
   def is_list(x):
      return isinstance(x, list)
