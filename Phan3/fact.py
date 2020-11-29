class Fact:
   def __init__(self, op='', args=[], negative=False):
      self.op = op               # Relation or function
      self.args = args           # Varibles and constants
      self.negative = negative   # Not

   def equal(self, other):
      if self.op != other.op:
         return False
      if self.negative != other.negative:
         return False
      return self.args == other.args

   def __eq__(self, other):
      return self.equal(other)

   def negate(self):
      self.negative = 1 - self.negative

   def get_args(self):
      return self.args

   def get_op(self):
      return self.op

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
   def is_fact_in_fact(x):
      return isinstance(x, Fact)

   @staticmethod
   def is_list_of_fact(x):
      return isinstance(x, list)