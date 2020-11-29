class Substitution:
  def __init__(self):
    self.vars = []
    self.vals = []

  def containVar(self, var):
    return var in self.vars

  def containVal(self, val):
    return val in self.vals

  def getValBaseOnVar(self, var):
    for i in range(len(self.vars)):
      if (self.vars[i] == var):
        return self.vals[i]

  def getVarBaseOnVal(self, val):
    for i in range(len(self.vals)):
      if (self.vals[i] == val):
        return self.vars[i]

  def add(self, var, val):
    self.vars.append(var)
    self.vals.append(val)
  def SUBST(self, fact):
    args = fact.get_args()
    for i in range(len(args)):
      if (self.containVar(args[i])):
        fact.args[i] = self.getValBaseOnVar(args[i])
